"""Focused acceptance checks for GitHub issue #82's serverless Questions."""

import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402

THEME = "serverless"
QUESTIONS = ROOT / "questions" / THEME


def test_serverless_set_is_complete_and_source_verified() -> None:
    questions = sorted(QUESTIONS.glob("*.md"))
    counts: Counter = Counter()
    tags = known_tags()
    for question in questions:
        fields, _ = validate_question(question, tags)
        assert fields["theme"] == THEME
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor(THEME, counts)


def test_serverless_theme_is_declared_complete() -> None:
    manifest = json.loads((ROOT / "config" / "content-manifest.json").read_text(encoding="utf-8"))
    states = {theme["name"]: theme["state"] for theme in manifest["themes"]}
    assert states[THEME] == "complete"


def test_serverless_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / f"{THEME}.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5


def test_every_serverless_question_is_registered_for_link_audit() -> None:
    manifest = json.loads((ROOT / "docs" / "research" / "link-audit-manifest.json").read_text(encoding="utf-8"))
    audited = {
        item["question"]
        for item in manifest["audited_questions"]
        if item["related_materials"] == f"docs/related-materials/{THEME}.md"
    }
    expected = {question.relative_to(ROOT).as_posix() for question in sorted(QUESTIONS.glob("*.md"))}
    assert audited == expected


def test_serverless_covers_the_required_curriculum_topics() -> None:
    corpus = "\n".join(question.read_text(encoding="utf-8").lower() for question in sorted(QUESTIONS.glob("*.md")))
    for topic in (
        "cold start",
        "concurrency",
        "idempot",
        "timeout",
        "connection",
        "package",
        "trac",
        "cost",
        "least-privilege",
        "vpc",
        "workflow",
    ):
        assert topic in corpus, f"serverless must cover {topic}"


def main() -> None:
    test_serverless_set_is_complete_and_source_verified()
    test_serverless_theme_is_declared_complete()
    test_serverless_related_materials_has_five_curated_links()
    test_every_serverless_question_is_registered_for_link_audit()
    test_serverless_covers_the_required_curriculum_topics()
    print(f"Validated the {THEME} Theme's shape.")


if __name__ == "__main__":
    main()
