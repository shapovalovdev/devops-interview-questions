from pathlib import Path


def test_every_networking_question_has_learning_resources() -> None:
    questions = sorted(Path("questions/networking").glob("*.md"))
    assert len(questions) == 25
    for question in questions:
        assert "## What to learn next" in question.read_text(encoding="utf-8")
