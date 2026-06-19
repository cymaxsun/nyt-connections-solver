import unittest

import torch

from src.gcn import ConnectionsGCN


class GCNScoringTests(unittest.TestCase):
    def test_candidate_scores_use_penalized_group_score(self):
        model = ConnectionsGCN()
        edge_probs = torch.zeros(16, 16)
        for i, j in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]:
            edge_probs[i, j] = 1.0
            edge_probs[j, i] = 1.0

        combinations, scores = model.get_candidate_scores_tensor(edge_probs)
        match = (combinations == torch.tensor([0, 1, 2, 3])).all(dim=1)

        self.assertAlmostEqual(float(scores[match][0]), 7.0 / 12.0, places=6)

    def test_candidate_subgraphs_match_tensor_scores(self):
        model = ConnectionsGCN()
        edge_probs = torch.zeros(16, 16)
        for i, j in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
            edge_probs[i, j] = 0.9
            edge_probs[j, i] = 0.9

        combinations, scores = model.get_candidate_scores_tensor(edge_probs)
        candidates = model.get_candidate_subgraphs(edge_probs)
        top_group, top_score = candidates[0]
        match = (combinations == torch.tensor(top_group)).all(dim=1)

        self.assertEqual(top_group, (0, 1, 2, 3))
        self.assertAlmostEqual(top_score, float(scores[match][0]), places=6)


if __name__ == "__main__":
    unittest.main()
