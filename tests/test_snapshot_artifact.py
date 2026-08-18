"""The release artifact is reproducible and verifiable without a live API."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_snapshot_artifact as snapshots

import contentdb_fixtures as fixtures


COMMIT = "a" * 40
TIMESTAMP = "2026-08-18T00:00:00Z"


class SnapshotArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temporary = Path(tempfile.mkdtemp(prefix="snapshot-artifact-"))
        self.addCleanup(shutil.rmtree, self.temporary, True)
        self.corpus = fixtures.write_corpus(self.temporary / "corpus")

    def build(self, destination: str = "artifacts"):
        return snapshots.build_artifact(
            self.corpus,
            self.temporary / destination,
            source_commit=COMMIT,
            build_timestamp=TIMESTAMP,
        )

    def test_metadata_matches_the_store_and_the_digest_names_every_path(self):
        artifact = self.build()
        self.assertEqual(artifact.archive.name, f"content-snapshot-{artifact.content_digest}.tar.gz")
        self.assertEqual(artifact.checksum.name, artifact.archive.name + ".sha256")
        verified = snapshots.verify_artifact(artifact.archive, artifact.checksum)
        self.assertEqual(verified["source_commit"], COMMIT)
        self.assertEqual(verified["content_digest"], artifact.content_digest)
        self.assertEqual(verified["api_version"], "v1")
        self.assertEqual(verified["build_timestamp"], TIMESTAMP)
        self.assertEqual(verified["license"], snapshots.LICENSE)
        self.assertEqual(verified["attribution"], snapshots.ATTRIBUTION)

    def test_same_corpus_and_provenance_produce_identical_archives(self):
        first = self.build("first")
        second = self.build("second")
        self.assertEqual(first.archive.read_bytes(), second.archive.read_bytes())
        self.assertEqual(first.checksum.read_bytes(), second.checksum.read_bytes())

    def test_verification_rejects_a_tampered_contained_file(self):
        artifact = self.build()
        tampered = self.temporary / "tampered.tar.gz"
        with tarfile.open(artifact.archive, "r:gz") as source:
            files = {member.name: source.extractfile(member).read() for member in source.getmembers()}
        files["snapshot.json"] += b" "
        snapshots.write_archive(tampered, files, snapshots.timestamp_seconds(TIMESTAMP))
        with self.assertRaisesRegex(ValueError, "checksum"):
            snapshots.verify_artifact(tampered)

    def test_extracted_archive_has_everything_needed_for_offline_verification(self):
        artifact = self.build()
        extraction = self.temporary / "extracted"
        with tarfile.open(artifact.archive, "r:gz") as bundle:
            bundle.extractall(extraction, filter="data")
        files = {path.name: path.read_bytes() for path in extraction.iterdir()}
        checksums = snapshots.parse_checksums(files["SHA256SUMS"])
        self.assertEqual(checksums["content.db"], hashlib.sha256(files["content.db"]).hexdigest())
        self.assertEqual(checksums["snapshot.json"], hashlib.sha256(files["snapshot.json"]).hexdigest())
        self.assertEqual(
            snapshots.digest_from_store(extraction / "content.db"),
            snapshots.store_meta(extraction / "content.db")["content_digest"],
        )
