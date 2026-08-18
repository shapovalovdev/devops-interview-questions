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

import sys
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


# -- Writing ---------------------------------------------------------------

SAFE_ROOTS = ("questions", "labs")
PAGE = 200


def target(root: Path, source_path: str) -> Path:
    """Resolve a record's `source_path` to a file it is allowed to write.

    A `source_path` is data: it arrives from a store row, and a store row can
    arrive from an API write.  So it is validated rather than trusted — the only
    acceptable shapes are `questions/<theme>/<slug>.md` and
    `labs/<theme>/<slug>.md`, and the resolved path must still sit inside the
    repository.  Anything else is refused, which is what stops `../../etc/…`
    from becoming a write.
    """
    parts = Path(source_path).parts
    if (
        len(parts) != 3
        or parts[0] not in SAFE_ROOTS
        or not parts[2].endswith(".md")
        or any(part in ("", ".", "..") for part in parts)
    ):
        raise ExportError(
            f"refusing to export {source_path!r}: expected questions/<theme>/<slug>.md "
            "or labs/<theme>/<slug>.md"
        )
    resolved = (root / source_path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ExportError(f"refusing to export {source_path!r}: it resolves outside {root}")
    return resolved


def write(root: Path, record: Mapping[str, object], kind: str) -> bool:
    """Render one record to its source file. True when the file changed.

    Unchanged files are left alone rather than rewritten, so Export is
    idempotent and a second run produces no diff for git to show.
    """
    path = target(root, str(record["source_path"]))
    rendered = render(record, kind)
    if path.exists() and path.read_text(encoding="utf-8") == rendered:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    return True


def export(store, root: Path) -> tuple[int, int]:
    """Write every Question and Lab in `store` back to `root`.

    Returns `(written, unchanged)`.
    """
    from contentdb.models import LabQuery, QuestionQuery

    written = unchanged = 0
    for kind, lister, query in (
        ("question", store.list_questions, QuestionQuery),
        ("lab", store.list_labs, LabQuery),
    ):
        offset = 0
        while True:
            page = lister(query(limit=PAGE, offset=offset))
            for record in page.items:
                if write(root, record, kind):
                    written += 1
                else:
                    unchanged += 1
            offset += len(page.items)
            if not page.items or offset >= page.total:
                break
    return written, unchanged



def main(argv: list[str] | None = None) -> int:
    import argparse

    from contentdb.store import Store

    parser = argparse.ArgumentParser(
        prog="python -m contentdb.export",
        description="Render every Content store record back to its Markdown source file.",
    )
    parser.add_argument("--database", type=Path, default=Path("build/content.db"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root to write questions/ and labs/ into (default: this repository)",
    )
    arguments = parser.parse_args(argv)
    try:
        opened = Store(arguments.database)
    except FileNotFoundError as error:
        print(f"Export failed: {error}", file=sys.stderr)
        return 1
    try:
        written, unchanged = export(opened, arguments.output)
    except ExportError as error:
        print(f"Export failed: {error}", file=sys.stderr)
        return 1
    finally:
        opened.close()
    print(f"Exported {written + unchanged} files: {written} written, {unchanged} already current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
