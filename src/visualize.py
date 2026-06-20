import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Optional
from src.relation_archetypes import RELATION_ARCHETYPES, relation_prediction_from_probabilities

def plot_connections_graph(
    words: List[str],
    similarity_matrix: np.ndarray,
    true_categories: Optional[List[int]] = None,
    threshold: float = 0.15,
    filepath: Optional[str] = None,
    title: str = "Connections Graph Connections",
    relation_logits: Optional[np.ndarray] = None
):
    """
    Plots a 16-node graph of the Connections puzzle, drawing connections based on similarity scores.
    
    Args:
        words: List of 16 word labels.
        similarity_matrix: 16x16 numpy array of pairwise similarity/probability scores.
        true_categories: Optional list of 16 integers (0, 1, 2, 3) indicating category groups.
        threshold: Edge weight threshold below which edges are not drawn.
        filepath: Filepath to save the figure. If directory doesn't exist, it will be created.
        title: Title of the plot.
        relation_logits: Optional 16x16xN numpy array of predicted relation type logits.
    """
    n = len(words)
    assert n == 16, "Graph must have exactly 16 nodes."
    
    # Ensure similarity matrix is symmetric (if not already)
    sim = (similarity_matrix + similarity_matrix.T) / 2.0
    
    # Initialize graph
    G = nx.Graph()
    for i, word in enumerate(words):
        G.add_node(i, label=word)
        
    # Add edges with weights above threshold
    for i in range(n):
        for j in range(i + 1, n):
            weight = sim[i, j]
            if weight >= threshold:
                G.add_edge(i, j, weight=float(weight))
                
    # Define nice palette for the 4 categories (Yellow, Green, Blue, Purple)
    # matching the Connections game aesthetic.
    category_colors = {
        0: "#F9E076", # Yellow (Easy)
        1: "#A0C9A2", # Green (Medium)
        2: "#B5E2FA", # Blue (Hard)
        3: "#D6A2E8"  # Purple (Tricky)
    }
    default_node_color = "#E0E0E0"
    
    # Color nodes
    node_colors = []
    for i in range(n):
        if true_categories is not None:
            cat = true_categories[i]
            node_colors.append(category_colors.get(cat, default_node_color))
        else:
            node_colors.append(default_node_color)
            
    # Set layout
    plt.figure(figsize=(10, 10), facecolor='#FDFDFD')
    pos = nx.spring_layout(G, k=0.45, seed=42)
    
    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos, 
        node_color=node_colors, 
        node_size=2000, 
        edgecolors='#666666', 
        linewidths=1.5
    )
    
    # Draw labels (words)
    labels = {i: words[i] for i in range(n)}
    nx.draw_networkx_labels(
        G, pos, 
        labels=labels, 
        font_size=10, 
        font_weight="bold", 
        font_family="sans-serif"
    )
    
    # Draw edges with varying thickness and transparency based on similarity
    edges = G.edges(data=True)
    if edges:
        weights = [data['weight'] for _, _, data in edges]
        # Normalize weights for visualization
        max_w = max(weights) if weights else 1.0
        edge_widths = [max(1, (w / max_w) * 6.0) for w in weights]
        edge_alphas = [max(0.1, min(0.9, w)) for w in weights]
        
        # Color palette for predicted positive relation types.
        archetype_colors = {
            1: "#2ECC71", # SEMANTIC_SET -> Emerald Green
            2: "#708090", # SYNONYM_OR_NEAR -> Slate Gray
            3: "#9B59B6", # NAMED_ENTITY_SET -> Purple
            4: "#3498DB", # WORD_FORM -> Sky Blue
            5: "#F1C40F", # SOUND_OR_SPELLING -> Yellow
            6: "#E74C3C", # WORDPLAY_TRANSFORM -> Red
            7: "#E67E22", # FILL_IN_THE_BLANK -> Orange
            8: "#16A085", # COMMON_PHRASE -> Teal
        }
        archetype_labels = {
            idx: name.replace("_", " ").title()
            for idx, name in enumerate(RELATION_ARCHETYPES)
        }
        drawn_types = set()
        
        # We draw edges one-by-one or in groups to support individual alphas and colors
        for (u, v, data), w, alpha in zip(edges, edge_widths, edge_alphas):
            color = "#4A90E2" # default blue
            label = None
            if relation_logits is not None:
                # Get prediction from symmetric relation logits only if it clears the no-relation gate.
                edge_logits = relation_logits[u, v]
                exp_logits = np.exp(edge_logits - np.max(edge_logits))
                edge_probs = exp_logits / np.sum(exp_logits)
                pred_type = relation_prediction_from_probabilities(edge_probs)
                if pred_type is not None:
                    color = archetype_colors.get(pred_type, color)
                if pred_type is not None and pred_type not in drawn_types:
                    drawn_types.add(pred_type)
                    label = archetype_labels.get(pred_type)
                    
            nx.draw_networkx_edges(
                G, pos, 
                edgelist=[(u, v)], 
                width=w, 
                alpha=alpha, 
                edge_color=color,
                label=label
            )
            
        if relation_logits is not None and drawn_types:
            import matplotlib.patches as mpatches
            legend_handles = [
                mpatches.Patch(color=archetype_colors[t], label=archetype_labels[t])
                for t in sorted(list(drawn_types))
            ]
            plt.legend(handles=legend_handles, loc="upper right")
            
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.axis("off")
    plt.tight_layout()
    
    if filepath:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        plt.savefig(filepath, dpi=150, facecolor=plt.gcf().get_facecolor(), bbox_inches='tight')
        plt.close()
    else:
        # Default save path if None provided
        default_dir = os.path.join(os.path.dirname(__file__), "../visualizations")
        os.makedirs(default_dir, exist_ok=True)
        default_path = os.path.join(default_dir, "latest_connections_graph.png")
        plt.savefig(default_path, dpi=150, facecolor=plt.gcf().get_facecolor(), bbox_inches='tight')
        plt.close()
        print(f"Saved visualization to {default_path}")

def plot_gcn_learning_curves(history_path: str, output_path: str) -> None:
    """
    Plots the GCN learning curves (losses and validation MRR over epochs).
    """
    import json
    if not os.path.exists(history_path):
        print(f"Warning: History file {history_path} not found. Skipping plot.")
        return
        
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)
        
    if not history:
        return
        
    epochs = [item["epoch"] for item in history]
    train_losses = [item["train_loss"] for item in history]
    val_losses = [item["val_loss"] for item in history]
    val_mrrs = [item["val_mrr"] for item in history]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Loss plot
    ax1.plot(epochs, train_losses, label="Train Loss", color="#E74C3C", marker="o", linewidth=2)
    ax1.plot(epochs, val_losses, label="Val Loss", color="#3498DB", marker="s", linewidth=2)
    ax1.set_xlabel("Epoch", fontweight="bold")
    ax1.set_ylabel("Loss", fontweight="bold")
    ax1.set_title("GCN Loss Curves", fontsize=12, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend()
    
    # MRR plot
    ax2.plot(epochs, val_mrrs, label="Val MRR", color="#2ECC71", marker="^", linewidth=2)
    ax2.set_xlabel("Epoch", fontweight="bold")
    ax2.set_ylabel("Mean Reciprocal Rank (MRR)", fontweight="bold")
    ax2.set_title("GCN Validation MRR", fontsize=12, fontweight="bold")
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend()
    
    plt.suptitle("GCN Model Training Progress", fontsize=14, fontweight="bold", y=0.98)
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved GCN learning curves to {output_path}")


def plot_dqn_learning_curves(history_path: str, output_path: str) -> None:
    """
    Plots the DQN training progress (win rate, average reward, and average steps).
    """
    import json
    if not os.path.exists(history_path):
        print(f"Warning: History file {history_path} not found. Skipping plot.")
        return
        
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)
        
    if not history:
        return
        
    episodes = [item["episode"] for item in history]
    win_rates = [item["win_rate"] for item in history]
    avg_rewards = [item["avg_reward"] for item in history]
    avg_steps = [item["avg_steps"] for item in history]
    epsilons = [item.get("epsilon", 0.0) for item in history]
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    
    # Win rate and Epsilon plot
    ax1.plot(episodes, win_rates, label="Win Rate", color="#9B59B6", marker="o", linewidth=2)
    ax1_twin = ax1.twinx()
    ax1_twin.plot(episodes, epsilons, label="Epsilon", color="#7F8C8D", linestyle="--", linewidth=1.5)
    ax1.set_xlabel("Episode", fontweight="bold")
    ax1.set_ylabel("Win Rate", fontweight="bold")
    ax1_twin.set_ylabel("Epsilon Exploration", color="#7F8C8D", fontweight="bold")
    ax1.set_title("RL DQN Win Rate & Exploration", fontsize=12, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.6)
    
    # Merge legends from dual axis
    lines, labels = ax1.get_legend_handles_labels()
    lines_twin, labels_twin = ax1_twin.get_legend_handles_labels()
    ax1.legend(lines + lines_twin, labels + labels_twin, loc="upper left")
    
    # Reward plot
    ax2.plot(episodes, avg_rewards, label="Avg Reward", color="#E67E22", marker="s", linewidth=2)
    ax2.set_xlabel("Episode", fontweight="bold")
    ax2.set_ylabel("Reward", fontweight="bold")
    ax2.set_title("RL DQN Average Reward", fontsize=12, fontweight="bold")
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend()
    
    # Steps plot
    ax3.plot(episodes, avg_steps, label="Avg Steps", color="#1ABC9C", marker="^", linewidth=2)
    ax3.set_xlabel("Episode", fontweight="bold")
    ax3.set_ylabel("Steps / Submissions", fontweight="bold")
    ax3.set_title("RL DQN Average Submissions", fontsize=12, fontweight="bold")
    ax3.grid(True, linestyle="--", alpha=0.6)
    ax3.legend()
    
    plt.suptitle("RL DQN Agent Training Progress", fontsize=14, fontweight="bold", y=0.98)
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved DQN learning curves to {output_path}")


if __name__ == "__main__":
    # Test plotting a random matrix
    test_words = [
        "HAIL", "RAIN", "SLEET", "SNOW",
        "BUCKS", "HEAT", "JAZZ", "NETS",
        "OPTION", "RETURN", "SHIFT", "TAB",
        "KAYAK", "LEVEL", "MOM", "RACECAR"
    ]
    # Simple simulated similarity matrix with 4 clusters
    sim_mat = np.zeros((16, 16))
    for i in range(16):
        cat_i = i // 4
        for j in range(16):
            cat_j = j // 4
            if cat_i == cat_j:
                sim_mat[i, j] = 0.8 + np.random.rand() * 0.2
            else:
                sim_mat[i, j] = np.random.rand() * 0.1
                
    sim_mat = (sim_mat + sim_mat.T) / 2.0
    true_cats = [i // 4 for i in range(16)]
    
    plot_connections_graph(test_words, sim_mat, true_categories=true_cats, threshold=0.15)
