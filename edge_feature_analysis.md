# Edge Feature Expansion Opportunities

## Current Edge Features (12 dims)

Each edge `(i, j)` carries 12 features encoding pairwise relationships between words:

| Dim | Feature | Source | Range | Adjacency Threshold |
|-----|---------|--------|-------|---------------------|
| 0 | WordNet path similarity | Max over synset pairs | [0, 1] | ≥ 0.15 |
| 1 | WordNet shares hypernym | Binary: any synset pair shares direct hypernym | {0, 1} | — |
| 2 | ConceptNet forward weight | Max weight where w_j in w_i's edges | [0, ~2] | — |
| 3 | ConceptNet backward weight | Max weight where w_i in w_j's edges | [0, ~2] | — |
| 4 | Clue TF-IDF similarity | Cosine sim of LLM description TF-IDF vectors | [0, 1] | ≥ 0.10 |
| 5 | Is anagram | Binary: sorted letters match | {0, 1} | — |
| 6 | Shares prefix | Binary: common prefix ≥ 3 chars | {0, 1} | — |
| 7 | Shares suffix | Binary: common suffix ≥ 3 chars | {0, 1} | — |
| 8 | Is substring | Binary: one word contains the other | {0, 1} | — |
| 9 | Length difference | `|len(w1)-len(w2)| / max(len)` | [0, 1] | ≥ 0.90 sim |
| 10 | SentenceTransformer cosine sim | Dot product of normalized `all-mpnet-base-v2` | [-1, 1] | ≥ 0.25 |
| 11 | Levenshtein distance | Normalized edit distance | [0, 1] | ≥ 0.75 sim |

### How edge features flow through the model

Edge features serve **three distinct roles** in the architecture:

1. **Relational adjacency** — Each of the 12 dims becomes a separate 16×16 adjacency matrix (after sparsification + row normalization). The `RelationalGCNLayer` learns a separate weight matrix `W_rel[r]` per relation channel. Messages are: `Σ_r adj[r] × H × W_rel[r]`.
2. **Edge scoring head** — Raw (unsparsified) edge features are concatenated with GCN node embeddings: `[h_i ‖ h_j ‖ raw_edge[i,j]]` → 44 dims → MLP → link logit + relation logit.

3. **Group scoring head** — For each quartet, the 6 internal edge feature vectors are pooled: `[mean_pool ‖ max_pool]` → 24 dims, concatenated with node summaries → 56 dims → MLP → group archetype logit.

> [!NOTE]
> Raw edge features bypass the GCN entirely in the scoring heads. This means new edge features get **immediate, direct access** to link prediction and archetype classification without needing to propagate through message passing first. Adding edge features is high-leverage.

---

## What's Missing — Grouped by Category

### 1. ConceptNet Relation-Type Decomposition (targets: SEMANTIC_SET 6.3%, NAMED_ENTITY_SET 0.8%)

**The biggest wasted data source.** The ConceptNet cache (`data/conceptnet_cache.json`, 232MB) contains rich relation-type information that is **completely discarded** — the current code only extracts the max scalar weight regardless of relation type.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`cn_is_a_weight`** | Max weight of `IsA` edges between word pair | Directly encodes taxonomy | **Very Strong** | Subclass membership (e.g. *poodle* IsA *dog*) is a core semantic category archetype. |
| **`cn_synonym_weight`** | Max weight of `Synonym` edges | SYNONYM_OR_NEAR signal independent of WordNet | **Very Strong** | Directly targets synonymy, but captures modern slang/contexts much better than WordNet. |
| **`cn_related_to_weight`** | Max weight of `RelatedTo` edges | Broad semantic association | **Medium** | Captures generic semantic relatedness, but can introduce substantial noise. |
| **`cn_has_context_match`** | Binary: words share a `HasContext` tag | Named entities often share context | **Very Strong** | Categories are often defined by a shared context (e.g. "Words in golf", "Theater terms"). |
| **`cn_derived_from_weight`** | Max weight of `DerivedFrom` / `FormOf` edges | Morphologically derived words | **Strong** | Identifies grammatical mutations and word form variations. |
| **`cn_etymological_weight`** | Max weight of `EtymologicallyRelatedTo` | Shared etymology links | **Weak** | Puzzles are built for a general audience and almost never group words by obscure historical etymological roots. |
| **`cn_antonym_weight`** | Max weight of `DistinctFrom` | Antonyms negative signal | **Incorrect** | **Incorrect Assumption:** Antonyms often form valid Connections categories under the theme "Opposites" (*UP*/*DOWN*, *YES*/*NO*). Treating them as a negative signal is a game-logical error. |

This replaces dims 2–3 (which collapse all relation types into a single scalar) with ~7 type-specific channels. The raw data already exists in the cache — this is pure parsing logic, zero API calls.

### 2. Additional WordNet Similarity Metrics (targets: SYNONYM_OR_NEAR, SEMANTIC_SET)

Currently only 2 of ~10 available WordNet similarity measures are used.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`wn_wup_similarity`** | Wu-Palmer similarity (LCS depth-based) | Often more discriminative | **Redundant** | WordNet path similarity is already included. Wu-Palmer is mathematically different but conceptually redundant and adds no new logical information. |
| **`wn_lch_similarity`** | Leacock-Chodorow similarity | Better calibrated for deep taxonomy | **Redundant** | Same as Wu-Palmer; adds redundancy rather than new logical dimensions. |
| **`wn_pos_match`** | Binary: best-matching synsets share the same POS | Mixed-POS pairs are less likely same-category | **Strong** | Enforces POS homogeneity, a major negative constraint in Connections groups. |
| **`wn_shared_hypernym_depth`** | Depth of lowest common subsumer | Shallow LCS = generic; deep LCS = specific | **Strong** | Shallow common ancestors (e.g., *entity*) are noise; deep common ancestors (e.g., *instrument*) are strong groups. |
| **`wn_meronym_overlap`** | Binary: any part/whole relation | Part-whole relationships indicate semantic sets | **Strong** | Directly targets part-whole categories (e.g., "Parts of a flower"). |
| **`wn_antonym`** | Binary: any lemma-level antonymy | Antonyms don't group | **Incorrect** | **Incorrect Assumption:** Same as ConceptNet antonyms; "Opposites" is a very common category theme. |
| **`wn_definition_overlap`** | Token overlap between glosses (Lesk-like) | General semantic similarity | **Medium** | Coarse proxy for description overlap, but clue cache similarity is much richer. |

### 3. Phonetic Similarity (targets: SOUND_OR_SPELLING — 0% group accuracy, 2.7% MRR)

There are currently **zero pairwise phonetic features**. This is the single most absent signal category.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`soundex_match`** | Binary: same Soundex code | Words that sound alike get same code | **Medium** | Crude phonetic hashing; edit distance on phonemes is much more precise. |
| **`metaphone_match`** | Binary: same Double Metaphone primary code | More accurate phonetic hashing | **Medium** | Better than Soundex, but still discrete compared to edit distance. |
| **`phoneme_edit_distance`** | Normalized edit distance on CMU dict phoneme sequences | Continuous phonetic similarity measure | **Very Strong** | Directly models rhymes and near-homophones. |
| **`rhyme_match`** | Binary: same final syllable phonemes | Rhyming pairs | **Very Strong** | Rhyming is a very common sound-based category style. |
| **`phoneme_overlap_ratio`** | Jaccard similarity of phoneme sets | Bag-of-phonemes similarity | **Medium** | Captures phonetic texture similarities. |

*Note: For indirect homophone groups (e.g. *BEE*, *SEA*, *TEA*, *WHY* sounding like letters), these pairwise phonetic metrics will output 0.0 because the board words themselves do not sound alike. Solving indirect homophones requires checking if the words' individual homophone sets intersect with a common semantic class.*

### 4. N-gram / Collocation Features (targets: FILL_IN_THE_BLANK — 0% group; COMMON_PHRASE — 0%)

These archetypes require knowing that words frequently appear next to a common "hidden" word. No current feature captures this.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`shared_bigram_partner_count`** | Count of common high-PMI bigram partners | If POPCORN, RUBBER, SPRING all collocate with "CHICKEN" | **Very Strong** | Directly models the exact reasoning players use to solve "words that precede/follow X" groups. |
| **`shared_trigram_context`** | Binary: both words complete "___X" or "X___" | Directly models fill-in-the-blank | **Strong** | Identifies specific multi-word contexts. |
| **`pmi_with_common_words`** | Max PMI of each word with connector words | Context collocations | **Medium** | Useful but noisier than counting explicit shared collocates. |

> [!WARNING]
> These require an external n-gram corpus (e.g., Google Books bigrams, or a pre-computed PMI table). This is the highest-effort category but targets the two weakest archetypes.

### 5. Clue Cache Enrichment (targets: all non-semantic archetypes)

The LLM clue cache has rich text descriptions per word, but only TF-IDF cosine similarity is extracted. More structured features could be derived.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`clue_named_entity_overlap`** | Count of shared named entities in descriptions | NAMED_ENTITY_SET members share entity class | **Strong** | Helps group words belonging to specific classes (e.g., actors, city names). |
| **`clue_category_word_overlap`** | Jaccard overlap of category-indicator words | Cheap proxy for domain matching | **Medium** | Good fallback for domain mapping. |
| **`clue_semantic_sim`** | SentenceTransformer cosine of full descriptions | Richer than TF-IDF | **Very Strong** | Captures paraphrase-level definitions of words that share deep dictionary semantics. |

### 6. Orthographic / String Pattern Features (targets: WORDPLAY_TRANSFORM, WORD_FORM)

Current orthographic features (dims 5–9, 11) cover basics but miss several patterns.

| Proposed Feature | Description | Why It Helps | Logical Strength | Game-Logical Reasoning |
|---|---|---|---|---|
| **`shared_infix`** | Binary: share a substring ≥ 3 chars not at prefix/suffix | Hidden-word patterns | **Strong** | Captures "words containing other words" (e.g. PINEAPPLE contains APPLE). |
| **`letter_set_jaccard`** | Jaccard similarity of character sets | Near-anagrams | **Medium** | Useful for character distribution checks. |
| **`consonant_skeleton_match`** | Binary: same consonant sequence | Morphological variant detection | **Strong** | Targets groups where words share consonants but swap vowels (*STRIP*, *STRAP*, *STRIPE*). |
| **`reverse_substring`** | Binary: one word contains the reverse of another | Reversal patterns | **Medium** | Reversals are rare but exist as categories. |
| **`common_transformation`** | Binary: one word becomes another via a transform | Targets WORDPLAY_TRANSFORM | **Very Strong** | Captures mutations like adding E to make a new word (*PLAN*/*PLANE*). |

---

## Impact vs Effort Matrix

| Feature Group | Dims Added | Data Source | Effort | Expected Impact |
|---|---|---|---|---|
| **ConceptNet relation decomposition** | ~7 (replaces 2) | Already cached (232MB) | **Low** — parsing only | **Very High** — largest wasted data source |
| **Phonetic similarity** | ~5 | nltk CMU dict + `fuzzy` lib | **Medium** | **Very High** — targets 0% archetype |
| **Additional WordNet metrics** | ~7 | WordNet (already loaded) | **Low** | **Medium** — incremental gains on synonyms/semantics |
| **Clue cache enrichment** | ~3 | Already cached (567KB) | **Low** | **Medium** — richer description comparison |
| **Orthographic patterns** | ~5 | String heuristics | **Low** | **Medium** — targets WORDPLAY_TRANSFORM |
| **N-gram / collocation** | ~3 | External corpus needed | **High** | **High** — only path to FILL_IN_THE_BLANK |

---

## Architecture Implications

Adding edge features increases `EDGE_FEATURE_DIM` which affects:

1. **`RelationalGCNLayer.W_rel`** — shape `(num_relations, in, out)`. More relation channels = more parameters. The current 12 channels are manageable; going to ~25-30 is still fine.

2. **Edge scoring head input** — currently `16+16+12 = 44`. Adding 15 edge dims → `16+16+27 = 59`. Still small.

3. **Group scoring head input** — currently `32+24 = 56`. Would become `32 + 27*2 = 86`. Still small.

4. **Adjacency sparsification** — new continuous features need threshold decisions. Binary features need none.

5. **Preprocessing cache** — `FEATURE_SCHEMA_VERSION` must be bumped. `preprocessed_graphs.pt` will need regeneration (~100MB).

> [!IMPORTANT]
> The most important observation: **ConceptNet relation-type decomposition** is pure upside. The data is already cached, the code already queries it, but then throws away all the relation type information and keeps only the max weight. Decomposing this into ~7 type-specific channels is the single highest-ROI edge feature change.

---

## Recommended Priority Order

1. **ConceptNet relation decomposition** — Replace the 2 collapsed scalar weights with ~7 relation-type-specific channels. Already cached, parsing-only change, directly helps SEMANTIC_SET and NAMED_ENTITY_SET.

2. **Phonetic pairwise features** — Add Soundex/Metaphone match + phoneme edit distance. The only way to make SOUND_OR_SPELLING (0% accuracy) detectable.

3. **Additional WordNet metrics** — Wu-Palmer, shared hypernym depth, POS match. Low effort, incremental gains.

4. **Orthographic patterns** — Shared infix, letter set Jaccard, consonant skeleton. Cheap heuristics targeting WORDPLAY_TRANSFORM.

5. **Clue cache enrichment** — SentenceTransformer similarity of full descriptions, entity overlap. Low effort.

6. **N-gram collocations** — Highest effort but the only path to solving FILL_IN_THE_BLANK and COMMON_PHRASE. Consider as a Phase 10 project.
