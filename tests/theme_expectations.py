#!/usr/bin/env python3
"""Shared coverage expectations for per-Theme acceptance tests.

`config/content-manifest.json` states the coverage target as a floor: at least 25
active Questions with at least junior 5 / middle 10 / senior 5 / staff 5.  The
per-Theme tests were each written against an exact count of 25, so a Theme that
legitimately grew through certification or roadmap work turned its own
acceptance test red.  They call this helper instead, so the floor is defined once
and every Theme test reads the same policy the validators read.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "content-manifest.json"


def policy() -> tuple[int, dict[str, int]]:
    theme_policy = json.loads(MANIFEST.read_text(encoding="utf-8"))["theme_policy"]
    return theme_policy["minimum_question_count"], theme_policy["minimum_difficulty_distribution"]


def assert_meets_floor(theme: str, counts: Counter) -> None:
    """Fail unless the Theme's difficulty counts satisfy the manifest floor."""
    minimum_total, baseline = policy()
    total = sum(counts.values())
    assert total >= minimum_total, f"{theme}: {total} Questions is below the {minimum_total}-Question floor"
    assert not set(counts) - set(baseline), f"{theme}: undeclared difficulty band in {sorted(counts)}"
    shortfall = {band: (counts[band], required) for band, required in baseline.items() if counts[band] < required}
    assert not shortfall, f"{theme}: below the baseline difficulty mix {shortfall}"
