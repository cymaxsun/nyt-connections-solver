import json
import os
import sys
import tempfile
import unittest
from unittest import mock

from src.label_archetypes_deepseek import (
    DEEPSEEK_MODEL,
    label_dataset,
    main,
)


def sample_dataset():
    return [{
        "id": 1,
        "date": "2023-06-12",
        "answers": [
            {"level": 0, "group": "WET WEATHER", "members": ["HAIL", "RAIN", "SLEET", "SNOW"], "relation_type": "SYNONYM"},
            {"level": 1, "group": "NBA TEAMS", "members": ["BUCKS", "HEAT", "JAZZ", "NETS"], "relation_type": "TRIVIA_ENCYCLOPEDIC"},
            {"level": 2, "group": "KEYBOARD KEYS", "members": ["OPTION", "RETURN", "SHIFT", "TAB"], "relation_type": "TRIVIA_ENCYCLOPEDIC"},
            {"level": 3, "group": "PALINDROMES", "members": ["KAYAK", "LEVEL", "MOM", "RACECAR"], "relation_type": "MORPHOLOGY"},
        ],
    }]


class FakeResponse:
    def __init__(self, payload, raw_content=None):
        self.payload = payload
        self.raw_content = raw_content

    def raise_for_status(self):
        return None

    def json(self):
        return {
            "choices": [{
                "message": {
                    "content": self.raw_content if self.raw_content is not None else json.dumps(self.payload),
                },
            }],
        }


class FakeSession:
    def __init__(self, payload=None, raw_content=None):
        self.payload = payload
        self.raw_content = raw_content
        self.requests = []

    def post(self, *args, **kwargs):
        self.requests.append((args, kwargs))
        return FakeResponse(self.payload, self.raw_content)


class FailingSession:
    def post(self, *args, **kwargs):
        raise AssertionError("API should not be called")


class LabelArchetypesDeepSeekTests(unittest.TestCase):
    def write_input(self, temp_dir):
        input_path = os.path.join(temp_dir, "connections.json")
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(sample_dataset(), f)
        return input_path

    def read_output(self, output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def test_high_confidence_labels_update_relation_type(self):
        payload = {
            "categories": [
                {"category_index": 0, "relation_type": "SYNONYM_OR_NEAR", "confidence": 0.91, "rationale": "near synonyms"},
                {"category_index": 1, "relation_type": "NAMED_ENTITY_SET", "confidence": 0.95, "rationale": "team names"},
                {"category_index": 2, "relation_type": "SEMANTIC_SET", "confidence": 0.90, "rationale": "keyboard keys"},
                {"category_index": 3, "relation_type": "WORD_FORM", "confidence": 0.93, "rationale": "palindromes"},
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)
            review_path = os.path.join(temp_dir, "review.md")

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=review_path,
                session=FakeSession(payload),
                workers=1,
                checkpoint_path=os.path.join(temp_dir, "checkpoint.jsonl"),
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 4)
            self.assertEqual(needs_review, 0)
            self.assertEqual(data[0]["answers"][0]["relation_type"], "SYNONYM_OR_NEAR")
            self.assertEqual(data[0]["answers"][1]["relation_label_model"], DEEPSEEK_MODEL)

    def test_low_confidence_label_preserves_old_label_and_marks_review(self):
        payload = {
            "categories": [
                {"category_index": 0, "relation_type": "SYNONYM_OR_NEAR", "confidence": 0.50, "rationale": "uncertain"},
                {"category_index": 1, "relation_type": "NAMED_ENTITY_SET", "confidence": 0.95, "rationale": "team names"},
                {"category_index": 2, "relation_type": "SEMANTIC_SET", "confidence": 0.90, "rationale": "keyboard keys"},
                {"category_index": 3, "relation_type": "WORD_FORM", "confidence": 0.93, "rationale": "palindromes"},
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)
            review_path = os.path.join(temp_dir, "review.md")

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=review_path,
                session=FakeSession(payload),
                workers=1,
                checkpoint_path=os.path.join(temp_dir, "checkpoint.jsonl"),
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 3)
            self.assertEqual(needs_review, 1)
            self.assertEqual(data[0]["answers"][0]["relation_type"], "SYNONYM")
            self.assertEqual(data[0]["answers"][0]["relation_label_status"], "needs_review")
            with open(review_path, "r", encoding="utf-8") as f:
                self.assertIn("WET WEATHER", f.read())

    def test_top_level_list_response_updates_relation_type(self):
        payload = [
            {"category_index": 0, "relation_type": "SYNONYM_OR_NEAR", "confidence": 0.91, "rationale": "near synonyms"},
            {"category_index": 1, "relation_type": "NAMED_ENTITY_SET", "confidence": 0.95, "rationale": "team names"},
            {"category_index": 2, "relation_type": "SEMANTIC_SET", "confidence": 0.90, "rationale": "keyboard keys"},
            {"category_index": 3, "relation_type": "WORD_FORM", "confidence": 0.93, "rationale": "palindromes"},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=os.path.join(temp_dir, "review.md"),
                session=FakeSession(payload),
                workers=1,
                checkpoint_path=os.path.join(temp_dir, "checkpoint.jsonl"),
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 4)
            self.assertEqual(needs_review, 0)
            self.assertEqual(data[0]["answers"][1]["relation_type"], "NAMED_ENTITY_SET")

    def test_unknown_label_preserves_old_label_and_marks_review(self):
        payload = {
            "categories": [
                {"category_index": 0, "relation_type": "NOT_A_LABEL", "confidence": 0.99, "rationale": "bad label"},
                {"category_index": 1, "relation_type": "NAMED_ENTITY_SET", "confidence": 0.95, "rationale": "team names"},
                {"category_index": 2, "relation_type": "SEMANTIC_SET", "confidence": 0.90, "rationale": "keyboard keys"},
                {"category_index": 3, "relation_type": "WORD_FORM", "confidence": 0.93, "rationale": "palindromes"},
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=os.path.join(temp_dir, "review.md"),
                session=FakeSession(payload),
                workers=1,
                checkpoint_path=os.path.join(temp_dir, "checkpoint.jsonl"),
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 3)
            self.assertEqual(needs_review, 1)
            self.assertEqual(data[0]["answers"][0]["relation_type"], "SYNONYM")
            self.assertEqual(data[0]["answers"][0]["relation_label_rationale"], "Unknown relation_type")

    def test_invalid_json_preserves_all_old_labels_and_marks_review(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=os.path.join(temp_dir, "review.md"),
                session=FakeSession(raw_content="{not json"),
                workers=1,
                checkpoint_path=os.path.join(temp_dir, "checkpoint.jsonl"),
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 0)
            self.assertEqual(needs_review, 4)
            self.assertEqual(data[0]["answers"][0]["relation_type"], "SYNONYM")
            self.assertEqual(data[0]["answers"][3]["relation_label_status"], "needs_review")

    def test_checkpointed_puzzle_skips_api_call_on_resume(self):
        checkpoint_record = {
            "puzzle_id": 1,
            "label_response": {
                "categories": [
                    {"category_index": 0, "relation_type": "SYNONYM_OR_NEAR", "confidence": 0.91, "rationale": "near synonyms"},
                    {"category_index": 1, "relation_type": "NAMED_ENTITY_SET", "confidence": 0.95, "rationale": "team names"},
                    {"category_index": 2, "relation_type": "SEMANTIC_SET", "confidence": 0.90, "rationale": "keyboard keys"},
                    {"category_index": 3, "relation_type": "WORD_FORM", "confidence": 0.93, "rationale": "palindromes"},
                ],
            },
            "error": None,
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)
            checkpoint_path = os.path.join(temp_dir, "checkpoint.jsonl")
            with open(checkpoint_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(checkpoint_record) + "\n")

            accepted, needs_review = label_dataset(
                input_path,
                input_path,
                api_key="test-key",
                review_path=os.path.join(temp_dir, "review.md"),
                session=FailingSession(),
                workers=4,
                checkpoint_path=checkpoint_path,
            )

            data = self.read_output(input_path)
            self.assertEqual(accepted, 4)
            self.assertEqual(needs_review, 0)
            self.assertEqual(data[0]["answers"][3]["relation_type"], "WORD_FORM")

    def test_missing_deepseek_key_exits_without_changing_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = self.write_input(temp_dir)
            with open(input_path, "r", encoding="utf-8") as f:
                before = f.read()
            with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(
                sys,
                "argv",
                ["label_archetypes_deepseek.py", "--input", input_path, "--output", input_path],
            ), mock.patch("src.label_archetypes_deepseek.load_env_file", return_value={}):
                self.assertEqual(main(), 1)
            with open(input_path, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), before)


if __name__ == "__main__":
    unittest.main()
