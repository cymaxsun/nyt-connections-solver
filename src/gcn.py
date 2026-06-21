import itertools
import torch
import torch.nn as nn
import torch.nn.functional as F
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
        if len(h.shape) == 3:
            # Batched case
            out = self.W_self(h)  # (batch_size, 16, out_features)
            h_proj = torch.einsum('bni,rio->brno', h, self.W_rel)  # (batch_size, num_relations, 16, out_features)
            out_rel = torch.einsum('bruv,brvo->buo', adj, h_proj)  # (batch_size, 16, out_features)
            return out + out_rel + self.bias
        else:
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
        group_input_dim = out_features * 2 + EDGE_FEATURE_DIM * 2
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
                dummy_edge = torch.zeros(batch_size, 16, 16, EDGE_FEATURE_DIM, device=node_embeddings.device)
                edge_input = torch.cat([h_exp1, h_exp2, dummy_edge], dim=-1)
        else:
            # Expand and concatenate to compute pairwise representations
            h_exp1 = node_embeddings.unsqueeze(1).expand(-1, 16, -1)
            h_exp2 = node_embeddings.unsqueeze(0).expand(16, -1, -1)
            
            if edge_features is not None:
                edge_input = torch.cat([h_exp1, h_exp2, edge_features], dim=-1)
            else:
                dummy_edge = torch.zeros(16, 16, EDGE_FEATURE_DIM, device=node_embeddings.device)
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
                    EDGE_FEATURE_DIM * 2,
                    dtype=node_embeddings.dtype,
                    device=node_embeddings.device,
                )
            else:
                edge_summary = torch.zeros(
                    c.shape[0],
                    EDGE_FEATURE_DIM * 2,
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
        if is_batched:
            pair_scores = torch.stack(
                [
                    edge_probs[:, c[:, 0], c[:, 1]],
                    edge_probs[:, c[:, 0], c[:, 2]],
                    edge_probs[:, c[:, 0], c[:, 3]],
                    edge_probs[:, c[:, 1], c[:, 2]],
                    edge_probs[:, c[:, 1], c[:, 3]],
                    edge_probs[:, c[:, 2], c[:, 3]],
                ],
                dim=-1,
            )
        else:
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
        if group_relation_logits is not None:
            group_probs = torch.softmax(group_relation_logits, dim=-1)
            positive_confidence = group_probs[..., 1:].max(dim=-1).values
            no_relation_confidence = group_probs[..., NO_RELATION_IDX]
            # Only boost if the prediction clears the archetype classification gate
            gate = (positive_confidence >= 0.45) & ((positive_confidence - no_relation_confidence) >= 0.10)
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
        self._init_scoring_heads(hidden_features=hidden_features, out_features=out_features)

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

    for start_idx in range(0, len(puzzles), batch_size):
        batch_puzzles = puzzles[start_idx : start_idx + batch_size]
        actual_batch_size = len(batch_puzzles)
        
        node_features_list = []
        edge_features_list = []
        adj_multi_list = []
        adj_true_list = []
        
        batch_words = []
        batch_word_to_cat = []
        
        for puzzle in batch_puzzles:
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
                
            adj_multi = graph.get_multi_relational_adjacency()
            adj_multi = drop_edges(adj_multi, p=0.2, training=True)
            
            node_features_list.append(graph.node_features)
            edge_features_list.append(graph.edge_features)
            adj_multi_list.append(adj_multi)
            adj_true_list.append(adj_true)
            
            batch_words.append(words)
            batch_word_to_cat.append(word_to_cat)
            
        batched_node_features = torch.stack(node_features_list)
        batched_edge_features = torch.stack(edge_features_list)
        batched_adj_multi = torch.stack(adj_multi_list)

        node_embeddings, edge_logits, relation_logits, group_relation_logits = model(
            batched_node_features,
            batched_adj_multi,
            batched_edge_features,
            return_logits=True,
            return_group_logits=True,
        )

        batch_losses = []
        for i in range(actual_batch_size):
            words = batch_words[i]
            word_to_cat = batch_word_to_cat[i]
            adj_true = adj_true_list[i]

            # Weighted BCE Loss with logits
            weight_mask = diag_mask.clone()
            weight_mask[adj_true == 1] *= 4.0
            bce_loss_i = F.binary_cross_entropy_with_logits(edge_logits[i], adj_true, weight=weight_mask)

            relation_true_i = build_relation_targets(words, word_to_cat, device)

            class_loss_i = focal_loss(
                relation_logits[i].view(-1, NUM_RELATION_ARCHETYPES),
                relation_true_i.view(-1),
                gamma=2.0,
                alpha=relation_class_weights,
                ignore_index=-100,
            )
            group_relation_true_i = build_group_relation_targets(
                model,
                edge_logits[i],
                words,
                word_to_cat,
                device,
                hard_negative_count=GROUP_RELATION_HARD_NEGATIVES,
            )
            group_class_loss_i = _focal_loss_with_optional_targets(
                group_relation_logits[i],
                group_relation_true_i,
                gamma=2.0,
                alpha=group_class_weights,
            )
            group_loss_i = groupwise_ranking_loss(
                model,
                edge_logits[i],
                words,
                word_to_cat,
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
) -> Tuple[float, float]:
    """
    Validates GCN. Computes mean BCE loss and Mean Reciprocal Rank (MRR) of correct 4-node categories.
    Also visualizes a chosen puzzle index to show model clustering updates.
    """
    model.eval()
    total_loss = 0.0
    mrr_sum = 0.0
    diag_mask = 1.0 - torch.eye(16, device=device)
    relation_class_weights = build_relation_class_weights(puzzles, device)
    group_class_weights = build_group_class_weights(puzzles, device, GROUP_RELATION_HARD_NEGATIVES)

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

            node_embeddings, edge_logits, relation_logits, group_relation_logits = model(
                graph.node_features,
                graph.get_multi_relational_adjacency(),
                graph.edge_features,
                return_logits=True,
                return_group_logits=True,
            )

            # Compute loss
            weight_mask = diag_mask.clone()
            weight_mask[adj_true == 1] *= 4.0
            bce_loss = F.binary_cross_entropy_with_logits(edge_logits, adj_true, weight=weight_mask)

            relation_true = build_relation_targets(words, word_to_cat, device)

            class_loss = focal_loss(
                relation_logits.view(-1, NUM_RELATION_ARCHETYPES),
                relation_true.view(-1),
                gamma=2.0,
                alpha=relation_class_weights,
                ignore_index=-100,
            )
            group_relation_true = build_group_relation_targets(
                model,
                edge_logits,
                words,
                word_to_cat,
                device,
                hard_negative_count=GROUP_RELATION_HARD_NEGATIVES,
            )
            group_class_loss = _focal_loss_with_optional_targets(
                group_relation_logits,
                group_relation_true,
                gamma=2.0,
                alpha=group_class_weights,
            )
            group_loss = groupwise_ranking_loss(
                model,
                edge_logits,
                words,
                word_to_cat,
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

            edge_probs = torch.sigmoid(edge_logits)
            c, scores = model.get_candidate_scores_tensor(edge_probs, group_relation_logits)

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
    is_batched = len(values.shape) == 4
    if is_batched:
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
    else:
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
