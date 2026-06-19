import unittest

import numpy as np

from src.features import EDGE_FEATURE_DIM, FeatureExtractor


class FeatureExtractorTests(unittest.TestCase):
    def test_graph_matrices_include_sentence_embedding_edge_feature(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * 7
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {
            word.strip().upper(): np.array([1.0, 0.0], dtype=np.float32)
            for word in words
        }

        words = [f"WORD{i}" for i in range(16)]
        node_features, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(node_features.shape, (16, 7))
        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, 10], 1.0)
        self.assertEqual(edge_features[0, 1, 10], 1.0)


if __name__ == "__main__":
    unittest.main()
