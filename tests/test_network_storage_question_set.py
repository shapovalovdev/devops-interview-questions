"""Focused regression checks for GitHub issue #33's Network Storage Questions."""

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402


def test_network_storage_set_has_distribution_and_verified_learning_materials() -> None:
    questions = sorted((ROOT / "questions" / "network-storage").glob("*.md"))
    assert len(questions) == 25
    counts = Counter()
    for question in questions:
        fields, _ = validate_question(question, known_tags())
        counts[fields["difficulty"]] += 1
        references = question.read_text(encoding="utf-8").split("## References", 1)[1]
        assert len([line for line in references.splitlines() if line.startswith("- ")]) >= 5
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert counts == {"junior": 5, "middle": 10, "senior": 5, "staff": 5}


def test_network_storage_related_materials_follow_learning_resource_schema() -> None:
    related = ROOT / "docs" / "related-materials" / "network-storage.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5
