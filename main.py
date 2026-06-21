import os
import argparse
import torch
import numpy as np
from typing import List
from src.dataset import ConnectionsPuzzle
from src.features import DEFAULT_NODE_FEATURE_DIM, EDGE_FEATURE_DIM, FeatureExtractor
from src.graph import ConnectionsGraph
from src.gcn import build_gcn_model, get_hidden_features_from_state_dict
from src.rl_agent import CANDIDATE_FEATURE_DIM, DQNAgent
from src.env import ConnectionsEnv
from src.visualize import plot_connections_graph
from src.train import train_pipeline, compare_checkpoints, _gcn_all_time_best_checkpoint_filename
from src.relation_archetypes import NUM_RELATION_ARCHETYPES

def auto_device() -> str:
    if torch.cuda.is_available():
        return "cuda"
    # CPU is preferred over MPS on Apple Silicon because dispatching many small GCN
    # operations to the GPU has high latency, making CPU training ~4.5x faster.
    return "cpu"


def solve_custom_board(
    words_str: str,
    model_dir: str = "models",
    device: str = "cpu",
    gcn_checkpoint: str = "all-time",
):
    """
    Solves a custom 16-word board using the trained GCN and DQN models.
    """
    words = [w.strip().upper() for w in words_str.split(",")]
    if len(words) != 16:
        print(f"Error: A Connections board must have exactly 16 words. Found {len(words)}.")
        print(f"Provided: {words}")
        return

    print(f"\nSolving Custom Connections Board:")
    print("Words: " + ", ".join(words))
    
    # Check if models exist
    if gcn_checkpoint == "all-time":
        gcn_path = os.path.join(model_dir, _gcn_all_time_best_checkpoint_filename())
        if not os.path.exists(gcn_path):
            gcn_path = os.path.join(model_dir, _gcn_checkpoint_filename())
    else:
        gcn_path = os.path.join(model_dir, _gcn_checkpoint_filename())
        
    dqn_path = os.path.join(model_dir, "dqn_q_net.pt")
    if not os.path.exists(gcn_path) or not os.path.exists(dqn_path):
        print(f"Error: Trained models not found at {model_dir}. Please run training first via: python main.py --train")
        return
        
    extractor = FeatureExtractor(ngram_live_lookup=True)
    graph = ConnectionsGraph(words, extractor, device=device)
    
    # Load Models
    gcn_state = torch.load(gcn_path, map_location=device)
    if not _is_gcn_checkpoint_compatible(gcn_state, graph.node_features.shape[1]):
        print(
            "Error: Existing GCN checkpoint is incompatible with the current "
            "GCN architecture. Retrain via: python main.py --train"
        )
        return
    hidden_feats = get_hidden_features_from_state_dict(gcn_state, default=128)
    gcn = build_gcn_model(
        in_features=graph.node_features.shape[1],
        hidden_features=hidden_feats,
        out_features=16,
        num_relations=EDGE_FEATURE_DIM,
    ).to(device)
    gcn.load_state_dict(gcn_state)
    gcn.eval()
    
    agent = DQNAgent(state_dim=33, candidate_dim=CANDIDATE_FEATURE_DIM, device=device)
    dqn_state = torch.load(dqn_path, map_location=device)
    if not _is_dqn_checkpoint_compatible(dqn_state):
        print(
            "Error: Existing DQN checkpoint is incompatible with partition-aware "
            "candidate features. Retrain via: python main.py --train --skip-gcn"
        )
        return
    agent.q_net.load_state_dict(dqn_state)
    agent.q_net.eval()
    agent.epsilon = 0.0 # pure greedy
    
    # Run initial GCN inference for visualization
    with torch.no_grad():
        node_embeddings, edge_probs, _, group_relation_logits = gcn(
            graph.node_features,
            graph.get_multi_relational_adjacency(),
            graph.edge_features,
            return_group_logits=True,
        )
        
    # Visualize the initial graph
    viz_path = os.path.join("visualizations", "custom_board_clusters.png")
    plot_connections_graph(
        words, 
        edge_probs.cpu().numpy(), 
        true_categories=None, 
        threshold=0.2, 
        filepath=viz_path,
        title="GCN Clusters - Custom Board"
    )
    print(f"Saved custom board graph visualization to: {viz_path}")
    
    # Initialize environment mockup
    # For custom boards, we don't know the ground truth categories, but we can simulate the game state tracking
    active_mask = np.ones(16, dtype=np.float32)
    mistakes_left = 4
    submission_history = np.zeros(16, dtype=np.float32)
    solved_groups = []
    
    print("\n--- Solver Traversal Strategy ---")
    step = 0
    while len(solved_groups) < 4 and mistakes_left > 0:
        step += 1
        # Re-build observation
        mistakes_norm = np.array([mistakes_left / 4.0], dtype=np.float32)
        obs = np.concatenate([active_mask, mistakes_norm, submission_history])

        # Re-run GCN on the feedback-adapted graph before each guess
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
        
        # Build current candidate features based on active words
        cand_list, cand_feats = agent.get_candidate_features(action_candidates, node_embeddings, obs)
        
        # Select action
        action_idx = agent.select_action(obs, cand_list, cand_feats)
        action_indices = cand_list[action_idx]
        guess_words = [words[i] for i in action_indices]
        
        print(f"\nStep {step} | Guessed Category: {', '.join(guess_words)}")
        
        # Prompt user for feedback (or simulate if we want, but since it's a CLI tool, we ask the user!)
        # To make it fully interactive, we prompt:
        feedback = input("Is the guess correct? (y / 1away / n): ").strip().lower()
        
        if feedback in ('y', 'yes', '1'):
            # Correct guess
            for idx in action_indices:
                active_mask[idx] = 0.0
            solved_groups.append(guess_words)
            graph.update_edges_from_feedback(action_indices, "Correct!")
            print(f"--> Success! {4 - len(solved_groups)} categories remaining.")
        else:
            # Increment submission count for wrong guess
            for idx in action_indices:
                submission_history[idx] += 1.0
            mistakes_left -= 1
            
            if feedback in ('1away', 'one away', '3'):
                graph.update_edges_from_feedback(action_indices, "One Away")
                print(f"--> One Away! {mistakes_left} lives left.")
            else:
                graph.update_edges_from_feedback(action_indices, "Incorrect")
                print(f"--> Incorrect. {mistakes_left} lives left.")
                
    if len(solved_groups) == 4:
        print("\n🎉 PUZZLE SOLVED SUCCESSFULY!")
        for idx, group in enumerate(solved_groups):
            print(f"Group {idx + 1}: {', '.join(group)}")
    else:
        print("\n💀 Game Over. Failed to solve the board.")

def main():
    parser = argparse.ArgumentParser(description="Connections augmented GCN + RL Solver")
    parser.add_argument("--train", action="store_true", help="Run the full training pipeline")
    parser.add_argument("--skip-gcn", action="store_true", help="Skip GCN training, load existing weights, retrain RL only")
    parser.add_argument("--gcn-epochs", type=int, default=20, help="Number of GCN training epochs")
    parser.add_argument("--gcn-patience", type=int, default=15, help="Early stopping patience for GCN training")
    parser.add_argument("--rl-episodes", type=int, default=300, help="Number of RL training episodes")
    parser.add_argument("--seed", type=int, help="Seed for repeatable train/validation splits and training RNGs")
    parser.add_argument("--solve", type=str, help="16 comma-separated words to solve interactively")
    parser.add_argument("--device", type=str, default=auto_device(), help="Device to use for training (cpu, mps, cuda)")
    parser.add_argument(
        "--gcn-checkpoint",
        type=str,
        choices=["best", "all-time"],
        default="all-time",
        help="Which GCN checkpoint to load (best or all-time) when --skip-gcn is set or when solving (default: all-time)",
    )
    parser.add_argument(
        "--skip-validation-artifacts",
        action="store_true",
        help="Skip regenerating validation PNGs and candidate summary after GCN training",
    )
    parser.add_argument(
        "--compare-models",
        nargs=2,
        metavar=("MODEL_A", "MODEL_B"),
        help="Compare two GCN models by registry name (e.g. gcn_best, gcn_all_time_best, raw_baseline) or checkpoint file path"
    )
    
    args = parser.parse_args()
    
    data_file = os.path.join(os.path.dirname(__file__), "data", "connections.json")
    
    if args.train:
        train_pipeline(
            data_path=data_file,
            gcn_epochs=args.gcn_epochs,
            rl_episodes=args.rl_episodes,
            device=args.device,
            gcn_patience=args.gcn_patience,
            skip_gcn=args.skip_gcn,
            update_artifacts=not args.skip_validation_artifacts,
            seed=args.seed,
            gcn_checkpoint=args.gcn_checkpoint,
        )
    elif args.compare_models:
        compare_checkpoints(args.compare_models[0], args.compare_models[1], device=args.device)
    elif args.solve:
        solve_custom_board(args.solve, device=args.device, gcn_checkpoint=args.gcn_checkpoint)
    else:
        parser.print_help()

def _is_dqn_checkpoint_compatible(state_dict: dict) -> bool:
    first_layer_weight = state_dict.get("net.0.weight")
    if first_layer_weight is None:
        return False
    expected_inputs = 33 + CANDIDATE_FEATURE_DIM
    return first_layer_weight.shape[1] == expected_inputs

def _gcn_checkpoint_filename() -> str:
    return "gcn_best.pt"

def _is_gcn_checkpoint_compatible(
    state_dict: dict,
    expected_in_features: int = DEFAULT_NODE_FEATURE_DIM,
) -> bool:
    rel_weights = state_dict.get("gcn1.W_rel")
    relation_head = state_dict.get("relation_score_net.2.weight")
    group_relation_head = state_dict.get("group_relation_score_net.2.weight")
    input_proj = state_dict.get("input_proj.weight")
    
    # Expect the current relation score net and input projection layer to be present.
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

if __name__ == "__main__":
    main()
