"""Validate the declarative coverage contract before validating Question content."""

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "content-manifest.json"
LABS = ROOT / "labs"
ALLOWED_STATES = {"complete", "in-progress", "planned"}

#: A Theme either carries Lab coverage or has not got there yet. `in-progress`
#: is deliberately not offered: a Theme has a Lab or it does not, and a third
#: state would only be somewhere to park a Theme that fails the floor.
ALLOWED_LAB_STATES = {"complete", "planned"}


def load_manifest() -> dict:
    assert MANIFEST.is_file(), "config/content-manifest.json is required"
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def lab_counts() -> Counter:
    """How many Labs each Theme actually carries on disk."""
    return Counter(path.parent.name for path in LABS.glob("*/*.md"))


def check_lab_coverage(policy: dict, themes: list[dict]) -> None:
    """Hold declared Lab coverage to the floor, in both directions.

    A Theme that declares `labs: complete` must carry at least the floor, so
    coverage cannot regress once claimed. A Theme that carries Labs must declare
    them, so coverage cannot appear undeclared either -- which is the direction
    that would otherwise let the manifest quietly stop describing the corpus.

    Themes that declare `planned` are *reported*, not failed. Thirty of the
    forty carry no Lab today; failing them would make this check red from the
    day it lands, and a check that is red on arrival is one everybody learns to
    skip. The gap is printed instead, so it stays visible without blocking.
    """
    floor = policy["minimum_labs_per_theme"]
    counts = lab_counts()

    short = [
        f"{theme['name']} declares labs: complete but carries {counts.get(theme['name'], 0)}"
        for theme in themes
        if theme["labs"] == "complete" and counts.get(theme["name"], 0) < floor
    ]
    assert not short, (
        f"these Themes fall below the Lab floor of {floor}: {short}. Either restore the Lab or "
        "set the Theme's labs state back to 'planned' deliberately."
    )

    declared = {theme["name"] for theme in themes if theme["labs"] == "complete"}
    undeclared = sorted(set(counts) - declared)
    assert not undeclared, (
        f"these Themes carry Labs but do not declare them: {undeclared}. Set labs: complete in "
        "config/content-manifest.json, so the manifest keeps describing the corpus."
    )

    unknown = sorted(set(counts) - {theme["name"] for theme in themes})
    assert not unknown, f"labs/ contains folders that are not declared Themes: {unknown}"


def main() -> None:
    manifest = load_manifest()
    assert manifest["schema_version"] == 2, "content manifest must use schema version 2"
    policy = manifest["theme_policy"]
    distribution = policy["minimum_difficulty_distribution"]
    assert set(distribution) == {"junior", "middle", "senior", "staff"}, "theme distribution must define every difficulty"
    assert sum(distribution.values()) == policy["minimum_question_count"], "difficulty distribution must total the minimum"
    assert policy["count_semantics"] == "floor", "theme counts are a floor, never an exact cap"
    assert policy["rationale"].strip(), "the count policy must record why it is a floor"

    labs = manifest["lab_policy"]
    assert labs["minimum_labs_per_theme"] > 0, "the Lab floor must be positive"
    assert labs["count_semantics"] == "floor", "Lab counts are a floor, never an exact cap"
    assert labs["enforcement"] == "declared-themes-only", (
        "the Lab floor is enforced only where a Theme declares coverage; see the rationale"
    )
    assert labs["rationale"].strip(), "the Lab policy must record why it is enforced this way"

    themes = manifest["themes"]
    names = [theme["name"] for theme in themes]
    assert names == sorted(names), "themes must be sorted by canonical name"
    assert len(names) == len(set(names)), "themes must not be duplicated"
    assert all(theme["state"] in ALLOWED_STATES for theme in themes), "themes must use a supported state"
    assert all(theme.get("labs") in ALLOWED_LAB_STATES for theme in themes), (
        "every Theme must declare a Lab state: 'complete' if it carries Labs, 'planned' if not"
    )

    check_lab_coverage(labs, themes)

    certifications = manifest["certifications"]
    tags = [certification["tag"] for certification in certifications]
    assert tags == sorted(tags), "certifications must be sorted by tag"
    assert len(tags) == len(set(tags)), "certification tags must not be duplicated"
    assert not set(names) & set(tags), "certifications are tags, never canonical Themes"
    for certification in certifications:
        assert certification["minimum_questions"] > 0, "certification minimum must be positive"
        assert (ROOT / certification["map"]).is_file(), f"missing certification map: {certification['map']}"

    declared = sum(1 for theme in themes if theme["labs"] == "complete")
    print(
        f"Validated manifest for {len(themes)} Themes and {len(certifications)} certifications; "
        f"{declared} Themes declare Lab coverage, {len(themes) - declared} do not."
    )


if __name__ == "__main__":
    main()
