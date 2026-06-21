import os
import re
import json
import urllib.request
import urllib.parse
import sqlite3
from collections import Counter, defaultdict
import numpy as np
from typing import List, Dict, Tuple, Set, Any, Optional
import nltk
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import jellyfish

try:
    from wordfreq import zipf_frequency
except Exception:
    zipf_frequency = None

# Ensure NLTK data directories exist
nltk_data_dir = os.path.expanduser("~/.cache/nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
if nltk_data_dir not in nltk.data.path:
    nltk.data.path.append(nltk_data_dir)

# Ensure WordNet is loaded
try:
    wn.ensure_loaded()
except Exception:
    nltk.download('wordnet', download_dir=nltk_data_dir, quiet=True)
    nltk.download('omw-1.4', download_dir=nltk_data_dir, quiet=True)

# Ensure CMUDict is loaded
try:
    from nltk.corpus import cmudict
    try:
        CMU_DICT = cmudict.dict()
    except Exception:
        nltk.download('cmudict', download_dir=nltk_data_dir, quiet=True)
        CMU_DICT = cmudict.dict()
except Exception as e:
    print(f"Warning: Failed to load CMUDict: {e}")
    CMU_DICT = {}

EDGE_FEATURE_DIM = 25
FEATURE_SCHEMA_VERSION = 13
NGRAM_COMPOUND_CACHE_SCHEMA_VERSION = 1
NGRAMS_DEV_COMPOUND_CACHE_SCHEMA_VERSION = 2
NGRAM_COMPOUND_CORPUS = "eng_2019"
NGRAM_COMPOUND_YEAR_START = 1980
NGRAM_COMPOUND_YEAR_END = 2019
NGRAM_COMPOUND_SMOOTHING = 0
BASE_NODE_METADATA_DIM = 7
WORDNET_DOMAIN_TAGS = (
    "adj.all",
    "adj.pert",
    "adv.all",
    "noun.Tops",
    "noun.act",
    "noun.animal",
    "noun.artifact",
    "noun.attribute",
    "noun.body",
    "noun.cognition",
    "noun.communication",
    "noun.event",
    "noun.feeling",
    "noun.food",
    "noun.group",
    "noun.location",
    "noun.motive",
    "noun.object",
    "noun.person",
    "noun.phenomenon",
    "noun.plant",
    "noun.possession",
    "noun.process",
    "noun.quantity",
    "noun.relation",
    "noun.shape",
    "noun.state",
    "noun.substance",
    "noun.time",
    "verb.body",
    "verb.change",
    "verb.cognition",
    "verb.communication",
    "verb.competition",
    "verb.consumption",
    "verb.contact",
    "verb.creation",
    "verb.emotion",
    "verb.motion",
    "verb.perception",
    "verb.possession",
    "verb.social",
    "verb.stative",
    "verb.weather",
)
WORDNET_DOMAIN_TAG_DIM = len(WORDNET_DOMAIN_TAGS)
INTRINSIC_NODE_METADATA_DIM = 15 + WORDNET_DOMAIN_TAG_DIM
NODE_METADATA_DIM = INTRINSIC_NODE_METADATA_DIM + 3
NODE_IS_PALINDROME_DIM = 7
NODE_HAS_DOUBLE_LETTER_DIM = 8
NODE_COMPOUND_PREFIX_VALENCE_DIM = 9
NODE_COMPOUND_SUFFIX_VALENCE_DIM = 10
NODE_HAS_ADVERB_POS_DIM = 11
NODE_WORDNET_MAX_DEPTH_DIM = 12
NODE_CONCEPTNET_IS_A_COUNT_DIM = 13
NODE_WORD_FREQUENCY_DIM = 14
NODE_WORDNET_DOMAIN_START_DIM = 15
NODE_BOARD_ST_CENTROID_DISTANCE_DIM = INTRINSIC_NODE_METADATA_DIM
NODE_BOARD_AVG_EDGE_WEIGHT_DIM = INTRINSIC_NODE_METADATA_DIM + 1
NODE_BOARD_MAX_EDGE_WEIGHT_DIM = INTRINSIC_NODE_METADATA_DIM + 2
DEFAULT_SENTENCE_EMBEDDING_DIM = 768
DEFAULT_NODE_FEATURE_DIM = NODE_METADATA_DIM + DEFAULT_SENTENCE_EMBEDDING_DIM
SENTENCE_EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

WORDNET_PATH_SIM_DIM = 0
WORDNET_SHARED_HYPERNYM_DIM = 1
CN_IS_A_DIM = 2
CN_SYNONYM_DIM = 3
CN_RELATED_TO_DIM = 4
CN_HAS_CONTEXT_DIM = 5
CN_DERIVED_FROM_DIM = 6
CN_ETYMOLOGICAL_DIM = 7
CN_DISTINCT_FROM_DIM = 8
CN_RESIDUAL_FORWARD_DIM = 9
CN_RESIDUAL_BACKWARD_DIM = 10
CLUE_SIMILARITY_DIM = 11
IS_ANAGRAM_DIM = 12
SHARED_PREFIX_DIM = 13
SHARED_SUFFIX_DIM = 14
IS_SUBSTRING_DIM = 15
LENGTH_DISTANCE_DIM = 16
SENTENCE_SIMILARITY_DIM = 17
LEVENSHTEIN_DISTANCE_DIM = 18
PHONEME_EDIT_DISTANCE_DIM = 19
RHYME_MATCH_DIM = 20
SOUNDEX_MATCH_DIM = 21
METAPHONE_MATCH_DIM = 22
PHONEME_OVERLAP_DIM = 23
COMPOUND_FRAGMENT_SHARED_DIM = 24
CONCEPTNET_RELATION_FEATURES = (
    ("cn_is_a_weight", ("IsA",)),
    ("cn_synonym_weight", ("Synonym",)),
    ("cn_related_to_weight", ("RelatedTo",)),
    ("cn_has_context_match", ("HasContext",)),
    ("cn_derived_from_weight", ("DerivedFrom", "FormOf")),
    ("cn_etymological_weight", ("EtymologicallyRelatedTo",)),
    ("cn_distinct_from_weight", ("DistinctFrom",)),
)
DISABLED_CONCEPTNET_RELATION_FEATURE_IDXS = set()
CONCEPTNET_DIRECT_RELATION_FEATURES = tuple(
    (idx, rel_names)
    for idx, (_, rel_names) in enumerate(CONCEPTNET_RELATION_FEATURES)
    if "HasContext" not in rel_names
    and idx not in DISABLED_CONCEPTNET_RELATION_FEATURE_IDXS
)
CONCEPTNET_HAS_CONTEXT_FEATURE_IDX = 3
CONCEPTNET_COVERED_RELATION_NAMES = {
    relation_name
    for _, relation_names in CONCEPTNET_RELATION_FEATURES
    for relation_name in relation_names
}
WORDNET_PATH_SIMILARITY_THRESHOLD = 0.15
CLUE_SIMILARITY_THRESHOLD = 0.10
LENGTH_SIMILARITY_THRESHOLD = 0.90
SENTENCE_SIMILARITY_THRESHOLD = 0.25
LEVENSHTEIN_SIMILARITY_THRESHOLD = 0.75
PHONEME_EDIT_DISTANCE_THRESHOLD = 0.70
PHONEME_OVERLAP_THRESHOLD = 0.60
COMPOUND_FRAGMENT_SHARED_THRESHOLD = 0.25

EDGE_FEATURE_NAMES = [
    "wordnet_path_similarity",
    "wordnet_shared_hypernyms",
    "conceptnet_isa",
    "conceptnet_synonym",
    "conceptnet_related_to",
    "conceptnet_has_context",
    "conceptnet_derived_from",
    "conceptnet_etymologically_related_to",
    "conceptnet_distinct_from",
    "conceptnet_residual_forward",
    "conceptnet_residual_backward",
    "clue_similarity",
    "is_anagram",
    "shared_prefix",
    "shared_suffix",
    "is_substring",
    "length_distance",
    "sentence_similarity",
    "levenshtein_distance",
    "phoneme_edit_distance",
    "rhyme_match",
    "soundex_match",
    "metaphone_match",
    "phoneme_overlap",
    "compound_fragment_shared",
]


# Ensure WordNet is downloaded
try:
    # Set nltk data path to a folder in the workspace to make it local and persistent
    nltk_data_dir = os.path.expanduser("~/.cache/nltk_data")
    os.makedirs(nltk_data_dir, exist_ok=True)
    nltk.data.path.append(nltk_data_dir)
    wn.ensure_loaded()
except Exception:
    nltk.download('wordnet', download_dir=nltk_data_dir, quiet=True)
    nltk.download('omw-1.4', download_dir=nltk_data_dir, quiet=True)

class FeatureExtractor:
    def __init__(
        self,
        cache_dir: str = None,
        ngram_live_lookup: bool = False,
        ngram_client: Optional[Any] = None,
    ):
        if cache_dir is None:
            cache_dir = os.path.join(os.path.dirname(__file__), "../data")
        os.makedirs(cache_dir, exist_ok=True)

        self.conceptnet_cache_path = os.path.join(cache_dir, "conceptnet_cache.json")
        self.clue_cache_path = os.path.join(cache_dir, "llm_context_cache.json")
        self.embedding_cache_path = os.path.join(cache_dir, "sentence_embedding_cache.json")
        self.ngram_compound_cache_path = os.path.join(cache_dir, "google_ngram_compound_cache.json")

        # Load caches
        self.conceptnet_cache = self._load_json_cache(self.conceptnet_cache_path)
        self.clue_cache = self._load_json_cache(self.clue_cache_path)
        self.embedding_cache = self._load_json_cache(self.embedding_cache_path)
        self.ngram_compound_cache = self._load_ngram_compound_cache()

        # Setup Clue TF-IDF if cache exists
        self.tfidf_vectorizer = None
        self.tfidf_matrix = None
        self.clue_words_list = []
        self._init_clue_tfidf()

        # WordNet caches for performance
        self.wordnet_cache_path = os.path.join(cache_dir, "wordnet_cache.json")
        wordnet_data = self._load_json_cache(self.wordnet_cache_path)

        self.wordnet_pair_cache = {}
        for k, v in wordnet_data.get("pairs", {}).items():
            words_key = tuple(k.split(","))
            self.wordnet_pair_cache[words_key] = tuple(v)

        self.wordnet_single_cache = wordnet_data.get("singles", {})
        self.conceptnet_offline = False
        self.db_conn = None
        self.embedding_model = None
        self.embedding_model_failed = False
        self.embedding_cache_dirty = False
        self._compound_prefix_counts = None
        self._compound_suffix_counts = None
        self.word_frequency_lookup = zipf_frequency
        self.ngram_live_lookup = ngram_live_lookup
        self.ngram_client = ngram_client
        self.ngram_cache_dirty = False

    def _load_json_cache(self, path: str) -> Dict[str, Any]:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    @staticmethod
    def _ngram_compound_cache_metadata() -> Dict[str, Any]:
        return {
            "schema_version": NGRAM_COMPOUND_CACHE_SCHEMA_VERSION,
            "corpus": NGRAM_COMPOUND_CORPUS,
            "year_start": NGRAM_COMPOUND_YEAR_START,
            "year_end": NGRAM_COMPOUND_YEAR_END,
            "smoothing": NGRAM_COMPOUND_SMOOTHING,
            "case_insensitive": True,
        }

    def _load_ngram_compound_cache(self) -> Dict[str, Any]:
        data = self._load_json_cache(self.ngram_compound_cache_path)
        metadata = self._ngram_compound_cache_metadata()
        profiles = data.get("profiles")
        if not isinstance(profiles, dict):
            return {"metadata": metadata, "profiles": {}}

        cache_metadata = data.get("metadata")
        if cache_metadata == metadata:
            return data
        if self._is_ngram_dev_compound_cache_metadata(cache_metadata):
            return data

        return {"metadata": metadata, "profiles": {}}

    @staticmethod
    def _is_ngram_dev_compound_cache_metadata(metadata: Any) -> bool:
        return (
            isinstance(metadata, dict)
            and metadata.get("schema_version") == NGRAMS_DEV_COMPOUND_CACHE_SCHEMA_VERSION
            and metadata.get("source") == "ngrams.dev/search"
            and metadata.get("corpus") == "eng"
        )

    def _save_conceptnet_cache(self):
        try:
            with open(self.conceptnet_cache_path, 'w') as f:
                json.dump(self.conceptnet_cache, f, indent=2)
        except Exception as e:
            print(f"Warning: Failed to save ConceptNet cache: {e}")

    def _save_wordnet_cache(self):
        try:
            serializable_pairs = {f"{k[0]},{k[1]}": list(v) for k, v in self.wordnet_pair_cache.items()}
            data = {
                "pairs": serializable_pairs,
                "singles": self.wordnet_single_cache
            }
            with open(self.wordnet_cache_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Failed to save WordNet cache: {e}")

    def _save_embedding_cache(self):
        try:
            with open(self.embedding_cache_path, 'w') as f:
                json.dump(self.embedding_cache, f)
        except Exception as e:
            print(f"Warning: Failed to save sentence embedding cache: {e}")

    def _save_ngram_compound_cache(self):
        try:
            with open(self.ngram_compound_cache_path, 'w') as f:
                json.dump(self.ngram_compound_cache, f, indent=2, sort_keys=True)
            self.ngram_cache_dirty = False
        except Exception as e:
            print(f"Warning: Failed to save Google Ngram compound cache: {e}")

    def _init_clue_tfidf(self):
        if not self.clue_cache:
            return

        self.clue_words_list = list(self.clue_cache.keys())
        descriptions = [self.clue_cache[w] for w in self.clue_words_list]

        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(descriptions)

        # O(1) lookup maps
        self.clue_words_index_map = {w: idx for idx, w in enumerate(self.clue_words_list)}
        self.clue_sim_cache = {}

    def get_clue_similarity(self, w1: str, w2: str) -> float:
        """Calculate TF-IDF similarity between descriptions of two words in the clue cache."""
        if not self.clue_cache or self.tfidf_matrix is None:
            return 0.0

        w1_clean = w1.strip().upper()
        w2_clean = w2.strip().upper()

        key = tuple(sorted([w1_clean, w2_clean]))
        if key in self.clue_sim_cache:
            return self.clue_sim_cache[key]

        if w1_clean not in self.clue_words_index_map or w2_clean not in self.clue_words_index_map:
            self.clue_sim_cache[key] = 0.0
            return 0.0

        try:
            idx1 = self.clue_words_index_map[w1_clean]
            idx2 = self.clue_words_index_map[w2_clean]

            vec1 = self.tfidf_matrix[idx1]
            vec2 = self.tfidf_matrix[idx2]

            sim = float(vec1.dot(vec2.T).toarray()[0][0])
            self.clue_sim_cache[key] = sim
            return sim
        except Exception:
            self.clue_sim_cache[key] = 0.0
            return 0.0

    def get_sentence_embeddings(self, words: List[str]) -> Dict[str, np.ndarray]:
        """Return normalized sentence-transformer embeddings for board words when available."""
        missing_words = []
        embeddings = {}
        for word in words:
            word_clean = word.strip().upper()
            cached = self.embedding_cache.get(word_clean)
            if cached is None:
                missing_words.append(word_clean)
            else:
                embeddings[word_clean] = np.array(cached, dtype=np.float32)

        if missing_words and not self.embedding_model_failed:
            try:
                if self.embedding_model is None:
                    from sentence_transformers import SentenceTransformer
                    model_name = os.environ.get("CONNECTIONS_SENTENCE_MODEL", SENTENCE_EMBEDDING_MODEL)
                    self.embedding_model = SentenceTransformer(model_name)

                encoded = self.embedding_model.encode(
                    missing_words,
                    normalize_embeddings=True,
                    convert_to_numpy=True,
                    show_progress_bar=False,
                )
                for word, embedding in zip(missing_words, encoded):
                    arr = np.asarray(embedding, dtype=np.float32)
                    embeddings[word] = arr
                    self.embedding_cache[word] = arr.tolist()
                self.embedding_cache_dirty = True
            except Exception as e:
                print(f"Warning: SentenceTransformer embeddings unavailable: {e}")
                self.embedding_model_failed = True

        return embeddings

    def get_sentence_embedding_similarity(
        self,
        w1: str,
        w2: str,
        embeddings: Dict[str, np.ndarray],
    ) -> float:
        w1_clean = w1.strip().upper()
        w2_clean = w2.strip().upper()
        emb1 = embeddings.get(w1_clean)
        emb2 = embeddings.get(w2_clean)
        if emb1 is None or emb2 is None:
            return 0.0
        # Embeddings are normalized, so dot product equals cosine similarity.
        return float(np.clip(np.dot(emb1, emb2), -1.0, 1.0))

    def __del__(self):
        if hasattr(self, 'db_conn') and self.db_conn is not None:
            try:
                self.db_conn.close()
            except Exception:
                pass

    def _query_local_conceptnet(self, word: str) -> List[Dict[str, Any]]:
        """Query local SQLite database for ConceptNet relations."""
        db_path = os.path.join(os.path.dirname(__file__), "../data/conceptnet_normalized.db")
        if not os.path.exists(db_path):
            return []

        word_clean = word.strip().lower().replace(" ", "_")
        url_exact = f"http://conceptnet.io/c/en/{word_clean}"
        url_prefix_start = f"http://conceptnet.io/c/en/{word_clean}/"
        url_prefix_end = f"http://conceptnet.io/c/en/{word_clean}0"

        try:
            if self.db_conn is None:
                self.db_conn = sqlite3.connect(db_path)

            cursor = self.db_conn.cursor()
            cursor.execute("""
                SELECT node_pk FROM node_norm
                WHERE node_url = ?
                   OR (node_url >= ? AND node_url < ?);
            """, (url_exact, url_prefix_start, url_prefix_end))
            nodes = cursor.fetchall()
            if not nodes:
                return []

            node_pks = [r[0] for r in nodes]
            placeholders = ",".join("?" for _ in node_pks)
            cursor.execute(f"""
                SELECT e.weight, r.rel_url, n_start.node_url, n_end.node_url
                FROM edge_norm e
                JOIN rel_norm r ON e.rel_fk = r.rel_pk
                JOIN node_norm n_start ON e.start_fk = n_start.node_pk
                JOIN node_norm n_end ON e.end_fk = n_end.node_pk
                WHERE e.start_fk IN ({placeholders}) OR e.end_fk IN ({placeholders});
            """, node_pks + node_pks)

            def get_label(url: str) -> str:
                parts = url.split('/')
                if len(parts) >= 6:
                    return parts[5].replace('_', ' ').lower()
                return url

            edges = []
            for weight, rel_url, start_url, end_url in cursor.fetchall():
                edges.append({
                    "rel": rel_url,
                    "start": get_label(start_url),
                    "end": get_label(end_url),
                    "weight": float(weight)
                })
            return edges
        except Exception as e:
            print(f"Warning: Local SQLite query failed for '{word}': {e}")
            self.db_conn = None
            return []

    def query_conceptnet(self, word: str) -> Dict[str, Any]:
        """Fetch relation edges from ConceptNet for a word (cached)."""
        word_clean = word.strip().lower().replace(" ", "_")
        if word_clean in self.conceptnet_cache:
            return self.conceptnet_cache[word_clean]

        # Try local SQLite lookup
        edges = self._query_local_conceptnet(word_clean)
        if edges:
            self.conceptnet_cache[word_clean] = edges
            return edges

        if self.conceptnet_offline:
            return []

        # Call API fallback
        url = f"http://api.conceptnet.io/c/en/{urllib.parse.quote(word_clean)}?limit=100"
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Connections-Solver; contact: max@example.com)'}
            )
            with urllib.request.urlopen(req, timeout=3) as response:
                res_data = json.loads(response.read().decode())
                # Extract simple node connection mappings
                edges = []
                for edge in res_data.get("edges", []):
                    rel = edge.get("rel", {}).get("@id", "")
                    start = edge.get("start", {}).get("label", "").lower()
                    end = edge.get("end", {}).get("label", "").lower()
                    weight = edge.get("weight", 1.0)
                    edges.append({
                        "rel": rel,
                        "start": start,
                        "end": end,
                        "weight": weight
                    })
                self.conceptnet_cache[word_clean] = edges
                self._save_conceptnet_cache()
                return edges
        except Exception as e:
            # Check for Bad Gateway (502) or Service Unavailable (503) or Gateway Timeout (504)
            if hasattr(e, 'code') and e.code in (502, 503, 504):
                print(f"ConceptNet API returned status {e.code}. Switching to offline fallback mode.")
                self.conceptnet_offline = True

            # Cache the failure to avoid repeating queries
            self.conceptnet_cache[word_clean] = []
            self._save_conceptnet_cache()
            return []

    def get_conceptnet_connection(self, w1: str, w2: str, relations: List[Dict[str, Any]]) -> float:
        """
        Check if w2 is connected to w1.
        First attempts to find a match in ConceptNet relations.
        If ConceptNet is down/offline (relations list is empty), falls back to local clue cache matching.
        """
        w2_clean = w2.strip().lower()
        w1_clean = w1.strip().lower()

        # 1. Attempt ConceptNet match if relations are present
        if relations:
            max_weight = 0.0
            for edge in relations:
                start = edge["start"]
                end = edge["end"]
                if (w2_clean == start or w2_clean == end or
                    w2_clean in start.split() or w2_clean in end.split()):
                    max_weight = max(max_weight, edge["weight"])
            if max_weight > 0.0:
                return max_weight

        # 2. Offline Fallback: Scan clue description of w1 for occurrences of w2
        if self.clue_cache:
            w1_upper = w1.strip().upper()
            w2_upper = w2.strip().upper()
            desc = self.clue_cache.get(w1_upper, "")
            if desc:
                # Tokenize upper case description to find exact word matches
                desc_tokens = set(re.findall(r'\b\w+\b', desc.upper()))

                # Check direct match
                if w2_upper in desc_tokens:
                    return 1.5

                # Check singular variant match if w2 ends in S
                if w2_upper.endswith('S') and len(w2_upper) > 3:
                    w2_singular = w2_upper[:-1]
                    if w2_singular in desc_tokens:
                        return 1.2

        return 0.0

    def get_conceptnet_relation_features(
        self,
        w1: str,
        w2: str,
        w1_relations: List[Dict[str, Any]],
        w2_relations: List[Dict[str, Any]],
    ) -> List[float]:
        """Return type-specific ConceptNet pair features for a board word pair."""
        features = [0.0] * len(CONCEPTNET_RELATION_FEATURES)
        self._update_direct_conceptnet_relation_features(features, w2, w1_relations)
        self._update_direct_conceptnet_relation_features(features, w1, w2_relations)

        w1_contexts = self._get_conceptnet_contexts(w1, w1_relations)
        w2_contexts = self._get_conceptnet_contexts(w2, w2_relations)
        if (
            CONCEPTNET_HAS_CONTEXT_FEATURE_IDX
            not in DISABLED_CONCEPTNET_RELATION_FEATURE_IDXS
            and w1_contexts.intersection(w2_contexts)
        ):
            features[CONCEPTNET_HAS_CONTEXT_FEATURE_IDX] = 1.0

        return features

    def get_conceptnet_residual_connection(
        self,
        target_word: str,
        relations: List[Dict[str, Any]],
    ) -> float:
        """Return max direct ConceptNet weight for relation types not separately modeled."""
        target = self._conceptnet_label_token(target_word)
        max_weight = 0.0
        for edge in relations or []:
            relation_name = self._conceptnet_relation_name(edge.get("rel", ""))
            if relation_name in CONCEPTNET_COVERED_RELATION_NAMES:
                continue
            if not self._conceptnet_edge_mentions(edge, target):
                continue
            max_weight = max(max_weight, float(edge.get("weight", 1.0)))
        return max_weight

    def _update_direct_conceptnet_relation_features(
        self,
        features: List[float],
        target_word: str,
        relations: List[Dict[str, Any]],
    ) -> None:
        target = self._conceptnet_label_token(target_word)
        for edge in relations or []:
            relation_name = self._conceptnet_relation_name(edge.get("rel", ""))
            if not relation_name:
                continue
            if not self._conceptnet_edge_mentions(edge, target):
                continue
            weight = float(edge.get("weight", 1.0))
            for feature_idx, relation_names in CONCEPTNET_DIRECT_RELATION_FEATURES:
                if relation_name in relation_names:
                    features[feature_idx] = max(features[feature_idx], weight)
                    break

    def _get_conceptnet_contexts(
        self,
        word: str,
        relations: List[Dict[str, Any]],
    ) -> Set[str]:
        word_token = self._conceptnet_label_token(word)
        contexts = set()
        for edge in relations or []:
            if self._conceptnet_relation_name(edge.get("rel", "")) != "HasContext":
                continue
            start = self._conceptnet_label_token(edge.get("start", ""))
            end = self._conceptnet_label_token(edge.get("end", ""))
            if start == word_token and end:
                contexts.add(end)
            elif end == word_token and start:
                contexts.add(start)
            else:
                if start:
                    contexts.add(start)
                if end:
                    contexts.add(end)
        return contexts

    @staticmethod
    def _conceptnet_relation_name(rel: str) -> str:
        return rel.rstrip("/").rsplit("/", 1)[-1]

    @staticmethod
    def _conceptnet_label_token(label: str) -> str:
        return label.strip().lower().replace("_", " ")

    @classmethod
    def _conceptnet_edge_mentions(cls, edge: Dict[str, Any], target: str) -> bool:
        start = cls._conceptnet_label_token(edge.get("start", ""))
        end = cls._conceptnet_label_token(edge.get("end", ""))
        return (
            cls._conceptnet_label_mentions(start, target)
            or cls._conceptnet_label_mentions(end, target)
        )

    @staticmethod
    def _conceptnet_label_mentions(label: str, target: str) -> bool:
        if target == label:
            return True
        target_tokens = set(target.split())
        label_tokens = set(label.split())
        return bool(target_tokens) and target_tokens.issubset(label_tokens)

    def extract_wordnet_features(self, w1: str, w2: str) -> Tuple[float, float]:
        """Compute path similarity and hypernym sharing between two words using WordNet."""
        key = tuple(sorted([w1.lower(), w2.lower()]))
        if key in self.wordnet_pair_cache:
            return self.wordnet_pair_cache[key]

        s1 = wn.synsets(w1.lower())
        s2 = wn.synsets(w2.lower())

        if not s1 or not s2:
            self.wordnet_pair_cache[key] = (0.0, 0.0)
            return 0.0, 0.0

        max_sim = 0.0
        shares_hypernym = 0.0

        for syn1 in s1:
            for syn2 in s2:
                sim = syn1.path_similarity(syn2)
                if sim and sim > max_sim:
                    max_sim = sim

                # Check hypernym overlap
                h1 = set(syn1.hypernyms())
                h2 = set(syn2.hypernyms())
                if h1.intersection(h2):
                    shares_hypernym = 1.0

        result = (float(max_sim), float(shares_hypernym))
        self.wordnet_pair_cache[key] = result
        return result

    def get_wordplay_features(self, w1: str, w2: str) -> Dict[str, float]:
        """Deterministic orthographic/wordplay features between word pairs."""
        w1_clean = w1.strip().upper()
        w2_clean = w2.strip().upper()

        # 1. Anagram check
        is_anagram = 1.0 if sorted(w1_clean) == sorted(w2_clean) and w1_clean != w2_clean else 0.0

        # 2. Shared prefix (length >= 3)
        prefix_len = 0
        min_len = min(len(w1_clean), len(w2_clean))
        for i in range(min(5, min_len)):
            if w1_clean[i] == w2_clean[i]:
                prefix_len += 1
            else:
                break
        shared_prefix = 1.0 if prefix_len >= 3 else 0.0

        # 3. Shared suffix (length >= 3)
        suffix_len = 0
        for i in range(1, min(6, min_len + 1)):
            if w1_clean[-i] == w2_clean[-i]:
                suffix_len += 1
            else:
                break
        shared_suffix = 1.0 if suffix_len >= 3 else 0.0

        # 4. Substring relationship
        is_substring = 0.0
        if len(w1_clean) > len(w2_clean) and w2_clean in w1_clean:
            is_substring = 1.0
        elif len(w2_clean) > len(w1_clean) and w1_clean in w2_clean:
            is_substring = 1.0

        # 5. Length ratio/difference
        len_diff = abs(len(w1_clean) - len(w2_clean))
        norm_len_diff = len_diff / max(1, max(len(w1_clean), len(w2_clean)))
        norm_levenshtein_distance = self._normalized_levenshtein_distance(
            w1_clean, w2_clean
        )

        return {
            "is_anagram": is_anagram,
            "shared_prefix": shared_prefix,
            "shared_suffix": shared_suffix,
            "is_substring": is_substring,
            "len_diff": norm_len_diff,
            "levenshtein_distance": norm_levenshtein_distance
        }

    @staticmethod
    def _normalized_levenshtein_distance(w1: str, w2: str) -> float:
        """Return edit distance normalized by the longer word length."""
        if w1 == w2:
            return 0.0

        previous_row = list(range(len(w2) + 1))
        for i, c1 in enumerate(w1, start=1):
            current_row = [i]
            for j, c2 in enumerate(w2, start=1):
                insertions = previous_row[j] + 1
                deletions = current_row[j - 1] + 1
                substitutions = previous_row[j - 1] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        distance = previous_row[-1]
        return distance / max(1, max(len(w1), len(w2)))

    @staticmethod
    def get_phonemes(word: str) -> List[str]:
        """Cleans word and returns its phoneme list from CMUDict. Supports splitting multi-word/compound phrases."""
        word_clean = word.strip().lower()
        if not word_clean:
            return []

        # Try direct dictionary lookup
        if word_clean in CMU_DICT:
            return CMU_DICT[word_clean][0]

        # Try splitting by space/hyphen and combining phonemes
        parts = re.split(r'[\s\-]+', word_clean)
        if len(parts) > 1:
            combined = []
            for part in parts:
                if part in CMU_DICT:
                    combined.extend(CMU_DICT[part][0])
                else:
                    return [] # If any part is missing, we consider the whole word missing
            return combined

        return []

    @staticmethod
    def get_soundex(word: str) -> str:
        """Compute the Soundex code for a word."""
        word = re.sub(r'[^a-zA-Z]', '', word).upper()
        if not word:
            return ""

        first_letter = word[0]
        mapping = {
            'B': '1', 'F': '1', 'P': '1', 'V': '1',
            'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
            'D': '3', 'T': '3',
            'L': '4',
            'M': '5', 'N': '5',
            'R': '6'
        }

        codes = []
        prev_code = mapping.get(first_letter, '0')
        for char in word[1:]:
            code = mapping.get(char, '0')
            if code != '0':
                if code != prev_code:
                    codes.append(code)
                prev_code = code
            else:
                if char in 'AEIOUY':
                    prev_code = '0'
        digits = "".join(codes).replace('0', '')
        return (first_letter + digits + "000")[:4]

    @staticmethod
    def get_metaphone(word: str) -> str:
        """Compute the Metaphone code for a word."""
        try:
            return jellyfish.metaphone(word)
        except Exception:
            return ""

    @staticmethod
    def _extract_rhyme_part(phonemes: List[str]) -> List[str]:
        """Extract the rhyming portion of a phoneme sequence (from the last stressed vowel)."""
        # Try finding last stressed vowel (stress 1 or 2)
        for idx in range(len(phonemes) - 1, -1, -1):
            ph = phonemes[idx]
            if any(char in '12' for char in ph):
                return phonemes[idx:]
        # Fallback to last vowel with stress 0
        for idx in range(len(phonemes) - 1, -1, -1):
            ph = phonemes[idx]
            if any(char.isdigit() for char in ph):
                return phonemes[idx:]
        # Fallback to last 2 phonemes
        return phonemes[-2:] if len(phonemes) >= 2 else phonemes

    @staticmethod
    def _normalized_phoneme_edit_distance(p1: List[str], p2: List[str]) -> float:
        """Return edit distance between two phoneme sequences normalized by the longer sequence."""
        if p1 == p2:
            return 0.0
        if not p1 or not p2:
            return 1.0

        previous_row = list(range(len(p2) + 1))
        for i, ph1 in enumerate(p1, start=1):
            current_row = [i]
            for j, ph2 in enumerate(p2, start=1):
                insertions = previous_row[j] + 1
                deletions = current_row[j - 1] + 1
                substitutions = previous_row[j - 1] + (ph1 != ph2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        distance = previous_row[-1]
        return distance / max(1, max(len(p1), len(p2)))

    @staticmethod
    def _phoneme_overlap_ratio(p1: List[str], p2: List[str]) -> float:
        """Return Jaccard similarity of phoneme sets between two phoneme sequences."""
        if not p1 or not p2:
            return 0.0
        set1 = set(p1)
        set2 = set(p2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        if not union:
            return 0.0
        return len(intersection) / len(union)

    @staticmethod
    def _orthographic_token(word: str) -> str:
        """Return uppercase alphabetic text for spelling-shape features."""
        return "".join(re.findall(r"[A-Z]", word.strip().upper()))

    @staticmethod
    def _compound_token(word: str) -> str:
        """Return lowercase alphabetic text for compound-fragment lookup."""
        return "".join(re.findall(r"[a-z]", word.strip().lower()))

    @staticmethod
    def _is_plausible_compound_part(part: str, lemma_words: Set[str]) -> bool:
        return len(part) >= 3 and part in lemma_words

    @staticmethod
    def _normalize_compound_valence(count: int) -> float:
        # Bounded so broad fragments do not dominate the node metadata scale.
        return float(min(1.0, np.log1p(count) / np.log1p(50.0)))

    @staticmethod
    def _normalize_log_count(count: int, max_count: int = 25) -> float:
        return float(min(1.0, np.log1p(max(0, count)) / np.log1p(max_count)))

    @staticmethod
    def _normalize_wordnet_depth(depth: int) -> float:
        # Noun taxonomy depths usually stay below 20; clamp unusual paths.
        return float(min(1.0, max(0, depth) / 20.0))

    @staticmethod
    def _normalize_zipf_frequency(value: float) -> float:
        return float(min(1.0, max(0.0, value) / 8.0))

    def _build_compound_fragment_counts(self) -> None:
        """Build WordNet-only prefix/suffix counts for compound fragments."""
        prefix_matches = defaultdict(set)
        suffix_matches = defaultdict(set)
        lemma_names = set()

        for synset in wn.all_synsets():
            lemma_names.update(synset.lemma_names())

        lemma_words = {
            self._compound_token(lemma)
            for lemma in lemma_names
            if self._compound_token(lemma)
        }

        for lemma in lemma_names:
            raw_parts = [p for p in re.split(r"[_-]+", lemma.lower()) if p]
            parts = [self._compound_token(p) for p in raw_parts]
            parts = [p for p in parts if self._is_plausible_compound_part(p, lemma_words)]
            compound_key = lemma.lower()

            if len(parts) >= 2:
                for idx, part in enumerate(parts):
                    if idx < len(parts) - 1:
                        prefix_matches[part].add(compound_key)
                    if idx > 0:
                        suffix_matches[part].add(compound_key)
                continue

            token = self._compound_token(lemma)
            if len(token) < 6 or token not in lemma_words:
                continue
            for split_idx in range(3, len(token) - 2):
                left = token[:split_idx]
                right = token[split_idx:]
                if (
                    self._is_plausible_compound_part(left, lemma_words)
                    and self._is_plausible_compound_part(right, lemma_words)
                ):
                    prefix_matches[left].add(token)
                    suffix_matches[right].add(token)

        self._compound_prefix_counts = {
            part: len(compounds) for part, compounds in prefix_matches.items()
        }
        self._compound_suffix_counts = {
            part: len(compounds) for part, compounds in suffix_matches.items()
        }

    def get_compound_fragment_valence(self, word: str) -> Tuple[float, float]:
        """Return normalized WordNet prefix/suffix compound-fragment counts."""
        if self._compound_prefix_counts is None or self._compound_suffix_counts is None:
            self._build_compound_fragment_counts()

        token = self._compound_token(word)
        prefix_count = self._compound_prefix_counts.get(token, 0)
        suffix_count = self._compound_suffix_counts.get(token, 0)
        return (
            self._normalize_compound_valence(prefix_count),
            self._normalize_compound_valence(suffix_count),
        )

    def get_ngram_compound_shared_score(self, w1: str, w2: str) -> float:
        """Return strongest shared Google Ngram wildcard completion score."""
        profile_1 = self.get_ngram_compound_profile(w1)
        profile_2 = self.get_ngram_compound_profile(w2)
        best_score = 0.0
        for direction in ("left", "right"):
            completions_1 = profile_1.get(direction, {})
            completions_2 = profile_2.get(direction, {})
            for completion in set(completions_1).intersection(completions_2):
                score = min(float(completions_1[completion]), float(completions_2[completion]))
                best_score = max(best_score, score)
        return float(min(1.0, best_score))

    def get_ngram_compound_profile(self, word: str) -> Dict[str, Dict[str, float]]:
        token = self._compound_token(word)
        empty_profile = {"left": {}, "right": {}}
        if not token:
            return empty_profile

        profiles = self.ngram_compound_cache.setdefault("profiles", {})
        cached = profiles.get(token)
        if self._is_valid_ngram_compound_profile(cached):
            return cached
        if not self.ngram_live_lookup:
            return empty_profile

        profile = self._fetch_ngram_compound_profile(token)
        profiles[token] = profile
        self.ngram_cache_dirty = True
        self._save_ngram_compound_cache()
        return profile

    @staticmethod
    def _is_valid_ngram_compound_profile(profile: Any) -> bool:
        return (
            isinstance(profile, dict)
            and isinstance(profile.get("left"), dict)
            and isinstance(profile.get("right"), dict)
        )

    def _fetch_ngram_compound_profile(self, token: str) -> Dict[str, Dict[str, float]]:
        return {
            "left": self._fetch_ngram_completions(f"* {token}", token, "left"),
            "right": self._fetch_ngram_completions(f"{token} *", token, "right"),
        }

    def _fetch_ngram_completions(
        self,
        query: str,
        token: str,
        direction: str,
    ) -> Dict[str, float]:
        try:
            records = self._query_ngram_records(query)
        except Exception as e:
            print(f"Warning: Google Ngram lookup failed for '{query}': {e}")
            return {}

        raw_scores = {}
        for record in records:
            ngram = str(record.get("ngram", ""))
            completion = self._extract_ngram_completion(ngram, token, direction)
            if completion is None:
                continue
            score = self._ngram_record_score(record)
            if score > 0.0:
                raw_scores[completion] = max(raw_scores.get(completion, 0.0), score)

        max_score = max(raw_scores.values(), default=0.0)
        if max_score <= 0.0:
            return {}
        return {
            completion: float(score / max_score)
            for completion, score in raw_scores.items()
        }

    def _query_ngram_records(self, query: str) -> List[Dict[str, Any]]:
        if self.ngram_client is not None:
            if callable(self.ngram_client):
                return self.ngram_client(query)
            if hasattr(self.ngram_client, "fetch"):
                return self.ngram_client.fetch(query)

        params = urllib.parse.urlencode({
            "content": query,
            "year_start": NGRAM_COMPOUND_YEAR_START,
            "year_end": NGRAM_COMPOUND_YEAR_END,
            "corpus": NGRAM_COMPOUND_CORPUS,
            "smoothing": NGRAM_COMPOUND_SMOOTHING,
            "case_insensitive": "true",
        })
        url = f"https://books.google.com/ngrams/json?{params}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Connections-Solver; contact: max@example.com)"},
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
        return data if isinstance(data, list) else []

    @staticmethod
    def _ngram_record_score(record: Dict[str, Any]) -> float:
        timeseries = record.get("timeseries")
        if isinstance(timeseries, list) and timeseries:
            return max(float(value) for value in timeseries)
        for key in ("score", "value"):
            if key in record:
                return float(record[key])
        return 0.0

    @classmethod
    def _extract_ngram_completion(
        cls,
        ngram: str,
        token: str,
        direction: str,
    ) -> Optional[str]:
        clean_ngram = re.sub(r"\s+\(all\)$", "", ngram.strip().lower())
        tokens = re.findall(r"[a-z]+", clean_ngram)
        if direction == "left" and len(tokens) >= 2 and tokens[-1] == token:
            completion = tokens[-2]
        elif direction == "right" and len(tokens) >= 2 and tokens[0] == token:
            completion = tokens[1]
        else:
            return None
        if not cls._is_ngram_completion_candidate(completion):
            return None
        return completion

    @staticmethod
    def _is_ngram_completion_candidate(token: str) -> bool:
        allowed_particles = {
            "up", "down", "in", "out", "off", "on",
            "over", "back", "away", "around", "through",
            "apart", "together",
        }
        excluded = {
            "start", "end", "root", "noun", "verb", "adj", "adv", "pron",
            "det", "adp", "num", "conj", "prt", "the", "and", "for", "with",
            "from", "into", "onto", "over", "under", "not", "but", "you",
            "your", "his", "her", "their", "our", "its", "this", "that",
            "these", "those", "are", "was", "were", "been", "being", "have",
            "has", "had", "can", "could", "would", "should", "will", "shall",
            "may", "might", "must", "all", "any", "each", "other", "some",
            "such", "than", "then", "there", "where", "when", "what", "which",
            "who", "whom", "whose", "why", "how", "also", "very",
        }
        if token in allowed_particles:
            return True
        return len(token) >= 3 and token.isalpha() and token not in excluded

    def get_conceptnet_is_a_count(self, word: str) -> float:
        """Return normalized offline ConceptNet IsA relation count for a word."""
        word_clean = word.strip().lower().replace(" ", "_")
        edges = self.conceptnet_cache.get(word_clean)
        if edges is None:
            edges = self._query_local_conceptnet(word_clean)
            if edges:
                self.conceptnet_cache[word_clean] = edges

        outgoing_count = 0
        incident_count = 0
        for edge in edges or []:
            rel = edge.get("rel", "")
            if not rel.endswith("/IsA"):
                continue
            incident_count += 1
            start = edge.get("start", "").strip().lower().replace(" ", "_")
            if start == word_clean:
                outgoing_count += 1

        return self._normalize_log_count(outgoing_count or incident_count)

    def get_word_frequency(self, word: str) -> float:
        """Return normalized English Zipf word frequency."""
        token = self._compound_token(word)
        if not token:
            return 0.0

        if self.word_frequency_lookup is not None:
            try:
                return self._normalize_zipf_frequency(
                    float(self.word_frequency_lookup(token, "en"))
                )
            except TypeError:
                try:
                    return self._normalize_zipf_frequency(
                        float(self.word_frequency_lookup(token))
                    )
                except Exception:
                    pass
            except Exception:
                pass

        return 0.0

    def get_wordnet_max_depth(self, synsets: List[Any]) -> float:
        max_depth = 0
        for synset in synsets:
            try:
                max_depth = max(max_depth, synset.max_depth())
            except Exception:
                continue
        return self._normalize_wordnet_depth(max_depth)

    @staticmethod
    def get_wordnet_domain_features(synsets: List[Any]) -> List[float]:
        domains = {synset.lexname() for synset in synsets}
        return [
            1.0 if domain in domains else 0.0
            for domain in WORDNET_DOMAIN_TAGS
        ]

    def get_word_node_features(self, w: str) -> List[float]:
        """Compute independent metadata features for a single word."""
        w_clean = w.strip().upper()
        cached = self.wordnet_single_cache.get(w_clean)
        if cached is not None and len(cached) == INTRINSIC_NODE_METADATA_DIM:
            return cached

        synsets = wn.synsets(w.lower())

        polysemy_count = len(synsets)
        word_len = len(w_clean)
        is_plural = 1.0 if w_clean.endswith('S') and len(w_clean) > 3 else 0.0

        # Count parts of speech available
        pos_counts = Counter([s.pos() for s in synsets])
        has_noun = 1.0 if pos_counts['n'] > 0 else 0.0
        has_verb = 1.0 if pos_counts['v'] > 0 else 0.0
        has_adj = 1.0 if (pos_counts['a'] > 0 or pos_counts['s'] > 0) else 0.0
        has_adverb = 1.0 if pos_counts['r'] > 0 else 0.0

        clue_len = 0.0
        if w_clean in self.clue_cache:
            clue_len = len(self.clue_cache[w_clean])

        ortho_token = self._orthographic_token(w)
        is_palindrome = (
            1.0
            if len(ortho_token) >= 3 and ortho_token == ortho_token[::-1]
            else 0.0
        )
        has_double_letter = (
            1.0
            if any(a == b for a, b in zip(ortho_token, ortho_token[1:]))
            else 0.0
        )
        compound_prefix_valence, compound_suffix_valence = (
            self.get_compound_fragment_valence(w)
        )
        wordnet_depth = self.get_wordnet_max_depth(synsets)
        conceptnet_is_a_count = self.get_conceptnet_is_a_count(w)
        word_frequency = self.get_word_frequency(w)
        wordnet_domain_features = self.get_wordnet_domain_features(synsets)

        result = [
            float(polysemy_count),
            float(word_len),
            float(is_plural),
            float(has_noun),
            float(has_verb),
            float(has_adj),
            float(clue_len),
            float(is_palindrome),
            float(has_double_letter),
            float(compound_prefix_valence),
            float(compound_suffix_valence),
            float(has_adverb),
            float(wordnet_depth),
            float(conceptnet_is_a_count),
            float(word_frequency),
            *wordnet_domain_features,
        ]
        self.wordnet_single_cache[w_clean] = result
        return result

    def build_graph_matrices(self, words: List[str]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Builds the node features and multi-dimensional edge features for a 16-word board.
        Returns:
            node_features: shape (16, num_node_features)
            edge_features: shape (16, 16, num_edge_features)
        """
        n = len(words)
        assert n == 16, "A Connections board must contain exactly 16 words."

        # 2. Pre-fetch board-level semantic and phonetic resources to save repeated calls
        cn_relations = {w: self.query_conceptnet(w) for w in words}
        sentence_embeddings = self.get_sentence_embeddings(words)
        phonemes_cache = {w: self.get_phonemes(w) for w in words}
        soundex_cache = {w: self.get_soundex(w) for w in words}
        metaphone_cache = {w: self.get_metaphone(w) for w in words}

        # 1. Node features (intrinsic metadata + sentence embeddings)
        # Determine sentence embedding dimensions dynamically (default to 768)
        emb_dim = DEFAULT_SENTENCE_EMBEDDING_DIM
        for emb in sentence_embeddings.values():
            emb_dim = emb.shape[0]
            break

        intrinsic_node_feats = []
        node_embeddings = []
        for w in words:
            intrinsic_node_feats.append(self.get_word_node_features(w))
            w_clean = w.strip().upper()
            node_embeddings.append(
                sentence_embeddings.get(w_clean, np.zeros(emb_dim, dtype=np.float32))
            )

        # 3. Edge features
        # Edge dimensions:
        # 0: WordNet path similarity
        # 1: WordNet shares hypernym
        # 2-8: ConceptNet relation-type features
        # 9: ConceptNet residual forward connection weight
        # 10: ConceptNet residual backward connection weight
        # 11: Clue description TF-IDF similarity
        # 12: Is Anagram
        # 13: Shares Prefix
        # 14: Shares Suffix
        # 15: Is Substring
        # 16: Length difference
        # 17: SentenceTransformer cosine similarity
        # 18: Levenshtein distance
        # 19: Phoneme edit distance
        # 20: Rhyme match
        # 21: Soundex match
        # 22: Double Metaphone match
        # 23: Phoneme overlap Jaccard similarity
        # 24: Shared Google Ngrams compound-fragment completion
        num_edge_feats = EDGE_FEATURE_DIM
        edge_features = np.zeros((n, n, num_edge_feats), dtype=np.float32)

        for i in range(n):
            for j in range(n):
                w_i = words[i]
                w_j = words[j]

                if i == j:
                    # Self-loops have identity features
                    edge_features[i, j, WORDNET_PATH_SIM_DIM] = 1.0
                    edge_features[i, j, WORDNET_SHARED_HYPERNYM_DIM] = 1.0
                    edge_features[i, j, CLUE_SIMILARITY_DIM] = 1.0
                    edge_features[i, j, SENTENCE_SIMILARITY_DIM] = 1.0
                    edge_features[i, j, RHYME_MATCH_DIM] = 1.0
                    edge_features[i, j, SOUNDEX_MATCH_DIM] = 1.0
                    edge_features[i, j, METAPHONE_MATCH_DIM] = 1.0
                    edge_features[i, j, PHONEME_OVERLAP_DIM] = 1.0
                    edge_features[i, j, COMPOUND_FRAGMENT_SHARED_DIM] = 1.0
                    continue

                # WordNet
                wn_sim, wn_hyp = self.extract_wordnet_features(w_i, w_j)
                edge_features[i, j, WORDNET_PATH_SIM_DIM] = wn_sim
                edge_features[i, j, WORDNET_SHARED_HYPERNYM_DIM] = wn_hyp

                # ConceptNet
                cn_features = self.get_conceptnet_relation_features(
                    w_i,
                    w_j,
                    cn_relations[w_i],
                    cn_relations[w_j],
                )
                edge_features[
                    i,
                    j,
                    CN_IS_A_DIM:CN_DISTINCT_FROM_DIM + 1,
                ] = cn_features
                edge_features[i, j, CN_RESIDUAL_FORWARD_DIM] = (
                    self.get_conceptnet_residual_connection(w_j, cn_relations[w_i])
                )
                edge_features[i, j, CN_RESIDUAL_BACKWARD_DIM] = (
                    self.get_conceptnet_residual_connection(w_i, cn_relations[w_j])
                )

                # Clue Cache
                edge_features[i, j, CLUE_SIMILARITY_DIM] = self.get_clue_similarity(w_i, w_j)

                # Wordplay
                wp = self.get_wordplay_features(w_i, w_j)
                edge_features[i, j, IS_ANAGRAM_DIM] = wp["is_anagram"]
                edge_features[i, j, SHARED_PREFIX_DIM] = wp["shared_prefix"]
                edge_features[i, j, SHARED_SUFFIX_DIM] = wp["shared_suffix"]
                edge_features[i, j, IS_SUBSTRING_DIM] = wp["is_substring"]
                edge_features[i, j, LENGTH_DISTANCE_DIM] = wp["len_diff"]
                edge_features[i, j, SENTENCE_SIMILARITY_DIM] = self.get_sentence_embedding_similarity(
                    w_i, w_j, sentence_embeddings
                )
                edge_features[i, j, LEVENSHTEIN_DISTANCE_DIM] = wp["levenshtein_distance"]

                # Phonetic features
                p_i = phonemes_cache[w_i]
                p_j = phonemes_cache[w_j]

                if not p_i or not p_j:
                    edge_features[i, j, PHONEME_EDIT_DISTANCE_DIM] = 1.0
                    edge_features[i, j, RHYME_MATCH_DIM] = 0.0
                    edge_features[i, j, PHONEME_OVERLAP_DIM] = 0.0
                else:
                    edge_features[i, j, PHONEME_EDIT_DISTANCE_DIM] = self._normalized_phoneme_edit_distance(p_i, p_j)
                    rhyme_i = self._extract_rhyme_part(p_i)
                    rhyme_j = self._extract_rhyme_part(p_j)
                    edge_features[i, j, RHYME_MATCH_DIM] = 1.0 if rhyme_i == rhyme_j else 0.0
                    edge_features[i, j, PHONEME_OVERLAP_DIM] = self._phoneme_overlap_ratio(p_i, p_j)

                s_i = soundex_cache[w_i]
                s_j = soundex_cache[w_j]
                edge_features[i, j, SOUNDEX_MATCH_DIM] = 1.0 if s_i and s_j and s_i == s_j else 0.0

                m_i = metaphone_cache[w_i]
                m_j = metaphone_cache[w_j]
                edge_features[i, j, METAPHONE_MATCH_DIM] = 1.0 if m_i and m_j and m_i == m_j else 0.0

                edge_features[i, j, COMPOUND_FRAGMENT_SHARED_DIM] = (
                    self.get_ngram_compound_shared_score(w_i, w_j)
                )

        board_context_features = self._get_board_context_features(
            node_embeddings,
            edge_features,
        )
        node_feats = []
        for idx, intrinsic_feats in enumerate(intrinsic_node_feats):
            combined_feats = (
                intrinsic_feats
                + board_context_features[idx].tolist()
                + node_embeddings[idx].tolist()
            )
            node_feats.append(combined_feats)
        node_features = np.array(node_feats, dtype=np.float32)

        return node_features, edge_features

    def _get_board_context_features(
        self,
        node_embeddings: List[np.ndarray],
        edge_features: np.ndarray,
    ) -> np.ndarray:
        centroid_distances = self._get_board_st_centroid_distances(node_embeddings)
        avg_edge_weights, max_edge_weights = self._get_board_edge_weight_stats(
            edge_features
        )
        return np.stack(
            [centroid_distances, avg_edge_weights, max_edge_weights],
            axis=1,
        ).astype(np.float32)

    @staticmethod
    def _get_board_st_centroid_distances(
        node_embeddings: List[np.ndarray],
    ) -> np.ndarray:
        n = len(node_embeddings)
        if not node_embeddings:
            return np.zeros(n, dtype=np.float32)

        embeddings = np.asarray(node_embeddings, dtype=np.float32)
        nonzero_mask = np.linalg.norm(embeddings, axis=1) > 0.0
        if not np.any(nonzero_mask):
            return np.zeros(n, dtype=np.float32)

        centroid = embeddings[nonzero_mask].mean(axis=0)
        centroid_norm = np.linalg.norm(centroid)
        if centroid_norm == 0.0:
            return np.zeros(n, dtype=np.float32)

        centroid = centroid / centroid_norm
        similarities = np.clip(embeddings @ centroid, -1.0, 1.0)
        distances = np.where(nonzero_mask, 1.0 - similarities, 0.0)
        return distances.astype(np.float32)

    @staticmethod
    def _get_board_edge_weight_stats(
        edge_features: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray]:
        strengths = FeatureExtractor._get_static_relation_strengths(edge_features)
        n = strengths.shape[0]
        if n <= 1:
            return (
                np.zeros(n, dtype=np.float32),
                np.zeros(n, dtype=np.float32),
            )

        off_diagonal_mask = ~np.eye(n, dtype=bool)
        incident_strengths = strengths[off_diagonal_mask].reshape(n, n - 1, -1)
        incident_strengths = incident_strengths.reshape(n, -1)
        return (
            incident_strengths.mean(axis=1).astype(np.float32),
            incident_strengths.max(axis=1).astype(np.float32),
        )

    @staticmethod
    def _get_static_relation_strengths(edge_features: np.ndarray) -> np.ndarray:
        strengths = np.array(edge_features, dtype=np.float32, copy=True)
        strengths[:, :, LENGTH_DISTANCE_DIM] = FeatureExtractor._threshold_similarity(
            1.0 - strengths[:, :, LENGTH_DISTANCE_DIM],
            LENGTH_SIMILARITY_THRESHOLD,
        )
        strengths[:, :, LEVENSHTEIN_DISTANCE_DIM] = FeatureExtractor._threshold_similarity(
            1.0 - strengths[:, :, LEVENSHTEIN_DISTANCE_DIM],
            LEVENSHTEIN_SIMILARITY_THRESHOLD,
        )
        strengths[:, :, WORDNET_PATH_SIM_DIM] = FeatureExtractor._threshold_similarity(
            strengths[:, :, WORDNET_PATH_SIM_DIM],
            WORDNET_PATH_SIMILARITY_THRESHOLD,
        )
        strengths[:, :, CLUE_SIMILARITY_DIM] = FeatureExtractor._threshold_similarity(
            strengths[:, :, CLUE_SIMILARITY_DIM],
            CLUE_SIMILARITY_THRESHOLD,
        )
        strengths[:, :, SENTENCE_SIMILARITY_DIM] = FeatureExtractor._threshold_similarity(
            strengths[:, :, SENTENCE_SIMILARITY_DIM],
            SENTENCE_SIMILARITY_THRESHOLD,
        )
        strengths[:, :, PHONEME_EDIT_DISTANCE_DIM] = FeatureExtractor._threshold_similarity(
            1.0 - strengths[:, :, PHONEME_EDIT_DISTANCE_DIM],
            PHONEME_EDIT_DISTANCE_THRESHOLD,
        )
        strengths[:, :, PHONEME_OVERLAP_DIM] = FeatureExtractor._threshold_similarity(
            strengths[:, :, PHONEME_OVERLAP_DIM],
            PHONEME_OVERLAP_THRESHOLD,
        )
        strengths[:, :, COMPOUND_FRAGMENT_SHARED_DIM] = FeatureExtractor._threshold_similarity(
            strengths[:, :, COMPOUND_FRAGMENT_SHARED_DIM],
            COMPOUND_FRAGMENT_SHARED_THRESHOLD,
        )

        idx = np.arange(strengths.shape[0])
        strengths[idx, idx, :] = 0.0
        return strengths

    @staticmethod
    def _threshold_similarity(values: np.ndarray, threshold: float) -> np.ndarray:
        return np.where(values >= threshold, values, 0.0).astype(np.float32)

if __name__ == "__main__":
    # Test on a small mockup
    extractor = FeatureExtractor()
    test_words = [
        "HAIL", "RAIN", "SLEET", "SNOW",
        "BUCKS", "HEAT", "JAZZ", "NETS",
        "OPTION", "RETURN", "SHIFT", "TAB",
        "KAYAK", "LEVEL", "MOM", "RACECAR"
    ]
    node_feat, edge_feat = extractor.build_graph_matrices(test_words)
    print("Node Features Shape:", node_feat.shape)
    print("Edge Features Shape:", edge_feat.shape)
    print("Sample edge between HAIL and RAIN features:", edge_feat[0, 1])
    print("Sample edge between HAIL and BUCKS features:", edge_feat[0, 4])
