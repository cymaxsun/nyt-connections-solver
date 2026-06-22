import itertools
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import List, Tuple, Any, Optional
from src.candidate_scoring import score_group_pair_values
from src.graph import ConnectionsGraph
from src.features import (
    DEFAULT_NODE_FEATURE_DIM,
    EDGE_FEATURE_DIM,
    FeatureExtractor,
    NODE_METADATA_DIM,
)
from src.relation_archetypes import (
    NO_RELATION_IDX,
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_TO_IDX,
    normalize_relation_archetype,
)
from src.visualize import plot_connections_graph

GROUPWISE_LOSS_MARGIN = 0.05
GROUPWISE_HARD_NEGATIVES = 64
GROUPWISE_LOSS_WEIGHT = 0.5
RELATION_LOSS_WEIGHT = 0.25
GROUP_RELATION_LOSS_WEIGHT = 0.50
GROUP_RELATION_HARD_NEGATIVES = 64
GROUP_ARCHETYPE_SCORE_WEIGHT = 0.05
GROUP_ARCHETYPE_POSITIVE_GATE = 0.40
GROUP_ARCHETYPE_MARGIN_GATE = 0.05
NEAR_MISS_HARD_NEGATIVE_BONUS = 0.10
NEAR_MISS_GROUP_LOSS_WEIGHT = 2.0


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
            h: Node features tensor of shape (batch_size, 16, in_features) or (16, in_features)
            adj: Relational adjacency tensor of shape (batch_size, num_relations, 16, 16) or (num_relations, 16, 16)
        """
        W_rel_flat = self.W_rel.permute(1, 0, 2).reshape(self.in_features, -1)

        if len(h.shape) == 3:
            # Batched case
            batch_size = h.shape[0]
            out = self.W_self(h)  # (batch_size, 16, out_features)

            # Project h: (batch_size * 16, num_relations * out_features)
            res = torch.matmul(h.view(-1, self.in_features), W_rel_flat)
            h_proj = res.view(batch_size, 16, self.num_relations, self.out_features).permute(0, 2, 1, 3)

            # Multiply by adjacencies:
            out_rel = torch.matmul(adj, h_proj).sum(dim=1)  # (batch_size, 16, out_features)

            return out + out_rel + self.bias
        else:
            # Unbatched case
            out = self.W_self(h) # (16, out_features)

            # Project h: (16, num_relations * out_features)
            res = torch.matmul(h, W_rel_flat)
            h_proj = res.view(16, self.num_relations, self.out_features).permute(1, 0, 2)

            # Multiply by adjacencies:
            out_rel = torch.matmul(adj, h_proj).sum(dim=0)  # (16, out_features)

            return out + out_rel + self.bias


class ConnectionsScoringMixin:
    def _init_scoring_heads(
        self,
        hidden_features: int = 32,
        out_features: int = 16,
        num_relations: int = EDGE_FEATURE_DIM,
    ):
        self.num_relations_for_scoring = num_relations
        # Concatenate node embeddings (out_features * 2) and raw edge features (num_relations)
        input_dim = out_features * 2 + num_relations
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
        group_input_dim = out_features * 2 + num_relations * 2
        self.group_relation_score_net = nn.Sequential(
            nn.Linear(group_input_dim, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, NUM_RELATION_ARCHETYPES),
        )

        # Precompute all 1820 combinations of 4 out of 16 nodes
        self.combinations = list(itertools.combinations(range(16), 4))
        self.comb_tensor = torch.tensor(self.combinations, dtype=torch.long)

    def _score_edges(self, node_embeddings: torch.Tensor, edge_features: torch.Tensor = None) -> Tuple[torch.Tensor, torch.Tensor]:
        is_batched = len(node_embeddings.shape) == 3
        if is_batched:
            batch_size = node_embeddings.shape[0]
            # Expand and concatenate to compute pairwise representations
            h_exp1 = node_embeddings.unsqueeze(2).expand(-1, -1, 16, -1)
            h_exp2 = node_embeddings.unsqueeze(1).expand(-1, 16, -1, -1)
            
            if edge_features is not None:
                edge_input = torch.cat([h_exp1, h_exp2, edge_features], dim=-1)
            else:
                dummy_edge = torch.zeros(batch_size, 16, 16, self.num_relations_for_scoring, device=node_embeddings.device)
                edge_input = torch.cat([h_exp1, h_exp2, dummy_edge], dim=-1)
        else:
            # Expand and concatenate to compute pairwise representations
            h_exp1 = node_embeddings.unsqueeze(1).expand(-1, 16, -1)
            h_exp2 = node_embeddings.unsqueeze(0).expand(16, -1, -1)
            
            if edge_features is not None:
                edge_input = torch.cat([h_exp1, h_exp2, edge_features], dim=-1)
            else:
                dummy_edge = torch.zeros(16, 16, self.num_relations_for_scoring, device=node_embeddings.device)
                edge_input = torch.cat([h_exp1, h_exp2, dummy_edge], dim=-1)
        
        # Predict pairwise logits
        edge_logits = self.edge_score_net(edge_input).squeeze(-1) # (batch_size, 16, 16) or (16, 16)
        
        # Symmetrize
        edge_logits = (edge_logits + edge_logits.transpose(-1, -2)) / 2.0
        
        # Mask out diagonal (self-loops)
        edge_logits = edge_logits * (1.0 - torch.eye(16, device=edge_logits.device))

        # Predict relation type logits
        relation_logits = self.relation_score_net(edge_input) # (batch_size, 16, 16, num_relation_archetypes) or (16, 16, num_relation_archetypes)
        # Symmetrize relation logits
        relation_logits = (relation_logits + relation_logits.transpose(-2, -3)) / 2.0

        return edge_logits, relation_logits

    def _score_group_relations(
        self,
        node_embeddings: torch.Tensor,
        edge_features: torch.Tensor = None,
    ) -> torch.Tensor:
        is_batched = len(node_embeddings.shape) == 3
        c = self.comb_tensor.to(node_embeddings.device)
        
        if is_batched:
            group_nodes = node_embeddings[:, c]  # (batch_size, 1820, 4, out_features)
        else:
            group_nodes = node_embeddings[c]  # (1820, 4, out_features)
            
        node_summary = torch.cat(
            [
                group_nodes.mean(dim=-2),
                group_nodes.max(dim=-2).values,
            ],
            dim=-1,
        )

        if edge_features is not None:
            pair_features = _candidate_pair_values(edge_features, c)
            edge_summary = torch.cat(
                [
                    pair_features.mean(dim=-2),
                    pair_features.max(dim=-2).values,
                ],
                dim=-1,
            )
        else:
            if is_batched:
                edge_summary = torch.zeros(
                    node_embeddings.shape[0],
                    c.shape[0],
                    self.num_relations_for_scoring * 2,
                    dtype=node_embeddings.dtype,
                    device=node_embeddings.device,
                )
            else:
                edge_summary = torch.zeros(
                    c.shape[0],
                    self.num_relations_for_scoring * 2,
                    dtype=node_embeddings.dtype,
                    device=node_embeddings.device,
                )

        group_input = torch.cat([node_summary, edge_summary], dim=-1)
        return self.group_relation_score_net(group_input)

    def get_candidate_subgraphs(
        self,
        edge_probs: torch.Tensor,
        group_relation_logits: torch.Tensor = None,
    ) -> List[Tuple[Tuple[int, ...], float]]:
        """
        Computes the cohesion score for all 1820 4-node combinations.
        Returns candidate subgraphs sorted by cohesion score (descending).
        """
        scores = self.get_candidate_scores_tensor(edge_probs, group_relation_logits)[1]
        sorted_indices = sorted(
            range(len(self.combinations)),
            key=lambda idx: (-float(scores[idx]), self.combinations[idx]),
        )

        candidates = []
        for idx in sorted_indices:
            comb = self.combinations[idx]
            candidates.append((comb, float(scores[idx])))

        return candidates

    def get_candidate_scores_tensor(
        self,
        edge_probs: torch.Tensor,
        group_relation_logits: torch.Tensor = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Return all 4-node combinations and their cohesion scores as tensors."""
        c = self.comb_tensor.to(edge_probs.device)
        is_batched = len(edge_probs.shape) == 3
        pair_scores = _candidate_pair_values(edge_probs, c)
        scores = score_group_pair_values(pair_scores)
        if group_relation_logits is not None:
            group_probs = torch.softmax(group_relation_logits, dim=-1)
            positive_confidence = group_probs[..., 1:].max(dim=-1).values
            no_relation_confidence = group_probs[..., NO_RELATION_IDX]
            # Only boost if the prediction clears the archetype classification gate
            gate = (
                (positive_confidence >= GROUP_ARCHETYPE_POSITIVE_GATE)
                & ((positive_confidence - no_relation_confidence) >= GROUP_ARCHETYPE_MARGIN_GATE)
            )
            archetype_boost = torch.where(
                gate,
                positive_confidence - no_relation_confidence,
                torch.zeros_like(positive_confidence),
            )
            scores = torch.clamp(
                scores + getattr(self, "group_archetype_score_weight", GROUP_ARCHETYPE_SCORE_WEIGHT) * archetype_boost,
                min=0.0,
                max=1.0,
            )
        return c, scores


class ConnectionsGCN(ConnectionsScoringMixin, nn.Module):
    def __init__(
        self,
        in_features: int = DEFAULT_NODE_FEATURE_DIM,
        hidden_features: int = 128,
        out_features: int = 16,
        num_relations: int = EDGE_FEATURE_DIM,
        group_archetype_score_weight: float = GROUP_ARCHETYPE_SCORE_WEIGHT,
    ):
        super().__init__()
        self.group_archetype_score_weight = group_archetype_score_weight
        # Linear projection to handle high-dimensional semantic node features
        self.input_proj = nn.Linear(in_features, 16)
        self.input_ln = nn.LayerNorm(16)
        self.gcn1 = RelationalGCNLayer(16, hidden_features, num_relations)
        self.ln1 = nn.LayerNorm(hidden_features)
        self.dropout1 = nn.Dropout(p=0.1)
        self.gcn2 = RelationalGCNLayer(hidden_features, out_features, num_relations)
        self.ln2 = nn.LayerNorm(out_features)
        self._init_scoring_heads(hidden_features=hidden_features, out_features=out_features, num_relations=num_relations)

    def forward(
        self,
        h: torch.Tensor,
        adj: torch.Tensor,
        edge_features: torch.Tensor = None,
        return_logits: bool = False,
        return_group_logits: bool = False,
    ):
        """
        Args:
            h: Node features (16, in_features)
            adj: Adjacency matrices (num_relations, 16, 16)
            edge_features: Raw pairwise edge features (16, 16, EDGE_FEATURE_DIM)
        Returns:
            node_embeddings: (16, out_features)
            edge_probs: (16, 16) pairwise similarity scores (or logits if return_logits is True)
            relation_logits: (16, 16, num_relation_archetypes) relation type logits
            group_relation_logits: Optional (1820, num_relation_archetypes) quartet relation logits
        """
        h_proj = self.input_proj(h)
        h_norm = self.input_ln(h_proj)
        h1 = self.dropout1(F.relu(self.ln1(self.gcn1(h_norm, adj))))
        h2 = self.ln2(self.gcn2(h1, adj)) # (16, out_features)
        edge_logits, relation_logits = self._score_edges(h2, edge_features)
        group_relation_logits = self._score_group_relations(h2, edge_features)
        if return_logits:
            if return_group_logits:
                return h2, edge_logits, relation_logits, group_relation_logits
            return h2, edge_logits, relation_logits
        edge_probs = torch.sigmoid(edge_logits)
        if return_group_logits:
            return h2, edge_probs, relation_logits, group_relation_logits
        return h2, edge_probs, relation_logits


class SliceRelationsGCN(nn.Module):
    def __init__(self, original_model, num_relations, in_features, hidden_features):
        super().__init__()
        self.original_model = original_model
        self.num_relations = num_relations
        self.in_features = in_features
        self.out_features = 16
        self.hidden_features = hidden_features
        
    def get_candidate_subgraphs(self, edge_probs, group_relation_logits=None):
        return self.original_model.get_candidate_subgraphs(edge_probs, group_relation_logits)
        
    def forward(self, node_features, adjacency, edge_features, return_group_logits=False):
        # Slice adjacency to [num_relations, 16, 16]
        sliced_adjacency = adjacency[:self.num_relations]
        # Slice edge_features to [num_edges, num_relations]
        sliced_edge_features = edge_features[..., :self.num_relations]
        return self.original_model(
            node_features,
            sliced_adjacency,
            sliced_edge_features,
            return_group_logits=return_group_logits
        )
        
    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(self.original_model, name)


def build_gcn_model(
    in_features: int = DEFAULT_NODE_FEATURE_DIM,
    hidden_features: int = 128,
    out_features: int = 16,
    num_relations: int = EDGE_FEATURE_DIM,
) -> nn.Module:
    return ConnectionsGCN(
        in_features=in_features,
        hidden_features=hidden_features,
        out_features=out_features,
        num_relations=num_relations,
    )

def _ensure_precomputed_puzzle_fields(puzzle: Any, comb_tensor: torch.Tensor):
    """Precompute static targets and multi-relational adjacency matrix on CPU to optimize training."""
    if isinstance(puzzle, dict):
        if "relation_targets" in puzzle and "true_group_mask" in puzzle and "static_group_targets" in puzzle and "adj_multi" in puzzle:
            return
        words = puzzle["words"]
        word_to_cat = puzzle["word_to_cat"]
        node_features = puzzle["node_features"]
        edge_features = puzzle["edge_features"]
    else:
        if hasattr(puzzle, "relation_targets") and hasattr(puzzle, "true_group_mask") and hasattr(puzzle, "static_group_targets") and hasattr(puzzle, "adj_multi"):
            return
        words = puzzle.words
        word_to_cat = puzzle.word_to_cat
        node_features = puzzle.node_features
        edge_features = puzzle.edge_features

    # Ensure node/edge features are torch CPU tensors
    if isinstance(node_features, np.ndarray):
        node_features = torch.tensor(node_features, dtype=torch.float32)
    else:
        node_features = torch.as_tensor(node_features, dtype=torch.float32).cpu()
        
    if isinstance(edge_features, np.ndarray):
        edge_features = torch.tensor(edge_features, dtype=torch.float32)
    else:
        edge_features = torch.as_tensor(edge_features, dtype=torch.float32).cpu()

    # Precompute static targets on CPU
    relation_targets = build_relation_targets(words, word_to_cat, device="cpu")
    true_groups = build_true_group_tensor(words, word_to_cat, device="cpu")
    true_mask = (comb_tensor.unsqueeze(1) == true_groups.unsqueeze(0)).all(dim=2).any(dim=1)
    
    targets = torch.full((comb_tensor.shape[0],), -100, dtype=torch.long)
    for true_group in true_groups:
        group_idx = int((comb_tensor == true_group).all(dim=1).nonzero(as_tuple=False)[0].item())
        first_word = words[int(true_group[0].item())]
        rtype = normalize_relation_archetype(
            _word_category(word_to_cat, first_word).get("relation_type", "SYNONYM_OR_NEAR")
        )
        targets[group_idx] = RELATION_ARCHETYPE_TO_IDX[rtype]
        
    graph_cpu = ConnectionsGraph(
        words,
        device="cpu",
        node_features=node_features,
        edge_features=edge_features
    )
    adj_multi = graph_cpu.get_multi_relational_adjacency()
    
    if isinstance(puzzle, dict):
        puzzle["node_features"] = node_features
        puzzle["edge_features"] = edge_features
        puzzle["relation_targets"] = relation_targets
        puzzle["true_group_mask"] = true_mask
        puzzle["static_group_targets"] = targets
        puzzle["adj_multi"] = adj_multi
    else:
        puzzle.node_features = node_features
        puzzle.edge_features = edge_features
        puzzle.relation_targets = relation_targets
        puzzle.true_group_mask = true_mask
        puzzle.static_group_targets = targets
        puzzle.adj_multi = adj_multi


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
    relation_class_weights = build_relation_class_weights(puzzles, device)
    group_class_weights = build_group_class_weights(puzzles, device, GROUP_RELATION_HARD_NEGATIVES)

    batch_size = 32
    optimizer.zero_grad()

    # Ensure puzzles have precomputed fields
    comb_tensor = model.comb_tensor
    for p in puzzles:
        _ensure_precomputed_puzzle_fields(p, comb_tensor)

    for start_idx in range(0, len(puzzles), batch_size):
        batch_puzzles = puzzles[start_idx : start_idx + batch_size]
        actual_batch_size = len(batch_puzzles)
        
        # Stack CPU tensors
        node_features_cpu = torch.stack([p["node_features"] for p in batch_puzzles])
        edge_features_cpu = torch.stack([p["edge_features"] for p in batch_puzzles])
        adj_multi_cpu = torch.stack([p["adj_multi"] for p in batch_puzzles])
        
        adj_true_cpu = torch.stack([
            torch.tensor(p["adj"], dtype=torch.float32) if isinstance(p, dict) else torch.tensor(p.adj, dtype=torch.float32)
            for p in batch_puzzles
        ])
        
        relation_targets_cpu = torch.stack([p["relation_targets"] for p in batch_puzzles])
        static_group_targets_cpu = torch.stack([p["static_group_targets"] for p in batch_puzzles])
        true_group_mask_cpu = torch.stack([p["true_group_mask"] for p in batch_puzzles])
        
        # Single device transfer for stacked tensors
        node_features = node_features_cpu.to(device)
        edge_features = edge_features_cpu.to(device)
        adj_multi = adj_multi_cpu.to(device)
        adj_true = adj_true_cpu.to(device)
        
        relation_targets = relation_targets_cpu.to(device)
        static_group_targets = static_group_targets_cpu.to(device)
        true_group_mask = true_group_mask_cpu.to(device)
        
        adj_multi = drop_edges(adj_multi, p=0.2, training=True)
        
        node_embeddings, edge_logits, relation_logits, group_relation_logits = model(
            node_features,
            adj_multi,
            edge_features,
            return_logits=True,
            return_group_logits=True,
        )

        batch_losses = []
        for i in range(actual_batch_size):
            # BCE Loss
            weight_mask = diag_mask.clone()
            weight_mask[adj_true[i] == 1] *= 4.0
            bce_loss_i = F.binary_cross_entropy_with_logits(edge_logits[i], adj_true[i], weight=weight_mask)

            # Relation Class Loss
            class_loss_i = focal_loss(
                relation_logits[i].view(-1, NUM_RELATION_ARCHETYPES),
                relation_targets[i].view(-1),
                gamma=2.0,
                alpha=relation_class_weights,
                ignore_index=-100,
            )
            
            # Group Relation Loss
            targets_i = static_group_targets[i].clone()
            edge_probs_i = torch.sigmoid(edge_logits[i])
            _, scores_i = model.get_candidate_scores_tensor(edge_probs_i)
            true_mask_i = true_group_mask[i]
            negative_indices = torch.nonzero(~true_mask_i, as_tuple=False).flatten()
            if negative_indices.numel() > 0:
                negative_scores = scores_i[negative_indices]
                top_k = min(GROUP_RELATION_HARD_NEGATIVES, negative_indices.numel())
                hard_negative_indices = negative_indices[torch.topk(negative_scores, k=top_k).indices]
                targets_i[hard_negative_indices] = NO_RELATION_IDX
                
            group_class_loss_i = _focal_loss_with_optional_targets(
                group_relation_logits[i],
                targets_i,
                gamma=2.0,
                alpha=group_class_weights,
            )
            
            combinations = model.comb_tensor.to(device)
            scores = score_group_pair_values(_candidate_pair_values(edge_probs_i, combinations))
            group_loss_i = _groupwise_margin_loss_from_scores(
                scores,
                combinations,
                true_mask_i,
                margin=GROUPWISE_LOSS_MARGIN,
                hard_negative_count=GROUPWISE_HARD_NEGATIVES,
            )

            loss_i = (
                bce_loss_i
                + RELATION_LOSS_WEIGHT * class_loss_i
                + GROUP_RELATION_LOSS_WEIGHT * group_class_loss_i
                + GROUPWISE_LOSS_WEIGHT * group_loss_i
            )
            batch_losses.append(loss_i)

        batch_loss = torch.stack(batch_losses).mean()
        batch_loss.backward()
        
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        optimizer.zero_grad()

        total_loss += batch_loss.item() * actual_batch_size

    return total_loss / len(puzzles)


def validate_gcn(
    model: ConnectionsGCN,
    puzzles: list,
    extractor: FeatureExtractor,
    device: str,
    visualize: bool = False,
    filepath: Optional[str] = None,
    visualize_idx: int = 0,
    epoch: Optional[int] = None,
) -> Tuple[float, float]:
    """
    Validates GCN. Computes mean BCE loss and Mean Reciprocal Rank (MRR) of correct 4-node categories.
    Also visualizes a chosen puzzle index to show model clustering updates.
    """
    model.eval()
    total_loss = 0.0
    mrr_sum = 0.0
    total_cos_sim = 0.0
    diag_mask = 1.0 - torch.eye(16, device=device)
    
    relation_class_weights = build_relation_class_weights(puzzles, device)
    group_class_weights = build_group_class_weights(puzzles, device, GROUP_RELATION_HARD_NEGATIVES)
    
    batch_size = 32
    
    comb_tensor = model.comb_tensor
    for p in puzzles:
        _ensure_precomputed_puzzle_fields(p, comb_tensor)

    with torch.no_grad():
        for start_idx in range(0, len(puzzles), batch_size):
            batch_puzzles = puzzles[start_idx : start_idx + batch_size]
            actual_batch_size = len(batch_puzzles)
            
            node_features_cpu = torch.stack([p["node_features"] for p in batch_puzzles])
            edge_features_cpu = torch.stack([p["edge_features"] for p in batch_puzzles])
            adj_multi_cpu = torch.stack([p["adj_multi"] for p in batch_puzzles])
            adj_true_cpu = torch.stack([
                torch.tensor(p["adj"], dtype=torch.float32) if isinstance(p, dict) else torch.tensor(p.adj, dtype=torch.float32)
                for p in batch_puzzles
            ])
            
            relation_targets_cpu = torch.stack([p["relation_targets"] for p in batch_puzzles])
            static_group_targets_cpu = torch.stack([p["static_group_targets"] for p in batch_puzzles])
            true_group_mask_cpu = torch.stack([p["true_group_mask"] for p in batch_puzzles])
            
            # Single device transfer
            node_features = node_features_cpu.to(device)
            edge_features = edge_features_cpu.to(device)
            adj_multi = adj_multi_cpu.to(device)
            adj_true = adj_true_cpu.to(device)
            
            relation_targets = relation_targets_cpu.to(device)
            static_group_targets = static_group_targets_cpu.to(device)
            true_group_mask = true_group_mask_cpu.to(device)
            
            node_embeddings, edge_logits, relation_logits, group_relation_logits = model(
                node_features,
                adj_multi,
                edge_features,
                return_logits=True,
                return_group_logits=True,
            )
            
            for i in range(actual_batch_size):
                idx = start_idx + i
                puzzle = batch_puzzles[i]
                words = puzzle["words"] if isinstance(puzzle, dict) else puzzle.words
                word_to_cat = puzzle["word_to_cat"] if isinstance(puzzle, dict) else puzzle.word_to_cat
                puzzle_id = puzzle["id"] if isinstance(puzzle, dict) else puzzle.id
                
                # Compute Mean Pairwise Cosine Similarity of node embeddings
                norm_embeddings = F.normalize(node_embeddings[i], p=2, dim=-1)
                cos_sim_matrix = torch.mm(norm_embeddings, norm_embeddings.t())
                triu_indices = torch.triu_indices(16, 16, offset=1)
                puzzle_cos_sim = cos_sim_matrix[triu_indices[0], triu_indices[1]].mean().item()
                total_cos_sim += puzzle_cos_sim
                
                # Compute loss
                weight_mask = diag_mask.clone()
                weight_mask[adj_true[i] == 1] *= 4.0
                bce_loss = F.binary_cross_entropy_with_logits(edge_logits[i], adj_true[i], weight=weight_mask)
                
                class_loss = focal_loss(
                    relation_logits[i].view(-1, NUM_RELATION_ARCHETYPES),
                    relation_targets[i].view(-1),
                    gamma=2.0,
                    alpha=relation_class_weights,
                    ignore_index=-100,
                )
                
                targets_i = static_group_targets[i].clone()
                edge_probs_i = torch.sigmoid(edge_logits[i])
                _, scores_i = model.get_candidate_scores_tensor(edge_probs_i)
                true_mask_i = true_group_mask[i]
                negative_indices = torch.nonzero(~true_mask_i, as_tuple=False).flatten()
                if negative_indices.numel() > 0:
                    negative_scores = scores_i[negative_indices]
                    top_k = min(GROUP_RELATION_HARD_NEGATIVES, negative_indices.numel())
                    hard_negative_indices = negative_indices[torch.topk(negative_scores, k=top_k).indices]
                    targets_i[hard_negative_indices] = NO_RELATION_IDX
                    
                group_class_loss = _focal_loss_with_optional_targets(
                    group_relation_logits[i],
                    targets_i,
                    gamma=2.0,
                    alpha=group_class_weights,
                )
                
                combinations = model.comb_tensor.to(device)
                scores = score_group_pair_values(_candidate_pair_values(edge_probs_i, combinations))
                group_loss = _groupwise_margin_loss_from_scores(
                    scores,
                    combinations,
                    true_mask_i,
                    margin=GROUPWISE_LOSS_MARGIN,
                    hard_negative_count=GROUPWISE_HARD_NEGATIVES,
                )
                    
                loss = (
                    bce_loss
                    + RELATION_LOSS_WEIGHT * class_loss
                    + GROUP_RELATION_LOSS_WEIGHT * group_class_loss
                    + GROUPWISE_LOSS_WEIGHT * group_loss
                )
                total_loss += loss.item()
                
                # Find rank of each of the 4 true categories
                ranks = []
                for cat_idx in range(4):
                    indices = []
                    for w_idx, w in enumerate(words):
                        if _word_category(word_to_cat, w)["cat_idx"] == cat_idx:
                            indices.append(w_idx)
                    tc = torch.tensor(sorted(indices), dtype=torch.long, device=device)
                    match_mask = (combinations == tc).all(dim=1)
                    true_score = scores_i[match_mask][0]
                    rank = int(torch.sum(scores_i >= true_score).item())
                    ranks.append(rank)
                    
                mrr_sum += sum(1.0 / r for r in ranks) / 4.0
                
                # Save visual progress for the requested puzzle index if requested
                if idx == visualize_idx and visualize and filepath is not None:
                    edge_probs_np = edge_probs_i.cpu().numpy()
                    true_cats = [word_to_cat[w]["cat_idx"] for w in words]
                    plot_connections_graph(
                        words,
                        edge_probs_np,
                        true_categories=true_cats,
                        threshold=0.45,
                        filepath=filepath,
                        title=f"GCN Edge Predictions - Puzzle {puzzle_id}"
                    )
                    
    avg_cos_sim = total_cos_sim / len(puzzles)
    if epoch is not None:
        try:
            import mlflow
            if mlflow.active_run():
                mlflow.log_metric("val_mean_node_cosine_similarity", avg_cos_sim, step=epoch)
        except Exception as e:
            print(f"Warning: Failed to log mean cosine similarity to MLflow: {e}")
            
    return total_loss / len(puzzles), mrr_sum / len(puzzles)


def _puzzle_value(puzzle: Any, field: str):
    return puzzle[field] if isinstance(puzzle, dict) else getattr(puzzle, field)


def _cross_entropy_with_optional_targets(
    logits: torch.Tensor,
    targets: torch.Tensor,
    weight: torch.Tensor = None,
) -> torch.Tensor:
    if not torch.any(targets != -100):
        return logits.sum() * 0.0
    return F.cross_entropy(logits, targets, ignore_index=-100, weight=weight)


def focal_loss(
    logits: torch.Tensor,
    targets: torch.Tensor,
    gamma: float = 2.0,
    alpha: Optional[torch.Tensor] = None,
    ignore_index: int = -100,
) -> torch.Tensor:
    """
    Computes multiclass focal loss:
    FL = -alpha * (1 - p_t)^gamma * log(p_t)
    """
    valid_mask = (targets != ignore_index)
    if not valid_mask.any():
        return logits.sum() * 0.0

    logits = logits[valid_mask]
    targets = targets[valid_mask]

    log_p = F.log_softmax(logits, dim=-1)
    p = torch.exp(log_p)

    log_p_target = log_p.gather(1, targets.unsqueeze(1)).squeeze(1)
    p_target = p.gather(1, targets.unsqueeze(1)).squeeze(1)

    loss = - (1.0 - p_target) ** gamma * log_p_target

    if alpha is not None:
        loss = loss * alpha[targets]

    return loss.mean()


def _focal_loss_with_optional_targets(
    logits: torch.Tensor,
    targets: torch.Tensor,
    gamma: float = 2.0,
    alpha: torch.Tensor = None,
) -> torch.Tensor:
    if not torch.any(targets != -100):
        return logits.sum() * 0.0
    return focal_loss(logits, targets, gamma=gamma, alpha=alpha, ignore_index=-100)


def get_hidden_features_from_state_dict(state_dict: dict, default: int = 128) -> int:
    """Detects hidden_features size dynamically from a GCN state_dict."""
    if "gcn1.W_rel" in state_dict:
        return state_dict["gcn1.W_rel"].shape[2]
    return default


def _candidate_pair_values(values: torch.Tensor, combinations: torch.Tensor) -> torch.Tensor:
    """Gather the six internal pair values for each 4-word candidate.

    Supports scalar edge score matrices with shape ``(16, 16)`` or
    ``(batch, 16, 16)``, and feature matrices with shape ``(16, 16, dim)`` or
    ``(batch, 16, 16, dim)``.
    """
    if len(values.shape) == 4:
        return torch.stack(
            [
                values[:, combinations[:, 0], combinations[:, 1]],
                values[:, combinations[:, 0], combinations[:, 2]],
                values[:, combinations[:, 0], combinations[:, 3]],
                values[:, combinations[:, 1], combinations[:, 2]],
                values[:, combinations[:, 1], combinations[:, 3]],
                values[:, combinations[:, 2], combinations[:, 3]],
            ],
            dim=2,
        )
    if len(values.shape) == 3 and values.shape[1] == values.shape[2]:
        return torch.stack(
            [
                values[:, combinations[:, 0], combinations[:, 1]],
                values[:, combinations[:, 0], combinations[:, 2]],
                values[:, combinations[:, 0], combinations[:, 3]],
                values[:, combinations[:, 1], combinations[:, 2]],
                values[:, combinations[:, 1], combinations[:, 3]],
                values[:, combinations[:, 2], combinations[:, 3]],
            ],
            dim=2,
        )
    if len(values.shape) in (2, 3):
        return torch.stack(
            [
                values[combinations[:, 0], combinations[:, 1]],
                values[combinations[:, 0], combinations[:, 2]],
                values[combinations[:, 0], combinations[:, 3]],
                values[combinations[:, 1], combinations[:, 2]],
                values[combinations[:, 1], combinations[:, 3]],
                values[combinations[:, 2], combinations[:, 3]],
            ],
            dim=1,
        )
    raise ValueError(f"Unsupported candidate pair tensor shape: {tuple(values.shape)}")


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
                rtype = normalize_relation_archetype(
                    w_i_cat.get("relation_type", "SYNONYM_OR_NEAR")
                )
                relation_true[i, j] = RELATION_ARCHETYPE_TO_IDX.get(
                    rtype,
                    RELATION_ARCHETYPE_TO_IDX["SEMANTIC_SET"],
                )
    return relation_true


def build_group_relation_targets(
    model: ConnectionsScoringMixin,
    edge_logits: torch.Tensor,
    words: List[str],
    word_to_cat: Any,
    device: str,
    hard_negative_count: int = GROUP_RELATION_HARD_NEGATIVES,
) -> torch.Tensor:
    """Build quartet archetype labels for true groups plus hard no-relation negatives."""
    combinations = model.comb_tensor.to(device)
    targets = torch.full((combinations.shape[0],), -100, dtype=torch.long, device=device)
    true_groups = build_true_group_tensor(words, word_to_cat, device)
    if true_groups.numel() == 0:
        return targets

    true_mask = (combinations.unsqueeze(1) == true_groups.unsqueeze(0)).all(dim=2).any(dim=1)
    for true_group in true_groups:
        group_idx = int((combinations == true_group).all(dim=1).nonzero(as_tuple=False)[0].item())
        first_word = words[int(true_group[0].item())]
        rtype = normalize_relation_archetype(
            _word_category(word_to_cat, first_word).get("relation_type", "SYNONYM_OR_NEAR")
        )
        targets[group_idx] = RELATION_ARCHETYPE_TO_IDX[rtype]

    edge_probs = torch.sigmoid(edge_logits)
    _, scores = model.get_candidate_scores_tensor(edge_probs)
    negative_indices = torch.nonzero(~true_mask, as_tuple=False).flatten()
    if negative_indices.numel() > 0 and hard_negative_count > 0:
        negative_scores = scores[negative_indices]
        top_k = min(hard_negative_count, negative_indices.numel())
        hard_negative_indices = negative_indices[torch.topk(negative_scores, k=top_k).indices]
        targets[hard_negative_indices] = NO_RELATION_IDX

    return targets


def build_relation_class_weights(puzzles: list, device: str) -> torch.Tensor:
    """Build clipped inverse-frequency relation weights with weak no-relation pressure."""
    counts = torch.zeros(NUM_RELATION_ARCHETYPES, dtype=torch.float32)
    for puzzle in puzzles:
        words = _puzzle_value(puzzle, "words")
        word_to_cat = _puzzle_value(puzzle, "word_to_cat")
        for i in range(16):
            for j in range(16):
                if i == j:
                    continue
                w_i_cat = _word_category(word_to_cat, words[i])
                w_j_cat = _word_category(word_to_cat, words[j])
                if w_i_cat["cat_idx"] == w_j_cat["cat_idx"]:
                    rtype = normalize_relation_archetype(
                        w_i_cat.get("relation_type", "SYNONYM_OR_NEAR")
                    )
                    counts[RELATION_ARCHETYPE_TO_IDX[rtype]] += 1.0
                else:
                    counts[NO_RELATION_IDX] += 1.0

    weights = torch.ones(NUM_RELATION_ARCHETYPES, dtype=torch.float32)
    positive_counts = counts[1:]
    present_positive = positive_counts > 0
    if torch.any(present_positive):
        mean_count = positive_counts[present_positive].mean()
        positive_weights = torch.ones_like(positive_counts)
        positive_weights[present_positive] = mean_count / positive_counts[present_positive]
        weights[1:] = torch.clamp(positive_weights, min=0.5, max=4.0)
    weights[NO_RELATION_IDX] = 0.25
    return weights.to(device)


def build_group_class_weights(puzzles: list, device: str, hard_negative_count: int) -> torch.Tensor:
    """Build class-balanced weights for group-level relation classifier."""
    counts = torch.zeros(NUM_RELATION_ARCHETYPES, dtype=torch.float32)
    for puzzle in puzzles:
        if isinstance(puzzle, dict):
            words = puzzle["words"]
            word_to_cat = puzzle["word_to_cat"]
        else:
            words = puzzle.words
            word_to_cat = puzzle.word_to_cat

        # Count true categories
        seen_cats = set()
        for w in words:
            w_cat = _word_category(word_to_cat, w)
            cat_idx = w_cat["cat_idx"]
            if cat_idx not in seen_cats:
                seen_cats.add(cat_idx)
                rtype = normalize_relation_archetype(w_cat.get("relation_type", "SYNONYM_OR_NEAR"))
                counts[RELATION_ARCHETYPE_TO_IDX[rtype]] += 1.0

        # Count hard negatives (NO_RELATION)
        counts[NO_RELATION_IDX] += float(hard_negative_count)

    total_samples = counts.sum()
    weights = torch.ones(NUM_RELATION_ARCHETYPES, dtype=torch.float32)
    for i in range(NUM_RELATION_ARCHETYPES):
        if counts[i] > 0:
            # Balanced weight formula: total / (num_classes * count)
            weights[i] = total_samples / (NUM_RELATION_ARCHETYPES * counts[i])
        else:
            weights[i] = 1.0

    # Clamp weights to stabilize training on rare classes
    weights = torch.clamp(weights, min=0.1, max=10.0)
    # Set explicit NO_RELATION weight to reduce false positives
    weights[NO_RELATION_IDX] = 0.15
    return weights.to(device)


def drop_edges(adj: torch.Tensor, p: float = 0.2, training: bool = True) -> torch.Tensor:
    """Randomly drop edges (set to 0) in multi-relational adjacency tensor to regularize GCN."""
    if not training or p <= 0.0:
        return adj
    mask = (torch.rand_like(adj) > p).to(adj.dtype)
    return adj * mask


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


def _near_miss_negative_mask(
    combinations: torch.Tensor,
    true_mask: torch.Tensor,
) -> torch.Tensor:
    """Return false candidate groups that overlap any true group by exactly 3 words."""
    true_groups = combinations[true_mask]
    if true_groups.numel() == 0:
        return torch.zeros_like(true_mask, dtype=torch.bool)

    overlaps = (combinations.unsqueeze(1) == true_groups.unsqueeze(0)).sum(dim=-1)
    max_overlap = overlaps.max(dim=1).values
    return (~true_mask) & (max_overlap == 3)


def _groupwise_margin_loss_from_scores(
    scores: torch.Tensor,
    combinations: torch.Tensor,
    true_mask: torch.Tensor,
    margin: float = GROUPWISE_LOSS_MARGIN,
    hard_negative_count: int = GROUPWISE_HARD_NEGATIVES,
) -> torch.Tensor:
    """Rank true groups above hard negatives, emphasizing 3-of-4 near misses."""
    true_scores = scores[true_mask]
    negative_mask = ~true_mask
    negative_scores = scores[negative_mask]
    if true_scores.numel() == 0 or negative_scores.numel() == 0:
        return scores.new_tensor(0.0)

    near_miss_mask = _near_miss_negative_mask(combinations, true_mask)[negative_mask]
    selection_scores = negative_scores + near_miss_mask.to(scores.dtype) * NEAR_MISS_HARD_NEGATIVE_BONUS
    hard_count = min(hard_negative_count, negative_scores.numel())
    hard_positions = torch.topk(selection_scores, k=hard_count).indices
    hard_negative_scores = negative_scores[hard_positions]
    hard_weights = torch.where(
        near_miss_mask[hard_positions],
        torch.full_like(hard_negative_scores, NEAR_MISS_GROUP_LOSS_WEIGHT),
        torch.ones_like(hard_negative_scores),
    )

    losses = torch.clamp(
        margin - true_scores.unsqueeze(1) + hard_negative_scores.unsqueeze(0),
        min=0.0,
    ) ** 2
    return (losses * hard_weights.unsqueeze(0)).mean()


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
    return _groupwise_margin_loss_from_scores(
        scores,
        combinations,
        true_mask,
        margin=margin,
        hard_negative_count=hard_negative_count,
    )
