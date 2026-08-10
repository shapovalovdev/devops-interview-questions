"""Focused contract tests for the Systems Performance Theme (issue #64)."""

from collections import Counter
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "questions" / "systems-performance"
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402


def test_systems_performance_has_targeted_distribution_and_original_prompts() -> None:
    files = sorted(THEME.glob("*.md"))
    difficulties = Counter(re.search(r"^difficulty: (.+)$", path.read_text(), re.MULTILINE).group(1) for path in files)
    assert_meets_floor("systems-performance", difficulties)
    text = "\n".join(path.read_text() for path in files).lower()
    assert "use method" in text
    assert "pressure stall" in text
    assert "brendan gregg" in text


def test_systems_performance_questions_include_verification_and_learning_material() -> None:
    for path in THEME.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "source_type: " in text
        assert "verified_on: 2026-08-06" in text
        assert "## References" in text
        assert re.search(r"Further reading \((?:personal )?blog\):", text)
        section = text.split("## What to learn next", 1)[1]
        assert len(re.findall(r"^- [^:]+: \[[^]]+\]\(https://", section, re.MULTILINE)) == 5


def test_systems_performance_materials_do_not_reintroduce_audited_stale_or_blocked_urls() -> None:
    """Keep the issue #65 repair list from silently returning to this Theme."""
    text = "\n".join(path.read_text(encoding="utf-8") for path in THEME.glob("*.md"))
    known_bad = (
        "blogs.oracle.com/linux/",
        "community.intel.com/",
        "sre.google/workbook/addressing-cascading-failures/",
        "sre.google/workbook/load-balancing-frontend/",
        "www.uber.com/blog/engineering/",
        "www.etsy.com/codeascraft",
        "netflixtechblog.com/",
        "www.redhat.com/en/blog/channel/performance",
        "www.brendangregg.com/blog/2014-09-11/",
        "www.brendangregg.com/blog/2015-02-10/",
        "www.brendangregg.com/blog/2015-05-15/",
        "www.brendangregg.com/blog/2015-12-03/linux-perf-analysis-in-60s.html",
        "www.brendangregg.com/blog/2016-03-07/",
        "www.brendangregg.com/blog/2016-09-01/",
        "www.brendangregg.com/blog/2018-01-18/",
        "www.brendangregg.com/blog/2018-08-31/",
        "www.brendangregg.com/blog/2019-11-13/",
    )
    assert not any(url in text for url in known_bad)

    related = (ROOT / "docs" / "related-materials" / "systems-performance.md").read_text(encoding="utf-8")
    assert "## Legal free books" in related
    assert "https://sre.google/sre-book/table-of-contents/" in related
    assert "https://sre.google/workbook/table-of-contents/" in related
