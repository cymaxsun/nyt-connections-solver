import argparse
import gzip
import html.parser
import json
import os
import re
import tempfile
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional, Set, Tuple

from src.dataset import ConnectionsPuzzle
from src.features import (
    FeatureExtractor,
    NGRAM_COMPOUND_CORPUS,
    NGRAM_COMPOUND_SMOOTHING,
    NGRAM_COMPOUND_YEAR_END,
    NGRAM_COMPOUND_YEAR_START,
)

DEFAULT_EXPORT_INDEX_URL = (
    "https://storage.googleapis.com/books/ngrams/books/20200217/eng/"
    "eng-2-ngrams_exports.html"
)
DEFAULT_PROGRESS_INTERVAL = 10.0


@dataclass(frozen=True)
class NgramRow:
    ngram: str
    year: int
    match_count: int


class _NgramExportIndexParser(html.parser.HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.urls: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if not href or not href.endswith(".gz"):
            return
        self.urls.append(urllib.parse.urljoin(self.base_url, href))


class _ProgressReader:
    def __init__(
        self,
        raw,
        total_bytes: Optional[int],
        label: str,
        interval_seconds: float,
    ):
        self.raw = raw
        self.total_bytes = total_bytes
        self.label = label
        self.interval_seconds = interval_seconds
        self.bytes_read = 0
        self._last_logged_at = 0.0

    def read(self, size: int = -1) -> bytes:
        chunk = self.raw.read(size)
        if chunk:
            self.bytes_read += len(chunk)
            self._maybe_log()
        return chunk

    def readable(self) -> bool:
        return True

    def close(self) -> None:
        if hasattr(self.raw, "close"):
            self.raw.close()

    def _maybe_log(self) -> None:
        now = time.monotonic()
        if now - self._last_logged_at < self.interval_seconds:
            return
        self._last_logged_at = now
        print(self.progress_message())

    def progress_message(self) -> str:
        read_mb = self.bytes_read / (1024 * 1024)
        if self.total_bytes:
            total_mb = self.total_bytes / (1024 * 1024)
            pct = min(100.0, (self.bytes_read / self.total_bytes) * 100.0)
            return f"{self.label}: {pct:.1f}% ({read_mb:.1f}/{total_mb:.1f} MiB compressed)"
        return f"{self.label}: {read_mb:.1f} MiB compressed read"


def cache_metadata(year_start: int, year_end: int) -> Dict[str, object]:
    return {
        "schema_version": FeatureExtractor._ngram_compound_cache_metadata()[
            "schema_version"
        ],
        "corpus": NGRAM_COMPOUND_CORPUS,
        "year_start": year_start,
        "year_end": year_end,
        "smoothing": NGRAM_COMPOUND_SMOOTHING,
        "case_insensitive": True,
    }


def load_target_tokens(data_path: str, letters: Optional[str] = None) -> Set[str]:
    allowed_letters = _parse_letters(letters)
    with open(data_path, "r") as f:
        raw_data = json.load(f)

    tokens = set()
    for item in raw_data:
        puzzle = ConnectionsPuzzle(item)
        for word in puzzle.words:
            token = FeatureExtractor._compound_token(word)
            if not token:
                continue
            if allowed_letters is not None and token[0] not in allowed_letters:
                continue
            tokens.add(token)
    return tokens


def _parse_letters(letters: Optional[str]) -> Optional[Set[str]]:
    if letters is None:
        return None
    parsed = {char.lower() for char in letters if char.isalpha()}
    return parsed or None


def fetch_export_urls(
    index_url: str = DEFAULT_EXPORT_INDEX_URL,
    opener=urllib.request.urlopen,
) -> List[str]:
    req = urllib.request.Request(
        index_url,
        headers={"User-Agent": "Mozilla/5.0 (Connections-Solver; contact: max@example.com)"},
    )
    with opener(req, timeout=30) as response:
        html = response.read().decode("utf-8")

    parser = _NgramExportIndexParser(index_url)
    parser.feed(html)
    return parser.urls


def stream_gzip_text(
    url: str,
    opener=urllib.request.urlopen,
    progress_label: Optional[str] = None,
    progress_interval: float = DEFAULT_PROGRESS_INTERVAL,
) -> Iterator[str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Connections-Solver; contact: max@example.com)"},
    )
    with opener(req, timeout=120) as response:
        total_bytes = _response_content_length(response)
        fileobj = response
        if progress_label and progress_interval > 0:
            fileobj = _ProgressReader(
                response,
                total_bytes=total_bytes,
                label=progress_label,
                interval_seconds=progress_interval,
            )
        with gzip.GzipFile(fileobj=fileobj) as gz:
            for raw_line in gz:
                yield raw_line.decode("utf-8", errors="replace")
        if isinstance(fileobj, _ProgressReader):
            print(fileobj.progress_message())


def _response_content_length(response) -> Optional[int]:
    headers = getattr(response, "headers", None)
    if headers is None and hasattr(response, "getheader"):
        try:
            value = response.getheader("Content-Length")
        except Exception:
            value = None
    elif headers is not None:
        value = headers.get("Content-Length")
    else:
        value = None

    try:
        return int(value) if value else None
    except (TypeError, ValueError):
        return None


def parse_ngram_row(line: str) -> Optional[NgramRow]:
    parts = line.rstrip("\n").split("\t")
    if len(parts) < 3:
        return None
    try:
        return NgramRow(
            ngram=parts[0],
            year=int(parts[1]),
            match_count=int(parts[2]),
        )
    except ValueError:
        return None


def parse_ngram_rows(line: str) -> Iterator[NgramRow]:
    parts = line.rstrip("\n").split("\t")
    if len(parts) < 2:
        return

    # Older exports use: ngram TAB year TAB match_count TAB volume_count.
    row = parse_ngram_row(line)
    if row is not None:
        yield row
        return

    # The 2019 export packs each ngram as:
    # ngram TAB year,match_count,volume_count TAB year,match_count,volume_count ...
    ngram = parts[0]
    for yearly_counts in parts[1:]:
        count_parts = yearly_counts.split(",")
        if len(count_parts) < 2:
            continue
        try:
            yield NgramRow(
                ngram=ngram,
                year=int(count_parts[0]),
                match_count=int(count_parts[1]),
            )
        except ValueError:
            continue


def normalize_ngram_token(token: str) -> Optional[str]:
    token = token.strip().lower()
    token = re.sub(r"_[a-z]+_?$", "", token)
    token = "".join(re.findall(r"[a-z]+", token))
    if not token:
        return None
    return token


def ngram_tokens(ngram: str) -> Optional[Tuple[str, str]]:
    raw_tokens = ngram.strip().split()
    if len(raw_tokens) != 2:
        return None

    left = normalize_ngram_token(raw_tokens[0])
    right = normalize_ngram_token(raw_tokens[1])
    if left is None or right is None:
        return None
    return left, right


def is_completion_candidate(token: str) -> bool:
    return FeatureExtractor._is_ngram_completion_candidate(token)


def update_scores_from_row(
    scores: Dict[Tuple[str, str], Dict[str, int]],
    row: NgramRow,
    target_tokens: Set[str],
    year_start: int,
    year_end: int,
) -> bool:
    if row.year < year_start or row.year > year_end or row.match_count <= 0:
        return False

    tokens = ngram_tokens(row.ngram)
    if tokens is None:
        return False

    left, right = tokens
    updated = False
    if left in target_tokens and is_completion_candidate(right):
        scores[(left, "right")][right] += row.match_count
        updated = True
    if right in target_tokens and is_completion_candidate(left):
        scores[(right, "left")][left] += row.match_count
        updated = True
    return updated


def build_profiles(
    scores: Dict[Tuple[str, str], Dict[str, int]],
    target_tokens: Set[str],
    top_k: int,
) -> Dict[str, Dict[str, Dict[str, float]]]:
    profiles = {
        token: {"left": {}, "right": {}}
        for token in sorted(target_tokens)
    }
    for (token, direction), completion_scores in scores.items():
        if token not in profiles or direction not in ("left", "right"):
            continue
        top_items = sorted(
            completion_scores.items(),
            key=lambda item: (-item[1], item[0]),
        )[:top_k]
        max_score = top_items[0][1] if top_items else 0
        if max_score <= 0:
            continue
        profiles[token][direction] = {
            completion: float(score / max_score)
            for completion, score in top_items
        }
    return profiles


def load_existing_cache(cache_path: str) -> Dict[str, object]:
    if not os.path.exists(cache_path):
        return {"profiles": {}}
    try:
        with open(cache_path, "r") as f:
            data = json.load(f)
    except Exception:
        return {"profiles": {}}
    if not isinstance(data, dict):
        return {"profiles": {}}
    if not isinstance(data.get("profiles"), dict):
        data["profiles"] = {}
    return data


def merge_cache_profiles(
    existing_cache: Dict[str, object],
    warmed_profiles: Dict[str, Dict[str, Dict[str, float]]],
    metadata: Dict[str, object],
    preserve_existing_targets: bool = False,
) -> Dict[str, object]:
    existing_profiles = existing_cache.get("profiles", {})
    if not isinstance(existing_profiles, dict):
        existing_profiles = {}

    merged_profiles = dict(existing_profiles)
    for token, profile in warmed_profiles.items():
        if preserve_existing_targets and _is_valid_profile(merged_profiles.get(token)):
            continue
        merged_profiles[token] = profile

    return {"metadata": metadata, "profiles": merged_profiles}


def _is_valid_profile(profile: object) -> bool:
    return (
        isinstance(profile, dict)
        and isinstance(profile.get("left"), dict)
        and isinstance(profile.get("right"), dict)
    )


def write_cache_atomic(cache_path: str, cache: Dict[str, object]) -> None:
    os.makedirs(os.path.dirname(cache_path) or ".", exist_ok=True)
    fd, temp_path = tempfile.mkstemp(
        prefix=os.path.basename(cache_path),
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
    year_start: int,
    year_end: int,
    top_k: int,
    index_url: str = DEFAULT_EXPORT_INDEX_URL,
    letters: Optional[str] = None,
    limit_files: Optional[int] = None,
    only_missing: bool = False,
    force: bool = False,
    dry_run: bool = False,
    progress_interval: float = DEFAULT_PROGRESS_INTERVAL,
) -> Dict[str, int]:
    if year_start > year_end:
        raise ValueError("--year-start must be less than or equal to --year-end")
    if top_k <= 0:
        raise ValueError("--top-k must be positive")

    existing_cache = load_existing_cache(cache_path)
    target_tokens = load_target_tokens(data_path, letters=letters)
    if only_missing and not force:
        existing_profiles = existing_cache.get("profiles", {})
        target_tokens = {
            token
            for token in target_tokens
            if not _is_valid_profile(existing_profiles.get(token))
        }

    urls = fetch_export_urls(index_url)
    if limit_files is not None:
        urls = urls[:limit_files]

    scores: Dict[Tuple[str, str], Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    rows_seen = 0
    rows_matched = 0
    for file_idx, url in enumerate(urls, start=1):
        print(f"[{file_idx}/{len(urls)}] Streaming {url}")
        progress_label = f"[{file_idx}/{len(urls)}] {os.path.basename(url)}"
        for line in stream_gzip_text(
            url,
            progress_label=progress_label,
            progress_interval=progress_interval,
        ):
            rows_seen += 1
            for row in parse_ngram_rows(line):
                if update_scores_from_row(scores, row, target_tokens, year_start, year_end):
                    rows_matched += 1

    warmed_profiles = build_profiles(scores, target_tokens, top_k=top_k)
    metadata = cache_metadata(year_start, year_end)
    merged_cache = merge_cache_profiles(
        existing_cache,
        warmed_profiles,
        metadata,
        preserve_existing_targets=only_missing and not force,
    )

    populated_profiles = sum(
        1
        for profile in warmed_profiles.values()
        if profile["left"] or profile["right"]
    )

    if dry_run:
        print("Dry run: cache file was not written.")
    else:
        write_cache_atomic(cache_path, merged_cache)
        print(f"Wrote warmed cache to {cache_path}")

    return {
        "target_tokens": len(target_tokens),
        "files_streamed": len(urls),
        "rows_seen": rows_seen,
        "rows_matched": rows_matched,
        "profiles_built": len(warmed_profiles),
        "profiles_populated": populated_profiles,
    }


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Warm Google Ngram compound profiles for Connections edge features."
    )
    parser.add_argument("--data", default="data/connections.json")
    parser.add_argument("--cache", default="data/google_ngram_compound_cache.json")
    parser.add_argument("--year-start", type=int, default=NGRAM_COMPOUND_YEAR_START)
    parser.add_argument("--year-end", type=int, default=NGRAM_COMPOUND_YEAR_END)
    parser.add_argument("--top-k", type=int, default=25)
    parser.add_argument("--index-url", default=DEFAULT_EXPORT_INDEX_URL)
    parser.add_argument("--letters", help="Only warm target tokens starting with these letters.")
    parser.add_argument("--limit-files", type=int, help="Stream only the first N gzip shards.")
    parser.add_argument(
        "--progress-interval",
        type=float,
        default=DEFAULT_PROGRESS_INTERVAL,
        help="Seconds between per-shard compressed-byte progress logs; use 0 to disable.",
    )
    parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Warm only target tokens without an existing valid cache profile.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target profiles even when --only-missing is set.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Stream and summarize without writing the cache file.",
    )
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    summary = warm_ngram_cache(
        data_path=args.data,
        cache_path=args.cache,
        year_start=args.year_start,
        year_end=args.year_end,
        top_k=args.top_k,
        index_url=args.index_url,
        letters=args.letters,
        limit_files=args.limit_files,
        only_missing=args.only_missing,
        force=args.force,
        dry_run=args.dry_run,
        progress_interval=args.progress_interval,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
