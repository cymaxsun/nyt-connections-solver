# Model System Architecture

This document defines the intended model, metric, report, and artifact architecture for the Connections solver after removing the redundant `previous best` checkpoint flow.

## Goals

1. Keep MLflow as the source of truth for metric history.
2. Keep local model artifacts self-identifying and load-safe.
3. Make every generated report clearly state exactly which model it evaluates.
4. Compare normal reports only against the all-time best model for the current feature schema.
5. Avoid ambiguous aliases such as `previous best`.

## Concepts

### Run model

A run model is the model produced or loaded by the current training/evaluation command. Reports should call this the **report model**, not `current`, because `current` becomes ambiguous once files are overwritten.

### All-time best model

The all-time best model is the highest-scoring GCN for the current feature schema and candidate-generation configuration. It is the only automatic baseline in normal validation reports.

### MLflow run

MLflow stores complete metric history, epoch-level metrics, artifacts, and run comparisons. Local JSON manifests should not duplicate the full MLflow metric history.

### Model manifest

A manifest is a small JSON identity card stored beside a model checkpoint. It should contain enough information to identify and validate the artifact before loading it.

## Recommended directory layout

```text
models/
  gcn_best.pt                         # mutable convenience alias for the latest run best
  gcn_all_time_best_v{schema}.pt       # schema-scoped all-time best GCN
  gcn_all_time_best_v{schema}.json     # all-time best manifest/metadata
  dqn_q_net.pt                         # current DQN alias
  dqn_q_net.json                       # recommended DQN manifest

visualizations/reports/
  candidates_summary.md                # report for the report model vs all-time best
  error_analysis.md                    # hardest-puzzle analysis for the report model
  model_comparison_report.md           # explicit ad hoc A/B report only
```

Longer term, prefer immutable run folders:

```text
models/runs/{model_id}/
  model.pt
  manifest.json
  candidates_summary.md
  error_analysis.md

models/aliases/
  current_gcn.json
  all_time_gcn_schema{schema}.json
  current_dqn.json
```

## Report rules

Every report should start with a report-subject header:

```text
Report model: models/gcn_all_time_best_v14.pt
Feature schema: 14
Validation split seed: 42
Selection metric: validation_selection_score
Baseline: models/gcn_all_time_best_v14.pt, if different from report model
Metric source: recomputed with current code
```

Normal validation reports should include these columns:

```text
Metric | Report Model | All-Time Best | Change vs All-Time
```

They should not include `Previous` or `Change vs Prev` columns.

## Metric ownership

MLflow owns:

- per-epoch train/validation loss,
- per-epoch validation MRR,
- per-epoch solver selection score,
- RL chunk metrics,
- final test metrics,
- historical run comparisons.

Local manifests own:

- model type,
- checkpoint path,
- feature schema version,
- node and edge feature dimensions,
- relation archetype schema version,
- candidate scoring/generation configuration,
- validation split seed,
- final selection score and a compact metric summary,
- MLflow run id when available.

Reports own:

- human-readable validation diagnosis,
- aggregate candidate/partition metrics for one report model,
- all-time baseline comparison,
- puzzle-level failure examples.

## Why previous-best was removed

`previous best` meant `gcn_best.pt` copied before the current training run. That is not the same as the previous epoch, the latest MLflow run, or the all-time best model. Because the concept is ambiguous and redundant with MLflow history plus all-time comparison, normal training/reporting should no longer create, load, display, or compare against `gcn_previous_best.pt`.

## Future cleanup

1. Add a DQN manifest and reject DQN checkpoints trained against incompatible GCN/candidate-feature configurations.
2. Add immutable model IDs to reports.
3. Save GCN checkpoints as bundles with `state_dict`, `metadata`, `training_config`, and `validation_stats`.
4. Normalize the GCN selection score to rates so it is stable across validation-set sizes.
5. Add failure-attribution sections to validation reports.
