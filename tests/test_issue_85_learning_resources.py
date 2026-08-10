"""Acceptance checks for #85's audited learning-resource Theme scope."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_learning_resources import resource_links  # noqa: E402

THEMES = ("version-control", "distributed-systems", "network-storage", "service-mesh")


def test_issue_85_themes_are_fully_registered_and_parse() -> None:
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text(encoding="utf-8"))
    entries = {item["question"]: item["related_materials"] for item in manifest["audited_questions"]}

    for theme in THEMES:
        related = ROOT / "docs" / "related-materials" / f"{theme}.md"
        assert related.is_file(), f"missing related materials for {theme}"
        assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5

        questions = sorted((ROOT / "questions" / theme).glob("*.md"))
        assert questions, f"no Questions for {theme}"
        for question in questions:
            key = str(question.relative_to(ROOT))
            assert entries.get(key) == str(related.relative_to(ROOT)), f"{key} is not audited"
            assert len(resource_links(question.read_text(encoding="utf-8"), key)) == 5

