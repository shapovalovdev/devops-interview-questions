"""Validate the lab records the site data layer publishes.

Labs are repository artifacts (`labs/<theme>/<slug>.md`, contract owned by
`tests/validate_labs.py`), invisible to the site until the catalog generator
resolves their front matter into `window.labs` beside the Question,
certification, learning-path, and study-order windows.  These checks pin that
contract: one record per lab on disk in both directions, fields faithful to
the front matter, every `questionHref` resolving to a published Question
record, deterministic theme-then-slug order, and regeneration that leaves the
tree byte-identical.
"""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

from validate_labs import front_matter as lab_front_matter


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
CATALOG = ROOT / "assets" / "questions.js"
GENERATOR = ROOT / "scripts" / "generate_question_catalog.py"
RELATED = ROOT / "docs" / "related-materials"


def load_generator():
    spec = importlib.util.spec_from_file_location("repo_generate_question_catalog_labs", GENERATOR)
    assert spec and spec.loader, "scripts/generate_question_catalog.py must be importable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def window(name: str) -> list[dict]:
    """Read one `window.<name>` array back out of the generated site catalog.

    `window.questions` is written one record per line with a trailing comma,
    so drop trailing commas before the closing bracket before parsing.
    """
    text = CATALOG.read_text(encoding="utf-8")
    match = re.search(rf"window\.{name} = (\[[\s\S]*?\]);", text)
    assert match, f"assets/questions.js must publish window.{name}"
    return json.loads(re.sub(r",(\s*\])", r"\1", match.group(1)))


def lab_slug(path: Path) -> str:
    return f"{path.parent.name}/{path.stem}"


class GeneratedLabCatalog(unittest.TestCase):
    """The site reads labs from `assets/questions.js`, which the generator writes."""

    def setUp(self) -> None:
        self.records = window("labs")
        self.lab_paths = sorted(LABS.glob("*/*.md"))
        self.by_slug = {record["slug"]: record for record in self.records}

    def test_the_catalog_publishes_the_labs_on_disk_one_for_one(self) -> None:
        self.assertTrue(self.records, "window.labs must publish at least one lab")
        self.assertTrue(self.lab_paths, "labs/ must contain at least one lab")
        on_disk = {lab_slug(path) for path in self.lab_paths}
        published = {record["slug"] for record in self.records}
        self.assertEqual(
            on_disk,
            published,
            "every labs/*/*.md file appears in window.labs and no record lacks a source file",
        )
        self.assertEqual(len(self.records), len(published), "no slug is published twice")
        self.assertEqual(len(self.records), len(self.lab_paths), "record count equals the lab count on disk")

    def test_records_are_ordered_by_theme_then_slug(self) -> None:
        keys = [(record["theme"], record["slug"]) for record in self.records]
        self.assertEqual(keys, sorted(keys), "window.labs publishes in deterministic theme-then-slug order")

    def test_every_record_matches_its_lab_front_matter(self) -> None:
        for path in self.lab_paths:
            slug = lab_slug(path)
            with self.subTest(lab=slug):
                record = self.by_slug[slug]
                fields = lab_front_matter(path.read_text(encoding="utf-8"), slug)
                self.assertEqual(
                    set(record),
                    {"title", "theme", "difficulty", "tags", "why", "questionTitle", "questionHref", "slug"},
                    "a lab record carries exactly the renderable fields",
                )
                self.assertNotIn("path", record, "`path` is the Question catalog's own key")
                self.assertEqual(record["title"], fields["title"], "title must match the front matter")
                self.assertEqual(record["theme"], fields["theme"], "theme must match the front matter")
                self.assertEqual(record["difficulty"], fields["difficulty"], "difficulty must match the front matter")
                self.assertEqual(record["tags"], fields["tags"], "tags must match the front matter")
                self.assertEqual(record["why"], fields["why"], "why must match the front matter")
                self.assertIsInstance(record["tags"], list, "tags publish as a list")

    def test_every_question_href_resolves_to_a_published_question(self) -> None:
        questions = {record["path"]: record for record in window("questions")}
        for record in self.records:
            with self.subTest(lab=record["slug"]):
                self.assertTrue(record["questionHref"].endswith(".html"), "a lab links to a rendered Question page")
                self.assertIn(
                    record["questionHref"],
                    questions,
                    "questionHref must resolve to an existing Question catalog record",
                )
                self.assertEqual(
                    record["questionTitle"],
                    questions[record["questionHref"]]["title"],
                    "questionTitle must be the referenced Question's title",
                )

    def test_regeneration_leaves_no_diff_in_the_working_tree(self) -> None:
        """The no-diff gate: run the generator, demand byte-identical output.

        A hand-edited `window.labs` block is overwritten by regeneration, which
        makes the tree differ and fails here instead of silently overriding
        the edit.
        """
        generator = load_generator()
        watched = sorted(RELATED.glob("*.md")) + [CATALOG]
        before = {path: path.read_bytes() for path in watched}
        try:
            generator.main()
            drifted = [path.name for path in watched if path.read_bytes() != before[path]]
        finally:
            for path, content in before.items():
                if path.read_bytes() != content:
                    path.write_bytes(content)
        self.assertEqual(
            drifted,
            [],
            "these files differ from what scripts/generate_question_catalog.py "
            f"generates: {drifted}; regenerate instead of hand-editing",
        )


if __name__ == "__main__":
    unittest.main()
