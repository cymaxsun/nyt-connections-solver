import unittest

import torch

from src.features import EDGE_FEATURE_DIM
from src.gcn import (
    ConnectionsGCN,
    build_relation_targets,
    build_true_group_tensor,
    groupwise_ranking_loss,
)
from src.relation_archetypes import (
    NO_RELATION_IDX,
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_TO_IDX,
)


class GCNScoringTests(unittest.TestCase):
    def test_relation_head_outputs_no_relation_class(self):
        model = ConnectionsGCN()
        node_features = torch.randn(16, 775)
        adj = torch.zeros(EDGE_FEATURE_DIM, 16, 16)

        _, _, relation_logits = model(node_features, adj, return_logits=True)

        self.assertEqual(relation_logits.shape, (16, 16, NUM_RELATION_ARCHETYPES))

    def test_relation_targets_include_no_relation_negatives(self):
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {
                "cat_idx": idx // 4,
                "relation_type": "WORDPLAY" if idx // 4 == 0 else "SYNONYM",
            }
            for idx, word in enumerate(words)
        }

        targets = build_relation_targets(words, word_to_cat, "cpu")

        self.assertEqual(int(targets[0, 0].item()), -100)
        self.assertEqual(int(targets[0, 1].item()), RELATION_ARCHETYPE_TO_IDX["WORDPLAY"])
        self.assertEqual(int(targets[0, 4].item()), NO_RELATION_IDX)

    def test_true_group_tensor_extracts_sorted_groups(self):
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM"}
            for idx, word in enumerate(words)
        }

        true_groups = build_true_group_tensor(words, word_to_cat, "cpu")

        self.assertEqual(true_groups.tolist(), [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15],
        ])

    def test_groupwise_loss_positive_when_false_group_outranks_true_group(self):
        model = ConnectionsGCN()
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM"}
            for idx, word in enumerate(words)
        }
        edge_logits = torch.full((16, 16), -6.0)
        for i, j in [(0, 1), (0, 2), (0, 4), (1, 2), (1, 4), (2, 4)]:
            edge_logits[i, j] = 6.0
            edge_logits[j, i] = 6.0

        loss = groupwise_ranking_loss(
            model,
            edge_logits,
            words,
            word_to_cat,
            margin=0.05,
            hard_negative_count=8,
        )

        self.assertGreater(float(loss), 0.0)

    def test_groupwise_loss_zero_when_true_groups_clear_margin(self):
        model = ConnectionsGCN()
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM"}
            for idx, word in enumerate(words)
        }
        edge_logits = torch.full((16, 16), -6.0)
        for start in [0, 4, 8, 12]:
            group = range(start, start + 4)
            for i in group:
                for j in group:
                    if i != j:
                        edge_logits[i, j] = 6.0

        loss = groupwise_ranking_loss(
            model,
            edge_logits,
            words,
            word_to_cat,
            margin=0.05,
            hard_negative_count=16,
        )

        self.assertAlmostEqual(float(loss), 0.0, places=6)

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
