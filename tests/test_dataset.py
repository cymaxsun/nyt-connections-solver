import json
import unittest
from collections import Counter

from src.dataset import ConnectionsPuzzle


class ConnectionsDatasetIntegrityTests(unittest.TestCase):
    def test_dataset_boards_have_four_non_empty_unique_groups(self):
        with open("data/connections.json", "r", encoding="utf-8") as f:
            puzzles = json.load(f)

        self.assertGreater(len(puzzles), 0)

        for puzzle in puzzles:
            puzzle_id = puzzle.get("id")
            answers = puzzle.get("answers")
            self.assertEqual(len(answers), 4, f"Puzzle {puzzle_id} must have 4 groups")

            board_words = []
            for answer in answers:
                members = answer.get("members")
                self.assertEqual(
                    len(members),
                    4,
                    f"Puzzle {puzzle_id} group {answer.get('group')} must have 4 members",
                )
                for member in members:
                    word = member.strip().upper()
                    self.assertTrue(word, f"Puzzle {puzzle_id} has an empty member")
                    board_words.append(word)

            counts = Counter(board_words)
            duplicates = sorted(word for word, count in counts.items() if count > 1)
            self.assertEqual(
                duplicates,
                [],
                f"Puzzle {puzzle_id} has duplicate board words: {duplicates}",
            )
            self.assertEqual(len(board_words), 16, f"Puzzle {puzzle_id} must have 16 words")

    def test_connections_puzzle_rejects_empty_and_duplicate_members(self):
        valid_answers = [
            {"level": 0, "group": "A", "members": ["A1", "A2", "A3", "A4"]},
            {"level": 1, "group": "B", "members": ["B1", "B2", "B3", "B4"]},
            {"level": 2, "group": "C", "members": ["C1", "C2", "C3", "C4"]},
            {"level": 3, "group": "D", "members": ["D1", "D2", "D3", "D4"]},
        ]

        empty_member = {"id": 1, "answers": [dict(answer) for answer in valid_answers]}
        empty_member["answers"][0]["members"] = ["", "A2", "A3", "A4"]
        with self.assertRaisesRegex(ValueError, "empty member"):
            ConnectionsPuzzle(empty_member)

        duplicate_member = {"id": 2, "answers": [dict(answer) for answer in valid_answers]}
        duplicate_member["answers"][1]["members"] = ["A1", "B2", "B3", "B4"]
        with self.assertRaisesRegex(ValueError, "duplicate member"):
            ConnectionsPuzzle(duplicate_member)


if __name__ == "__main__":
    unittest.main()
