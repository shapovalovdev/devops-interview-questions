"""The one front-matter parser the Content store agrees on.

This is the YAML-subset parser proven in `tests/validate_labs.py` and
`scripts/generate_question_catalog.py`, factored out and extended with the one
shape those callers never see: a block list of mappings, which Question
``sources`` uses (``- url:`` / ``source_type:`` / ``verified_on:``).  The
existing callers keep their own copies of the scalar-and-block-list subset and
are unaffected; new code parses Markdown front matter through here instead of
growing a third dialect.

Supported shapes, and nothing else:

- scalars, optionally quoted: ``title: "A title"``
- inline lists: ``tags: [kubernetes, security]``
- block lists of scalars::

      checklist:
        - "Step one"
        - "Step two"

- block lists of mappings::

      sources:
        - url: https://example.com
          source_type: official-docs
          verified_on: 2026-08-06

Failures raise :class:`FrontMatterError` naming the file and the offending
line, so a caller can fail loudly instead of silently skipping a document.
"""

from __future__ import annotations

import re

LIST_ITEM_FIELD = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$")
INLINE_LIST_TOKEN = re.compile(r"[a-z0-9-]+")


class FrontMatterError(ValueError):
    """Raised when a document's front matter cannot be parsed."""


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _front_matter_lines(text: str, context: str) -> tuple[list[str], int]:
    """Return the front-matter lines and the index of the closing ``---``."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontMatterError(f"{context}: front matter must begin with ---")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise FrontMatterError(f"{context}: front matter must be closed with ---") from error
    return lines, end


def parse(text: str, context: str = "<memory>") -> dict[str, object]:
    """Parse front matter into scalars, lists of scalars, and lists of mappings."""
    lines, end = _front_matter_lines(text, context)
    fields: dict[str, object] = {}
    open_list: str | None = None
    open_item: dict[str, str] | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith("  - "):
            if open_list is None:
                raise FrontMatterError(f"{context}: list item outside any front-matter field: {line!r}")
            open_item = None
            raw = line.strip()[2:].strip()
            match = LIST_ITEM_FIELD.match(raw)
            if match:
                open_item = {match.group(1): _unquote(match.group(2).strip())}
                fields[open_list].append(open_item)  # type: ignore[union-attr]
            else:
                fields[open_list].append(_unquote(raw))  # type: ignore[union-attr]
        elif line.startswith("    ") and open_item is not None:
            match = LIST_ITEM_FIELD.match(line.strip())
            if not match:
                raise FrontMatterError(f"{context}: unsupported mapping-item line: {line!r}")
            open_item[match.group(1)] = _unquote(match.group(2).strip())
        elif line.startswith(" "):
            raise FrontMatterError(f"{context}: unsupported indented front matter: {line!r}")
        else:
            key, separator, value = line.partition(":")
            if not separator:
                raise FrontMatterError(f"{context}: front-matter line is not a field: {line!r}")
            key, value = key.strip(), value.strip()
            if key in fields:
                raise FrontMatterError(f"{context}: duplicate front-matter field {key}")
            open_list = None
            open_item = None
            if not value:
                fields[key] = []
                open_list = key
            elif value.startswith("[") and value.endswith("]"):
                fields[key] = INLINE_LIST_TOKEN.findall(value)
            else:
                fields[key] = _unquote(value)
    return fields


def split(text: str, context: str = "<memory>") -> tuple[dict[str, object], str]:
    """Parse front matter and return ``(fields, body_markdown)``.

    The body is everything after the closing ``---``, with the newline that
    closed the front matter consumed, mirroring the ``text.split("\\n---\\n", 1)``
    idiom the existing validators use.
    """
    lines, end = _front_matter_lines(text, context)
    return parse(text, context), "\n".join(lines[end + 1 :])
