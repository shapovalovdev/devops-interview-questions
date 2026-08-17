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
