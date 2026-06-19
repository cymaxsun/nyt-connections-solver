import gymnasium as gym
from gymnasium import spaces
import numpy as np
from typing import List, Dict, Tuple, Set, Any, Optional
from src.dataset import ConnectionsPuzzle

class ConnectionsEnv(gym.Env):
    """
    Custom Gymnasium Environment for the Connections game.
    """
    def __init__(self, puzzle: Any):
        super().__init__()
        self.puzzle = puzzle
        if isinstance(puzzle, dict):
            self.words = puzzle["words"]
            self.word_to_cat = puzzle["word_to_cat"]
            self.categories = puzzle["categories"]
        else:
            self.words = puzzle.words
            self.word_to_cat = puzzle.word_to_cat
            self.categories = puzzle.categories
        
        # 16 nodes, each word can be active (1) or solved (0)
        self.active_mask = np.ones(16, dtype=np.float32)
        self.mistakes_left = 4
        self.solved_count = 0
        
        # History tracks how many times each word has been submitted in a wrong guess
        self.submission_history = np.zeros(16, dtype=np.float32)
        
        # Define action space: we submit 4 indices of words (0-15)
        # To match gym standards, we define spaces, but step will accept a tuple of 4 indices.
        self.action_space = spaces.Tuple((
            spaces.Discrete(16),
            spaces.Discrete(16),
            spaces.Discrete(16),
            spaces.Discrete(16)
        ))
        
        # Observation space:
        # 16-dim active mask
        # 1-dim mistakes left (normalized: mistakes / 4.0)
        # 16-dim submission history
        self.observation_space = spaces.Box(
            low=0.0,
            high=10.0,
            shape=(16 + 1 + 16,),
            dtype=np.float32
        )

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None) -> Tuple[np.ndarray, dict]:
        super().reset(seed=seed)
        self.active_mask = np.ones(16, dtype=np.float32)
        self.mistakes_left = 4
        self.solved_count = 0
        self.submission_history = np.zeros(16, dtype=np.float32)
        
        obs = self._get_obs()
        info = {
            "words": self.words,
            "mistakes_left": self.mistakes_left,
            "solved_groups": 0
        }
        return obs, info

    def _get_obs(self) -> np.ndarray:
        # Concatenate active mask, mistakes normalized, and submission history
        mistakes_norm = np.array([self.mistakes_left / 4.0], dtype=np.float32)
        return np.concatenate([self.active_mask, mistakes_norm, self.submission_history])

    def step(self, action: Tuple[int, int, int, int]) -> Tuple[np.ndarray, float, bool, bool, dict]:
        """
        Executes one step in the environment.
        Args:
            action: Tuple of 4 distinct indices in [0, 15]
        """
        assert len(action) == 4, "Action must contain exactly 4 indices."
        assert len(set(action)) == 4, "Action indices must be unique."
        
        # Check if any word is already solved
        for idx in action:
            if self.active_mask[idx] == 0.0:
                # Submitting a solved word is invalid, small penalty, no change in state
                return self._get_obs(), -0.1, False, False, {"error": "Submitting already solved words", "mistakes_left": self.mistakes_left}
                
        # Check if the guess is correct
        guess_words = [self.words[i] for i in action]
        guess_cats = [self.word_to_cat[w]["cat_idx"] for w in guess_words]
        
        # A guess is correct if all 4 words belong to the same category group
        is_correct = len(set(guess_cats)) == 1
        
        terminated = False
        reward = 0.0
        info = {}
        
        if is_correct:
            # Mark words as solved
            for idx in action:
                self.active_mask[idx] = 0.0
            self.solved_count += 1
            reward = 1.0
            info["feedback"] = "Correct!"
            
            # Check win condition (all 4 groups solved)
            if self.solved_count == 4:
                terminated = True
                info["win"] = True
        else:
            # Incorrect guess. Check if "One Away" (3 words from same category)
            cat_counts = {}
            for cat in guess_cats:
                cat_counts[cat] = cat_counts.get(cat, 0) + 1
            max_overlap = max(cat_counts.values())
            
            # Increment submission history for these words since they were in a wrong guess
            for idx in action:
                self.submission_history[idx] += 1.0
                
            self.mistakes_left -= 1
            
            if max_overlap == 3:
                reward = 0.1
                info["feedback"] = "One Away"
            else:
                reward = -0.2
                info["feedback"] = "Incorrect"
                
            # Check loss condition
            if self.mistakes_left <= 0:
                terminated = True
                reward = -1.0
                info["win"] = False
                
        info["mistakes_left"] = self.mistakes_left
        info["solved_groups"] = self.solved_count
        
        return self._get_obs(), reward, terminated, False, info
