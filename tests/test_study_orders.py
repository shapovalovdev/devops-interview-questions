"""Validate the within-Theme study-order manifest.

A study order is ordered data, never prose.  The order lives in
`config/study-orders.json` — one entry per Theme, mirroring the way
cross-Theme routes live in `config/learning-paths.json` — so the
"Suggested study order" guidance a related-materials page shows can be
generated instead of hand-maintained.  These checks defend that contract:
every Theme with a related-materials page declares exactly one order, every
step points at a Question of that same Theme, every position is earned with
a `why`, and no order contradicts the learning paths' sequencing of the
same Questions.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "study-orders.json"
PATHS = ROOT / "config" / "learning-paths.json"
RELATED = ROOT / "docs" / "related-materials"


def load_manifest() -> dict:
    assert MANIFEST.is_file(), "config/study-orders.json is required"
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def load_paths() -> list[dict]:
    assert PATHS.is_file(), "config/learning-paths.json is required"
    return json.loads(PATHS.read_text(encoding="utf-8"))["paths"]


class StudyOrderManifest(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = load_manifest()
        self.themes = self.manifest["themes"]

    def test_manifest_declares_a_supported_version_and_at_least_one_theme(self) -> None:
        self.assertEqual(self.manifest["version"], 1, "study-order manifest must use version 1")
        self.assertEqual(set(self.manifest), {"version", "themes"}, "manifest carries a version and its themes")
        self.assertTrue(self.themes, "the manifest must declare at least one theme")

    def test_theme_set_matches_related_materials_pages_in_both_directions(self) -> None:
        declared = [theme["theme"] for theme in self.themes]
        self.assertEqual(len(declared), len(set(declared)), f"themes must not be declared twice: {declared}")
        pages = {page.stem for page in RELATED.glob("*.md")}
        self.assertEqual(set(declared), pages, "every related-materials page declares a study order and vice versa")

    def test_every_theme_declares_the_required_fields(self) -> None:
        for theme in self.themes:
            with self.subTest(theme=theme.get("theme")):
                self.assertEqual(
                    set(theme),
                    {"theme", "note", "steps"},
                    "a theme entry declares exactly theme, note, and steps",
                )
                self.assertTrue(theme["note"].strip(), "a theme must carry a one-sentence note")
                self.assertGreaterEqual(
                    len(theme["note"].strip().split()),
                    8,
                    "a note opens the order in the page's own voice, not a label",
                )

    def test_theme_notes_are_authored_not_shared_templates(self) -> None:
        notes = [theme["note"].strip() for theme in self.themes]
        self.assertEqual(len(notes), len(set(notes)), "no two themes share a study-order note")

    def test_every_theme_is_a_non_empty_ordered_list_of_steps(self) -> None:
        for theme in self.themes:
            with self.subTest(theme=theme["theme"]):
                steps = theme["steps"]
                self.assertIsInstance(steps, list, "steps are an ordered list")
                self.assertTrue(steps, f"{theme['theme']} declares no steps; an empty order guides nobody")

    def test_every_step_resolves_to_an_existing_question_of_the_same_theme(self) -> None:
        for theme in self.themes:
            for position, step in enumerate(theme["steps"], start=1):
                with self.subTest(theme=theme["theme"], position=position):
                    self.assertEqual(set(step), {"question", "why"}, "a step is a Question reference and its reason")
                    question = step["question"]
                    self.assertTrue(
                        question.startswith(f"questions/{theme['theme']}/") and question.endswith(".md"),
                        "a step references a Markdown Question of the same Theme",
                    )
                    self.assertTrue(
                        (ROOT / question).is_file(),
                        f"{theme['theme']} step {position}: missing {question}",
                    )

    def test_no_question_repeats_within_a_single_theme(self) -> None:
        for theme in self.themes:
            with self.subTest(theme=theme["theme"]):
                questions = [step["question"] for step in theme["steps"]]
                duplicates = sorted({item for item in questions if questions.count(item) > 1})
                self.assertFalse(duplicates, f"{theme['theme']} repeats {duplicates}")

    def test_every_step_earns_its_position_with_a_why(self) -> None:
        for theme in self.themes:
            for position, step in enumerate(theme["steps"], start=1):
                with self.subTest(theme=theme["theme"], position=position):
                    why = step["why"].strip()
                    self.assertTrue(why, f"{theme['theme']} step {position} has no why")
                    self.assertGreaterEqual(
                        len(why.split()),
                        8,
                        f"{theme['theme']} step {position}: a why must explain the position, not label the topic",
                    )

    def test_study_orders_do_not_contradict_learning_path_ordering(self) -> None:
        """A Theme's order must preserve each path's relative order of its Questions."""
        orders = {theme["theme"]: [step["question"] for step in theme["steps"]] for theme in self.themes}
        for path in load_paths():
            path_position = {step["question"]: index for index, step in enumerate(path["steps"])}
            for theme, questions in orders.items():
                shared = [question for question in questions if question in path_position]
                if len(shared) < 2:
                    continue
                with self.subTest(path=path["slug"], theme=theme):
                    self.assertEqual(
                        shared,
                        sorted(shared, key=lambda question: path_position[question]),
                        f"{theme}'s study order contradicts the {path['slug']} path's relative order of its Questions",
                    )


if __name__ == "__main__":
    unittest.main()
