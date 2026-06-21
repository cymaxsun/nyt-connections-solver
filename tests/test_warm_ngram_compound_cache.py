import gzip
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from collections import defaultdict

from src import warm_ngram_compound_cache as warmer


class WarmNgramCompoundCacheTests(unittest.TestCase):
    def test_normalize_ngram_token_strips_pos_tags_and_noise(self):
        self.assertEqual(warmer.normalize_ngram_token("Board_NOUN"), "board")
        self.assertEqual(warmer.normalize_ngram_token("surf_VERB_"), "surf")
        self.assertEqual(warmer.normalize_ngram_token("can't"), "cant")
        self.assertIsNone(warmer.normalize_ngram_token("_START_"))

    def test_update_scores_aggregates_only_configured_year_range(self):
        scores = defaultdict(lambda: defaultdict(int))
        targets = {"surf", "skate"}
        rows = [
            warmer.NgramRow("surf board", 1979, 100),
            warmer.NgramRow("surf board", 1980, 3),
            warmer.NgramRow("surf board", 2019, 7),
            warmer.NgramRow("ice skate", 2019, 11),
            warmer.NgramRow("skate board", 2020, 13),
        ]

        for row in rows:
            warmer.update_scores_from_row(scores, row, targets, 1980, 2019)

        self.assertEqual(scores[("surf", "right")]["board"], 10)
        self.assertEqual(scores[("skate", "left")]["ice"], 11)
        self.assertNotIn("board", scores[("skate", "right")])

    def test_parse_ngram_rows_supports_packed_2019_export_format(self):
        rows = list(
            warmer.parse_ngram_rows(
                "surf board\t1979,100,90\t1980,3,2\t2019,7,6\n"
            )
        )

        self.assertEqual(
            rows,
            [
                warmer.NgramRow("surf board", 1979, 100),
                warmer.NgramRow("surf board", 1980, 3),
                warmer.NgramRow("surf board", 2019, 7),
            ],
        )

    def test_completion_filter_rejects_filler_words(self):
        for token in ["and", "the", "of", "but", "with", "from", "your", "have"]:
            self.assertFalse(warmer.is_completion_candidate(token), token)

    def test_capitalized_filler_words_are_normalized_before_filtering(self):
        scores = defaultdict(lambda: defaultdict(int))

        matched = warmer.update_scores_from_row(
            scores,
            warmer.NgramRow("surf The_DET", 2019, 100),
            {"surf"},
            1980,
            2019,
        )

        self.assertFalse(matched)
        self.assertEqual(dict(scores), {})

    def test_completion_filter_keeps_phrasal_particles(self):
        for token in [
            "up",
            "down",
            "in",
            "out",
            "off",
            "on",
            "over",
            "back",
            "away",
            "around",
            "through",
            "apart",
            "together",
        ]:
            self.assertTrue(warmer.is_completion_candidate(token), token)

    def test_build_profiles_normalizes_and_keeps_top_k(self):
        scores = defaultdict(lambda: defaultdict(int))
        scores[("surf", "right")]["board"] = 10
        scores[("surf", "right")]["shop"] = 5
        scores[("surf", "right")]["wax"] = 1

        profiles = warmer.build_profiles(scores, {"surf", "skate"}, top_k=2)

        self.assertEqual(profiles["surf"]["right"], {"board": 1.0, "shop": 0.5})
        self.assertEqual(profiles["surf"]["left"], {})
        self.assertEqual(profiles["skate"], {"left": {}, "right": {}})

    def test_merge_cache_profiles_preserves_non_target_entries(self):
        existing = {
            "metadata": {"old": True},
            "profiles": {
                "legacy": {"left": {"old": 1.0}, "right": {}},
                "surf": {"left": {}, "right": {"api": 1.0}},
            },
        }
        warmed = {"surf": {"left": {}, "right": {"board": 1.0}}}

        merged = warmer.merge_cache_profiles(
            existing,
            warmed,
            {"schema_version": 1},
            preserve_existing_targets=False,
        )

        self.assertEqual(merged["profiles"]["legacy"], existing["profiles"]["legacy"])
        self.assertEqual(merged["profiles"]["surf"], warmed["surf"])
        self.assertEqual(merged["metadata"], {"schema_version": 1})

    def test_merge_cache_profiles_can_preserve_existing_targets(self):
        existing = {
            "profiles": {
                "surf": {"left": {}, "right": {"api": 1.0}},
            },
        }
        warmed = {"surf": {"left": {}, "right": {"board": 1.0}}}

        merged = warmer.merge_cache_profiles(
            existing,
            warmed,
            {"schema_version": 1},
            preserve_existing_targets=True,
        )

        self.assertEqual(merged["profiles"]["surf"], existing["profiles"]["surf"])

    def test_stream_gzip_text_reads_compressed_lines(self):
        payload = gzip.compress(b"surf board\t2019\t7\t2\n")

        def opener(req, timeout):
            return io.BytesIO(payload)

        self.assertEqual(
            list(warmer.stream_gzip_text("https://example.test/file.gz", opener=opener)),
            ["surf board\t2019\t7\t2\n"],
        )

    def test_progress_reader_reports_content_length_percentage(self):
        one_mib = 1024 * 1024
        reader = warmer._ProgressReader(
            io.BytesIO(b"x" * one_mib),
            total_bytes=2 * one_mib,
            label="test-shard",
            interval_seconds=0,
        )

        with redirect_stdout(io.StringIO()):
            self.assertEqual(len(reader.read(one_mib)), one_mib)
        self.assertEqual(
            reader.progress_message(),
            "test-shard: 50.0% (1.0/2.0 MiB compressed)",
        )

    def test_fetch_export_urls_parses_gzip_links(self):
        html = b"""
        <html>
          <a href="2-00000-of-00589.gz">first</a>
          <a href="notes.txt">skip</a>
          <a href="https://example.test/2-00001-of-00589.gz">second</a>
        </html>
        """

        def opener(req, timeout):
            return io.BytesIO(html)

        urls = warmer.fetch_export_urls(
            "https://storage.googleapis.com/books/ngrams/books/20200217/eng/index.html",
            opener=opener,
        )

        self.assertEqual(
            urls,
            [
                "https://storage.googleapis.com/books/ngrams/books/20200217/eng/2-00000-of-00589.gz",
                "https://example.test/2-00001-of-00589.gz",
            ],
        )

    def test_warm_ngram_cache_dry_run_uses_synthetic_stream(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            data_path = os.path.join(tmpdir, "connections.json")
            cache_path = os.path.join(tmpdir, "google_ngram_compound_cache.json")
            with open(data_path, "w") as f:
                json.dump(
                    [
                        {
                            "id": 1,
                            "answers": [
                                {
                                    "level": 0,
                                    "group": "boards",
                                    "members": ["SURF", "SKATE", "SNOW", "DASH"],
                                },
                                {
                                    "level": 1,
                                    "group": "fill",
                                    "members": ["A", "B", "C", "D"],
                                },
                                {
                                    "level": 2,
                                    "group": "fill2",
                                    "members": ["E", "F", "G", "H"],
                                },
                                {
                                    "level": 3,
                                    "group": "fill3",
                                    "members": ["I", "J", "K", "L"],
                                },
                            ],
                        }
                    ],
                    f,
                )

            original_fetch = warmer.fetch_export_urls
            original_stream = warmer.stream_gzip_text
            try:
                warmer.fetch_export_urls = lambda index_url: ["memory://one.gz"]
                warmer.stream_gzip_text = lambda url, **kwargs: iter(
                    [
                        "surf board\t1980\t3\t1\n",
                        "surf board\t2019\t7\t1\n",
                        "skate board\t2019\t5\t1\n",
                        "surf the\t2019\t99\t1\n",
                    ]
                )

                summary = warmer.warm_ngram_cache(
                    data_path=data_path,
                    cache_path=cache_path,
                    year_start=1980,
                    year_end=2019,
                    top_k=25,
                    dry_run=True,
                    progress_interval=0,
                )
            finally:
                warmer.fetch_export_urls = original_fetch
                warmer.stream_gzip_text = original_stream

            self.assertEqual(summary["files_streamed"], 1)
            self.assertEqual(summary["rows_matched"], 3)
            self.assertFalse(os.path.exists(cache_path))


if __name__ == "__main__":
    unittest.main()
