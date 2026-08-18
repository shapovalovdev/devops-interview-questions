"""Refuse a corpus and a Content store that disagree.

ADR 0001 lets the Content API write, and accepts that writes make the store
diverge from the Markdown corpus.  What keeps that honest is this check: a
change is not landed until it exists as reviewed Markdown in git.  Drift builds
a store from the committed corpus, exports it into a throwaway tree, and
compares.  Clean means every file the store holds is exactly the file on disk.

Run it in CI.  When it fails, the diff names the file and the lines that differ,
because "something drifted" is not an actionable failure.
"""

from __future__ import annotations

import argparse
import difflib
import sys
import tempfile
from pathlib import Path

from contentdb import export
from contentdb.corpus import CorpusError
from contentdb.ingest import build
from contentdb.store import Store

CONTEXT_LINES = 2


def compare(root: Path, exported: Path) -> list[str]:
    """Unified diffs for every corpus file the export did not reproduce."""
    differences: list[str] = []
    for directory in export.SAFE_ROOTS:
        for original in sorted((root / directory).rglob("*.md")):
            relative = original.relative_to(root)
            candidate = exported / relative
            if not candidate.exists():
                differences.append(f"{relative}: the Content store holds no record for this file\n")
                continue
            want = original.read_text(encoding="utf-8").splitlines(keepends=True)
            got = candidate.read_text(encoding="utf-8").splitlines(keepends=True)
            if want != got:
                differences.append(
                    "".join(
                        difflib.unified_diff(
                            want, got, f"{relative} (corpus)", f"{relative} (store)", n=CONTEXT_LINES
                        )
                    )
                )
    return differences


def check(root: Path) -> list[str]:
    """Build a store from `root`, export it to a temporary tree, and diff."""
    with tempfile.TemporaryDirectory(prefix="contentdb-drift-") as scratch:
        scratch_path = Path(scratch)
        database = scratch_path / "content.db"
        build(root, database)
        exported = scratch_path / "corpus"
        for directory in export.SAFE_ROOTS:
            (exported / directory).mkdir(parents=True, exist_ok=True)
        opened = Store(database)
        try:
            export.export(opened, exported)
        finally:
            opened.close()
        return compare(root, exported)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m contentdb.drift",
        description="Fail when the Markdown corpus and a store built from it disagree.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root holding questions/ and labs/",
    )
    arguments = parser.parse_args(argv)
    try:
        differences = check(arguments.root)
    except (CorpusError, export.ExportError) as error:
        print(f"Drift check failed: {error}", file=sys.stderr)
        return 1
    if differences:
        print(
            f"Drift detected: {len(differences)} file(s) differ between the corpus and the "
            "Content store built from it.\n",
            file=sys.stderr,
        )
        for difference in differences:
            print(difference, file=sys.stderr)
        return 1
    print("No drift: every Question and Lab round-trips through the Content store unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
