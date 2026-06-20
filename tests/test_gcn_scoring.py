import unittest

import torch

from src.features import DEFAULT_NODE_FEATURE_DIM, EDGE_FEATURE_DIM
from src.gcn import (
    ConnectionsGCN,
    build_group_relation_targets,
    build_relation_class_weights,
    build_relation_targets,
    build_true_group_tensor,
    _cross_entropy_with_optional_targets,
    groupwise_ranking_loss,
)
from src.relation_archetypes import (
    NO_RELATION_IDX,
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_TO_IDX,
    relation_prediction_from_probabilities,
)


class GCNScoringTests(unittest.TestCase):
    def test_relation_head_outputs_no_relation_class(self):
        model = ConnectionsGCN()
        node_features = torch.randn(16, DEFAULT_NODE_FEATURE_DIM)
        adj = torch.zeros(EDGE_FEATURE_DIM, 16, 16)

        _, _, relation_logits = model(node_features, adj, return_logits=True)

        self.assertEqual(relation_logits.shape, (16, 16, NUM_RELATION_ARCHETYPES))

    def test_group_relation_head_outputs_candidate_archetype_logits(self):
        model = ConnectionsGCN()
        node_features = torch.randn(16, DEFAULT_NODE_FEATURE_DIM)
        adj = torch.zeros(EDGE_FEATURE_DIM, 16, 16)

        _, _, _, group_relation_logits = model(
            node_features,
            adj,
            return_logits=True,
            return_group_logits=True,
        )

        self.assertEqual(group_relation_logits.shape, (1820, NUM_RELATION_ARCHETYPES))

    def test_relation_targets_include_no_relation_negatives(self):
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {
                "cat_idx": idx // 4,
                "relation_type": "SOUND_OR_SPELLING" if idx // 4 == 0 else "SYNONYM_OR_NEAR",
            }
            for idx, word in enumerate(words)
        }

        targets = build_relation_targets(words, word_to_cat, "cpu")

        self.assertEqual(int(targets[0, 0].item()), -100)
        self.assertEqual(int(targets[0, 1].item()), RELATION_ARCHETYPE_TO_IDX["SOUND_OR_SPELLING"])
        self.assertEqual(int(targets[0, 4].item()), NO_RELATION_IDX)

    def test_relation_targets_normalize_legacy_and_unknown_positive_labels(self):
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {
                "cat_idx": idx // 4,
                "relation_type": "MORPHOLOGY" if idx // 4 == 0 else "UNKNOWN_LEGACY",
            }
            for idx, word in enumerate(words)
        }

        targets = build_relation_targets(words, word_to_cat, "cpu")

        self.assertEqual(int(targets[0, 1].item()), RELATION_ARCHETYPE_TO_IDX["WORD_FORM"])
        self.assertEqual(int(targets[4, 5].item()), RELATION_ARCHETYPE_TO_IDX["SEMANTIC_SET"])

    def test_group_relation_targets_label_true_groups_and_hard_negatives(self):
        model = ConnectionsGCN()
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {
                "cat_idx": idx // 4,
                "relation_type": "FILL_IN_THE_BLANK" if idx // 4 == 0 else "SYNONYM_OR_NEAR",
            }
            for idx, word in enumerate(words)
        }
        edge_logits = torch.zeros(16, 16)

        targets = build_group_relation_targets(
            model,
            edge_logits,
            words,
            word_to_cat,
            "cpu",
            hard_negative_count=8,
        )
        combinations = model.comb_tensor
        true_group_idx = int(
            (combinations == torch.tensor([0, 1, 2, 3])).all(dim=1).nonzero(as_tuple=False)[0].item()
        )

        self.assertEqual(
            int(targets[true_group_idx].item()),
            RELATION_ARCHETYPE_TO_IDX["FILL_IN_THE_BLANK"],
        )
        self.assertEqual(int((targets == NO_RELATION_IDX).sum().item()), 8)

    def test_optional_cross_entropy_returns_zero_for_all_ignored_targets(self):
        logits = torch.randn(4, NUM_RELATION_ARCHETYPES, requires_grad=True)
        targets = torch.full((4,), -100, dtype=torch.long)

        loss = _cross_entropy_with_optional_targets(logits, targets)

        self.assertEqual(float(loss.detach()), 0.0)
        loss.backward()
        self.assertIsNotNone(logits.grad)

    def test_relation_class_weights_downweight_no_relation(self):
        words = [f"W{i}" for i in range(16)]
        puzzles = [{
            "words": words,
            "word_to_cat": {
                word: {"cat_idx": idx // 4, "relation_type": "SYNONYM_OR_NEAR"}
                for idx, word in enumerate(words)
            },
        }]

        weights = build_relation_class_weights(puzzles, "cpu")

        self.assertEqual(float(weights[NO_RELATION_IDX]), 0.25)
        self.assertGreater(float(weights[RELATION_ARCHETYPE_TO_IDX["SYNONYM_OR_NEAR"]]), 0.0)

    def test_relation_prediction_suppresses_weak_positive_guess(self):
        probs = [0.40, 0.10, 0.44, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

        self.assertIsNone(relation_prediction_from_probabilities(probs))

    def test_relation_prediction_returns_confident_positive_guess(self):
        probs = [0.20, 0.10, 0.56, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02]

        self.assertEqual(
            relation_prediction_from_probabilities(probs),
            RELATION_ARCHETYPE_TO_IDX["SYNONYM_OR_NEAR"],
        )

    def test_true_group_tensor_extracts_sorted_groups(self):
        words = [f"W{i}" for i in range(16)]
        word_to_cat = {
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM_OR_NEAR"}
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
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM_OR_NEAR"}
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
            word: {"cat_idx": idx // 4, "relation_type": "SYNONYM_OR_NEAR"}
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

    def test_candidate_scores_get_small_boost_from_group_archetype_confidence(self):
        model = ConnectionsGCN()
        edge_probs = torch.zeros(16, 16)
        for i, j in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
            edge_probs[i, j] = 0.5
            edge_probs[j, i] = 0.5
        combinations, base_scores = model.get_candidate_scores_tensor(edge_probs)
        group_logits = torch.zeros(1820, NUM_RELATION_ARCHETYPES)
        match = (combinations == torch.tensor([0, 1, 2, 3])).all(dim=1)
        group_logits[match, NO_RELATION_IDX] = -3.0
        group_logits[match, RELATION_ARCHETYPE_TO_IDX["SYNONYM_OR_NEAR"]] = 3.0

        _, boosted_scores = model.get_candidate_scores_tensor(edge_probs, group_logits)

        self.assertGreater(float(boosted_scores[match][0]), float(base_scores[match][0]))

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
