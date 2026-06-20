import unittest
import tempfile

import numpy as np

from src.features import (
    DEFAULT_SENTENCE_EMBEDDING_DIM,
    EDGE_FEATURE_DIM,
    INTRINSIC_NODE_METADATA_DIM,
    LENGTH_DISTANCE_DIM,
    LEVENSHTEIN_DISTANCE_DIM,
    NODE_BOARD_AVG_EDGE_WEIGHT_DIM,
    NODE_BOARD_MAX_EDGE_WEIGHT_DIM,
    NODE_BOARD_ST_CENTROID_DISTANCE_DIM,
    NODE_COMPOUND_PREFIX_VALENCE_DIM,
    NODE_COMPOUND_SUFFIX_VALENCE_DIM,
    NODE_HAS_DOUBLE_LETTER_DIM,
    NODE_IS_PALINDROME_DIM,
    NODE_METADATA_DIM,
    FeatureExtractor,
)


class FeatureExtractorTests(unittest.TestCase):
    def test_graph_matrices_include_sentence_embedding_edge_feature(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {
            word.strip().upper(): np.array([1.0, 0.0], dtype=np.float32)
            for word in words
        }

        words = [f"WORD{i}" for i in range(16)]
        node_features, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(node_features.shape, (16, NODE_METADATA_DIM + 2))
        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, 10], 1.0)
        self.assertEqual(edge_features[0, 1, 10], 1.0)

    def test_wordplay_features_include_normalized_levenshtein_distance(self):
        extractor = FeatureExtractor()

        features = extractor.get_wordplay_features("CAT", "CATS")

        self.assertEqual(features["levenshtein_distance"], 0.25)

    def test_graph_matrices_include_levenshtein_edge_feature(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}

        words = ["CAT", "CATS"] + [f"WORD{i}" for i in range(14)]
        node_features, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(
            node_features.shape,
            (16, NODE_METADATA_DIM + DEFAULT_SENTENCE_EMBEDDING_DIM),
        )
        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, 11], 0.0)
        self.assertEqual(edge_features[0, 1, 11], 0.25)
        self.assertEqual(edge_features[1, 0, 11], 0.25)

    def test_node_features_include_palindrome_flags(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.get_compound_fragment_valence = lambda word: (0.0, 0.0)

            for word in ["KAYAK", "LEVEL", "MOM", "RACECAR"]:
                features = extractor.get_word_node_features(word)
                self.assertEqual(features[NODE_IS_PALINDROME_DIM], 1.0)

            features = extractor.get_word_node_features("HAMMER")
            self.assertEqual(features[NODE_IS_PALINDROME_DIM], 0.0)

    def test_node_features_include_double_letter_flags(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.get_compound_fragment_valence = lambda word: (0.0, 0.0)

            book_features = extractor.get_word_node_features("BOOK")
            jazz_features = extractor.get_word_node_features("JAZZ")
            cat_features = extractor.get_word_node_features("CAT")

            self.assertEqual(book_features[NODE_HAS_DOUBLE_LETTER_DIM], 1.0)
            self.assertEqual(jazz_features[NODE_HAS_DOUBLE_LETTER_DIM], 1.0)
            self.assertEqual(cat_features[NODE_HAS_DOUBLE_LETTER_DIM], 0.0)

    def test_node_features_include_compound_valence(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor._compound_prefix_counts = {"surf": 4}
            extractor._compound_suffix_counts = {"board": 2}

            surf_features = extractor.get_word_node_features("SURF")
            board_features = extractor.get_word_node_features("BOARD")

            self.assertGreater(surf_features[NODE_COMPOUND_PREFIX_VALENCE_DIM], 0.0)
            self.assertEqual(surf_features[NODE_COMPOUND_SUFFIX_VALENCE_DIM], 0.0)
            self.assertEqual(board_features[NODE_COMPOUND_PREFIX_VALENCE_DIM], 0.0)
            self.assertGreater(board_features[NODE_COMPOUND_SUFFIX_VALENCE_DIM], 0.0)

    def test_stale_wordnet_single_cache_entry_is_recomputed(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.wordnet_single_cache["KAYAK"] = [0.0] * 7
            extractor.get_compound_fragment_valence = lambda word: (0.0, 0.0)

            features = extractor.get_word_node_features("KAYAK")

            self.assertEqual(len(features), INTRINSIC_NODE_METADATA_DIM)
            self.assertEqual(features[NODE_IS_PALINDROME_DIM], 1.0)
            self.assertEqual(extractor.wordnet_single_cache["KAYAK"], features)

    def test_graph_matrices_include_board_st_centroid_distance(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0

        def embeddings(words):
            result = {}
            for idx, word in enumerate(words):
                if idx < 15:
                    result[word.strip().upper()] = np.array([1.0, 0.0], dtype=np.float32)
                else:
                    result[word.strip().upper()] = np.array([0.0, 1.0], dtype=np.float32)
            return result

        extractor.get_sentence_embeddings = embeddings

        words = [f"WORD{i}" for i in range(16)]
        node_features, _ = extractor.build_graph_matrices(words)

        clustered_distance = node_features[0, NODE_BOARD_ST_CENTROID_DISTANCE_DIM]
        outlier_distance = node_features[15, NODE_BOARD_ST_CENTROID_DISTANCE_DIM]
        self.assertGreater(outlier_distance, clustered_distance)

    def test_graph_matrices_include_static_board_edge_weight_stats(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}

        def wordplay(w1, w2):
            base = {
                "is_anagram": 0.0,
                "shared_prefix": 0.0,
                "shared_suffix": 0.0,
                "is_substring": 0.0,
                "len_diff": 1.0,
                "levenshtein_distance": 1.0,
            }
            if {w1, w2} == {"WORD0", "WORD1"}:
                base["len_diff"] = 0.05
                base["levenshtein_distance"] = 0.20
            elif {w1, w2} == {"WORD0", "WORD2"}:
                base["len_diff"] = 0.20
                base["levenshtein_distance"] = 0.30
            return base

        extractor.get_wordplay_features = wordplay

        words = [f"WORD{i}" for i in range(16)]
        node_features, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(edge_features[0, 1, LENGTH_DISTANCE_DIM], 0.05)
        self.assertEqual(edge_features[0, 1, LEVENSHTEIN_DISTANCE_DIM], 0.20)
        expected_avg = (0.95 + 0.80) / (15 * EDGE_FEATURE_DIM)
        self.assertAlmostEqual(
            node_features[0, NODE_BOARD_AVG_EDGE_WEIGHT_DIM],
            expected_avg,
            places=6,
        )
        self.assertAlmostEqual(
            node_features[0, NODE_BOARD_MAX_EDGE_WEIGHT_DIM],
            0.95,
            places=6,
        )
        self.assertEqual(node_features[3, NODE_BOARD_AVG_EDGE_WEIGHT_DIM], 0.0)
        self.assertEqual(node_features[3, NODE_BOARD_MAX_EDGE_WEIGHT_DIM], 0.0)

    def test_clue_similarity_uses_tfidf_descriptions(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.clue_cache = {
                "APPLE": "fruit tree orchard crisp",
                "PEAR": "fruit tree orchard soft",
                "HAMMER": "tool nail construction",
            }
            extractor._init_clue_tfidf()

            similarity = extractor.get_clue_similarity("APPLE", "PEAR")

            self.assertIsInstance(similarity, float)
            self.assertGreater(similarity, 0.0)

    def test_clue_similarity_returns_zero_for_missing_words(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.clue_cache = {
                "APPLE": "fruit tree orchard crisp",
                "PEAR": "fruit tree orchard soft",
            }
            extractor._init_clue_tfidf()

            self.assertEqual(extractor.get_clue_similarity("APPLE", "MISSING"), 0.0)


if __name__ == "__main__":
    unittest.main()
