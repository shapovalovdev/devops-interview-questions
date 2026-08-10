"""Targeted acceptance checks for GitHub issue #32's Distributed Systems theme."""

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402


def test_distributed_systems_set_is_complete_and_source_verified() -> None:
    questions = sorted((ROOT / "questions" / "distributed-systems").glob("*.md"))
    counts = Counter()
    for question in questions:
        fields, _ = validate_question(question, known_tags())
        assert fields["theme"] == "distributed-systems"
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor("distributed-systems", counts)


def test_distributed_systems_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / "distributed-systems.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5
