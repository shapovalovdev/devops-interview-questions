"""Render Content store records back into the Markdown corpus.

Export is Ingest run backwards, and it exists to keep the promise ADR 0001
makes: Markdown in git stays the durable, reviewable record of content, even
though the Content API can write.  A write that only ever lived in the store
would bypass content policy, source verification, and review; Export is what
turns it back into a file a human can read in a pull request.

Reproducing a file byte for byte is possible because Ingest keeps
``body_markdown`` verbatim — everything below the closing ``---`` — so only the
front matter has to be re-rendered.  The corpus makes that tractable by being
uniform, which was measured rather than assumed:

- all 1100 Questions carry exactly ``title, theme, difficulty, type, tags,
  sources``, with plain unquoted scalars, an inline ``tags`` list, and a
  ``sources`` block whose every entry has all three of ``url``,
  ``source_type``, ``verified_on``;
- all 11 Labs carry exactly ``title, theme, difficulty, question_ref, tags,
  why, checklist``, with double-quoted scalars, an inline ``tags`` list, and a
  block ``checklist`` of quoted steps;
- every file ends with a newline, none contains CRLF, no title contains ``:``
  and no quoted value contains an embedded quote.

Those uniformities are the renderer's contract, so it asserts them instead of
guessing: a record that cannot be rendered exactly raises rather than writing an
approximation.  If the corpus ever grows a shape this module does not know, the
right fix is to teach the renderer, never to reshape the corpus to match it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping

QUESTION_FIELDS = ("title", "theme", "difficulty", "type", "tags", "sources")
LAB_FIELDS = ("title", "theme", "difficulty", "question_ref", "tags", "why", "checklist")
SOURCE_FIELDS = ("url", "source_type", "verified_on")


class ExportError(ValueError):
    """Raised when a record cannot be rendered back to its Markdown source."""


def _plain(value: object, field: str, context: str) -> str:
    """A scalar written bare, as Questions write theirs."""
    text = str(value)
    if ": " in text or text != text.strip():
        raise ExportError(f"{context}: {field} would not survive as a plain scalar: {text!r}")
    return text


def _quoted(value: object, field: str, context: str) -> str:
    """A scalar written in double quotes, as Labs write theirs."""
    text = str(value)
    if '"' in text:
        raise ExportError(f"{context}: {field} contains a quote this renderer cannot escape: {text!r}")
    return f'"{text}"'


def _inline_list(values: Iterable[str]) -> str:
    return "[" + ", ".join(values) + "]"


def _document(front_matter: list[str], body: str) -> str:
    """Assemble a corpus file: front matter, the verbatim body, one final newline.

    `frontmatter.split` drops the newline that ended the file, because
    `splitlines` does; putting exactly one back is what makes the round trip
    exact for a corpus in which every file is newline-terminated.
    """
    return "---\n" + "\n".join(front_matter) + "\n---\n" + body + "\n"


def render_question(record: Mapping[str, object]) -> str:
    """Render one Question record as the Markdown file it came from."""
    context = str(record.get("source_path", record.get("id", "<unknown Question>")))
    lines = [
        f"title: {_plain(record['title'], 'title', context)}",
        f"theme: {_plain(record['theme'], 'theme', context)}",
        f"difficulty: {_plain(record['difficulty'], 'difficulty', context)}",
        f"type: {_plain(record['type'], 'type', context)}",
        f"tags: {_inline_list(str(tag) for tag in record['tags'])}",
        "sources:",
    ]
    for source in record["sources"]:
        missing = [field for field in SOURCE_FIELDS if not source.get(field)]
        if missing:
            raise ExportError(f"{context}: source is missing {', '.join(missing)}")
        lines.append(f"  - url: {source['url']}")
        lines.append(f"    source_type: {source['source_type']}")
        lines.append(f"    verified_on: {source['verified_on']}")
    return _document(lines, str(record["body_markdown"]))


def render_lab(record: Mapping[str, object]) -> str:
    """Render one Lab record as the Markdown file it came from.

    `question_ref` crosses the seam as a Question `id`, because the epic pins it
    that way; the corpus writes it as a path, so the `.md` goes back on here.
    """
    context = str(record.get("source_path", record.get("id", "<unknown Lab>")))
    lines = [
        f"title: {_quoted(record['title'], 'title', context)}",
        f"theme: {_quoted(record['theme'], 'theme', context)}",
        f"difficulty: {_quoted(record['difficulty'], 'difficulty', context)}",
        f"question_ref: {_quoted(str(record['question_ref']) + '.md', 'question_ref', context)}",
        f"tags: {_inline_list(str(tag) for tag in record['tags'])}",
        f"why: {_quoted(record['why'], 'why', context)}",
        "checklist:",
    ]
    for step in record["checklist"]:
        lines.append(f"  - {_quoted(step, 'checklist step', context)}")
    return _document(lines, str(record["body_markdown"]))


def render(record: Mapping[str, object], kind: str) -> str:
    if kind == "question":
        return render_question(record)
    if kind == "lab":
        return render_lab(record)
    raise ExportError(f"unknown record kind {kind!r}; expected 'question' or 'lab'")
