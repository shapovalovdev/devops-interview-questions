"""The snapshot identity: `GET /api/v1/meta` and the header it names.

The snapshot-service epic pins three things this module holds together:

* **`GET /api/v1/meta`** serves the provenance Ingest recorded — which commit
  the corpus came from, the corpus-wide digest, when that commit was made —
  plus the contract's own version and licensing, all anonymously;
* **every response carries `X-Content-Snapshot`**, the digest, stamped by
  app-level middleware that no route can opt out of — including error
  responses, including the `500` an outermost renderer answers with when a
  handler raises past every other layer;
* **the digest is the pinned recipe**, recomputable by anyone from the listing
  endpoints alone: sha256 over the sorted `(id, content_hash)` pairs of the
  Questions and Labs the snapshot holds.
"""

from __future__ import annotations

import hashlib
import sqlite3

import pytest

from support import (
    DEMO_QUESTION,
    ExplodingStore,
    client_for,
    demo_corpus,
)

from api.app import ATTRIBUTION_URL, CONTRACT_VERSION, SNAPSHOT_HEADER, StoreDoesNotConform, create_app
from api.store import corpus_digest
from api.testing import DEMO_BUILD_TIMESTAMP, DEMO_SOURCE_COMMIT

import contentdb_fixtures  # noqa: F401  - puts the fixture corpus builder in reach


# ------------------------------------------------------------- the endpoint


def test_meta_names_the_snapshot_the_service_serves(client):
    store = demo_corpus()
    body = client.get("/api/v1/meta").json()
    assert body == {
        "source_commit": DEMO_SOURCE_COMMIT,
        "content_digest": corpus_digest(store.questions, store.labs),
        "api_version": CONTRACT_VERSION,
        "build_timestamp": DEMO_BUILD_TIMESTAMP,
        "license": {
            "name": "CC BY 4.0",
            "spdx_id": "CC-BY-4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/",
        },
        "attribution": ATTRIBUTION_URL,
    }


def test_meta_is_anonymous_and_needs_nothing_from_the_caller(client):
    response = client.get("/api/v1/meta")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")


def test_meta_serves_the_store_not_runtime_inspection(make_client):
    """The digest is read from the store at startup, not recomputed per request."""
    store = demo_corpus()
    client = make_client(store)
    before = client.get("/api/v1/meta").json()["content_digest"]
    # A record removed from the store afterwards does not move what the service
    # says: the snapshot identity was resolved when this app was built.
    question = store.get_question("kubernetes/demo-pod-disruption")
    store.questions.remove(question)
    assert before == client.get("/api/v1/meta").json()["content_digest"]
    assert before == client.get("/api/v1/health").headers[SNAPSHOT_HEADER]


# -------------------------------------------------------- the snapshot header


def test_the_snapshot_header_is_on_a_success_response(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.headers[SNAPSHOT_HEADER] == client.get("/api/v1/meta").json()["content_digest"]


def test_the_snapshot_header_is_on_a_read_error_response(client):
    response = client.get("/api/v1/questions/kubernetes/nothing-here")
    assert response.status_code == 404
    assert response.headers[SNAPSHOT_HEADER] == client.get("/api/v1/meta").json()["content_digest"]


def test_the_snapshot_header_is_on_a_validation_error_response(client):
    response = client.get("/api/v1/questions?limit=0")
    assert response.status_code == 422
    assert response.headers[SNAPSHOT_HEADER]


def test_the_snapshot_header_is_on_a_write_refusal(make_client):
    response = make_client(demo_corpus(), credential=None).post(
        "/api/v1/questions", json={}
    )
    assert response.status_code == 422
    assert response.headers[SNAPSHOT_HEADER]


def test_the_snapshot_header_is_on_an_auth_refusal(client):
    from support import QUESTION_WRITE

    response = client.post("/api/v1/questions", json=QUESTION_WRITE)
    assert response.status_code == 401
    assert response.headers[SNAPSHOT_HEADER]


def test_the_snapshot_header_is_on_a_500_rendered_outside_every_layer(make_client):
    """The 500 renderer sits above all user middleware; the header must beat it.

    This is the response the outermost `ServerErrorMiddleware` answers when a
    handler raises past everything — the case a route decorator or an ordinary
    `add_middleware` placement cannot cover, and the reason the snapshot stamp
    wraps the whole built stack.
    """
    response = make_client(ExplodingStore()).get("/api/v1/questions")
    assert response.status_code == 500
    assert response.headers[SNAPSHOT_HEADER]


def test_the_snapshot_header_is_on_a_204_delete(client):
    from support import TEST_WRITE_CREDENTIAL

    identifier = "kubernetes/demo-pod-disruption"
    etag = client.get(f"/api/v1/questions/{identifier}").headers["ETag"]
    response = client.delete(
        f"/api/v1/questions/{identifier}",
        headers={"If-Match": etag, "X-API-Key": TEST_WRITE_CREDENTIAL},
    )
    assert response.status_code == 204
    assert response.headers[SNAPSHOT_HEADER]


def test_the_snapshot_header_is_on_the_304_of_a_conditional_read(client):
    first = client.get(DEMO_QUESTION)
    again = client.get(DEMO_QUESTION, headers={"If-None-Match": first.headers["ETag"]})
    assert again.status_code == 304
    assert again.headers[SNAPSHOT_HEADER]


def test_the_digest_moves_only_when_the_corpus_moves(make_client):
    store = demo_corpus()
    client = make_client(store)
    header = client.get("/api/v1/health").headers[SNAPSHOT_HEADER]
    # A write through the fake changes the records it holds, and the fake's
    # digest — recomputed from the records — moves with them. The recipe reads
    # `(id, content_hash)`, so it is the hash, not the title, that has to move.
    record = store.get_question("kubernetes/demo-pod-disruption")
    store.write_question({**record, "content_hash": "sha256:moved"}, "PATCH")
    moved = make_client(store).get("/api/v1/health").headers[SNAPSHOT_HEADER]
    assert moved != header
    assert moved == corpus_digest(store.questions, store.labs)


# ------------------------------------------------ the recipe, pinned end to end


def test_the_served_digest_is_recomputable_from_the_listing_endpoints(client):
    """The recipe the contract publishes, executed by a downstream consumer."""
    meta = client.get("/api/v1/meta").json()
    pairs = []
    for path in ("/api/v1/questions", "/api/v1/labs"):
        offset = 0
        while True:
            page = client.get(f"{path}?limit=200&offset={offset}").json()
            pairs += [(item["id"], item["content_hash"]) for item in page["items"]]
            offset += page["limit"]
            if offset >= page["total"]:
                break
    material = "".join(f"{identifier} {content_hash}\n" for identifier, content_hash in sorted(pairs))
    assert meta["content_digest"] == hashlib.sha256(material.encode("utf-8")).hexdigest()


def test_the_two_copies_of_the_recipe_agree(fixture_store, tmp_path):
    """`contentdb` computes the digest at Ingest; the seam carries its own copy."""
    from contentdb import corpus as content_corpus
    from contentdb import ingest

    root = contentdb_fixtures.write_corpus(tmp_path / "corpus")
    database = tmp_path / "content.db"
    ingest.build(root, database, **contentdb_fixtures.PROVENANCE)
    recorded = dict(
        sqlite3.connect(database).execute("SELECT key, value FROM store_meta")
    )["content_digest"]
    read = content_corpus.read_corpus(root)
    assert recorded == content_corpus.content_digest(read)
    assert recorded == corpus_digest(read.questions, read.labs)
    # And the adapter serves exactly what Ingest recorded:
    assert fixture_store.get_meta()["content_digest"] == recorded


# ------------------------------------------------------ startup is strict


def test_a_store_that_cannot_name_its_snapshot_is_refused_at_startup():
    class SnapshotlessStore(demo_corpus().__class__):
        def get_meta(self):
            raise RuntimeError("no metadata table")

    with pytest.raises(StoreDoesNotConform) as error:
        create_app(store=SnapshotlessStore())
    message = str(error.value)
    assert "get_meta" in message
    assert "contentdb.ingest" in message, "the refusal has to name the fix"


def test_a_store_whose_meta_is_not_a_mapping_of_strings_is_refused():
    class HollowStore(demo_corpus().__class__):
        def get_meta(self):
            return {"source_commit": "ok", "content_digest": "", "build_timestamp": "ok"}

    with pytest.raises(StoreDoesNotConform) as error:
        create_app(store=HollowStore())
    assert "content_digest" in str(error.value)


def test_the_real_store_serves_its_own_provenance(fixture_client):
    meta = fixture_client.get("/api/v1/meta").json()
    assert meta["source_commit"] == contentdb_fixtures.PROVENANCE["source_commit"]
    assert meta["build_timestamp"].startswith("2026-08-18T00:00:00")
    assert meta["content_digest"] == fixture_client.get("/api/v1/health").headers[SNAPSHOT_HEADER]
