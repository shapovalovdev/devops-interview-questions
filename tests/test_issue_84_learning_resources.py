"""Acceptance coverage for #84's fully audited learning-resource Themes."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from validate_learning_resources import resource_links  # noqa: E402

THEMES = ("troubleshooting", "processes", "logging", "web-servers")


def test_issue_84_questions_are_schema_valid_and_registered() -> None:
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text(encoding="utf-8"))
    entries = {item["question"]: item["related_materials"] for item in manifest["audited_questions"]}
    for theme in THEMES:
        related = ROOT / "docs/related-materials" / f"{theme}.md"
        assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5
        for question in sorted((ROOT / "questions" / theme).glob("*.md")):
            key = str(question.relative_to(ROOT))
            assert entries.get(key) == str(related.relative_to(ROOT))
            assert len(resource_links(question.read_text(encoding="utf-8"), key)) == 5
