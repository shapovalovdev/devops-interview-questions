"""Acceptance checks for GitHub issue #71's observability learning resources.

Every active observability Question must parse under the curated-resource schema
and must be registered in the link-audit manifest alongside the Theme's
related-materials page.
"""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_learning_resources import REQUIRED_CATEGORIES, resource_links  # noqa: E402

THEME = "observability"
RELATED_MATERIALS = f"docs/related-materials/{THEME}.md"


def observability_questions() -> list[Path]:
    questions = sorted((ROOT / "questions" / THEME).glob("*.md"))
    assert questions, "no observability Questions found"
    return questions


def manifest_entries() -> dict[str, str]:
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text(encoding="utf-8"))
    return {item["question"]: item["related_materials"] for item in manifest["audited_questions"]}


def test_every_observability_question_has_five_curated_links() -> None:
    for question in observability_questions():
        links = resource_links(question.read_text(encoding="utf-8"), str(question))
        assert len(links) == 5
        assert {category.strip().lower() for category, _ in links} == REQUIRED_CATEGORIES
        assert len({url for _, url in links}) == 5


def test_observability_related_materials_page_is_curated() -> None:
    related = ROOT / RELATED_MATERIALS
    assert related.is_file(), f"missing {RELATED_MATERIALS}"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5


def test_every_observability_question_is_registered_in_the_manifest() -> None:
    entries = manifest_entries()
    for question in observability_questions():
        key = str(question.relative_to(ROOT))
        assert key in entries, f"{key} is missing from the link-audit manifest"
        assert entries[key] == RELATED_MATERIALS, f"{key} points at {entries[key]}"


if __name__ == "__main__":
    failures = 0
    for name, test in sorted(dict(globals()).items()):
        if not name.startswith("test_") or not callable(test):
            continue
        try:
            test()
        except AssertionError as error:
            failures += 1
            print(f"FAIL {name}: {error}", file=sys.stderr)
        else:
            print(f"ok {name}")
    raise SystemExit(1 if failures else 0)
