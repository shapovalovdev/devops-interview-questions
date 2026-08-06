"""Validate the declarative coverage contract before validating Question content."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "content-manifest.json"
ALLOWED_STATES = {"complete", "in-progress", "planned"}


def load_manifest() -> dict:
    assert MANIFEST.is_file(), "config/content-manifest.json is required"
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def main() -> None:
    manifest = load_manifest()
    assert manifest["schema_version"] == 2, "content manifest must use schema version 2"
    policy = manifest["theme_policy"]
    distribution = policy["minimum_difficulty_distribution"]
    assert set(distribution) == {"junior", "middle", "senior", "staff"}, "theme distribution must define every difficulty"
    assert sum(distribution.values()) == policy["minimum_question_count"], "difficulty distribution must total the minimum"
    assert policy["count_semantics"] == "floor", "theme counts are a floor, never an exact cap"
    assert policy["rationale"].strip(), "the count policy must record why it is a floor"

    themes = manifest["themes"]
    names = [theme["name"] for theme in themes]
    assert names == sorted(names), "themes must be sorted by canonical name"
    assert len(names) == len(set(names)), "themes must not be duplicated"
    assert all(theme["state"] in ALLOWED_STATES for theme in themes), "themes must use a supported state"

    certifications = manifest["certifications"]
    tags = [certification["tag"] for certification in certifications]
    assert tags == sorted(tags), "certifications must be sorted by tag"
    assert len(tags) == len(set(tags)), "certification tags must not be duplicated"
    assert not set(names) & set(tags), "certifications are tags, never canonical Themes"
    for certification in certifications:
        assert certification["minimum_questions"] > 0, "certification minimum must be positive"
        assert (ROOT / certification["map"]).is_file(), f"missing certification map: {certification['map']}"

    print(f"Validated manifest for {len(themes)} Themes and {len(certifications)} certifications.")


if __name__ == "__main__":
    main()
