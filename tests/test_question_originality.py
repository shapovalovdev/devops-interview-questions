#!/usr/bin/env python3
"""Catch boilerplate Questions that pass every structural check.

A Question can satisfy `validate_questions.py` completely — front-matter sources,
a long-enough answer guide, References, a blog link, five curated learning links
— and still say nothing. Three Themes were once built by stamping the same prompt
and the same answer-guide bullets across every file: 19 `testing-strategy`
Questions literally asked "How should a team make this testing strategy
decision?", three `caching` Questions shared one generic prompt, and all 25
`performance-engineering` Questions shared two identical bullets.

Structure validators cannot see that, so this test checks distinctiveness
directly:

* a Question's prompt must not be reused by another Question;
* an answer-guide bullet must not appear in more than `MAX_SHARED_BULLET`
  Questions.

All 53 files were rewritten under issues #102 and #103, so the gate is now
unconditional: there is no allowlist to add a new exception to.
"""

from __future__ import annotations

import collections
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
MAX_SHARED_BULLET = 2
MIN_BULLET_LENGTH = 40


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


def test_no_boilerplate_questions() -> None:
    new = sorted(offenders())
    assert not new, (
        "These Questions reuse another Question's prompt or share an answer-guide bullet with "
        f"more than {MAX_SHARED_BULLET} Questions. Write the specific question and a specific "
        f"answer instead of restating the Theme:\n" + "\n".join(new)
    )




def main() -> None:
    test_no_boilerplate_questions()
    print(f"Validated that {len(list(QUESTIONS.glob('*/*.md')))} Questions each ask something distinct.")


if __name__ == "__main__":
    main()
