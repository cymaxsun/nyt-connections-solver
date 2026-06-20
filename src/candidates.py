from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Set, Tuple

import numpy as np


GroupScore = Tuple[Tuple[int, ...], float]


@dataclass(frozen=True)
class PartitionGroupCandidate:
    group: Tuple[int, ...]
    group_score: float
    partition_score: float
    partition_mean_score: float
    partition_min_score: float
    group_rank: int
    remaining_mean_score: float


@dataclass(frozen=True)
class PartitionCandidate:
    groups: Tuple[PartitionGroupCandidate, ...]
    score: float


def build_partition_candidates(
    candidates: Sequence[GroupScore],
    active_mask: np.ndarray,
    rejected_groups: Set[Tuple[int, ...]] | None = None,
    top_n: int = 200,
    top_k: int = 20,
) -> List[PartitionCandidate]:
    """
    Build deterministic, bounded partitions from GCN-scored 4-word candidates.

    Each partition covers all active words exactly once. If the active word count is
    not divisible by four, no complete partition is possible and an empty list is returned.
    """
    active_indices = tuple(i for i, active in enumerate(active_mask) if active == 1.0)
    if len(active_indices) < 4 or len(active_indices) % 4 != 0:
        return []

    active_set = set(active_indices)
    rejected_groups = rejected_groups or set()
    group_scores = _active_group_scores(candidates, active_set, rejected_groups, top_n)
    if not group_scores:
        return []

    groups_by_first_word: Dict[int, List[GroupScore]] = {idx: [] for idx in active_indices}
    for group, score in group_scores:
        for idx in group:
            groups_by_first_word[idx].append((group, score))

    partitions: List[Tuple[Tuple[GroupScore, ...], float]] = []
    _search_partitions(
        uncovered=frozenset(active_indices),
        selected=(),
        groups_by_first_word=groups_by_first_word,
        partitions=partitions,
        top_k=top_k,
        state_counter=[0],
        max_states=5000,
    )

    partitions.sort(key=lambda item: (-item[1], item[0]))
    return [_make_partition_candidate(groups, score) for groups, score in partitions[:top_k]]


def partition_groups_for_actions(
    partitions: Sequence[PartitionCandidate],
    candidates: Sequence[GroupScore],
    active_mask: np.ndarray,
    rejected_groups: Set[Tuple[int, ...]] | None = None,
    top_n: int = 20,
) -> List[PartitionGroupCandidate]:
    """Return deduplicated group actions, preferring the strongest partition context."""
    best_by_group: Dict[Tuple[int, ...], PartitionGroupCandidate] = {}
    for partition in partitions:
        for group_candidate in partition.groups:
            existing = best_by_group.get(group_candidate.group)
            if existing is None or _is_better_group_context(group_candidate, existing):
                best_by_group[group_candidate.group] = group_candidate

    if not best_by_group:
        active_set = {i for i, active in enumerate(active_mask) if active == 1.0}
        rejected_groups = rejected_groups or set()
        fallback_groups = _active_group_scores(candidates, active_set, rejected_groups, top_n)
        for group, score in fallback_groups:
            best_by_group[group] = PartitionGroupCandidate(
                group=group,
                group_score=score,
                partition_score=score,
                partition_mean_score=score,
                partition_min_score=score,
                group_rank=0,
                remaining_mean_score=0.0,
            )

    return sorted(
        best_by_group.values(),
        key=lambda item: (
            -item.partition_score,
            -item.group_score,
            item.group_rank,
            item.group,
        ),
    )


def _active_group_scores(
    candidates: Sequence[GroupScore],
    active_set: Set[int],
    rejected_groups: Set[Tuple[int, ...]],
    top_n: int,
) -> List[GroupScore]:
    group_scores = []
    seen = set()
    for comb, score in candidates:
        group = tuple(sorted(comb))
        if group in seen or group in rejected_groups:
            continue
        if all(idx in active_set for idx in group):
            seen.add(group)
            group_scores.append((group, float(score)))
            if len(group_scores) == top_n:
                break
    return group_scores


def _search_partitions(
    uncovered: frozenset[int],
    selected: Tuple[GroupScore, ...],
    groups_by_first_word: Dict[int, List[GroupScore]],
    partitions: List[Tuple[Tuple[GroupScore, ...], float]],
    top_k: int,
    state_counter: List[int] | None = None,
    max_states: int = 5000,
):
    if state_counter is None:
        state_counter = [0]
    state_counter[0] += 1
    if state_counter[0] > max_states:
        return

    if not uncovered:
        ordered_groups = tuple(sorted(selected, key=lambda item: item[0]))
        score = _score_partition([score for _, score in ordered_groups])
        partitions.append((ordered_groups, score))
        partitions.sort(key=lambda item: (-item[1], item[0]))
        del partitions[top_k * 4:]
        return

    pivot = min(uncovered)
    for group, score in groups_by_first_word.get(pivot, []):
        group_set = frozenset(group)
        if not group_set.issubset(uncovered):
            continue
        _search_partitions(
            uncovered=uncovered - group_set,
            selected=selected + ((group, score),),
            groups_by_first_word=groups_by_first_word,
            partitions=partitions,
            top_k=top_k,
            state_counter=state_counter,
            max_states=max_states,
        )


def _score_partition(scores: Iterable[float]) -> float:
    score_list = list(scores)
    mean_score = sum(score_list) / len(score_list)
    return mean_score - 0.25 * (max(score_list) - min(score_list))


def _make_partition_candidate(
    groups: Tuple[GroupScore, ...],
    partition_score: float,
) -> PartitionCandidate:
    scores = [score for _, score in groups]
    mean_score = sum(scores) / len(scores)
    min_score = min(scores)
    ranked = sorted(groups, key=lambda item: (-item[1], item[0]))
    group_candidates = []

    for rank, (group, score) in enumerate(ranked):
        remaining_scores = [other_score for other_group, other_score in ranked if other_group != group]
        remaining_mean = sum(remaining_scores) / len(remaining_scores) if remaining_scores else 0.0
        group_candidates.append(
            PartitionGroupCandidate(
                group=group,
                group_score=score,
                partition_score=partition_score,
                partition_mean_score=mean_score,
                partition_min_score=min_score,
                group_rank=rank,
                remaining_mean_score=remaining_mean,
            )
        )

    return PartitionCandidate(groups=tuple(group_candidates), score=partition_score)


def _is_better_group_context(
    candidate: PartitionGroupCandidate,
    existing: PartitionGroupCandidate,
) -> bool:
    return (
        candidate.partition_score,
        candidate.group_score,
        -candidate.group_rank,
    ) > (
        existing.partition_score,
        existing.group_score,
        -existing.group_rank,
    )


def build_greedy_partition_candidates(
    candidates: Sequence[GroupScore],
    active_mask: np.ndarray,
    rejected_groups: Set[Tuple[int, ...]] | None = None,
    top_n: int | None = None,
    top_k: int = 20,
) -> List[PartitionCandidate]:
    """
    Build partitions greedily, mimicking a human's elimination strategy.

    Starting from each of the top-k candidate groups as a seed, it iteratively selects
    the most confident remaining group that fits without overlap. The final group is
    solved by elimination (remaining 4 active words).
    """
    active_indices = tuple(i for i, active in enumerate(active_mask) if active == 1.0)
    if len(active_indices) < 4 or len(active_indices) % 4 != 0:
        return []

    active_set = set(active_indices)
    rejected_groups = rejected_groups or set()
    candidate_map = {tuple(sorted(group)): float(score) for group, score in candidates}

    # Fetch active group scores up to top_n
    limit_n = top_n if top_n is not None else len(candidates)
    group_scores = _active_group_scores(candidates, active_set, rejected_groups, limit_n)
    if not group_scores:
        return []


    partitions: List[Tuple[Tuple[GroupScore, ...], float]] = []
    seen_partitions = set()

    # Generate up to top_k partitions by seeding with each of the top group candidates
    for seed_idx in range(min(len(group_scores), top_k)):
        seed_group, seed_score = group_scores[seed_idx]

        current_groups = [(seed_group, seed_score)]
        uncovered = set(active_indices) - set(seed_group)

        success = True
        while len(uncovered) >= 4:
            if len(uncovered) == 4:
                # Elimination step: last group is whatever active words remain
                leftover_group = tuple(sorted(uncovered))
                leftover_score = candidate_map.get(leftover_group, 0.0)
                current_groups.append((leftover_group, leftover_score))
                uncovered.clear()
                break

            # Find the most confident group that is a subset of uncovered
            found_next = False
            for next_group, next_score in group_scores:
                if set(next_group).issubset(uncovered):
                    current_groups.append((next_group, next_score))
                    uncovered -= set(next_group)
                    found_next = True
                    break

            if not found_next:
                success = False
                break

        if success and len(current_groups) * 4 == len(active_indices):
            ordered_groups = tuple(sorted(current_groups, key=lambda item: item[0]))
            if ordered_groups not in seen_partitions:
                seen_partitions.add(ordered_groups)
                score = _score_partition([score for _, score in ordered_groups])
                partitions.append((ordered_groups, score))

    partitions.sort(key=lambda item: (-item[1], item[0]))
    return [_make_partition_candidate(groups, score) for groups, score in partitions[:top_k]]

