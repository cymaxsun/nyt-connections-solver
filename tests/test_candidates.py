import unittest

import numpy as np
import torch

from src.candidates import (
    PartitionCandidate,
    PartitionGroupCandidate,
    build_partition_candidates,
    partition_groups_for_actions,
)
from src.rl_agent import CANDIDATE_FEATURE_DIM, DQNAgent


class PartitionCandidateTests(unittest.TestCase):
    def test_partitions_cover_active_words_once(self):
        active_mask = np.ones(16, dtype=np.float32)
        solution = [
            ((0, 1, 2, 3), 0.95),
            ((4, 5, 6, 7), 0.90),
            ((8, 9, 10, 11), 0.85),
            ((12, 13, 14, 15), 0.80),
        ]
        noise = [((0, 4, 8, 12), 0.70), ((1, 5, 9, 13), 0.65)]
        partitions = build_partition_candidates(solution + noise, active_mask, top_n=10, top_k=3)

        self.assertGreaterEqual(len(partitions), 1)
        for partition in partitions:
            flattened = [idx for group in partition.groups for idx in group.group]
            self.assertEqual(sorted(flattened), list(range(16)))
            self.assertEqual(len(flattened), len(set(flattened)))

    def test_rejected_and_inactive_groups_are_excluded(self):
        active_mask = np.ones(16, dtype=np.float32)
        active_mask[15] = 0.0
        candidates = [
            ((0, 1, 2, 3), 0.95),
            ((4, 5, 6, 7), 0.90),
            ((8, 9, 10, 11), 0.85),
            ((12, 13, 14, 15), 0.80),
            ((12, 13, 14, 0), 0.75),
        ]
        actions = partition_groups_for_actions(
            build_partition_candidates(
                candidates,
                active_mask,
                rejected_groups={(0, 1, 2, 3)},
                top_n=10,
                top_k=3,
            ),
            candidates,
            active_mask,
            rejected_groups={(0, 1, 2, 3)},
        )

        for action in actions:
            self.assertNotEqual(action.group, (0, 1, 2, 3))
            self.assertNotIn(15, action.group)

    def test_action_deduplication_keeps_best_partition_context(self):
        group = PartitionGroupCandidate((0, 1, 2, 3), 0.9, 0.7, 0.7, 0.6, 0, 0.6)
        better_group = PartitionGroupCandidate((0, 1, 2, 3), 0.9, 0.8, 0.8, 0.7, 0, 0.7)
        partitions = [
            PartitionCandidate(groups=(group,), score=0.7),
            PartitionCandidate(groups=(better_group,), score=0.8),
        ]
        actions = partition_groups_for_actions(partitions, [], np.ones(4, dtype=np.float32))

        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0].partition_score, 0.8)

    def test_candidate_features_match_partition_dimension(self):
        agent = DQNAgent(device="cpu")
        obs = np.concatenate([
            np.ones(16, dtype=np.float32),
            np.array([1.0], dtype=np.float32),
            np.zeros(16, dtype=np.float32),
        ])
        node_embeddings = torch.zeros(16, 16)
        candidates = [
            PartitionGroupCandidate((0, 1, 2, 3), 0.9, 0.8, 0.8, 0.7, 0, 0.75),
            PartitionGroupCandidate((4, 5, 6, 7), 0.8, 0.8, 0.8, 0.7, 1, 0.78),
        ]

        cand_list, feats = agent.get_candidate_features(candidates, node_embeddings, obs)

        self.assertEqual(cand_list, [(0, 1, 2, 3), (4, 5, 6, 7)])
        self.assertEqual(feats.shape, (2, CANDIDATE_FEATURE_DIM))


if __name__ == "__main__":
    unittest.main()
