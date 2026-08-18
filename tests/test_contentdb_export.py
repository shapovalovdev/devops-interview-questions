"""Export must reproduce the corpus, and Drift must refuse it when it does not.

These checks are what make ADR 0001's promise enforceable rather than aspirational:
Markdown in git stays the durable record only if a store can be turned back into
exactly the files it came from, and only if CI notices when it cannot.

The fidelity checks run against the **real committed corpus**, not a fixture, and
assert per file rather than in aggregate. A fixture cannot prove that 1111 real
documents survive a round trip; only the corpus can, and it is the corpus that
would break.
"""

from __future__ import annotations

import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import drift, export, ingest, store  # noqa: E402  - needs the path above
from contentdb.export import ExportError  # noqa: E402
from contentdb.models import LabQuery, QuestionQuery  # noqa: E402

import contentdb_fixtures as fixtures  # noqa: E402  - a tests/ sibling

PAGE = 200


def _every(lister, query):
    offset = 0
    while True:
        page = lister(query(limit=PAGE, offset=offset))
        for record in page.items:
            yield record
        offset += len(page.items)
        if not page.items or offset >= page.total:
            return


class CorpusRoundTrip(unittest.TestCase):
    """Every real Question and Lab survives store → Markdown byte for byte."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="contentdb-export-corpus-"))
        cls.database = cls.tmp / "content.db"
        ingest.build(ROOT, cls.database)
        cls.store = store.Store(cls.database)

    @classmethod
    def tearDownClass(cls):
        cls.store.close()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _check(self, records, kind):
        checked = 0
        for record in records:
            source = ROOT / str(record["source_path"])
            rendered = export.render(record, kind)
            if rendered != source.read_text(encoding="utf-8"):
                self.fail(
                    f"{record['source_path']} does not round-trip; the corpus is the "
                    "specification, so the renderer is what is wrong"
                )
            checked += 1
        return checked

    def test_every_question_round_trips(self):
        checked = self._check(_every(self.store.list_questions, QuestionQuery), "question")
        self.assertEqual(checked, len(list((ROOT / "questions").rglob("*.md"))))

    def test_every_lab_round_trips(self):
        checked = self._check(_every(self.store.list_labs, LabQuery), "lab")
        self.assertEqual(checked, len(list((ROOT / "labs").rglob("*.md"))))

    def test_tag_order_survives_the_store(self):
        """The defect this slice found: sorted tags cannot be un-sorted later."""
        record = self.store.get_question("advanced-containers/capabilities-least-privilege")
        self.assertEqual(
            record["tags"], ["containers", "linux", "capabilities", "security", "least-privilege"]
        )


class ExportWrites(unittest.TestCase):
    """Writing is idempotent, and refuses paths that are not corpus files."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="contentdb-export-write-"))
        self.root = fixtures.write_corpus(self.tmp / "corpus")
        self.database = self.tmp / "content.db"
        ingest.build(self.root, self.database)
        self.store = store.Store(self.database)
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.addCleanup(self.store.close)

    def test_exporting_over_its_own_corpus_changes_nothing(self):
        written, unchanged = export.export(self.store, self.root)
        self.assertEqual(written, 0)
        self.assertGreater(unchanged, 0)

    def test_export_is_idempotent(self):
        target = self.tmp / "fresh"
        for directory in export.SAFE_ROOTS:
            (target / directory).mkdir(parents=True)
        first_written, _ = export.export(self.store, target)
        second_written, second_unchanged = export.export(self.store, target)
        self.assertGreater(first_written, 0)
        self.assertEqual(second_written, 0)
        self.assertEqual(second_unchanged, first_written)

    def test_a_rewritten_file_matches_the_original(self):
        sample = next(_every(self.store.list_questions, QuestionQuery))
        path = self.root / str(sample["source_path"])
        original = path.read_text(encoding="utf-8")
        path.write_text("clobbered\n", encoding="utf-8")
        self.assertTrue(export.write(self.root, sample, "question"))
        self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_hostile_source_paths_are_refused(self):
        for hostile in (
            "../../etc/passwd",
            "questions/../../escape.md",
            "/etc/passwd",
            "docs/not-a-question.md",
            "questions/theme/slug.txt",
            "questions/slug.md",
        ):
            with self.subTest(source_path=hostile):
                with self.assertRaises(ExportError):
                    export.target(self.root, hostile)

    def test_a_hostile_path_never_reaches_the_filesystem(self):
        record = dict(next(_every(self.store.list_questions, QuestionQuery)))
        record["source_path"] = "../escaped.md"
        with self.assertRaises(ExportError):
            export.write(self.root, record, "question")
        self.assertFalse((self.tmp / "escaped.md").exists())


class RendererRefusals(unittest.TestCase):
    """A record that cannot be rendered exactly raises instead of approximating."""

    def _question(self, **overrides):
        record = {
            "title": "A title",
            "theme": "kubernetes",
            "difficulty": "middle",
            "type": "theory",
            "tags": ["kubernetes"],
            "sources": [
                {"url": "https://example.invalid/a", "source_type": "official-docs", "verified_on": "2026-08-06"}
            ],
            "body_markdown": "\n# A title\n",
            "source_path": "questions/kubernetes/a.md",
        }
        record.update(overrides)
        return record

    def test_a_title_yaml_could_not_hold_is_refused(self):
        with self.assertRaises(ExportError):
            export.render_question(self._question(title="Explain this: carefully"))

    def test_a_source_missing_a_field_is_refused(self):
        with self.assertRaises(ExportError) as caught:
            export.render_question(
                self._question(sources=[{"url": "https://example.invalid/a", "source_type": "official-docs"}])
            )
        self.assertIn("verified_on", str(caught.exception))

    def test_an_embedded_quote_in_a_lab_scalar_is_refused(self):
        record = {
            "title": 'A "quoted" title',
            "theme": "kubernetes",
            "difficulty": "middle",
            "question_ref": "kubernetes/a",
            "tags": ["kubernetes"],
            "why": "because",
            "checklist": ["step"],
            "body_markdown": "\n# x\n",
            "source_path": "labs/kubernetes/a.md",
        }
        with self.assertRaises(ExportError):
            export.render_lab(record)

    def test_an_unknown_kind_is_refused(self):
        with self.assertRaises(ExportError):
            export.render(self._question(), "theme")


class DriftGate(unittest.TestCase):
    """Drift passes on the committed corpus and fails on a perturbed store."""

    def test_the_committed_corpus_does_not_drift(self):
        self.assertEqual(drift.check(ROOT), [])

    def test_the_cli_reports_a_clean_corpus(self):
        self.assertEqual(drift.main(["--root", str(ROOT)]), 0)

    def test_a_perturbed_store_is_caught_with_a_diff_naming_the_file(self):
        tmp = Path(tempfile.mkdtemp(prefix="contentdb-drift-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        root = fixtures.write_corpus(tmp / "corpus")
        database = tmp / "content.db"
        ingest.build(root, database)

        connection = sqlite3.connect(database)
        victim = connection.execute("SELECT id, source_path FROM questions ORDER BY id").fetchone()
        connection.execute("UPDATE questions SET title = 'Tampered title' WHERE id = ?", (victim[0],))
        connection.commit()
        connection.close()

        exported = tmp / "exported"
        for directory in export.SAFE_ROOTS:
            (exported / directory).mkdir(parents=True)
        opened = store.Store(database)
        self.addCleanup(opened.close)
        export.export(opened, exported)

        differences = drift.compare(root, exported)
        self.assertEqual(len(differences), 1)
        self.assertIn(victim[1], differences[0])
        self.assertIn("Tampered title", differences[0])

    def test_a_record_the_store_lost_is_reported(self):
        tmp = Path(tempfile.mkdtemp(prefix="contentdb-drift-missing-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        root = fixtures.write_corpus(tmp / "corpus")
        exported = tmp / "exported"
        (exported / "questions").mkdir(parents=True)
        (exported / "labs").mkdir(parents=True)
        differences = drift.compare(root, exported)
        self.assertTrue(differences)
        self.assertIn("no record", differences[0])


class CommandLine(unittest.TestCase):
    """The CLIs report failure by exit code, not by traceback."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="contentdb-export-cli-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.root = fixtures.write_corpus(self.tmp / "corpus")
        self.database = self.tmp / "content.db"
        ingest.build(self.root, self.database)

    def test_export_writes_the_corpus_and_reports_success(self):
        target = self.tmp / "fresh"
        for directory in export.SAFE_ROOTS:
            (target / directory).mkdir(parents=True)
        self.assertEqual(
            export.main(["--database", str(self.database), "--output", str(target)]), 0
        )
        self.assertTrue((target / "questions").rglob("*.md"))

    def test_export_without_a_store_fails_instead_of_raising(self):
        self.assertEqual(
            export.main(["--database", str(self.tmp / "absent.db"), "--output", str(self.tmp)]), 1
        )

    def test_export_refuses_a_hostile_source_path_through_the_cli(self):
        connection = sqlite3.connect(self.database)
        connection.execute("UPDATE questions SET source_path = '../escaped.md' WHERE id = (SELECT MIN(id) FROM questions)")
        connection.commit()
        connection.close()
        self.assertEqual(
            export.main(["--database", str(self.database), "--output", str(self.root)]), 1
        )
        self.assertFalse((self.tmp / "escaped.md").exists())

    def test_drift_reports_a_corpus_it_cannot_ingest(self):
        broken = self.tmp / "broken"
        shutil.copytree(self.root, broken)
        victim = next(iter((broken / "questions").rglob("*.md")))
        victim.write_text("no front matter here\n", encoding="utf-8")
        self.assertEqual(drift.main(["--root", str(broken)]), 1)


class TargetSafety(unittest.TestCase):
    """`target` refuses a path that escapes the tree even when its shape is legal."""

    def test_a_symlinked_theme_cannot_smuggle_a_write_outside_the_root(self):
        tmp = Path(tempfile.mkdtemp(prefix="contentdb-export-symlink-"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        root = tmp / "repo"
        (root / "questions").mkdir(parents=True)
        outside = tmp / "outside"
        outside.mkdir()
        (root / "questions" / "smuggled").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ExportError) as caught:
            export.target(root, "questions/smuggled/note.md")
        self.assertIn("outside", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
