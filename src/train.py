import os
import shutil
import itertools
import torch
import numpy as np
from typing import List, Dict, Any, Tuple
from src.dataset import load_dataset, ConnectionsPuzzle
from src.features import (
    DEFAULT_NODE_FEATURE_DIM,
    EDGE_FEATURE_DIM,
    FEATURE_SCHEMA_VERSION,
    FeatureExtractor,
)
from src.gcn import ConnectionsGCN, build_gcn_model, train_gcn_epoch, validate_gcn
from src.rl_agent import CANDIDATE_FEATURE_DIM, DQNAgent, train_rl_episodes
from src.env import ConnectionsEnv
from src.graph import ConnectionsGraph
from src.visualize import plot_connections_graph
from src.candidates import build_partition_candidates, partition_groups_for_actions
from src.relation_archetypes import (
    NUM_RELATION_ARCHETYPES,
    RELATION_ARCHETYPE_SCHEMA_VERSION,
    RELATION_ARCHETYPES,
    NO_RELATION_IDX,
    relation_prediction_from_probabilities,
)

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
):
    """
    Main training pipeline.
    1. Loads dataset.
    2. Trains GCN to generate candidate subgraphs.
    3. Trains RL (DQN) agent to navigate candidates and solve puzzles.
    4. Saves models.
    """
    print("Starting Connections Solver Training Pipeline...")
    os.makedirs(model_dir, exist_ok=True)
    
    # 1. Load Data
    preprocessed_path = os.path.join(os.path.dirname(data_path), "preprocessed_graphs.pt")
    if os.path.exists(preprocessed_path):
        from src.dataset import load_preprocessed_dataset
        print(f"Loading preprocessed graphs from {preprocessed_path}...")
        train_puzzles, val_puzzles, test_puzzles = load_preprocessed_dataset(preprocessed_path)
        if not _preprocessed_features_are_current(train_puzzles + val_puzzles + test_puzzles):
            print(
                "Preprocessed graphs are stale; expected feature schema "
                f"{FEATURE_SCHEMA_VERSION} with {EDGE_FEATURE_DIM} edge features. "
                "Loading raw dataset so features can be rebuilt."
            )
            train_puzzles, val_puzzles, test_puzzles = load_dataset(data_path)
    else:
        print(f"Loading raw dataset from {data_path}...")
        train_puzzles, val_puzzles, test_puzzles = load_dataset(data_path)
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
        hidden_features=32,
        out_features=16,
        num_relations=EDGE_FEATURE_DIM # edge features count
    ).to(device)
    
    gcn_weights_path = os.path.join(model_dir, _gcn_checkpoint_filename())
    previous_gcn_weights_path = os.path.join(model_dir, _gcn_previous_best_checkpoint_filename())
    
    if skip_gcn:
        print("\n--- Phase 1: Loading Pre-trained GCN (skipping training) ---")
        gcn_state = torch.load(gcn_weights_path, map_location=device)
        if not _gcn_checkpoint_matches_model(gcn_state, in_features):
            raise RuntimeError(
                "Existing GCN checkpoint is incompatible with the current model "
                "architecture. Retrain without --skip-gcn."
            )
        gcn.load_state_dict(gcn_state)
        _, best_mrr = validate_gcn(gcn, val_puzzles, extractor, device, visualize=False)
        print(f"Loaded GCN with Validation MRR: {best_mrr:.4f}")
    else:
        print("\n--- Phase 1: Training GCN ---")
        gcn_optimizer = torch.optim.Adam(gcn.parameters(), lr=1e-3, weight_decay=1e-5)
        _preserve_existing_artifact(gcn_weights_path, previous_gcn_weights_path)
        _preserve_existing_artifact(
            os.path.join("visualizations", "val_best.png"),
            os.path.join("visualizations", "val_previous_best.png"),
        )
        
        best_mrr = 0.0
        epochs_no_improve = 0
        for epoch in range(1, gcn_epochs + 1):
            loss = train_gcn_epoch(gcn, train_puzzles, extractor, gcn_optimizer, device)
            val_loss, val_mrr = validate_gcn(gcn, val_puzzles, extractor, device, visualize=False)
            
            print(f"Epoch {epoch:02d}/{gcn_epochs:02d} | Train Loss: {loss:.4f} | Val Loss: {val_loss:.4f} | Val MRR: {val_mrr:.4f}")
            
            # Save best GCN and store its visualization
            if val_mrr > best_mrr:
                best_mrr = val_mrr
                epochs_no_improve = 0
                _save_gcn_best_checkpoint(
                    gcn.state_dict(),
                    gcn_weights_path,
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
                
        # Load best GCN for RL training
        gcn.load_state_dict(torch.load(gcn_weights_path, map_location=device))
        print(f"GCN training complete. Best Validation MRR: {best_mrr:.4f}")

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
    for i in range(0, rl_episodes, eval_freq):
        chunk_episodes = min(eval_freq, rl_episodes - i)
        stats = train_rl_episodes(agent, gcn, train_puzzles, extractor, chunk_episodes, batch_size=batch_size)
        
        # Calculate recent metrics
        win_rate = np.mean([s["won"] for s in stats])
        avg_reward = np.mean([s["reward"] for s in stats])
        avg_steps = np.mean([s["steps"] for s in stats])
        
        print(f"RL Episode {i + chunk_episodes:04d}/{rl_episodes:04d} | Win Rate: {win_rate:.2%} | Avg Reward: {avg_reward:.2f} | Avg Steps: {avg_steps:.1f} | Epsilon: {agent.epsilon:.3f}")
        
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
    summary_path = os.path.join(output_dir, "candidates_summary.md")
    previous_summary_path = os.path.join(output_dir, "candidates_previous_best_summary.md")
    _preserve_existing_artifact(summary_path, previous_summary_path)
    gcn.eval()
    top_group_limit = top_k * 4
    aggregate_stats = _new_validation_summary_stats(top_group_limit)

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
    puzzle_lines = []

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

            node_embeddings, edge_probs, relation_logits, group_relation_logits = gcn(
                graph.node_features,
                graph.get_multi_relational_adjacency(),
                graph.edge_features,
                return_group_logits=True,
            )
            candidates = gcn.get_candidate_subgraphs(edge_probs, group_relation_logits)
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
            )
            true_cats = [word_to_cat[w]["cat_idx"] for w in words]
            edge_probs_np = edge_probs.cpu().numpy()

            if idx < 5:
                visualization_path = os.path.join(output_dir, f"val_puzzle_{puzzle_id}.png")
                previous_visualization_path = os.path.join(
                    output_dir,
                    f"val_previous_best_puzzle_{puzzle_id}.png",
                )
                _preserve_existing_artifact(visualization_path, previous_visualization_path)
                plot_connections_graph(
                    words,
                    edge_probs_np,
                    true_categories=true_cats,
                    threshold=0.45,
                    filepath=visualization_path,
                    title=f"GCN Edge Predictions - Puzzle {puzzle_id}",
                    relation_logits=relation_logits.cpu().numpy()
                )

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

            if (idx + 1) % 10 == 0 or (idx + 1) == len(val_puzzles):
                print(f"Updated {idx + 1}/{len(val_puzzles)} validation visualizations")

    lines.extend(_format_validation_summary_stats(aggregate_stats))
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
    }


def _update_validation_summary_stats(
    stats: Dict[str, Any],
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
    true_groups: Dict[int, Tuple[int, ...]],
    partitions: List[Any],
    action_candidates: List[Any],
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
            },
        )
        archetype_stats["total"] += 1
        best_rank = best_rank_by_cat.get(cat_idx)
        if best_rank is not None:
            archetype_stats["hit_top_candidates"] += 1
            archetype_stats["rank_sum"] += best_rank
            archetype_stats["rank_count"] += 1
            if best_rank <= 5:
                archetype_stats["hit_top_5"] += 1


def _format_validation_summary_stats(stats: Dict[str, Any]) -> List[str]:
    puzzles = max(1, stats["puzzles"])
    total_true_groups = stats["puzzles"] * 4
    top_group_limit = stats["top_group_limit"]
    ranks = stats["true_group_ranks"]
    mean_rank = float(np.mean(ranks)) if ranks else 0.0
    median_rank = float(np.median(ranks)) if ranks else 0.0

    lines = [
        "## Aggregate Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Validation puzzles | {stats['puzzles']} |",
        f"| Puzzles with complete partition candidates | {stats['with_partitions']} / {stats['puzzles']} ({_pct(stats['with_partitions'], stats['puzzles'])}) |",
        f"| Top partition solves all 4 groups | {stats['top_partition_solved']} / {stats['puzzles']} ({_pct(stats['top_partition_solved'], stats['puzzles'])}) |",
        f"| Any top-{stats['top_group_limit'] // 4} partition solves all 4 groups | {stats['best_top_k_partition_solved']} / {stats['puzzles']} ({_pct(stats['best_top_k_partition_solved'], stats['puzzles'])}) |",
        f"| Avg correct groups in top partition | {stats['top_partition_correct_groups'] / puzzles:.2f} / 4 |",
        f"| Avg best correct groups across top partitions | {stats['best_top_k_partition_correct_groups'] / puzzles:.2f} / 4 |",
        f"| True groups in top-{top_group_limit} candidates | {stats['true_groups_in_top_candidates']} / {total_true_groups} ({_pct(stats['true_groups_in_top_candidates'], total_true_groups)}) |",
        f"| Puzzles with any true group in top-{top_group_limit} | {stats['puzzles_with_any_true_group']} / {stats['puzzles']} ({_pct(stats['puzzles_with_any_true_group'], stats['puzzles'])}) |",
        f"| Puzzles with all true groups in top-{top_group_limit} | {stats['puzzles_with_all_true_groups']} / {stats['puzzles']} ({_pct(stats['puzzles_with_all_true_groups'], stats['puzzles'])}) |",
        f"| Mean rank of true groups found in top-{top_group_limit} | {mean_rank:.2f} |",
        f"| Median rank of true groups found in top-{top_group_limit} | {median_rank:.1f} |",
        f"| 3-of-4 near-miss candidates in top-{top_group_limit} | {stats['near_miss_3_of_4_candidates']} |",
        "",
        "### Recall By Relation Archetype",
        "",
        f"| Archetype | True Groups | Hit Top {top_group_limit} | Recall | Hit Top 5 | Avg Best Rank |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for archetype, archetype_stats in sorted(stats["archetypes"].items()):
        rank_count = archetype_stats["rank_count"]
        avg_rank = (
            archetype_stats["rank_sum"] / rank_count
            if rank_count
            else 0.0
        )
        lines.append(
            f"| {archetype} | {archetype_stats['total']} | "
            f"{archetype_stats['hit_top_candidates']} | "
            f"{_pct(archetype_stats['hit_top_candidates'], archetype_stats['total'])} | "
            f"{archetype_stats['hit_top_5']} | "
            f"{avg_rank:.2f} |"
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

def _save_gcn_best_checkpoint(
    state_dict: Dict[str, torch.Tensor],
    best_path: str,
) -> None:
    torch.save(state_dict, best_path)

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

if __name__ == "__main__":
    import sys
    data_file = os.path.join(os.path.dirname(__file__), "../data/connections.json")
    train_pipeline(data_file, gcn_epochs=5, rl_episodes=50)
