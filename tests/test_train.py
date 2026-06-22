import os
import json
import tempfile
import unittest

import numpy as np
import torch

from src.features import DEFAULT_NODE_FEATURE_DIM, EDGE_FEATURE_DIM, FEATURE_SCHEMA_VERSION
from src.relation_archetypes import (
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_SCHEMA_VERSION,
)
from src.train import (
    _all_time_metadata_requires_selection_refresh,
    _gcn_all_time_best_metadata_is_current,
    _gcn_checkpoint_matches_model,
    _gcn_selection_score_from_stats,
    _load_gcn_all_time_best_selection_score,
    _load_gcn_all_time_best_mrr,
    _preprocessed_features_are_current,
    _preserve_existing_artifact,
    _save_gcn_all_time_best_checkpoint,
    _save_gcn_best_checkpoint,
    _parse_numeric_value,
    _format_comparison,
    _parse_previous_summary,
    set_deterministic_seed,
)


class PreprocessedFeatureCompatibilityTests(unittest.TestCase):
    def test_current_schema_and_edge_dim_matches(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION,
            "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32),
        }]

        self.assertTrue(_preprocessed_features_are_current(puzzles))

    def test_missing_schema_version_is_stale(self):
        puzzles = [{
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))

    def test_wrong_schema_version_is_stale(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION - 1,
            "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))

    def test_wrong_edge_feature_dim_is_stale(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION,
            "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM + 1), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))

    def test_wrong_relation_archetype_schema_is_stale(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION,
            "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION - 1,
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))


class DeterministicSeedTests(unittest.TestCase):
    def test_set_deterministic_seed_resets_python_numpy_and_torch_rngs(self):
        import random

        set_deterministic_seed(123)
        first = (
            random.random(),
            float(np.random.rand()),
            float(torch.rand(1).item()),
        )

        set_deterministic_seed(123)
        second = (
            random.random(),
            float(np.random.rand()),
            float(torch.rand(1).item()),
        )

        self.assertEqual(first, second)


class GCNCheckpointTests(unittest.TestCase):
    def _compatible_gcn_state(self, input_width: int = DEFAULT_NODE_FEATURE_DIM):
        return {
            "gcn1.W_rel": torch.zeros((EDGE_FEATURE_DIM, 16, 32)),
            "relation_score_net.2.weight": torch.zeros((NUM_RELATION_ARCHETYPES, 32)),
            "group_relation_score_net.2.weight": torch.zeros((NUM_RELATION_ARCHETYPES, 32)),
            "input_proj.weight": torch.zeros((16, input_width)),
        }

    def test_checkpoint_with_current_input_width_matches_model(self):
        self.assertTrue(_gcn_checkpoint_matches_model(self._compatible_gcn_state()))

    def test_checkpoint_with_old_input_width_is_incompatible(self):
        state = self._compatible_gcn_state(input_width=DEFAULT_NODE_FEATURE_DIM - 4)

        self.assertFalse(_gcn_checkpoint_matches_model(state))

    def test_previous_best_remains_previous_run_after_multiple_saves(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            best_path = os.path.join(temp_dir, "gcn_best.pt")
            previous_best_path = os.path.join(temp_dir, "gcn_previous_best.pt")

            previous_run_state = {"weight": torch.tensor([1.0])}
            first_current_run_state = {"weight": torch.tensor([2.0])}
            second_current_run_state = {"weight": torch.tensor([3.0])}

            _save_gcn_best_checkpoint(previous_run_state, best_path)
            _preserve_existing_artifact(best_path, previous_best_path)

            _save_gcn_best_checkpoint(first_current_run_state, best_path)
            _save_gcn_best_checkpoint(second_current_run_state, best_path)

            best_state = torch.load(best_path, map_location="cpu")
            previous_state = torch.load(previous_best_path, map_location="cpu")
            self.assertTrue(torch.equal(best_state["weight"], second_current_run_state["weight"]))
            self.assertTrue(torch.equal(previous_state["weight"], previous_run_state["weight"]))

    def test_preserve_existing_artifact_copies_current_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            current_path = os.path.join(temp_dir, "current.md")
            previous_path = os.path.join(temp_dir, "archive", "previous.md")

            with open(current_path, "w", encoding="utf-8") as f:
                f.write("old summary\n")

            _preserve_existing_artifact(current_path, previous_path)

            with open(previous_path, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), "old summary\n")

    def test_preserve_existing_artifact_ignores_missing_current_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            _preserve_existing_artifact(
                os.path.join(temp_dir, "missing.png"),
                os.path.join(temp_dir, "previous.png"),
            )

            self.assertFalse(os.path.exists(os.path.join(temp_dir, "previous.png")))

    def test_save_all_time_best_checkpoint_writes_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            checkpoint_path = os.path.join(temp_dir, "gcn_all_time_best.pt")
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")
            state = {"weight": torch.tensor([5.0])}
            validation_stats = {
                "top_partition_solved": 2,
                "best_top_k_partition_solved": 3,
                "true_groups_in_top_candidates": 20,
                "puzzles_with_all_true_groups": 4,
                "near_miss_3_of_4_candidates": 10,
            }

            _save_gcn_all_time_best_checkpoint(
                state,
                checkpoint_path,
                metadata_path,
                val_mrr=0.42,
                epoch=3,
                selection_score=123.45,
                validation_stats=validation_stats,
                validation_split_seed=32,
            )

            loaded_state = torch.load(checkpoint_path, map_location="cpu")
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            self.assertTrue(torch.equal(loaded_state["weight"], state["weight"]))
            self.assertEqual(metadata["validation_mrr"], 0.42)
            self.assertEqual(metadata["validation_selection_score"], 123.45)
            self.assertEqual(metadata["validation_split_seed"], 32)
            self.assertEqual(metadata["selection_metrics"]["best_top_k_partition_solved"], 3)
            self.assertEqual(metadata["candidate_score_weights"], {"mean": 0.6, "min": 0.4, "median": 0.0})
            self.assertEqual(
                metadata["candidate_generation"],
                {
                    "single_swap_repair_seed_score_priority_weight": 0.05,
                    "group_archetype_score_weight": 0.05,
                    "group_archetype_positive_gate": 0.4,
                    "group_archetype_margin_gate": 0.05,
                    "partition_score_mean_weight": 0.45,
                    "partition_score_min_weight": 0.4,
                    "partition_score_median_weight": 0.15,
                    "default_partition_top_n": 300.0,
                    "default_partition_top_k": 20.0,
                    "partition_search_max_states": 20000.0,
                    "default_single_swap_repair_seed_limit": 40.0,
                    "default_single_swap_max_repairs": 160.0,
                },
            )
            self.assertEqual(metadata["epoch"], 3)
            self.assertTrue(_gcn_all_time_best_metadata_is_current(metadata))
            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.42)
            self.assertEqual(_load_gcn_all_time_best_selection_score(metadata_path), 123.45)
            self.assertFalse(_all_time_metadata_requires_selection_refresh(metadata_path, 32))
            self.assertTrue(_all_time_metadata_requires_selection_refresh(metadata_path, 42))

    def test_all_time_best_metadata_without_selection_requires_refresh(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                        "default_node_feature_dim": DEFAULT_NODE_FEATURE_DIM,
                    },
                    f,
                )

            self.assertTrue(_all_time_metadata_requires_selection_refresh(metadata_path, 42))

    def test_stale_all_time_best_metadata_is_ignored(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM + 1,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                    },
                    f,
                )

            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.0)

    def test_all_time_best_metadata_with_stale_candidate_scorer_is_ignored(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                        "default_node_feature_dim": DEFAULT_NODE_FEATURE_DIM,
                        "candidate_score_weights": {"mean": 0.55, "min": 0.35, "median": 0.10},
                    },
                    f,
                )

            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.0)
            self.assertTrue(_all_time_metadata_requires_selection_refresh(metadata_path, 42))

    def test_all_time_best_metadata_with_stale_candidate_generation_is_ignored(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                        "default_node_feature_dim": DEFAULT_NODE_FEATURE_DIM,
                        "candidate_score_weights": {"mean": 0.6, "min": 0.4, "median": 0.0},
                        "candidate_generation": {
                            "single_swap_repair_seed_score_priority_weight": 0.0,
                            "group_archetype_score_weight": 0.05,
                            "group_archetype_positive_gate": 0.4,
                            "group_archetype_margin_gate": 0.05,
                            "partition_score_mean_weight": 0.6,
                            "partition_score_min_weight": 0.4,
                            "partition_score_median_weight": 0.0,
                            "default_partition_top_n": 200.0,
                            "default_partition_top_k": 20.0,
                            "partition_search_max_states": 5000.0,
                            "default_single_swap_repair_seed_limit": 80.0,
                            "default_single_swap_max_repairs": 80.0,
                        },
                    },
                    f,
                )

            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.0)
            self.assertTrue(_all_time_metadata_requires_selection_refresh(metadata_path, 42))

    def test_selection_score_prioritizes_partition_success_over_mrr(self):
        mrr_only_better = {
            "best_top_k_partition_solved": 16,
            "top_partition_solved": 13,
            "puzzles_with_all_true_groups": 19,
            "true_groups_in_top_candidates": 191,
            "near_miss_3_of_4_candidates": 949,
            "exact_mrr_sum": 0.2058,
            "exact_mrr_count": 1,
        }
        solver_better = {
            "best_top_k_partition_solved": 20,
            "top_partition_solved": 13,
            "puzzles_with_all_true_groups": 22,
            "true_groups_in_top_candidates": 202,
            "near_miss_3_of_4_candidates": 947,
            "exact_mrr_sum": 0.2038,
            "exact_mrr_count": 1,
        }

        self.assertGreater(
            _gcn_selection_score_from_stats(solver_better),
            _gcn_selection_score_from_stats(mrr_only_better),
        )

    def test_all_time_best_metadata_missing_or_mismatched_node_dim_is_ignored(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_path = os.path.join(temp_dir, "gcn_all_time_best.json")

            # Missing default_node_feature_dim
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                    },
                    f,
                )
            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.0)

            # Mismatched default_node_feature_dim
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "validation_mrr": 0.99,
                        "edge_feature_dim": EDGE_FEATURE_DIM,
                        "feature_schema_version": FEATURE_SCHEMA_VERSION,
                        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
                        "default_node_feature_dim": DEFAULT_NODE_FEATURE_DIM + 1,
                    },
                    f,
                )
            self.assertEqual(_load_gcn_all_time_best_mrr(metadata_path), 0.0)


class ValidationArtifactComparisonTests(unittest.TestCase):
    def test_parse_numeric_value(self):
        self.assertEqual(_parse_numeric_value("109"), 109.0)
        self.assertEqual(_parse_numeric_value("85 / 109 (78.0%)"), 78.0)
        self.assertEqual(_parse_numeric_value("0.72 / 4"), 0.72)
        self.assertEqual(_parse_numeric_value("4.73"), 4.73)
        self.assertEqual(_parse_numeric_value("3.0"), 3.0)
        self.assertEqual(_parse_numeric_value("798"), 798.0)
        self.assertIsNone(_parse_numeric_value("no numbers here"))

    def test_format_comparison_higher_is_better(self):
        # Improved
        prev, change = _format_comparison("Validation puzzles", "115", "109")
        self.assertEqual(prev, "109")
        self.assertEqual(change, "🟢 +6 (improved)")

        # Regressed
        prev, change = _format_comparison("Validation puzzles", "105", "109")
        self.assertEqual(prev, "109")
        self.assertEqual(change, "🔴 -4 (regressed)")

        # Unchanged
        prev, change = _format_comparison("Validation puzzles", "109", "109")
        self.assertEqual(prev, "109")
        self.assertEqual(change, "0")

    def test_format_comparison_lower_is_better_rank(self):
        # Improved (lower rank)
        prev, change = _format_comparison("Mean rank of true groups found", "4.50", "4.75")
        self.assertEqual(prev, "4.75")
        self.assertEqual(change, "🟢 -0.25 (improved)")

        # Regressed (higher rank)
        prev, change = _format_comparison("Mean rank of true groups found", "5.10", "4.75")
        self.assertEqual(prev, "4.75")
        self.assertEqual(change, "🔴 +0.35 (regressed)")

    def test_format_comparison_lower_is_better_near_miss(self):
        prev, change = _format_comparison("3-of-4 near-miss candidates in top-20", "850", "873")
        self.assertEqual(prev, "873")
        self.assertEqual(change, "🟢 -23 (improved)")

        prev, change = _format_comparison("3-of-4 near-miss candidates in top-20", "896", "873")
        self.assertEqual(prev, "873")
        self.assertEqual(change, "🔴 +23 (regressed)")

    def test_format_comparison_percentage(self):
        prev, change = _format_comparison(
            "Puzzles with complete partition candidates",
            "85 / 109 (78.0%)",
            "82 / 109 (75.2%)"
        )
        self.assertEqual(prev, "82 / 109 (75.2%)")
        self.assertEqual(change, "🟢 +2.8% (improved)")

    def test_parse_previous_summary(self):
        dummy_content = """# Dummy Header
## Aggregate Summary

| Metric | Current | Previous | Change vs Prev | All-Time Best | Change vs All-Time |
|---|---:|---:|---:|---:|---:|
| Validation puzzles | 109 | 109 | 0 | 109 | 0 |
| Puzzles with complete partition candidates | 85 / 109 (78.0%) | 82 / 109 (75.2%) | 🟢 +2.8% (improved) | 88 / 109 (80.7%) | 🔴 -2.7% (regressed) |
| Mean rank of true groups found in top-20 | 4.73 | 4.88 | 🟢 -0.15 (improved) | 4.50 | 🔴 +0.23 (regressed) |

### Recall By Relation Archetype
...
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "candidates_summary.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(dummy_content)

            parsed = _parse_previous_summary(file_path)
            self.assertEqual(parsed.get("Validation puzzles"), "109")
            self.assertEqual(parsed.get("Puzzles with complete partition candidates"), "85 / 109 (78.0%)")
            self.assertEqual(parsed.get("Mean rank of true groups found in top-20"), "4.73")


if __name__ == "__main__":
    unittest.main()
