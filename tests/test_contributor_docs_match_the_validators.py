#!/usr/bin/env python3
"""Keep the docs a contributor reads consistent with what the validators enforce.

Three defects motivated this check, each found by reading the docs against the
code rather than by any failing test:

`TEST_PLAN.md` described the Coverage target as an "exact" 25-Question mix that
in-progress Themes "may never exceed".  `CONTEXT.md`, the manifest's own
`count_semantics`, and `validate_content_manifest.py` all say the opposite --
the target is a floor.  A contributor following `TEST_PLAN.md` would have
retired verified Questions to hit a count nothing enforces.

`CONTRIBUTING.md` published a front-matter schema offering only
`junior | middle | senior`, while `validate_questions.py` accepts `staff` and
the corpus carries hundreds of staff-level Questions.  The schema a contributor
copies could not express a band the Coverage target requires.

`CONTRIBUTING.md` also said nothing about installing dependencies or running the
suite, though `CLAUDE.md` requires every agent to run local validation before
pushing.

None of these is detectable by the content validators, because none of them is
wrong about a Question -- they are wrong about the rules.  This module asserts
the prose agrees with the code it describes.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEST_PLAN = ROOT / "TEST_PLAN.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
MANIFEST = ROOT / "config" / "content-manifest.json"
VALIDATE_QUESTIONS = ROOT / "tests" / "validate_questions.py"


def allowed_difficulties() -> set[str]:
    """The difficulty vocabulary `validate_questions.py` actually enforces."""
    source = VALIDATE_QUESTIONS.read_text(encoding="utf-8")
    literal = re.search(r"^ALLOWED_DIFFICULTIES = \{([^}]*)\}", source, re.MULTILINE)
    assert literal, "validate_questions.py no longer defines ALLOWED_DIFFICULTIES as a set literal"
    return set(re.findall(r'"([^"]+)"', literal.group(1)))


def test_test_plan_does_not_describe_the_coverage_target_as_exact() -> None:
    """The manifest calls the target a floor; the test plan must not call it a cap."""
    policy = json.loads(MANIFEST.read_text(encoding="utf-8"))["theme_policy"]
    assert policy["count_semantics"] == "floor", (
        "this test encodes a floor policy; the manifest now says "
        f"{policy['count_semantics']!r} and this check needs rewriting"
    )

    prose = TEST_PLAN.read_text(encoding="utf-8")
    for forbidden in (
        r"exact\s+\d+-Question",
        r"may never exceed",
        r"enforces the exact",
    ):
        assert not re.search(forbidden, prose, re.IGNORECASE), (
            f"TEST_PLAN.md describes the Coverage target with {forbidden!r}, but "
            "config/content-manifest.json sets count_semantics to 'floor' and "
            "tests/validate_content_manifest.py enforces it. The target is a floor, not a cap."
        )

    assert "floor, not a cap" in prose, (
        "TEST_PLAN.md must state that the Coverage target is a floor, not a cap"
    )
    assert "count_semantics" in prose, (
        "TEST_PLAN.md must cite theme_policy.count_semantics as the authority rather than "
        "restating a count that can drift"
    )


def test_contributing_publishes_every_difficulty_the_validator_accepts() -> None:
    """A contributor copying the schema must be able to write any legal Question."""
    prose = CONTRIBUTING.read_text(encoding="utf-8")
    schema = re.search(r"^difficulty: (.+)$", prose, re.MULTILINE)
    assert schema, "CONTRIBUTING.md no longer publishes a difficulty line in its schema"

    published = {value.strip() for value in schema.group(1).split("|")}
    enforced = allowed_difficulties()
    assert published == enforced, (
        f"CONTRIBUTING.md offers {sorted(published)} but tests/validate_questions.py accepts "
        f"{sorted(enforced)}. Missing: {sorted(enforced - published)}; "
        f"invented: {sorted(published - enforced)}."
    )


def test_contributing_documents_how_to_run_the_checks() -> None:
    """`CLAUDE.md` requires local validation; the procedure has to be written down."""
    prose = CONTRIBUTING.read_text(encoding="utf-8")
    for required in (
        "requirements-dev.txt",
        "python -m venv",
        "pytest",
        "tests/run_all_tests.py",
        "contentdb.drift",
        "tests/site_check.py",
    ):
        assert required in prose, (
            f"CONTRIBUTING.md must document {required!r} so a contributor can reproduce CI locally"
        )

    assert "standard-library only" in prose, (
        "CONTRIBUTING.md must say which checks run without installed dependencies -- "
        "tests/test_api_dependency_separation.py enforces that separation"
    )


def main() -> None:
    test_test_plan_does_not_describe_the_coverage_target_as_exact()
    test_contributing_publishes_every_difficulty_the_validator_accepts()
    test_contributing_documents_how_to_run_the_checks()
    print("Contributor docs agree with the validators they describe.")


if __name__ == "__main__":
    main()
