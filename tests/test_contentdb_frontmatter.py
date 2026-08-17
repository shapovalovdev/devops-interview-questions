"""Hold `contentdb.frontmatter` to the dialect the repository already speaks.

The corpus is parsed by three callers now: `tests/validate_labs.py`,
`scripts/generate_question_catalog.py`, and Ingest.  A parser that drifts from
the other two is worse than no parser at all — it would let a Question into the
Content store with a field the validators never saw.  So the agreement checks
below re-parse the *whole* live corpus with both the old parsers and the new one
and demand identical results, which is the only assertion that keeps the three
honest as the corpus grows.

The failure checks cover the other half of the contract: front matter that
cannot be read must raise `FrontMatterError` naming the file, never return a
half-parsed mapping that Ingest would happily store.
"""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import frontmatter  # noqa: E402  - needs the path above

import validate_labs  # noqa: E402  - a tests/ sibling


def _load_catalog_generator():
    spec = importlib.util.spec_from_file_location(
        "repo_generate_question_catalog", ROOT / "scripts" / "generate_question_catalog.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


QUESTION = """---
title: A title with: a colon
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, cks]
sources:
  - url: https://kubernetes.io/docs/concepts/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://kubernetes.io/docs/reference/
    source_type: official-api
    verified_on: 2026-08-07
---

# A title with: a colon

The prompt paragraph.

## Answer guide

- One point.
"""


class ParsesTheSupportedShapes(unittest.TestCase):
    def test_scalars_inline_lists_and_mapping_lists(self):
        fields = frontmatter.parse(QUESTION, "memory.md")
        self.assertEqual(fields["title"], "A title with: a colon")
        self.assertEqual(fields["difficulty"], "senior")
        self.assertEqual(fields["tags"], ["kubernetes", "security", "cks"])
        self.assertEqual(
            fields["sources"],
            [
                {
                    "url": "https://kubernetes.io/docs/concepts/",
                    "source_type": "official-docs",
                    "verified_on": "2026-08-06",
                },
                {
                    "url": "https://kubernetes.io/docs/reference/",
                    "source_type": "official-api",
                    "verified_on": "2026-08-07",
                },
            ],
        )

    def test_quoted_scalars_and_block_lists_of_scalars(self):
        fields = frontmatter.parse(
            '---\ntitle: "Quoted"\nchecklist:\n  - "Step one"\n  - "Step two"\n---\n',
            "memory.md",
        )
        self.assertEqual(fields["title"], "Quoted")
        self.assertEqual(fields["checklist"], ["Step one", "Step two"])

    def test_split_returns_the_body_below_the_front_matter(self):
        _, body = frontmatter.split(QUESTION, "memory.md")
        self.assertTrue(body.startswith("\n# A title with: a colon"))
        self.assertIn("## Answer guide", body)
        self.assertNotIn("difficulty: senior", body)


class RefusesFrontMatterItCannotRead(unittest.TestCase):
    def assert_refused(self, text: str, needle: str):
        with self.assertRaises(frontmatter.FrontMatterError) as caught:
            frontmatter.parse(text, "broken.md")
        self.assertIn("broken.md", str(caught.exception))
        self.assertIn(needle, str(caught.exception))

    def test_missing_opening_marker(self):
        self.assert_refused("title: x\n", "must begin with ---")

    def test_missing_closing_marker(self):
        self.assert_refused("---\ntitle: x\n", "must be closed with ---")

    def test_duplicate_field(self):
        self.assert_refused("---\ntitle: x\ntitle: y\n---\n", "duplicate front-matter field title")

    def test_list_item_outside_any_field(self):
        self.assert_refused("---\n  - orphan\n---\n", "list item outside")

    def test_line_that_is_not_a_field(self):
        self.assert_refused("---\ntitle x\n---\n", "not a field")

    def test_unsupported_indented_line(self):
        self.assert_refused("---\ntitle: x\n    nested: y\n---\n", "unsupported indented")


class AgreesWithTheExistingParsers(unittest.TestCase):
    """The whole corpus, parsed both ways, must come out identical."""

    @classmethod
    def setUpClass(cls):
        cls.catalog = _load_catalog_generator()

    def test_every_question_matches_the_catalog_generator(self):
        paths = sorted((ROOT / "questions").glob("*/*.md"))
        self.assertTrue(paths, "no Questions found to compare")
        for path in paths:
            fields = frontmatter.parse(path.read_text(encoding="utf-8"), str(path))
            legacy = self.catalog.front_matter(path)
            for name in ("title", "theme", "difficulty", "type"):
                self.assertEqual(fields[name], legacy[name], f"{path}: {name}")
            self.assertEqual(fields["tags"], re.findall(r"[a-z0-9-]+", legacy["tags"]), str(path))

    def test_every_lab_matches_the_lab_validator(self):
        paths = sorted((ROOT / "labs").glob("*/*.md"))
        self.assertTrue(paths, "no Labs found to compare")
        for path in paths:
            text = path.read_text(encoding="utf-8")
            self.assertEqual(
                frontmatter.parse(text, str(path)),
                validate_labs.front_matter(text, str(path)),
                str(path),
            )
