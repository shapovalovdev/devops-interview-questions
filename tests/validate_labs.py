#!/usr/bin/env python3
"""Validate every hands-on lab under `labs/` against the repository catalogs.

**A lab is published.**  `scripts/generate_question_catalog.py` writes every
lab into `window.labs` in `assets/questions.js`, publishing its `title`,
`theme`, `difficulty`, `tags`, `why`, `slug`, and the title and href of the
Question it prepares for.  `assets/site.js` renders that array twice: as the
standalone Labs view (`#labs-view`), and as a per-Theme "Hands-on labs" panel
(`#theme-labs`).  A lab's prose is public on the same terms as a Question's.

This docstring used to say the opposite — that a lab "is not listed in
`assets/questions.js` and does not appear in the site navigation".  Both halves
were false, and the cost was not cosmetic: because this file is what a
maintainer reads to learn what a lab *is*, nobody treated lab prose as public
content, and six labs shipped naming four companies and the author's own job
search.  `tests/test_labs_carry_no_personal_references.py` now guards the
content; `test_the_docstring_matches_reality` below guards this claim.

A lab also carries structured front matter that points into the Question
corpus, the Theme list, and the Tag vocabulary, so it can rot exactly the way an
unchecked Question can — a renamed Question leaves `question_ref` dangling, and
a tag invented in a lab never reaches `TAGS.md`.

This validator holds labs to the catalog rules the Question corpus already
obeys.  Lab URLs are audited for liveness by
`tests/validate_learning_resources.py`, which reads `labs/` directly so a new
lab cannot be published outside the audit.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
QUESTIONS = ROOT / "questions"
MANIFEST = ROOT / "config" / "content-manifest.json"
ALLOWED_DIFFICULTIES = {"junior", "middle", "senior", "staff"}
REQUIRED_SCALARS = ("title", "theme", "difficulty", "question_ref", "why")
REQUIRED_LISTS = ("tags", "checklist")
MINIMUM_CHECKLIST_STEPS = 3
MINIMUM_WHY_WORDS = 15
QUESTION_REF = re.compile(r"^[a-z0-9-]+/[a-z0-9-]+\.md$")
TAG = re.compile(r"[a-z0-9-]+")


def declared_themes() -> set[str]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {theme["name"] for theme in manifest["themes"]}


def known_tags() -> set[str]:
    text = (ROOT / "TAGS.md").read_text(encoding="utf-8")
    return set(re.findall(r"`([a-z0-9-]+)`", text))


def lab_files() -> list[Path]:
    return sorted(LABS.glob("*/*.md"))


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def front_matter(text: str, context: str) -> dict[str, object]:
    """Parse the small YAML subset labs use: scalars, an inline list, and a block list.

    Written for labs rather than reused from `validate_questions.py`, whose
    parser deliberately skips indented lines: a lab's `checklist` lives entirely
    in those lines, and dropping them would let an empty checklist pass.
    """
    lines = text.splitlines()
    assert lines and lines[0] == "---", f"{context}: front matter must begin with ---"
    assert "---" in lines[1:], f"{context}: front matter must be closed with ---"
    end = lines.index("---", 1)
    fields: dict[str, object] = {}
    open_list: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith("  - "):
            assert open_list, f"{context}: list item outside any front-matter field"
            fields[open_list].append(unquote(line.strip()[2:].strip()))  # type: ignore[union-attr]
            continue
        assert not line.startswith(" "), f"{context}: unsupported indented front matter: {line!r}"
        assert ":" in line, f"{context}: front-matter line is not a field: {line!r}"
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        assert key not in fields, f"{context}: duplicate front-matter field {key}"
        if not value:
            fields[key] = []
            open_list = key
        elif value.startswith("[") and value.endswith("]"):
            fields[key] = TAG.findall(value)
            open_list = None
        else:
            fields[key] = unquote(value)
            open_list = None
    return fields


def validate_lab(path: Path, tags: set[str], themes: set[str]) -> dict[str, object]:
    context = str(path.relative_to(ROOT)) if ROOT in path.parents else str(path)
    text = path.read_text(encoding="utf-8")
    fields = front_matter(text, context)

    missing = [name for name in REQUIRED_SCALARS + REQUIRED_LISTS if name not in fields]
    assert not missing, f"{context}: missing required front-matter fields {missing}"
    empty = [name for name in REQUIRED_SCALARS + REQUIRED_LISTS if not fields[name]]
    assert not empty, f"{context}: required front-matter fields are empty {empty}"
    for name in REQUIRED_SCALARS:
        assert isinstance(fields[name], str), f"{context}: {name} must be a single value"
    for name in REQUIRED_LISTS:
        assert isinstance(fields[name], list), f"{context}: {name} must be a list"

    theme = fields["theme"]
    assert theme == path.parent.name, f"{context}: theme must match its lab folder, got {theme}"
    assert theme in themes, f"{context}: undeclared canonical Theme {theme}"
    assert fields["difficulty"] in ALLOWED_DIFFICULTIES, f"{context}: invalid difficulty {fields['difficulty']}"

    reference = fields["question_ref"]
    assert QUESTION_REF.match(reference), f"{context}: question_ref must be '<theme>/<question>.md', got {reference}"
    assert (QUESTIONS / reference).is_file(), (
        f"{context}: question_ref points at a Question that does not exist: questions/{reference}"
    )

    lab_tags = set(fields["tags"])
    unknown_tags = sorted(lab_tags - tags)
    assert not unknown_tags, f"{context}: uses Tags missing from TAGS.md: {unknown_tags}"

    checklist = fields["checklist"]
    assert len(checklist) >= MINIMUM_CHECKLIST_STEPS, (
        f"{context}: a lab needs at least {MINIMUM_CHECKLIST_STEPS} checklist steps, got {len(checklist)}"
    )
    assert all(step.strip() for step in checklist), f"{context}: every checklist step must be written out"

    why_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", fields["why"])
    assert len(why_words) >= MINIMUM_WHY_WORDS, (
        f"{context}: why must explain what the lab teaches in at least {MINIMUM_WHY_WORDS} words"
    )

    body = text.split("\n---\n", 1)[-1]
    assert re.search(r"^# .+", body, re.MULTILINE), f"{context}: missing a lab title heading"
    assert re.search(r"^## .+", body, re.MULTILINE), f"{context}: missing an instruction section"
    insecure = re.findall(r"http://[^\s`\"'()<>]+", text)
    assert not insecure, f"{context}: lab links must use HTTPS, got {insecure}"
    return fields


def main() -> None:
    labs = lab_files()
    assert labs, "No labs found under labs/"
    tags = known_tags()
    themes = declared_themes()
    referenced: set[str] = set()
    for path in labs:
        fields = validate_lab(path, tags, themes)
        referenced.add(fields["question_ref"])  # type: ignore[arg-type]
    print(f"Validated {len(labs)} labs referencing {len(referenced)} active Questions.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
