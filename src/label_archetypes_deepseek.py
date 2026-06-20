import argparse
import concurrent.futures
import json
import os
import tempfile
from typing import Any, Dict, List, Optional, Tuple

import requests

from src.relation_archetypes import LEGACY_RELATION_ARCHETYPE_ALIASES, RELATION_ARCHETYPES

DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-v4-flash"
ACCEPT_CONFIDENCE_THRESHOLD = 0.75
VALID_POSITIVE_ARCHETYPES = set(RELATION_ARCHETYPES[1:])
VALID_DATASET_ARCHETYPES = VALID_POSITIVE_ARCHETYPES | set(LEGACY_RELATION_ARCHETYPE_ALIASES)
DEFAULT_CHECKPOINT_PATH = "data/archetype_labeling_checkpoint.jsonl"


SYSTEM_PROMPT = """You label NYT Connections answer categories by solving mechanism.
Return only valid json. Choose exactly one relation_type for each category.

Allowed relation_type values:
- SEMANTIC_SET: category members share a general topic or class.
- SYNONYM_OR_NEAR: category members are synonyms or near-synonyms.
- NAMED_ENTITY_SET: category members are names of specific entities, brands, people, places, works, teams, or characters.
- WORD_FORM: category members share surface word form such as prefixes, suffixes, substrings, palindromes, initials, or letter patterns.
- SOUND_OR_SPELLING: category members depend on sound, pronunciation, homophones, rhymes, or spelling quirks.
- WORDPLAY_TRANSFORM: category members require adding, removing, changing, hiding, or reinterpreting letters/words.
- FILL_IN_THE_BLANK: category members complete the same blank or template.
- COMMON_PHRASE: category members are tied by idioms, collocations, words before/after another word, or common phrases.

Prefer the mechanism a solver would use. If a category fits several labels, use this priority:
FILL_IN_THE_BLANK, COMMON_PHRASE, SOUND_OR_SPELLING, WORDPLAY_TRANSFORM, WORD_FORM, SYNONYM_OR_NEAR, NAMED_ENTITY_SET, SEMANTIC_SET.

Example json output:
{
  "categories": [
    {
      "category_index": 0,
      "relation_type": "SEMANTIC_SET",
      "confidence": 0.92,
      "rationale": "The members are all examples of the named category."
    }
  ]
}
"""


def load_env_file(path: str = ".env") -> Dict[str, str]:
    values = {}
    if not os.path.exists(path):
        return values
    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def get_deepseek_api_key(env_path: str = ".env") -> Optional[str]:
    return os.environ.get("DEEPSEEK_API_KEY") or load_env_file(env_path).get("DEEPSEEK_API_KEY")


def build_user_prompt(puzzle: Dict[str, Any]) -> str:
    categories = []
    for idx, category in enumerate(puzzle["answers"]):
        categories.append({
            "category_index": idx,
            "group": category["group"],
            "members": category["members"],
            "current_relation_type": category.get("relation_type"),
        })
    return json.dumps({
        "task": "Return json labeling each category by relation_type.",
        "puzzle_id": puzzle.get("id"),
        "date": puzzle.get("date"),
        "categories": categories,
    }, ensure_ascii=False)


def call_deepseek_for_puzzle(
    puzzle: Dict[str, Any],
    api_key: str,
    session=requests,
    timeout: int = 60,
) -> Dict[str, Any]:
    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(puzzle)},
        ],
        "temperature": 0,
        "stream": False,
        "response_format": {"type": "json_object"},
    }
    response = session.post(
        DEEPSEEK_API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    body = response.json()
    content = body["choices"][0]["message"]["content"]
    return json.loads(content)


def validate_label(raw_label: Dict[str, Any], expected_index: int) -> Tuple[bool, Optional[str], float, str]:
    try:
        category_index = int(raw_label.get("category_index"))
        relation_type = str(raw_label.get("relation_type"))
        confidence = float(raw_label.get("confidence", 0.0))
        rationale = str(raw_label.get("rationale", "")).strip()
    except (TypeError, ValueError):
        return False, None, 0.0, "Malformed label fields"

    if category_index != expected_index:
        return False, relation_type, confidence, "Category index mismatch"
    if relation_type not in VALID_POSITIVE_ARCHETYPES:
        return False, relation_type, confidence, "Unknown relation_type"
    if not 0.0 <= confidence <= 1.0:
        return False, relation_type, confidence, "Confidence outside [0, 1]"
    return True, relation_type, confidence, rationale


def merge_puzzle_labels(
    puzzle: Dict[str, Any],
    label_response: Optional[Dict[str, Any]],
    error: Optional[str] = None,
) -> List[Dict[str, Any]]:
    raw_labels = {}
    if isinstance(label_response, dict):
        label_categories = label_response.get("categories")
    elif isinstance(label_response, list):
        label_categories = label_response
    else:
        label_categories = None
    if isinstance(label_categories, list):
        for raw_label in label_categories:
            if isinstance(raw_label, dict) and "category_index" in raw_label:
                try:
                    raw_labels[int(raw_label["category_index"])] = raw_label
                except (TypeError, ValueError):
                    continue

    review_items = []
    for idx, category in enumerate(puzzle["answers"]):
        previous_relation_type = category.get("relation_type", "")
        raw_label = raw_labels.get(idx)
        if error:
            valid, relation_type, confidence, rationale = False, None, 0.0, error
        elif raw_label is None:
            valid, relation_type, confidence, rationale = False, None, 0.0, "Missing category label"
        else:
            valid, relation_type, confidence, rationale = validate_label(raw_label, idx)

        accepted = valid and confidence >= ACCEPT_CONFIDENCE_THRESHOLD
        category["relation_type_previous"] = previous_relation_type
        category["relation_label_confidence"] = confidence
        category["relation_label_status"] = "accepted" if accepted else "needs_review"
        category["relation_label_model"] = DEEPSEEK_MODEL
        category["relation_label_rationale"] = rationale
        if accepted:
            category["relation_type"] = relation_type

        if not accepted:
            review_items.append({
                "puzzle_id": puzzle.get("id"),
                "date": puzzle.get("date", ""),
                "category_index": idx,
                "group": category.get("group", ""),
                "members": category.get("members", []),
                "previous_relation_type": previous_relation_type,
                "suggested_relation_type": relation_type,
                "confidence": confidence,
                "reason": rationale,
            })
    return review_items


def validate_dataset(data: List[Dict[str, Any]]) -> None:
    for puzzle in data:
        if "answers" not in puzzle or len(puzzle["answers"]) != 4:
            raise ValueError(f"Puzzle {puzzle.get('id')} must have exactly 4 answer categories")
        for category in puzzle["answers"]:
            if category.get("relation_type") not in VALID_DATASET_ARCHETYPES:
                raise ValueError(
                    f"Puzzle {puzzle.get('id')} has invalid relation_type: {category.get('relation_type')}"
                )


def atomic_write_json(data: List[Dict[str, Any]], output_path: str) -> None:
    output_dir = os.path.dirname(output_path) or "."
    os.makedirs(output_dir, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(prefix=".tmp_archetypes_", suffix=".json", dir=output_dir)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(temp_path, output_path)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def load_checkpoint(checkpoint_path: str) -> Dict[str, Dict[str, Any]]:
    records = {}
    if not os.path.exists(checkpoint_path):
        return records
    with open(checkpoint_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            record = json.loads(line)
            records[str(record["puzzle_id"])] = record
    return records


def append_checkpoint_record(checkpoint_path: str, record: Dict[str, Any]) -> None:
    checkpoint_dir = os.path.dirname(checkpoint_path)
    if checkpoint_dir:
        os.makedirs(checkpoint_dir, exist_ok=True)
    with open(checkpoint_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def build_label_record(
    puzzle: Dict[str, Any],
    api_key: str,
    session=requests,
) -> Dict[str, Any]:
    puzzle_id = puzzle.get("id")
    try:
        label_response = call_deepseek_for_puzzle(puzzle, api_key, session=session)
        return {
            "puzzle_id": puzzle_id,
            "label_response": label_response,
            "error": None,
        }
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"DeepSeek API request failed for puzzle {puzzle_id}: {exc}") from exc
    except Exception as exc:
        return {
            "puzzle_id": puzzle_id,
            "label_response": None,
            "error": str(exc),
        }


def fetch_missing_label_records(
    puzzles_to_label: List[Dict[str, Any]],
    api_key: str,
    checkpoint_path: str,
    workers: int,
    session=requests,
) -> Dict[str, Dict[str, Any]]:
    records = load_checkpoint(checkpoint_path)
    missing = [
        puzzle
        for puzzle in puzzles_to_label
        if str(puzzle.get("id")) not in records
    ]
    if not missing:
        print(f"Loaded {len(records)} checkpointed puzzle labels; nothing to fetch.", flush=True)
        return records

    print(
        f"Loaded {len(records)} checkpointed puzzle labels; fetching {len(missing)} remaining "
        f"with {workers} worker(s).",
        flush=True,
    )
    if workers <= 1:
        for idx, puzzle in enumerate(missing, start=1):
            print(f"[{idx}/{len(missing)}] Labeling puzzle {puzzle.get('id')}...", flush=True)
            record = build_label_record(puzzle, api_key, session=session)
            append_checkpoint_record(checkpoint_path, record)
            records[str(record["puzzle_id"])] = record
        return records

    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_puzzle = {
            executor.submit(build_label_record, puzzle, api_key, session): puzzle
            for puzzle in missing
        }
        for future in concurrent.futures.as_completed(future_to_puzzle):
            puzzle = future_to_puzzle[future]
            record = future.result()
            append_checkpoint_record(checkpoint_path, record)
            records[str(record["puzzle_id"])] = record
            completed += 1
            print(
                f"[{completed}/{len(missing)}] Checkpointed puzzle {puzzle.get('id')}",
                flush=True,
            )
    return records


def write_review_report(review_items: List[Dict[str, Any]], review_path: str) -> None:
    review_dir = os.path.dirname(review_path)
    if review_dir:
        os.makedirs(review_dir, exist_ok=True)
    lines = [
        "# Archetype Labeling Review",
        "",
        f"Model: `{DEEPSEEK_MODEL}`",
        f"Needs review: {len(review_items)}",
        "",
    ]
    for item in review_items:
        members = ", ".join(item["members"])
        lines.extend([
            f"## Puzzle {item['puzzle_id']} Category {item['category_index']}: {item['group']}",
            f"- Date: {item['date']}",
            f"- Members: {members}",
            f"- Previous: `{item['previous_relation_type']}`",
            f"- Suggested: `{item['suggested_relation_type']}`",
            f"- Confidence: {item['confidence']:.2f}",
            f"- Reason: {item['reason']}",
            "",
        ])
    with open(review_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def label_dataset(
    input_path: str,
    output_path: str,
    api_key: str,
    review_path: str,
    limit: Optional[int] = None,
    workers: int = 128,
    checkpoint_path: str = DEFAULT_CHECKPOINT_PATH,
    session=requests,
) -> Tuple[int, int]:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    review_items = []
    puzzles_to_label = data[:limit] if limit is not None else data
    records = fetch_missing_label_records(
        puzzles_to_label,
        api_key,
        checkpoint_path=checkpoint_path,
        workers=workers,
        session=session,
    )
    for puzzle in puzzles_to_label:
        record = records.get(str(puzzle.get("id")))
        if record is None:
            raise RuntimeError(f"Missing label record for puzzle {puzzle.get('id')}")
        review_items.extend(
            merge_puzzle_labels(
                puzzle,
                record.get("label_response"),
                error=record.get("error"),
            )
        )

    validate_dataset(data)
    atomic_write_json(data, output_path)
    write_review_report(review_items, review_path)
    accepted = sum(
        1
        for puzzle in puzzles_to_label
        for category in puzzle["answers"]
        if category.get("relation_label_status") == "accepted"
    )
    return accepted, len(review_items)


def main() -> int:
    parser = argparse.ArgumentParser(description="Relabel Connections category archetypes with DeepSeek Flash")
    parser.add_argument("--input", default="data/connections.json", help="Input dataset JSON path")
    parser.add_argument("--output", default="data/connections.json", help="Output dataset JSON path")
    parser.add_argument("--review-output", default="visualizations/archetype_labeling_review.md")
    parser.add_argument("--limit", type=int, default=None, help="Limit puzzles for a smoke run")
    parser.add_argument("--workers", type=int, default=128, help="Concurrent DeepSeek requests")
    parser.add_argument("--checkpoint", default=DEFAULT_CHECKPOINT_PATH, help="JSONL checkpoint path")
    args = parser.parse_args()

    api_key = get_deepseek_api_key()
    if not api_key:
        print("Error: DEEPSEEK_API_KEY is required in the environment or .env")
        return 1

    accepted, needs_review = label_dataset(
        input_path=args.input,
        output_path=args.output,
        api_key=api_key,
        review_path=args.review_output,
        limit=args.limit,
        workers=args.workers,
        checkpoint_path=args.checkpoint,
    )
    print(f"Accepted labels: {accepted}")
    print(f"Needs review: {needs_review}")
    print(f"Review report: {args.review_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
