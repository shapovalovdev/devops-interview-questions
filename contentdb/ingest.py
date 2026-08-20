"""Write the validated corpus into a SQLite file, reproducibly.

Ingest is the build step named in `CONTEXT.md`: it loads the Markdown corpus
into the Content store. The store is a derived, disposable artifact — it is
rebuilt from Markdown on every build, and nothing may live in it that does not
survive a rebuild — so this module reads, writes, and exits. It never updates.

Determinism is a requirement, not a nicety: a Drift gate compares a store built
from the committed corpus against the corpus, and a build that produced
different bytes from identical inputs could not be compared, cached, or
published. Four things buy it:

- the schema is created from scratch into a fresh file, so no earlier layout
  survives;
- `page_size` is pinned rather than inherited from the running SQLite build;
- every insert is ordered — records arrive sorted by `id`, tags and sources by
  their position in the source file, which Export needs to reproduce it — so page contents never depend on directory-walk order;
- nothing derived from wall-clock time is written; `updated_at` comes from git
  commit history (see :mod:`contentdb.corpus`), the snapshot's `source_commit`
  and `build_timestamp` come from the same history (`build_timestamp` is the
  commit's time, not the run's), and `VACUUM` normalises the
  free list before the file is published.

The file is written to a sibling temporary path and renamed into place at the
very end, so a failed run leaves no half-written store for a later build to
mistake for a good one.

FTS5 is the one feature not every `sqlite3` build ships. Its absence is not
fatal: the store is written without the index, a clear warning goes to stderr,
and :class:`contentdb.store.Store` raises a clear error if anything later asks
it to search.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .corpus import Corpus, CorpusError, content_digest, read_corpus
from .schema import FTS_DDL, FTS_TABLE, SCHEMA_DDL


PAGE_SIZE = 4096

#: Where `build_timestamp` falls back to when git cannot answer — the same
#: convention `updated_at` uses. A build outside a repository that was handed
#: a commit explicitly but no timestamp gets the epoch, which says "unknown"
#: without breaking determinism.
EPOCH_BUILD_TIMESTAMP = "1970-01-01T00:00:00Z"


@dataclass(frozen=True)
class Summary:
    """What one Ingest run put in the store."""

    questions: int
    labs: int
    themes: int
    tags: int
    learning_paths: int
    search: bool
    source_commit: str = ""
    content_digest: str = ""

    def describe(self) -> str:
        index = "with full-text search" if self.search else "WITHOUT full-text search (FTS5 unavailable)"
        described = (
            f"Ingested {self.questions} Questions and {self.labs} Labs across {self.themes} Themes, "
            f"{self.tags} Tags, and {self.learning_paths} learning paths, {index}."
        )
        if self.content_digest:
            described += (
                f" Snapshot {self.content_digest} from commit {self.source_commit}."
            )
        return described


def source_commit_at(root: Path) -> str:
    """The commit the repository at `root` has checked out, or a clear refusal.

    Provenance is a property of the snapshot, so a build that cannot name its
    commit stops rather than recording a guess. Environments without a
    repository — a container image, whose build context carries no `.git` —
    hand the commit in explicitly (`--source-commit`) and never reach here.
    """
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", "") or error
        raise CorpusError(
            f"cannot record the source commit: {root} is not a readable Git repository "
            f"({str(detail).strip()}). The snapshot's provenance is part of the store, so "
            "Ingest refuses to build without it; pass --source-commit (and optionally "
            "--build-timestamp) when building outside a repository, as a container image does."
        ) from error
    commit = completed.stdout.strip()
    if not commit:
        raise CorpusError(
            f"git at {root} answered with no commit; pass --source-commit to name it explicitly."
        )
    return commit


def build_timestamp_for(root: Path, commit: str) -> str:
    """When `commit` was made, in UTC — a function of the commit, not of now.

    The store is byte-for-byte reproducible from the same inputs, so the build
    timestamp cannot be the wall-clock time the run happened to run at; the
    commit's own time is the deterministic answer to "when was this snapshot
    produced". Where git cannot answer, the epoch records "unknown" the same
    way `updated_at` does, keeping the build deterministic there too.
    """
    try:
        seconds = int(
            subprocess.run(
                ["git", "-C", str(root), "show", "-s", "--format=%ct", commit],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
        )
        return datetime.fromtimestamp(seconds, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (OSError, subprocess.CalledProcessError, ValueError):
        return EPOCH_BUILD_TIMESTAMP


def _connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.execute(f"PRAGMA page_size = {PAGE_SIZE}")
    connection.execute("PRAGMA journal_mode = DELETE")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _create_search_index(connection: sqlite3.Connection) -> bool:
    try:
        connection.executescript(FTS_DDL)
    except sqlite3.OperationalError as error:
        print(
            f"warning: this sqlite3 build cannot create the {FTS_TABLE} index ({error}); "
            "the store will be written without full-text search",
            file=sys.stderr,
        )
        return False
    return True


def _write(connection: sqlite3.Connection, corpus: Corpus, meta: dict[str, str]) -> bool:
    connection.executescript(SCHEMA_DDL)
    search = _create_search_index(connection)

    connection.executemany(
        "INSERT INTO store_meta (key, value) VALUES (?, ?)",
        sorted(meta.items()),
    )

    connection.executemany(
        "INSERT INTO themes (name, state, question_count, lab_count, difficulty_counts)"
        " VALUES (?, ?, ?, ?, ?)",
        [
            (
                theme["name"],
                theme["state"],
                theme["question_count"],
                theme["lab_count"],
                json.dumps(theme["difficulty_counts"], sort_keys=True),
            )
            for theme in corpus.themes
        ],
    )
    connection.executemany(
        "INSERT INTO tags (name, question_count, lab_count) VALUES (?, ?, ?)",
        [(tag["name"], tag["question_count"], tag["lab_count"]) for tag in corpus.tags],
    )

    connection.executemany(
        "INSERT INTO questions (id, theme, slug, title, difficulty, type, prompt, answer_guide,"
        " body_markdown, source_path, content_hash, updated_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                question["id"],
                question["theme"],
                question["slug"],
                question["title"],
                question["difficulty"],
                question["type"],
                question["prompt"],
                json.dumps(list(question["answer_guide"]), ensure_ascii=False),
                question["body_markdown"],
                question["source_path"],
                question["content_hash"],
                question["updated_at"],
            )
            for question in corpus.questions
        ],
    )
    connection.executemany(
        "INSERT INTO question_tags (question_id, position, tag) VALUES (?, ?, ?)",
        [
            (question["id"], position, tag)
            for question in corpus.questions
            for position, tag in enumerate(question["tags"])
        ],
    )
    connection.executemany(
        "INSERT INTO question_sources (question_id, position, url, source_type, verified_on)"
        " VALUES (?, ?, ?, ?, ?)",
        [
            (question["id"], position, source["url"], source["source_type"], source["verified_on"])
            for question in corpus.questions
            for position, source in enumerate(question["sources"])
        ],
    )

    connection.executemany(
        "INSERT INTO labs (id, theme, slug, title, difficulty, question_ref, why, checklist,"
        " body_markdown, source_path, content_hash, updated_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                lab["id"],
                lab["theme"],
                lab["slug"],
                lab["title"],
                lab["difficulty"],
                lab["question_ref"],
                lab["why"],
                json.dumps(list(lab["checklist"]), ensure_ascii=False),
                lab["body_markdown"],
                lab["source_path"],
                lab["content_hash"],
                lab["updated_at"],
            )
            for lab in corpus.labs
        ],
    )
    connection.executemany(
        "INSERT INTO lab_tags (lab_id, position, tag) VALUES (?, ?, ?)",
        [(lab["id"], position, tag) for lab in corpus.labs for position, tag in enumerate(lab["tags"])],
    )

    connection.executemany(
        """INSERT INTO learning_paths (
            slug, title, description, icon, color, target_audience, certifications, prerequisites
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        [
            (
                path["slug"],
                path["title"],
                path["description"],
                path.get("icon", "🗺️"),
                path.get("color", "#38bdf8"),
                path.get("target_audience", ""),
                json.dumps(list(path.get("certifications", ())), ensure_ascii=False),
                json.dumps(list(path.get("prerequisites", ())), ensure_ascii=False),
            )
            for path in corpus.learning_paths
        ],
    )
    connection.executemany(
        """INSERT INTO learning_path_steps (
            path_slug, position, step_id, skill_id, title, difficulty, theme, question_id, lab_slug, concepts, why
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [
            (
                path["slug"],
                position,
                step.get("step_id", f"step-{position}"),
                step.get("skill_id", ""),
                step.get("title", ""),
                step.get("difficulty", "middle"),
                step.get("theme", ""),
                step.get("question_id"),
                step.get("lab_slug"),
                json.dumps(list(step.get("concepts", ())), ensure_ascii=False),
                step.get("why", ""),
            )
            for path in corpus.learning_paths
            for position, step in enumerate(path["steps"])
        ],
    )
    prereq_rows = []
    for path in corpus.learning_paths:
        for step in path["steps"]:
            step_id = step.get("step_id", f"step-{0}")
            for prereq in step.get("prerequisites", ()):
                prereq_rows.append((path["slug"], step_id, prereq))
    if prereq_rows:
        connection.executemany(
            "INSERT INTO learning_path_prerequisites (path_slug, step_id, depends_on_step) VALUES (?, ?, ?)",
            prereq_rows,
        )

    if search:
        connection.executemany(
            f"INSERT INTO {FTS_TABLE} (kind, ref_id, title, prompt, body) VALUES (?, ?, ?, ?, ?)",
            [
                ("question", question["id"], question["title"], question["prompt"], question["body_markdown"])
                for question in corpus.questions
            ]
            + [
                ("lab", lab["id"], lab["title"], lab["why"], lab["body_markdown"])
                for lab in corpus.labs
            ],
        )
    return search


def build(
    root: Path,
    output: Path,
    *,
    source_commit: str | None = None,
    build_timestamp: str | None = None,
) -> Summary:
    """Read the corpus under `root` and write the Content store to `output`.

    Raises :class:`contentdb.corpus.CorpusError` — before creating any file —
    if the corpus cannot be read or breaks a catalog rule, or if `root` is not
    a readable Git repository and no `source_commit` was handed in: the
    snapshot's provenance is recorded in the store, so a build that cannot
    name its commit stops rather than record a guess.

    `source_commit` and `build_timestamp` carry provenance explicitly for
    builds without a repository (a container image, whose build context
    carries no `.git`). Both stay out of the digest: the digest is a function
    of the corpus alone, so the same corpus answers the same digest whatever
    commit labels it.
    """
    root = Path(root)
    output = Path(output)
    corpus = read_corpus(root)
    commit = source_commit or source_commit_at(root)
    stamp = build_timestamp or build_timestamp_for(root, commit)
    meta = {
        "source_commit": commit,
        "content_digest": content_digest(corpus),
        "build_timestamp": stamp,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    staging = output.with_name(output.name + ".building")
    staging.unlink(missing_ok=True)
    connection = _connect(staging)
    try:
        with connection:
            search = _write(connection, corpus, meta)
        # VACUUM rewrites the file with no free pages, so two runs cannot differ
        # by the incidental layout left behind by insert order within a page.
        connection.execute("VACUUM")
    finally:
        connection.close()
    os.replace(staging, output)

    return Summary(
        questions=len(corpus.questions),
        labs=len(corpus.labs),
        themes=len(corpus.themes),
        tags=len(corpus.tags),
        learning_paths=len(corpus.learning_paths),
        search=search,
        source_commit=commit,
        content_digest=meta["content_digest"],
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m contentdb.ingest",
        description="Build the Content store from the Markdown corpus.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root holding questions/, labs/, config/, and TAGS.md",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("build/content.db"),
        help="path to write the Content store to (default: build/content.db)",
    )
    parser.add_argument(
        "--source-commit",
        default=None,
        help="commit SHA to record as provenance when building outside a Git repository",
    )
    parser.add_argument(
        "--build-timestamp",
        default=None,
        help="ISO 8601 build timestamp to record when building outside a Git repository",
    )
    arguments = parser.parse_args(argv)
    try:
        summary = build(
            arguments.root,
            arguments.output,
            source_commit=arguments.source_commit,
            build_timestamp=arguments.build_timestamp,
        )
    except CorpusError as error:
        print(f"Ingest failed: {error}", file=sys.stderr)
        return 1
    print(f"{summary.describe()} Wrote {arguments.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
