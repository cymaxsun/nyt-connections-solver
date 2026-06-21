import itertools
import unittest

import numpy as np

from src.features import EDGE_FEATURE_DIM, SENTENCE_SIMILARITY_DIM, PHONEME_EDIT_DISTANCE_DIM
from src.raw_candidates import (
    evaluate_raw_candidates,
    raw_candidate_groups,
    raw_pair_scores,
)
from src.graph import LENGTH_SIMILARITY_DIM, LEVENSHTEIN_DISTANCE_DIM


class RawCandidateTests(unittest.TestCase):
    def test_raw_pair_scores_sparsify_length_channel(self):
        edge_features = np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32)
        edge_features[:, :, LEVENSHTEIN_DISTANCE_DIM] = 1.0
        edge_features[:, :, PHONEME_EDIT_DISTANCE_DIM] = 1.0
        edge_features[0, 1, LENGTH_SIMILARITY_DIM] = 0.0
        edge_features[1, 0, LENGTH_SIMILARITY_DIM] = 0.0
        edge_features[0, 2, LENGTH_SIMILARITY_DIM] = 0.2
        edge_features[2, 0, LENGTH_SIMILARITY_DIM] = 0.2

        scores = raw_pair_scores(edge_features)

        self.assertGreater(scores[0, 1], 0.0)
        self.assertEqual(scores[0, 2], 0.0)

    def test_raw_pair_scores_sparsify_levenshtein_channel(self):
        edge_features = np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32)
        edge_features[:, :, LENGTH_SIMILARITY_DIM] = 1.0
        edge_features[:, :, LEVENSHTEIN_DISTANCE_DIM] = 1.0
        edge_features[:, :, PHONEME_EDIT_DISTANCE_DIM] = 1.0
        edge_features[0, 1, LEVENSHTEIN_DISTANCE_DIM] = 0.25
        edge_features[1, 0, LEVENSHTEIN_DISTANCE_DIM] = 0.25
        edge_features[0, 2, LEVENSHTEIN_DISTANCE_DIM] = 0.5
        edge_features[2, 0, LEVENSHTEIN_DISTANCE_DIM] = 0.5

        scores = raw_pair_scores(edge_features)

        self.assertGreater(scores[0, 1], 0.0)
        self.assertEqual(scores[0, 2], 0.0)

    def test_raw_candidate_groups_rank_cohesive_group_first(self):
        pair_scores = np.zeros((16, 16), dtype=np.float32)
        for i in range(4):
            for j in range(4):
                if i != j:
                    pair_scores[i, j] = 1.0

        candidates = raw_candidate_groups(pair_scores)

        self.assertEqual(candidates[0][0], (0, 1, 2, 3))
        self.assertEqual(candidates[0][1], 1.0)

    def test_raw_candidate_groups_penalize_one_weak_pair(self):
        pair_scores = np.zeros((16, 16), dtype=np.float32)
        for i, j in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]:
            pair_scores[i, j] = 1.0
            pair_scores[j, i] = 1.0
        for i, j in itertools.combinations((4, 5, 6, 7), 2):
            pair_scores[i, j] = 0.7
            pair_scores[j, i] = 0.7

        candidates = raw_candidate_groups(pair_scores)

        self.assertLess(
            [group for group, _ in candidates].index((4, 5, 6, 7)),
            [group for group, _ in candidates].index((0, 1, 2, 3)),
        )

    def test_evaluate_raw_candidates_finds_perfect_synthetic_partition(self):
        edge_features = np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32)
        edge_features[:, :, LENGTH_SIMILARITY_DIM] = 1.0
        edge_features[:, :, LEVENSHTEIN_DISTANCE_DIM] = 1.0
        edge_features[:, :, PHONEME_EDIT_DISTANCE_DIM] = 1.0
        words = [f"WORD{i}" for i in range(16)]
        word_to_cat = {}
        for cat_idx in range(4):
            group_indices = range(cat_idx * 4, cat_idx * 4 + 4)
            for idx in group_indices:
                word_to_cat[words[idx]] = {"cat_idx": cat_idx}
            for i in group_indices:
                for j in group_indices:
                    if i != j:
                        edge_features[i, j, SENTENCE_SIMILARITY_DIM] = 1.0

        metrics = evaluate_raw_candidates(
            [{
                "id": 1,
                "words": words,
                "word_to_cat": word_to_cat,
                "edge_features": edge_features,
            }],
            top_ks=(4,),
        )

        self.assertEqual(metrics.group_recall_at_k[4], 1.0)
        self.assertEqual(metrics.perfect_best_partitions, 1)
        self.assertEqual(metrics.avg_exact_groups_in_best_partition, 4.0)


if __name__ == "__main__":
    unittest.main()
