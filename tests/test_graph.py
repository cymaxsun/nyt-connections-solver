import unittest

import numpy as np

from src.features import EDGE_FEATURE_DIM
from src.graph import ConnectionsGraph, LENGTH_SIMILARITY_DIM


class ConnectionsGraphLengthSimilarityTests(unittest.TestCase):
    def _build_graph(self, length_diffs):
        node_features = np.zeros((16, 7), dtype=np.float32)
        edge_features = np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32)
        edge_features[:, :, LENGTH_SIMILARITY_DIM] = 1.0
        for i, j, value in length_diffs:
            edge_features[i, j, LENGTH_SIMILARITY_DIM] = value

        return ConnectionsGraph(
            [f"WORD{i}" for i in range(16)],
            node_features=node_features,
            edge_features=edge_features,
        )

    def test_equal_length_pair_remains_connected(self):
        graph = self._build_graph([(0, 1, 0.0)])

        adj = graph.get_adjacency_for_dimension(LENGTH_SIMILARITY_DIM)

        self.assertEqual(adj[0, 1].item(), 1.0)

    def test_length_similarity_below_threshold_is_removed(self):
        graph = self._build_graph([(0, 1, 0.2)])

        adj = graph.get_adjacency_for_dimension(LENGTH_SIMILARITY_DIM)

        self.assertEqual(adj[0, 1].item(), 0.0)

    def test_single_and_multi_relation_paths_have_same_sparsity(self):
        graph = self._build_graph([
            (0, 1, 0.0),
            (0, 2, 0.2),
            (1, 2, 0.1),
        ])

        single_adj = graph.get_adjacency_for_dimension(LENGTH_SIMILARITY_DIM)
        multi_adj = graph.get_multi_relational_adjacency()[LENGTH_SIMILARITY_DIM]

        np.testing.assert_array_equal(
            (single_adj.numpy() > 0.0),
            (multi_adj.numpy() > 0.0),
        )

    def test_active_masks_and_adaptive_weights_still_apply(self):
        graph = self._build_graph([
            (0, 1, 0.0),
            (0, 2, 0.0),
        ])
        graph.adaptive_edge_weights[0, 1] = 0.5
        graph.active_node_mask[2] = 0.0

        adj = graph.get_adjacency_for_dimension(LENGTH_SIMILARITY_DIM)

        self.assertEqual(adj[0, 1].item(), 0.5)
        self.assertEqual(adj[0, 2].item(), 0.0)


if __name__ == "__main__":
    unittest.main()
