"""Tests for track manifests ingestion, DAG integrity, cycle detection, and store reads."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import ingest, store
from contentdb.corpus import CorpusError, read_corpus
import contentdb_fixtures as fixtures


class ContentDbTracksTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="contentdb-tracks-"))
        self.root = fixtures.write_corpus(self.tmp / "corpus")
        self.database = self.tmp / "content.db"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_track_manifest(self, filename: str, data: dict) -> Path:
        tracks_dir = self.root / "tracks"
        tracks_dir.mkdir(parents=True, exist_ok=True)
        path = tracks_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f)
        return path

    def test_valid_track_manifest_ingestion_and_store_reads(self):
        track_data = {
            "id": "k8s-core-track",
            "name": "Kubernetes Core Competencies",
            "description": "Comprehensive journey into Kubernetes scheduling and policies",
            "icon": "☸️",
            "color": "#326ce5",
            "target_audience": "DevOps Engineers",
            "certifications": ["CKA", "CKAD"],
            "steps": [
                {
                    "id": "step-sched",
                    "skill_id": "k8s-sched",
                    "title": "Pod Scheduling Mechanics",
                    "difficulty": "middle",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/pod-scheduling",
                    "lab_slug": "kubernetes/admission-lab",
                    "concepts": ["NodeSelector", "Tolerations", "Affinity"],
                    "why": "Master scheduling before admission policies",
                    "prerequisites": [],
                },
                {
                    "id": "step-adm",
                    "skill_id": "k8s-adm",
                    "title": "Admission Webhooks",
                    "difficulty": "senior",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/admission-policy",
                    "lab_slug": "kubernetes/admission-lab",
                    "concepts": ["ValidatingWebhook", "MutatingWebhook"],
                    "why": "Enforce policies across the cluster",
                    "prerequisites": ["step-sched"],
                },
            ],
        }
        self.write_track_manifest("k8s-core.yml", track_data)

        summary = ingest.build(self.root, self.database, **fixtures.PROVENANCE)
        self.assertGreaterEqual(summary.learning_paths, 1)

        db_store = store.Store(self.database)
        try:
            paths = db_store.list_learning_paths()
            slugs = [p["slug"] for p in paths]
            self.assertIn("k8s-core-track", slugs)

            path = db_store.get_learning_path("k8s-core-track")
            self.assertIsNotNone(path)
            self.assertEqual(path["title"], "Kubernetes Core Competencies")
            self.assertEqual(path["icon"], "☸️")
            self.assertEqual(path["color"], "#326ce5")
            self.assertEqual(path["certifications"], ["CKA", "CKAD"])
            self.assertEqual(len(path["steps"]), 2)

            step1 = path["steps"][0]
            self.assertEqual(step1["step_id"], "step-sched")
            self.assertEqual(step1["skill_id"], "k8s-sched")
            self.assertEqual(step1["question_id"], "kubernetes/pod-scheduling")
            self.assertEqual(step1["concepts"], ["NodeSelector", "Tolerations", "Affinity"])
            self.assertEqual(step1["prerequisites"], [])

            step2 = path["steps"][1]
            self.assertEqual(step2["step_id"], "step-adm")
            self.assertEqual(step2["prerequisites"], ["step-sched"])
        finally:
            db_store.close()

    def test_cycle_detection_raises_corpus_error(self):
        cyclic_track = {
            "id": "cyclic-track",
            "name": "Cyclic Dependency Track",
            "description": "Invalid cyclic track",
            "steps": [
                {
                    "id": "step-a",
                    "title": "Step A",
                    "difficulty": "junior",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/pod-scheduling",
                    "prerequisites": ["step-b"],
                },
                {
                    "id": "step-b",
                    "title": "Step B",
                    "difficulty": "middle",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/admission-policy",
                    "prerequisites": ["step-a"],
                },
            ],
        }
        self.write_track_manifest("cyclic.yml", cyclic_track)

        with self.assertRaises(CorpusError) as ctx:
            read_corpus(self.root)
        self.assertIn("cycle detected", str(ctx.exception).lower())

    def test_self_dependency_raises_corpus_error(self):
        self_dep_track = {
            "id": "self-dep-track",
            "name": "Self Dependent Track",
            "description": "Step depends on itself",
            "steps": [
                {
                    "id": "step-self",
                    "title": "Self Step",
                    "difficulty": "junior",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/pod-scheduling",
                    "prerequisites": ["step-self"],
                }
            ],
        }
        self.write_track_manifest("self_dep.yml", self_dep_track)

        with self.assertRaises(CorpusError) as ctx:
            read_corpus(self.root)
        self.assertIn("cannot depend on itself", str(ctx.exception).lower())

    def test_missing_question_reference_raises_corpus_error(self):
        missing_q_track = {
            "id": "missing-q-track",
            "name": "Missing Question Track",
            "description": "References unknown question",
            "steps": [
                {
                    "id": "step-1",
                    "title": "Missing Q Step",
                    "difficulty": "junior",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/no-such-question",
                    "prerequisites": [],
                }
            ],
        }
        self.write_track_manifest("missing_q.yml", missing_q_track)

        with self.assertRaises(CorpusError) as ctx:
            read_corpus(self.root)
        self.assertIn("missing Question", str(ctx.exception))

    def test_duplicate_step_id_raises_corpus_error(self):
        dup_step_track = {
            "id": "dup-step-track",
            "name": "Duplicate Step Track",
            "description": "Has duplicate step id",
            "steps": [
                {
                    "id": "step-dup",
                    "title": "Step 1",
                    "difficulty": "junior",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/pod-scheduling",
                },
                {
                    "id": "step-dup",
                    "title": "Step 2",
                    "difficulty": "middle",
                    "theme": "kubernetes",
                    "question_id": "kubernetes/admission-policy",
                },
            ],
        }
        self.write_track_manifest("dup_step.yml", dup_step_track)

        with self.assertRaises(CorpusError) as ctx:
            read_corpus(self.root)
        self.assertIn("duplicate step id", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
