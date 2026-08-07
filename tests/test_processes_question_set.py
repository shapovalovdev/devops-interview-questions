"""Focused regression checks for GitHub issue #58's Processes Question set."""

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402


def test_processes_question_set_has_expected_distribution_and_learning_materials() -> None:
    questions = sorted((ROOT / "questions" / "processes").glob("*.md"))
    counts = Counter()
    for question in questions:
        fields, _ = validate_question(question, known_tags())
        counts[fields["difficulty"]] += 1
        references = question.read_text(encoding="utf-8").split("## References", 1)[1]
        assert len([line for line in references.splitlines() if line.startswith("- ")]) >= 5
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor("processes", counts)


def test_processes_related_materials_follow_learning_resource_schema() -> None:
    related = ROOT / "docs" / "related-materials" / "processes.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5
