"""The coverage census: every response the contract promises must be exercised.

The rule the epic sets is mechanical, not editorial. Walk `api/openapi.yaml`;
for an operation marked `x-implementation: implemented`, every documented status
code must be produced by a real request; for one marked `stub`, its `501` must
be. Flipping a marker to `implemented` therefore immediately obliges the slice
that flipped it to produce the operation's whole set of documented responses.

**Why this module drives the requests itself.** The earlier census read a
module-level set that ASGI middleware appended to, and a `conftest.py` hook
reordered the session so it ran last. That census reported success whenever it
happened to run alone — under `-k`, under `-x` after an early failure, under
`pytest-xdist`, where each worker sees only the requests made in its own
process. A census that passes because nothing ran is worse than no census: it
converts an absence of evidence into a green build.

So there is no shared state and no ordering requirement here. `census()` is a
single test that builds its own clients, issues every request itself, and
compares what it got against what the contract promises. It cannot be partially
run: either it runs and every promise is checked, or it does not run at all and
nothing claims otherwise.
"""

from __future__ import annotations

from typing import Any, Callable

import yaml

from support import (
    CONTRACT_PATH,
    ExplodingStore,
    STUB_REQUESTS,
    client_for,
    demo_client,
    demo_corpus,
    send,
)

METHODS = ("get", "put", "post", "delete", "patch")
MARKER = "x-implementation"
IMPLEMENTED = "implemented"
STUB = "stub"


def load_contract() -> dict[str, Any]:
    return yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8"))


def promised_responses(contract: dict[str, Any]) -> dict[tuple[str, str], set[str]]:
    """What each operation owes a test today, according to its marker."""
    owed: dict[tuple[str, str], set[str]] = {}
    for path, item in contract["paths"].items():
        for method, operation in item.items():
            if method not in METHODS:
                continue
            marker = operation.get(MARKER)
            assert marker in (IMPLEMENTED, STUB), (
                f"{method.upper()} {path} carries {MARKER}={marker!r}; the census cannot "
                "tell what it owes"
            )
            if marker == IMPLEMENTED:
                owed[(path, method)] = {str(code) for code in operation["responses"]}
            else:
                owed[(path, method)] = {"501"}
    return owed


def implemented_producers() -> dict[tuple[str, str, str], Callable[[], int]]:
    """One request per documented response of every implemented operation."""
    client = demo_client()
    failing = client_for(ExplodingStore())
    return {
        ("/api/v1/health", "get", "200"): lambda: client.get("/api/v1/health").status_code,
        ("/api/v1/questions", "get", "200"): lambda: client.get("/api/v1/questions").status_code,
        # The 422 is a real out-of-range limit, not a fabricated one: the census
        # is only worth running if the requests it makes are requests a client
        # could make.
        ("/api/v1/questions", "get", "422"): lambda: client.get(
            "/api/v1/questions?limit=0"
        ).status_code,
        ("/api/v1/questions", "get", "500"): lambda: failing.get("/api/v1/questions").status_code,
    }


def stub_producers() -> dict[tuple[str, str, str], Callable[[], int]]:
    """One request per stubbed operation, each owing a `501`."""
    client = demo_client()
    return {
        (path, method, "501"): (lambda p=path, m=method: send(client, p, m).status_code)
        for path, method in STUB_REQUESTS
    }


def test_the_census_covers_every_response_the_contract_promises():
    contract = load_contract()
    owed = promised_responses(contract)
    required = {(path, method, status) for (path, method), codes in owed.items() for status in codes}

    assert len(owed) == 19, (
        "the census expects the epic's 19 v1 operations; api/openapi.yaml describes "
        f"{len(owed)}. If an operation was added or removed, say so on the epic first."
    )
    assert required, "the census found nothing to check, which means it is not checking"

    producers = {**implemented_producers(), **stub_producers()}

    unproduced = sorted(required - set(producers))
    unpromised = sorted(set(producers) - required)
    assert not unproduced and not unpromised, (
        "the census and api/openapi.yaml disagree about what needs a test.\n"
        f"  promised by the contract but never exercised: {unproduced or 'none'}\n"
        f"  exercised here but not promised anywhere: {unpromised or 'none'}\n"
        "Add a request to tests/api/support.py (for a stub) or to implemented_producers() "
        "(for an implemented operation) — or correct the contract."
    )

    wrong: list[str] = []
    for key in sorted(required):
        path, method, status = key
        observed = producers[key]()
        if str(observed) != status:
            wrong.append(
                f"{method.upper()} {path} was exercised for {status} but answered {observed}"
            )
    assert not wrong, "the census exercised these responses and got something else:\n  " + "\n  ".join(wrong)


def test_the_census_demands_more_the_moment_an_operation_is_implemented():
    """Prove the marker is load-bearing, not decorative.

    Flipping `createQuestion` to `implemented` in a copy of the contract must
    make the census require its `401`, `403`, `409`, `422`, and `503` instead of
    a single `501`. If this assertion ever fails, the census has stopped
    reading the marker and every `stub` in the file has become free.
    """
    contract = load_contract()
    key = ("/api/v1/questions", "post")
    assert promised_responses(contract)[key] == {"501"}

    contract["paths"][key[0]][key[1]][MARKER] = IMPLEMENTED
    assert promised_responses(contract)[key] == {"201", "401", "403", "409", "422", "503"}


def test_no_stub_operation_secretly_works():
    """A stub that quietly returns data would make the census lie by omission."""
    client = demo_client()
    store = demo_corpus()
    assert store.questions, "the demo corpus must hold data, or a 501 proves nothing"
    for path, method in sorted(STUB_REQUESTS):
        response = send(client, path, method)
        assert response.status_code == 501, f"{method.upper()} {path} answered {response.status_code}"
