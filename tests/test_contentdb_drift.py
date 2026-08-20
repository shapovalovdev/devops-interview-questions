"""The Drift gate must fail when the corpus and the store disagree.

`python -m contentdb.drift` is the check that keeps Markdown in git the durable
record: it builds a Content store from the corpus, exports it back, and refuses
any difference.  ADR 0001 rests on it.

It had no test module of its own.  `main()` ran on every CI push and nothing
asserted on what it does -- not the exit code, not the message, not the
difference list.  A gate nobody tests is a gate that can stop biting quietly,
which is worse than not having one, because the green tick still appears.

Each case below mutates one file of a fixture corpus that the same class proves
clean first, so a passing assertion is evidence about the gate rather than about
a fixture that never round-tripped.
"""

from __future__ import annotations

import io
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import drift, export  # noqa: E402  - needs the path above
from contentdb.corpus import CorpusError  # noqa: E402

import contentdb_fixtures as fixtures  # noqa: E402  - a tests/ sibling


def run_main(*argv: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = drift.main(list(argv))
    return code, out.getvalue(), err.getvalue()


class DriftGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.directory, ignore_errors=True)
        self.root = self.directory / "corpus"
        fixtures.write_corpus(self.root)
        self._make_a_git_repository(self.root)

    @staticmethod
    def _make_a_git_repository(root: Path) -> None:
        """Ingest records the source commit, so the fixture needs one.

        Refusing to build outside a repository is deliberate -- the snapshot's
        provenance is part of the store -- so the fixture meets that
        requirement rather than the test working around it.
        """
        def git(*args: str) -> None:
            subprocess.run(
                ["git", *args],
                cwd=root,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        git("init", "--quiet")
        git("config", "user.email", "fixture@example.invalid")
        git("config", "user.name", "Fixture")
        git("add", "-A")
        git("commit", "--quiet", "-m", "fixture corpus")

    def question(self) -> Path:
        return next((self.root / "questions").glob("*/*.md"))

    def test_a_clean_corpus_round_trips_and_says_so(self) -> None:
        """The control: every case below mutates this same fixture."""
        code, out, err = run_main("--root", str(self.root))
        self.assertEqual(0, code, err)
        self.assertIn("No drift", out)
        self.assertEqual("", err)

    def test_a_changed_file_is_reported_and_fails(self) -> None:
        """Drift is a difference between the corpus and its own export."""
        differences = ["questions/linux/one.md"]
        with patch.object(drift, "check", return_value=differences):
            code, out, err = run_main("--root", str(self.root))

        self.assertEqual(1, code)
        self.assertIn("Drift detected", err)
        self.assertIn("1 file(s) differ", err)
        self.assertIn("questions/linux/one.md", err)
        self.assertEqual("", out, "a failing gate must not also print the success line")

    def test_every_differing_file_is_named(self) -> None:
        """A count without the names cannot be acted on."""
        differences = [f"questions/linux/{name}.md" for name in ("a", "b", "c")]
        with patch.object(drift, "check", return_value=differences):
            _, _, err = run_main("--root", str(self.root))

        self.assertIn("3 file(s) differ", err)
        for difference in differences:
            self.assertIn(difference, err)

    def test_a_corpus_error_is_an_exit_code_and_a_message(self) -> None:
        """A corpus that cannot be read is a failure, not a traceback."""
        with patch.object(drift, "check", side_effect=CorpusError("bad front matter")):
            code, out, err = run_main("--root", str(self.root))

        self.assertEqual(1, code)
        self.assertIn("Drift check failed:", err)
        self.assertIn("bad front matter", err)
        self.assertEqual("", out)

    def test_an_export_error_is_handled_the_same_way(self) -> None:
        """Export failing is the other half of the round trip, and fails alike."""
        with patch.object(drift, "check", side_effect=export.ExportError("cannot write")):
            code, out, err = run_main("--root", str(self.root))

        self.assertEqual(1, code)
        self.assertIn("Drift check failed:", err)
        self.assertIn("cannot write", err)
        self.assertEqual("", out)

    def test_the_gate_actually_bites_on_a_real_difference(self) -> None:
        """Not a stub: change a file on disk and watch the real check find it.

        The cases above patch `check` to exercise `main`'s reporting. This one
        patches nothing, so it proves the two halves are connected -- that a
        difference on disk really does reach the exit code.

        The mutation is trailing whitespace, and the choice is the point. An
        ordinary content edit is **not** drift: Ingest stores it and Export
        writes it back byte for byte, which is exactly the round trip working.
        Drift is the corpus disagreeing with its own normal form -- so the
        mutation has to be something Export would write differently, and
        trailing whitespace is the smallest such thing.

        This was worth discovering rather than assuming. The first version of
        this test changed `difficulty` and expected drift; the gate correctly
        reported none, because a faithful round trip is what it is there to
        confirm.
        """
        question = self.question()
        original = question.read_text(encoding="utf-8")
        self.assertEqual(0, run_main("--root", str(self.root))[0], "fixture must start clean")

        question.write_text(original.replace("\n", "   \n", 1), encoding="utf-8")
        code, out, err = run_main("--root", str(self.root))

        self.assertEqual(1, code, "a file that is not in its own normal form is drift")
        self.assertIn("Drift detected", err)
        self.assertIn(question.name, err, "the gate must name the file that differs")
        self.assertEqual("", out)

    def test_an_ordinary_content_edit_is_not_drift(self) -> None:
        """The other half of the same rule, stated so it cannot be lost.

        If editing a Question produced drift, the gate would be unusable -- every
        content change would trip it. It does not, because the store holds what
        the Markdown says and Export writes it back unchanged.
        """
        question = self.question()
        original = question.read_text(encoding="utf-8")
        # Read the fixture's difficulty rather than assuming one, so this test
        # keeps working if the fixture changes.
        current = re.search(r"^difficulty: (\w+)$", original, re.MULTILINE)
        self.assertIsNotNone(current, "fixture has no difficulty to change")
        replacement = "junior" if current.group(1) != "junior" else "senior"

        question.write_text(
            original.replace(f"difficulty: {current.group(1)}", f"difficulty: {replacement}"),
            encoding="utf-8",
        )
        code, out, _ = run_main("--root", str(self.root))

        self.assertEqual(0, code, "an edited Question round-trips; that is not drift")
        self.assertIn("No drift", out)


if __name__ == "__main__":
    unittest.main()
