from typing import Any

import numpy as np
import torch


GROUP_SCORE_SPREAD_PENALTY = 0.25


def score_group_pair_values(pair_scores: Any):
    """Score quartet cohesion from the six internal pair scores."""
    if torch.is_tensor(pair_scores):
        mean_score = pair_scores.mean(dim=-1)
        spread = pair_scores.max(dim=-1).values - pair_scores.min(dim=-1).values
        return torch.clamp(mean_score - GROUP_SCORE_SPREAD_PENALTY * spread, 0.0, 1.0)

    scores = np.asarray(pair_scores, dtype=np.float32)
    mean_score = np.mean(scores, axis=-1)
    spread = np.max(scores, axis=-1) - np.min(scores, axis=-1)
    return np.clip(mean_score - GROUP_SCORE_SPREAD_PENALTY * spread, 0.0, 1.0)
