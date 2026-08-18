"""The rules a write has to satisfy before the Content store hears about it.

This module holds three things the write surface cannot work without, and
nothing else: the **Write credential**, the **vocabularies** a record has to
draw from, and the **candidate record** a request body becomes. `api/app.py`
turns what is raised here into the contract's status codes; `api/content.py`
turns what is returned here into rows.

**Validation is the Markdown rules, and it is not restated here.** A Question
in this corpus is legal exactly when `contentdb.corpus` can read it — that is
what Ingest enforces, what the Drift gate compares against, and what a reviewer
sees in a pull request. So a proposed write is not checked against a second
list of rules written from memory. It is *rendered* to Markdown by
`contentdb.export` and *read back* by `contentdb.corpus`, and the record that
comes out of that round trip is the record that gets stored. Three things fall
out of doing it this way, and none of them would fall out of a hand-written
validator:

- a write that Export cannot render is refused instead of stored, so the store
  can never hold a record that has no Markdown form;
- the stored `content_hash` is the sha256 of the exact bytes Export will later
  write to `questions/<theme>/<slug>.md`, so after Export and Ingest run, the
  record still has the same hash — the round trip closes;
- `prompt` and `answer_guide`, which the corpus derives from the body rather
  than from front matter, are derived here too, so the API cannot publish a
  prompt that the Markdown does not actually ask.

The named checks below — Theme, tag, difficulty, type, `question_ref`, id shape
— exist on top of that round trip for one reason: to name the offending field.
A `CorpusError` says what is wrong in prose aimed at a person reading a build
log, and the contract promises a problem document that names a field. Each of
them is expressed against the *same* constant, vocabulary, or regular
expression `contentdb.corpus` uses, so there is one definition of "a known tag"
in the repository and this module borrows it rather than copying it.

**The Write credential comes from the environment, and has no default.** With
:data:`WRITE_CREDENTIAL_VARIABLE` unset — or set to whitespace, which is how a
half-configured deployment usually presents itself — the service is read-only
and every mutating request is answered `503`. Falling back to an empty string
or to a well-known development key would mean a deployment that forgot to
configure the credential is not read-only but *open*, which is the worst of the
available failures. The value is compared with `hmac.compare_digest` and is
never put in a log line, a problem document, or a response header.
"""

from __future__ import annotations

import hmac
import os
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from contentdb import corpus, export

#: Names the environment variable carrying the Write credential. Unset means
#: read-only; it never falls back to a value.
WRITE_CREDENTIAL_VARIABLE = "CONTENT_API_WRITE_KEY"

#: Names the environment variable pointing at the corpus the store was built
#: from. The Theme and tag vocabularies are read from `config/content-manifest.json`
#: and `TAGS.md` there, because neither is fully recoverable from the store:
#: the `tags` table lists only the tags the corpus *uses*, and a tag that is
#: permitted but currently unused would otherwise be rejected on write.
CORPUS_ROOT_VARIABLE = "CONTENT_API_CORPUS_ROOT"

#: The repository this package lives in, which is also the corpus root in every
#: deployment that ships the Markdown beside the service.
DEFAULT_CORPUS_ROOT = Path(__file__).resolve().parents[1]

#: `updated_at` is written in the format Ingest writes, so a record created
#: through the API and a record read from a file are the same shape to a client.
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

#: The fields a problem document may blame, per kind. `_blame` scans a
#: `CorpusError` for the first of these it mentions, so a rule this module does
#: not name individually still produces a problem document a client can act on.
QUESTION_FIELDS = (
    "theme",
    "slug",
    "title",
    "difficulty",
    "type",
    "tags",
    "sources",
    "prompt",
    "answer_guide",
    "body_markdown",
)
LAB_FIELDS = (
    "theme",
    "slug",
    "title",
    "difficulty",
    "tags",
    "question_ref",
    "why",
    "checklist",
    "body_markdown",
)

#: Where a rule breach lands when the message names no field of its own. The
#: body is the only part of a document that is carried through verbatim, so it
#: is the only part that can be wrong without a front-matter field being wrong.
DEFAULT_BLAME = "body_markdown"


class WriteRejected(ValueError):
    """A proposed write breaks a rule the corpus enforces, and names the field.

    `field` is what the contract's problem document reports, so it is a field of
    the request body a client can go and fix — never an internal name and never
    a value the client sent, because a value that was rejected has no business
    being echoed back into a log or a response.
    """

    def __init__(self, field: str, message: str):
        super().__init__(message)
        self.field = field
        self.message = message


# ------------------------------------------------------------ Write credential


def write_credential(environ: Mapping[str, str] | None = None) -> str | None:
    """The configured Write credential, or `None` when the service is read-only.

    Whitespace counts as unset. A deployment that exported an empty value meant
    to configure a credential and failed; treating that as "the credential is
    the empty string" would accept `X-API-Key:` from anyone.
    """
    environ = os.environ if environ is None else environ
    configured = environ.get(WRITE_CREDENTIAL_VARIABLE, "").strip()
    return configured or None


def credential_matches(expected: str, presented: str) -> bool:
    """Whether the presented credential is the configured one.

    `hmac.compare_digest` rather than `==`: the comparison runs on a value an
    unauthenticated client controls, and a short-circuiting comparison leaks how
    much of a guess was right through its own timing.
    """
    return hmac.compare_digest(expected.encode("utf-8"), presented.encode("utf-8"))


# -------------------------------------------------------------- Vocabularies


@dataclass(frozen=True)
class Vocabulary:
    """The Theme and tag vocabularies a write is allowed to draw from.

    Loaded once when the service starts, because both are declarations that
    change through a reviewed commit and a restart, not through a request. A
    per-request read would also mean the answer to "is this tag known?" could
    change between validating a body and storing it.
    """

    themes: Mapping[str, str]
    tags: frozenset[str]
    root: Path

    @classmethod
    def load(cls, root: Path | str | None = None, environ: Mapping[str, str] | None = None) -> "Vocabulary":
        root = Path(root) if root is not None else corpus_root(environ)
        return cls(
            themes=dict(corpus.declared_themes(root)),
            tags=frozenset(corpus.known_tags(root)),
            root=root,
        )


def corpus_root(environ: Mapping[str, str] | None = None) -> Path:
    """Where to read `TAGS.md` and `config/content-manifest.json` from."""
    environ = os.environ if environ is None else environ
    configured = environ.get(CORPUS_ROOT_VARIABLE, "").strip()
    return Path(configured) if configured else DEFAULT_CORPUS_ROOT


# ------------------------------------------------------------------ Timestamps


def timestamp(moment: datetime | None = None) -> str:
    """Now, in the format Ingest writes `updated_at` in."""
    moment = datetime.now(timezone.utc) if moment is None else moment
    return moment.astimezone(timezone.utc).strftime(TIMESTAMP_FORMAT)


# ------------------------------------------------------------------- Identity


def identity(theme: Any, slug: Any, kind: str) -> str:
    """`<theme>/<slug>`, or say which half of it is malformed.

    The shape is not restated: `contentdb.corpus.QUESTION_REF` is the pattern
    the corpus already holds every `question_ref` to, and an id is exactly the
    part of it before `.md`. Testing each half separately is only so the problem
    document can blame `theme` or `slug` rather than "the id".
    """
    theme, slug = str(theme), str(slug)
    if corpus.QUESTION_REF.match(f"{theme}/{slug}.md"):
        return f"{theme}/{slug}"
    field = "slug" if corpus.QUESTION_REF.match(f"{theme}/placeholder.md") else "theme"
    raise WriteRejected(
        field,
        f"a {kind} id reads '<theme>/<slug>' with each half lowercase letters, digits, and "
        f"hyphens, so that it names a file under {kind}s/; this one does not.",
    )


def source_path(directory: str, theme: str, slug: str) -> str:
    return f"{directory}/{theme}/{slug}.md"


# ----------------------------------------------------------- The named checks


def _known_theme(vocabulary: Vocabulary, theme: str) -> None:
    if theme not in vocabulary.themes:
        raise WriteRejected(
            "theme",
            "theme is not a canonical Theme: config/content-manifest.json declares "
            f"{len(vocabulary.themes)} Themes and this is not one of them.",
        )


def _known_tags(vocabulary: Vocabulary, tags: Sequence[str]) -> None:
    if not tags:
        raise WriteRejected("tags", "tags must list at least one tag from TAGS.md.")
    unknown = sorted(set(tags) - vocabulary.tags)
    if unknown:
        raise WriteRejected("tags", f"tags include values that TAGS.md does not define: {unknown}.")


def _one_of(field: str, value: str, allowed: Sequence[str]) -> None:
    if value not in allowed:
        raise WriteRejected(field, f"{field} must be one of {list(allowed)}.")


def _blame(error: Exception, fields: Sequence[str]) -> WriteRejected:
    """Turn a corpus or export complaint into a problem document with a field.

    The corpus reports a rule breach in prose, naming the file and the field it
    was reading. Scanning that prose for a field name is not elegant, but the
    alternative is a parallel set of rules in this module whose whole purpose
    would be to produce a label — and a second set of rules is exactly what this
    slice is meant not to grow.
    """
    message = str(error)
    field = next((name for name in fields if name in message), DEFAULT_BLAME)
    # The context prefix is the record's own `source_path`; a client that just
    # sent a theme and a slug does not need it repeated back.
    detail = message.split(": ", 1)[1] if ": " in message else message
    return WriteRejected(field, detail)


# ------------------------------------------------------- Candidate records


def _round_trip(
    candidate: Mapping[str, Any], kind: str, fields: Sequence[str], read: Any
) -> dict[str, Any]:
    """Render a candidate to Markdown and read it straight back as a record.

    This is the whole validation strategy in four lines. What comes back is what
    Ingest would produce from the file Export is going to write, which is why
    the record it returns — not the request body — is what gets stored.
    """
    try:
        document = export.render(candidate, kind)
    except export.ExportError as error:
        raise _blame(error, fields) from error
    try:
        return read(document)
    except corpus.CorpusError as error:
        raise _blame(error, fields) from error


def _derived_must_agree(payload: Mapping[str, Any], record: Mapping[str, Any], field: str) -> None:
    """Refuse a body whose derived field disagrees with the Markdown it sent.

    `prompt` and `answer_guide` are not front matter: the corpus reads them out
    of the body, so they are whatever the body says regardless of what the
    request claims. Silently overwriting the client's value would mean a `201`
    describing a Question that is not the one it asked for, so the disagreement
    is a `422` that says where the truth comes from.
    """
    supplied = payload.get(field)
    if supplied is None:
        return
    if _normalised(supplied) != _normalised(record[field]):
        raise WriteRejected(
            field,
            f"{field} is read out of body_markdown — the paragraph under the '# ' heading, and the "
            f"'- ' points under '## Answer guide' — so it cannot be set independently. The body "
            f"supplied yields a different {field}.",
        )


def _normalised(value: Any) -> Any:
    return [str(item) for item in value] if isinstance(value, (list, tuple)) else str(value)


def question_record(
    payload: Mapping[str, Any], vocabulary: Vocabulary, updated_at: str | None = None
) -> dict[str, Any]:
    """The Question record a `QuestionWrite` body becomes, or why it cannot."""
    theme, slug = str(payload.get("theme", "")), str(payload.get("slug", ""))
    identity(theme, slug, "Question")
    _known_theme(vocabulary, theme)
    _known_tags(vocabulary, list(payload.get("tags") or ()))
    _one_of("difficulty", str(payload.get("difficulty", "")), corpus.DIFFICULTIES)
    _one_of("type", str(payload.get("type", "")), corpus.QUESTION_TYPES)

    context = source_path("questions", theme, slug)
    candidate = {
        "title": payload.get("title", ""),
        "theme": theme,
        "difficulty": payload.get("difficulty", ""),
        "type": payload.get("type", ""),
        "tags": list(payload.get("tags") or ()),
        "sources": [dict(source) for source in payload.get("sources") or ()],
        "body_markdown": payload.get("body_markdown", ""),
        "source_path": context,
    }
    stamp = updated_at or timestamp()
    record = _round_trip(
        candidate,
        "question",
        QUESTION_FIELDS,
        lambda document: corpus.read_question_document(
            document, context, dict(vocabulary.themes), set(vocabulary.tags), stamp
        ),
    )
    _derived_must_agree(payload, record, "prompt")
    _derived_must_agree(payload, record, "answer_guide")
    return _listed(record)


def lab_record(
    payload: Mapping[str, Any],
    vocabulary: Vocabulary,
    question_ids: set[str],
    updated_at: str | None = None,
) -> dict[str, Any]:
    """The Lab record a `LabWrite` body becomes, or why it cannot."""
    theme, slug = str(payload.get("theme", "")), str(payload.get("slug", ""))
    identity(theme, slug, "Lab")
    _known_theme(vocabulary, theme)
    _known_tags(vocabulary, list(payload.get("tags") or ()))
    _one_of("difficulty", str(payload.get("difficulty", "")), corpus.DIFFICULTIES)

    reference = str(payload.get("question_ref", ""))
    if reference not in question_ids:
        raise WriteRejected(
            "question_ref",
            "question_ref must name a Question this Content store holds; "
            "no Question has that id.",
        )

    context = source_path("labs", theme, slug)
    candidate = {
        "title": payload.get("title", ""),
        "theme": theme,
        "difficulty": payload.get("difficulty", ""),
        "question_ref": reference,
        "tags": list(payload.get("tags") or ()),
        "why": payload.get("why", ""),
        "checklist": list(payload.get("checklist") or ()),
        "body_markdown": payload.get("body_markdown", ""),
        "source_path": context,
    }
    stamp = updated_at or timestamp()
    record = _round_trip(
        candidate,
        "lab",
        LAB_FIELDS,
        lambda document: corpus.read_lab_document(
            document, context, dict(vocabulary.themes), set(vocabulary.tags), question_ids, stamp
        ),
    )
    return _listed(record)


def _listed(record: Mapping[str, Any]) -> dict[str, Any]:
    """The corpus hands back tuples; the seam carries plain JSON-shaped data."""
    return {
        key: [dict(item) if isinstance(item, Mapping) else item for item in value]
        if isinstance(value, tuple)
        else value
        for key, value in record.items()
    }


# ----------------------------------------------------------------- Patching


#: The fields a `PATCH` may carry, per kind. `theme` and `slug` are absent on
#: purpose: they are the id, the id is in the URL, and a patch that moved a
#: record would be a create and a delete wearing one status code.
QUESTION_PATCH_FIELDS = (
    "title",
    "difficulty",
    "type",
    "tags",
    "sources",
    "prompt",
    "answer_guide",
    "body_markdown",
)
LAB_PATCH_FIELDS = ("title", "difficulty", "tags", "question_ref", "why", "checklist", "body_markdown")

#: Derived from the body rather than set, so a patch that changes the body and
#: says nothing about these must take the body's answer rather than the stored
#: one — otherwise every body edit would collide with the old prompt.
DERIVED_FIELDS = ("prompt", "answer_guide")


def merge(existing: Mapping[str, Any], changes: Mapping[str, Any], fields: Sequence[str]) -> dict[str, Any]:
    """The body a `PATCH` means: the stored record with the supplied fields on top.

    `changes` holds only what the client actually sent — FastAPI's
    `exclude_unset` — so a field left out keeps its stored value and a field set
    to `null` is not silently treated as "unchanged" by this function; the
    models reject a null where the contract requires a value.
    """
    merged = {field: existing[field] for field in fields if field in existing}
    merged.update({field: value for field, value in changes.items() if field in fields})
    merged["theme"] = existing["theme"]
    merged["slug"] = existing["slug"]
    for field in DERIVED_FIELDS:
        if field in merged and field not in changes:
            del merged[field]
    return merged
