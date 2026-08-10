#!/usr/bin/env python3
"""Enforce complete Theme and certification coverage for the published database.

`validate_questions.py` checks each Question and each declared Theme against the
manifest. A `complete` Theme meets the baseline coverage floor and difficulty
distribution. An `in-progress` Theme may publish a reviewed incremental slice
below that floor. Every declared certification must have a map document and
enough tagged Questions. A `planned` Theme holds no active Questions.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
MANIFEST = ROOT / "config" / "content-manifest.json"


def manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def theme_difficulties() -> dict[str, Counter]:
    counts: dict[str, Counter] = {}
    for path in sorted(QUESTIONS.glob("*/*.md")):
        difficulty = re.search(r"^difficulty:\s*(\S+)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        assert difficulty, f"{path}: missing difficulty"
        counts.setdefault(path.parent.name, Counter())[difficulty.group(1)] += 1
    return counts


def certification_counts() -> Counter:
    counts: Counter = Counter()
    for path in sorted(QUESTIONS.glob("*/*.md")):
        tags = re.search(r"^tags: \[([^\]]*)\]", path.read_text(encoding="utf-8"), re.MULTILINE)
        assert tags, f"{path}: missing tags"
        counts.update(tag.strip() for tag in tags.group(1).split(","))
    return counts


def main() -> None:
    data = manifest()
    policy = data["theme_policy"]
    floor = policy["minimum_question_count"]
    baseline = policy["minimum_difficulty_distribution"]
    counts = theme_difficulties()
    states = {theme["name"]: theme["state"] for theme in data["themes"]}

    assert set(counts) <= set(states), f"undeclared Theme folders: {sorted(set(counts) - set(states))}"

    for name, state in states.items():
        theme_counts = counts.get(name, Counter())
        total = sum(theme_counts.values())
        if state == "complete":
            assert total >= floor, f"{name}: {total} Questions is below the {floor}-Question floor"
            for difficulty, required in baseline.items():
                assert theme_counts[difficulty] >= required, (
                    f"{name}: {difficulty} has {theme_counts[difficulty]} Questions, baseline is {required}"
                )
        elif state == "in-progress":
            assert 0 < total < floor, (
                f"{name} is in-progress but has {total} Questions; use planned for zero or complete at the {floor}-Question floor"
            )
        else:
            assert total == 0, f"{name} is {state} but publishes {total} Questions"

    tagged = certification_counts()
    for certification in data["certifications"]:
        tag = certification["tag"]
        assert (ROOT / certification["map"]).is_file(), f"{tag}: missing curriculum map"
        minimum = certification["minimum_questions"]
        assert tagged[tag] >= minimum, f"{tag}: {tagged[tag]} tagged Questions is below the minimum of {minimum}"

    complete = sum(1 for state in states.values() if state == "complete")
    print(
        f"Validated complete coverage for {complete} Themes "
        f"({sum(sum(c.values()) for c in counts.values())} Questions) and {len(data['certifications'])} certifications."
    )


if __name__ == "__main__":
    main()
