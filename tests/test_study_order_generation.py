"""Prove the study-order prose on related-materials pages cannot drift.

The "Suggested study order" section of every `docs/related-materials/*.md`
page is generated from `config/study-orders.json` by
`scripts/generate_question_catalog.py`: the Theme's authored `note` opens the
section and each manifest step renders as an ordered link to its Question
followed by its `why`.  These checks defend that contract twice over.
Regeneration must leave the working tree byte-identical, so a hand-edited
section fails CI the same way a stale `assets/questions.js` does.  And each
page must actually carry the manifest's note and every step, in order, so a
generator bug cannot paper over a mismatch it created itself.
"""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_question_catalog.py"
MANIFEST = ROOT / "config" / "study-orders.json"
RELATED = ROOT / "docs" / "related-materials"
CATALOG = ROOT / "assets" / "questions.js"
HEADER = re.compile(r"^## Suggested study order\s*$", re.MULTILINE)
NEXT_SECTION = re.compile(r"^## ", re.MULTILINE)
ORDERED_ITEM = re.compile(r"^(\d+)\. ", re.MULTILINE)


def load_generator():
    spec = importlib.util.spec_from_file_location("repo_generate_question_catalog", GENERATOR)
    assert spec and spec.loader, "scripts/generate_question_catalog.py must be importable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def section_body(text: str) -> str:
    match = HEADER.search(text)
    assert match is not None, "page carries the study-order header"
    rest = text[match.end():]
    following = NEXT_SECTION.search(rest)
    return rest[: following.start()] if following else rest


def step_href(question: str) -> str:
    return "../../" + question.removesuffix(".md") + ".html"


class GeneratedStudyOrderSections(unittest.TestCase):
    def setUp(self) -> None:
        self.themes = load_manifest()["themes"]

    def test_regeneration_leaves_no_diff_in_the_working_tree(self) -> None:
        """The no-diff gate: run the generator, demand byte-identical output.

        A hand-edited section is rewritten back to the manifest's rendering,
        which makes the tree differ and fails here instead of silently
        overriding the edit.
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

    def test_every_page_renders_its_manifest_note_and_steps_in_order(self) -> None:
        for theme in self.themes:
            with self.subTest(theme=theme["theme"]):
                page = RELATED / f"{theme['theme']}.md"
                body = section_body(page.read_text(encoding="utf-8"))
                paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", body) if chunk.strip()]
                self.assertTrue(paragraphs, "the section has a body")
                self.assertEqual(
                    " ".join(paragraphs[0].split()),
                    " ".join(theme["note"].split()),
                    "the section opens with the manifest's authored note",
                )
                items = ORDERED_ITEM.findall(body)
                self.assertEqual(
                    [int(number) for number in items],
                    list(range(1, len(theme["steps"]) + 1)),
                    "the section numbers one ordered item per manifest step",
                )
                positions = [body.find(step_href(step["question"])) for step in theme["steps"]]
                self.assertNotIn(-1, positions, "every step links to the Question the manifest ordered")
                self.assertEqual(
                    positions,
                    sorted(positions),
                    "steps appear on the page in the manifest's order",
                )


if __name__ == "__main__":
    unittest.main()
