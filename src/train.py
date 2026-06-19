import os
import torch
import numpy as np
from typing import List, Dict, Any
from src.dataset import load_dataset, ConnectionsPuzzle
from src.features import EDGE_FEATURE_DIM, FEATURE_SCHEMA_VERSION, FeatureExtractor
from src.gcn import ConnectionsGCN, build_gcn_model, train_gcn_epoch, validate_gcn
from src.rl_agent import CANDIDATE_FEATURE_DIM, DQNAgent, train_rl_episodes
from src.env import ConnectionsEnv
from src.graph import ConnectionsGraph
from src.visualize import plot_connections_graph
from src.candidates import build_partition_candidates, partition_groups_for_actions

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
    
    # 2. Train or Load GCN
    gcn = build_gcn_model(
        in_features=7, # node features count
        hidden_features=32,
        out_features=16,
        num_relations=EDGE_FEATURE_DIM # edge features count
    ).to(device)
    
    gcn_weights_path = os.path.join(model_dir, _gcn_checkpoint_filename())
    
    if skip_gcn:
        print("\n--- Phase 1: Loading Pre-trained GCN (skipping training) ---")
        gcn_state = torch.load(gcn_weights_path, map_location=device)
        if not _gcn_checkpoint_matches_model(gcn_state):
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
                torch.save(gcn.state_dict(), gcn_weights_path)
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
                node_embeddings, edge_probs, _ = gcn(
                    graph.node_features, graph.get_multi_relational_adjacency()
                )
                candidates = graph.filter_candidates(gcn.get_candidate_subgraphs(edge_probs))
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
    gcn.eval()

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

            node_embeddings, edge_probs, relation_logits = gcn(graph.node_features, graph.get_multi_relational_adjacency())
            candidates = gcn.get_candidate_subgraphs(edge_probs)
            active_mask = np.ones(16, dtype=np.float32)
            partitions = build_partition_candidates(candidates, active_mask, top_n=200)
            action_candidates = partition_groups_for_actions(partitions, candidates, active_mask)
            true_cats = [word_to_cat[w]["cat_idx"] for w in words]
            edge_probs_np = edge_probs.cpu().numpy()

            if idx < 5:
                plot_connections_graph(
                    words,
                    edge_probs_np,
                    true_categories=true_cats,
                    threshold=0.45,
                    filepath=os.path.join(output_dir, f"val_puzzle_{puzzle_id}.png"),
                    title=f"GCN Edge Predictions - Puzzle {puzzle_id}",
                    relation_logits=relation_logits.cpu().numpy()
                )

            lines.extend([
                f"## Puzzle {idx} (ID: {puzzle_id})",
                f"**Words on Board:** {', '.join(words)}",
                "",
                "### Ground Truth Categories:",
            ])
            for cat in sorted(categories, key=lambda item: item["level"]):
                members = ", ".join(member.strip().upper() for member in cat["members"])
                rtype_str = f" [Type: {cat.get('relation_type', 'SYNONYM')}]"
                lines.append(f"* **Level {cat['level']} ({cat['group']}){rtype_str}:** {members}")

            lines.extend(["", "### Top Candidate Partitions:"])
            if partitions:
                for rank, partition in enumerate(partitions[:top_k], start=1):
                    lines.append(f"{rank}. **Partition Score: {partition.score:.4f}**")
                    for group_idx, candidate in enumerate(partition.groups, start=1):
                        lines.append(
                            _candidate_summary_line(
                                group_idx,
                                candidate,
                                words,
                                word_to_cat,
                                relation_logits
                            )
                        )
            else:
                lines.append(
                    "_No complete four-group partitions were found from the bounded search; "
                    "showing top individual candidate groups instead._"
                )

            lines.extend(["", "### Top Candidate Groups:"])
            if action_candidates:
                for group_idx, candidate in enumerate(action_candidates[:top_k * 4], start=1):
                    lines.append(
                        _candidate_summary_line(
                            group_idx,
                            candidate,
                            words,
                            word_to_cat,
                            relation_logits
                        )
                    )
            else:
                lines.append("_No candidate groups were available._")
            lines.extend(["", "---", ""])

            if (idx + 1) % 10 == 0 or (idx + 1) == len(val_puzzles):
                print(f"Updated {idx + 1}/{len(val_puzzles)} validation visualizations")

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Updated validation candidate summary: {summary_path}")

def _puzzle_value(puzzle: Any, field: str):
    return puzzle[field] if isinstance(puzzle, dict) else getattr(puzzle, field)

def _candidate_summary_line(
    group_idx: int,
    candidate: Any,
    words: List[str],
    word_to_cat: Dict[str, Dict[str, Any]],
    relation_logits = None
) -> str:
    candidate_words = [words[i] for i in candidate.group]
    status = _candidate_status(candidate_words, word_to_cat)
    
    relation_str = ""
    if relation_logits is not None:
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
        
        pred_idx = torch.argmax(avg_probs).item()
        confidence = avg_probs[pred_idx].item()
        
        archetypes = ["SYNONYM", "WORDPLAY", "PHRASE_COMPLETION", "TRIVIA_ENCYCLOPEDIC", "MORPHOLOGY"]
        relation_str = f" | [Pred Type: {archetypes[pred_idx]} ({confidence:.1%})]"
        
    return (
        f"   - Group {group_idx}: **{candidate.group_score:.4f}** | "
        f"{', '.join(candidate_words):<65} | {status}{relation_str}"
    )

def _preprocessed_features_are_current(puzzles: list) -> bool:
    if not puzzles:
        return True
    first = puzzles[0]
    if not isinstance(first, dict) or "edge_features" not in first:
        return True
    if first.get("feature_schema_version") != FEATURE_SCHEMA_VERSION:
        return False
    return first["edge_features"].shape[-1] == EDGE_FEATURE_DIM

def _gcn_checkpoint_filename() -> str:
    return "gcn_best.pt"

def _gcn_checkpoint_matches_model(state_dict: Dict[str, torch.Tensor]) -> bool:
    rel_weights = state_dict.get("gcn1.W_rel")
    relation_head = state_dict.get("relation_score_net.2.weight")
    return (
        rel_weights is not None
        and rel_weights.shape[0] == EDGE_FEATURE_DIM
        and relation_head is not None
        and relation_head.shape[0] == 5
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
