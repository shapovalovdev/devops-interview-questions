"""Validate the ordered learning-path manifest and its generated site catalog.

A learning path is ordered data, never prose.  The order lives in
`config/learning-paths.json`, so one Question can hold different positions in
several paths without a single Question file changing.  These checks defend
that contract: a step must point at a Question that exists, must justify its
position, and must not appear twice inside the same path.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "learning-paths.json"
CATALOG = ROOT / "assets" / "questions.js"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_manifest() -> dict:
    assert MANIFEST.is_file(), "config/learning-paths.json is required"
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def generated_paths() -> list[dict]:
    """Read `window.learningPaths` back out of the generated site catalog."""
    text = CATALOG.read_text(encoding="utf-8")
    match = re.search(r"window\.learningPaths = (\[[\s\S]*?\]);", text)
    assert match, "assets/questions.js must publish window.learningPaths"
    return json.loads(match.group(1))


class LearningPathManifest(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = load_manifest()
        self.paths = self.manifest["paths"]

    def test_manifest_declares_a_supported_version_and_at_least_one_path(self) -> None:
        self.assertEqual(self.manifest["version"], 1, "learning-path manifest must use version 1")
        self.assertEqual(set(self.manifest), {"version", "paths"}, "manifest carries a version and its paths")
        self.assertTrue(self.paths, "the manifest must declare at least one path")

    def test_every_path_declares_the_required_fields(self) -> None:
        slugs = [path["slug"] for path in self.paths]
        self.assertEqual(len(slugs), len(set(slugs)), f"path slugs must not be duplicated: {slugs}")
        for path in self.paths:
            with self.subTest(path=path.get("slug")):
                self.assertEqual(
                    set(path),
                    {"slug", "title", "audience", "prerequisites", "steps"},
                    "a path declares exactly slug, title, audience, prerequisites, and steps",
                )
                self.assertRegex(path["slug"], SLUG, "a slug is lowercase and hyphen-separated so it can be URL state")
                self.assertTrue(path["title"].strip(), "a path must be titled")
                self.assertTrue(path["audience"].strip(), "a path must state who it is for")
                self.assertIsInstance(path["prerequisites"], list, "prerequisites are a list of path slugs")

    def test_prerequisites_resolve_to_other_declared_paths(self) -> None:
        slugs = {path["slug"] for path in self.paths}
        for path in self.paths:
            with self.subTest(path=path["slug"]):
                for prerequisite in path["prerequisites"]:
                    self.assertIn(prerequisite, slugs, "a prerequisite must name a declared path")
                    self.assertNotEqual(prerequisite, path["slug"], "a path cannot require itself")

    def test_every_path_is_a_non_empty_ordered_list_of_steps(self) -> None:
        for path in self.paths:
            with self.subTest(path=path["slug"]):
                steps = path["steps"]
                self.assertIsInstance(steps, list, "steps are an ordered list")
                self.assertTrue(steps, f"{path['slug']} declares no steps; an empty path teaches no sequence")

    def test_every_step_resolves_to_an_existing_question(self) -> None:
        for path in self.paths:
            for position, step in enumerate(path["steps"], start=1):
                with self.subTest(path=path["slug"], position=position):
                    self.assertEqual(set(step), {"question", "why"}, "a step is a Question reference and its reason")
                    question = step["question"]
                    self.assertTrue(
                        question.startswith("questions/") and question.endswith(".md"),
                        "a step references a Markdown Question under questions/",
                    )
                    self.assertTrue((ROOT / question).is_file(), f"{path['slug']} step {position}: missing {question}")

    def test_no_question_repeats_within_a_single_path(self) -> None:
        for path in self.paths:
            with self.subTest(path=path["slug"]):
                questions = [step["question"] for step in path["steps"]]
                duplicates = sorted({item for item in questions if questions.count(item) > 1})
                self.assertFalse(duplicates, f"{path['slug']} repeats {duplicates}")

    def test_every_step_earns_its_position_with_a_why(self) -> None:
        for path in self.paths:
            for position, step in enumerate(path["steps"], start=1):
                with self.subTest(path=path["slug"], position=position):
                    why = step["why"].strip()
                    self.assertTrue(why, f"{path['slug']} step {position} has no why")
                    self.assertGreaterEqual(
                        len(why.split()),
                        8,
                        f"{path['slug']} step {position}: a why must explain the position, not label the topic",
                    )

    def test_the_sre_track_is_a_complete_cross_theme_progression(self) -> None:
        track = next((path for path in self.paths if path["slug"] == "sre-track"), None)
        self.assertIsNotNone(track, "sre-track is the seed path and must stay declared")
        steps = track["steps"]
        self.assertGreaterEqual(len(steps), 30, "the SRE track is a full progression, not a shortlist")
        self.assertLessEqual(len(steps), 40, "keep the SRE track finishable")
        themes = {step["question"].split("/")[1] for step in steps}
        self.assertGreaterEqual(len(themes), 7, "an SRE track crosses Themes rather than sitting in one folder")
        self.assertEqual(
            steps[0]["question"],
            "questions/sre/define-service-reliability.md",
            "the track opens on what reliability means; every later technique defends that promise",
        )


class GeneratedLearningPathCatalog(unittest.TestCase):
    """The site reads paths from `assets/questions.js`, which the generator writes."""

    def setUp(self) -> None:
        self.manifest = load_manifest()
        self.generated = generated_paths()

    def test_generated_catalog_matches_the_manifest_order(self) -> None:
        self.assertEqual(
            [path["slug"] for path in self.generated],
            [path["slug"] for path in self.manifest["paths"]],
            "regenerate assets/questions.js with scripts/generate_question_catalog.py",
        )
        for declared, generated in zip(self.manifest["paths"], self.generated):
            with self.subTest(path=declared["slug"]):
                self.assertEqual(
                    [step["why"] for step in generated["steps"]],
                    [step["why"] for step in declared["steps"]],
                    "the published steps must keep the manifest order and reasons",
                )
                # A `why` explains a position, so it is only correct next to the
                # Question the manifest put there.
                self.assertEqual(
                    [step["href"] for step in generated["steps"]],
                    [f"{step['question'].removesuffix('.md')}.html" for step in declared["steps"]],
                    "each published step must link to the Question the manifest ordered at that position",
                )

    def test_generated_steps_link_to_published_question_pages(self) -> None:
        for path in self.generated:
            for position, step in enumerate(path["steps"], start=1):
                with self.subTest(path=path["slug"], position=position):
                    self.assertTrue(step["href"].endswith(".html"), "a published step links to a rendered page")
                    self.assertTrue(step["title"].strip(), "a published step carries its Question title")
                    self.assertTrue((ROOT / step["href"]).with_suffix(".md").is_file(), "step must resolve to a Question")


if __name__ == "__main__":
    unittest.main()
