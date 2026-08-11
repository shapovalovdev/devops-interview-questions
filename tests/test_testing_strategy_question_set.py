"""Focused acceptance checks for GitHub issue #83's testing-strategy Theme.

The Theme shipped complete but unregistered in the link-audit manifest, so its
curated links were never live-checked and could rot silently — the failure mode
that left four dead URLs published in the logging Theme.  These checks assert
both halves: the Theme's shape, and the manifest registration that puts it in
`validate_learning_resources.py --check-live` scope.
"""

from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402

THEME = "testing-strategy"
QUESTIONS = ROOT / "questions" / THEME
RELATED = ROOT / "docs" / "related-materials" / f"{THEME}.md"
AUDIT_MANIFEST = ROOT / "docs" / "research" / "link-audit-manifest.json"
CONTENT_MANIFEST = ROOT / "config" / "content-manifest.json"


def test_testing_strategy_set_is_complete_and_source_verified() -> None:
    counts = Counter()
    for question in sorted(QUESTIONS.glob("*.md")):
        fields, _ = validate_question(question, known_tags())
        assert fields["theme"] == THEME
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor(THEME, counts)


def test_testing_strategy_related_materials_has_five_curated_links() -> None:
    assert RELATED.is_file(), f"{RELATED} is required by the learning-resource schema"
    assert len(resource_links(RELATED.read_text(encoding="utf-8"), str(RELATED))) == 5


def test_testing_strategy_is_declared_complete() -> None:
    themes = {theme["name"]: theme for theme in json.loads(CONTENT_MANIFEST.read_text(encoding="utf-8"))["themes"]}
    assert themes[THEME]["state"] == "complete", f"{THEME} must be declared complete"


def test_every_testing_strategy_question_is_registered_for_live_link_checks() -> None:
    """Without this the Theme's links never reach the --check-live gate."""
    audited = json.loads(AUDIT_MANIFEST.read_text(encoding="utf-8"))["audited_questions"]
    registered = {
        item["question"]: item["related_materials"]
        for item in audited
        if item["question"].startswith(f"questions/{THEME}/")
    }
    expected = {f"questions/{THEME}/{path.name}" for path in QUESTIONS.glob("*.md")}
    assert set(registered) == expected, f"unregistered {THEME} Questions: {sorted(expected - set(registered))}"
    assert set(registered.values()) == {f"docs/related-materials/{THEME}.md"}


def test_testing_strategy_maintainer_links_name_an_individual() -> None:
    """The maintainer slot must credit a person, not an anonymous publication."""
    paths = sorted(QUESTIONS.glob("*.md")) + [RELATED]
    for path in paths:
        links = dict(
            (category.strip().lower(), url)
            for category, url in resource_links(path.read_text(encoding="utf-8"), str(path))
        )
        maintainer = links["maintainer or personal blog"]
        line = next(
            line
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith("- Maintainer or personal blog:")
        )
        title = line.split("[", 1)[1].split("]", 1)[0]
        author = title.split(" — ", 1)[0]
        assert " — " in title and len(author.split()) >= 2, (
            f"{path}: maintainer link must be titled 'Author — topic', got {title!r}"
        )
        assert maintainer.startswith("https://"), f"{path}: maintainer link must be HTTPS"


def test_testing_strategy_covers_its_curriculum() -> None:
    """Issue #83 named the topics this Theme has to reach; keep them present."""
    required = {
        "test-pyramid-boundaries",
        "unit-test-design",
        "integration-test-boundaries",
        "end-to-end-test-scope",
        "contract-testing-boundaries",
        "test-data-management",
        "test-data-isolation",
        "ephemeral-test-environments",
        "shared-test-environment-policy",
        "flaky-test-quarantine-policy",
        "test-coverage-signal",
        "performance-tests-in-ci",
        "shadow-traffic-testing",
        "release-gate-design",
        "quality-investment-portfolio",
    }
    present = {path.stem for path in QUESTIONS.glob("*.md")}
    assert required <= present, f"missing curriculum Questions: {sorted(required - present)}"
