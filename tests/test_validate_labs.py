"""Prove `tests/validate_labs.py` fails on the breakage it exists to catch.

Every failure case below is produced by mutating one field of a fixture that the
same test class proves valid, so a passing assertion is evidence about the rule
under test rather than about a broken fixture.
"""

import tempfile
import unittest
from pathlib import Path

from validate_labs import (
    LABS,
    declared_themes,
    known_tags,
    lab_files,
    main,
    validate_lab,
)
from validate_learning_resources import lab_urls, load_manifest, validate_scope


VALID_LAB = """---
title: "Recover a failed systemd unit"
theme: "linux"
difficulty: "middle"
question_ref: "linux/systemd-service-failure.md"
tags: [linux, systemd, troubleshooting]
why: "A unit that fails on boot has to be diagnosed from its journal, its dependencies, and its unit file before any restart policy will hold, which is the skill this lab drills."
checklist:
  - "Inspect the failing unit with systemctl status."
  - "Read the unit journal for the first error."
  - "Add a restart policy and verify recovery."
---

# Lab: Recovering a failed unit

## Instructions
1. Inspect the unit.
"""


def lab_with(replacement: str | None = None, original: str | None = None, folder: str = "linux") -> Path:
    """Write the fixture lab into a temporary Theme folder, optionally mutated."""
    text = VALID_LAB if original is None else VALID_LAB.replace(original, replacement or "")
    directory = Path(tempfile.mkdtemp()) / folder
    directory.mkdir(parents=True)
    path = directory / "fixture-lab.md"
    path.write_text(text, encoding="utf-8")
    return path


def check(path: Path) -> dict:
    return validate_lab(path, known_tags(), declared_themes())


class LabSchemaTests(unittest.TestCase):
    def test_the_fixture_lab_is_valid(self) -> None:
        """The control: every failure below is caused by its own mutation."""
        fields = check(lab_with())
        self.assertEqual("linux", fields["theme"])
        self.assertEqual(3, len(fields["checklist"]))

    def test_missing_required_field_fails(self) -> None:
        for field, line in (
            ("why", 'why: "A unit that fails'),
            ("difficulty", 'difficulty: "middle"'),
            ("question_ref", 'question_ref: "linux/systemd-service-failure.md"'),
        ):
            with self.subTest(field=field):
                removed = VALID_LAB[VALID_LAB.index(line) : VALID_LAB.index("\n", VALID_LAB.index(line)) + 1]
                with self.assertRaisesRegex(AssertionError, "missing required front-matter fields"):
                    check(lab_with("", removed))

    def test_empty_required_field_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "required front-matter fields are empty"):
            check(lab_with('title: ""', 'title: "Recover a failed systemd unit"'))

    def test_empty_checklist_fails(self) -> None:
        emptied = "checklist:\n"
        original = VALID_LAB[VALID_LAB.index("checklist:") : VALID_LAB.index("---\n\n# Lab")]
        with self.assertRaisesRegex(AssertionError, "required front-matter fields are empty"):
            check(lab_with(emptied, original))

    def test_lab_pointing_at_a_renamed_question_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "question_ref points at a Question that does not exist"):
            check(
                lab_with(
                    'question_ref: "linux/systemd-service-failure-renamed.md"',
                    'question_ref: "linux/systemd-service-failure.md"',
                )
            )

    def test_undeclared_tag_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, r"Tags missing from TAGS.md: \['chaos'\]"):
            check(lab_with("tags: [linux, chaos]", "tags: [linux, systemd, troubleshooting]"))

    def test_undeclared_theme_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "undeclared canonical Theme"):
            check(lab_with('theme: "not-a-theme"', 'theme: "linux"', folder="not-a-theme"))

    def test_theme_must_match_its_folder(self) -> None:
        with self.assertRaisesRegex(AssertionError, "theme must match its lab folder"):
            check(lab_with('theme: "sre"', 'theme: "linux"'))

    def test_invalid_difficulty_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "invalid difficulty"):
            check(lab_with('difficulty: "intermediate"', 'difficulty: "middle"'))

    def test_short_checklist_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "at least 3 checklist steps"):
            check(lab_with("", '  - "Add a restart policy and verify recovery."\n'))

    def test_insecure_link_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "must use HTTPS"):
            check(lab_with("1. Inspect the unit at http://example.test/unit", "1. Inspect the unit."))

    def test_missing_instruction_section_fails(self) -> None:
        with self.assertRaisesRegex(AssertionError, "missing an instruction section"):
            check(lab_with("", "## Instructions\n"))


class LabCorpusTests(unittest.TestCase):
    def test_every_committed_lab_validates(self) -> None:
        labs = lab_files()
        self.assertTrue(labs, "labs/ must contain at least one lab")
        self.assertEqual(sorted(LABS.glob("*/*.md")), labs)
        for path in labs:
            with self.subTest(lab=path.name):
                check(path)

    def test_validator_entry_point_runs_over_the_repository(self) -> None:
        main()


class LabLinkAuditTests(unittest.TestCase):
    def test_lab_urls_are_collected_from_disk(self) -> None:
        urls = lab_urls()
        self.assertTrue(urls, "labs cite URLs that must be audited")
        self.assertTrue(all(url.startswith("https://") for url in urls))

    def test_lab_urls_enter_the_live_audit_scope(self) -> None:
        """A dead lab link must fail the same CI gate a dead Question link fails."""
        self.assertTrue(lab_urls() <= validate_scope(load_manifest()))


if __name__ == "__main__":
    unittest.main()
