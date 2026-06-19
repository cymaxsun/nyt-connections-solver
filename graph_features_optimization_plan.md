# Graph Formation Optimization Plan

This document outlines the proposed orthographic, phonetic, and collocational features to extend [features.py](file:///Users/maxsun/projects/connections/src/features.py) and improve GCN candidate group recall for NYT-style Connections puzzles.

## Concern Classification

Use these severity labels when turning this plan into implementation work:

| Severity | Meaning | Required action |
| --- | --- | --- |
| **P0 - Correctness bug** | Existing graph/training logic is broken or silently disables a feature. | Fix before adding new features or retraining checkpoints. |
| **P1 - Model-quality risk** | Logic runs, but strongly biases learning/candidate ranking or makes validation misleading. | Fix or explicitly benchmark before treating results as meaningful. |
| **P2 - Feature gap** | Missing signal that likely improves recall for specific Connections archetypes. | Add after P0/P1 issues are controlled. |
| **P3 - Operational/reproducibility** | Cache, preprocessing, or artifact behavior can make experiments stale or expensive. | Fix alongside the first implementation pass. |

### Current Major Flaws / Bugs to Fix First

| Concern | Severity | Location | Why it matters | Recommended fix |
| --- | --- | --- | --- | --- |
| Clue TF-IDF similarity is effectively dead code. `get_clue_similarity` returns `None` after cache/membership checks because the actual TF-IDF computation is indented after `get_sentence_embedding_similarity` and after an unconditional `return`. | **P0 - Correctness bug** | [src/features.py](file:///Users/maxsun/projects/connections/src/features.py#L115), [src/features.py](file:///Users/maxsun/projects/connections/src/features.py#L180) | Edge feature 4 is documented, preprocessed, thresholded, and fed to the GCN, but non-self clue similarities become `None`/0.0. This removes one of the few phrase/category context channels. | Move the TF-IDF lookup block back into `get_clue_similarity`; add a tiny regression check where two cached descriptions with shared terms produce a positive score. |
| Preprocessed graph staleness is detected only by `EDGE_FEATURE_DIM`. | **P0 - Correctness bug** | [src/train.py](file:///Users/maxsun/projects/connections/src/train.py#L37), [src/train.py](file:///Users/maxsun/projects/connections/src/train.py#L42) | Fixing feature logic without changing dimensionality will keep loading old `data/preprocessed_graphs.pt`, so validation can silently use stale/broken features. | Store a feature schema/version/hash in the preprocessed file and invalidate when feature extraction logic changes. At minimum, bump a `FEATURE_SCHEMA_VERSION` when fixing clue similarity or normalization. |
| GINE backbone builds a complete directed graph for every off-diagonal pair, including pairs whose relational adjacency vector is all zero. | **P1 - Model-quality risk** | [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L219), [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L224) | Sparsification in `get_multi_relational_adjacency` does not actually remove edges for GINE; zero-feature edges still allow message passing between unrelated words. This can wash out graph structure. | In `_dense_adj_to_pyg`, mask edges with `adj.permute(1, 2, 0).abs().sum(dim=-1) > 0` in addition to `src != dst`, or build `edge_index` from nonzero feature channels before row normalization. |
| Dense length-similarity channel connects nearly every word to nearly every other word after `1.0 - len_diff`. | **P1 - Model-quality risk** | [src/graph.py](file:///Users/maxsun/projects/connections/src/graph.py#L83), [src/graph.py](file:///Users/maxsun/projects/connections/src/graph.py#L99) | Length is weak evidence for most Connections groups. As a dense relation, it can dominate message passing and encourage grouping words by surface length rather than relation. | Threshold or downweight the length channel, or keep it as a pairwise scoring feature instead of a message-passing adjacency relation. |
| Self-loop signal is duplicated: relation channels include diagonal identity features while `RelationalGCNLayer` also has `W_self`. | **P1 - Model-quality risk** | [src/features.py](file:///Users/maxsun/projects/connections/src/features.py#L503), [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L35) | Sparse channels can become mostly self-loops after thresholding, reducing useful cross-word propagation and making relation weights partly redundant with `W_self`. | Consider zeroing diagonal relation adjacency before row normalization and relying on `W_self`, or benchmark both choices. |
| Candidate group score is the arithmetic mean of six pairwise probabilities. | **P1 - Model-quality risk** | [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L92), [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L108) | A candidate with one weak or unrelated pair can still rank high if the other edges are strong; this is common for broad semantic hubs. | Add minimum-edge, geometric mean, or learned quartet scoring; evaluate candidate recall@k and exact-group rank, not only average edge BCE. |
| Relation archetype head is trained only on positive edges and gets no explicit negative/unknown class. | **P1 - Model-quality risk** | [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L304), [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py#L318) | The head can produce confident archetype labels for arbitrary candidate groups because it never learns "not a valid relation." This mostly affects visualization and downstream candidate explanations, but can mislead debugging. | Keep it auxiliary-only, or add a `NO_RELATION` class / gate relation type by edge probability. |
| WordNet and sentence embedding caches are only saved by preprocessing, not ordinary on-the-fly graph builds. | **P3 - Operational/reproducibility** | [src/features.py](file:///Users/maxsun/projects/connections/src/features.py#L94), [src/preprocess.py](file:///Users/maxsun/projects/connections/src/preprocess.py#L62) | Interactive solving or raw-data training can recompute embeddings/WordNet features and produce slow, inconsistent runs if interrupted before preprocessing saves. | Add an explicit `FeatureExtractor.close()`/`save_caches()` call in training/CLI paths or periodically flush dirty caches. |

---

## 1. Orthographic & Sub-Word Features (for Morphology & Wordplay)

**Classification:** **P2 - Feature gap**, with one integration caveat: these features should not be added until the P0 feature-path bugs above are fixed and preprocessed schema invalidation exists.

These features help identify letter-level patterns, stripping/adding operations, and structural characteristics that dictionary definitions and semantic embeddings cannot see.

### Proposed Feature Details
* **Normalized Edit Distance (Jaro-Winkler or Levenshtein):**
  * *Logic:* Measure character distance to identify anagrams, spelling mistakes, or single-character edits.
  * *Formula:* $1.0 - (\text{LevenshteinDistance}(w_1, w_2) / \max(\text{len}(w_1), \text{len}(w_2)))$.
  * *Example:* *TICK* and *TICKLE* or *COLE* and *POLE*.
* **Letter Addition / Stripping (Prefix & Suffix Removal):**
  * *Logic:* Explicitly check if $w_1$ is identical to $w_2$ with its first or last letter removed.
  * *Example:* *PAIN* and *T-PAIN* (rapper minus first letter) $\to$ *PAIN* matches *PAIN*.
* **Interior Character n-Gram Jaccard Overlap:**
  * *Logic:* Tokenize words into character 2-grams or 3-grams, and calculate the Jaccard similarity of these sets.
  * *Example:* *SPRING* and *STRING* $\to$ bigrams `{'SP', 'PR', 'RI', 'IN', 'NG'}` vs `{'ST', 'TR', 'RI', 'IN', 'NG'}` (Jaccard: $0.43$).

---

## 2. Phonetic & Pronunciation Features (for Homophones & Rhymes)

**Classification:** **P2 - Feature gap**. This is likely high-value for WORDPLAY/MORPHOLOGY categories, but it requires careful fallback behavior for multi-word answers, proper nouns, abbreviations, and entries absent from CMU Dict.

Connections frequently features groups based on how words sound (homophones) or rhyme, which standard text representations miss.

### Proposed Feature Details
* **Homophone Relationship (CMU Dict Match):**
  * *Logic:* Use the Carnegie Mellon Pronouncing Dictionary (`nltk.corpus.cmudict`) to fetch phonetic transcriptions (phonemes). If two words share an identical phoneme sequence, set the edge to $1.0$.
  * *Example:* *HARE* `['HH', 'EH', 'R']` and *HAIR* `['HH', 'EH', 'R']` $\to 1.0$.
* **Rhyming Relationship (Sound-Alike Suffix):**
  * *Logic:* Compare the final $K$ phonemes of the words (particularly matching from the last stressed vowel phoneme to the end).
  * *Example:* *SIGHT* `['S', 'AY', 'T']` and *KITE* `['K', 'AY', 'T']` $\to 1.0$ (matching `['AY', 'T']`).

---

## 3. Idiom & Phrase Collocation Features (for Phrase Completion)

**Classification:** **P2 - Feature gap / P3 data-dependency risk**. Phrase-completion signal is important, but a naive pairwise bigram/PMI feature can miss the actual puzzle pattern, which is often "all four words share a hidden common prefix/suffix/completion" rather than each pair co-occurring directly.

Phrase completion groups (e.g. *___ CHICKEN*) consist of semantically disparate words that only group because they can precede or follow a common word.

### Proposed Feature Details
* **Bigram/Collocation Lookup:**
  * *Logic:* Measure if $w_1$ and $w_2$ frequently co-occur in the same idiomatic expressions or compound nouns using a local bigram index or Google Books Ngrams cache.
  * *Example:* *RUBBER* and *CHICKEN* or *FUNKY* and *CHICKEN*.
* **Pointwise Mutual Information (PMI):**
  * *Logic:* Calculate the PMI between word pairs in a large corpus to find highly correlated collocates.
  * *Formula:* $\text{PMI}(w_1, w_2) = \log \frac{P(w_1, w_2)}{P(w_1)P(w_2)}$.

---

## 4. Feature Matrix Integration

**Classification:** **P0/P1 integration risk**. Increasing `EDGE_FEATURE_DIM` is mechanically simple, but graph construction, adjacency normalization, checkpoint compatibility, preprocessing invalidation, and visualization labels all need coordinated updates.

We will extend `EDGE_FEATURE_DIM` (currently 11) to incorporate these new features.

```python
# Extended Edge Feature Indices:
# 11: Normalized Levenshtein similarity [0.0 - 1.0]
# 12: Is letter addition/removal match (Boolean)
# 13: Character bigram Jaccard similarity [0.0 - 1.0]
# 14: Is Homophone (Boolean)
# 15: Rhymes (Boolean)
# 16: Co-occurs in common phrase completion/bigrams (Boolean)
```

### Implementation Checklist
- [ ] Fix the existing P0 bugs before adding feature dimensions: restore clue TF-IDF similarity and add feature-schema invalidation for preprocessed graphs.
- [ ] Decide which channels should be message-passing adjacencies versus candidate-scoring-only features; downweight or threshold dense weak channels such as length similarity.
- [ ] If using `--gcn-backbone gine`, make `_dense_adj_to_pyg` drop zero-adjacency edges instead of creating a complete graph.
- [ ] Install the Pronouncing package or download the NLTK `cmudict` corpus.
- [ ] Add `extract_phonetic_features` and `extract_collocation_features` functions in [features.py](file:///Users/maxsun/projects/connections/src/features.py).
- [ ] Increase `EDGE_FEATURE_DIM` and map the new values in `build_graph_matrices`.
- [ ] Update graph adjacency handling for dimensions 11-16, including thresholds, inversions, diagonal behavior, and feature comments.
- [ ] Add small deterministic feature tests for each new channel and regression tests for existing channels.
- [ ] Re-run the preprocessing pipeline (`PYTHONPATH=. python src/preprocess.py`).
- [ ] Re-train the Relational GCN model (`PYTHONPATH=. python -u main.py --train --gcn-epochs 100 --rl-episodes 0`) and compare validation MRR, exact group recall@k, and candidate partition quality against the current checkpoint.
