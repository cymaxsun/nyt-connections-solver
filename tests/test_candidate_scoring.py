import unittest

import numpy as np
import torch

from src.candidate_scoring import score_group_pair_values


class CandidateScoringTests(unittest.TestCase):
    def test_equal_pair_scores_return_mean(self):
        self.assertAlmostEqual(float(score_group_pair_values([0.6] * 6)), 0.6, places=6)

    def test_weak_pair_penalizes_unbalanced_group(self):
        unbalanced = float(score_group_pair_values([1.0, 1.0, 1.0, 1.0, 1.0, 0.0]))
        balanced = float(score_group_pair_values([0.7] * 6))

        self.assertLess(unbalanced, balanced)

    def test_all_zero_pair_scores_return_zero(self):
        self.assertEqual(float(score_group_pair_values(np.zeros(6, dtype=np.float32))), 0.0)

    def test_torch_tensor_scores_vectorized_groups(self):
        pair_scores = torch.tensor([[0.5] * 6, [1.0, 1.0, 1.0, 1.0, 1.0, 0.0]])

        scores = score_group_pair_values(pair_scores)

        self.assertTrue(torch.allclose(scores, torch.tensor([0.5, 7.0 / 12.0])))


if __name__ == "__main__":
    unittest.main()
