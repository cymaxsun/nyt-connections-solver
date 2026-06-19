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

## Coding Style & Naming Conventions

Use Python 3 with 4-space indentation, descriptive snake_case names for functions and variables, and PascalCase for classes such as `ConnectionsGraph` and `DQNAgent`. Keep modules focused on one responsibility and prefer explicit imports from `src.*`. Follow the existing style: type hints for public helpers, short docstrings for major pipeline functions, and concise comments only where the model or training logic is non-obvious.

## Testing Guidelines

For code changes, run at least `python -m compileall main.py src tests` to catch syntax errors and `python -m unittest discover tests` for the existing unit tests. If the shell has no `python` command, use `.venv/bin/python -m compileall main.py src tests` and `.venv/bin/python -m unittest discover tests`. For training or inference changes, run a small smoke test such as `python main.py --train --gcn-epochs 1 --rl-episodes 5` and verify that checkpoints and visualizations are produced without exceptions. Add future tests under `tests/` using filenames like `test_dataset.py` or `test_env.py`.

## Commit & Pull Request Guidelines

Git history is not available in this checkout, so use clear imperative commit messages, for example `Add RL smoke test` or `Fix graph feature normalization`. Pull requests should include a short summary, the commands run, any changed model/data artifacts, and screenshots or paths for new visualizations when relevant. Link related issues when available.

## Data, Models, and Generated Artifacts

Treat `data/*.json`, `data/*.db`, and `models/*.pt` as large or reproducibility-sensitive artifacts. Do not overwrite trained checkpoints or cached data unless the change is intentional and documented in the PR. Keep generated exploratory outputs in `visualizations/` with descriptive names.
