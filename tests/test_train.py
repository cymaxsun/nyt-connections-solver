import unittest

import numpy as np

from src.features import EDGE_FEATURE_DIM, FEATURE_SCHEMA_VERSION
from src.train import _preprocessed_features_are_current


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


if __name__ == "__main__":
    unittest.main()
