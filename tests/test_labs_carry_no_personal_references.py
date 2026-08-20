#!/usr/bin/env python3
"""Keep named employers and personal job-search detail out of the published corpus.

Six of the eleven Labs shipped with their `why` field written as a note to the
author's own job hunt: four named companies, counts like "four of the eight
analyzed vacancies", and a line describing the author's own CV.  All of it was
live on the public CC BY site, because every Lab's `why` is copied verbatim into
`window.labs` in `assets/questions.js` and rendered by the Labs view.

`tests/validate_labs.py` did not catch it, and could not have: it checks that a
Lab's front matter points at real Themes, Tags, and Questions, which this
content did.  The defect was never structural.  It was that a Lab said who the
author was interviewing with.

Six of the eleven were also written in Russian, while none of the 1,100
Questions contains a single Cyrillic character.  #191 settled that Labs are
corpus material on the same terms as Questions, so #197 translated them and
`test_labs_are_written_in_english` keeps them that way.

This module holds Labs to the same neutrality the 1,100 Questions already keep,
and checks the **generated catalog** as well as the sources — the catalog is
what the site actually serves, and it regenerates independently, so a source fix
that is never regenerated leaves the published copy exposed.  That happened
while this check was being written.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
CATALOG = ROOT / "assets" / "questions.js"

#: Companies that appeared by name in Lab prose. Kept explicit rather than
#: inferred: a general "does this look like a company name" check would be
#: unreliable, and these are the ones that actually leaked.
NAMED_EMPLOYERS = ("interlizing", "efin", "ostrovok")

#: Phrasings that mark a Lab as a note to one person's job search rather than
#: corpus material a stranger can use.
PERSONAL_FRAMINGS = (
    r"\bvacanc(?:y|ies)\b",
    r"\b(?:eight|seven|six|five|four|three)\s+(?:of\s+the\s+\w+\s+)?(?:analyzed|current|target)\b",
    r"\bjob requirement\b",
    r"\bA candidate with\b",
    r"\bmy (?:CV|resume|experience)\b",
)


def lab_sources() -> dict[Path, str]:
    return {path: path.read_text(encoding="utf-8") for path in sorted(LABS.glob("*/*.md"))}


def published_labs() -> list[dict]:
    """The Lab records the site actually serves, from the generated catalog."""
    text = CATALOG.read_text(encoding="utf-8")
    block = re.search(r"window\.labs = (\[.*?\]);", text, re.DOTALL)
    assert block, "assets/questions.js no longer publishes window.labs"
    return json.loads(block.group(1))


#: Any character in the Cyrillic block or its supplement. A Lab is corpus
#: material on a public English-language site, so a single one of these is a
#: regression rather than a style question.
CYRILLIC = re.compile(r"[\u0400-\u04FF\u0500-\u052F]")


def _offences(haystack: str) -> list[str]:
    found = []
    for employer in NAMED_EMPLOYERS:
        if re.search(rf"\b{employer}\b", haystack, re.IGNORECASE):
            found.append(f"names the employer {employer!r}")
    for pattern in PERSONAL_FRAMINGS:
        match = re.search(pattern, haystack, re.IGNORECASE)
        if match:
            found.append(f"personal job-search framing: {match.group(0)!r}")
    return found


def test_lab_sources_name_no_employer_and_no_job_search() -> None:
    failures = []
    for path, text in lab_sources().items():
        for offence in _offences(text):
            failures.append(f"  {path.relative_to(ROOT)}: {offence}")
    assert not failures, (
        "Labs are published corpus material on a public CC BY site. These name a "
        "specific employer or read as one person's job-search notes:\n"
        + "\n".join(failures)
        + "\n\nRewrite the claim generically -- what the topic is worth knowing for, "
        "not who asked about it."
    )


def test_labs_are_written_in_english() -> None:
    """No Lab source may carry Cyrillic text.

    The check is deliberately crude -- it counts characters rather than
    detecting a language -- because the failure it guards is crude too: six
    Labs shipped in Russian on a public English-language site, carrying between
    2,236 and 3,972 Cyrillic characters each.  A character count cannot be
    argued with, and it costs nothing to run.
    """
    failures = []
    for path, text in lab_sources().items():
        found = CYRILLIC.findall(text)
        if found:
            failures.append(
                f"  {path.relative_to(ROOT)}: {len(found)} Cyrillic characters, "
                f"first at {text.index(found[0])}"
            )
    assert not failures, (
        "Labs are published corpus material on an English-language site, and none of the 1,100 "
        "Questions contains Cyrillic. These do:\n" + "\n".join(failures)
    )


def test_the_published_catalog_is_english_too() -> None:
    """The catalog is what the site serves, and it regenerates separately."""
    failures = []
    for record in published_labs():
        blob = " ".join(str(value) for value in record.values())
        found = CYRILLIC.findall(blob)
        if found:
            failures.append(f"  {record.get('title', '<untitled>')[:60]}: {len(found)} Cyrillic characters")
    assert not failures, (
        "assets/questions.js still publishes Cyrillic Lab text:\n" + "\n".join(failures)
        + "\n\nRegenerate it with: python scripts/generate_question_catalog.py"
    )


def test_the_published_catalog_is_clean_too() -> None:
    """The catalog is what the site serves, and it regenerates separately.

    A source fix that is never followed by
    `python scripts/generate_question_catalog.py` leaves the exposed text live.
    """
    failures = []
    for record in published_labs():
        blob = " ".join(str(value) for value in record.values())
        for offence in _offences(blob):
            failures.append(f"  {record.get('title', '<untitled>')[:60]}: {offence}")
    assert not failures, (
        "assets/questions.js still publishes employer or job-search references:\n"
        + "\n".join(failures)
        + "\n\nRegenerate it with: python scripts/generate_question_catalog.py"
    )


def test_questions_stay_clean_as_well() -> None:
    """The 1,100 Questions have always been neutral. Keep it that way."""
    failures = []
    for path in sorted((ROOT / "questions").glob("*/*.md")):
        for offence in _offences(path.read_text(encoding="utf-8")):
            failures.append(f"  {path.relative_to(ROOT)}: {offence}")
    assert not failures, "Questions must stay employer-neutral:\n" + "\n".join(failures)


def main() -> None:
    test_lab_sources_name_no_employer_and_no_job_search()
    test_labs_are_written_in_english()
    test_the_published_catalog_is_english_too()
    test_the_published_catalog_is_clean_too()
    test_questions_stay_clean_as_well()
    labs = published_labs()
    print(
        f"Checked {len(lab_sources())} Lab sources and {len(labs)} published Lab records: "
        "neutral and English."
    )


if __name__ == "__main__":
    main()
