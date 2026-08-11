"""Focused acceptance checks for GitHub issue #78's chaos-engineering Questions."""

import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import load_manifest, resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402

THEME = "chaos-engineering"
QUESTIONS = ROOT / "questions" / THEME


def test_chaos_engineering_set_is_complete_and_source_verified() -> None:
    tags = known_tags()
    counts: Counter = Counter()
    for question in sorted(QUESTIONS.glob("*.md")):
        fields, _ = validate_question(question, tags)
        assert fields["theme"] == THEME
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor(THEME, counts)


def test_chaos_engineering_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / f"{THEME}.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5


def test_every_chaos_engineering_question_is_registered_for_the_link_audit() -> None:
    audited = {
        item["question"]
        for item in load_manifest()["audited_questions"]
        if item["question"].startswith(f"questions/{THEME}/")
    }
    expected = {path.relative_to(ROOT).as_posix() for path in QUESTIONS.glob("*.md")}
    assert audited == expected, f"{THEME}: link-audit manifest is out of step with the Question folder"


def test_chaos_engineering_is_declared_complete_and_registered_in_the_catalog() -> None:
    manifest = json.loads((ROOT / "config" / "content-manifest.json").read_text(encoding="utf-8"))
    states = {theme["name"]: theme["state"] for theme in manifest["themes"]}
    assert states[THEME] == "complete", f"{THEME} must be declared complete once it meets the floor"

    catalog = (ROOT / "assets" / "questions.js").read_text(encoding="utf-8")
    for path in sorted(QUESTIONS.glob("*.md")):
        entry = path.relative_to(ROOT).with_suffix(".html").as_posix()
        assert f'"path": "{entry}"' in catalog, f"{entry} is missing from the website catalog"


def test_chaos_engineering_covers_the_required_experiment_lifecycle() -> None:
    """Every stage of an experiment must be represented, not only fault injection.

    A Theme can reach the numeric floor while covering only the easy half of the
    practice, so pin the stages an interview actually probes: hypothesis and
    steady state, blast-radius control and aborting, the fault classes
    themselves, game days, and the programme-level judgement calls.
    """
    corpus = "\n".join(path.read_text(encoding="utf-8").lower() for path in sorted(QUESTIONS.glob("*.md")))
    for concept in (
        "steady-state hypothesis",
        "blast radius",
        "stop condition",
        "packet loss",
        "partition",
        "game day",
        "availability zone",
        "consent",
        "error budget",
    ):
        assert concept in corpus, f"{THEME} does not cover {concept}"


def test_chaos_engineering_does_not_restate_neighbouring_theme_questions() -> None:
    neighbours = {"sre", "distributed-systems", "troubleshooting"}
    reserved = set()
    for theme in neighbours:
        for path in sorted((ROOT / "questions" / theme).glob("*.md")):
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith("title: "):
                    reserved.add(line.removeprefix("title: ").strip())
                    break

    titles = []
    for path in sorted(QUESTIONS.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("title: "):
                titles.append(line.removeprefix("title: ").strip())
                break

    overlap = set(titles) & reserved
    assert not overlap, f"{THEME} restates a neighbouring Theme's Question: {sorted(overlap)}"
    assert len(set(titles)) == len(titles), f"{THEME}: duplicate Question titles"
