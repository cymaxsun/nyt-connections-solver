# Repository Guidelines

## Project Structure & Module Organization

This repository is a Python solver for NYT-style Connections puzzles using graph features, a GCN, and a DQN agent. `main.py` is the CLI entry point. Core implementation lives in `src/`: `dataset.py` loads puzzle data, `features.py` builds lexical features, `graph.py` creates graph inputs, `gcn.py` defines and trains the graph model, `env.py` models game state, `rl_agent.py` trains the DQN agent, and `visualize.py`/`visualize_dataset.py` generate plots. Data and caches live in `data/`, trained weights in `models/`, and generated plots or reports in `visualizations/`.

## Build, Test, and Development Commands

Use the project virtual environment for all Python commands. If `.venv/` already exists, activate it or call its interpreter directly:

```bash
source .venv/bin/activate
.venv/bin/python -m compileall main.py src tests
```

If `.venv/` does not exist, create it and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After activation, `python` should resolve to the virtualenv interpreter. If it does not, use `.venv/bin/python` explicitly. Run the CLI help with `python main.py`. Train both models with:

```bash
python main.py --train --gcn-epochs 20 --rl-episodes 300
```

> [!NOTE]
> When running training scripts in the background or redirecting their output to a log file, Python block-buffers standard output by default, meaning logs won't appear in real time. To bypass this and see logs instantly, run Python with the `-u` flag (e.g., `python -u main.py ...`) or set `PYTHONUNBUFFERED=1` in your shell environment.

Retrain only the RL agent from an existing GCN checkpoint with `python main.py --train --skip-gcn`. Solve a custom board interactively with `python main.py --solve "WORD1,WORD2,...,WORD16"`.

## GCN Model Evaluation & Analysis

To analyze, compare, and debug model performance, use the following tools, reports, and logs:

* **Model Comparison CLI Action**: Compare any two GCN checkpoints or registered configurations on the validation split. Run:
  ```bash
  python main.py --compare-models [MODEL_A] [MODEL_B]
  ```
  Both inputs can be registry keys (e.g., `gcn_best`, `gcn_previous_best`, `gcn_all_time_best`, `raw_baseline`) or direct file paths (e.g., `models/gcn_best.pt`). This outputs a delta performance table to the terminal and compiles a comprehensive Markdown comparison to `visualizations/model_comparison_report.md`.

* **Model Registry (`models/model_registry.json`)**: Persistent JSON catalog recording evaluation metrics and archetype recall profiles for all GCN checkpoints and baseline configurations.

* **Training Progress Curves**: Check training history plots to diagnose overfitting/convergence rate:
  - `visualizations/gcn_learning_curves.png` (Train/val loss and validation MRR progression; logged to `visualizations/gcn_training_history.json`)
  - `visualizations/dqn_learning_curves.png` (DQN win rate, rewards, steps, and epsilon exploration; logged to `visualizations/dqn_training_history.json`)

* **Worst-Performing Puzzles Error Analysis**: After training, the validation suite identifies the 10 hardest boards (by candidate MRR) and outputs a detailed diagnostic report in `visualizations/val_puzzles/error_analysis.md`. This details words, category levels, failure archetypes, and relation archetype failure distributions to pinpoint semantic vs. orthographic GCN weakness.

* **Archetype Evaluation Script**: Evaluate GCN's auxiliary head relation classification accuracy and category Mean Reciprocal Rank (MRR) per relation archetype on the validation set:
  ```bash
  PYTHONPATH=. .venv/bin/python src/evaluate_archetypes.py
  ```

* **Validation Partition Summaries**: Validation candidates and partition search outcomes are saved in:
  - `visualizations/val_puzzles/candidates_summary.md` (Current run's validation candidates and partitions breakdown)
  - `visualizations/val_puzzles/candidates_previous_best_summary.md` (Previous best run's predictions, preserved for regression checks)

* **Validation Graphs & Plots**: Individual graph plots showing predicted link probabilities and node clusters are written to:
  - `visualizations/val_best.png` (Overall summary plot)
  - `visualizations/val_puzzles/val_puzzle_<id>.png` (Individual puzzle graphs)

## Coding Style & Naming Conventions

Use Python 3 with 4-space indentation, descriptive snake_case names for functions and variables, and PascalCase for classes such as `ConnectionsGraph` and `DQNAgent`. Keep modules focused on one responsibility and prefer explicit imports from `src.*`. Follow the existing style: type hints for public helpers, short docstrings for major pipeline functions, and concise comments only where the model or training logic is non-obvious.

## Model Development Timeline

Periodically update `model_development_timeline.md` when making significant model, feature, training, evaluation, or data pipeline changes. Add concise milestone notes for architectural changes, measurable performance improvements or regressions, feature schema/cache changes, training stability fixes, new baselines, and refreshed model artifacts. Include relevant metrics, dataset scope, command details, and affected files when they help future contributors understand why the model behavior changed.

## Commit & Pull Request Guidelines

Git history is not available in this checkout, so use clear imperative commit messages, for example `Add RL smoke test` or `Fix graph feature normalization`. Pull requests should include a short summary, the commands run, any changed model/data artifacts, and screenshots or paths for new visualizations when relevant. Link related issues when available.

## Data, Models, and Generated Artifacts

Treat `data/*.json`, `data/*.db`, and `models/*.pt` as large or reproducibility-sensitive artifacts. Do not overwrite trained checkpoints or cached data unless the change is intentional and documented in the PR. Keep generated exploratory outputs in `visualizations/` with descriptive names.
