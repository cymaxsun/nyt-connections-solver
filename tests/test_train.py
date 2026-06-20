import os
import tempfile
import unittest

import numpy as np
import torch

from src.features import EDGE_FEATURE_DIM, FEATURE_SCHEMA_VERSION
from src.train import (
    _preprocessed_features_are_current,
    _preserve_existing_artifact,
    _save_gcn_best_checkpoint,
)


class PreprocessedFeatureCompatibilityTests(unittest.TestCase):
    def test_current_schema_and_edge_dim_matches(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION,
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
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))

    def test_wrong_edge_feature_dim_is_stale(self):
        puzzles = [{
            "feature_schema_version": FEATURE_SCHEMA_VERSION,
            "edge_features": np.zeros((16, 16, EDGE_FEATURE_DIM + 1), dtype=np.float32),
        }]

        self.assertFalse(_preprocessed_features_are_current(puzzles))


class GCNCheckpointTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
