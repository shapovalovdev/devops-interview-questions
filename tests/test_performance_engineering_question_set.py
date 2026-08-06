"""Focused acceptance checks for issue #62 performance-engineering Questions."""

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "questions" / "performance-engineering"


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    end = lines.index("---", 1)
    return {
        key: value
        for line in lines[1:end]
        if ": " in line and not line.startswith("  ")
        for key, value in [line.split(": ", 1)]
    }


def test_performance_engineering_has_the_25_question_distribution() -> None:
    questions = sorted(THEME.glob("*.md"))
    assert len(questions) == 25
    assert Counter(front_matter(path)["difficulty"] for path in questions) == {
        "junior": 5,
        "middle": 10,
        "senior": 5,
        "staff": 5,
    }


def test_performance_engineering_questions_are_source_verified_and_teach_next_steps() -> None:
    for path in THEME.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert front_matter(path)["theme"] == "performance-engineering"
        assert "source_type: official-docs" in text
        assert "verified_on: 2026-08-06" in text
        assert "Further reading (blog):" in text
        answer = text.split("## Answer guide", 1)[1].split("## References", 1)[0]
        assert len(re.findall(r"^- ", answer, re.MULTILINE)) >= 3
        assert len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", answer)) >= 60
        learning = text.split("## What to learn next", 1)[1]
        assert len(re.findall(r"^- [^:]+: \[[^]]+\]\(https://", learning, re.MULTILINE)) == 5
