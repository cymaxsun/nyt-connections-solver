import argparse
import itertools
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Sequence, Tuple

import numpy as np
import torch

from src.candidate_scoring import score_group_pair_values
from src.candidates import PartitionCandidate, build_partition_candidates
from src.dataset import load_preprocessed_dataset
from src.features import (
    CLUE_SIMILARITY_DIM,
    CN_DERIVED_FROM_DIM,
    CN_DISTINCT_FROM_DIM,
    CN_ETYMOLOGICAL_DIM,
    CN_HAS_CONTEXT_DIM,
    CN_IS_A_DIM,
    CN_RELATED_TO_DIM,
    CN_RESIDUAL_BACKWARD_DIM,
    CN_RESIDUAL_FORWARD_DIM,
    CN_SYNONYM_DIM,
    COMPOUND_FRAGMENT_SHARED_DIM,
    COMPOUND_FRAGMENT_SHARED_THRESHOLD,
    EDGE_FEATURE_DIM,
    IS_ANAGRAM_DIM,
    IS_SUBSTRING_DIM,
    SENTENCE_SIMILARITY_DIM,
    SHARED_PREFIX_DIM,
    SHARED_SUFFIX_DIM,
    WORDNET_PATH_SIM_DIM,
    WORDNET_SHARED_HYPERNYM_DIM,
    PHONEME_EDIT_DISTANCE_DIM,
    PHONEME_EDIT_DISTANCE_THRESHOLD,
    RHYME_MATCH_DIM,
    SOUNDEX_MATCH_DIM,
    METAPHONE_MATCH_DIM,
    PHONEME_OVERLAP_DIM,
    PHONEME_OVERLAP_THRESHOLD,
)
from src.graph import (
    LENGTH_SIMILARITY_DIM,
    LENGTH_SIMILARITY_THRESHOLD,
    LEVENSHTEIN_DISTANCE_DIM,
    LEVENSHTEIN_SIMILARITY_THRESHOLD,
)
from src.visualize import plot_connections_graph


RawCandidate = Tuple[Tuple[int, ...], float]


RAW_FEATURE_WEIGHTS: Dict[int, float] = {
    WORDNET_PATH_SIM_DIM: 1.0,
    WORDNET_SHARED_HYPERNYM_DIM: 0.75,
    CN_IS_A_DIM: 1.25,
    CN_SYNONYM_DIM: 1.25,
    CN_RELATED_TO_DIM: 0.75,
    CN_HAS_CONTEXT_DIM: 1.25,
    CN_DERIVED_FROM_DIM: 1.0,
    CN_ETYMOLOGICAL_DIM: 0.25,
    CN_DISTINCT_FROM_DIM: 0.75,
    CN_RESIDUAL_FORWARD_DIM: 1.0,
    CN_RESIDUAL_BACKWARD_DIM: 1.0,
    CLUE_SIMILARITY_DIM: 1.25,
    IS_ANAGRAM_DIM: 1.5,
    SHARED_PREFIX_DIM: 1.0,
    SHARED_SUFFIX_DIM: 1.0,
    IS_SUBSTRING_DIM: 1.0,
    LENGTH_SIMILARITY_DIM: 0.25,
    SENTENCE_SIMILARITY_DIM: 1.25,
    LEVENSHTEIN_DISTANCE_DIM: 0.75,
    PHONEME_EDIT_DISTANCE_DIM: 0.25,
    RHYME_MATCH_DIM: 0.25,
    SOUNDEX_MATCH_DIM: 0.10,
    METAPHONE_MATCH_DIM: 0.15,
    PHONEME_OVERLAP_DIM: 0.10,
    COMPOUND_FRAGMENT_SHARED_DIM: 1.0,
}


@dataclass(frozen=True)
class RawCandidateMetrics:
    puzzles: int
    mrr: float
    group_recall_at_k: Dict[int, float]
    avg_best_true_group_rank: float
    partitions_found: int
    avg_exact_groups_in_best_partition: float
    perfect_best_partitions: int


def raw_pair_scores(edge_features: np.ndarray) -> np.ndarray:
    """Collapse preprocessed edge features into one symmetric raw pair score matrix."""
    if edge_features.shape[-1] != EDGE_FEATURE_DIM:
        raise ValueError(
            f"Expected {EDGE_FEATURE_DIM} edge features, got {edge_features.shape[-1]}"
        )

    features = np.nan_to_num(edge_features.astype(np.float32), nan=0.0, posinf=1.0, neginf=0.0)
    channels = []
    weights = []

    for dim, weight in RAW_FEATURE_WEIGHTS.items():
        channel = features[:, :, dim].copy()
        if dim == WORDNET_PATH_SIM_DIM:
            channel = np.where(channel >= 0.15, channel, 0.0)
        elif dim == CLUE_SIMILARITY_DIM:
            channel = np.where(channel >= 0.10, channel, 0.0)
        elif dim == LENGTH_SIMILARITY_DIM:
            channel = 1.0 - channel
            channel = np.where(channel >= LENGTH_SIMILARITY_THRESHOLD, channel, 0.0)
        elif dim == SENTENCE_SIMILARITY_DIM:
            channel = np.where(channel >= 0.25, channel, 0.0)
        elif dim == LEVENSHTEIN_DISTANCE_DIM:
            channel = 1.0 - channel
            channel = np.where(channel >= LEVENSHTEIN_SIMILARITY_THRESHOLD, channel, 0.0)
        elif dim == PHONEME_EDIT_DISTANCE_DIM:
            channel = 1.0 - channel
            channel = np.where(channel >= PHONEME_EDIT_DISTANCE_THRESHOLD, channel, 0.0)
        elif dim == PHONEME_OVERLAP_DIM:
            channel = np.where(channel >= PHONEME_OVERLAP_THRESHOLD, channel, 0.0)
        elif dim == COMPOUND_FRAGMENT_SHARED_DIM:
            channel = np.where(channel >= COMPOUND_FRAGMENT_SHARED_THRESHOLD, channel, 0.0)

        channels.append(np.clip(channel, 0.0, 1.0) * weight)
        weights.append(weight)

    score = np.sum(channels, axis=0) / sum(weights)
    score = (score + score.T) / 2.0
    np.fill_diagonal(score, 0.0)
    return score.astype(np.float32)


def raw_candidate_groups(pair_scores: np.ndarray) -> List[RawCandidate]:
    """Score all 4-word groups by penalized cohesion over the six internal edges."""
    candidates = []
    for group in itertools.combinations(range(pair_scores.shape[0]), 4):
        pairs = itertools.combinations(group, 2)
        score = float(score_group_pair_values([pair_scores[i, j] for i, j in pairs]))
        candidates.append((group, score))
    candidates.sort(key=lambda item: (-item[1], item[0]))
    return candidates


def evaluate_raw_candidates(
    puzzles: Sequence[dict],
    top_ks: Sequence[int] = (5, 10, 20, 50),
    partition_top_n: int = 400,
    partition_top_k: int = 20,
) -> RawCandidateMetrics:
    reciprocal_ranks = []
    best_true_ranks = []
    recall_hits = {k: 0 for k in top_ks}
    total_true_groups = 0
    partitions_found = 0
    exact_groups_in_best_partition = []
    perfect_best_partitions = 0

    for puzzle in puzzles:
        pair_scores = raw_pair_scores(puzzle["edge_features"])
        candidates = raw_candidate_groups(pair_scores)
        candidate_ranks = {tuple(group): rank for rank, (group, _) in enumerate(candidates, start=1)}
        true_groups = _true_groups(puzzle)

        ranks = [candidate_ranks[group] for group in true_groups]
        reciprocal_ranks.extend(1.0 / rank for rank in ranks)
        best_true_ranks.append(min(ranks))
        total_true_groups += len(true_groups)
        for k in top_ks:
            recall_hits[k] += sum(1 for rank in ranks if rank <= k)

        partitions = build_partition_candidates(
            candidates,
            np.ones(16, dtype=np.float32),
            top_n=partition_top_n,
            top_k=partition_top_k,
        )
        if partitions:
            partitions_found += 1
            exact_count = _exact_groups_in_partition(partitions[0], true_groups)
            exact_groups_in_best_partition.append(exact_count)
            if exact_count == 4:
                perfect_best_partitions += 1
        else:
            exact_groups_in_best_partition.append(0)

    return RawCandidateMetrics(
        puzzles=len(puzzles),
        mrr=float(np.mean(reciprocal_ranks)) if reciprocal_ranks else 0.0,
        group_recall_at_k={
            k: recall_hits[k] / total_true_groups if total_true_groups else 0.0
            for k in top_ks
        },
        avg_best_true_group_rank=float(np.mean(best_true_ranks)) if best_true_ranks else 0.0,
        partitions_found=partitions_found,
        avg_exact_groups_in_best_partition=(
            float(np.mean(exact_groups_in_best_partition))
            if exact_groups_in_best_partition
            else 0.0
        ),
        perfect_best_partitions=perfect_best_partitions,
    )


def write_raw_candidate_artifacts(
    puzzles: Sequence[dict],
    metrics: RawCandidateMetrics,
    output_dir: str,
    top_groups: int = 12,
    max_visuals: int = 5,
):
    os.makedirs(output_dir, exist_ok=True)
    lines = [
        "# Raw Preprocessed Graph Candidate Evaluation",
        "",
        f"Evaluated puzzles: {metrics.puzzles}",
        f"MRR over true groups: {metrics.mrr:.4f}",
        f"Average best true-group rank per puzzle: {metrics.avg_best_true_group_rank:.2f}",
        f"Partitions found: {metrics.partitions_found}/{metrics.puzzles}",
        (
            "Average exact groups in best partition: "
            f"{metrics.avg_exact_groups_in_best_partition:.2f}/4"
        ),
        f"Perfect best partitions: {metrics.perfect_best_partitions}/{metrics.puzzles}",
        "",
        "## Recall",
    ]
    for k, value in metrics.group_recall_at_k.items():
        lines.append(f"- Recall@{k}: {value:.2%}")

    for idx, puzzle in enumerate(puzzles):
        pair_scores = raw_pair_scores(puzzle["edge_features"])
        candidates = raw_candidate_groups(pair_scores)
        true_groups = _true_groups(puzzle)
        partitions = build_partition_candidates(
            candidates,
            np.ones(16, dtype=np.float32),
            top_n=400,
            top_k=5,
        )

        words = puzzle["words"]
        lines.extend([
            "",
            f"## Puzzle {idx} (ID: {puzzle['id']})",
            f"Words: {', '.join(words)}",
            "",
            "### Top Raw Candidate Groups",
        ])
        for rank, (group, score) in enumerate(candidates[:top_groups], start=1):
            status = "EXACT" if tuple(sorted(group)) in true_groups else _max_overlap(group, true_groups)
            group_words = ", ".join(words[i] for i in group)
            lines.append(f"{rank}. **{score:.4f}** | {group_words} | {status}")

        lines.append("")
        lines.append("### Top Raw Partitions")
        if not partitions:
            lines.append("_No complete partitions found from the bounded search._")
        for rank, partition in enumerate(partitions[:3], start=1):
            exact = _exact_groups_in_partition(partition, true_groups)
            lines.append(f"{rank}. **{partition.score:.4f}** | exact groups: {exact}/4")
            for group_candidate in partition.groups:
                group_words = ", ".join(words[i] for i in group_candidate.group)
                lines.append(f"   - {group_candidate.group_score:.4f} | {group_words}")

        if idx < max_visuals:
            true_cats = [puzzle["word_to_cat"][word]["cat_idx"] for word in words]
            plot_connections_graph(
                words,
                pair_scores,
                true_categories=true_cats,
                threshold=0.15,
                filepath=os.path.join(output_dir, f"raw_puzzle_{puzzle['id']}.png"),
                title=f"Raw Graph Candidate Scores - Puzzle {puzzle['id']}",
            )

    summary_path = os.path.join(output_dir, "raw_candidates_summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    metrics_path = os.path.join(output_dir, "raw_candidates_metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(_metrics_to_dict(metrics), f, indent=2)

    return summary_path, metrics_path


def main():
    parser = argparse.ArgumentParser(description="Evaluate candidate groups from raw preprocessed graph features")
    parser.add_argument("--data", default="data/preprocessed_graphs.pt", help="Preprocessed graph .pt file")
    parser.add_argument("--split", choices=("train", "val", "test", "all"), default="val")
    parser.add_argument("--limit", type=int, default=None, help="Limit puzzles from the selected split")
    parser.add_argument("--output-dir", default="visualizations/raw_candidates")
    parser.add_argument("--top-k", type=int, nargs="+", default=[5, 10, 20, 50])
    args = parser.parse_args()

    train_puzzles, val_puzzles, test_puzzles = load_preprocessed_dataset(args.data)
    split_map = {
        "train": train_puzzles,
        "val": val_puzzles,
        "test": test_puzzles,
        "all": train_puzzles + val_puzzles + test_puzzles,
    }
    puzzles = split_map[args.split]
    if args.limit is not None:
        puzzles = puzzles[:args.limit]

    metrics = evaluate_raw_candidates(puzzles, top_ks=args.top_k)
    summary_path, metrics_path = write_raw_candidate_artifacts(puzzles, metrics, args.output_dir)

    print(f"Evaluated {metrics.puzzles} puzzles from split '{args.split}'.")
    print(f"MRR: {metrics.mrr:.4f}")
    for k, value in metrics.group_recall_at_k.items():
        print(f"Recall@{k}: {value:.2%}")
    print(f"Best partition exact groups: {metrics.avg_exact_groups_in_best_partition:.2f}/4 avg")
    print(f"Summary: {summary_path}")
    print(f"Metrics: {metrics_path}")


def _true_groups(puzzle: dict) -> Tuple[Tuple[int, ...], ...]:
    groups = []
    for cat_idx in range(4):
        indices = [
            idx for idx, word in enumerate(puzzle["words"])
            if puzzle["word_to_cat"][word]["cat_idx"] == cat_idx
        ]
        groups.append(tuple(sorted(indices)))
    return tuple(groups)


def _exact_groups_in_partition(
    partition: PartitionCandidate,
    true_groups: Tuple[Tuple[int, ...], ...],
) -> int:
    true_group_set = set(true_groups)
    return sum(1 for group in partition.groups if tuple(sorted(group.group)) in true_group_set)


def _max_overlap(group: Tuple[int, ...], true_groups: Tuple[Tuple[int, ...], ...]) -> str:
    group_set = set(group)
    overlap = max(len(group_set.intersection(true_group)) for true_group in true_groups)
    return f"max overlap {overlap}/4"


def _metrics_to_dict(metrics: RawCandidateMetrics) -> Dict[str, Any]:
    return {
        "puzzles": metrics.puzzles,
        "mrr": metrics.mrr,
        "group_recall_at_k": {
            str(k): value for k, value in metrics.group_recall_at_k.items()
        },
        "avg_best_true_group_rank": metrics.avg_best_true_group_rank,
        "partitions_found": metrics.partitions_found,
        "avg_exact_groups_in_best_partition": metrics.avg_exact_groups_in_best_partition,
        "perfect_best_partitions": metrics.perfect_best_partitions,
    }


if __name__ == "__main__":
    main()
