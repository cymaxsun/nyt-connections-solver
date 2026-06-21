import json
import random
from typing import List, Dict, Tuple, Any

class ConnectionsPuzzle:
    def __init__(self, puzzle_data: Dict[str, Any]):
        self.id = puzzle_data["id"]
        self.date = puzzle_data.get("date", "")
        self.categories = puzzle_data["answers"]
        if len(self.categories) != 4:
            raise ValueError(f"Puzzle {self.id} must contain exactly 4 categories.")
        
        # Flatten all words
        self.words = []
        # Keep track of mapping from word to category level and category index
        self.word_to_cat = {}
        seen_words = set()
        for cat_idx, cat in enumerate(self.categories):
            members = cat["members"]
            if len(members) != 4:
                raise ValueError(
                    f"Puzzle {self.id} category {cat.get('group', cat_idx)!r} "
                    "must contain exactly 4 members."
                )
            for member in members:
                # Clean up word (strip and uppercase)
                w = member.strip().upper()
                if not w:
                    raise ValueError(f"Puzzle {self.id} contains an empty member.")
                if w in seen_words:
                    raise ValueError(f"Puzzle {self.id} contains duplicate member {w!r}.")
                seen_words.add(w)
                self.words.append(w)
                self.word_to_cat[w] = {
                    "level": cat["level"],
                    "group": cat["group"],
                    "cat_idx": cat_idx,
                    "relation_type": cat.get("relation_type", "SYNONYM_OR_NEAR")
                }
        
        # Shuffle words to avoid passing category order hints
        # Seed by puzzle ID to make it deterministic but randomized per puzzle
        rng = random.Random(self.id)
        rng.shuffle(self.words)
        
        # Ground truth adjacency matrix
        # adj[i, j] = 1 if words[i] and words[j] belong to the same category
        n = len(self.words)
        self.adj = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                w_i = self.words[i]
                w_j = self.words[j]
                if self.word_to_cat[w_i]["cat_idx"] == self.word_to_cat[w_j]["cat_idx"]:
                    self.adj[i][j] = 1

    def __repr__(self):
        return f"<Puzzle {self.id} ({self.date}): {', '.join(self.words[:4])}...>"

def load_dataset(filepath: str, train_ratio: float = 0.8, val_ratio: float = 0.1, seed: int = 42) -> Tuple[List[ConnectionsPuzzle], List[ConnectionsPuzzle], List[ConnectionsPuzzle]]:
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    puzzles = [ConnectionsPuzzle(item) for item in data]
    
    # Shuffle and split
    rng = random.Random(seed)
    rng.shuffle(puzzles)
    
    total = len(puzzles)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)
    
    train_puzzles = puzzles[:train_end]
    val_puzzles = puzzles[train_end:val_end]
    test_puzzles = puzzles[val_end:]
    
    return train_puzzles, val_puzzles, test_puzzles

def load_preprocessed_dataset(filepath: str, train_ratio: float = 0.8, val_ratio: float = 0.1, seed: int = 42) -> Tuple[list, list, list]:
    import torch
    data = torch.load(filepath, weights_only=False)
    
    # Shuffle and split
    rng = random.Random(seed)
    rng.shuffle(data)
    
    total = len(data)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)
    
    train_puzzles = data[:train_end]
    val_puzzles = data[train_end:val_end]
    test_puzzles = data[val_end:]
    
    return train_puzzles, val_puzzles, test_puzzles


if __name__ == "__main__":
    import os
    # Quick sanity check
    data_path = os.path.join(os.path.dirname(__file__), "../data/connections.json")
    if os.path.exists(data_path):
        train, val, test = load_dataset(data_path)
        print(f"Loaded {len(train)} train, {len(val)} val, {len(test)} test puzzles.")
        if len(train) > 0:
            print("Sample puzzle:", train[0])
            print("Words:", train[0].words)
            print("Adjacency sum:", sum(sum(row) for row in train[0].adj))
