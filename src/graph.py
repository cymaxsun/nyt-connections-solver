import itertools
import torch
from typing import List, Dict, Tuple, Any
from src.features import FeatureExtractor

class ConnectionsGraph:
    """
    Representation of a single Connections puzzle graph.
    Wraps the node and edge feature matrices in PyTorch tensors.
    """
    def __init__(
        self, 
        words: List[str], 
        extractor: FeatureExtractor = None, 
        device: str = "cpu",
        node_features: torch.Tensor = None,
        edge_features: torch.Tensor = None
    ):
        self.words = [w.strip().upper() for w in words]
        self.device = device
        
        if node_features is not None and edge_features is not None:
            self.node_features = torch.as_tensor(node_features, dtype=torch.float32, device=device)
            self.edge_features = torch.as_tensor(edge_features, dtype=torch.float32, device=device)
        else:
            assert extractor is not None, "extractor must be provided if features are not precomputed"
            node_feats_np, edge_feats_np = extractor.build_graph_matrices(self.words)
            self.node_features = torch.tensor(node_feats_np, dtype=torch.float32, device=device)
            self.edge_features = torch.tensor(edge_feats_np, dtype=torch.float32, device=device)

        self.node_features = torch.nan_to_num(self.node_features, nan=0.0, posinf=1.0, neginf=0.0)
        self.edge_features = torch.nan_to_num(self.edge_features, nan=0.0, posinf=1.0, neginf=0.0)
            
        self.num_nodes = len(words)
        self.active_node_mask = torch.ones(self.num_nodes, dtype=torch.float32, device=device)
        self.adaptive_edge_weights = torch.ones(
            (self.num_nodes, self.num_nodes), dtype=torch.float32, device=device
        )
        self.rejected_groups = set()
        
    def to(self, device: str):
        """Move tensors to the specified device."""
        self.device = device
        self.node_features = self.node_features.to(device)
        self.edge_features = self.edge_features.to(device)
        self.active_node_mask = self.active_node_mask.to(device)
        self.adaptive_edge_weights = self.adaptive_edge_weights.to(device)
        return self

    def get_adjacency_for_dimension(self, dim_idx: int) -> torch.Tensor:
        """
        Extracts a single 16x16 adjacency matrix for a given feature dimension.
        Dimensions:
            0: WordNet path similarity
            1: WordNet shares hypernym
            2: ConceptNet forward connection weight
            3: ConceptNet backward connection weight
            4: Clue description TF-IDF similarity
            5: Is Anagram
            6: Shares Prefix
            7: Shares Suffix
            8: Is Substring
            9: Length difference (needs inversion to be adjacency)
            10: SentenceTransformer cosine similarity
        """
        adj = self.edge_features[:, :, dim_idx]
        if dim_idx == 9:
            # Invert length difference so similar lengths have high edge weights
            adj = 1.0 - adj
        active_edges = torch.outer(self.active_node_mask, self.active_node_mask)
        adj = adj * self.adaptive_edge_weights * active_edges
        return adj

    def get_multi_relational_adjacency(self) -> torch.Tensor:
        """
        Returns a combined adjacency matrix by aggregating the multi-dimensional edge features.
        Weights each dimension equally or returns a tensor of shape (num_dimensions, 16, 16).
        """
        # Shape: (num_nodes, num_nodes, num_edge_features)
        # We permute it to (num_edge_features, num_nodes, num_nodes) for multi-relational convolution
        adj = self.edge_features.permute(2, 0, 1).clone()
        # Invert the length difference dimension (dimension 9)
        adj[9] = 1.0 - adj[9]
        adj = adj * self.adaptive_edge_weights.unsqueeze(0)
        active_edges = torch.outer(self.active_node_mask, self.active_node_mask)
        adj = adj * active_edges.unsqueeze(0)
        return adj

    def update_edges_from_feedback(self, action_indices: tuple, feedback: str):
        """
        Modify edge features based on game feedback to refine the graph for subsequent GCN passes.

        The raw feature tensor stays immutable. Feedback is stored in an adaptive edge-weight
        layer so inverse/distance-like feature channels cannot be accidentally strengthened.

        - Incorrect: Penalize all 6 pairwise edges between the 4 guessed words.
        - One Away: Reject the exact quartet while preserving most internal cohesion and
          lightly opening replacement edges to other active words.
        - Correct: Mask solved words out of all future graph passes.
        """
        feedback = self._normalize_feedback(feedback)
        indices = list(action_indices)
        group_key = tuple(sorted(indices))

        if feedback == "correct":
            for idx in indices:
                self.active_node_mask[idx] = 0.0
                self.adaptive_edge_weights[idx, :] = 0.0
                self.adaptive_edge_weights[:, idx] = 0.0
            return

        if feedback not in {"incorrect", "one_away"}:
            return

        self.rejected_groups.add(group_key)

        if feedback == "incorrect":
            self._scale_internal_edges(indices, factor=0.25)
        else:
            self._scale_internal_edges(indices, factor=0.9)
            self._scale_replacement_edges(indices, factor=1.08)

        self.adaptive_edge_weights.clamp_(0.02, 2.0)

    def filter_candidates(
        self,
        candidates: List[Tuple[Tuple[int, ...], float]]
    ) -> List[Tuple[Tuple[int, ...], float]]:
        """Remove candidate quartets already ruled out by feedback."""
        return [
            (comb, score)
            for comb, score in candidates
            if tuple(sorted(comb)) not in self.rejected_groups
        ]

    def _scale_internal_edges(self, indices: List[int], factor: float):
        for a, b in itertools.combinations(indices, 2):
            self.adaptive_edge_weights[a, b] *= factor
            self.adaptive_edge_weights[b, a] *= factor

    def _scale_replacement_edges(self, indices: List[int], factor: float):
        guessed = set(indices)
        active_outside = [
            idx for idx in range(self.num_nodes)
            if idx not in guessed and self.active_node_mask[idx].item() == 1.0
        ]
        for a in indices:
            for b in active_outside:
                self.adaptive_edge_weights[a, b] *= factor
                self.adaptive_edge_weights[b, a] *= factor

    @staticmethod
    def _normalize_feedback(feedback: str) -> str:
        normalized = feedback.strip().lower().replace("-", " ").replace("_", " ")
        if normalized in {"correct", "correct!", "y", "yes", "1"}:
            return "correct"
        if normalized in {"one away", "1away", "oneaway", "3"}:
            return "one_away"
        if normalized in {"incorrect", "wrong", "n", "no"}:
            return "incorrect"
        return normalized

if __name__ == "__main__":
    extractor = FeatureExtractor()
    test_words = [
        "HAIL", "RAIN", "SLEET", "SNOW",
        "BUCKS", "HEAT", "JAZZ", "NETS",
        "OPTION", "RETURN", "SHIFT", "TAB",
        "KAYAK", "LEVEL", "MOM", "RACECAR"
    ]
    graph = ConnectionsGraph(test_words, extractor)
    print("PyTorch Node Features Shape:", graph.node_features.shape)
    print("PyTorch Multi-Relational Adjacency Shape:", graph.get_multi_relational_adjacency().shape)
