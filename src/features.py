import os
import re
import json
import urllib.request
import urllib.parse
import sqlite3
from collections import Counter
import numpy as np
from typing import List, Dict, Tuple, Set, Any
import nltk
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EDGE_FEATURE_DIM = 12
FEATURE_SCHEMA_VERSION = 5
SENTENCE_EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

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
    def __init__(self, cache_dir: str = None):
        if cache_dir is None:
            cache_dir = os.path.join(os.path.dirname(__file__), "../data")
        os.makedirs(cache_dir, exist_ok=True)
        
        self.conceptnet_cache_path = os.path.join(cache_dir, "conceptnet_cache.json")
        self.clue_cache_path = os.path.join(cache_dir, "llm_context_cache.json")
        self.embedding_cache_path = os.path.join(cache_dir, "sentence_embedding_cache.json")
        
        # Load caches
        self.conceptnet_cache = self._load_json_cache(self.conceptnet_cache_path)
        self.clue_cache = self._load_json_cache(self.clue_cache_path)
        self.embedding_cache = self._load_json_cache(self.embedding_cache_path)
        
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

    def _load_json_cache(self, path: str) -> Dict[str, Any]:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

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

    def get_word_node_features(self, w: str) -> List[float]:
        """Compute independent metadata features for a single word."""
        w_clean = w.strip().upper()
        if w_clean in self.wordnet_single_cache:
            return self.wordnet_single_cache[w_clean]
            
        synsets = wn.synsets(w.lower())
        
        polysemy_count = len(synsets)
        word_len = len(w_clean)
        is_plural = 1.0 if w_clean.endswith('S') and len(w_clean) > 3 else 0.0
        
        # Count parts of speech available
        pos_counts = Counter([s.pos() for s in synsets])
        has_noun = 1.0 if pos_counts['n'] > 0 else 0.0
        has_verb = 1.0 if pos_counts['v'] > 0 else 0.0
        has_adj = 1.0 if (pos_counts['a'] > 0 or pos_counts['s'] > 0) else 0.0
        
        clue_len = 0.0
        if w_clean in self.clue_cache:
            clue_len = len(self.clue_cache[w_clean])
            
        result = [
            float(polysemy_count),
            float(word_len),
            float(is_plural),
            float(has_noun),
            float(has_verb),
            float(has_adj),
            float(clue_len)
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
        
        # 2. Pre-fetch board-level semantic resources to save repeated calls
        cn_relations = {w: self.query_conceptnet(w) for w in words}
        sentence_embeddings = self.get_sentence_embeddings(words)

        # 1. Node features (metadata + sentence embeddings)
        # Determine sentence embedding dimensions dynamically (default to 768)
        emb_dim = 768
        for emb in sentence_embeddings.values():
            emb_dim = emb.shape[0]
            break

        node_feats = []
        for w in words:
            meta_feats = self.get_word_node_features(w)
            w_clean = w.strip().upper()
            embedding = sentence_embeddings.get(w_clean, np.zeros(emb_dim, dtype=np.float32))
            combined_feats = meta_feats + embedding.tolist()
            node_feats.append(combined_feats)
        node_features = np.array(node_feats, dtype=np.float32)
        
        # 3. Edge features
        # Edge dimensions:
        # 0: WordNet path similarity
        # 1: WordNet shares hypernym
        # 2: ConceptNet forward connection weight
        # 3: ConceptNet backward connection weight
        # 4: Clue description TF-IDF similarity
        # 5: Is Anagram
        # 6: Shares Prefix
        # 7: Shares Suffix
        # 8: Is Substring
        # 9: Length difference
        # 10: SentenceTransformer cosine similarity
        # 11: Levenshtein distance
        num_edge_feats = EDGE_FEATURE_DIM
        edge_features = np.zeros((n, n, num_edge_feats), dtype=np.float32)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    # Self-loops have identity features
                    edge_features[i, j, 0] = 1.0 # path sim
                    edge_features[i, j, 1] = 1.0 # hypernym
                    edge_features[i, j, 4] = 1.0 # clue sim
                    edge_features[i, j, 10] = 1.0 # sentence embedding sim
                    continue
                
                w_i = words[i]
                w_j = words[j]
                
                # WordNet
                wn_sim, wn_hyp = self.extract_wordnet_features(w_i, w_j)
                edge_features[i, j, 0] = wn_sim
                edge_features[i, j, 1] = wn_hyp
                
                # ConceptNet
                cn_fwd = self.get_conceptnet_connection(w_i, w_j, cn_relations[w_i])
                cn_bwd = self.get_conceptnet_connection(w_j, w_i, cn_relations[w_j])
                edge_features[i, j, 2] = cn_fwd
                edge_features[i, j, 3] = cn_bwd
                
                # Clue Cache
                edge_features[i, j, 4] = self.get_clue_similarity(w_i, w_j)
                
                # Wordplay
                wp = self.get_wordplay_features(w_i, w_j)
                edge_features[i, j, 5] = wp["is_anagram"]
                edge_features[i, j, 6] = wp["shared_prefix"]
                edge_features[i, j, 7] = wp["shared_suffix"]
                edge_features[i, j, 8] = wp["is_substring"]
                edge_features[i, j, 9] = wp["len_diff"]
                edge_features[i, j, 10] = self.get_sentence_embedding_similarity(
                    w_i, w_j, sentence_embeddings
                )
                edge_features[i, j, 11] = wp["levenshtein_distance"]
                
        return node_features, edge_features

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
