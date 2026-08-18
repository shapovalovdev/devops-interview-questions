"""Fixtures for the API test suite.

There is exactly one `conftest.py` for the API tests, and it holds no state.
The coverage census used to depend on a module-level set that ASGI middleware
mutated and on a collection hook that reordered the session so the census ran
last; both are gone. A census that only tells the truth when the whole suite
ran in the right order is not a census, and `test_coverage_census.py` now
drives every response it counts itself.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from support import client_for, demo_client, demo_corpus  # noqa: E402

if str(ROOT / "tests") not in sys.path:
    sys.path.insert(0, str(ROOT / "tests"))

import contentdb_fixtures  # noqa: E402  - a tests/ sibling, not a test module

from api.content import ContentStore  # noqa: E402
from contentdb import ingest  # noqa: E402


def _ingested(root: Path, database: Path) -> ContentStore:
    """Build a Content store the way a deployment does, then open it read-only.

    Every store-backed fixture goes through Ingest rather than through a
    hand-built SQLite file, because the point of these tests is that the API
    serves what Ingest produced — a fixture assembled by hand could agree with
    the API and disagree with the corpus.
    """
    ingest.build(root, database)
    return ContentStore.open(database)


@pytest.fixture(scope="session")
def fixture_store(tmp_path_factory):
    """The real Content store over the small corpus in `tests/contentdb_fixtures.py`.

    Predictable answers ("this filter matches exactly one Question") need a
    corpus that does not change when somebody writes a Question, which the
    committed one does daily.
    """
    directory = tmp_path_factory.mktemp("api-fixture-corpus")
    store = _ingested(contentdb_fixtures.write_corpus(directory / "corpus"), directory / "content.db")
    yield store
    store.close()


@pytest.fixture(scope="session")
def fixture_client(fixture_store):
    """A client over the fixture corpus, served through the real Content store."""
    return client_for(fixture_store)


@pytest.fixture(scope="session")
def corpus_store(tmp_path_factory):
    """The real Content store over the committed corpus.

    This is the fixture that catches schema drift in real content: a Question
    whose front matter the API cannot serve fails here and nowhere else.
    """
    directory = tmp_path_factory.mktemp("api-real-corpus")
    store = _ingested(ROOT, directory / "content.db")
    yield store
    store.close()


@pytest.fixture(scope="session")
def corpus_client(corpus_store):
    return client_for(corpus_store)


@pytest.fixture
def client():
    """A client over the demo corpus."""
    with demo_client() as test_client:
        yield test_client


@pytest.fixture
def store():
    """A fresh in-memory store holding the demo corpus."""
    return demo_corpus()


@pytest.fixture
def make_client():
    """Build a client over a store the test supplies."""
    return client_for
