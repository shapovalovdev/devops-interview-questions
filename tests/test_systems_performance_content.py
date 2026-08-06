"""Focused contract tests for the Systems Performance Theme (issue #64)."""

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "questions" / "systems-performance"


def test_systems_performance_has_targeted_distribution_and_original_prompts() -> None:
    files = sorted(THEME.glob("*.md"))
    assert len(files) == 25
    difficulties = Counter(re.search(r"^difficulty: (.+)$", path.read_text(), re.MULTILINE).group(1) for path in files)
    assert difficulties == {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
    text = "\n".join(path.read_text() for path in files).lower()
    assert "use method" in text
    assert "pressure stall" in text
    assert "brendan gregg" in text


def test_systems_performance_questions_include_verification_and_learning_material() -> None:
    for path in THEME.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "source_type: " in text
        assert "verified_on: 2026-08-06" in text
        assert "## References" in text and "Further reading (blog):" in text
        section = text.split("## What to learn next", 1)[1]
        assert len(re.findall(r"^- [^:]+: \[[^]]+\]\(https://", section, re.MULTILINE)) == 5
