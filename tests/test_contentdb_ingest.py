"""Ingest must read the whole corpus, read it the same way twice, or stop.

Three properties are worth a test here, and they are in tension:

*Completeness* — the Content store is only trustworthy if every Question and
Lab reached it, so the counts are asserted against a fresh walk of the corpus
rather than a number somebody typed.

*Determinism* — the store is a derived artifact rebuilt on every build, and a
build that produces different bytes from identical inputs cannot be cached,
diffed, or used by a Drift gate.  The check is the strongest available one:
build twice, compare sha256 of the two files.

*Loudness* — a parser that silently skips the file it cannot read hides missing
content behind a plausible count.  Every failure case below mutates exactly one
field of a fixture the same module proves valid, so a passing assertion is
evidence about the rule and not about a fixture that never worked.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import corpus, ingest  # noqa: E402  - needs the path above

import contentdb_fixtures as fixtures  # noqa: E402  - a tests/ sibling


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


#: Provenance handed to Ingest explicitly for fixture corpora, which live in a
#: temporary directory outside any Git repository. A fixture commit of all
#: zeros can never be mistaken for a real one, and a fixed timestamp keeps the
#: byte-identity checks meaningful.
FIXTURE_COMMIT = "0" * 40
FIXTURE_TIMESTAMP = "2026-08-18T00:00:00Z"


def fixture_build(root: Path, output: Path):
    return ingest.build(
        root, output, source_commit=FIXTURE_COMMIT, build_timestamp=FIXTURE_TIMESTAMP
    )


class FixtureCorpus(unittest.TestCase):
    """Base class giving each test a private, writable copy of the fixture corpus."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="contentdb-fixture-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = fixtures.write_corpus(self.tmp / "corpus")
        self.output = self.tmp / "content.db"

    def build(self):
        return fixture_build(self.root, self.output)

    def refuses(self, needles: tuple[str, ...]):
        with self.assertRaises(corpus.CorpusError) as caught:
            self.build()
        message = str(caught.exception)
        for needle in needles:
            self.assertIn(needle, message)
        return message

    def rewrite_question(self, theme: str, slug: str, old: str, new: str):
        path = self.root / "questions" / theme / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture no longer contains {old!r}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return path

    def rewrite_lab(self, theme: str, slug: str, old: str, new: str):
        path = self.root / "labs" / theme / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture no longer contains {old!r}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return path

    def meta(self, database: Path | None = None) -> dict:
        """The `store_meta` table of a built store, as a dict."""
        connection = sqlite3.connect(database or self.output)
        rows = connection.execute("SELECT key, value FROM store_meta").fetchall()
        connection.close()
        return dict(rows)


class BuildsTheFixtureCorpus(FixtureCorpus):
    def test_summary_counts_every_record(self):
        summary = self.build()
        self.assertEqual(summary.questions, len(fixtures.QUESTIONS))
        self.assertEqual(summary.labs, len(fixtures.LABS))
        self.assertEqual(summary.learning_paths, 1)
        self.assertTrue(self.output.is_file())

    def test_stores_the_fields_the_markdown_declares(self):
        self.build()
        connection = sqlite3.connect(self.output)
        self.addCleanup(connection.close)
        row = connection.execute(
            "SELECT theme, slug, title, difficulty, type, prompt, answer_guide, source_path, content_hash"
            " FROM questions WHERE id = ?",
            ("kubernetes/admission-policy",),
        ).fetchone()
        self.assertIsNotNone(row)
        theme, slug, title, difficulty, type_, prompt, answer_guide, source_path, content_hash = row
        self.assertEqual((theme, slug), ("kubernetes", "admission-policy"))
        self.assertEqual(title, "Design an admission policy")
        self.assertEqual((difficulty, type_), ("senior", "scenario"))
        self.assertIn("admission policy without breaking", prompt)
        self.assertEqual(len(json.loads(answer_guide)), 3)
        self.assertEqual(source_path, "questions/kubernetes/admission-policy.md")
        self.assertEqual(content_hash, digest(self.root / source_path))

    def test_lab_question_ref_is_stored_as_a_question_id(self):
        self.build()
        connection = sqlite3.connect(self.output)
        self.addCleanup(connection.close)
        reference = connection.execute(
            "SELECT question_ref FROM labs WHERE id = ?", ("kubernetes/admission-lab",)
        ).fetchone()[0]
        self.assertEqual(reference, "kubernetes/admission-policy")

    def test_theme_and_tag_counts_are_derived_from_the_corpus(self):
        self.build()
        connection = sqlite3.connect(self.output)
        self.addCleanup(connection.close)
        counts = dict(
            connection.execute("SELECT name, question_count FROM themes").fetchall()
        )
        self.assertEqual(counts["kubernetes"], 4)
        self.assertEqual(counts["linux"], 4)
        self.assertEqual(counts["queue-messaging"], 0)
        kubernetes = connection.execute(
            "SELECT difficulty_counts FROM themes WHERE name = 'kubernetes'"
        ).fetchone()[0]
        self.assertEqual(
            json.loads(kubernetes), {"junior": 1, "middle": 1, "senior": 1, "staff": 1}
        )
        storage = connection.execute(
            "SELECT question_count, lab_count FROM tags WHERE name = 'storage'"
        ).fetchone()
        self.assertEqual(tuple(storage), (2, 1))

    def test_rebuild_is_byte_identical(self):
        self.build()
        first = digest(self.output)
        second_output = self.tmp / "second.db"
        fixture_build(self.root, second_output)
        self.assertEqual(first, digest(second_output))

    def test_rebuild_over_an_existing_file_replaces_it(self):
        self.build()
        first = digest(self.output)
        self.build()
        self.assertEqual(first, digest(self.output))


class RecordsSnapshotProvenance(FixtureCorpus):
    """The store names the corpus snapshot it was built from."""

    def test_the_commit_and_timestamp_handed_in_are_recorded(self):
        self.build()
        meta = self.meta()
        self.assertEqual(meta["source_commit"], FIXTURE_COMMIT)
        self.assertEqual(meta["build_timestamp"], FIXTURE_TIMESTAMP)

    def test_the_digest_is_computed_by_the_pinned_recipe(self):
        summary = self.build()
        read = corpus.read_corpus(self.root)
        self.assertEqual(summary.content_digest, corpus.content_digest(read))
        self.assertEqual(self.meta()["content_digest"], corpus.content_digest(read))

    def test_two_runs_over_the_same_corpus_answer_the_same_digest(self):
        self.build()
        first = self.meta()["content_digest"]
        second_output = self.tmp / "again.db"
        fixture_build(self.root, second_output)
        self.assertEqual(first, self.meta(second_output)["content_digest"])

    def test_any_content_change_moves_the_digest(self):
        self.build()
        before = self.meta()["content_digest"]
        self.rewrite_question(
            "linux", "disk-full", "Recover a full filesystem", "Recover a full filesystem fast"
        )
        self.build()
        self.assertNotEqual(before, self.meta()["content_digest"])

    def test_the_digest_ignores_the_provenance_labels(self):
        """The digest is a function of the corpus alone, not of its labels."""
        self.build()
        before = self.meta()["content_digest"]
        ingest.build(
            self.root,
            self.tmp / "labelled.db",
            source_commit="f" * 40,
            build_timestamp="2001-02-03T04:05:06Z",
        )
        self.assertEqual(before, self.meta(self.tmp / "labelled.db")["content_digest"])

    def test_the_summary_describes_the_snapshot(self):
        summary = self.build()
        text = summary.describe()
        self.assertIn("Snapshot", text)
        self.assertIn(FIXTURE_COMMIT, text)
        self.assertIn(summary.content_digest, text)


class ResolvesProvenance(FixtureCorpus):
    """Where the commit comes from, and what happens where git cannot answer."""

    def test_a_root_outside_a_repository_is_refused_with_the_fix(self):
        with self.assertRaises(corpus.CorpusError) as caught:
            ingest.build(self.root, self.output)
        message = str(caught.exception)
        self.assertIn("source commit", message)
        self.assertIn("--source-commit", message)
        self.assertFalse(self.output.exists(), "a refused Ingest must not write a store")

    def test_an_explicit_commit_without_a_timestamp_falls_back_to_the_epoch(self):
        ingest.build(self.root, self.output, source_commit="deadbeef")
        self.assertEqual(self.meta()["build_timestamp"], ingest.EPOCH_BUILD_TIMESTAMP)
        self.assertEqual(self.meta()["source_commit"], "deadbeef")

    def test_the_command_line_accepts_explicit_provenance(self):
        completed = subprocess.run(
            [
                sys.executable, "-m", "contentdb.ingest",
                "--root", str(self.root), "--output", str(self.output),
                "--source-commit", "cafe123", "--build-timestamp", "2020-01-01T00:00:00Z",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        meta = self.meta()
        self.assertEqual(meta["source_commit"], "cafe123")
        self.assertEqual(meta["build_timestamp"], "2020-01-01T00:00:00Z")

    def test_git_answering_with_no_commit_is_refused(self):
        from unittest import mock

        with mock.patch.object(ingest.subprocess, "run") as run:
            run.return_value = mock.Mock(stdout="\n", returncode=0)
            with self.assertRaises(corpus.CorpusError) as caught:
                ingest.build(self.root, self.output)
        self.assertIn("--source-commit", str(caught.exception))


class RefusesContentItCannotTrust(FixtureCorpus):
    def test_valid_fixture_builds(self):
        """The control: every mutation below starts from a corpus that works."""
        self.assertEqual(self.build().questions, len(fixtures.QUESTIONS))

    def test_unparseable_front_matter(self):
        path = self.root / "questions" / "linux" / "disk-full.md"
        path.write_text("---\ntitle: Recover a full filesystem\n", encoding="utf-8")
        self.refuses(("questions/linux/disk-full.md", "closed with ---"))

    def test_missing_required_field(self):
        self.rewrite_question("linux", "disk-full", "type: troubleshooting\n", "")
        self.refuses(("questions/linux/disk-full.md", "type"))

    def test_undeclared_theme(self):
        path = self.root / "questions" / "undeclared" / "orphan.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            fixtures.question_markdown(
                fixtures.QuestionSpec(
                    "undeclared", "orphan", "Orphan", "junior", "theory", ("linux",), "Why?"
                )
            ),
            encoding="utf-8",
        )
        self.refuses(("questions/undeclared/orphan.md", "theme", "undeclared"))

    def test_theme_that_disagrees_with_its_folder(self):
        self.rewrite_question("linux", "disk-full", "theme: linux\n", "theme: kubernetes\n")
        self.refuses(("questions/linux/disk-full.md", "theme"))

    def test_tag_missing_from_tags_md(self):
        self.rewrite_question(
            "linux", "disk-full", "tags: [linux, storage, troubleshooting]", "tags: [linux, invented-tag]"
        )
        self.refuses(("questions/linux/disk-full.md", "tags", "invented-tag"))

    def test_invalid_difficulty(self):
        self.rewrite_question("linux", "disk-full", "difficulty: middle\n", "difficulty: expert\n")
        self.refuses(("questions/linux/disk-full.md", "difficulty", "expert"))

    def test_invalid_question_type(self):
        self.rewrite_question("linux", "disk-full", "type: troubleshooting\n", "type: quiz\n")
        self.refuses(("questions/linux/disk-full.md", "type", "quiz"))

    def test_missing_answer_guide(self):
        self.rewrite_question("linux", "disk-full", "## Answer guide", "## Notes")
        self.refuses(("questions/linux/disk-full.md", "answer_guide"))

    def test_lab_question_ref_that_resolves_to_nothing(self):
        self.rewrite_lab(
            "linux", "disk-lab", 'question_ref: "linux/disk-full.md"', 'question_ref: "linux/no-such.md"'
        )
        self.refuses(("labs/linux/disk-lab.md", "question_ref", "linux/no-such"))

    def test_lab_checklist_step_that_is_not_a_string(self):
        # An unquoted step reading `- Verify: the pod is ready` parses as a
        # mapping in this YAML subset.  Ingest must say so rather than store it.
        self.rewrite_lab(
            "linux",
            "disk-lab",
            '  - "Stand the environment up from nothing."',
            "  - Verify: the environment is up",
        )
        self.refuses(("labs/linux/disk-lab.md", "checklist"))

    def test_learning_path_step_pointing_at_a_missing_question(self):
        declaration = json.loads((self.root / "config" / "learning-paths.json").read_text(encoding="utf-8"))
        declaration["paths"][0]["steps"][0]["question"] = "questions/kubernetes/no-such.md"
        (self.root / "config" / "learning-paths.json").write_text(
            json.dumps(declaration, indent=2), encoding="utf-8"
        )
        self.refuses(("kubernetes-track", "questions/kubernetes/no-such.md"))

    def test_the_command_line_exits_non_zero_and_names_the_file(self):
        self.rewrite_question("linux", "disk-full", "difficulty: middle\n", "difficulty: expert\n")
        completed = subprocess.run(
            [sys.executable, "-m", "contentdb.ingest", "--root", str(self.root), "--output", str(self.output)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("questions/linux/disk-full.md", completed.stderr)
        self.assertIn("difficulty", completed.stderr)
        self.assertFalse(self.output.exists(), "a failed Ingest must not leave a half-written store")


class BuildsTheRealCorpus(unittest.TestCase):
    """The acceptance criteria that only the live corpus can answer."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="contentdb-real-"))
        cls.first = cls.tmp / "first.db"
        cls.second = cls.tmp / "second.db"
        cls.summary = ingest.build(ROOT, cls.first)
        ingest.build(ROOT, cls.second)
        cls.connection = sqlite3.connect(cls.first)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def count(self, table: str) -> int:
        return self.connection.execute(f"SELECT count(*) FROM {table}").fetchone()[0]

    def test_every_question_and_lab_in_the_corpus_is_stored(self):
        questions = len(list((ROOT / "questions").rglob("*.md")))
        labs = len(list((ROOT / "labs").rglob("*.md")))
        self.assertTrue(questions > 0 and labs > 0, "corpus walk found nothing")
        self.assertEqual(self.count("questions"), questions)
        self.assertEqual(self.count("labs"), labs)
        self.assertEqual(self.summary.questions, questions)
        self.assertEqual(self.summary.labs, labs)

    def test_two_runs_produce_identical_bytes(self):
        self.assertEqual(digest(self.first), digest(self.second))

    def test_provenance_is_answered_from_the_repository(self):
        """The real corpus carries no override, so git at the root answers."""
        meta = dict(
            self.connection.execute("SELECT key, value FROM store_meta").fetchall()
        )
        head = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        self.assertEqual(meta["source_commit"], head)
        self.assertRegex(meta["build_timestamp"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
        self.assertNotEqual(meta["build_timestamp"], ingest.EPOCH_BUILD_TIMESTAMP)
        self.assertEqual(self.summary.source_commit, head)
        self.assertTrue(self.summary.content_digest)

    def test_the_real_corpus_digest_follows_the_recipe(self):
        meta = dict(
            self.connection.execute("SELECT key, value FROM store_meta").fetchall()
        )
        self.assertEqual(meta["content_digest"], self.summary.content_digest)
        self.assertEqual(len(meta["content_digest"]), 64)
        self.assertRegex(meta["content_digest"], r"^[0-9a-f]{64}$")

    def test_content_hash_is_the_sha256_of_the_source_file(self):
        for table in ("questions", "labs"):
            for source_path, content_hash in self.connection.execute(
                f"SELECT source_path, content_hash FROM {table}"
            ):
                self.assertEqual(content_hash, digest(ROOT / source_path), source_path)

    def test_updated_at_is_an_iso_8601_utc_instant(self):
        for (updated_at,) in self.connection.execute("SELECT DISTINCT updated_at FROM questions"):
            self.assertRegex(updated_at, r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

    def test_every_theme_and_tag_used_is_declared(self):
        manifest = json.loads((ROOT / "config" / "content-manifest.json").read_text(encoding="utf-8"))
        declared = {theme["name"] for theme in manifest["themes"]}
        used = {row[0] for row in self.connection.execute("SELECT DISTINCT theme FROM questions")}
        used |= {row[0] for row in self.connection.execute("SELECT DISTINCT theme FROM labs")}
        self.assertTrue(used <= declared, f"undeclared Themes reached the store: {sorted(used - declared)}")
        known = corpus.known_tags(ROOT)
        stored = {row[0] for row in self.connection.execute("SELECT name FROM tags")}
        self.assertTrue(stored <= known, f"unknown Tags reached the store: {sorted(stored - known)}")

    def test_every_lab_question_ref_resolves_to_a_stored_question(self):
        dangling = self.connection.execute(
            "SELECT labs.id FROM labs LEFT JOIN questions ON questions.id = labs.question_ref"
            " WHERE questions.id IS NULL"
        ).fetchall()
        self.assertEqual(dangling, [])

    def test_foreign_keys_are_enforced_by_the_schema(self):
        connection = sqlite3.connect(self.first)
        self.addCleanup(connection.close)
        connection.execute("PRAGMA foreign_keys = ON")
        with self.assertRaises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO question_tags (question_id, tag) VALUES ('no/such', 'kubernetes')"
            )

    def test_the_command_line_builds_the_store(self):
        output = self.tmp / "cli.db"
        completed = subprocess.run(
            [sys.executable, "-m", "contentdb.ingest", "--output", str(output)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(output.is_file())
        self.assertIn("Question", completed.stdout)

    def test_the_store_is_never_committed(self):
        ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").split()
        self.assertIn("build/", ignored)


class ReadsADocumentWithoutAFileBehindIt(FixtureCorpus):
    """The corpus rules apply to text, so the Content API can run them on a write.

    Slice 4's write surface has to answer "would this record be a legal
    Question?" before anything is stored, and the only honest way to answer is
    to ask the code that reads the corpus. `read_question_document` and
    `read_lab_document` are that entry point: same rules, same errors, same
    `content_hash`, no file. The tests below pin the equivalence, because a
    document reader that quietly diverged from the file reader would hand the
    API a second, laxer definition of a valid Question.
    """

    def question_text(self, theme: str, slug: str) -> tuple[str, str]:
        path = self.root / "questions" / theme / f"{slug}.md"
        return path.read_text(encoding="utf-8"), f"questions/{theme}/{slug}.md"

    def vocabularies(self):
        return corpus.declared_themes(self.root), corpus.known_tags(self.root)

    def test_a_document_reads_exactly_as_the_file_it_came_from(self):
        themes, tags = self.vocabularies()
        specification = fixtures.QUESTIONS[0]
        text, context = self.question_text(specification.theme, specification.slug)
        from_file = corpus.read_question(
            self.root,
            self.root / "questions" / specification.theme / f"{specification.slug}.md",
            themes,
            tags,
            "2026-08-17T00:00:00Z",
        )
        from_text = corpus.read_question_document(text, context, themes, tags, "2026-08-17T00:00:00Z")
        self.assertEqual(from_file, from_text)

    def test_a_documents_hash_is_the_hash_of_the_bytes_export_would_write(self):
        themes, tags = self.vocabularies()
        specification = fixtures.QUESTIONS[0]
        text, context = self.question_text(specification.theme, specification.slug)
        record = corpus.read_question_document(text, context, themes, tags, "2026-08-17T00:00:00Z")
        self.assertEqual(record["content_hash"], hashlib.sha256(text.encode("utf-8")).hexdigest())

    def test_a_document_breaking_a_rule_fails_the_same_way_a_file_does(self):
        themes, tags = self.vocabularies()
        specification = fixtures.QUESTIONS[0]
        text, context = self.question_text(specification.theme, specification.slug)
        broken = text.replace(f"theme: {specification.theme}", "theme: atlantis", 1)
        with self.assertRaises(corpus.CorpusError) as caught:
            corpus.read_question_document(broken, context, themes, tags, "2026-08-17T00:00:00Z")
        self.assertIn(context, str(caught.exception))
        self.assertIn("theme", str(caught.exception))

    def test_a_lab_document_needs_its_question_to_resolve(self):
        themes, tags = self.vocabularies()
        specification = fixtures.LABS[0]
        path = self.root / "labs" / specification.theme / f"{specification.slug}.md"
        text = path.read_text(encoding="utf-8")
        context = f"labs/{specification.theme}/{specification.slug}.md"
        question_id = specification.question_ref.removesuffix(".md")
        resolved = corpus.read_lab_document(
            text, context, themes, tags, {question_id}, "2026-08-17T00:00:00Z"
        )
        self.assertEqual(resolved["question_ref"], question_id)
        with self.assertRaises(corpus.CorpusError) as caught:
            corpus.read_lab_document(text, context, themes, tags, set(), "2026-08-17T00:00:00Z")
        self.assertIn("question_ref", str(caught.exception))
