import os
import torch
import numpy as np
from src.dataset import load_preprocessed_dataset
from src.gcn import build_gcn_model, build_relation_targets
from src.features import FeatureExtractor, EDGE_FEATURE_DIM
from src.graph import ConnectionsGraph
from src.relation_archetypes import (
    NO_RELATION_IDX,
    RELATION_ARCHETYPE_TO_IDX,
    RELATION_ARCHETYPES,
)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate GCN auxiliary head on validation set")
    args = parser.parse_args()

    device = "cpu"
    data_path = "data/preprocessed_graphs.pt"
    
    model_path = os.path.join("models", "gcn_best.pt")
    
    if not os.path.exists(data_path):
        print(f"Error: Preprocessed dataset not found at {data_path}")
        return
    if not os.path.exists(model_path):
        print(f"Error: Trained model checkpoint not found at {model_path}")
        return
        
    print(f"Loading preprocessed validation set...")
    _, val_puzzles, _ = load_preprocessed_dataset(data_path)
    print(f"Loaded {len(val_puzzles)} validation puzzles.")
    
    extractor = FeatureExtractor()
    
    print(f"Loading GCN model from {model_path}...")
    in_features = val_puzzles[0]["node_features"].shape[1] if len(val_puzzles) > 0 else 775
    model = build_gcn_model(in_features=in_features, hidden_features=32, out_features=16, num_relations=EDGE_FEATURE_DIM)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    # Track statistics
    overall_correct = 0
    overall_total = 0
    by_archetype_correct = {i: 0 for i in range(len(RELATION_ARCHETYPES))}
    by_archetype_total = {i: 0 for i in range(len(RELATION_ARCHETYPES))}
    
    mrr_by_archetype = {i: [] for i in range(len(RELATION_ARCHETYPES))}
    
    with torch.no_grad():
        for puzzle in val_puzzles:
            graph = ConnectionsGraph(
                puzzle["words"], 
                device=device, 
                node_features=puzzle["node_features"], 
                edge_features=puzzle["edge_features"]
            )
            words = puzzle["words"]
            word_to_cat = puzzle["word_to_cat"]
            
            _, edge_probs, relation_logits = model(graph.node_features, graph.get_multi_relational_adjacency(), graph.edge_features)
            
            # 1. Evaluate auxiliary relation classification accuracy on positives and negatives.
            relation_true = build_relation_targets(words, word_to_cat, device)
            for i in range(16):
                for j in range(16):
                    true_idx = int(relation_true[i, j].item())
                    if true_idx == -100:
                        continue

                    logits = relation_logits[i, j]
                    pred_idx = torch.argmax(logits).item()
                    
                    is_correct = (pred_idx == true_idx)
                    overall_total += 1
                    if is_correct:
                        overall_correct += 1
                        
                    by_archetype_total[true_idx] += 1
                    if is_correct:
                        by_archetype_correct[true_idx] += 1
            
            # 2. Evaluate MRR of categories grouped by their archetype
            c, scores = model.get_candidate_scores_tensor(edge_probs)
            for cat_idx in range(4):
                indices = []
                for i, w in enumerate(words):
                    w_cat = word_to_cat[w] if isinstance(word_to_cat, dict) else word_to_cat.get(w)
                    if w_cat["cat_idx"] == cat_idx:
                        indices.append(i)
                tc = torch.tensor(sorted(indices), dtype=torch.long, device=device)
                
                # Fetch relation archetype for this category
                first_word = words[indices[0]]
                first_word_cat = word_to_cat[first_word] if isinstance(word_to_cat, dict) else word_to_cat.get(first_word)
                rtype = first_word_cat.get("relation_type", "SYNONYM")
                rtype_idx = RELATION_ARCHETYPE_TO_IDX.get(
                    rtype,
                    RELATION_ARCHETYPE_TO_IDX["SYNONYM"],
                )
                
                match_mask = (c == tc).all(dim=1)
                true_score = scores[match_mask][0]
                rank = int(torch.sum(scores >= true_score).item())
                mrr_by_archetype[rtype_idx].append(1.0 / rank)
                
    print("\n" + "="*50)
    print(" GCN AUXILIARY HEAD EVALUATION REPORT")
    print("="*50)
    
    # 1. Print Relation Classification Accuracy
    overall_acc = overall_correct / overall_total if overall_total > 0 else 0
    print(f"Overall Relation Type Accuracy (non-diagonal edges): {overall_acc:.2%} ({overall_correct}/{overall_total})")
    print("\nAccuracy per Relation Archetype:")
    for idx, name in enumerate(RELATION_ARCHETYPES):
        total = by_archetype_total[idx]
        correct = by_archetype_correct[idx]
        acc = correct / total if total > 0 else 0.0
        print(f" - {name:<20}: {acc:>6.2%} ({correct:>3}/{total:<3})")
        
    # 2. Print MRR per Archetype
    print("\nMean Reciprocal Rank (MRR) per Relation Archetype:")
    for idx, name in enumerate(RELATION_ARCHETYPES):
        if idx == NO_RELATION_IDX:
            continue
        mrrs = mrr_by_archetype[idx]
        mean_mrr = np.mean(mrrs) if mrrs else 0.0
        print(f" - {name:<20}: {mean_mrr:.4f} (count: {len(mrrs)})")
    print("="*50)

if __name__ == "__main__":
    main()
