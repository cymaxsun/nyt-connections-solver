import os
import shutil
import itertools
import json
import random
import torch
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from src.dataset import load_dataset, ConnectionsPuzzle
from src.features import (
    DEFAULT_NODE_FEATURE_DIM,
    EDGE_FEATURE_DIM,
    FEATURE_SCHEMA_VERSION,
    FeatureExtractor,
    EDGE_FEATURE_NAMES,
)
from src.gcn import (
    ConnectionsGCN,
    build_gcn_model,
    train_gcn_epoch,
    validate_gcn,
    build_relation_targets,
    build_group_relation_targets,
    get_hidden_features_from_state_dict,
)
from src.rl_agent import CANDIDATE_FEATURE_DIM, DQNAgent, train_rl_episodes
from src.env import ConnectionsEnv
from src.graph import ConnectionsGraph
from src.visualize import plot_connections_graph, plot_gcn_learning_curves, plot_dqn_learning_curves
from src.candidates import build_partition_candidates, partition_groups_for_actions
from src.relation_archetypes import (
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_SCHEMA_VERSION,
    RELATION_ARCHETYPES,
    NO_RELATION_IDX,
    relation_prediction_from_probabilities,
    RELATION_ARCHETYPE_TO_IDX,
    normalize_relation_archetype,
)

def set_deterministic_seed(seed: int) -> None:
    """Seed Python, NumPy, and PyTorch RNGs for repeatable training runs."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

def train_pipeline(
    data_path: str,
    gcn_epochs: int = 15,
    rl_episodes: int = 200,
    model_dir: str = "models",
    device: str = "cpu",
    batch_size: int = 16,
    gcn_patience: int = 15,
    skip_gcn: bool = False,
    update_artifacts: bool = True,
    seed: int | None = None,
    gcn_checkpoint: str = "all-time",
):
    """
    Main training pipeline.
    1. Loads dataset.
    2. Trains GCN to generate candidate subgraphs.
    3. Trains RL (DQN) agent to navigate candidates and solve puzzles.
    4. Saves models.
    """
    print("Starting Connections Solver Training Pipeline...")
    if seed is not None:
        set_deterministic_seed(seed)
        print(f"Using deterministic seed: {seed}")
    os.makedirs(model_dir, exist_ok=True)
    
    # 1. Load Data
    preprocessed_path = os.path.join(os.path.dirname(data_path), "preprocessed_graphs.pt")
    if os.path.exists(preprocessed_path):
        from src.dataset import load_preprocessed_dataset
        print(f"Loading preprocessed graphs from {preprocessed_path}...")
        train_puzzles, val_puzzles, test_puzzles = load_preprocessed_dataset(
            preprocessed_path,
            seed=seed if seed is not None else 42,
        )
        if not _preprocessed_features_are_current(train_puzzles + val_puzzles + test_puzzles):
            print(
                "Preprocessed graphs are stale; expected feature schema "
                f"{FEATURE_SCHEMA_VERSION} with {EDGE_FEATURE_DIM} edge features. "
                "Loading raw dataset so features can be rebuilt."
            )
            train_puzzles, val_puzzles, test_puzzles = load_dataset(
                data_path,
                seed=seed if seed is not None else 42,
            )
    else:
        print(f"Loading raw dataset from {data_path}...")
        train_puzzles, val_puzzles, test_puzzles = load_dataset(
            data_path,
            seed=seed if seed is not None else 42,
        )
    print(f"Loaded {len(train_puzzles)} train, {len(val_puzzles)} val, {len(test_puzzles)} test puzzles.")
    
    # Initialize feature extractor
    extractor = FeatureExtractor()
    
    # Determine in_features dynamically
    if len(train_puzzles) > 0:
        first_puzzle = train_puzzles[0]
        if isinstance(first_puzzle, dict) and "node_features" in first_puzzle:
            in_features = first_puzzle["node_features"].shape[1]
        else:
            dummy_words = ["CAT"] * 16
            dummy_graph = ConnectionsGraph(dummy_words, extractor, device=device)
            in_features = dummy_graph.node_features.shape[1]
    else:
        in_features = DEFAULT_NODE_FEATURE_DIM
        
    # 2. Train or Load GCN
    gcn = build_gcn_model(
        in_features=in_features,
        hidden_features=128,
        out_features=16,
        num_relations=EDGE_FEATURE_DIM # edge features count
    ).to(device)
    
    gcn_weights_path = os.path.join(model_dir, _gcn_checkpoint_filename())
    previous_gcn_weights_path = os.path.join(model_dir, _gcn_previous_best_checkpoint_filename())
    all_time_gcn_weights_path = os.path.join(model_dir, _gcn_all_time_best_checkpoint_filename())
    all_time_gcn_metadata_path = os.path.join(model_dir, _gcn_all_time_best_metadata_filename())
    
    if skip_gcn:
        print("\n--- Phase 1: Loading Pre-trained GCN (skipping training) ---")
        gcn_state = None
        checkpoint_label = ""

        # Try loading requested checkpoint
        if gcn_checkpoint == "all-time" and os.path.exists(all_time_gcn_weights_path):
            try:
                state = torch.load(all_time_gcn_weights_path, map_location=device)
                if _gcn_checkpoint_matches_model(state, in_features):
                    gcn_state = state
                    checkpoint_label = "all-time best GCN"
                else:
                    print("Warning: All-time best GCN checkpoint is incompatible with the current model architecture.")
            except Exception as e:
                print(f"Warning: Failed to load all-time best GCN checkpoint: {e}")

        if gcn_state is None:
            # Fall back to current best GCN checkpoint
            if os.path.exists(gcn_weights_path):
                try:
                    state = torch.load(gcn_weights_path, map_location=device)
                    if _gcn_checkpoint_matches_model(state, in_features):
                        gcn_state = state
                        checkpoint_label = "current best GCN"
                    else:
                        print("Warning: Current best GCN checkpoint is incompatible with the current model architecture.")
                except Exception as e:
                    print(f"Warning: Failed to load current best GCN checkpoint: {e}")

        if gcn_state is None:
            raise RuntimeError(
                "No compatible GCN checkpoint (all-time or current best) could be loaded. "
                "Retrain without --skip-gcn."
            )

        hidden_feats = get_hidden_features_from_state_dict(gcn_state, default=128)
        gcn = build_gcn_model(
            in_features=in_features,
            hidden_features=hidden_feats,
            out_features=16,
            num_relations=EDGE_FEATURE_DIM,
        ).to(device)
        gcn.load_state_dict(gcn_state)
        _, best_mrr = validate_gcn(gcn, val_puzzles, extractor, device, visualize=False)
        print(f"Loaded {checkpoint_label} with Validation MRR: {best_mrr:.4f}")
    else:
        print("\n--- Phase 1: Training GCN ---")
        gcn_optimizer = torch.optim.Adam(gcn.parameters(), lr=1e-3, weight_decay=1e-4)
        _preserve_existing_artifact(gcn_weights_path, previous_gcn_weights_path)
        _preserve_existing_artifact(
            os.path.join("visualizations", "val_best.png"),
            os.path.join("visualizations", "val_previous_best.png"),
        )
        all_time_best_mrr = _initialize_all_time_gcn_best(
            gcn_weights_path,
            all_time_gcn_weights_path,
            all_time_gcn_metadata_path,
            in_features,
            val_puzzles,
            extractor,
            device,
        )
        
        best_mrr = 0.0
        epochs_no_improve = 0
        gcn_history = []
        for epoch in range(1, gcn_epochs + 1):
            loss = train_gcn_epoch(gcn, train_puzzles, extractor, gcn_optimizer, device)
            val_loss, val_mrr = validate_gcn(gcn, val_puzzles, extractor, device, visualize=False)
            
            print(f"Epoch {epoch:02d}/{gcn_epochs:02d} | Train Loss: {loss:.4f} | Val Loss: {val_loss:.4f} | Val MRR: {val_mrr:.4f}")
            
            gcn_history.append({
                "epoch": epoch,
                "train_loss": float(loss),
                "val_loss": float(val_loss),
                "val_mrr": float(val_mrr)
            })
            
            # Save best GCN and store its visualization
            if val_mrr > best_mrr:
                best_mrr = val_mrr
                epochs_no_improve = 0
                _save_gcn_best_checkpoint(
                    gcn.state_dict(),
                    gcn_weights_path,
                )
                if val_mrr > all_time_best_mrr:
                    all_time_best_mrr = val_mrr
                    _save_gcn_all_time_best_checkpoint(
                        gcn.state_dict(),
                        all_time_gcn_weights_path,
                        all_time_gcn_metadata_path,
                        val_mrr,
                        epoch,
                    )
                    print(f"New all-time best GCN Validation MRR: {val_mrr:.4f}")
                    # Also save the all-time best validation graph visualization
                    all_time_best_filepath = os.path.join("visualizations", "val_all_time_best.png")
                    _, _ = validate_gcn(
                        gcn,
                        val_puzzles[:1],
                        extractor,
                        device,
                        visualize=True,
                        filepath=all_time_best_filepath,
                        visualize_idx=0
                    )
                best_filepath = os.path.join("visualizations", "val_best.png")
                _, _ = validate_gcn(
                    gcn, 
                    val_puzzles[:1],
                    extractor, 
                    device, 
                    visualize=True, 
                    filepath=best_filepath,
                    visualize_idx=0
                )
            else:
                epochs_no_improve += 1
                
            if epochs_no_improve >= gcn_patience:
                print(f"Early stopping GCN training at epoch {epoch}. No validation MRR improvement for {gcn_patience} epochs.")
                break
                
        # Save training history and plot learning curves
        history_dir = "visualizations"
        os.makedirs(history_dir, exist_ok=True)
        gcn_history_path = os.path.join(history_dir, "gcn_training_history.json")
        try:
            existing_history = []
            if os.path.exists(gcn_history_path):
                try:
                    with open(gcn_history_path, "r", encoding="utf-8") as f:
                        old_data = json.load(f)
                        if isinstance(old_data, dict) and "history" in old_data:
                            existing_history = old_data["history"]
                        elif isinstance(old_data, list):
                            existing_history = old_data
                except Exception as e:
                    print(f"Warning: Failed to load existing GCN training history: {e}. Starting fresh.")

            # Determine start epoch offset if appending
            epoch_offset = 0
            if existing_history:
                epoch_offset = max(item.get("epoch", 0) for item in existing_history if isinstance(item, dict))

            # Adjust new history epoch numbers to be sequential
            adjusted_new_history = []
            for item in gcn_history:
                adjusted_item = item.copy()
                adjusted_item["epoch"] = item["epoch"] + epoch_offset
                adjusted_new_history.append(adjusted_item)

            combined_history = existing_history + adjusted_new_history

            gcn_history_data = {
                "metadata": {
                    "edge_feature_dim": EDGE_FEATURE_DIM,
                    "node_feature_dim": in_features,
                    "edge_features": EDGE_FEATURE_NAMES,
                    "gcn_hidden_features": 128,
                    "gcn_out_features": 16,
                    "params": {
                        "gcn_epochs": gcn_epochs,
                        "gcn_lr": 1e-3,
                        "gcn_weight_decay": 1e-4,
                        "gcn_patience": gcn_patience,
                        "seed": seed,
                    }
                },
                "history": combined_history
            }
            with open(gcn_history_path, "w", encoding="utf-8") as f:
                json.dump(gcn_history_data, f, indent=2)
            plot_gcn_learning_curves(
                gcn_history_path,
                os.path.join(history_dir, "gcn_learning_curves.png"),
                history_override=adjusted_new_history,
            )
        except Exception as e:
            print(f"Warning: Failed to save or plot GCN training history: {e}")
                
        # Load GCN for RL training - default to all-time best if requested and compatible
        loaded_gcn = False
        if gcn_checkpoint == "all-time" and os.path.exists(all_time_gcn_weights_path):
            try:
                state = torch.load(all_time_gcn_weights_path, map_location=device)
                if _gcn_checkpoint_matches_model(state, in_features):
                    hidden_feats = get_hidden_features_from_state_dict(state, default=128)
                    gcn = build_gcn_model(
                        in_features=in_features,
                        hidden_features=hidden_feats,
                        out_features=16,
                        num_relations=EDGE_FEATURE_DIM,
                    ).to(device)
                    gcn.load_state_dict(state)
                    checkpoint_label = "all-time best GCN"
                    loaded_gcn = True
                else:
                    print("Warning: All-time best GCN checkpoint is incompatible. Falling back to current best.")
            except Exception as e:
                print(f"Warning: Failed to load all-time best GCN checkpoint: {e}")

        if not loaded_gcn:
            state = torch.load(gcn_weights_path, map_location=device)
            hidden_feats = get_hidden_features_from_state_dict(state, default=128)
            gcn = build_gcn_model(
                in_features=in_features,
                hidden_features=hidden_feats,
                out_features=16,
                num_relations=EDGE_FEATURE_DIM,
            ).to(device)
            gcn.load_state_dict(state)
            checkpoint_label = "current best GCN"

        print(f"GCN training complete. Loaded {checkpoint_label} for RL training.")

    if update_artifacts:
        print("\n--- Phase 1b: Updating Validation Artifacts ---")
        update_validation_artifacts(
            gcn,
            val_puzzles,
            extractor,
            device,
            checkpoint_label=os.path.join(model_dir, _gcn_checkpoint_filename()),
        )
    else:
        print("\n--- Phase 1b: Skipping Validation Artifacts ---")
    
    if rl_episodes <= 0:
        print("\n--- Phase 2: Skipping RL DQN Agent Training ---")
        return best_mrr

    # 3. Train RL DQN Agent
    print("\n--- Phase 2: Training RL DQN Agent ---")
    # State space dimension = 16 (mask) + 1 (mistakes normalized) + 16 (history) = 33
    # Candidate feature dimension includes GCN group features plus partition context.
    agent = DQNAgent(
        state_dim=33,
        candidate_dim=CANDIDATE_FEATURE_DIM,
        lr=5e-4,
        gamma=0.9,
        epsilon_start=1.0,
        epsilon_end=0.05,
        epsilon_decay=0.998,
        device=device
    )
    
    # Train DQN agent
    # We log success statistics periodically
    eval_freq = max(5, rl_episodes // 10)
    dqn_history = []
    for i in range(0, rl_episodes, eval_freq):
        chunk_episodes = min(eval_freq, rl_episodes - i)
        stats = train_rl_episodes(agent, gcn, train_puzzles, extractor, chunk_episodes, batch_size=batch_size)
        
        # Calculate recent metrics
        win_rate = np.mean([s["won"] for s in stats])
        avg_reward = np.mean([s["reward"] for s in stats])
        avg_steps = np.mean([s["steps"] for s in stats])
        
        print(f"RL Episode {i + chunk_episodes:04d}/{rl_episodes:04d} | Win Rate: {win_rate:.2%} | Avg Reward: {avg_reward:.2f} | Avg Steps: {avg_steps:.1f} | Epsilon: {agent.epsilon:.3f}")
        
        dqn_history.append({
            "episode": i + chunk_episodes,
            "win_rate": float(win_rate),
            "avg_reward": float(avg_reward),
            "avg_steps": float(avg_steps),
            "epsilon": float(agent.epsilon)
        })
        
    # Save training history and plot learning curves
    history_dir = "visualizations"
    os.makedirs(history_dir, exist_ok=True)
    dqn_history_path = os.path.join(history_dir, "dqn_training_history.json")
    try:
        dqn_history_data = {
            "metadata": {
                "rl_state_dim": 33,
                "rl_candidate_dim": CANDIDATE_FEATURE_DIM,
                "params": {
                    "rl_episodes": rl_episodes,
                    "rl_lr": 5e-4,
                    "rl_gamma": 0.9,
                    "rl_epsilon_start": 1.0,
                    "rl_epsilon_end": 0.05,
                    "rl_epsilon_decay": 0.998,
                    "batch_size": batch_size,
                    "seed": seed,
                }
            },
            "history": dqn_history
        }
        with open(dqn_history_path, "w", encoding="utf-8") as f:
            json.dump(dqn_history_data, f, indent=2)
        plot_dqn_learning_curves(dqn_history_path, os.path.join(history_dir, "dqn_learning_curves.png"))
    except Exception as e:
        print(f"Warning: Failed to save or plot DQN training history: {e}")

    # Save DQN weights
    torch.save(agent.q_net.state_dict(), os.path.join(model_dir, "dqn_q_net.pt"))
    print("DQN Agent training complete. Saved models.")
    
    # 4. Final Evaluation
    print("\n--- Phase 3: Evaluating System on Test Set ---")
    evaluate_system(gcn, agent, test_puzzles, extractor, device)

def evaluate_system(gcn: ConnectionsGCN, agent: DQNAgent, test_puzzles: List[ConnectionsPuzzle], extractor: FeatureExtractor, device: str) -> float:
    gcn.eval()
    agent.q_net.eval()
    agent.epsilon = 0.0 # pure greedy evaluation
    
    successes = 0
    total_reward = 0.0
    steps_list = []
    
    for puzzle in test_puzzles:
        with torch.no_grad():
            if isinstance(puzzle, dict):
                graph = ConnectionsGraph(
                    puzzle["words"], 
                    device=device, 
                    node_features=puzzle["node_features"], 
                    edge_features=puzzle["edge_features"]
                )
            else:
                graph = ConnectionsGraph(puzzle.words, extractor, device=device)
            
            # Clone edge features for episode-local mutations
            graph.edge_features = graph.edge_features.clone()
                
        env = ConnectionsEnv(puzzle)
        obs, info = env.reset()
        done = False
        steps = 0
        
        while not done:
            # Re-run GCN on the (potentially updated) graph each step
            with torch.no_grad():
                node_embeddings, edge_probs, _, group_relation_logits = gcn(
                    graph.node_features,
                    graph.get_multi_relational_adjacency(),
                    graph.edge_features,
                    return_group_logits=True,
                )
                candidates = graph.filter_candidates(
                    gcn.get_candidate_subgraphs(edge_probs, group_relation_logits)
                )
                action_candidates = agent.get_partition_action_candidates(
                    candidates, obs, graph.rejected_groups
                )
            
            cand_list, cand_feats = agent.get_candidate_features(action_candidates, node_embeddings, obs)
            action_idx = agent.select_action(obs, cand_list, cand_feats)
            action_indices = cand_list[action_idx]
            
            obs, reward, done, _, info = env.step(action_indices)
            total_reward += reward
            steps += 1
            
            # Update graph edges based on feedback
            feedback = info.get("feedback", "")
            graph.update_edges_from_feedback(action_indices, feedback)
            
        if info.get("win", False):
            successes += 1
        steps_list.append(steps)
        
    test_win_rate = successes / len(test_puzzles)
    print(f"Test Set Evaluation | Total Puzzles: {len(test_puzzles)}")
    print(f"Win Rate: {test_win_rate:.2%}")
    print(f"Average Reward: {total_reward / len(test_puzzles):.2f}")
    print(f"Average Submissions: {np.mean(steps_list):.1f}")
    return test_win_rate

def _evaluate_gcn_model_stats(
    model: ConnectionsGCN,
    val_puzzles: list,
    extractor: FeatureExtractor,
    device: str,
    top_k: int = 5,
    visualize_prefix: Optional[str] = None,
    output_dir: Optional[str] = None,
    collect_puzzle_details: bool = False,
) -> Tuple[Dict[str, Any], List[str], List[Dict[str, Any]]]:
    model.eval()
    top_group_limit = top_k * 4
    aggregate_stats = _new_validation_summary_stats(top_group_limit)
    puzzle_lines = []
    puzzle_mrrs = []

    with torch.no_grad():
        for idx, puzzle in enumerate(val_puzzles):
            words = _puzzle_value(puzzle, "words")
            word_to_cat = _puzzle_value(puzzle, "word_to_cat")
            categories = _puzzle_value(puzzle, "categories")
            puzzle_id = _puzzle_value(puzzle, "id")

            if isinstance(puzzle, dict):
                graph = ConnectionsGraph(
                    words,
                    device=device,
                    node_features=puzzle["node_features"],
                    edge_features=puzzle["edge_features"],
                )
            else:
                graph = ConnectionsGraph(words, extractor, device=device)

            node_embeddings, edge_probs, relation_logits, group_relation_logits = model(
                graph.node_features,
                graph.get_multi_relational_adjacency(),
                graph.edge_features,
                return_group_logits=True,
            )
            candidates = model.get_candidate_subgraphs(edge_probs, group_relation_logits)
            active_mask = np.ones(16, dtype=np.float32)
            partitions = build_partition_candidates(candidates, active_mask, top_n=200)
            action_candidates = partition_groups_for_actions(partitions, candidates, active_mask)
            true_groups = _true_groups_for_words(words, word_to_cat)
            
            _update_validation_summary_stats(
                aggregate_stats,
                words,
                word_to_cat,
                true_groups,
                partitions[:top_k],
                action_candidates[:top_group_limit],
                model,
                device,
                edge_probs,
                relation_logits,
                group_relation_logits,
            )
            
            # Calculate puzzle MRR
            puzzle_mrr_sum = 0.0
            c_tensor, scores_tensor = model.get_candidate_scores_tensor(edge_probs, group_relation_logits)
            for cat_idx, true_group in true_groups.items():
                indices = list(true_group)
                tc = torch.tensor(sorted(indices), dtype=torch.long, device=device)
                match_mask = (c_tensor == tc).all(dim=1)
                if match_mask.any():
                    true_score = scores_tensor[match_mask][0]
                    rank = int(torch.sum(scores_tensor >= true_score).item())
                    puzzle_mrr_sum += 1.0 / rank
            puzzle_mrr = puzzle_mrr_sum / 4.0
            puzzle_mrrs.append({
                "id": puzzle_id,
                "words": words,
                "categories": categories,
                "mrr": puzzle_mrr
            })
            
            true_cats = [word_to_cat[w]["cat_idx"] for w in words]
            edge_probs_np = edge_probs.cpu().numpy()

            if idx < 5 and visualize_prefix is not None and output_dir is not None:
                visualization_path = os.path.join(output_dir, f"{visualize_prefix}_puzzle_{puzzle_id}.png")
                plot_connections_graph(
                    words,
                    edge_probs_np,
                    true_categories=true_cats,
                    threshold=0.45,
                    filepath=visualization_path,
                    title=f"GCN Edge Predictions - Puzzle {puzzle_id}",
                    relation_logits=relation_logits.cpu().numpy()
                )

            if collect_puzzle_details:
                puzzle_lines.extend([
                    f"## Puzzle {idx} (ID: {puzzle_id})",
                    f"**Words on Board:** {', '.join(words)}",
                    "",
                    "### Ground Truth Categories:",
                ])
                for cat in sorted(categories, key=lambda item: item["level"]):
                    members = ", ".join(member.strip().upper() for member in cat["members"])
                    rtype_str = f" [Type: {cat.get('relation_type', 'SYNONYM_OR_NEAR')}]"
                    puzzle_lines.append(f"* **Level {cat['level']} ({cat['group']}){rtype_str}:** {members}")

                puzzle_lines.extend(["", "### Top Candidate Partitions:"])
                if partitions:
                    for rank, partition in enumerate(partitions[:top_k], start=1):
                        puzzle_lines.append(f"{rank}. **Partition Score: {partition.score:.4f}**")
                        for group_idx, candidate in enumerate(partition.groups, start=1):
                            puzzle_lines.append(
                                _candidate_summary_line(
                                    group_idx,
                                    candidate,
                                    words,
                                    word_to_cat,
                                    relation_logits,
                                    group_relation_logits,
                                )
                            )
                else:
                    puzzle_lines.append(
                        "_No complete four-group partitions were found from the bounded search; "
                        "showing top individual candidate groups instead._"
                    )

                puzzle_lines.extend(["", "### Top Candidate Groups:"])
                if action_candidates:
                    for group_idx, candidate in enumerate(action_candidates[:top_group_limit], start=1):
                        puzzle_lines.append(
                            _candidate_summary_line(
                                group_idx,
                                candidate,
                                words,
                                word_to_cat,
                                relation_logits,
                                group_relation_logits,
                            )
                        )
                else:
                    puzzle_lines.append("_No candidate groups were available._")
                puzzle_lines.extend(["", "---", ""])

            if (idx + 1) % 20 == 0 or (idx + 1) == len(val_puzzles):
                print(f"Evaluated {idx + 1}/{len(val_puzzles)} validation puzzles for {visualize_prefix or 'metrics'}")

    return aggregate_stats, puzzle_lines, puzzle_mrrs


def _stats_to_metric_dict(stats: Dict[str, Any]) -> Dict[str, str]:
    puzzles = max(1, stats["puzzles"])
    total_true_groups = stats["puzzles"] * 4
    top_group_limit = stats["top_group_limit"]
    top_k = top_group_limit // 4
    ranks = stats["true_group_ranks"]
    mean_rank = float(np.mean(ranks)) if ranks else 0.0
    median_rank = float(np.median(ranks)) if ranks else 0.0
    
    return {
        "Validation puzzles": f"{stats['puzzles']}",
        "Overall GCN Candidate MRR": f"{stats['exact_mrr_sum'] / max(1, stats['exact_mrr_count']):.4f}",
        "Overall Pairwise Relation Accuracy": f"{_pct(stats['pairwise_correct'], stats['pairwise_total'])}",
        "Overall Group Relation Accuracy": f"{_pct(stats['group_correct'], stats['group_total'])}",
        "Puzzles with complete partition candidates": f"{stats['with_partitions']} / {stats['puzzles']} ({_pct(stats['with_partitions'], stats['puzzles'])})",
        "Top partition solves all 4 groups": f"{stats['top_partition_solved']} / {stats['puzzles']} ({_pct(stats['top_partition_solved'], stats['puzzles'])})",
        f"Any top-{top_k} partition solves all 4 groups": f"{stats['best_top_k_partition_solved']} / {stats['puzzles']} ({_pct(stats['best_top_k_partition_solved'], stats['puzzles'])})",
        "Avg correct groups in top partition": f"{stats['top_partition_correct_groups'] / puzzles:.2f} / 4",
        "Avg best correct groups across top partitions": f"{stats['best_top_k_partition_correct_groups'] / puzzles:.2f} / 4",
        f"True groups in top-{top_group_limit} candidates": f"{stats['true_groups_in_top_candidates']} / {total_true_groups} ({_pct(stats['true_groups_in_top_candidates'], total_true_groups)})",
        f"Puzzles with any true group in top-{top_group_limit}": f"{stats['puzzles_with_any_true_group']} / {stats['puzzles']} ({_pct(stats['puzzles_with_any_true_group'], stats['puzzles'])})",
        f"Puzzles with all true groups in top-{top_group_limit}": f"{stats['puzzles_with_all_true_groups']} / {stats['puzzles']} ({_pct(stats['puzzles_with_all_true_groups'], stats['puzzles'])})",
        f"Mean rank of true groups found in top-{top_group_limit}": f"{mean_rank:.2f}",
        f"Median rank of true groups found in top-{top_group_limit}": f"{median_rank:.1f}",
        f"3-of-4 near-miss candidates in top-{top_group_limit}": f"{stats['near_miss_3_of_4_candidates']}",
    }


def update_validation_artifacts(
    gcn: ConnectionsGCN,
    val_puzzles: list,
    extractor: FeatureExtractor,
    device: str,
    output_dir: str = "visualizations/val_puzzles",
    best_filepath: str = "visualizations/val_best.png",
    top_k: int = 5,
    checkpoint_label: str = "current GCN checkpoint",
):
    """Refresh validation graph PNGs and candidate summary for the loaded GCN."""
    os.makedirs(output_dir, exist_ok=True)
    summary_path = os.path.join(output_dir, "candidates_summary")
    # append .md if not present
    if not summary_path.endswith(".md"):
        summary_path += ".md"

    # 1. Parse previous stats from existing summary file (if any) before writing over it
    previous_stats_parsed = _parse_previous_summary(summary_path)

    # 2. Evaluate current GCN model
    print("Evaluating current model...")
    aggregate_stats, puzzle_lines, puzzle_mrrs = _evaluate_gcn_model_stats(
        gcn,
        val_puzzles,
        extractor,
        device,
        top_k=top_k,
        visualize_prefix="val",
        output_dir=output_dir,
        collect_puzzle_details=True,
    )

    # 3. Generate overall validation best visualization
    validate_gcn(
        gcn,
        val_puzzles[:1],
        extractor,
        device,
        visualize=True,
        filepath=best_filepath,
        visualize_idx=0,
    )

    # 4. Try loading and evaluating previous best model from checkpoint
    previous_best_path = "models/gcn_previous_best.pt"
    previous_metrics = previous_stats_parsed
    prev_stats = None
    if os.path.exists(previous_best_path):
        try:
            print("Evaluating previous best GCN from checkpoint...")
            state = torch.load(previous_best_path, map_location=device)
            hidden_feats = get_hidden_features_from_state_dict(state, default=32)
            prev_gcn = ConnectionsGCN(
                in_features=gcn.input_proj.in_features,
                hidden_features=hidden_feats,
                out_features=16,
                num_relations=EDGE_FEATURE_DIM,
            ).to(device)
            prev_gcn.load_state_dict(state)
            
            prev_stats, _, _ = _evaluate_gcn_model_stats(
                prev_gcn,
                val_puzzles,
                extractor,
                device,
                top_k=top_k,
                visualize_prefix="val_previous_best",
                output_dir=output_dir,
                collect_puzzle_details=False,
            )
            previous_metrics = _stats_to_metric_dict(prev_stats)
            
            # Save previous best overall visualization
            validate_gcn(
                prev_gcn,
                val_puzzles[:1],
                extractor,
                device,
                visualize=True,
                filepath="visualizations/val_previous_best.png",
                visualize_idx=0,
            )
        except Exception as e:
            print(f"Warning: Failed to evaluate previous best GCN checkpoint: {e}")

    # 5. Try loading and evaluating all-time best model from checkpoint
    all_time_best_path = os.path.join(model_dir, _gcn_all_time_best_checkpoint_filename())
    all_time_metrics = None
    all_time_stats = None
    if os.path.exists(all_time_best_path):
        try:
            print("Evaluating all-time best GCN from checkpoint...")
            state = torch.load(all_time_best_path, map_location=device)
            hidden_feats = get_hidden_features_from_state_dict(state, default=32)
            all_time_gcn = ConnectionsGCN(
                in_features=gcn.input_proj.in_features,
                hidden_features=hidden_feats,
                out_features=16,
                num_relations=EDGE_FEATURE_DIM,
            ).to(device)
            all_time_gcn.load_state_dict(state)
            
            all_time_stats, _, _ = _evaluate_gcn_model_stats(
                all_time_gcn,
                val_puzzles,
                extractor,
                device,
                top_k=top_k,
                visualize_prefix="val_all_time_best",
                output_dir=output_dir,
                collect_puzzle_details=False,
            )
            all_time_metrics = _stats_to_metric_dict(all_time_stats)
            
            # Save all-time best overall visualization
            validate_gcn(
                all_time_gcn,
                val_puzzles[:1],
                extractor,
                device,
                visualize=True,
                filepath="visualizations/val_all_time_best.png",
                visualize_idx=0,
            )
        except Exception as e:
            print(f"Warning: Failed to evaluate all-time best GCN checkpoint: {e}")

    # Register checkpoints in model registry
    curr_metrics = _stats_to_metric_dict(aggregate_stats)
    _update_model_registry("gcn_best", curr_metrics, aggregate_stats)
    if prev_stats is not None:
        _update_model_registry("gcn_previous_best", previous_metrics, prev_stats)
    if all_time_stats is not None:
        _update_model_registry(f"gcn_all_time_best_v{FEATURE_SCHEMA_VERSION}", all_time_metrics, all_time_stats)

    # Write error analysis report
    _write_error_analysis_report(puzzle_mrrs, os.path.join(output_dir, "error_analysis.md"))

    # Format output file content
    lines = [
        "# GCN Subgraph Predictions - All Validation Puzzles",
        "",
        f"Generated from the current `{checkpoint_label}` checkpoint loaded by the training pipeline.",
        "",
        (
            f"This document summarizes the top {top_k} candidate partitions "
            f"built from GCN predictions for all {len(val_puzzles)} validation puzzles. "
            "Each group is labeled with exact correctness or maximum overlap with "
            "a ground truth category."
        ),
        "",
    ]
    lines.extend(_format_validation_summary_stats(aggregate_stats, previous_metrics, all_time_metrics))
    lines.extend(puzzle_lines)

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Updated validation candidate summary: {summary_path}")

def _puzzle_value(puzzle: Any, field: str):
    return puzzle[field] if isinstance(puzzle, dict) else getattr(puzzle, field)


def _new_validation_summary_stats(top_group_limit: int) -> Dict[str, Any]:
    return {
        "puzzles": 0,
        "top_group_limit": top_group_limit,
        "with_partitions": 0,
        "top_partition_solved": 0,
        "best_top_k_partition_solved": 0,
        "top_partition_correct_groups": 0,
        "best_top_k_partition_correct_groups": 0,
        "true_groups_in_top_candidates": 0,
        "puzzles_with_any_true_group": 0,
        "puzzles_with_all_true_groups": 0,
        "true_group_ranks": [],
        "near_miss_3_of_4_candidates": 0,
        "archetypes": {},
        "exact_mrr_sum": 0.0,
        "exact_mrr_count": 0,
        "pairwise_correct": 0,
        "pairwise_total": 0,
        "group_correct": 0,
        "group_total": 0,
    }


def _update_validation_summary_stats(
    stats: Dict[str, Any],
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
    true_groups: Dict[int, Tuple[int, ...]],
    partitions: List[Any],
    action_candidates: List[Any],
    gcn: ConnectionsGCN,
    device: str,
    edge_probs: torch.Tensor,
    relation_logits: torch.Tensor,
    group_relation_logits: torch.Tensor,
) -> None:
    stats["puzzles"] += 1
    stats["with_partitions"] += 1 if partitions else 0

    partition_correct_counts = [
        _exact_groups_in_candidate_partition(partition, true_groups)
        for partition in partitions
    ]
    top_partition_correct = partition_correct_counts[0] if partition_correct_counts else 0
    best_partition_correct = max(partition_correct_counts) if partition_correct_counts else 0
    stats["top_partition_correct_groups"] += top_partition_correct
    stats["best_top_k_partition_correct_groups"] += best_partition_correct
    stats["top_partition_solved"] += 1 if top_partition_correct == 4 else 0
    stats["best_top_k_partition_solved"] += 1 if best_partition_correct == 4 else 0

    best_rank_by_cat: Dict[int, int] = {}
    for rank, candidate in enumerate(action_candidates, start=1):
        exact_cat_idx = _exact_candidate_cat_idx(candidate, true_groups)
        if exact_cat_idx is not None and exact_cat_idx not in best_rank_by_cat:
            best_rank_by_cat[exact_cat_idx] = rank
            stats["true_group_ranks"].append(rank)
        elif exact_cat_idx is None and _candidate_max_overlap(candidate, true_groups) == 3:
            stats["near_miss_3_of_4_candidates"] += 1

    stats["true_groups_in_top_candidates"] += len(best_rank_by_cat)
    stats["puzzles_with_any_true_group"] += 1 if best_rank_by_cat else 0
    stats["puzzles_with_all_true_groups"] += 1 if len(best_rank_by_cat) == len(true_groups) else 0

    # Pairwise Relation Accuracy
    relation_true = build_relation_targets(words, word_to_cat, device)
    for i in range(16):
        for j in range(16):
            true_idx = int(relation_true[i, j].item())
            if true_idx == -100:
                continue
            pred_idx = torch.argmax(relation_logits[i, j]).item()
            is_correct = (pred_idx == true_idx)
            stats["pairwise_total"] += 1
            if is_correct:
                stats["pairwise_correct"] += 1

            arch_name = RELATION_ARCHETYPES[true_idx]
            arch_stats = stats["archetypes"].setdefault(
                arch_name,
                {
                    "total": 0,
                    "hit_top_candidates": 0,
                    "hit_top_5": 0,
                    "rank_sum": 0,
                    "rank_count": 0,
                    "exact_mrr_sum": 0.0,
                    "pairwise_correct": 0,
                    "pairwise_total": 0,
                    "group_correct": 0,
                    "group_total": 0,
                },
            )
            arch_stats["pairwise_total"] += 1
            if is_correct:
                arch_stats["pairwise_correct"] += 1

    # Group Relation Accuracy
    group_relation_true = build_group_relation_targets(
        gcn,
        torch.logit(edge_probs.clamp(1e-6, 1 - 1e-6)),
        words,
        word_to_cat,
        device,
    )
    group_pred = torch.argmax(group_relation_logits, dim=-1)
    for group_idx in range(group_relation_true.shape[0]):
        true_idx = int(group_relation_true[group_idx].item())
        if true_idx == -100:
            continue
        pred_idx = int(group_pred[group_idx].item())
        stats["group_total"] += 1
        is_correct = (pred_idx == true_idx)
        if is_correct:
            stats["group_correct"] += 1

        arch_name = RELATION_ARCHETYPES[true_idx]
        arch_stats = stats["archetypes"].setdefault(
            arch_name,
            {
                "total": 0,
                "hit_top_candidates": 0,
                "hit_top_5": 0,
                "rank_sum": 0,
                "rank_count": 0,
                "exact_mrr_sum": 0.0,
                "pairwise_correct": 0,
                "pairwise_total": 0,
                "group_correct": 0,
                "group_total": 0,
                },
            )
        arch_stats["group_total"] += 1
        if is_correct:
            arch_stats["group_correct"] += 1

    # Exact MRR and category level metrics
    c, scores = gcn.get_candidate_scores_tensor(edge_probs, group_relation_logits)
    for cat_idx, true_group in true_groups.items():
        relation_type = _relation_type_for_cat(words, word_to_cat, cat_idx)
        archetype_stats = stats["archetypes"].setdefault(
            relation_type,
            {
                "total": 0,
                "hit_top_candidates": 0,
                "hit_top_5": 0,
                "rank_sum": 0,
                "rank_count": 0,
                "exact_mrr_sum": 0.0,
                "pairwise_correct": 0,
                "pairwise_total": 0,
                "group_correct": 0,
                "group_total": 0,
            },
        )
        archetype_stats["total"] += 1

        # Exact MRR for this group
        indices = list(true_group)
        tc = torch.tensor(sorted(indices), dtype=torch.long, device=device)
        match_mask = (c == tc).all(dim=1)
        if match_mask.any():
            true_score = scores[match_mask][0]
            rank = int(torch.sum(scores >= true_score).item())
            exact_mrr = 1.0 / rank
            stats["exact_mrr_sum"] += exact_mrr
            stats["exact_mrr_count"] += 1
            archetype_stats["exact_mrr_sum"] += exact_mrr

        # Top candidate rank updates
        best_rank = best_rank_by_cat.get(cat_idx)
        if best_rank is not None:
            archetype_stats["hit_top_candidates"] += 1
            archetype_stats["rank_sum"] += best_rank
            archetype_stats["rank_count"] += 1
            if best_rank <= 5:
                archetype_stats["hit_top_5"] += 1


def _parse_numeric_value(val_str: str) -> float | None:
    import re
    val_str = val_str.strip()
    # 1. Look for percentage first, e.g., "78.0%"
    pct_match = re.search(r"([\d\.]+)\s*%", val_str)
    if pct_match:
        return float(pct_match.group(1))
    # 2. Look for fractions, e.g., "85 / 109" or "0.72 / 4"
    frac_match = re.search(r"([\d\.]+)\s*/", val_str)
    if frac_match:
        return float(frac_match.group(1))
    # 3. Look for plain numbers, e.g., "109" or "4.73" or "3.0"
    num_match = re.match(r"^([\d\.\-]+)$", val_str)
    if num_match:
        return float(num_match.group(1))
    # Fallback: extract the first float-like sequence
    fallback_match = re.search(r"(-?[\d\.]+)", val_str)
    if fallback_match:
        return float(fallback_match.group(1))
    return None


def _format_comparison(metric_name: str, curr_str: str, prev_str: str | None) -> Tuple[str, str]:
    if not prev_str:
        return "-", "-"
    
    curr_val = _parse_numeric_value(curr_str)
    prev_val = _parse_numeric_value(prev_str)
    
    if curr_val is None or prev_val is None:
        return prev_str, "-"
        
    diff = curr_val - prev_val
    lower_is_better = "rank" in metric_name.lower()
    is_pct = "%" in curr_str and "%" in prev_str
    
    if abs(diff) < 1e-5:
        change_str = "0" if not is_pct else "0.0%"
        return prev_str, change_str
        
    sign = "+" if diff > 0 else ""
    if is_pct:
        change_val_str = f"{sign}{diff:.1f}%"
    else:
        if "." in curr_str or "." in prev_str:
            change_val_str = f"{sign}{diff:.2f}"
        else:
            change_val_str = f"{sign}{int(diff)}"
            
    if lower_is_better:
        if diff < 0:
            change_display = f"🟢 {change_val_str} (improved)"
        else:
            change_display = f"🔴 {change_val_str} (regressed)"
    else:
        if diff > 0:
            change_display = f"🟢 {change_val_str} (improved)"
        else:
            change_display = f"🔴 {change_val_str} (regressed)"
            
    return prev_str, change_display


def _parse_previous_summary(path: str) -> Dict[str, str]:
    if not os.path.exists(path):
        return {}
    results = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            in_summary = False
            for line in f:
                line = line.strip()
                if line.startswith("## Aggregate Summary"):
                    in_summary = True
                    continue
                if in_summary:
                    if line.startswith("###") or line.startswith("---"):
                        break
                    if line.startswith("|") and not line.startswith("|---"):
                        parts = [p.strip() for p in line.split("|")]
                        if len(parts) >= 4:
                            metric = parts[1]
                            value = parts[2]
                            if metric and metric != "Metric":
                                results[metric] = value
    except Exception as e:
        print(f"Warning: Failed to parse previous summary: {e}")
    return results


def _format_validation_summary_stats(
    stats: Dict[str, Any],
    previous_stats: Dict[str, str] | None = None,
    all_time_stats: Dict[str, str] | None = None,
) -> List[str]:
    puzzles = max(1, stats["puzzles"])
    total_true_groups = stats["puzzles"] * 4
    top_group_limit = stats["top_group_limit"]
    top_k = top_group_limit // 4
    ranks = stats["true_group_ranks"]
    mean_rank = float(np.mean(ranks)) if ranks else 0.0
    median_rank = float(np.median(ranks)) if ranks else 0.0

    if previous_stats is None:
        previous_stats = {}
    if all_time_stats is None:
        all_time_stats = {}

    metric_items = [
        ("Validation puzzles", f"{stats['puzzles']}"),
        ("Overall GCN Candidate MRR", f"{stats['exact_mrr_sum'] / max(1, stats['exact_mrr_count']):.4f}"),
        ("Overall Pairwise Relation Accuracy", f"{_pct(stats['pairwise_correct'], stats['pairwise_total'])}"),
        ("Overall Group Relation Accuracy", f"{_pct(stats['group_correct'], stats['group_total'])}"),
        ("Puzzles with complete partition candidates", f"{stats['with_partitions']} / {stats['puzzles']} ({_pct(stats['with_partitions'], stats['puzzles'])})"),
        ("Top partition solves all 4 groups", f"{stats['top_partition_solved']} / {stats['puzzles']} ({_pct(stats['top_partition_solved'], stats['puzzles'])})"),
        (f"Any top-{top_k} partition solves all 4 groups", f"{stats['best_top_k_partition_solved']} / {stats['puzzles']} ({_pct(stats['best_top_k_partition_solved'], stats['puzzles'])})"),
        ("Avg correct groups in top partition", f"{stats['top_partition_correct_groups'] / puzzles:.2f} / 4"),
        ("Avg best correct groups across top partitions", f"{stats['best_top_k_partition_correct_groups'] / puzzles:.2f} / 4"),
        (f"True groups in top-{top_group_limit} candidates", f"{stats['true_groups_in_top_candidates']} / {total_true_groups} ({_pct(stats['true_groups_in_top_candidates'], total_true_groups)})"),
        (f"Puzzles with any true group in top-{top_group_limit}", f"{stats['puzzles_with_any_true_group']} / {stats['puzzles']} ({_pct(stats['puzzles_with_any_true_group'], stats['puzzles'])})"),
        (f"Puzzles with all true groups in top-{top_group_limit}", f"{stats['puzzles_with_all_true_groups']} / {stats['puzzles']} ({_pct(stats['puzzles_with_all_true_groups'], stats['puzzles'])})"),
        (f"Mean rank of true groups found in top-{top_group_limit}", f"{mean_rank:.2f}"),
        (f"Median rank of true groups found in top-{top_group_limit}", f"{median_rank:.1f}"),
        (f"3-of-4 near-miss candidates in top-{top_group_limit}", f"{stats['near_miss_3_of_4_candidates']}"),
    ]

    def _make_row(metric: str, curr_str: str) -> str:
        def _find_val(d: Dict[str, str], key: str) -> str | None:
            if key in d:
                return d[key]
            import re
            norm_key = re.sub(r'\d+', '', key).replace(" ", "").replace("-", "").lower()
            for k, v in d.items():
                norm_k = re.sub(r'\d+', '', k).replace(" ", "").replace("-", "").lower()
                if norm_key == norm_k:
                    return v
            return None

        prev_str = _find_val(previous_stats, metric)
        all_time_str = _find_val(all_time_stats, metric)
        
        prev_display, change_prev = _format_comparison(metric, curr_str, prev_str)
        all_time_display, change_all_time = _format_comparison(metric, curr_str, all_time_str)
        
        return f"| {metric} | {curr_str} | {prev_display} | {change_prev} | {all_time_display} | {change_all_time} |"

    lines = [
        "## Aggregate Summary",
        "",
        "| Metric | Current | Previous | Change vs Prev | All-Time Best | Change vs All-Time |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for metric_name, curr_str in metric_items:
        lines.append(_make_row(metric_name, curr_str))

    lines.extend([
        "",
        "### Recall By Relation Archetype",
        "",
        f"| Archetype | True Groups | Hit Top {top_group_limit} | Recall | Hit Top 5 | Avg Best Rank | Exact MRR | Pairwise Acc | Group Acc |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])

    for archetype, archetype_stats in sorted(stats["archetypes"].items()):
        rank_count = archetype_stats["rank_count"]
        avg_rank = (
            archetype_stats["rank_sum"] / rank_count
            if rank_count
            else 0.0
        )
        exact_mrr = (
            archetype_stats.get("exact_mrr_sum", 0.0) / archetype_stats["total"]
            if archetype_stats["total"] > 0
            else 0.0
        )
        p_correct = archetype_stats.get("pairwise_correct", 0)
        p_total = archetype_stats.get("pairwise_total", 0)
        pairwise_acc = _pct(p_correct, p_total) if p_total > 0 else "-"
        
        g_correct = archetype_stats.get("group_correct", 0)
        g_total = archetype_stats.get("group_total", 0)
        group_acc = _pct(g_correct, g_total) if g_total > 0 else "-"

        lines.append(
            f"| {archetype} | {archetype_stats['total']} | "
            f"{archetype_stats['hit_top_candidates']} | "
            f"{_pct(archetype_stats['hit_top_candidates'], archetype_stats['total'])} | "
            f"{archetype_stats['hit_top_5']} | "
            f"{avg_rank:.2f} | "
            f"{exact_mrr:.4f} | "
            f"{pairwise_acc} | "
            f"{group_acc} |"
        )

    lines.extend(["", "---", ""])
    return lines


def _pct(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return "0.0%"
    return f"{numerator / denominator:.1%}"


def _true_groups_for_words(
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
) -> Dict[int, Tuple[int, ...]]:
    groups: Dict[int, List[int]] = {}
    for idx, word in enumerate(words):
        cat_idx = word_to_cat[word]["cat_idx"]
        groups.setdefault(cat_idx, []).append(idx)
    return {cat_idx: tuple(sorted(indices)) for cat_idx, indices in groups.items()}


def _exact_groups_in_candidate_partition(
    partition: Any,
    true_groups: Dict[int, Tuple[int, ...]],
) -> int:
    true_group_set = set(true_groups.values())
    return sum(
        1 for candidate in partition.groups
        if tuple(sorted(candidate.group)) in true_group_set
    )


def _exact_candidate_cat_idx(
    candidate: Any,
    true_groups: Dict[int, Tuple[int, ...]],
) -> int | None:
    group = tuple(sorted(candidate.group))
    for cat_idx, true_group in true_groups.items():
        if group == true_group:
            return cat_idx
    return None


def _candidate_max_overlap(
    candidate: Any,
    true_groups: Dict[int, Tuple[int, ...]],
) -> int:
    group = set(candidate.group)
    return max(
        (len(group.intersection(true_group)) for true_group in true_groups.values()),
        default=0,
    )


def _relation_type_for_cat(
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
    cat_idx: int,
) -> str:
    for word in words:
        cat_info = word_to_cat[word]
        if cat_info["cat_idx"] == cat_idx:
            return cat_info.get("relation_type", "SYNONYM_OR_NEAR")
    return "SYNONYM_OR_NEAR"


def _candidate_summary_line(
    group_idx: int,
    candidate: Any,
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
    relation_logits = None,
    group_relation_logits = None,
) -> str:
    candidate_words = [words[i] for i in candidate.group]
    status = _candidate_status(candidate_words, word_to_cat)
    
    relation_str = ""
    if group_relation_logits is not None:
        combination_idx = _candidate_combination_index(candidate.group)
        if combination_idx is not None:
            group_probs = torch.softmax(group_relation_logits[combination_idx], dim=-1)
            pred_idx = relation_prediction_from_probabilities(group_probs.cpu().tolist())
            if pred_idx is not None:
                confidence = group_probs[pred_idx].item()
                no_relation_confidence = group_probs[NO_RELATION_IDX].item()
                relation_name = RELATION_ARCHETYPES[pred_idx]
                relation_str = (
                    f" | [Pred Type: {relation_name} ({confidence:.1%}, "
                    f"no-rel {no_relation_confidence:.1%})]"
                )
    elif relation_logits is not None:
        idx = list(candidate.group)
        # Gather the 6 internal edges
        pairs = [(idx[0], idx[1]), (idx[0], idx[2]), (idx[0], idx[3]), 
                 (idx[1], idx[2]), (idx[1], idx[3]), (idx[2], idx[3])]
        
        probs = []
        for u, v in pairs:
            edge_logits = relation_logits[u, v]
            edge_probs = torch.softmax(edge_logits, dim=-1)
            probs.append(edge_probs)
        avg_probs = torch.stack(probs).mean(dim=0)
        
        pred_idx = relation_prediction_from_probabilities(avg_probs.cpu().tolist())
        if pred_idx is not None:
            confidence = avg_probs[pred_idx].item()
            relation_name = RELATION_ARCHETYPES[pred_idx]
            relation_str = f" | [Pred Type: {relation_name} ({confidence:.1%})]"
        
    return (
        f"   - Group {group_idx}: **{candidate.group_score:.4f}** | "
        f"{', '.join(candidate_words):<65} | {status}{relation_str}"
    )


def _candidate_combination_index(group: Tuple[int, ...]) -> int | None:
    sorted_group = tuple(sorted(group))
    try:
        return list(itertools.combinations(range(16), 4)).index(sorted_group)
    except ValueError:
        return None

def _preprocessed_features_are_current(puzzles: list) -> bool:
    if not puzzles:
        return True
    first = puzzles[0]
    if not isinstance(first, dict) or "edge_features" not in first:
        return True
    if first.get("feature_schema_version") != FEATURE_SCHEMA_VERSION:
        return False
    if first.get("relation_archetype_schema_version") != RELATION_ARCHETYPE_SCHEMA_VERSION:
        return False
    return first["edge_features"].shape[-1] == EDGE_FEATURE_DIM

def _gcn_checkpoint_filename() -> str:
    return "gcn_best.pt"

def _gcn_previous_best_checkpoint_filename() -> str:
    return "gcn_previous_best.pt"

def _gcn_all_time_best_checkpoint_filename() -> str:
    return f"gcn_all_time_best_v{FEATURE_SCHEMA_VERSION}.pt"

def _gcn_all_time_best_metadata_filename() -> str:
    return f"gcn_all_time_best_v{FEATURE_SCHEMA_VERSION}.json"

def _save_gcn_best_checkpoint(
    state_dict: Dict[str, torch.Tensor],
    best_path: str,
) -> None:
    torch.save(state_dict, best_path)

def _save_gcn_all_time_best_checkpoint(
    state_dict: Dict[str, torch.Tensor],
    checkpoint_path: str,
    metadata_path: str,
    val_mrr: float,
    epoch: int | None = None,
) -> None:
    os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
    torch.save(state_dict, checkpoint_path)
    metadata = _gcn_all_time_best_metadata(val_mrr, epoch)
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)

def _gcn_all_time_best_metadata(val_mrr: float, epoch: int | None = None) -> Dict[str, Any]:
    metadata = {
        "validation_mrr": float(val_mrr),
        "edge_feature_dim": EDGE_FEATURE_DIM,
        "feature_schema_version": FEATURE_SCHEMA_VERSION,
        "relation_archetype_schema_version": RELATION_ARCHETYPE_SCHEMA_VERSION,
        "default_node_feature_dim": DEFAULT_NODE_FEATURE_DIM,
    }
    if epoch is not None:
        metadata["epoch"] = int(epoch)
    return metadata

def _load_gcn_all_time_best_mrr(metadata_path: str) -> float:
    if not os.path.exists(metadata_path):
        return 0.0
    try:
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        if not _gcn_all_time_best_metadata_is_current(metadata):
            return 0.0
        return float(metadata.get("validation_mrr", 0.0))
    except Exception:
        return 0.0

def _gcn_all_time_best_metadata_is_current(metadata: Dict[str, Any]) -> bool:
    return (
        metadata.get("edge_feature_dim") == EDGE_FEATURE_DIM
        and metadata.get("feature_schema_version") == FEATURE_SCHEMA_VERSION
        and metadata.get("relation_archetype_schema_version")
        == RELATION_ARCHETYPE_SCHEMA_VERSION
        and metadata.get("default_node_feature_dim") == DEFAULT_NODE_FEATURE_DIM
    )

def _initialize_all_time_gcn_best(
    current_checkpoint_path: str,
    all_time_checkpoint_path: str,
    all_time_metadata_path: str,
    in_features: int,
    val_puzzles: list,
    extractor: FeatureExtractor,
    device: str,
) -> float:
    all_time_mrr = _load_gcn_all_time_best_mrr(all_time_metadata_path)
    if all_time_mrr > 0.0 and os.path.exists(all_time_checkpoint_path):
        try:
            state_dict = torch.load(all_time_checkpoint_path, map_location=device)
            if _gcn_checkpoint_matches_model(state_dict, in_features):
                print(f"Loaded all-time best GCN Validation MRR: {all_time_mrr:.4f}")
                return all_time_mrr
            else:
                print(
                    "Warning: All-time best GCN checkpoint is incompatible with the current model "
                    "architecture. Resetting all-time best."
                )
        except Exception as e:
            print(f"Warning: Failed to load all-time best GCN checkpoint: {e}")

    if not os.path.exists(current_checkpoint_path):
        return 0.0

    try:
        state_dict = torch.load(current_checkpoint_path, map_location=device)
        if not _gcn_checkpoint_matches_model(state_dict, in_features):
            return 0.0
        hidden_feats = get_hidden_features_from_state_dict(state_dict, default=32)
        baseline_gcn = build_gcn_model(
            in_features=in_features,
            hidden_features=hidden_feats,
            out_features=16,
            num_relations=EDGE_FEATURE_DIM,
        ).to(device)
        baseline_gcn.load_state_dict(state_dict)
        _, baseline_mrr = validate_gcn(
            baseline_gcn,
            val_puzzles,
            extractor,
            device,
            visualize=False,
        )
        _save_gcn_all_time_best_checkpoint(
            state_dict,
            all_time_checkpoint_path,
            all_time_metadata_path,
            baseline_mrr,
            epoch=None,
        )
        print(
            "Initialized all-time best GCN from existing checkpoint "
            f"with Validation MRR: {baseline_mrr:.4f}"
        )
        return baseline_mrr
    except Exception as e:
        print(f"Warning: Failed to initialize all-time best GCN checkpoint: {e}")
        return 0.0

def _preserve_existing_artifact(current_path: str, previous_path: str) -> None:
    if os.path.exists(current_path):
        os.makedirs(os.path.dirname(previous_path), exist_ok=True)
        shutil.copy2(current_path, previous_path)

def _gcn_checkpoint_matches_model(
    state_dict: Dict[str, torch.Tensor],
    expected_in_features: int = DEFAULT_NODE_FEATURE_DIM,
) -> bool:
    rel_weights = state_dict.get("gcn1.W_rel")
    relation_head = state_dict.get("relation_score_net.2.weight")
    group_relation_head = state_dict.get("group_relation_score_net.2.weight")
    input_proj = state_dict.get("input_proj.weight")
    return (
        rel_weights is not None
        and rel_weights.shape[0] == EDGE_FEATURE_DIM
        and relation_head is not None
        and relation_head.shape[0] == NUM_RELATION_ARCHETYPES
        and group_relation_head is not None
        and group_relation_head.shape[0] == NUM_RELATION_ARCHETYPES
        and input_proj is not None
        and input_proj.shape[1] == expected_in_features
    )

def _candidate_status(candidate_words: List[str], word_to_cat: Dict[str, Dict[str, Any]]) -> str:
    cat_counts = {}
    for word in candidate_words:
        cat_idx = word_to_cat[word]["cat_idx"]
        cat_counts[cat_idx] = cat_counts.get(cat_idx, 0) + 1

    best_cat_idx, max_overlap = max(cat_counts.items(), key=lambda item: item[1])
    matching_word = next(
        word for word in candidate_words
        if word_to_cat[word]["cat_idx"] == best_cat_idx
    )
    cat_info = word_to_cat[matching_word]
    if max_overlap == 4:
        return f"CORRECT GROUP ({cat_info['group']}, Level {cat_info['level']})"
    return (
        f"INCORRECT (Max overlap: {max_overlap}/4 with {cat_info['group']})"
    )


def _update_model_registry(
    model_name: str,
    metrics: Dict[str, str],
    stats: Dict[str, Any],
    registry_path: str = "models/model_registry.json"
) -> None:
    import datetime
    registry = {}
    if os.path.exists(registry_path):
        try:
            with open(registry_path, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load model registry: {e}")
            
    # Convert archetype stats
    archetype_metrics = {}
    if stats and "archetypes" in stats:
        for arch, arch_stats in stats["archetypes"].items():
            rank_count = arch_stats.get("rank_count", 0)
            avg_rank = arch_stats.get("rank_sum", 0) / rank_count if rank_count > 0 else 0.0
            exact_mrr = arch_stats.get("exact_mrr_sum", 0.0) / arch_stats.get("total", 1) if arch_stats.get("total", 0) > 0 else 0.0
            p_correct = arch_stats.get("pairwise_correct", 0)
            p_total = arch_stats.get("pairwise_total", 0)
            p_acc = p_correct / p_total if p_total > 0 else 0.0
            
            g_correct = arch_stats.get("group_correct", 0)
            g_total = arch_stats.get("group_total", 0)
            g_acc = g_correct / g_total if g_total > 0 else 0.0
            
            archetype_metrics[arch] = {
                "total": arch_stats.get("total", 0),
                "hit_top_candidates": arch_stats.get("hit_top_candidates", 0),
                "recall": arch_stats.get("hit_top_candidates", 0) / arch_stats.get("total", 1) if arch_stats.get("total", 0) > 0 else 0.0,
                "hit_top_5": arch_stats.get("hit_top_5", 0),
                "avg_best_rank": avg_rank,
                "exact_mrr": exact_mrr,
                "pairwise_acc": p_acc,
                "group_acc": g_acc
            }
            
    flat_metrics = {}
    for k, v in metrics.items():
        num = _parse_numeric_value(v)
        flat_metrics[k] = num if num is not None else v
        
    registry[model_name] = {
        "timestamp": datetime.datetime.now().isoformat(),
        "feature_schema_version": FEATURE_SCHEMA_VERSION,
        "edge_feature_dim": EDGE_FEATURE_DIM,
        "metrics": flat_metrics,
        "archetypes": archetype_metrics
    }
    
    # Also register raw_baseline if it exists and hasn't been registered yet
    raw_metrics_path = "visualizations/raw_candidates/raw_candidates_metrics.json"
    if "raw_baseline" not in registry and os.path.exists(raw_metrics_path):
        try:
            with open(raw_metrics_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
            registry["raw_baseline"] = {
                "timestamp": datetime.datetime.fromtimestamp(os.path.getmtime(raw_metrics_path)).isoformat(),
                "feature_schema_version": FEATURE_SCHEMA_VERSION,
                "metrics": {
                    "Validation puzzles": float(raw_data.get("puzzles", 0)),
                    "Overall GCN Candidate MRR": float(raw_data.get("mrr", 0.0)),
                    "Puzzles with complete partition candidates": float(raw_data.get("partitions_found", 0)),
                    "Avg correct groups in top partition": float(raw_data.get("avg_exact_groups_in_best_partition", 0.0)),
                    "Top partition solves all 4 groups": float(raw_data.get("perfect_best_partitions", 0.0))
                },
                "archetypes": {}
            }
        except Exception as e:
            print(f"Warning: Failed to auto-register raw baseline in registry: {e}")

    try:
        with open(registry_path, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, sort_keys=True)
        print(f"Registered model '{model_name}' in {registry_path}")
    except Exception as e:
        print(f"Warning: Failed to save model registry: {e}")


def _write_error_analysis_report(puzzle_mrrs: List[Dict[str, Any]], output_path: str) -> None:
    # Sort by MRR ascending
    sorted_puzzles = sorted(puzzle_mrrs, key=lambda x: x["mrr"])
    worst_puzzles = sorted_puzzles[:10]
    
    # Calculate archetype counts in worst puzzles
    worst_archetypes = {}
    total_worst_cats = 0
    for p in worst_puzzles:
        for cat in p["categories"]:
            rtype = cat.get("relation_type", "SYNONYM_OR_NEAR")
            worst_archetypes[rtype] = worst_archetypes.get(rtype, 0) + 1
            total_worst_cats += 1
            
    # Calculate archetype counts in all validation puzzles
    all_archetypes = {}
    total_all_cats = 0
    for p in puzzle_mrrs:
        for cat in p["categories"]:
            rtype = cat.get("relation_type", "SYNONYM_OR_NEAR")
            all_archetypes[rtype] = all_archetypes.get(rtype, 0) + 1
            total_all_cats += 1
            
    lines = [
        "# Validation Puzzle Error Analysis",
        "",
        "This report identifies and analyzes the 10 hardest validation puzzles based on GCN candidate Mean Reciprocal Rank (MRR).",
        "",
        "## Worst-Performing Puzzles Summary",
        "",
        "| Rank | Puzzle ID | GCN MRR | Words |",
        "|---|---:|---:|---|",
    ]
    for rank, p in enumerate(worst_puzzles, start=1):
        words_preview = ", ".join(p["words"][:6]) + "..."
        lines.append(f"| {rank} | {p['id']} | {p['mrr']:.4f} | {words_preview} |")
        
    lines.extend([
        "",
        "## Archetype Failure Distribution",
        "",
        "The table below shows the distribution of relation archetypes in the top 10 hardest puzzles compared to the overall validation set.",
        "A higher relative frequency in the hardest puzzles indicates that the model struggles disproportionately with that archetype.",
        "",
        "| Archetype | Count in Worst 10 | % in Worst 10 | Count in Val Set | % in Val Set | Delta Ratio |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    
    for arch in sorted(set(list(worst_archetypes.keys()) + list(all_archetypes.keys()))):
        worst_count = worst_archetypes.get(arch, 0)
        worst_pct = worst_count / total_worst_cats if total_worst_cats > 0 else 0.0
        val_count = all_archetypes.get(arch, 0)
        val_pct = val_count / total_all_cats if total_all_cats > 0 else 0.0
        ratio = worst_pct / val_pct if val_pct > 0 else 0.0
        
        ratio_str = f"{ratio:.2f}x" if ratio > 0 else "0.00x"
        if ratio > 1.2:
            ratio_str = f"🔴 {ratio_str} (Overrepresented)"
        elif ratio > 0 and ratio < 0.8:
            ratio_str = f"🟢 {ratio_str} (Underrepresented)"
            
        lines.append(
            f"| {arch} | {worst_count} | {worst_pct:.1%} | {val_count} | {val_pct:.1%} | {ratio_str} |"
        )
        
    lines.extend([
        "",
        "## Hardest Puzzles Detailed Breakdown",
        "",
    ])
    
    for rank, p in enumerate(worst_puzzles, start=1):
        lines.extend([
            f"### {rank}. Puzzle {p['id']} (GCN MRR: {p['mrr']:.4f})",
            f"**Words:** {', '.join(p['words'])}",
            "",
            "**Ground Truth Categories:**",
        ])
        for cat in sorted(p["categories"], key=lambda x: x["level"]):
            lines.append(
                f"- **Level {cat['level']} ({cat['group']})** [Type: {cat.get('relation_type', 'SYNONYM_OR_NEAR')}]: "
                f"{', '.join(cat['members'])}"
            )
        lines.extend(["", "---", ""])
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Generated error analysis report: {output_path}")

def compare_checkpoints(model_a_ref: str, model_b_ref: str, device: str) -> None:
    """
    Compares two models (by registry name or checkpoint path) on the validation set,
    prints a comparison table to the terminal, and writes visualizations/model_comparison_report.md.
    """
    import json
    # 1. Load registry to see if we can resolve names
    registry_path = "models/model_registry.json"
    registry = {}
    if os.path.exists(registry_path):
        try:
            with open(registry_path, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception:
            pass
            
    # Helper to get model data (either from registry or evaluate path)
    def get_model_data(ref: str) -> Dict[str, Any]:
        # Fallback for generic 'gcn_all_time_best' to current schema version
        if ref == "gcn_all_time_best":
            schema_ref = f"gcn_all_time_best_v{FEATURE_SCHEMA_VERSION}"
            if schema_ref in registry:
                print(f"Resolving 'gcn_all_time_best' to '{schema_ref}' from model registry.")
                return registry[schema_ref]
        # If it's a key in registry, return it
        if ref in registry:
            print(f"Loaded '{ref}' from model registry.")
            return registry[ref]
            
        # Otherwise, assume it's a checkpoint path
        if not os.path.exists(ref):
            raise FileNotFoundError(f"Could not find model registry key or file path: {ref}")
            
        print(f"Evaluating checkpoint '{ref}' on validation set...")
        # Load validation dataset
        preprocessed_path = "data/preprocessed_graphs.pt"
        from src.dataset import load_preprocessed_dataset
        _, val_puzzles, _ = load_preprocessed_dataset(preprocessed_path)
        
        # Load GCN
        in_features = val_puzzles[0]["node_features"].shape[1] if val_puzzles else DEFAULT_NODE_FEATURE_DIM
        state = torch.load(ref, map_location=device)
        if not _gcn_checkpoint_matches_model(state, in_features):
            raise ValueError(f"Checkpoint '{ref}' is incompatible with current GCN architecture.")
        hidden_feats = get_hidden_features_from_state_dict(state, default=32)
        gcn = build_gcn_model(
            in_features=in_features,
            hidden_features=hidden_feats,
            out_features=16,
            num_relations=EDGE_FEATURE_DIM
        ).to(device)
        gcn.load_state_dict(state)
        
        extractor = FeatureExtractor()
        stats, _, _ = _evaluate_gcn_model_stats(
            gcn, val_puzzles, extractor, device, top_k=5, collect_puzzle_details=False
        )
        
        # Format metrics and convert archetype stats
        metrics = _stats_to_metric_dict(stats)
        flat_metrics = {}
        for k, v in metrics.items():
            num = _parse_numeric_value(v)
            flat_metrics[k] = num if num is not None else v
            
        archetype_metrics = {}
        for arch, arch_stats in stats.get("archetypes", {}).items():
            rank_count = arch_stats.get("rank_count", 0)
            avg_rank = arch_stats.get("rank_sum", 0) / rank_count if rank_count > 0 else 0.0
            exact_mrr = arch_stats.get("exact_mrr_sum", 0.0) / arch_stats.get("total", 1) if arch_stats.get("total", 0) > 0 else 0.0
            p_correct = arch_stats.get("pairwise_correct", 0)
            p_total = arch_stats.get("pairwise_total", 0)
            p_acc = p_correct / p_total if p_total > 0 else 0.0
            
            g_correct = arch_stats.get("group_correct", 0)
            g_total = arch_stats.get("group_total", 0)
            g_acc = g_correct / g_total if g_total > 0 else 0.0
            
            archetype_metrics[arch] = {
                "total": arch_stats.get("total", 0),
                "hit_top_candidates": arch_stats.get("hit_top_candidates", 0),
                "recall": arch_stats.get("hit_top_candidates", 0) / arch_stats.get("total", 1) if arch_stats.get("total", 0) > 0 else 0.0,
                "hit_top_5": arch_stats.get("hit_top_5", 0),
                "avg_best_rank": avg_rank,
                "exact_mrr": exact_mrr,
                "pairwise_acc": p_acc,
                "group_acc": g_acc
            }
            
        import datetime
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "metrics": flat_metrics,
            "archetypes": archetype_metrics
        }
        
    data_a = get_model_data(model_a_ref)
    data_b = get_model_data(model_b_ref)
    
    # 2. Build comparison tables
    lines = [
        f"# Model Comparison Report",
        "",
        f"Comparing Model A (**{model_a_ref}**) vs Model B (**{model_b_ref}**).",
        "",
        "## Overall Metrics Comparison",
        "",
        "| Metric | Model A | Model B | Delta (B - A) | Status |",
        "|---|---:|---:|---:|---|",
    ]
    
    # Find all common metrics
    all_keys = sorted(list(set(data_a["metrics"].keys()) | set(data_b["metrics"].keys())))
    
    print("\n" + "="*80)
    print(f" MODEL COMPARISON: {model_a_ref} vs {model_b_ref}")
    print("="*80)
    print(f"{'Metric':<45} | {'Model A':>10} | {'Model B':>10} | {'Delta':>10}")
    print("-"*80)
    
    for key in all_keys:
        val_a = data_a["metrics"].get(key, "-")
        val_b = data_b["metrics"].get(key, "-")
        
        if isinstance(val_a, (int, float)) and isinstance(val_b, (int, float)):
            diff = val_b - val_a
            sign = "+" if diff > 0 else ""
            lower_is_better = "rank" in key.lower() or "loss" in key.lower()
            
            if abs(diff) < 1e-5:
                status = "No Change"
                delta_str = "0"
            elif lower_is_better:
                status = "🟢 Improved" if diff < 0 else "🔴 Regressed"
                delta_str = f"{sign}{diff:.4f}"
            else:
                status = "🟢 Improved" if diff > 0 else "🔴 Regressed"
                delta_str = f"{sign}{diff:.4f}"
                
            val_a_str = f"{val_a:.4f}" if isinstance(val_a, float) else str(val_a)
            val_b_str = f"{val_b:.4f}" if isinstance(val_b, float) else str(val_b)
            
            lines.append(f"| {key} | {val_a_str} | {val_b_str} | {delta_str} | {status} |")
            print(f"{key:<45} | {val_a_str:>10} | {val_b_str:>10} | {delta_str:>10} ({status})")
        else:
            lines.append(f"| {key} | {val_a} | {val_b} | - | - |")
            print(f"{key:<45} | {str(val_a):>10} | {str(val_b):>10} | {'-':>10}")
            
    # 3. Archetype comparison table
    lines.extend([
        "",
        "## Archetype Metrics Comparison",
        "",
        "| Archetype | Metric | Model A | Model B | Delta (B - A) | Status |",
        "|---|---|---:|---:|---:|---|",
    ])
    
    archetypes = sorted(list(set(data_a["archetypes"].keys()) | set(data_b["archetypes"].keys())))
    arch_metrics = ["recall", "exact_mrr", "pairwise_acc", "group_acc", "avg_best_rank"]
    
    print("\nArchetype Performance Comparison:")
    for arch in archetypes:
        arch_a = data_a["archetypes"].get(arch, {})
        arch_b = data_b["archetypes"].get(arch, {})
        
        has_printed_arch = False
        for m in arch_metrics:
            v_a = arch_a.get(m, 0.0)
            v_b = arch_b.get(m, 0.0)
            diff = v_b - v_a
            
            lower_is_better = m == "avg_best_rank"
            sign = "+" if diff > 0 else ""
            
            if abs(diff) < 1e-5:
                status = "No Change"
                delta_str = "0"
            elif lower_is_better:
                status = "🟢 Improved" if diff < 0 else "🔴 Regressed"
                delta_str = f"{sign}{diff:.4f}"
            else:
                status = "🟢 Improved" if diff > 0 else "🔴 Regressed"
                delta_str = f"{sign}{diff:.4f}"
                
            lines.append(f"| {arch} | {m} | {v_a:.4f} | {v_b:.4f} | {delta_str} | {status} |")
            
            # Print significant differences to terminal
            if abs(diff) >= 0.01:
                if not has_printed_arch:
                    print(f" - {arch}:")
                    has_printed_arch = True
                print(f"   * {m:<15}: {v_a:>6.2f} -> {v_b:>6.2f} | Delta: {delta_str:>6} ({status})")
                
    print("="*80)
    
    report_path = "visualizations/model_comparison_report.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Saved complete comparison report to {report_path}")


if __name__ == "__main__":
    import sys
    data_file = os.path.join(os.path.dirname(__file__), "../data/connections.json")
    train_pipeline(data_file, gcn_epochs=5, rl_episodes=50)
