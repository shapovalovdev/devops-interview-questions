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
  commit history (see :mod:`contentdb.corpus`), and `VACUUM` normalises the
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
import sys
from dataclasses import dataclass
from pathlib import Path

from .corpus import Corpus, CorpusError, read_corpus
from .schema import FTS_DDL, FTS_TABLE, SCHEMA_DDL


PAGE_SIZE = 4096


@dataclass(frozen=True)
class Summary:
    """What one Ingest run put in the store."""

    questions: int
    labs: int
    themes: int
    tags: int
    learning_paths: int
    search: bool

    def describe(self) -> str:
        index = "with full-text search" if self.search else "WITHOUT full-text search (FTS5 unavailable)"
        return (
            f"Ingested {self.questions} Questions and {self.labs} Labs across {self.themes} Themes, "
            f"{self.tags} Tags, and {self.learning_paths} learning paths, {index}."
        )


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


def _write(connection: sqlite3.Connection, corpus: Corpus) -> bool:
    connection.executescript(SCHEMA_DDL)
    search = _create_search_index(connection)

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
        "INSERT INTO learning_paths (slug, title, description, prerequisites) VALUES (?, ?, ?, ?)",
        [
            (
                path["slug"],
                path["title"],
                path["description"],
                json.dumps(list(path["prerequisites"]), ensure_ascii=False),
            )
            for path in corpus.learning_paths
        ],
    )
    connection.executemany(
        "INSERT INTO learning_path_steps (path_slug, position, question_id, why) VALUES (?, ?, ?, ?)",
        [
            (path["slug"], position, step["question_id"], step["why"])
            for path in corpus.learning_paths
            for position, step in enumerate(path["steps"])
        ],
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


def build(root: Path, output: Path) -> Summary:
    """Read the corpus under `root` and write the Content store to `output`.

    Raises :class:`contentdb.corpus.CorpusError` — before creating any file —
    if the corpus cannot be read or breaks a catalog rule.
    """
    root = Path(root)
    output = Path(output)
    corpus = read_corpus(root)

    output.parent.mkdir(parents=True, exist_ok=True)
    staging = output.with_name(output.name + ".building")
    staging.unlink(missing_ok=True)
    connection = _connect(staging)
    try:
        with connection:
            search = _write(connection, corpus)
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
    arguments = parser.parse_args(argv)
    try:
        summary = build(arguments.root, arguments.output)
    except CorpusError as error:
        print(f"Ingest failed: {error}", file=sys.stderr)
        return 1
    print(f"{summary.describe()} Wrote {arguments.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
