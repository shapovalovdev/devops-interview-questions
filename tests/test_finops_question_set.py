"""Focused acceptance checks for GitHub issue #79's FinOps Questions."""

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import load_manifest, resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402

THEME = "finops"
QUESTIONS = ROOT / "questions" / THEME


def test_finops_set_is_complete_and_source_verified() -> None:
    tags = known_tags()
    counts: Counter = Counter()
    for question in sorted(QUESTIONS.glob("*.md")):
        fields, _ = validate_question(question, tags)
        assert fields["theme"] == THEME
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor(THEME, counts)


def test_finops_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / f"{THEME}.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5


def test_every_finops_question_is_registered_for_the_link_audit() -> None:
    audited = {
        item["question"]
        for item in load_manifest()["audited_questions"]
        if item["question"].startswith(f"questions/{THEME}/")
    }
    expected = {path.relative_to(ROOT).as_posix() for path in QUESTIONS.glob("*.md")}
    assert audited == expected, f"{THEME}: link-audit manifest is out of step with the Question folder"


def test_finops_is_declared_complete_and_registered_in_the_catalog() -> None:
    import json

    manifest = json.loads((ROOT / "config" / "content-manifest.json").read_text(encoding="utf-8"))
    states = {theme["name"]: theme["state"] for theme in manifest["themes"]}
    assert states[THEME] == "complete", f"{THEME} must be declared complete once it meets the floor"

    catalog = (ROOT / "assets" / "questions.js").read_text(encoding="utf-8")
    for path in sorted(QUESTIONS.glob("*.md")):
        entry = path.relative_to(ROOT).with_suffix(".html").as_posix()
        assert f'"path": "{entry}"' in catalog, f"{entry} is missing from the website catalog"


def test_finops_is_mapped_in_the_roadmap_coverage_table() -> None:
    roadmap = (ROOT / "ROADMAP_COVERAGE.md").read_text(encoding="utf-8")
    assert f"`{THEME}`" in roadmap, f"{THEME} must appear in ROADMAP_COVERAGE.md"


def test_finops_does_not_restate_reserved_cross_theme_questions() -> None:
    reserved = {
        "Establish cloud cost governance",
        "Build a CI/CD cost and capacity model",
        "Plan service capacity",
    }
    titles = set()
    for path in sorted(QUESTIONS.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("title: "):
                titles.add(line.removeprefix("title: ").strip())
                break
    assert not titles & reserved, f"{THEME} restates a Question owned by another Theme: {sorted(titles & reserved)}"
    assert len(titles) == len(list(QUESTIONS.glob("*.md"))), f"{THEME}: duplicate Question titles"
