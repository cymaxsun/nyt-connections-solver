import os
import torch
import time
from tqdm import tqdm
from typing import List, Dict, Any
from src.dataset import load_dataset, ConnectionsPuzzle
from src.features import FeatureExtractor

def preprocess_all_puzzles(
    data_path: str,
    output_path: str,
    limit: int = None
):
    """
    Precomputes and saves graph node and edge features for all puzzles in the dataset.
    This saves massive amounts of time during training by avoiding on-the-fly feature extraction.
    """
    print(f"Loading dataset from {data_path}...")
    with open(data_path, 'r') as f:
        import json
        raw_data = json.load(f)
        
    puzzles = [ConnectionsPuzzle(item) for item in raw_data]
    if limit:
        puzzles = puzzles[:limit]
        
    print(f"Total puzzles to preprocess: {len(puzzles)}")
    
    extractor = FeatureExtractor()
    # Preprocessing should be reproducible and fast: use local ConceptNet DB/cache only.
    extractor.conceptnet_offline = True
    preprocessed_data = []
    
    # Track metrics
    start_time = time.time()
    
    for idx, puzzle in enumerate(puzzles):
        print(f"[{idx+1}/{len(puzzles)}] Processing puzzle {puzzle.id}...")
        try:
            # Build node and edge feature matrices
            node_feats, edge_feats = extractor.build_graph_matrices(puzzle.words)
            
            # Save relevant data
            preprocessed_data.append({
                "id": puzzle.id,
                "date": puzzle.date,
                "words": puzzle.words,
                "categories": puzzle.categories,
                "word_to_cat": puzzle.word_to_cat,
                "adj": puzzle.adj,
                "node_features": node_feats, # numpy array
                "edge_features": edge_feats  # numpy array
            })
            
            if not extractor.conceptnet_offline:
                time.sleep(0.1)
            
        except Exception as e:
            print(f"Error processing puzzle {puzzle.id}: {e}")
            continue
            
    print(f"\nSuccessfully processed {len(preprocessed_data)} puzzles in {time.time() - start_time:.1f}s.")
    extractor._save_wordnet_cache()
    extractor._save_embedding_cache()
    
    # Save using torch.save for easy tensor loading
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    torch.save(preprocessed_data, output_path)
    print(f"Saved preprocessed dataset to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Preprocess Connections puzzles into graph features")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of puzzles to preprocess")
    args = parser.parse_args()
    
    data_file = os.path.join(os.path.dirname(__file__), "../data/connections.json")
    output_file = os.path.join(os.path.dirname(__file__), "../data/preprocessed_graphs.pt")
    
    preprocess_all_puzzles(data_file, output_file, limit=args.limit)
