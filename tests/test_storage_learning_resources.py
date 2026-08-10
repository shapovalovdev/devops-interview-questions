from pathlib import Path


def test_storage_learning_resources_are_present() -> None:
    questions = list(Path("questions/storage").glob("*.md"))
    assert len(questions) == 25
    assert all("## What to learn next" in question.read_text(encoding="utf-8") for question in questions)
