# Node Feature Expansion Opportunities

## Current Node Features (775 dims)

Each node currently carries **7 metadata scalars** + a **768-dim SentenceTransformer embedding**:

| Dim | Feature | Source | Notes |
|-----|---------|--------|-------|
| 0 | `polysemy_count` | WordNet | Number of synsets |
| 1 | `word_len` | Literal | Character count |
| 2 | `is_plural` | Heuristic | Ends in 'S' and len > 3 |
| 3 | `has_noun` | WordNet POS | Binary |
| 4 | `has_verb` | WordNet POS | Binary |
| 5 | `has_adj` | WordNet POS | Binary |
| 6 | `clue_len` | LLM clue cache | Length of cached description |
| 7–774 | ST embedding | all-mpnet-base-v2 | Normalized 768-d |

> [!NOTE]
> The metadata features (dims 0–6) are mostly **word-intrinsic** — they describe properties of each word in isolation. There is almost **no board-context information** encoded per-node, and no phonetic, morphological, or frequency-based signals.

---

## What's Missing — Grouped by Category

### 1. Morphological / Orthographic (targets: WORD_FORM, SOUND_OR_SPELLING, WORDPLAY_TRANSFORM)

These archetypes are at **0% group accuracy** and near-zero MRR. The model has no per-node features to distinguish morphologically interesting words.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`num_syllables`** | Syllable count | Words in FILL_IN_THE_BLANK and COMMON_PHRASE often share syllable-count patterns | **Weak** | Words in phrase/blank categories do not share syllable count patterns except by random coincidence (e.g. `___ TICKET` has 3, 3, 1, 2 syllables). |
| **`has_silent_letters`** | Binary: common silent-letter patterns (e.g. KNIGHT, GNOME) | Helps SOUND_OR_SPELLING homophones | **Weak** | Silent letters are common in English generally; it does not help cluster words unless the category itself is explicitly "Words with silent letters". |
| **`is_compound_fragment`** | Binary or count: checks if the word is a valid prefix/suffix of known compounds | FILL_IN_THE_BLANK often uses compound word constituents | **Strong** | While board words themselves are rarely compounds, they are frequently the single-morpheme fragments that combine with a hidden target word (e.g., *surf*, *card*, *back* all form compounds with *board*). Measuring a word's "compound valence" against a standard lexicon captures this. |
| **`vowel_ratio`** | Vowels / total length | Phonetic similarity proxy | **Weak** | A crude spelling proxy. If words rhyme or share non-semantic traits, their vowel ratios can still vary wildly. |
| **`consonant_cluster_count`** | Consecutive-consonant runs ≥ 2 | Groups words by phonetic texture | **Weak** | Too generic to serve as a meaningful clustering signal for spelling-based groups. |
| **`is_palindrome`** | Binary | Captures WORD_FORM patterns | **Strong** | Directly represents a classic, recurring Connections category type (e.g., `KAYAK`, `LEVEL`, `MOM`, `RACECAR`). |
| **`has_double_letter`** | Binary: any repeated adjacent letter (BOOK, JAZZ) | Orthographic signal | **Strong** | Directly maps to recurring orthographic categories (e.g. "double letter words"). |

### 2. Phonetic Encoding (targets: SOUND_OR_SPELLING — 0% group accuracy, 2.7% MRR)

The model currently has **zero phonetic information**. Homophones and rhymes are invisible.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **Soundex / Metaphone / Rhyme / Phoneme hashes** | Standard phonetic hashes and rhyming group IDs | Words that sound alike get matched | **Weak as Node Features (Must be Edge Features)** | 1. For homophone sets like letters (*BEE*, *SEA*, *TEA*, *WHY*) or numbers (*WON*, *TOO*, *FOR*, *ATE*), the board words do not sound like each other. Direct phonetic hashes of board words will fail to match them.<br>2. Phonetic relationships are inherently *pairwise*. Adding them as edge weights in the multi-relational adjacency matrix is much more powerful than forcing the GCN to map disparate node features. |

#### Algorithm: Resolving Indirect Homophones (Sound's Semantic Context)
To identify indirect homophone groups (e.g. words on the board sounding like letters or numbers), we can execute a four-step pipeline:
1. **Phonetic Lookup**: Map board words to their phonemes via a dictionary like NLTK's CMUDict (e.g. `BEE` $\rightarrow$ `/B IY1/`).
2. **Reverse Lexicon Search**: Retrieve all spelling variants (homophones) for that pronunciation (e.g. `/B IY1/` $\rightarrow$ `{"BEE", "BE", "B"}`).
3. **Candidate Embedding**: Fetch dense embeddings (via `SentenceTransformers`) for every variant in the homophone sets.
4. **Cohesion Optimization**: Evaluate combinations of candidate words to find the set of homophones with the highest average semantic similarity:
   * Combination A: `{"BEE", "SEA", "TEA", "WHY"}` $\rightarrow$ Cosine Similarity $\approx 0.15$ (Weak context)
   * Combination B: `{"B", "C", "T", "Y"}` $\rightarrow$ Cosine Similarity $\approx 0.85$ (Strong context: "Alphabet letters")

### 3. Board-Context Features (targets: all — currently no context-awareness)

Every node feature is currently computed **independently of the other 15 words on the board**. This misses important distributional signals.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`board_word_len_percentile`** | Length rank among the 16 words (0–1) | Length-based categories cluster by relative position | **Weak** | Relative ranks have no logical relation to category definitions (e.g. dog breeds are dog breeds regardless of the other words). |
| **`board_polysemy_percentile`** | Polysemy rank among the 16 words | High-polysemy words tend to be "decoy" connectors | **Weak** | Same as length; does not logically define groups. |
| **`board_st_centroid_distance`** | Cosine distance to the board's mean ST embedding | Outliers are often in wordplay categories | **Very Strong** | Since boards usually have three semantic groups and one wordplay group, wordplay words act as semantic outliers on the board. Distance to the board centroid is a great outlier proxy. |
| **`board_st_cluster_id`** | k-means cluster assignment (k=4) | Pre-clusters nodes into 4 groups | **Weak (Target Leakage Risk)** | Pre-clustering 16 words into 4 clusters using k-means introduces severe target leakage since the true answer is exactly 4 clusters of 4. |
| **`board_st_cluster_distance`** | Distance to assigned cluster center | Confidence of the unsupervised clustering | **Weak** | Correlated with the target leakage of cluster ID. |
| **`board_avg_edge_weight`** | Mean of this node's 15 edge weights | Hub-ness indicator — helps detect decoy words | **Strong** | Directly models the concept of "decoy words" (nodes connecting strongly to multiple target groups). |
| **`board_max_edge_weight`** | Max edge weight to any other node | How strongly this word connects to its best partner | **Strong** | Helps detect isolated word pairs or triplets. |

### 4. Knowledge-Graph Derived (targets: NAMED_ENTITY_SET — 0.8% pairwise, SEMANTIC_SET — 6.3%)

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`conceptnet_degree`** | Number of ConceptNet edges | Named entities have distinctive degree distributions | **Medium** | Captures overall connectivity, but is highly sensitive to local database/cache incompleteness. |
| **`conceptnet_is_a_count`** | Count of `IsA` relations in ConceptNet | Semantic set members share `IsA` parents | **Strong** | Identifies member-of-class relationships (e.g., types of colors, shapes, materials). |
| **`wordnet_depth`** | Max depth in WordNet taxonomy tree | Abstract vs concrete distinction | **Strong** | WordNet depth represents the abstraction level of concepts. Connections categories are highly homogeneous in concreteness/abstraction (e.g., a category is either all concrete objects or all abstract concepts). |
| **`wordnet_domain_tags`** | Domain labels (sport, music, food…) | Directly encodes topical category membership | **Strong** | Directly maps to topical or domain-themed categories. |
| **`is_proper_noun`** | Binary: capitalized or in a known entity list | Named entities are structurally different | **Strong (Requires Gazetteer)** | Capitalization heuristics cannot be used because all board inputs are capitalized. Requires a robust gazetteer/named-entity lookup dictionary. |

### 5. Frequency / Register (targets: COMMON_PHRASE — 0% accuracy, FILL_IN_THE_BLANK — 0% group)

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`word_frequency`** | Log word frequency from a corpus | Common phrases use high-frequency words | **Strong** | Wordplay categories (anagrams, homophones) are almost exclusively restricted to common words. Obsolescent/rare words are usually technical terms or proper nouns. |
| **`has_adverb_pos`** | Binary: WordNet adverb synsets exist | Expands POS coverage | **Medium** | Helps enforce parts-of-speech homogeneity within groups. |

---

## Recommended Priority Order

1. **Palindromes & Double Letters (Morphological)** — High logical strength, easy to implement cleanly without external libraries or caching concerns. Targets `WORD_FORM` and `WORDPLAY_TRANSFORM`.
2. **Semantic Centroid Distance & Edge Weight Stats (Board-Context)** — High logical strength for identifying non-semantic wordplay groups and decoy words. Must be computed statically at the start of a board to avoid RL state representation shifts.
3. **Word Frequency & WordNet Depth (Register / KG)** — Strong indicators of group abstraction level and word playability. High coverage and minimal overhead.
4. **Phonetic Edge Features (Phonetics)** — Moving phonetic features from node features to **edge weights** (e.g. phoneme edit distance and Metaphone matches). This correctly treats phonetics as pairwise connections and addresses the `SOUND_OR_SPELLING` archetype.
