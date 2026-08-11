#!/usr/bin/env python3
"""Catch boilerplate Questions that pass every structural check.

A Question can satisfy `validate_questions.py` completely — front-matter sources,
a long-enough answer guide, References, a blog link, five curated learning links
— and still say nothing. Three Themes were built by stamping the same prompt and
the same answer-guide bullets across every file: 19 `testing-strategy` Questions
literally ask "How should a team make this testing strategy decision?", and all
25 `performance-engineering` Questions share two identical bullets.

Structure validators cannot see that, so this test checks distinctiveness
directly:

* a Question's prompt must not be reused by another Question;
* an answer-guide bullet must not appear in more than `MAX_SHARED_BULLET`
  Questions.

`KNOWN_BOILERPLATE` is the recorded backlog of files that already fail, so this
gate blocks *new* boilerplate today instead of waiting for the rewrite. It is
allowed to shrink and never to grow: an entry that no longer fails must be
deleted, and the test enforces that too, so the debt cannot be quietly retained.
"""

from __future__ import annotations

import collections
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
MAX_SHARED_BULLET = 2
MIN_BULLET_LENGTH = 40

# Tracked by the Question-rewrite issue. Remove entries as they are rewritten.
KNOWN_BOILERPLATE = {
    "questions/caching/cache-aside-basics.md",
    "questions/caching/cache-consistency-tradeoffs.md",
    "questions/caching/cache-invalidation-policy.md",
    "questions/performance-engineering/benchmark-control-variables.md",
    "questions/performance-engineering/benchmark-production-safety.md",
    "questions/performance-engineering/cache-performance-evaluation.md",
    "questions/performance-engineering/capacity-baseline-design.md",
    "questions/performance-engineering/capacity-economics-governance.md",
    "questions/performance-engineering/cross-team-performance-contracts.md",
    "questions/performance-engineering/define-performance-objectives.md",
    "questions/performance-engineering/load-shedding-design.md",
    "questions/performance-engineering/multi-tenant-noisy-neighbor.md",
    "questions/performance-engineering/performance-budget-api.md",
    "questions/performance-engineering/performance-investment-portfolio.md",
    "questions/performance-engineering/performance-observability-strategy.md",
    "questions/performance-engineering/performance-regression-ci.md",
    "questions/performance-engineering/resilience-performance-tradeoffs.md",
    "questions/performance-engineering/select-load-test-model.md",
    "questions/testing-strategy/accessibility-test-strategy.md",
    "questions/testing-strategy/consumer-driven-contracts.md",
    "questions/testing-strategy/contract-testing-boundaries.md",
    "questions/testing-strategy/end-to-end-test-scope.md",
    "questions/testing-strategy/ephemeral-test-environments.md",
    "questions/testing-strategy/flaky-test-quarantine-policy.md",
    "questions/testing-strategy/integration-test-boundaries.md",
    "questions/testing-strategy/integration-test-data-contract.md",
    "questions/testing-strategy/mutation-testing-tradeoffs.md",
    "questions/testing-strategy/performance-tests-in-ci.md",
    "questions/testing-strategy/production-experiment-guardrails.md",
    "questions/testing-strategy/quality-investment-portfolio.md",
    "questions/testing-strategy/release-gate-design.md",
    "questions/testing-strategy/security-test-boundaries.md",
    "questions/testing-strategy/shadow-traffic-testing.md",
    "questions/testing-strategy/shared-test-environment-policy.md",
    "questions/testing-strategy/test-case-naming.md",
    "questions/testing-strategy/test-coverage-signal.md",
    "questions/testing-strategy/test-data-isolation.md",
    "questions/testing-strategy/test-data-management.md",
    "questions/testing-strategy/test-observability.md",
    "questions/testing-strategy/test-pyramid-boundaries.md",
    "questions/testing-strategy/test-suite-execution-policy.md",
    "questions/testing-strategy/test-suite-ownership.md",
    "questions/testing-strategy/unit-test-design.md",
}


def prompt_of(text: str) -> str:
    """The Question itself: everything between the title and the answer guide."""
    body = text.split("---", 2)[2]
    match = re.search(r"^# .+?$\n(.*?)^## Answer guide", body, re.S | re.MULTILINE)
    return " ".join(match.group(1).split()) if match else ""


def answer_bullets(text: str) -> list[str]:
    if "## Answer guide" not in text:
        return []
    guide = text.split("## Answer guide")[1].split("##")[0]
    return [line.strip() for line in guide.splitlines() if line.strip().startswith("- ") and len(line.strip()) > MIN_BULLET_LENGTH]


def offenders() -> set[str]:
    prompts: dict[str, list[str]] = collections.defaultdict(list)
    bullets: dict[str, list[str]] = collections.defaultdict(list)
    for path in sorted(QUESTIONS.glob("*/*.md")):
        name = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        prompt = prompt_of(text)
        if prompt:
            prompts[prompt].append(name)
        for bullet in answer_bullets(text):
            bullets[bullet].append(name)

    failing: set[str] = set()
    for files in prompts.values():
        if len(files) > 1:
            failing.update(files)
    for files in bullets.values():
        if len(files) > MAX_SHARED_BULLET:
            failing.update(files)
    return failing


def test_no_new_boilerplate_questions() -> None:
    new = sorted(offenders() - KNOWN_BOILERPLATE)
    assert not new, (
        "These Questions reuse another Question's prompt or share an answer-guide bullet with "
        f"more than {MAX_SHARED_BULLET} Questions. Write the specific question and a specific "
        f"answer instead of restating the Theme:\n" + "\n".join(new)
    )


def test_known_boilerplate_list_only_shrinks() -> None:
    fixed = sorted(KNOWN_BOILERPLATE - offenders())
    assert not fixed, (
        "These Questions are no longer boilerplate. Delete them from KNOWN_BOILERPLATE so the "
        "backlog cannot silently retain fixed entries:\n" + "\n".join(fixed)
    )


def main() -> None:
    test_no_new_boilerplate_questions()
    test_known_boilerplate_list_only_shrinks()
    print(f"Validated Question distinctiveness; {len(KNOWN_BOILERPLATE)} Questions remain on the rewrite backlog.")


if __name__ == "__main__":
    main()
