import itertools
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Any, Optional
from src.candidate_scoring import score_group_pair_values
from src.graph import ConnectionsGraph
from src.features import EDGE_FEATURE_DIM, FeatureExtractor
from src.relation_archetypes import (
    NO_RELATION_IDX,
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_TO_IDX,
)
from src.visualize import plot_connections_graph

GROUPWISE_LOSS_MARGIN = 0.05
GROUPWISE_HARD_NEGATIVES = 64
GROUPWISE_LOSS_WEIGHT = 0.5
RELATION_LOSS_WEIGHT = 0.0


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
        # Concatenate node embeddings (out_features * 2) and raw edge features (EDGE_FEATURE_DIM)
        input_dim = out_features * 2 + EDGE_FEATURE_DIM
        self.edge_score_net = nn.Sequential(
            nn.Linear(input_dim, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, 1)
        )
        self.relation_score_net = nn.Sequential(
            nn.Linear(input_dim, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, NUM_RELATION_ARCHETYPES)
        )

        # Precompute all 1820 combinations of 4 out of 16 nodes
        self.combinations = list(itertools.combinations(range(16), 4))
        self.comb_tensor = torch.tensor(self.combinations, dtype=torch.long)

    def _score_edges(self, node_embeddings: torch.Tensor, edge_features: torch.Tensor = None) -> Tuple[torch.Tensor, torch.Tensor]:
        # Expand and concatenate to compute pairwise representations
        h_exp1 = node_embeddings.unsqueeze(1).expand(-1, 16, -1)
        h_exp2 = node_embeddings.unsqueeze(0).expand(16, -1, -1)
        
        if edge_features is not None:
            edge_input = torch.cat([h_exp1, h_exp2, edge_features], dim=-1)
        else:
            dummy_edge = torch.zeros(16, 16, EDGE_FEATURE_DIM, device=node_embeddings.device)
            edge_input = torch.cat([h_exp1, h_exp2, dummy_edge], dim=-1)
        
        # Predict pairwise logits
        edge_logits = self.edge_score_net(edge_input).squeeze(-1) # (16, 16)
        
        # Symmetrize
        edge_logits = (edge_logits + edge_logits.T) / 2.0
        
        # Mask out diagonal (self-loops)
        edge_logits = edge_logits * (1.0 - torch.eye(16, device=edge_logits.device))

        # Predict relation type logits
        relation_logits = self.relation_score_net(edge_input) # (16, 16, num_relation_archetypes)
        # Symmetrize relation logits
        relation_logits = (relation_logits + relation_logits.transpose(0, 1)) / 2.0

        return edge_logits, relation_logits

    def get_candidate_subgraphs(self, edge_probs: torch.Tensor) -> List[Tuple[Tuple[int, ...], float]]:
        """
        Computes the cohesion score for all 1820 4-node combinations.
        Returns candidate subgraphs sorted by cohesion score (descending).
        """
        scores = self.get_candidate_scores_tensor(edge_probs)[1]
        sorted_indices = sorted(
            range(len(self.combinations)),
            key=lambda idx: (-float(scores[idx]), self.combinations[idx]),
        )
        
        candidates = []
        for idx in sorted_indices:
            comb = self.combinations[idx]
            candidates.append((comb, float(scores[idx])))
            
        return candidates

    def get_candidate_scores_tensor(self, edge_probs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Return all 4-node combinations and their cohesion scores as tensors."""
        c = self.comb_tensor.to(edge_probs.device)
        pair_scores = torch.stack(
            [
                edge_probs[c[:, 0], c[:, 1]],
                edge_probs[c[:, 0], c[:, 2]],
                edge_probs[c[:, 0], c[:, 3]],
                edge_probs[c[:, 1], c[:, 2]],
                edge_probs[c[:, 1], c[:, 3]],
                edge_probs[c[:, 2], c[:, 3]],
            ],
            dim=-1,
        )
        scores = score_group_pair_values(pair_scores)
        return c, scores


class ConnectionsGCN(ConnectionsScoringMixin, nn.Module):
    def __init__(
        self,
        in_features: int = 775, # 7 metadata + 768 SentenceTransformer embedding
        hidden_features: int = 32,
        out_features: int = 16,
        num_relations: int = EDGE_FEATURE_DIM,
    ):
        super().__init__()
        # Linear projection to handle high-dimensional semantic node features
        self.input_proj = nn.Linear(in_features, 16)
        self.input_ln = nn.LayerNorm(16)
        self.gcn1 = RelationalGCNLayer(16, hidden_features, num_relations)
        self.ln1 = nn.LayerNorm(hidden_features)
        self.dropout1 = nn.Dropout(p=0.1)
        self.gcn2 = RelationalGCNLayer(hidden_features, out_features, num_relations)
        self.ln2 = nn.LayerNorm(out_features)
        self._init_scoring_heads(hidden_features=hidden_features, out_features=out_features)
        
    def forward(self, h: torch.Tensor, adj: torch.Tensor, edge_features: torch.Tensor = None, return_logits: bool = False) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Args:
            h: Node features (16, in_features)
            adj: Adjacency matrices (num_relations, 16, 16)
            edge_features: Raw pairwise edge features (16, 16, EDGE_FEATURE_DIM)
        Returns:
            node_embeddings: (16, out_features)
            edge_probs: (16, 16) pairwise similarity scores (or logits if return_logits is True)
            relation_logits: (16, 16, num_relation_archetypes) relation type logits
        """
        h_proj = self.input_proj(h)
        h_norm = self.input_ln(h_proj)
        h1 = self.dropout1(F.relu(self.ln1(self.gcn1(h_norm, adj))))
        h2 = self.ln2(self.gcn2(h1, adj)) # (16, out_features)
        edge_logits, relation_logits = self._score_edges(h2, edge_features)
        if return_logits:
            return h2, edge_logits, relation_logits
        return h2, torch.sigmoid(edge_logits), relation_logits


def build_gcn_model(
    in_features: int = 775,
    hidden_features: int = 32,
    out_features: int = 16,
    num_relations: int = EDGE_FEATURE_DIM,
) -> nn.Module:
    return ConnectionsGCN(
        in_features=in_features,
        hidden_features=hidden_features,
        out_features=out_features,
        num_relations=num_relations,
    )

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
            graph.node_features, graph.get_multi_relational_adjacency(), graph.edge_features, return_logits=True
        )
        
        # Weighted BCE Loss with logits (positive pairs are less frequent: 48 out of 240, so weight pos by 4x)
        weight_mask = diag_mask.clone()
        weight_mask[adj_true == 1] *= 4.0
        bce_loss = F.binary_cross_entropy_with_logits(edge_logits, adj_true, weight=weight_mask)
        
        relation_true = build_relation_targets(words, word_to_cat, device)
                    
        class_loss = F.cross_entropy(
            relation_logits.view(-1, NUM_RELATION_ARCHETYPES), 
            relation_true.view(-1), 
            ignore_index=-100
        )
        group_loss = groupwise_ranking_loss(
            model,
            edge_logits,
            words,
            word_to_cat,
            margin=GROUPWISE_LOSS_MARGIN,
            hard_negative_count=GROUPWISE_HARD_NEGATIVES,
        )
        
        # Combined loss
        loss = bce_loss + RELATION_LOSS_WEIGHT * class_loss + GROUPWISE_LOSS_WEIGHT * group_loss
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
                graph.node_features, graph.get_multi_relational_adjacency(), graph.edge_features, return_logits=True
            )
            
            # Compute loss
            weight_mask = diag_mask.clone()
            weight_mask[adj_true == 1] *= 4.0
            bce_loss = F.binary_cross_entropy_with_logits(edge_logits, adj_true, weight=weight_mask)
            
            relation_true = build_relation_targets(words, word_to_cat, device)
                        
            class_loss = F.cross_entropy(
                relation_logits.view(-1, NUM_RELATION_ARCHETYPES), 
                relation_true.view(-1), 
                ignore_index=-100
            )
            group_loss = groupwise_ranking_loss(
                model,
                edge_logits,
                words,
                word_to_cat,
                margin=GROUPWISE_LOSS_MARGIN,
                hard_negative_count=GROUPWISE_HARD_NEGATIVES,
            )
            
            loss = bce_loss + RELATION_LOSS_WEIGHT * class_loss + GROUPWISE_LOSS_WEIGHT * group_loss
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


def build_relation_targets(
    words: List[str],
    word_to_cat: Any,
    device: str,
) -> torch.Tensor:
    """Build relation-archetype labels, including explicit negatives."""
    relation_true = torch.full((16, 16), NO_RELATION_IDX, dtype=torch.long, device=device)
    relation_true.fill_diagonal_(-100)

    for i in range(16):
        for j in range(16):
            if i == j:
                continue
            w_i_cat = _word_category(word_to_cat, words[i])
            w_j_cat = _word_category(word_to_cat, words[j])
            if w_i_cat["cat_idx"] == w_j_cat["cat_idx"]:
                rtype = w_i_cat.get("relation_type", "SYNONYM")
                relation_true[i, j] = RELATION_ARCHETYPE_TO_IDX.get(
                    rtype,
                    RELATION_ARCHETYPE_TO_IDX["SYNONYM"],
                )
    return relation_true


def _word_category(word_to_cat: Any, word: str) -> Any:
    return word_to_cat[word] if isinstance(word_to_cat, dict) else word_to_cat.get(word)


def build_true_group_tensor(
    words: List[str],
    word_to_cat: Any,
    device: str,
) -> torch.Tensor:
    groups = {}
    for idx, word in enumerate(words):
        cat_idx = _word_category(word_to_cat, word)["cat_idx"]
        groups.setdefault(cat_idx, []).append(idx)

    true_groups = [
        sorted(indices)
        for _, indices in sorted(groups.items(), key=lambda item: item[0])
        if len(indices) == 4
    ]
    return torch.tensor(true_groups, dtype=torch.long, device=device)


def groupwise_ranking_loss(
    model: ConnectionsScoringMixin,
    edge_logits: torch.Tensor,
    words: List[str],
    word_to_cat: Any,
    margin: float = GROUPWISE_LOSS_MARGIN,
    hard_negative_count: int = GROUPWISE_HARD_NEGATIVES,
) -> torch.Tensor:
    """Push exact 4-word groups above the highest-scoring false groups using a soft-min score and softplus loss."""
    edge_probs = torch.sigmoid(edge_logits)
    combinations = model.comb_tensor.to(edge_probs.device)
    
    # Compute 6 pairwise scores for all 1820 combinations
    pair_scores = torch.stack(
        [
            edge_probs[combinations[:, 0], combinations[:, 1]],
            edge_probs[combinations[:, 0], combinations[:, 2]],
            edge_probs[combinations[:, 0], combinations[:, 3]],
            edge_probs[combinations[:, 1], combinations[:, 2]],
            edge_probs[combinations[:, 1], combinations[:, 3]],
            edge_probs[combinations[:, 2], combinations[:, 3]],
        ],
        dim=-1,
    )
    
    # Smooth soft-minimum with beta=10.0 (strongly weights lowest values, differentiable, no gradient contradictions)
    beta = 10.0
    scores = - (1.0 / beta) * torch.log(torch.sum(torch.exp(-beta * pair_scores), dim=-1))
    
    true_groups = build_true_group_tensor(words, word_to_cat, edge_logits.device)
    if true_groups.numel() == 0:
        return edge_logits.new_tensor(0.0)

    true_mask = (combinations.unsqueeze(1) == true_groups.unsqueeze(0)).all(dim=2).any(dim=1)
    true_scores = scores[true_mask]
    negative_scores = scores[~true_mask]
    if true_scores.numel() == 0 or negative_scores.numel() == 0:
        return edge_logits.new_tensor(0.0)

    hard_count = min(hard_negative_count, negative_scores.numel())
    hard_negative_scores = torch.topk(negative_scores, k=hard_count).values
    
    # Use squared hinge loss (ReLU squared) so gradients scale down near convergence, and loss is exactly 0 when margin is cleared
    losses = torch.clamp(margin - true_scores.unsqueeze(1) + hard_negative_scores.unsqueeze(0), min=0.0) ** 2
    return losses.mean()
