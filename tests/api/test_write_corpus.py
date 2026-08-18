"""Writes, exercised against the real Content store rather than the fake.

Two defects in this epic have already come from an in-memory fake diverging
from the store that ships: a search hit shaped one way in the fake and another
in SQLite, and a raw store that satisfied the `Store` protocol structurally
while breaking four endpoints. Both were invisible to a suite that only ever
spoke to the fake.

So the write surface is swept here against a store built by Ingest from a real
corpus on disk — the same code path production runs, including the second
`mode=rw` connection the writer opens beside the read-only one. The final check
is the one that matters most for ADR 0001: a record written through the API must
still Export to Markdown, because a write that cannot be exported can never be
reviewed, and would leave the Drift gate permanently red.
"""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "tests") not in sys.path:
    sys.path.insert(0, str(ROOT / "tests"))

from fastapi.testclient import TestClient  # noqa: E402

import contentdb_fixtures as corpus_fixtures  # noqa: E402  - tests/ sibling
from api.app import create_app  # noqa: E402
from api.content import ContentStore  # noqa: E402
from contentdb import export, ingest  # noqa: E402
from support import (  # noqa: E402
    TEST_WRITE_CREDENTIAL,
    WRONG_WRITE_CREDENTIAL,
    environment,
    lab_body,
    question_body,
)

WRITE = {"X-API-Key": TEST_WRITE_CREDENTIAL}


class WritesAgainstTheRealStore(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="api-write-corpus-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.root = corpus_fixtures.write_corpus(self.tmp / "corpus")
        self.database = self.tmp / "content.db"
        ingest.build(self.root, self.database, **corpus_fixtures.PROVENANCE)
        self.store = ContentStore.open(self.database)
        self.addCleanup(self.store.close)
        self.client = TestClient(
            create_app(
                store=self.store,
                environ=environment(TEST_WRITE_CREDENTIAL, corpus_root=self.root),
            ),
            raise_server_exceptions=False,
        )
        self.existing = self.client.get("/api/v1/questions").json()["items"][0]

    def body(self, **overrides):
        return question_body(theme=self.existing["theme"], **overrides)

    # -- the journey ------------------------------------------------------

    def test_a_question_can_be_created_read_replaced_and_deleted(self):
        body = self.body(slug="written-through-the-api")
        url = f"/api/v1/questions/{body['theme']}/{body['slug']}"

        created = self.client.post("/api/v1/questions", json=body, headers=WRITE)
        self.assertEqual(created.status_code, 201, created.text)

        fetched = self.client.get(url)
        self.assertEqual(fetched.status_code, 200)
        self.assertEqual(fetched.json()["title"], body["title"])

        replaced = self.client.put(
            url,
            json=self.body(slug=body["slug"], title="Replaced through the API"),
            headers={**WRITE, "If-Match": fetched.headers["ETag"]},
        )
        self.assertEqual(replaced.status_code, 200, replaced.text)
        self.assertEqual(self.client.get(url).json()["title"], "Replaced through the API")

        deleted = self.client.delete(
            url, headers={**WRITE, "If-Match": self.client.get(url).headers["ETag"]}
        )
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_a_lab_written_through_the_api_keeps_its_question_link(self):
        body = lab_body(
            theme=self.existing["theme"],
            slug="lab-written-through-the-api",
            question_ref=self.existing["id"],
        )
        created = self.client.post("/api/v1/labs", json=body, headers=WRITE)
        self.assertEqual(created.status_code, 201, created.text)

        fetched = self.client.get(f"/api/v1/labs/{body['theme']}/{body['slug']}")
        self.assertEqual(fetched.json()["question_ref"], self.existing["id"])
        self.assertEqual(self.client.get(f"/api/v1/questions/{self.existing['id']}").status_code, 200)

    def test_a_write_survives_reopening_the_store(self):
        """It reached SQLite, not just the connection that served the request."""
        body = self.body(slug="persisted-through-the-api")
        self.assertEqual(
            self.client.post("/api/v1/questions", json=body, headers=WRITE).status_code, 201
        )
        self.store.close()

        reopened = ContentStore.open(self.database)
        self.addCleanup(reopened.close)
        client = TestClient(
            create_app(store=reopened, environ=environment(TEST_WRITE_CREDENTIAL, self.root))
        )
        self.assertEqual(
            client.get(f"/api/v1/questions/{body['theme']}/{body['slug']}").status_code, 200
        )

    # -- the refusals -----------------------------------------------------

    def test_the_real_store_refuses_the_same_things_the_fake_does(self):
        body = self.body(slug="refused-through-the-api")
        url = f"/api/v1/questions/{self.existing['id']}"
        for name, response in (
            ("no credential", self.client.post("/api/v1/questions", json=body)),
            (
                "wrong credential",
                self.client.post(
                    "/api/v1/questions", json=body, headers={"X-API-Key": WRONG_WRITE_CREDENTIAL}
                ),
            ),
            ("no If-Match", self.client.patch(url, json={"difficulty": "senior"}, headers=WRITE)),
            (
                "stale If-Match",
                self.client.patch(
                    url, json={"difficulty": "senior"}, headers={**WRITE, "If-Match": '"stale"'}
                ),
            ),
            (
                "unknown theme",
                self.client.post(
                    "/api/v1/questions",
                    json=question_body(slug="bad-theme", theme="not-a-theme"),
                    headers=WRITE,
                ),
            ),
        ):
            with self.subTest(refusal=name):
                self.assertIn(response.status_code, (401, 403, 412, 422, 428))
                self.assertTrue(
                    response.headers["content-type"].startswith("application/problem+json")
                )

    def test_a_refused_write_leaves_the_store_untouched(self):
        url = f"/api/v1/questions/{self.existing['id']}"
        before = self.client.get(url).json()
        self.client.patch(url, json={"difficulty": "senior"}, headers={"X-API-Key": WRONG_WRITE_CREDENTIAL})
        self.client.patch(url, json={"difficulty": "senior"}, headers={**WRITE, "If-Match": '"stale"'})
        self.assertEqual(self.client.get(url).json(), before)

    def test_a_lab_can_be_deleted_through_the_real_store(self):
        body = lab_body(
            theme=self.existing["theme"],
            slug="lab-to-delete",
            question_ref=self.existing["id"],
        )
        self.assertEqual(self.client.post("/api/v1/labs", json=body, headers=WRITE).status_code, 201)
        url = f"/api/v1/labs/{body['theme']}/{body['slug']}"
        etag = self.client.get(url).headers["ETag"]
        self.assertEqual(self.client.delete(url, headers={**WRITE, "If-Match": etag}).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_every_write_leaves_an_audit_entry(self):
        """Export and a Drift investigation both need to know what changed."""
        body = self.body(slug="audited-write")
        identifier = f"{body['theme']}/{body['slug']}"
        self.client.post("/api/v1/questions", json=body, headers=WRITE)
        url = f"/api/v1/questions/{identifier}"
        self.client.patch(
            url,
            json={"difficulty": "senior"},
            headers={**WRITE, "If-Match": self.client.get(url).headers["ETag"]},
        )
        self.client.delete(
            url, headers={**WRITE, "If-Match": self.client.get(url).headers["ETag"]}
        )

        trail = self.store.audit_trail(identifier)
        self.assertEqual([entry["method"] for entry in trail], ["POST", "PATCH", "DELETE"])
        self.assertIsNone(trail[-1]["content_hash"], "a delete leaves no content to hash")

    def test_a_refused_write_leaves_no_audit_entry(self):
        body = self.body(slug="never-written")
        self.client.post("/api/v1/questions", json=body)  # no credential
        self.assertEqual(self.store.audit_trail(f"{body['theme']}/{body['slug']}"), ())

    # -- the promise ADR 0001 makes ---------------------------------------

    def test_a_record_written_through_the_api_exports_to_markdown(self):
        """A write that Export cannot render could never be reviewed in git."""
        body = self.body(slug="exported-after-the-api-wrote-it")
        self.assertEqual(
            self.client.post("/api/v1/questions", json=body, headers=WRITE).status_code, 201
        )

        record = self.store.get_question(f"{body['theme']}/{body['slug']}")
        self.assertIsNotNone(record, "the write never reached the store")

        rendered = export.render_question(record)
        self.assertTrue(rendered.startswith("---\n"))
        self.assertIn(f"title: {body['title']}", rendered)
        self.assertTrue(rendered.endswith("\n"))

        written = export.write(self.root, record, "question")
        self.assertTrue(written)
        on_disk = self.root / str(record["source_path"])
        self.assertTrue(on_disk.exists(), "Export did not place the file where the record says")
        self.assertEqual(on_disk.read_text(encoding="utf-8"), rendered)

    def test_the_exported_file_can_be_ingested_again(self):
        """The full loop: API write, Export, Ingest — no Drift left behind."""
        body = self.body(slug="round-trips-after-an-api-write")
        self.client.post("/api/v1/questions", json=body, headers=WRITE)
        record = self.store.get_question(f"{body['theme']}/{body['slug']}")
        export.write(self.root, record, "question")

        rebuilt = self.tmp / "rebuilt.db"
        ingest.build(self.root, rebuilt, **corpus_fixtures.PROVENANCE)
        from contentdb.store import Store

        reingested = Store(rebuilt)
        self.addCleanup(reingested.close)
        again = reingested.get_question(f"{body['theme']}/{body['slug']}")
        self.assertIsNotNone(again, "the exported file did not come back through Ingest")
        self.assertEqual(again["title"], body["title"])
        self.assertEqual(list(again["tags"]), list(body["tags"]))


if __name__ == "__main__":
    unittest.main()
