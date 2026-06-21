import argparse
import json
import os
import tempfile
import time
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Set

from src.dataset import ConnectionsPuzzle
from src.features import FeatureExtractor

NGRAMS_DEV_CACHE_SCHEMA_VERSION = 2
NGRAMS_DEV_API_BASE = "https://api.ngrams.dev/eng/search"
NGRAMS_DEV_FLAGS = "crepes"
NGRAMS_DEV_SEARCH_LIMIT = 100
DEFAULT_SLEEP_SECONDS = 0.05
USER_AGENT = "Mozilla/5.0 (Connections-Solver; contact: max@example.com)"


def cache_metadata(flags: str = NGRAMS_DEV_FLAGS) -> Dict[str, object]:
    return {
        "schema_version": NGRAMS_DEV_CACHE_SCHEMA_VERSION,
        "source": "ngrams.dev/search",
        "corpus": "eng",
        "score": "total_rel_match_count",
        "case_insensitive": True,
        "flags": flags,
    }


def load_target_tokens(data_path: str) -> Set[str]:
    with open(data_path, "r") as f:
        raw_data = json.load(f)

    tokens = set()
    for item in raw_data:
        puzzle = ConnectionsPuzzle(item)
        for word in puzzle.words:
            token = FeatureExtractor._compound_token(word)
            if token:
                tokens.add(token)
    return tokens


def normalize_ngram_token(token: str) -> Optional[str]:
    token = token.strip().lower()
    token = "".join(urllib.parse.unquote(token).split())
    token = "".join(char for char in token if char.isalpha())
    return token or None


def build_search_url(
    query: str,
    flags: str = NGRAMS_DEV_FLAGS,
    limit: int = NGRAMS_DEV_SEARCH_LIMIT,
    api_base: str = NGRAMS_DEV_API_BASE,
) -> str:
    params = urllib.parse.urlencode({
        "query": query,
        "flags": flags,
        "limit": limit,
    })
    return f"{api_base}?{params}"


def fetch_search_results(
    query: str,
    flags: str = NGRAMS_DEV_FLAGS,
    limit: int = NGRAMS_DEV_SEARCH_LIMIT,
    api_base: str = NGRAMS_DEV_API_BASE,
    opener=urllib.request.urlopen,
) -> Dict[str, Any]:
    url = build_search_url(query, flags=flags, limit=limit, api_base=api_base)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with opener(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_completion(
    ngram: Dict[str, Any],
    target: str,
    direction: str,
) -> Optional[str]:
    raw_tokens = ngram.get("tokens")
    if not isinstance(raw_tokens, list):
        return None

    tokens = []
    for token_info in raw_tokens:
        if not isinstance(token_info, dict):
            continue
        text = token_info.get("text")
        if not isinstance(text, str):
            continue
        token = normalize_ngram_token(text)
        if token:
            tokens.append(token)

    if direction == "right" and len(tokens) >= 2 and tokens[0] == target:
        completion = tokens[1]
    elif direction == "left" and len(tokens) >= 2 and tokens[-1] == target:
        completion = tokens[-2]
    else:
        return None

    if completion == target:
        return None
    if not FeatureExtractor._is_ngram_completion_candidate(completion):
        return None
    return completion


def ngram_score(ngram: Dict[str, Any]) -> float:
    for key in ("relTotalMatchCount", "absTotalMatchCount"):
        value = ngram.get(key)
        if isinstance(value, (int, float)):
            return max(0.0, float(value))
    return 0.0


def extract_completion_scores(
    response: Dict[str, Any],
    target: str,
    direction: str,
) -> Dict[str, float]:
    scores: Dict[str, float] = {}
    ngrams = response.get("ngrams")
    if not isinstance(ngrams, list):
        return scores

    for ngram in ngrams:
        if not isinstance(ngram, dict):
            continue
        completion = extract_completion(ngram, target, direction)
        if completion is None:
            continue
        score = ngram_score(ngram)
        if score <= 0.0:
            continue
        scores[completion] = max(scores.get(completion, 0.0), score)
    return scores


def normalize_completion_scores(
    scores: Dict[str, float],
    top_k: int,
) -> Dict[str, float]:
    top_items = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:top_k]
    max_score = top_items[0][1] if top_items else 0.0
    if max_score <= 0.0:
        return {}
    return {
        completion: float(score / max_score)
        for completion, score in top_items
    }


def fetch_profile_for_token(
    token: str,
    top_k: int,
    flags: str = NGRAMS_DEV_FLAGS,
    search_limit: int = NGRAMS_DEV_SEARCH_LIMIT,
    api_base: str = NGRAMS_DEV_API_BASE,
    sleep_seconds: float = 0.0,
    opener=urllib.request.urlopen,
) -> Dict[str, Dict[str, float]]:
    right_response = fetch_search_results(
        f"{token} *",
        flags=flags,
        limit=search_limit,
        api_base=api_base,
        opener=opener,
    )
    if sleep_seconds:
        time.sleep(sleep_seconds)
    left_response = fetch_search_results(
        f"* {token}",
        flags=flags,
        limit=search_limit,
        api_base=api_base,
        opener=opener,
    )
    return {
        "left": normalize_completion_scores(
            extract_completion_scores(left_response, token, "left"),
            top_k=top_k,
        ),
        "right": normalize_completion_scores(
            extract_completion_scores(right_response, token, "right"),
            top_k=top_k,
        ),
    }


def write_cache_atomic(cache_path: str, cache: Dict[str, object]) -> None:
    os.makedirs(os.path.dirname(cache_path) or ".", exist_ok=True)
    fd, temp_path = tempfile.mkstemp(
        prefix=f"{os.path.basename(cache_path)}.",
        suffix=".tmp",
        dir=os.path.dirname(cache_path) or ".",
        text=True,
    )
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(cache, f, indent=2, sort_keys=True)
            f.write("\n")
        os.replace(temp_path, cache_path)
    except Exception:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise


def warm_ngram_cache(
    data_path: str,
    cache_path: str,
    top_k: int = 25,
    limit: Optional[int] = None,
    sleep_seconds: float = DEFAULT_SLEEP_SECONDS,
    dry_run: bool = False,
    cache_failures: bool = False,
    flags: str = NGRAMS_DEV_FLAGS,
    search_limit: int = NGRAMS_DEV_SEARCH_LIMIT,
    api_base: str = NGRAMS_DEV_API_BASE,
    opener=urllib.request.urlopen,
) -> Dict[str, int]:
    if top_k <= 0:
        raise ValueError("--top-k must be positive")
    if limit is not None and limit <= 0:
        raise ValueError("--limit must be positive")
    if sleep_seconds < 0.0:
        raise ValueError("--sleep must be non-negative")
    if search_limit <= 0:
        raise ValueError("--search-limit must be positive")

    target_tokens = sorted(load_target_tokens(data_path))
    if limit is not None:
        target_tokens = target_tokens[:limit]

    profiles: Dict[str, Dict[str, Dict[str, float]]] = {}
    failed_tokens: List[str] = []

    for idx, token in enumerate(target_tokens, start=1):
        print(f"[{idx}/{len(target_tokens)}] Warming {token}")
        try:
            profiles[token] = fetch_profile_for_token(
                token,
                top_k=top_k,
                flags=flags,
                search_limit=search_limit,
                api_base=api_base,
                sleep_seconds=sleep_seconds,
                opener=opener,
            )
        except Exception as exc:
            failed_tokens.append(token)
            print(f"Warning: ngrams.dev lookup failed for {token!r}: {exc}")
            if cache_failures:
                profiles[token] = {"left": {}, "right": {}}

        if sleep_seconds and idx < len(target_tokens):
            time.sleep(sleep_seconds)

    cache = {
        "metadata": cache_metadata(flags=flags),
        "profiles": profiles,
    }
    populated_profiles = sum(
        1
        for profile in profiles.values()
        if profile["left"] or profile["right"]
    )

    if dry_run:
        print("Dry run: cache file was not written.")
    else:
        write_cache_atomic(cache_path, cache)
        print(f"Wrote warmed cache to {cache_path}")

    return {
        "target_tokens": len(target_tokens),
        "profiles_built": len(profiles),
        "profiles_populated": populated_profiles,
        "failed_tokens": len(failed_tokens),
    }


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Overwrite Google Ngram compound cache using ngrams.dev search."
    )
    parser.add_argument("--data", default="data/connections.json")
    parser.add_argument("--cache", default="data/google_ngram_compound_cache.json")
    parser.add_argument("--top-k", type=int, default=25)
    parser.add_argument("--limit", type=int, help="Warm only the first N dataset tokens.")
    parser.add_argument(
        "--sleep",
        type=float,
        default=DEFAULT_SLEEP_SECONDS,
        help="Seconds to sleep between target-token requests.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and summarize without writing the cache file.",
    )
    parser.add_argument(
        "--cache-failures",
        action="store_true",
        help="Include empty profiles for failed tokens instead of omitting them.",
    )
    parser.add_argument("--flags", default=NGRAMS_DEV_FLAGS)
    parser.add_argument("--search-limit", type=int, default=NGRAMS_DEV_SEARCH_LIMIT)
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    summary = warm_ngram_cache(
        data_path=args.data,
        cache_path=args.cache,
        top_k=args.top_k,
        limit=args.limit,
        sleep_seconds=args.sleep,
        dry_run=args.dry_run,
        cache_failures=args.cache_failures,
        flags=args.flags,
        search_limit=args.search_limit,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    if summary["failed_tokens"] and not args.cache_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
