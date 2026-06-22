from typing import Any

import numpy as np
import torch


GROUP_SCORE_MEAN_WEIGHT = 0.60
GROUP_SCORE_MIN_WEIGHT = 0.40
GROUP_SCORE_MEDIAN_WEIGHT = 0.00


def score_group_pair_values(pair_scores: Any):
    """Score quartet cohesion from the six internal pair scores.

    Connections groups are only valid when all four words fit. A 3-of-4 near miss
    can have a strong mean, so include weakest-link pressure directly.
    """
    if torch.is_tensor(pair_scores):
        mean_score = pair_scores.mean(dim=-1)
        min_score = pair_scores.min(dim=-1).values
        median_score = pair_scores.median(dim=-1).values
        score = (
            GROUP_SCORE_MEAN_WEIGHT * mean_score
            + GROUP_SCORE_MIN_WEIGHT * min_score
            + GROUP_SCORE_MEDIAN_WEIGHT * median_score
        )
        return torch.clamp(score, 0.0, 1.0)

    scores = np.asarray(pair_scores, dtype=np.float32)
    mean_score = np.mean(scores, axis=-1)
    min_score = np.min(scores, axis=-1)
    median_score = np.median(scores, axis=-1)
    score = (
        GROUP_SCORE_MEAN_WEIGHT * mean_score
        + GROUP_SCORE_MIN_WEIGHT * min_score
        + GROUP_SCORE_MEDIAN_WEIGHT * median_score
    )
    return np.clip(score, 0.0, 1.0)
