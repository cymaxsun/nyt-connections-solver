import unittest
import tempfile

import numpy as np

from src.features import (
    DEFAULT_SENTENCE_EMBEDDING_DIM,
    CN_DERIVED_FROM_DIM,
    CN_DISTINCT_FROM_DIM,
    CN_ETYMOLOGICAL_DIM,
    CN_HAS_CONTEXT_DIM,
    CN_IS_A_DIM,
    CN_RELATED_TO_DIM,
    CN_RESIDUAL_BACKWARD_DIM,
    CN_RESIDUAL_FORWARD_DIM,
    CN_SYNONYM_DIM,
    COMPOUND_FRAGMENT_SHARED_DIM,
    CONCATENATED_COMPLETION_DIM,
    EDGE_FEATURE_DIM,
    INTRINSIC_NODE_METADATA_DIM,
    LENGTH_DISTANCE_DIM,
    LEVENSHTEIN_DISTANCE_DIM,
    NODE_BOARD_AVG_EDGE_WEIGHT_DIM,
    NODE_BOARD_MAX_EDGE_WEIGHT_DIM,
    NODE_BOARD_ST_CENTROID_DISTANCE_DIM,
    NODE_COMPOUND_PREFIX_VALENCE_DIM,
    NODE_COMPOUND_SUFFIX_VALENCE_DIM,
    NODE_CONCEPTNET_IS_A_COUNT_DIM,
    NODE_HAS_ADVERB_POS_DIM,
    NODE_HAS_DOUBLE_LETTER_DIM,
    NODE_IS_PALINDROME_DIM,
    NODE_METADATA_DIM,
    NODE_WORD_FREQUENCY_DIM,
    NODE_WORDNET_DOMAIN_START_DIM,
    NODE_WORDNET_MAX_DEPTH_DIM,
    SENTENCE_SIMILARITY_DIM,
    FeatureExtractor,
    WORDNET_DOMAIN_TAG_DIM,
    PHONEME_EDIT_DISTANCE_DIM,
    RHYME_MATCH_DIM,
    SOUNDEX_MATCH_DIM,
    METAPHONE_MATCH_DIM,
    PHONEME_OVERLAP_DIM,
)


class FeatureExtractorTests(unittest.TestCase):
    def _stub_expensive_node_features(self, extractor):
        extractor.get_compound_fragment_valence = lambda word: (0.0, 0.0)
        extractor.get_conceptnet_is_a_count = lambda word: 0.0
        extractor.get_word_frequency = lambda word: 0.0

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
        self.assertEqual(edge_features[0, 0, SENTENCE_SIMILARITY_DIM], 1.0)
        self.assertEqual(edge_features[0, 1, SENTENCE_SIMILARITY_DIM], 1.0)

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
        self.assertEqual(edge_features[0, 0, LEVENSHTEIN_DISTANCE_DIM], 0.0)
        self.assertEqual(edge_features[0, 1, LEVENSHTEIN_DISTANCE_DIM], 0.25)
        self.assertEqual(edge_features[1, 0, LEVENSHTEIN_DISTANCE_DIM], 0.25)

    def test_graph_matrices_include_ngram_compound_shared_edge_feature(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}
        extractor.ngram_compound_cache["profiles"] = {
            "surf": {"left": {}, "right": {"board": 1.0}},
            "skate": {"left": {}, "right": {"board": 0.75}},
        }

        words = ["SURF", "SKATE"] + [f"WORD{i}" for i in range(14)]
        _, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, COMPOUND_FRAGMENT_SHARED_DIM], 1.0)
        self.assertEqual(edge_features[0, 1, COMPOUND_FRAGMENT_SHARED_DIM], 0.75)
        self.assertEqual(edge_features[1, 0, COMPOUND_FRAGMENT_SHARED_DIM], 0.75)

    def test_concatenated_completion_score_finds_shared_right_completion(self):
        extractor = FeatureExtractor()

        for w1, w2 in [
            ("A", "CAPRI"),
            ("A", "POP"),
            ("A", "UNI"),
            ("CAPRI", "POP"),
            ("CAPRI", "UNI"),
            ("POP", "UNI"),
        ]:
            self.assertEqual(extractor.get_concatenated_completion_score(w1, w2), 1.0)

    def test_concatenated_completion_score_keeps_directions_separate(self):
        extractor = FeatureExtractor()
        extractor._concat_right_completions_by_fragment = {
            "red": {"wood"},
            "blue": {"bird"},
        }
        extractor._concat_left_completions_by_fragment = {
            "red": {"blue"},
            "blue": {"black"},
        }

        self.assertEqual(extractor.get_concatenated_completion_score("RED", "BLUE"), 0.0)

    def test_concatenated_completion_score_finds_shared_left_completion(self):
        extractor = FeatureExtractor()
        extractor._concat_right_completions_by_fragment = {}
        extractor._concat_left_completions_by_fragment = {
            "one": {"stone"},
            "age": {"stone"},
        }

        self.assertEqual(extractor.get_concatenated_completion_score("ONE", "AGE"), 1.0)

    def test_concatenated_completion_map_ignores_short_hidden_completion(self):
        original_right = FeatureExtractor._SHARED_CONCAT_RIGHT_COMPLETIONS_BY_FRAGMENT
        original_left = FeatureExtractor._SHARED_CONCAT_LEFT_COMPLETIONS_BY_FRAGMENT
        try:
            FeatureExtractor._SHARED_CONCAT_RIGHT_COMPLETIONS_BY_FRAGMENT = None
            FeatureExtractor._SHARED_CONCAT_LEFT_COMPLETIONS_BY_FRAGMENT = None
            extractor = FeatureExtractor()
            extractor._build_concatenated_completion_maps()

            self.assertNotIn(
                "le",
                extractor._concat_right_completions_by_fragment.get("app", set()),
            )
        finally:
            FeatureExtractor._SHARED_CONCAT_RIGHT_COMPLETIONS_BY_FRAGMENT = original_right
            FeatureExtractor._SHARED_CONCAT_LEFT_COMPLETIONS_BY_FRAGMENT = original_left

    def test_graph_matrices_include_concatenated_completion_edge_feature(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}
        extractor.get_ngram_compound_shared_score = lambda w1, w2: 0.0
        extractor._concat_right_completions_by_fragment = {
            "a": {"corn"},
            "capri": {"corn"},
        }
        extractor._concat_left_completions_by_fragment = {}

        words = ["A", "CAPRI"] + [f"WORD{i}" for i in range(14)]
        _, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, CONCATENATED_COMPLETION_DIM], 1.0)
        self.assertEqual(edge_features[0, 1, CONCATENATED_COMPLETION_DIM], 1.0)
        self.assertEqual(edge_features[1, 0, CONCATENATED_COMPLETION_DIM], 1.0)

    def test_graph_matrices_decompose_conceptnet_relation_types(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}
        relation_map = {
            "cat": [
                {
                    "rel": "http://conceptnet.io/r/IsA",
                    "start": "cat",
                    "end": "animal",
                    "weight": 2.0,
                },
                {
                    "rel": "http://conceptnet.io/r/Synonym",
                    "start": "cat",
                    "end": "feline",
                    "weight": 1.5,
                },
                {
                    "rel": "http://conceptnet.io/r/HasContext",
                    "start": "cat",
                    "end": "zoology",
                    "weight": 1.0,
                },
                {
                    "rel": "http://conceptnet.io/r/AtLocation",
                    "start": "cat",
                    "end": "home",
                    "weight": 1.2,
                },
            ],
            "animal": [
                {
                    "rel": "http://conceptnet.io/r/RelatedTo",
                    "start": "animal",
                    "end": "cat",
                    "weight": 0.8,
                },
                {
                    "rel": "http://conceptnet.io/r/HasContext",
                    "start": "animal",
                    "end": "zoology",
                    "weight": 1.0,
                },
                {
                    "rel": "http://conceptnet.io/r/AtLocation",
                    "start": "animal",
                    "end": "cat",
                    "weight": 0.6,
                },
            ],
            "home": [],
            "feline": [
                {
                    "rel": "http://conceptnet.io/r/FormOf",
                    "start": "feline",
                    "end": "cat",
                    "weight": 0.7,
                },
                {
                    "rel": "http://conceptnet.io/r/EtymologicallyRelatedTo",
                    "start": "feline",
                    "end": "cat",
                    "weight": 0.4,
                },
                {
                    "rel": "http://conceptnet.io/r/DistinctFrom",
                    "start": "feline",
                    "end": "canine",
                    "weight": 0.9,
                },
            ],
        }
        extractor.query_conceptnet = lambda word: relation_map.get(word.lower(), [])

        words = ["CAT", "ANIMAL", "FELINE", "CANINE", "HOME"] + [f"WORD{i}" for i in range(11)]
        _, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(edge_features[0, 1, CN_IS_A_DIM], 2.0)
        self.assertEqual(edge_features[0, 1, CN_RELATED_TO_DIM], 0.8)
        self.assertEqual(edge_features[0, 1, CN_HAS_CONTEXT_DIM], 1.0)
        self.assertEqual(edge_features[0, 1, CN_RESIDUAL_FORWARD_DIM], 0.0)
        self.assertEqual(edge_features[0, 1, CN_RESIDUAL_BACKWARD_DIM], 0.6)
        self.assertEqual(edge_features[0, 2, CN_SYNONYM_DIM], 1.5)
        self.assertEqual(edge_features[0, 2, CN_DERIVED_FROM_DIM], 0.7)
        self.assertEqual(edge_features[0, 2, CN_ETYMOLOGICAL_DIM], 0.4)
        self.assertEqual(edge_features[2, 3, CN_DISTINCT_FROM_DIM], 0.9)
        self.assertEqual(edge_features[0, 4, CN_RESIDUAL_FORWARD_DIM], 1.2)
        self.assertEqual(edge_features[0, 4, CN_RESIDUAL_BACKWARD_DIM], 0.0)

    def test_node_features_include_palindrome_flags(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            self._stub_expensive_node_features(extractor)

            for word in ["KAYAK", "LEVEL", "MOM", "RACECAR"]:
                features = extractor.get_word_node_features(word)
                self.assertEqual(features[NODE_IS_PALINDROME_DIM], 1.0)

            features = extractor.get_word_node_features("HAMMER")
            self.assertEqual(features[NODE_IS_PALINDROME_DIM], 0.0)

    def test_node_features_include_double_letter_flags(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            self._stub_expensive_node_features(extractor)

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
            extractor.get_conceptnet_is_a_count = lambda word: 0.0
            extractor.get_word_frequency = lambda word: 0.0

            surf_features = extractor.get_word_node_features("SURF")
            board_features = extractor.get_word_node_features("BOARD")

            self.assertGreater(surf_features[NODE_COMPOUND_PREFIX_VALENCE_DIM], 0.0)
            self.assertEqual(surf_features[NODE_COMPOUND_SUFFIX_VALENCE_DIM], 0.0)
            self.assertEqual(board_features[NODE_COMPOUND_PREFIX_VALENCE_DIM], 0.0)
            self.assertGreater(board_features[NODE_COMPOUND_SUFFIX_VALENCE_DIM], 0.0)

    def test_ngram_compound_shared_score_uses_shared_completion(self):
        def ngram_client(query):
            return {
                "surf *": [{"ngram": "surf board", "timeseries": [0.2]}],
                "skate *": [{"ngram": "skate board", "timeseries": [0.3]}],
                "* surf": [{"ngram": "wind surf", "timeseries": [0.1]}],
                "* skate": [{"ngram": "ice skate", "timeseries": [0.1]}],
            }.get(query, [])

        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(
                cache_dir=cache_dir,
                ngram_live_lookup=True,
                ngram_client=ngram_client,
            )

            score = extractor.get_ngram_compound_shared_score("SURF", "SKATE")

            self.assertGreater(score, 0.0)
            self.assertLessEqual(score, 1.0)

    def test_ngram_compound_shared_score_returns_zero_for_unrelated_profiles(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.ngram_compound_cache["profiles"] = {
                "surf": {"left": {}, "right": {"board": 1.0}},
                "apple": {"left": {}, "right": {"pie": 1.0}},
            }

            score = extractor.get_ngram_compound_shared_score("SURF", "APPLE")

            self.assertEqual(score, 0.0)

    def test_ngram_compound_profile_cache_avoids_live_lookup(self):
        calls = []

        def ngram_client(query):
            calls.append(query)
            return [{"ngram": "surf board", "timeseries": [0.2]}]

        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(
                cache_dir=cache_dir,
                ngram_live_lookup=True,
                ngram_client=ngram_client,
            )
            profile = extractor.get_ngram_compound_profile("SURF")
            self.assertIn("board", profile["right"])
            self.assertEqual(len(calls), 2)

            extractor.ngram_client = lambda query: self.fail("cache hit should not query live client")
            cached_profile = extractor.get_ngram_compound_profile("SURF")
            self.assertEqual(cached_profile, profile)

    def test_ngram_compound_cache_miss_is_zero_without_live_lookup(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(
                cache_dir=cache_dir,
                ngram_live_lookup=False,
                ngram_client=lambda query: self.fail("cache-only mode should not query live client"),
            )

            profile = extractor.get_ngram_compound_profile("MISSING")

            self.assertEqual(profile, {"left": {}, "right": {}})

    def test_ngram_compound_completion_filter_rejects_function_words(self):
        self.assertIsNone(
            FeatureExtractor._extract_ngram_completion("surf the", "surf", "right")
        )
        self.assertIsNone(
            FeatureExtractor._extract_ngram_completion("and surf", "surf", "left")
        )

    def test_ngram_compound_completion_filter_keeps_phrasal_particles(self):
        self.assertEqual(
            FeatureExtractor._extract_ngram_completion("dress up", "dress", "right"),
            "up",
        )
        self.assertEqual(
            FeatureExtractor._extract_ngram_completion("log on", "log", "right"),
            "on",
        )
        self.assertEqual(
            FeatureExtractor._extract_ngram_completion("tune in", "tune", "right"),
            "in",
        )
        self.assertEqual(
            FeatureExtractor._extract_ngram_completion("take off", "take", "right"),
            "off",
        )

    def test_stale_wordnet_single_cache_entry_is_recomputed(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.wordnet_single_cache["KAYAK"] = [0.0] * 7
            self._stub_expensive_node_features(extractor)

            features = extractor.get_word_node_features("KAYAK")

            self.assertEqual(len(features), INTRINSIC_NODE_METADATA_DIM)
            self.assertEqual(features[NODE_IS_PALINDROME_DIM], 1.0)
            self.assertEqual(extractor.wordnet_single_cache["KAYAK"], features)

    def test_node_features_include_adverb_pos(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            self._stub_expensive_node_features(extractor)

            features = extractor.get_word_node_features("QUICKLY")

            self.assertEqual(features[NODE_HAS_ADVERB_POS_DIM], 1.0)

    def test_node_features_include_wordnet_max_depth(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            self._stub_expensive_node_features(extractor)

            features = extractor.get_word_node_features("DOG")

            self.assertGreater(features[NODE_WORDNET_MAX_DEPTH_DIM], 0.0)
            self.assertLessEqual(features[NODE_WORDNET_MAX_DEPTH_DIM], 1.0)

    def test_conceptnet_is_a_count_uses_offline_relations(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.conceptnet_cache["cat"] = [
                {
                    "rel": "http://conceptnet.io/r/IsA",
                    "start": "cat",
                    "end": "animal",
                    "weight": 1.0,
                },
                {
                    "rel": "http://conceptnet.io/r/IsA",
                    "start": "cat",
                    "end": "pet",
                    "weight": 1.0,
                },
            ]

            feature = extractor.get_conceptnet_is_a_count("CAT")

            self.assertGreater(feature, 0.0)
            self.assertLessEqual(feature, 1.0)

    def test_word_frequency_uses_wordfreq_lookup_and_defaults_to_zero(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.word_frequency_lookup = lambda word, lang: 4.0

            self.assertEqual(extractor.get_word_frequency("CAT"), 0.5)

            extractor.word_frequency_lookup = None
            self.assertEqual(extractor.get_word_frequency("CAT"), 0.0)

    def test_node_features_include_wordnet_domain_vector(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            self._stub_expensive_node_features(extractor)

            features = extractor.get_word_node_features("DOG")
            domain_features = features[
                NODE_WORDNET_DOMAIN_START_DIM:
                NODE_WORDNET_DOMAIN_START_DIM + WORDNET_DOMAIN_TAG_DIM
            ]

            self.assertEqual(len(domain_features), WORDNET_DOMAIN_TAG_DIM)
            self.assertGreater(sum(domain_features), 0.0)

    def test_node_features_include_word_frequency_slot(self):
        with tempfile.TemporaryDirectory() as cache_dir:
            extractor = FeatureExtractor(cache_dir=cache_dir)
            extractor.get_compound_fragment_valence = lambda word: (0.0, 0.0)
            extractor.get_conceptnet_is_a_count = lambda word: 0.0
            extractor.get_word_frequency = lambda word: 0.75

            features = extractor.get_word_node_features("CAT")

            self.assertEqual(features[NODE_WORD_FREQUENCY_DIM], 0.75)
            self.assertEqual(features[NODE_CONCEPTNET_IS_A_COUNT_DIM], 0.0)

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
        extractor.get_soundex = lambda word: word
        extractor.get_metaphone = lambda word: word
        extractor.get_ngram_compound_shared_score = lambda w1, w2: 0.0
        extractor.get_concatenated_completion_score = lambda w1, w2: 0.0

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

    def test_phonetic_helpers_and_features(self):
        extractor = FeatureExtractor()

        # Test Soundex
        self.assertEqual(extractor.get_soundex("hail"), "H400")
        self.assertEqual(extractor.get_soundex("hale"), "H400")
        self.assertEqual(extractor.get_soundex("rain"), "R500")

        # Test Metaphone (via jellyfish)
        self.assertEqual(extractor.get_metaphone("hail"), "HL")
        self.assertEqual(extractor.get_metaphone("hale"), "HL")

        # Test phonemes extract
        p_hail = extractor.get_phonemes("hail")
        p_rail = extractor.get_phonemes("rail")
        p_rain = extractor.get_phonemes("rain")

        if p_hail and p_rail:
            # Rhyme extract
            self.assertEqual(extractor._extract_rhyme_part(p_hail), extractor._extract_rhyme_part(p_rail))
            self.assertNotEqual(extractor._extract_rhyme_part(p_hail), extractor._extract_rhyme_part(p_rain))

            # Edit distance
            dist_hail_rail = extractor._normalized_phoneme_edit_distance(p_hail, p_rail)
            dist_hail_rain = extractor._normalized_phoneme_edit_distance(p_hail, p_rain)
            self.assertLess(dist_hail_rail, dist_hail_rain)

            # Overlap ratio
            self.assertGreater(extractor._phoneme_overlap_ratio(p_hail, p_rail), 0.0)

    def test_graph_matrices_include_phonetic_edge_features(self):
        extractor = FeatureExtractor()
        extractor.get_word_node_features = lambda word: [0.0] * INTRINSIC_NODE_METADATA_DIM
        extractor.query_conceptnet = lambda word: []
        extractor.extract_wordnet_features = lambda w1, w2: (0.0, 0.0)
        extractor.get_clue_similarity = lambda w1, w2: 0.0
        extractor.get_sentence_embeddings = lambda words: {}

        words = ["HAIL", "RAIL"] + [f"WORD{i}" for i in range(14)]
        node_features, edge_features = extractor.build_graph_matrices(words)

        self.assertEqual(edge_features.shape, (16, 16, EDGE_FEATURE_DIM))
        self.assertEqual(edge_features[0, 0, RHYME_MATCH_DIM], 1.0)
        self.assertEqual(edge_features[0, 1, RHYME_MATCH_DIM], 1.0)
        self.assertEqual(edge_features[0, 0, SOUNDEX_MATCH_DIM], 1.0)
        self.assertEqual(edge_features[0, 0, METAPHONE_MATCH_DIM], 1.0)
        self.assertEqual(edge_features[0, 0, PHONEME_OVERLAP_DIM], 1.0)
        self.assertEqual(edge_features[0, 0, PHONEME_EDIT_DISTANCE_DIM], 0.0)



if __name__ == "__main__":
    unittest.main()
