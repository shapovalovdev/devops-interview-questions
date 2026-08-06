"""Focused acceptance checks for GitHub issue #31's backend-architecture Theme."""

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402


def test_backend_architecture_set_is_complete_and_source_verified() -> None:
    questions = sorted((ROOT / "questions" / "backend-architecture").glob("*.md"))
    assert len(questions) == 25
    counts = Counter()
    for question in questions:
        fields, _ = validate_question(question, known_tags())
        assert fields["theme"] == "backend-architecture"
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert counts == {"junior": 5, "middle": 10, "senior": 5, "staff": 5}


def test_backend_architecture_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / "backend-architecture.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5
