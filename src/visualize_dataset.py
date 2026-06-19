import os
import torch
import numpy as np
from typing import List
from src.dataset import load_dataset, ConnectionsPuzzle
from src.features import FeatureExtractor
from src.graph import ConnectionsGraph
from src.visualize import plot_connections_graph

def visualize_all_raw_puzzles(data_path: str, output_dir: str = "visualizations/raw", limit: int = None):
    """
    Generates and saves the raw feature graph visualization for all puzzles in the dataset.
    This shows how well-clustered the words are based purely on lexical/semantic/wordplay similarity.
    """
    print(f"Loading puzzles from {data_path}...")
    train_puzzles, val_puzzles, test_puzzles = load_dataset(data_path)
    all_puzzles = train_puzzles + val_puzzles + test_puzzles
    
    if limit:
        all_puzzles = all_puzzles[:limit]
        
    print(f"Generating raw feature graph visualizations for {len(all_puzzles)} puzzles...")
    os.makedirs(output_dir, exist_ok=True)
    
    extractor = FeatureExtractor()
    
    for idx, puzzle in enumerate(all_puzzles):
        print(f"[{idx+1}/{len(all_puzzles)}] Visualizing puzzle {puzzle.id}...")
        try:
            # Build graph features
            node_feats, edge_feats = extractor.build_graph_matrices(puzzle.words)
            
            # Combine raw similarity dimensions: WordNet path sim (0) + ConceptNet fwd (2) + Clue TF-IDF sim (4)
            # Normalize to [0, 1] range
            raw_sim = (edge_feats[:, :, 0] + edge_feats[:, :, 2] + edge_feats[:, :, 4]) / 3.0
            
            # Make symmetric
            raw_sim = (raw_sim + raw_sim.T) / 2.0
            
            # True categories
            true_cats = [puzzle.word_to_cat[w]["cat_idx"] for w in puzzle.words]
            
            # Plot
            filepath = os.path.join(output_dir, f"puzzle_{puzzle.id}.png")
            plot_connections_graph(
                puzzle.words,
                raw_sim,
                true_categories=true_cats,
                threshold=0.12, # lower threshold for raw similarity
                filepath=filepath,
                title=f"Raw Feature Graph - Puzzle {puzzle.id} ({puzzle.date})"
            )
        except Exception as e:
            print(f"Error visualising puzzle {puzzle.id}: {e}")
            
    print(f"Finished. All raw visualizations saved to: {output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Visualize raw graphs for dataset puzzles")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of puzzles to visualize")
    args = parser.parse_args()
    
    data_file = os.path.join(os.path.dirname(__file__), "../data/connections.json")
    visualize_all_raw_puzzles(data_file, limit=args.limit)
