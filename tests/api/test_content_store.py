"""Wiring the real Content store in behind the `Store` seam.

`tests/test_contentdb_store.py` already holds `contentdb.store.Store` to its own
documented answers. What is untested until here is the adapter in
`api/content.py`: that it hands the API the shapes `api/store.py` documents,
that it fails loudly when the store file is missing or is not a database, and
that it reaches the service through `CONTENT_API_STORE` and no second door.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest

from support import ROOT  # noqa: F401  - puts the repository root on sys.path

from api.app import STORE_ENVIRONMENT_VARIABLE, create_app
from api.content import (
    DEFAULT_STORE_PATH,
    INGEST_COMMAND,
    STORE_PATH_VARIABLE,
    ContentStore,
    ContentStoreUnavailable,
    content_store,
    rank_score,
    read_guard,
    store_path,
)
from api.store import LabQuery, Page, QuestionQuery, SearchQuery, Store

if str(ROOT / "tests") not in sys.path:
    sys.path.insert(0, str(ROOT / "tests"))

import contentdb_fixtures  # noqa: E402


# ------------------------------------------------------------- the seam


def test_the_adapter_satisfies_the_store_protocol(fixture_store):
    assert isinstance(fixture_store, Store)


def test_every_list_read_comes_back_in_the_api_s_own_page(fixture_store):
    """`contentdb` has a `Page` of its own; only the seam's shape may cross."""
    for page in (
        fixture_store.list_questions(QuestionQuery()),
        fixture_store.list_labs(LabQuery()),
        fixture_store.list_themes(),
        fixture_store.list_tags(),
        fixture_store.list_learning_paths(),
        fixture_store.search(SearchQuery(q="admission")),
    ):
        assert isinstance(page, Page), page
        assert page.total >= len(page.items)
        for record in page.items:
            assert isinstance(record, dict)


def test_a_catalogue_reports_its_own_size_as_the_total(fixture_store):
    """Themes, tags, and paths are bounded, so the whole catalogue is the page."""
    for page in (
        fixture_store.list_themes(),
        fixture_store.list_tags(),
        fixture_store.list_learning_paths(),
    ):
        assert page.total == len(page.items)
        assert page.items


def test_a_search_hit_carries_its_kind_score_and_whole_item(fixture_store):
    hits = fixture_store.search(SearchQuery(q="admission")).items
    assert hits, "the fixture corpus mentions admission control, so this cannot be empty"
    for hit in hits:
        assert set(hit) == {"kind", "score", "item"}
        assert hit["kind"] in {"question", "lab"}
        assert hit["item"]["id"]
    assert [hit["score"] for hit in hits] == sorted((hit["score"] for hit in hits), reverse=True)


def test_the_score_keeps_falling_across_a_page_boundary(fixture_store):
    """Rank is global, so page two must not restart at the top score."""
    first = fixture_store.search(SearchQuery(q="kubernetes", limit=1)).items
    second = fixture_store.search(SearchQuery(q="kubernetes", limit=1, offset=1)).items
    assert first and second
    assert first[0]["score"] > second[0]["score"]


def test_rank_score_is_strictly_decreasing():
    assert rank_score(0) > rank_score(1) > rank_score(50)
    assert rank_score(0) == 1.0


def test_a_query_the_store_cannot_parse_is_an_invalid_query(fixture_store):
    """FTS5 syntax errors are the client's fault and must not read as faults."""
    from api.store import InvalidQuery

    with pytest.raises(InvalidQuery):
        fixture_store.search(SearchQuery(q='"unbalanced'))
    with pytest.raises(InvalidQuery):
        fixture_store.list_questions(QuestionQuery(q='"unbalanced'))


# --------------------------------------------------- sharing one connection


def test_the_read_guard_is_re_entrant():
    """`search()` reads through the guard while already holding it."""
    lock = read_guard()
    with lock:
        assert lock.acquire(blocking=False), "a plain lock would deadlock inside search()"
        lock.release()


def test_one_shared_store_answers_readers_on_many_threads(fixture_store):
    """The connection is shared, so concurrent reads must all get the truth."""
    import threading

    expected = fixture_store.list_questions(QuestionQuery()).total
    seen: list[int] = []
    barrier = threading.Barrier(4)

    def read() -> None:
        barrier.wait()
        seen.append(fixture_store.list_questions(QuestionQuery(theme="kubernetes")).total)
        seen.append(fixture_store.search(SearchQuery(q="kubernetes")).total)

    threads = [threading.Thread(target=read) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert len(seen) == 8
    assert all(count > 0 for count in seen)
    assert expected > 0


def test_search_resolves_its_hits_without_deadlocking_on_its_own_guard(fixture_store):
    """Regression: `search()` re-enters the lock once per hit it resolves."""
    assert fixture_store.search(SearchQuery(q="admission")).items


# ------------------------------------------------------------ failing fast


def test_a_missing_store_names_the_path_and_the_ingest_command(tmp_path):
    missing = tmp_path / "content.db"
    with pytest.raises(ContentStoreUnavailable) as error:
        ContentStore.open(missing)
    message = str(error.value)
    assert str(missing) in message
    assert INGEST_COMMAND in message


def test_a_file_that_is_not_a_database_fails_the_same_way(tmp_path):
    """An unreadable store must not become an API that serves nothing, quietly."""
    corrupt = tmp_path / "content.db"
    corrupt.write_text("this is not a SQLite file\n", encoding="utf-8")
    with pytest.raises(ContentStoreUnavailable) as error:
        ContentStore.open(corrupt)
    assert INGEST_COMMAND in str(error.value)


def test_the_error_is_not_a_bare_sqlite_error(tmp_path):
    corrupt = tmp_path / "content.db"
    corrupt.write_bytes(b"\x00\x01\x02")
    with pytest.raises(ContentStoreUnavailable) as error:
        ContentStore.open(corrupt)
    assert not isinstance(error.value, sqlite3.Error)


# --------------------------------------------------------- the environment


def test_the_store_path_defaults_to_where_ingest_writes():
    assert store_path({}) == DEFAULT_STORE_PATH
    assert store_path({STORE_PATH_VARIABLE: "  "}) == DEFAULT_STORE_PATH
    assert store_path({STORE_PATH_VARIABLE: "/tmp/other.db"}) == Path("/tmp/other.db")


def test_the_service_reaches_the_real_store_through_content_api_store(monkeypatch, tmp_path):
    """One door: `CONTENT_API_STORE`, pointed at this module's factory."""
    root = contentdb_fixtures.write_corpus(tmp_path / "corpus")
    from contentdb import ingest

    database = tmp_path / "content.db"
    ingest.build(root, database)

    monkeypatch.setenv(STORE_PATH_VARIABLE, str(database))
    monkeypatch.setenv(STORE_ENVIRONMENT_VARIABLE, "api.content:content_store")
    application = create_app()
    try:
        from fastapi.testclient import TestClient

        with TestClient(application) as client:
            body = client.get("/api/v1/questions?theme=kubernetes").json()
        assert body["total"] > 0
        assert all(item["theme"] == "kubernetes" for item in body["items"])
    finally:
        application.state.store.close()


def test_the_factory_reads_the_configured_path(monkeypatch, tmp_path):
    monkeypatch.setenv(STORE_PATH_VARIABLE, str(tmp_path / "nowhere.db"))
    with pytest.raises(ContentStoreUnavailable):
        content_store()
