"""Focused contract tests for Linux troubleshooting content (issue #60)."""

from collections import Counter
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "questions" / "linux-troubleshooting"
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402


def test_linux_troubleshooting_has_required_distribution_and_core_topics() -> None:
    files = sorted(THEME.glob("*.md"))
    difficulties = Counter(
        re.search(r"^difficulty: (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE).group(1)
        for path in files
    )
    assert_meets_floor("linux-troubleshooting", difficulties)
    text = "\\n".join(path.read_text(encoding="utf-8") for path in files).lower()
    for topic in ("oom", "systemd", "nfs", "conntrack", "kernel panic", "runbook"):
        assert topic in text


def test_linux_troubleshooting_questions_have_sources_answers_and_learning_links() -> None:
    for path in THEME.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "source_type: official-docs" in text
        assert "verified_on: 2026-08-06" in text
        assert text.count("- ") >= 10
        assert "## References" in text and "Further reading (blog):" in text
        section = text.split("## What to learn next", 1)[1]
        assert len(re.findall(r"^- [^:]+: \[[^]]+\]\(https://", section, re.MULTILINE)) == 5
