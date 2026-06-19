import itertools
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Any, Optional
from src.graph import ConnectionsGraph
from src.features import EDGE_FEATURE_DIM, FeatureExtractor
from src.visualize import plot_connections_graph

try:
    from torch_geometric.nn import GINEConv
except ImportError:
    GINEConv = None

class RelationalGCNLayer(nn.Module):
    def __init__(self, in_features: int, out_features: int, num_relations: int):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.num_relations = num_relations
        
        # Self-loop weights
        self.W_self = nn.Linear(in_features, out_features)
        
        # Relational weights
        self.W_rel = nn.Parameter(torch.empty(num_relations, in_features, out_features))
        nn.init.xavier_uniform_(self.W_rel)
        
        self.bias = nn.Parameter(torch.zeros(out_features))
        
    def forward(self, h: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        """
        Args:
            h: Node features tensor of shape (16, in_features)
            adj: Relational adjacency tensor of shape (num_relations, 16, 16)
        """
        # Self contribution
        out = self.W_self(h) # (16, out_features)
        
        # Relational contributions
        # Project h using all relational matrices: (num_relations, 16, out_features)
        h_proj = torch.einsum('ni,rio->rno', h, self.W_rel)
        
        # Multiply by adjacencies: (16, out_features)
        out_rel = torch.einsum('ruv,rvo->uo', adj, h_proj)
        
        return out + out_rel + self.bias

class ConnectionsScoringMixin:
    def _init_scoring_heads(
        self,
        hidden_features: int = 32,
        out_features: int = 16,
    ):
        self.edge_score_net = nn.Sequential(
            nn.Linear(out_features * 2, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, 1)
        )
        self.relation_score_net = nn.Sequential(
            nn.Linear(out_features * 2, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, 5) # 5 categories: SYNONYM, WORDPLAY, PHRASE_COMPLETION, TRIVIA_ENCYCLOPEDIC, MORPHOLOGY
        )

        # Precompute all 1820 combinations of 4 out of 16 nodes
        self.combinations = list(itertools.combinations(range(16), 4))
        self.comb_tensor = torch.tensor(self.combinations, dtype=torch.long)

    def _score_edges(self, node_embeddings: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        # Expand and concatenate to compute pairwise representations
        h_exp1 = node_embeddings.unsqueeze(1).expand(-1, 16, -1)
        h_exp2 = node_embeddings.unsqueeze(0).expand(16, -1, -1)
        edge_input = torch.cat([h_exp1, h_exp2], dim=-1) # (16, 16, out_features * 2)
        
        # Predict pairwise logits
        edge_logits = self.edge_score_net(edge_input).squeeze(-1) # (16, 16)
        
        # Symmetrize
        edge_logits = (edge_logits + edge_logits.T) / 2.0
        
        # Mask out diagonal (self-loops)
        edge_logits = edge_logits * (1.0 - torch.eye(16, device=edge_logits.device))

        # Predict relation type logits
        relation_logits = self.relation_score_net(edge_input) # (16, 16, 5)
        # Symmetrize relation logits
        relation_logits = (relation_logits + relation_logits.transpose(0, 1)) / 2.0

        return edge_logits, relation_logits

    def get_candidate_subgraphs(self, edge_probs: torch.Tensor) -> List[Tuple[Tuple[int, ...], float]]:
        """
        Computes the cohesion score for all 1820 4-node combinations.
        Returns candidate subgraphs sorted by cohesion score (descending).
        """
        device = edge_probs.device
        c = self.comb_tensor.to(device)
        
        # Extract edge probabilities for the 6 pairs in each 4-node combination
        p_01 = edge_probs[c[:, 0], c[:, 1]]
        p_02 = edge_probs[c[:, 0], c[:, 2]]
        p_03 = edge_probs[c[:, 0], c[:, 3]]
        p_12 = edge_probs[c[:, 1], c[:, 2]]
        p_13 = edge_probs[c[:, 1], c[:, 3]]
        p_23 = edge_probs[c[:, 2], c[:, 3]]
        
        # Average probability across all 6 internal edges
        scores = (p_01 + p_02 + p_03 + p_12 + p_13 + p_23) / 6.0 # (1820,)
        
        # Sort scores in descending order
        sorted_indices = torch.argsort(scores, descending=True)
        
        candidates = []
        for idx in sorted_indices.tolist():
            comb = self.combinations[idx]
            candidates.append((comb, float(scores[idx])))
            
        return candidates

    def get_candidate_scores_tensor(self, edge_probs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Return all 4-node combinations and their cohesion scores as tensors."""
        c = self.comb_tensor.to(edge_probs.device)
        scores = (
            edge_probs[c[:, 0], c[:, 1]]
            + edge_probs[c[:, 0], c[:, 2]]
            + edge_probs[c[:, 0], c[:, 3]]
            + edge_probs[c[:, 1], c[:, 2]]
            + edge_probs[c[:, 1], c[:, 3]]
            + edge_probs[c[:, 2], c[:, 3]]
        ) / 6.0
        return c, scores


class ConnectionsGCN(ConnectionsScoringMixin, nn.Module):
    def __init__(
        self,
        in_features: int = 7,
        hidden_features: int = 32,
        out_features: int = 16,
        num_relations: int = EDGE_FEATURE_DIM,
    ):
        super().__init__()
        self.input_ln = nn.LayerNorm(in_features)
        self.gcn1 = RelationalGCNLayer(in_features, hidden_features, num_relations)
        self.ln1 = nn.LayerNorm(hidden_features)
        self.dropout1 = nn.Dropout(p=0.1)
        self.gcn2 = RelationalGCNLayer(hidden_features, out_features, num_relations)
        self.ln2 = nn.LayerNorm(out_features)
        self._init_scoring_heads(hidden_features=hidden_features, out_features=out_features)
        
    def forward(self, h: torch.Tensor, adj: torch.Tensor, return_logits: bool = False) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Args:
            h: Node features (16, in_features)
            adj: Adjacency matrices (num_relations, 16, 16)
        Returns:
            node_embeddings: (16, out_features)
            edge_probs: (16, 16) pairwise similarity scores (or logits if return_logits is True)
            relation_logits: (16, 16, 5) relation type logits
        """
        h_norm = self.input_ln(h)
        h1 = self.dropout1(F.relu(self.ln1(self.gcn1(h_norm, adj))))
        h2 = self.ln2(self.gcn2(h1, adj)) # (16, out_features)
        edge_logits, relation_logits = self._score_edges(h2)
        if return_logits:
            return h2, edge_logits, relation_logits
        return h2, torch.sigmoid(edge_logits), relation_logits


class ConnectionsGINE(ConnectionsScoringMixin, nn.Module):
    def __init__(
        self,
        in_features: int = 7,
        hidden_features: int = 32,
        out_features: int = 16,
        num_relations: int = EDGE_FEATURE_DIM,
    ):
        super().__init__()
        if GINEConv is None:
            raise RuntimeError(
                "torch-geometric is required for --gcn-backbone gine. "
                "Install dependencies with: pip install -r requirements.txt"
            )

        self.num_relations = num_relations
        self.input_ln = nn.LayerNorm(in_features)
        self.gine1 = GINEConv(
            nn.Sequential(
                nn.Linear(in_features, hidden_features),
                nn.ReLU(),
                nn.Linear(hidden_features, hidden_features),
            ),
            edge_dim=num_relations,
        )
        self.ln1 = nn.LayerNorm(hidden_features)
        self.dropout1 = nn.Dropout(p=0.1)
        self.gine2 = GINEConv(
            nn.Sequential(
                nn.Linear(hidden_features, out_features),
                nn.ReLU(),
                nn.Linear(out_features, out_features),
            ),
            edge_dim=num_relations,
        )
        self.ln2 = nn.LayerNorm(out_features)
        self._init_scoring_heads(hidden_features=hidden_features, out_features=out_features)

    def forward(self, h: torch.Tensor, adj: torch.Tensor, return_logits: bool = False) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        edge_index, edge_attr = self._dense_adj_to_pyg(adj)
        h_norm = self.input_ln(h)
        h1 = self.dropout1(F.relu(self.ln1(self.gine1(h_norm, edge_index, edge_attr))))
        h2 = self.ln2(self.gine2(h1, edge_index, edge_attr))
        edge_logits, relation_logits = self._score_edges(h2)
        if return_logits:
            return h2, edge_logits, relation_logits
        return h2, torch.sigmoid(edge_logits), relation_logits

    def _dense_adj_to_pyg(self, adj: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        adj = torch.nan_to_num(adj, nan=0.0, posinf=1.0, neginf=0.0)
        num_nodes = adj.shape[1]
        node_ids = torch.arange(num_nodes, device=adj.device)
        src, dst = torch.meshgrid(node_ids, node_ids, indexing="ij")
        mask = src != dst
        edge_index = torch.stack([src[mask], dst[mask]], dim=0)
        edge_attr = adj.permute(1, 2, 0)[mask]
        return edge_index, edge_attr


def build_gcn_model(
    backbone: str,
    in_features: int = 7,
    hidden_features: int = 32,
    out_features: int = 16,
    num_relations: int = EDGE_FEATURE_DIM,
) -> nn.Module:
    if backbone == "relational":
        return ConnectionsGCN(
            in_features=in_features,
            hidden_features=hidden_features,
            out_features=out_features,
            num_relations=num_relations,
        )
    if backbone == "gine":
        return ConnectionsGINE(
            in_features=in_features,
            hidden_features=hidden_features,
            out_features=out_features,
            num_relations=num_relations,
        )
    raise ValueError(f"Unknown GCN backbone: {backbone}")

def train_gcn_epoch(
    model: ConnectionsGCN, 
    puzzles: list, 
    extractor: FeatureExtractor, 
    optimizer: torch.optim.Optimizer, 
    device: str,
) -> float:
    model.train()
    total_loss = 0.0
    
    # Mask to ignore diagonal elements in loss calculation
    diag_mask = 1.0 - torch.eye(16, device=device)
    
    accum_batch_size = 32
    optimizer.zero_grad()
    
    archetype_to_idx = {
        "SYNONYM": 0,
        "WORDPLAY": 1,
        "PHRASE_COMPLETION": 2,
        "TRIVIA_ENCYCLOPEDIC": 3,
        "MORPHOLOGY": 4
    }
    
    for idx, puzzle in enumerate(puzzles):
        # Support both preprocessed dict format and ConnectionsPuzzle object format
        if isinstance(puzzle, dict):
            graph = ConnectionsGraph(
                puzzle["words"], 
                device=device, 
                node_features=puzzle["node_features"], 
                edge_features=puzzle["edge_features"]
            )
            adj_true = torch.tensor(puzzle["adj"], dtype=torch.float32, device=device)
            words = puzzle["words"]
            word_to_cat = puzzle["word_to_cat"]
        else:
            graph = ConnectionsGraph(puzzle.words, extractor, device=device)
            adj_true = torch.tensor(puzzle.adj, dtype=torch.float32, device=device)
            words = puzzle.words
            word_to_cat = puzzle.word_to_cat
            
        node_embeddings, edge_logits, relation_logits = model(
            graph.node_features, graph.get_multi_relational_adjacency(), return_logits=True
        )
        
        # Weighted BCE Loss with logits (positive pairs are less frequent: 48 out of 240, so weight pos by 4x)
        weight_mask = diag_mask.clone()
        weight_mask[adj_true == 1] *= 4.0
        bce_loss = F.binary_cross_entropy_with_logits(edge_logits, adj_true, weight=weight_mask)
        
        # Ground truth relation indices (-100 for ignore / negative edges)
        relation_true = torch.full((16, 16), -100, dtype=torch.long, device=device)
        for i in range(16):
            for j in range(16):
                if i == j:
                    continue
                w_i = words[i]
                w_j = words[j]
                w_i_cat = word_to_cat[w_i] if isinstance(word_to_cat, dict) else word_to_cat.get(w_i)
                w_j_cat = word_to_cat[w_j] if isinstance(word_to_cat, dict) else word_to_cat.get(w_j)
                if w_i_cat["cat_idx"] == w_j_cat["cat_idx"]:
                    rtype = w_i_cat.get("relation_type", "SYNONYM")
                    relation_true[i, j] = archetype_to_idx.get(rtype, 0)
                    
        class_loss = F.cross_entropy(
            relation_logits.view(-1, 5), 
            relation_true.view(-1), 
            ignore_index=-100
        )
        
        # Combined loss
        loss = bce_loss + 0.5 * class_loss
        scaled_loss = loss / accum_batch_size
        scaled_loss.backward()
        
        total_loss += loss.item()
        
        # Update weights at accumulation boundaries
        if (idx + 1) % accum_batch_size == 0 or (idx + 1) == len(puzzles):
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            optimizer.zero_grad()
            
    return total_loss / len(puzzles)

def validate_gcn(
    model: ConnectionsGCN, 
    puzzles: list, 
    extractor: FeatureExtractor, 
    device: str,
    visualize: bool = False,
    filepath: Optional[str] = None,
    visualize_idx: int = 0,
) -> Tuple[float, float]:
    """
    Validates GCN. Computes mean BCE loss and Mean Reciprocal Rank (MRR) of correct 4-node categories.
    Also visualizes a chosen puzzle index to show model clustering updates.
    """
    model.eval()
    total_loss = 0.0
    mrr_sum = 0.0
    diag_mask = 1.0 - torch.eye(16, device=device)
    
    archetype_to_idx = {
        "SYNONYM": 0,
        "WORDPLAY": 1,
        "PHRASE_COMPLETION": 2,
        "TRIVIA_ENCYCLOPEDIC": 3,
        "MORPHOLOGY": 4
    }
    
    with torch.no_grad():
        for idx, puzzle in enumerate(puzzles):
            if isinstance(puzzle, dict):
                graph = ConnectionsGraph(
                    puzzle["words"], 
                    device=device, 
                    node_features=puzzle["node_features"], 
                    edge_features=puzzle["edge_features"]
                )
                adj_true = torch.tensor(puzzle["adj"], dtype=torch.float32, device=device)
                words = puzzle["words"]
                word_to_cat = puzzle["word_to_cat"]
                puzzle_id = puzzle["id"]
            else:
                graph = ConnectionsGraph(puzzle.words, extractor, device=device)
                adj_true = torch.tensor(puzzle.adj, dtype=torch.float32, device=device)
                words = puzzle.words
                word_to_cat = puzzle.word_to_cat
                puzzle_id = puzzle.id
            
            node_embeddings, edge_logits, relation_logits = model(
                graph.node_features, graph.get_multi_relational_adjacency(), return_logits=True
            )
            
            # Compute loss
            weight_mask = diag_mask.clone()
            weight_mask[adj_true == 1] *= 4.0
            bce_loss = F.binary_cross_entropy_with_logits(edge_logits, adj_true, weight=weight_mask)
            
            relation_true = torch.full((16, 16), -100, dtype=torch.long, device=device)
            for i in range(16):
                for j in range(16):
                    if i == j:
                        continue
                    w_i = words[i]
                    w_j = words[j]
                    w_i_cat = word_to_cat[w_i] if isinstance(word_to_cat, dict) else word_to_cat.get(w_i)
                    w_j_cat = word_to_cat[w_j] if isinstance(word_to_cat, dict) else word_to_cat.get(w_j)
                    if w_i_cat["cat_idx"] == w_j_cat["cat_idx"]:
                        rtype = w_i_cat.get("relation_type", "SYNONYM")
                        relation_true[i, j] = archetype_to_idx.get(rtype, 0)
                        
            class_loss = F.cross_entropy(
                relation_logits.view(-1, 5), 
                relation_true.view(-1), 
                ignore_index=-100
            )
            
            loss = bce_loss + 0.5 * class_loss
            total_loss += loss.item()
            
            edge_probs = torch.sigmoid(edge_logits)
            c, scores = model.get_candidate_scores_tensor(edge_probs)
            
            # 2. Find rank of each of the 4 true categories
            ranks = []
            for cat_idx in range(4):
                indices = []
                for i, w in enumerate(words):
                    if word_to_cat[w]["cat_idx"] == cat_idx:
                        indices.append(i)
                tc = torch.tensor(sorted(indices), dtype=torch.long, device=device)
                match_mask = (c == tc).all(dim=1)
                true_score = scores[match_mask][0]
                rank = int(torch.sum(scores >= true_score).item())
                ranks.append(rank)
            
            mrr_sum += sum(1.0 / r for r in ranks) / 4.0
            
            # Save visual progress for the requested puzzle index if requested
            if idx == visualize_idx and visualize and filepath is not None:
                # Convert edge probabilities to numpy
                edge_probs_np = edge_probs.cpu().numpy()
                true_cats = [word_to_cat[w]["cat_idx"] for w in words]
                
                # Save plot
                plot_connections_graph(
                    words, 
                    edge_probs_np, 
                    true_categories=true_cats, 
                    threshold=0.45, 
                    filepath=filepath,
                    title=f"GCN Edge Predictions - Puzzle {puzzle_id}"
                )
                
    return total_loss / len(puzzles), mrr_sum / len(puzzles)


def _puzzle_value(puzzle: Any, field: str):
    return puzzle[field] if isinstance(puzzle, dict) else getattr(puzzle, field)
