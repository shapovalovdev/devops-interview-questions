"""Read the Markdown corpus into validated records, or refuse to read it at all.

This module owns everything that is true about the corpus before SQLite is
involved: which fields a Question carries, which vocabularies it has to draw
from, where its `prompt` and `answer_guide` live in the body, and what a Lab's
`question_ref` points at.  :mod:`contentdb.ingest` only moves the result into a
database, so the rules are testable without touching a file.

Three decisions are worth explaining, because none of them is forced:

**Failure is loud and total.** A corpus reader that skips the file it cannot
parse reports a plausible count for an incomplete store, and the missing
Question is discovered by a learner rather than by CI.  Every problem raises
:class:`CorpusError` naming the file and the field, and Ingest stops.  This is
also why front-matter failures are re-raised as `CorpusError`: one exception
type crosses out of this module, so no caller can catch the narrow one and
carry on.

**`prompt` falls back to the heading.** The epic pins `prompt` as "the question
itself".  Most Questions state it as a paragraph under the `#` heading, but
seventy-five of them ask it in the heading and go straight to the answer guide.
Those are not malformed, so the heading text becomes the prompt rather than
Ingest failing or storing an empty string.

**`updated_at` is the source file's git commit time, in UTC.** The issue allows
a fixed value instead, but `updated_at` is published by the Content API and a
constant would make it a lie.  Commit times are read in one batched `git log`
pass and are a pure function of the checked-out history, so two runs agree.
Where git cannot answer — no repository, as in a Docker build, or a file not
yet committed — the value falls back to :data:`UNTRACKED_UPDATED_AT`, which
keeps the build deterministic in that environment too.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from . import frontmatter


DIFFICULTIES = ("junior", "middle", "senior", "staff")
QUESTION_TYPES = ("theory", "scenario", "troubleshooting")
QUESTION_REF = re.compile(r"^([a-z0-9-]+/[a-z0-9-]+)\.md$")
TAG_IN_TAGS_MD = re.compile(r"`([a-z0-9-]+)`")
HEADING = re.compile(r"^# (.+)$", re.MULTILINE)
SECTION = re.compile(r"^## ", re.MULTILINE)
ANSWER_GUIDE_HEADING = "## Answer guide"
BULLET = re.compile(r"^- (.+)$", re.MULTILINE)
UNTRACKED_UPDATED_AT = "1970-01-01T00:00:00Z"


class CorpusError(ValueError):
    """Raised when a corpus file cannot be read, or breaks a catalog rule."""


@dataclass(frozen=True)
class Corpus:
    """Everything Ingest needs, already validated and in a deterministic order."""

    themes: tuple[dict, ...]
    tags: tuple[dict, ...]
    questions: tuple[dict, ...]
    labs: tuple[dict, ...]
    learning_paths: tuple[dict, ...]


def content_digest(corpus: Corpus) -> str:
    """The corpus-wide content digest, computed by a pinned recipe.

    Take every Question and every Lab the corpus holds; for each, form the
    line ``f"{id} {content_hash}\\n"``; sort the lines lexicographically by
    ``id``; concatenate them; return the sha256 of the UTF-8 bytes. The recipe
    is order-independent (the sort), total (one changed byte in one file moves
    the digest), and covers Questions and Labs together.

    It is duplicated on purpose: `contentdb` may not import `api/`, and
    `api/store.py` may import nothing outside the standard library, so the
    seam carries its own copy for the in-memory store to stand in with, and
    `tests/api/test_meta.py` pins the two implementations to the same answer
    over the same records. The recipe is also published in
    `api/openapi.yaml`, so a downstream consumer can recompute the digest from
    the API's own listing endpoints and verify a snapshot.
    """
    pairs = sorted(
        (str(record["id"]), str(record["content_hash"]))
        for record in (*corpus.questions, *corpus.labs)
    )
    material = "".join(f"{identifier} {content_hash}\n" for identifier, content_hash in pairs)
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def known_tags(root: Path) -> set[str]:
    """The Tag vocabulary, read the way the existing validators read it."""
    text = (root / "TAGS.md").read_text(encoding="utf-8")
    return set(TAG_IN_TAGS_MD.findall(text))


def declared_themes(root: Path) -> dict[str, str]:
    """Canonical Theme name to state, from the content manifest."""
    manifest = json.loads((root / "config" / "content-manifest.json").read_text(encoding="utf-8"))
    return {theme["name"]: theme["state"] for theme in manifest["themes"]}


def commit_times(root: Path) -> dict[str, str]:
    """Map each tracked corpus path to its latest commit time, in UTC.

    One `git log` pass rather than one per file: the corpus is over a thousand
    documents, and a subprocess each would dominate the build.  Unix timestamps
    (`%ct`) are asked for instead of an ISO string so the result cannot pick up
    the running machine's timezone.
    """
    try:
        toplevel = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        if Path(toplevel).resolve() != root.resolve():
            # `root` is not the repository top level, so `git log` would report
            # paths relative to a different directory.  Rather than guess, let
            # every file fall back.
            return {}
        completed = subprocess.run(
            ["git", "-C", str(root), "log", "--pretty=format:%x00%ct", "--name-only", "--no-renames",
             "--", "questions", "labs"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return {}

    times: dict[str, str] = {}
    stamp: str | None = None
    for line in completed.stdout.splitlines():
        if line.startswith("\x00"):
            stamp = datetime.fromtimestamp(int(line[1:]), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        elif line.strip() and stamp is not None:
            # `git log` walks newest first, so the first mention of a path wins.
            times.setdefault(line.strip(), stamp)
    return times


def _context(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _parse_document(text: str, context: str) -> tuple[dict[str, object], str, str]:
    """Front matter, body, and content hash for one corpus *document*.

    The rules below apply to the text of a document, not to a file, which is
    what lets the Content API run them on a candidate record before anything is
    stored: slice 4 renders a proposed write through :mod:`contentdb.export` and
    reads the result back through here, so a write is validated by the same code
    that validates the corpus rather than by a second copy of the rules that
    could drift away from it.

    The hash is taken over the UTF-8 encoding of `text`, which is byte for byte
    the file Export writes, so a record read here carries the `content_hash`
    Ingest would compute after that file is committed.
    """
    try:
        fields, body = frontmatter.split(text, context)
    except frontmatter.FrontMatterError as error:
        raise CorpusError(str(error)) from error
    return fields, body, hashlib.sha256(text.encode("utf-8")).hexdigest()


def _document_text(path: Path, context: str) -> str:
    """One corpus file as text, or a `CorpusError` saying it is not readable."""
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as error:
        raise CorpusError(f"{context}: file is not valid UTF-8") from error


def _scalar(fields: dict[str, object], name: str, context: str) -> str:
    value = fields.get(name)
    if value is None:
        raise CorpusError(f"{context}: missing required front-matter field {name}")
    if not isinstance(value, str) or not value.strip():
        raise CorpusError(f"{context}: front-matter field {name} must be a non-empty single value")
    return value.strip()


def _string_list(fields: dict[str, object], name: str, context: str) -> tuple[str, ...]:
    value = fields.get(name)
    if value is None:
        raise CorpusError(f"{context}: missing required front-matter field {name}")
    if not isinstance(value, list) or not value:
        raise CorpusError(f"{context}: front-matter field {name} must be a non-empty list")
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise CorpusError(
                f"{context}: every item of {name} must be a written-out value, got {item!r} "
                f"(a list item reading `- key: value` parses as a mapping — quote it)"
            )
    return tuple(item.strip() for item in value)


def _one_of(value: str, allowed: tuple[str, ...], name: str, context: str) -> str:
    if value not in allowed:
        raise CorpusError(f"{context}: {name} must be one of {list(allowed)}, got {value!r}")
    return value


def _theme(fields: dict[str, object], folder: str, themes: dict[str, str], context: str) -> str:
    theme = _scalar(fields, "theme", context)
    if theme != folder:
        raise CorpusError(f"{context}: theme must match its folder {folder!r}, got {theme!r}")
    if theme not in themes:
        raise CorpusError(f"{context}: theme is not declared in config/content-manifest.json: {theme!r}")
    return theme


def _tags(fields: dict[str, object], vocabulary: set[str], context: str) -> tuple[str, ...]:
    tags = _string_list(fields, "tags", context)
    unknown = sorted(set(tags) - vocabulary)
    if unknown:
        raise CorpusError(f"{context}: tags include a Tag missing from TAGS.md: {unknown}")
    # Author order is information the corpus carries, and Export has to put it
    # back byte for byte, so it is preserved rather than sorted: 1025 of the
    # 1111 corpus files list their tags non-alphabetically.  `dict.fromkeys`
    # still drops a repeated Tag, of which the corpus currently has none.
    return tuple(dict.fromkeys(tags))


def _sources(fields: dict[str, object], context: str) -> tuple[dict, ...]:
    value = fields.get("sources")
    if not isinstance(value, list) or not value:
        raise CorpusError(f"{context}: missing required front-matter field sources")
    records = []
    for item in value:
        if not isinstance(item, dict) or set(item) != {"url", "source_type", "verified_on"}:
            raise CorpusError(
                f"{context}: every sources entry needs url, source_type, and verified_on, got {item!r}"
            )
        records.append({key: str(item[key]) for key in ("url", "source_type", "verified_on")})
    return tuple(records)


def _prompt(body: str, context: str) -> str:
    """The question itself: the paragraph under the heading, or the heading."""
    heading = HEADING.search(body)
    if not heading:
        raise CorpusError(f"{context}: cannot extract prompt: no '# ' heading in the body")
    rest = body[heading.end():]
    section = SECTION.search(rest)
    paragraph = (rest[: section.start()] if section else rest).strip()
    return paragraph or heading.group(1).strip()


def _answer_guide(body: str, context: str) -> tuple[str, ...]:
    if ANSWER_GUIDE_HEADING not in body:
        raise CorpusError(f"{context}: cannot extract answer_guide: no '{ANSWER_GUIDE_HEADING}' section")
    section = body.split(ANSWER_GUIDE_HEADING, 1)[1]
    following = SECTION.search(section)
    points = tuple(match.strip() for match in BULLET.findall(section[: following.start()] if following else section))
    if not points:
        raise CorpusError(f"{context}: cannot extract answer_guide: the section lists no '- ' points")
    return points


def _placement(context: str) -> tuple[str, str]:
    """The folder and stem a corpus path carries, which pin a record's identity.

    A `source_path` is `questions/<theme>/<slug>.md`, so the folder is the Theme
    the front matter has to agree with and the stem is the slug. Deriving both
    from the path string rather than from a `Path` object is what lets the
    document readers below work on text the Content API has not written to disk.
    """
    placement = Path(context)
    return placement.parent.name, placement.stem


def read_question_document(
    text: str, context: str, themes: dict[str, str], vocabulary: set[str], updated_at: str
) -> dict:
    """Read one Question from the text of its Markdown document.

    `context` is the document's `source_path`; it names the file in every error
    message and carries the Theme folder and slug that the front matter must
    agree with. Nothing here touches the filesystem, which is the point: the
    Content API's write surface validates a proposed Question by rendering it
    and reading it back through this function, so "valid to write" and "valid in
    the corpus" cannot drift apart into two different answers.
    """
    folder, stem = _placement(context)
    fields, body, content_hash = _parse_document(text, context)
    theme = _theme(fields, folder, themes, context)
    return {
        "id": f"{theme}/{stem}",
        "theme": theme,
        "slug": stem,
        "title": _scalar(fields, "title", context),
        "difficulty": _one_of(_scalar(fields, "difficulty", context), DIFFICULTIES, "difficulty", context),
        "type": _one_of(_scalar(fields, "type", context), QUESTION_TYPES, "type", context),
        "tags": _tags(fields, vocabulary, context),
        "sources": _sources(fields, context),
        "prompt": _prompt(body, context),
        "answer_guide": _answer_guide(body, context),
        "body_markdown": body,
        "source_path": context,
        "content_hash": content_hash,
        "updated_at": updated_at,
    }


def read_question(root: Path, path: Path, themes: dict[str, str], vocabulary: set[str], updated_at: str) -> dict:
    """Read one Question from its file under `root`."""
    context = _context(root, path)
    return read_question_document(_document_text(path, context), context, themes, vocabulary, updated_at)


def read_lab_document(
    text: str,
    context: str,
    themes: dict[str, str],
    vocabulary: set[str],
    question_ids: set[str],
    updated_at: str,
) -> dict:
    """Read one Lab from the text of its Markdown document.

    `question_ids` is the set the reference has to land in. Ingest passes every
    Question it just read; the Content API passes the ids its store can resolve,
    so a Lab that points at nothing is refused identically in both.
    """
    folder, stem = _placement(context)
    fields, body, content_hash = _parse_document(text, context)
    theme = _theme(fields, folder, themes, context)
    reference = _scalar(fields, "question_ref", context)
    match = QUESTION_REF.match(reference)
    if not match:
        raise CorpusError(f"{context}: question_ref must read '<theme>/<slug>.md', got {reference!r}")
    # The corpus writes `question_ref` as a path; the epic pins it as a Question
    # `id`, so the `.md` is dropped on the way in and Export puts it back.
    question_id = match.group(1)
    if question_id not in question_ids:
        raise CorpusError(f"{context}: question_ref does not resolve to a Question: {question_id}")
    return {
        "id": f"{theme}/{stem}",
        "theme": theme,
        "slug": stem,
        "title": _scalar(fields, "title", context),
        "difficulty": _one_of(_scalar(fields, "difficulty", context), DIFFICULTIES, "difficulty", context),
        "question_ref": question_id,
        "why": _scalar(fields, "why", context),
        "checklist": _string_list(fields, "checklist", context),
        "tags": _tags(fields, vocabulary, context),
        "body_markdown": body,
        "source_path": context,
        "content_hash": content_hash,
        "updated_at": updated_at,
    }


def read_lab(
    root: Path,
    path: Path,
    themes: dict[str, str],
    vocabulary: set[str],
    question_ids: set[str],
    updated_at: str,
) -> dict:
    """Read one Lab from its file under `root`."""
    context = _context(root, path)
    return read_lab_document(
        _document_text(path, context), context, themes, vocabulary, question_ids, updated_at
    )


def _validate_cycle_freedom(track_slug: str, steps: list[dict]) -> None:
    """Verify that prerequisites form a valid Directed Acyclic Graph (DAG) with no cycles."""
    step_ids = {s["step_id"] for s in steps}
    adj: dict[str, list[str]] = {s["step_id"]: [] for s in steps}

    for step in steps:
        step_id = step["step_id"]
        for prereq in step.get("prerequisites", ()):
            if prereq not in step_ids:
                raise CorpusError(
                    f"track {track_slug}: step '{step_id}' references unknown prerequisite '{prereq}'"
                )
            if prereq == step_id:
                raise CorpusError(f"track {track_slug}: step '{step_id}' cannot depend on itself")
            adj[prereq].append(step_id)

    visited: dict[str, int] = {s["step_id"]: 0 for s in steps}

    def dfs(node: str, path: list[str]) -> None:
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 1:
                cycle = " -> ".join(path + [neighbor])
                raise CorpusError(f"track {track_slug}: prerequisite cycle detected: {cycle}")
            if visited[neighbor] == 0:
                dfs(neighbor, path + [neighbor])
        visited[node] = 2

    for step in steps:
        if visited[step["step_id"]] == 0:
            dfs(step["step_id"], [step["step_id"]])


def read_learning_paths(root: Path, question_ids: set[str]) -> tuple[dict, ...]:
    """Read track manifests from `tracks/` and legacy paths from `config/learning-paths.json`."""
    paths: list[dict] = []
    seen_slugs: set[str] = set()

    # 1. Track manifests in tracks/
    tracks_dir = root / "tracks"
    if tracks_dir.is_dir():
        track_files = sorted(tracks_dir.glob("*.json"))
        if not track_files:
            try:
                import yaml  # noqa: F401
                track_files = sorted(list(tracks_dir.glob("*.yml")) + list(tracks_dir.glob("*.yaml")))
            except ImportError:
                track_files = []

        for track_path in track_files:
            try:
                if track_path.suffix == ".json":
                    data = json.loads(track_path.read_text(encoding="utf-8"))
                else:
                    import yaml
                    data = yaml.safe_load(track_path.read_text(encoding="utf-8"))
            except Exception as err:
                raise CorpusError(f"{track_path}: cannot parse track manifest ({err})") from err

            if not isinstance(data, dict):
                raise CorpusError(f"{track_path}: track manifest root must be a dictionary")

            slug = str(data.get("id", track_path.stem))
            title = str(data.get("name", ""))
            description = str(data.get("description", ""))
            icon = str(data.get("icon", "🗺️"))
            color = str(data.get("color", "#38bdf8"))
            target_audience = str(data.get("target_audience", ""))
            certifications = tuple(str(c) for c in data.get("certifications", ()))
            prerequisites = tuple(str(p) for p in data.get("prerequisites", ()))

            steps = []
            raw_steps = data.get("steps", [])
            if not isinstance(raw_steps, list):
                raise CorpusError(f"{track_path}: 'steps' must be a list")

            step_ids = set()
            for idx, step in enumerate(raw_steps):
                step_id = str(step.get("id", f"step-{idx}"))
                if step_id in step_ids:
                    raise CorpusError(f"{track_path}: duplicate step id '{step_id}'")
                step_ids.add(step_id)

                q_id = step.get("question_id")
                if q_id:
                    q_id = str(q_id)
                    if q_id not in question_ids:
                        raise CorpusError(f"{track_path}: step '{step_id}' points at a missing Question '{q_id}'")

                steps.append(
                    {
                        "step_id": step_id,
                        "skill_id": str(step.get("skill_id", step_id)),
                        "title": str(step.get("title", "")),
                        "difficulty": str(step.get("difficulty", "middle")),
                        "theme": str(step.get("theme", "")),
                        "question_id": q_id,
                        "lab_slug": str(step.get("lab_slug")) if step.get("lab_slug") else None,
                        "concepts": tuple(str(c) for c in step.get("concepts", ())),
                        "why": str(step.get("why", step.get("description", ""))),
                        "prerequisites": tuple(str(p) for p in step.get("prerequisites", ())),
                    }
                )

            _validate_cycle_freedom(slug, steps)

            paths.append(
                {
                    "slug": slug,
                    "title": title,
                    "description": description,
                    "icon": icon,
                    "color": color,
                    "target_audience": target_audience,
                    "certifications": certifications,
                    "prerequisites": prerequisites,
                    "steps": tuple(steps),
                }
            )
            seen_slugs.add(slug)

    # 2. Legacy config/learning-paths.json (if not superseded by track)
    source = root / "config" / "learning-paths.json"
    if source.is_file():
        declaration = json.loads(source.read_text(encoding="utf-8"))
        for path in declaration.get("paths", []):
            slug = path["slug"]
            if slug in seen_slugs:
                continue
            steps = []
            for step in path["steps"]:
                reference = step["question"]
                question_id = reference[len("questions/"):].removesuffix(".md")
                if not reference.startswith("questions/") or question_id not in question_ids:
                    raise CorpusError(
                        f"config/learning-paths.json: {slug} step points at a missing Question: {reference}"
                    )
                steps.append(
                    {
                        "step_id": f"step-{len(steps)}",
                        "skill_id": question_id,
                        "title": "",
                        "difficulty": "middle",
                        "theme": question_id.split("/")[0] if "/" in question_id else "",
                        "question_id": question_id,
                        "lab_slug": None,
                        "concepts": (),
                        "why": step["why"],
                        "prerequisites": (),
                    }
                )
            paths.append(
                {
                    "slug": slug,
                    "title": path["title"],
                    "description": path.get("audience", ""),
                    "icon": "🗺️",
                    "color": "#38bdf8",
                    "target_audience": path.get("audience", ""),
                    "certifications": (),
                    "prerequisites": tuple(path.get("prerequisites", ())),
                    "steps": tuple(steps),
                }
            )
            seen_slugs.add(slug)

    return tuple(sorted(paths, key=lambda path: path["slug"]))


def read_corpus(root: Path) -> Corpus:
    """Read every Question, Lab, Theme, Tag, and LearningPath under `root`."""
    themes = declared_themes(root)
    vocabulary = known_tags(root)
    times = commit_times(root)

    questions = []
    for path in sorted((root / "questions").rglob("*.md")):
        updated_at = times.get(_context(root, path), UNTRACKED_UPDATED_AT)
        questions.append(read_question(root, path, themes, vocabulary, updated_at))
    question_ids = {question["id"] for question in questions}

    labs = []
    lab_root = root / "labs"
    if lab_root.is_dir():
        for path in sorted(lab_root.rglob("*.md")):
            updated_at = times.get(_context(root, path), UNTRACKED_UPDATED_AT)
            labs.append(read_lab(root, path, themes, vocabulary, question_ids, updated_at))

    return Corpus(
        themes=_theme_records(themes, questions, labs),
        tags=_tag_records(vocabulary, questions, labs),
        questions=tuple(sorted(questions, key=lambda record: record["id"])),
        labs=tuple(sorted(labs, key=lambda record: record["id"])),
        learning_paths=read_learning_paths(root, question_ids),
    )


def _theme_records(themes: dict[str, str], questions: list[dict], labs: list[dict]) -> tuple[dict, ...]:
    """Every declared Theme, including the planned ones that hold nothing yet."""
    records = []
    for name in sorted(themes):
        owned = [question for question in questions if question["theme"] == name]
        records.append(
            {
                "name": name,
                "state": themes[name],
                "question_count": len(owned),
                "lab_count": sum(1 for lab in labs if lab["theme"] == name),
                # Every band is published, zeros included: a client charting a
                # Theme's mix should not have to guess whether a missing key
                # means "none" or "not counted".
                "difficulty_counts": {
                    difficulty: sum(1 for question in owned if question["difficulty"] == difficulty)
                    for difficulty in DIFFICULTIES
                },
            }
        )
    return tuple(records)


def _tag_records(vocabulary: set[str], questions: list[dict], labs: list[dict]) -> tuple[dict, ...]:
    """Only Tags the corpus actually uses.

    `TAGS.md` is the permitted vocabulary, not an inventory: publishing its
    unused entries would tell an API client that filtering by them returns
    something.
    """
    records = []
    for name in sorted(vocabulary):
        question_count = sum(1 for question in questions if name in question["tags"])
        lab_count = sum(1 for lab in labs if name in lab["tags"])
        if question_count or lab_count:
            records.append({"name": name, "question_count": question_count, "lab_count": lab_count})
    return tuple(records)
