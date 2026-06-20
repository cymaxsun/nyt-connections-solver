# Graph Formation Optimization Plan

This document tracks graph-feature fixes and future feature work for the Connections solver. The goal is simple: generate better 4-word candidate groups before the RL agent makes guesses.

## Status Summary

Use these labels when turning items into implementation work:

| Severity | Meaning | Required action |
| --- | --- | --- |
| **P0 - Correctness bug** | A feature or training path is broken or silently disabled. | Fix before trusting experiments. |
| **P1 - Model-quality risk** | Code runs, but the model can learn the wrong signal or validation can mislead us. | Fix or benchmark before treating results as meaningful. |
| **P2 - Feature gap** | A useful Connections signal is missing. | Add after the P0/P1 issues are under control. |
| **P3 - Operational/reproducibility** | Caches, artifacts, or scripts can make experiments stale or expensive. | Fix when touching the related pipeline. |

## Resolved Issues

### Clue TF-IDF Similarity Was Dead Code

**Status:** Resolved.  
**Severity:** P0 - Correctness bug.  
**Main files:** [src/features.py](file:///Users/maxsun/projects/connections/src/features.py), [tests/test_features.py](file:///Users/maxsun/projects/connections/tests/test_features.py).

`get_clue_similarity` was supposed to compare cached clue descriptions with TF-IDF. That code had slipped below `get_sentence_embedding_similarity`, after an unconditional `return`, so Python never reached it. In practice, edge feature `4` was mostly zero even though the rest of the pipeline treated it as a real feature.

Why this mattered: clue descriptions are one of the few features that can connect words by category context. For example, two words whose descriptions both mention “fruit” should get a positive clue-similarity score. With this bug, the GCN and raw graph scorer lost that signal.

What changed: the TF-IDF lookup now lives inside `get_clue_similarity`, missing words return `0.0`, and tests cover positive shared-description similarity plus missing-word fallback.

### Preprocessed Graphs Could Stay Stale After Feature Fixes

**Status:** Resolved.  
**Severity:** P0 - Correctness bug.  
**Main files:** [src/features.py](file:///Users/maxsun/projects/connections/src/features.py), [src/preprocess.py](file:///Users/maxsun/projects/connections/src/preprocess.py), [src/train.py](file:///Users/maxsun/projects/connections/src/train.py), [tests/test_train.py](file:///Users/maxsun/projects/connections/tests/test_train.py).

The training pipeline used to check only `EDGE_FEATURE_DIM` to decide whether `data/preprocessed_graphs.pt` was current. That is not enough. Many feature fixes change values without changing the number of feature columns.

Why this mattered: after fixing a feature bug, training could still load old preprocessed tensors. That would make validation look like it used the new code when it actually used stale graph features.

What changed: preprocessed puzzle records now include `feature_schema_version`, and the loader rejects preprocessed graphs when the stored schema does not match `FEATURE_SCHEMA_VERSION`. The current schema version is `3`.

### Dense Length Similarity Connected Too Many Words

**Status:** Resolved.  
**Severity:** P1 - Model-quality risk.  
**Main files:** [src/graph.py](file:///Users/maxsun/projects/connections/src/graph.py), [tests/test_graph.py](file:///Users/maxsun/projects/connections/tests/test_graph.py).

Feature `9` stores normalized length difference. The graph used `1.0 - len_diff` as a length-similarity adjacency. That made many unrelated pairs positive edges because most words on a board have roughly similar lengths.

Why this mattered: word length is weak evidence for most Connections groups. As a dense message-passing relation, it can make the graph look connected even when words have no real relation. This can blur useful sparse signals such as WordNet, clue TF-IDF, ConceptNet, or wordplay features.

What changed: the raw stored feature remains normalized length difference, but graph adjacency now converts it through one helper:

```python
length_similarity = 1.0 - normalized_len_diff
keep edge only if length_similarity >= 0.90
```

Tests cover equal-length pairs, below-threshold pairs, consistency between single-channel and multi-relational adjacency, and active-mask/adaptive-weight behavior.

### Raw Preprocessed Graph Candidate Baseline Added

**Status:** Resolved as a baseline tool; still needs tuning.  
**Severity:** P1 - Model-quality diagnostic.  
**Main files:** [src/raw_candidates.py](file:///Users/maxsun/projects/connections/src/raw_candidates.py), [tests/test_raw_candidates.py](file:///Users/maxsun/projects/connections/tests/test_raw_candidates.py).

The GCN can hide whether the hand-built graph features are useful. A raw candidate scorer gives us a direct baseline: collapse preprocessed pair features into one pair-score matrix, score every 4-word group by its six internal pair scores, and build full-board partitions from those groups.

Why this mattered: on a 40-puzzle smoke subset, raw candidate scoring beat the small GCN by a large margin:

| Method | Split | MRR |
| --- | --- | ---: |
| Raw graph candidate scorer | all 40 smoke puzzles | `0.1470` |
| Raw graph candidate scorer | smoke validation split | `0.0648` |
| Raw graph candidate scorer | smoke test split | `0.2066` |
| 3-epoch relational GCN | smoke validation split | `0.0066` |
| 39-epoch relational GCN | smoke validation split | `0.0072` |
| 39-epoch relational GCN | smoke test split | `0.0059` |

This does not mean raw scoring is good enough to solve the puzzle. Its best partitions are still weak. It does mean the raw features currently rank true groups better than the trained GCN on the smoke subset.

### Candidate Group Score Used A Simple Mean

**Status:** Resolved.  
**Severity:** P1 - Model-quality risk.  
**Main files:** [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py), [src/raw_candidates.py](file:///Users/maxsun/projects/connections/src/raw_candidates.py), [src/candidate_scoring.py](file:///Users/maxsun/projects/connections/src/candidate_scoring.py).

Candidate groups were scored by averaging the six internal pair scores. A group could rank high even if one word did not belong, as long as the other pairs were strong enough.

Why this mattered: Connections groups need all four words to fit. A simple mean can over-rank “three correct plus one hub word” candidates. The raw baseline results showed this pattern often: many top groups had `3/4` overlap but missed the exact group.

What changed: GCN candidates and raw graph candidates now use one shared quartet scorer:

```python
score = mean(pair_scores) - 0.25 * (max(pair_scores) - min(pair_scores))
score = clamp(score, 0.0, 1.0)
```

This keeps balanced groups at their original mean score while penalizing candidates with one or more weak internal pair links.

### Self-Loop Signal Is Duplicated

**Status:** Resolved in the default GCN adjacency path; smoke benchmark completed.  
**Severity:** P1 - Model-quality risk.  
**Main files:** [src/features.py](file:///Users/maxsun/projects/connections/src/features.py), [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py).

`build_graph_matrices` sets several diagonal relation features to `1.0`. The relational GCN layer also has `W_self`, which separately handles each node's own features.

Why this matters: the model gets two ways to pass “the node to itself.” After sparsification, some channels may contain mostly self-loops. That can make relation weights partly redundant with `W_self` and reduce cross-word signal.

What changed: stored edge features remain unchanged for cache compatibility, but `ConnectionsGraph.get_multi_relational_adjacency()` now zeros relation diagonals by default before row normalization. This makes the GCN rely on `W_self` for each node's own features. Benchmark code can still reproduce the old behavior with `include_self_loops=True`.

Existing GCN checkpoints should be treated as behavior-stale even if their tensor shapes still load. Retrain before trusting solve or training results with the default zero-diagonal adjacency.

Smoke benchmark: a 1-epoch in-memory run on 32 train puzzles and 8 validation puzzles produced weak ranking metrics for both variants, so this should not be treated as a final model-quality result.

| Variant | Val MRR | Recall@20 | Recall@50 | Best partition exact groups |
| --- | ---: | ---: | ---: | ---: |
| Zero diagonal relation adjacency | `0.0044` | `0.00%` | `6.25%` | `0.00/4` |
| Keep relation self-loops | `0.0058` | `3.12%` | `6.25%` | `0.00/4` |

Full retraining should still compare candidate recall@k, true-group MRR, and partition quality. Do not decide from BCE loss alone.

### Relation Archetype Head Has No Negative Class

**Status:** Resolved.  
**Severity:** P1 - Model-quality risk.  
**Main files:** [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py), [src/relation_archetypes.py](file:///Users/maxsun/projects/connections/src/relation_archetypes.py), [src/visualize.py](file:///Users/maxsun/projects/connections/src/visualize.py), [src/evaluate_archetypes.py](file:///Users/maxsun/projects/connections/src/evaluate_archetypes.py), [tests/test_gcn_scoring.py](file:///Users/maxsun/projects/connections/tests/test_gcn_scoring.py).

The auxiliary relation-type head is trained only on true positive edges. It learns labels such as `SYNONYM`, `WORDPLAY`, and `TRIVIA_ENCYCLOPEDIC`, but it never learns “these two words are not related.”

Why this matters: the visualizer can show confident relation labels for bad candidate groups. That can mislead debugging because the label may look meaningful even when the pair should have been rejected.

What changed: relation archetypes now live in one shared module and include `NO_RELATION` as class `0`. GCN relation logits widened from 5 to 6 outputs. Training and validation label every off-diagonal cross-category pair as `NO_RELATION` and still ignore only the diagonal. Visualization and candidate summaries use the shared label list, so bad or uncertain groups can surface `NO_RELATION` instead of forcing a positive archetype.

Existing GCN checkpoints with a five-class relation head are architecture-stale and will be rejected by checkpoint compatibility checks. Retrain before using solve or validation artifact generation.

### GCN Training Used Only Pairwise Edge Loss

**Status:** Resolved as a first groupwise-training pass.  
**Severity:** P1 - Model-quality risk.  
**Main files:** [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py), [tests/test_gcn_scoring.py](file:///Users/maxsun/projects/connections/tests/test_gcn_scoring.py).

The GCN was trained to predict whether each pair of words belongs together, but candidate generation ranks 4-word groups. Pairwise BCE is a useful local signal, but it does not directly push exact quartets above near-miss groups.

What changed: GCN train and validation loss now include a groupwise margin-ranking term. The model learns pairwise edges, scores all 1,820 candidate 4-word groups, and pushes the four true groups above the highest-scoring false groups by a margin. This uses the same penalized group scorer used during candidate generation.

Follow-up comparison: relation-archetype classification loss is currently weighted at `0.0` so it does not influence GCN training. This isolates whether pairwise-plus-groupwise training improves candidate ranking without the auxiliary relation objective.

Benchmark note: this changes the training objective but not tensor shapes. Retrain before comparing candidate recall@k, true-group MRR, and partition quality against earlier pairwise-only runs.

## Open Issues To Fix Next

### GCN Representation Collapse & Embedding Oversmoothing

**Status:** Open (Diagnosis complete).  
**Severity:** P1 - Model-quality risk (Critical).  
**Main files:** [src/gcn.py](file:///Users/maxsun/projects/connections/src/gcn.py), [src/candidate_scoring.py](file:///Users/maxsun/projects/connections/src/candidate_scoring.py).

**Why this mattered:**  
When `GROUPWISE_LOSS_WEIGHT` was increased from `0.5` to `1.0` in Phase 6, GCN candidate ranking performance collapsed. On validation puzzles, the Validation MRR dropped to `0.0395` (down from the previous best of `0.0967` and the raw feature baseline of `0.1458`).

Diagnostic analysis of the saved model weights and inference embeddings revealed that:
1. **Oversmoothing**: The GCN's final node embeddings became completely identical to each other, with a mean pairwise cosine similarity of **`0.991464`** (minimum `0.967473`).
2. **Probability Collapse**: Because the node embeddings were identical, the pairwise edge scoring head received identical inputs for all pairs. This forced all edge probabilities to collapse to exactly **`0.5001 ± 0.0001`**, rendering GCN predictions completely flat and non-informative.

**Root Causes:**
* **The Hinge Loss "Shortcut"**: GCN ranking is trained using a margin hinge loss: `F.relu(margin - true_scores + hard_negative_scores)`. A model that tries to learn features but makes mistakes yields a high loss (`~0.4 - 0.5`). However, if the GCN collapses all node embeddings to be identical, then every group (true and negative) gets the exact same score. The hinge loss immediately drops to exactly `margin = 0.05`! This makes the collapsed state a powerful local attractor (minimum) that the model easily falls into. Once collapsed, any attempt to diverge node embeddings creates variance, raising the loss back up, trapping the model.
* **Spread Penalty Gradient Contradiction**: The candidate scoring function uses `mean - 0.25 * (max - min)`. Backpropagating the spread penalty during GCN training causes bad gradients: for true groups, the gradient pushes the maximum edge down and minimum up (equalizing them). For negative groups, the gradient pushes the maximum edge **up** to maximize spread (which actively trains false links to have high probability!). These forces conflict across the 1820 combinations and result in a collapsed flat representation.
* **Scale and Gradient Overwhelm**: While BCE gradients shrink to 0 as the model predicts correctly, the ranking hinge loss maintains a constant gradient magnitude as long as any margin violation exists. At weight `1.0`, these constant ranking gradients completely overwhelm the shrinking BCE gradients, forcing the model to collapse.
* **Metadata Bottleneck**: The GCN only receives 7 non-semantic metadata node features (e.g., word length, plural suffix), while throwing away the 12 rich semantic/lexical edge similarities. Bottlenecking all information through 16-dimensional node embeddings makes it very hard to learn, further incentivizing the model to take the collapse shortcut.

**Recommended fixes:**
1. **Training Score Simplification**: Compute `groupwise_ranking_loss` using the raw **mean** of the 6 edges in the group, bypassing the spread penalty during training (but keeping it for validation/inference). This removes the gradient contradictions.
2. **Smooth Ranking Loss**: Replace the hard ReLU hinge loss with a soft margin loss (`F.softplus(margin - true_scores + negative_scores)`) so that gradients naturally scale down as the margin violation decreases.
3. **Lower Ranking Weight**: Scale down `GROUPWISE_LOSS_WEIGHT` to `0.1` or `0.2` to balance it with BCE.
4. **Edge-Conditioned Scoring**: Concatenate the raw edge features directly with the node embeddings in the edge scoring head: `edge_input = torch.cat([h_exp1, h_exp2, raw_edge_features], dim=-1)` so the model doesn't throw away the 12 semantic similarities.

### Caches Are Saved Mainly By Preprocessing

**Status:** Open.  
**Severity:** P3 - Operational/reproducibility.  
**Main files:** [src/features.py](file:///Users/maxsun/projects/connections/src/features.py), [src/preprocess.py](file:///Users/maxsun/projects/connections/src/preprocess.py), [main.py](file:///Users/maxsun/projects/connections/main.py).

WordNet and sentence embedding caches are saved at the end of preprocessing. Interactive solving and raw-data training can still compute features on the fly.

Why this mattered: if a run computes many features and then exits before preprocessing saves caches, later runs may repeat slow work. That makes experiments slower and less reproducible.

Recommended fix: add an explicit `FeatureExtractor.save_caches()` method and call it from training, preprocessing, and CLI solve paths. Prefer explicit lifecycle management over relying on `__del__`.

## Feature Gaps To Add Later

Do not add new feature dimensions until the open P1 graph/model issues have a benchmark or fix. Increasing `EDGE_FEATURE_DIM` requires coordinated changes to preprocessing, checkpoint compatibility, graph normalization, raw candidate scoring, and visualization labels.

### 1. Orthographic And Sub-Word Features

**Classification:** P2 - Feature gap.

These features help with morphology and wordplay categories that semantic embeddings often miss.

- **Normalized edit distance:** score words by character edits, such as `TICK` and `TICKLE`.
- **Letter addition/removal:** detect one-letter prefix or suffix changes.
- **Character n-gram overlap:** compare character bigrams or trigrams, such as `SPRING` and `STRING`.

### 2. Phonetic And Pronunciation Features

**Classification:** P2 - Feature gap.

Connections often uses sound-based groups. Text embeddings usually miss homophones and rhymes.

- **Homophone match:** use CMU Dict phoneme sequences, such as `HARE` and `HAIR`.
- **Rhyme match:** compare the suffix from the last stressed vowel, such as `SIGHT` and `KITE`.

Handle multi-word answers, proper nouns, abbreviations, and words missing from CMU Dict with clear fallbacks.

### 3. Idiom And Phrase Collocation Features

**Classification:** P2 - Feature gap / P3 data-dependency risk.

Phrase-completion groups often connect words because all four share a hidden prefix, suffix, or completion. Pairwise co-occurrence alone may miss that pattern.

- **Bigram/collocation lookup:** use a local phrase or n-gram index to find common compounds.
- **PMI score:** estimate whether two words co-occur more often than chance.
- **Shared completion search:** look for one hidden word that works with all four candidate words, not just pairwise matches.

## Feature Matrix Integration Checklist

- [x] Restore clue TF-IDF similarity.
- [x] Store and validate `FEATURE_SCHEMA_VERSION` in preprocessed graphs.
- [x] Bump `FEATURE_SCHEMA_VERSION` after graph-feature behavior changes.
- [x] Sparsify the length-similarity adjacency channel.
- [x] Add deterministic tests for clue TF-IDF, schema invalidation, length sparsification, and raw candidate scoring.
- [x] Add a raw preprocessed graph candidate baseline.
- [x] Benchmark diagonal relation adjacency versus relying on `W_self`.
- [x] Replace or supplement arithmetic-mean group scoring.
- [x] Add a `NO_RELATION` class to the relation archetype head.
- [x] Add groupwise ranking loss to GCN training.
- [ ] Fix GCN collapse by using mean-only groupwise loss during training.
- [ ] Replace ReLU hinge loss with softplus smooth ranking loss in GCN training.
- [ ] Add raw edge features to the GCN edge scoring head to bypass the metadata bottleneck.
- [ ] Add explicit cache-saving lifecycle methods.
- [ ] Add orthographic, phonetic, and collocation feature dimensions.
- [ ] Re-run full preprocessing after the next feature-schema bump.
- [ ] Retrain and compare using candidate recall@k, true-group MRR, and partition quality.

## Current Experiment Takeaway

The raw preprocessed graph baseline is the best current candidate-generation signal. Relational GCN training has suffered from representation collapse and embedding oversmoothing when groupwise ranking loss is heavily weighted (`GROUPWISE_LOSS_WEIGHT = 1.0` or `0.5`). This is caused by the model taking a "collapse shortcut" to minimize hinge loss and gradient conflicts from the spread penalty. The next development phase must implement training score simplification (mean-only ranking loss), smooth softplus loss, and edge-conditioned scoring before retraining and comparing GCN candidates against the raw baseline.
