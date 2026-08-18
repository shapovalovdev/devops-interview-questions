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
    DEMO_LAB,
    DEMO_LEARNING_PATH,
    DEMO_QUESTION,
    DEMO_THEME,
    UNKNOWN_LAB,
    UNKNOWN_LEARNING_PATH,
    UNKNOWN_QUESTION,
    UNKNOWN_THEME,
    ExplodingStore,
    DEMO_REFERENCED_QUESTION,
    WRITE_REQUESTS,
    WRONG_WRITE_CREDENTIAL,
    lab_body,
    question_body,
    client_for,
    demo_client,
    demo_corpus,
    revalidate,
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
        ("/api/v1/meta", "get", "200"): lambda: client.get("/api/v1/meta").status_code,
        ("/api/v1/questions", "get", "200"): lambda: client.get("/api/v1/questions").status_code,
        # The 422 is a real out-of-range limit, not a fabricated one: the census
        # is only worth running if the requests it makes are requests a client
        # could make.
        ("/api/v1/questions", "get", "422"): lambda: client.get(
            "/api/v1/questions?limit=0"
        ).status_code,
        ("/api/v1/questions", "get", "500"): lambda: failing.get("/api/v1/questions").status_code,
        ("/api/v1/questions/{theme}/{slug}", "get", "200"): lambda: client.get(
            DEMO_QUESTION
        ).status_code,
        # The `304` is produced the way a client produces one: read the item,
        # then ask again with the ETag the read handed over.
        ("/api/v1/questions/{theme}/{slug}", "get", "304"): lambda: revalidate(
            client, DEMO_QUESTION
        ).status_code,
        ("/api/v1/questions/{theme}/{slug}", "get", "404"): lambda: client.get(
            UNKNOWN_QUESTION
        ).status_code,
        ("/api/v1/questions/{theme}/{slug}", "get", "500"): lambda: failing.get(
            DEMO_QUESTION
        ).status_code,
        ("/api/v1/labs", "get", "200"): lambda: client.get("/api/v1/labs").status_code,
        ("/api/v1/labs", "get", "422"): lambda: client.get("/api/v1/labs?limit=0").status_code,
        ("/api/v1/labs", "get", "500"): lambda: failing.get("/api/v1/labs").status_code,
        ("/api/v1/labs/{theme}/{slug}", "get", "200"): lambda: client.get(DEMO_LAB).status_code,
        ("/api/v1/labs/{theme}/{slug}", "get", "304"): lambda: revalidate(
            client, DEMO_LAB
        ).status_code,
        ("/api/v1/labs/{theme}/{slug}", "get", "404"): lambda: client.get(UNKNOWN_LAB).status_code,
        ("/api/v1/labs/{theme}/{slug}", "get", "500"): lambda: failing.get(DEMO_LAB).status_code,
        ("/api/v1/themes", "get", "200"): lambda: client.get("/api/v1/themes").status_code,
        ("/api/v1/themes", "get", "500"): lambda: failing.get("/api/v1/themes").status_code,
        ("/api/v1/themes/{name}", "get", "200"): lambda: client.get(DEMO_THEME).status_code,
        ("/api/v1/themes/{name}", "get", "304"): lambda: revalidate(client, DEMO_THEME).status_code,
        ("/api/v1/themes/{name}", "get", "404"): lambda: client.get(UNKNOWN_THEME).status_code,
        ("/api/v1/themes/{name}", "get", "500"): lambda: failing.get(DEMO_THEME).status_code,
        ("/api/v1/tags", "get", "200"): lambda: client.get("/api/v1/tags").status_code,
        ("/api/v1/tags", "get", "500"): lambda: failing.get("/api/v1/tags").status_code,
        ("/api/v1/learning-paths", "get", "200"): lambda: client.get(
            "/api/v1/learning-paths"
        ).status_code,
        ("/api/v1/learning-paths", "get", "500"): lambda: failing.get(
            "/api/v1/learning-paths"
        ).status_code,
        ("/api/v1/learning-paths/{slug}", "get", "200"): lambda: client.get(
            DEMO_LEARNING_PATH
        ).status_code,
        ("/api/v1/learning-paths/{slug}", "get", "304"): lambda: revalidate(
            client, DEMO_LEARNING_PATH
        ).status_code,
        ("/api/v1/learning-paths/{slug}", "get", "404"): lambda: client.get(
            UNKNOWN_LEARNING_PATH
        ).status_code,
        ("/api/v1/learning-paths/{slug}", "get", "500"): lambda: failing.get(
            DEMO_LEARNING_PATH
        ).status_code,
        ("/api/v1/search", "get", "200"): lambda: client.get(
            "/api/v1/search?q=admission"
        ).status_code,
        # `q` is required and has a minimum length, so an empty one is the
        # smallest request a client could actually send and get a 422 for.
        ("/api/v1/search", "get", "422"): lambda: client.get("/api/v1/search?q=").status_code,
        ("/api/v1/search", "get", "500"): lambda: failing.get(
            "/api/v1/search?q=admission"
        ).status_code,
    }


def write_producers() -> dict[tuple[str, str, str], Callable[[], int]]:
    """One request per documented response of every write operation.

    Each producer builds its own client, because a write mutates the store and a
    census that shared one would depend on the order its entries happened to run
    in. The requests are the ones a client would really make: a refusal is
    produced by withholding the credential or the validator, never by reaching
    past the service.
    """
    producers: dict[tuple[str, str, str], Callable[[], int]] = {}

    def add(path: str, method: str, status: str, **kwargs: Any) -> None:
        producers[(path, method, status)] = lambda: send(
            demo_client(kwargs.pop("credential_for_client", ...))
            if "credential_for_client" in kwargs
            else demo_client(),
            path,
            method,
            **kwargs,
        ).status_code

    for path, method in WRITE_REQUESTS:
        # The refusals every write shares.
        producers[(path, method, "401")] = (
            lambda p=path, m=method: send(demo_client(), p, m, credential=None).status_code
        )
        producers[(path, method, "403")] = (
            lambda p=path, m=method: send(
                demo_client(), p, m, credential=WRONG_WRITE_CREDENTIAL
            ).status_code
        )
        producers[(path, method, "503")] = (
            lambda p=path, m=method: send(demo_client(credential=None), p, m).status_code
        )

        success = "201" if method == "post" else ("204" if method == "delete" else "200")
        producers[(path, method, success)] = (
            lambda p=path, m=method: send(demo_client(), p, m).status_code
        )

        if method in ("put", "patch", "delete"):
            producers[(path, method, "428")] = (
                lambda p=path, m=method: send(demo_client(), p, m, if_match="").status_code
            )
            producers[(path, method, "412")] = (
                lambda p=path, m=method: send(demo_client(), p, m, if_match='"stale"').status_code
            )
            absent = (
                "/api/v1/labs/kubernetes/nothing-here"
                if "labs" in path
                else "/api/v1/questions/kubernetes/nothing-here"
            )
            producers[(path, method, "404")] = (
                lambda p=path, m=method, u=absent: send(
                    demo_client(), p, m, url=u, if_match='"anything"'
                ).status_code
            )

    # A create whose id already exists.
    for path in ("/api/v1/questions", "/api/v1/labs"):
        def duplicate(p=path):
            client = demo_client()
            send(client, p, "post")
            return send(client, p, "post").status_code

        producers[(path, "post", "409")] = duplicate

    # A body the corpus rules reject.
    producers[("/api/v1/questions", "post", "422")] = lambda: send(
        demo_client(), "/api/v1/questions", "post", json=question_body(theme="not-a-theme")
    ).status_code
    producers[("/api/v1/labs", "post", "422")] = lambda: send(
        demo_client(), "/api/v1/labs", "post", json=lab_body(question_ref="kubernetes/nothing-here")
    ).status_code
    for path in ("/api/v1/questions/{theme}/{slug}", "/api/v1/labs/{theme}/{slug}"):
        for method in ("put", "patch"):
            body = (
                {"difficulty": "wizard"}
                if method == "patch"
                else (lab_body if "labs" in path else question_body)(theme="not-a-theme")
            )
            producers[(path, method, "422")] = (
                lambda p=path, m=method, b=body: send(demo_client(), p, m, json=b).status_code
            )

    # Deleting a Question a Lab still points at cannot be exported, so it is refused.
    producers[("/api/v1/questions/{theme}/{slug}", "delete", "409")] = lambda: send(
        demo_client(),
        "/api/v1/questions/{theme}/{slug}",
        "delete",
        url=f"/api/v1/questions/{DEMO_REFERENCED_QUESTION}",
    ).status_code
    return producers


def test_the_census_covers_every_response_the_contract_promises():
    contract = load_contract()
    owed = promised_responses(contract)
    required = {(path, method, status) for (path, method), codes in owed.items() for status in codes}

    assert len(owed) == 20, (
        "the census expects the 20 v1 operations — the epic's original 19 plus "
        "GET /api/v1/meta from the snapshot-service epic; api/openapi.yaml describes "
        f"{len(owed)}. If an operation was added or removed, say so on the epic first."
    )
    assert required, "the census found nothing to check, which means it is not checking"

    producers = {**implemented_producers(), **write_producers()}

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

    # Every operation is implemented now, so the stub side of the rule is proved
    # against a copy: marking a live operation `stub` must collapse everything
    # it owes down to a single `501`, and restoring the marker must bring the
    # whole set back. Reading it off a real stub stopped being possible when
    # slice 0004 removed the last one.
    documented = {"201", "401", "403", "409", "422", "503"}
    assert promised_responses(contract)[key] == documented

    contract["paths"][key[0]][key[1]][MARKER] = STUB
    assert promised_responses(contract)[key] == {"501"}

    contract["paths"][key[0]][key[1]][MARKER] = IMPLEMENTED
    assert promised_responses(contract)[key] == documented


def test_no_operation_is_still_a_stub():
    """The release gate: slice 0004 was the last one allowed to leave a stub."""
    contract = load_contract()
    stubs = sorted(
        f"{method.upper()} {path}"
        for path, item in contract["paths"].items()
        for method, operation in item.items()
        if method in METHODS and operation.get(MARKER) == STUB
    )
    assert stubs == [], f"the contract still marks these as stubs: {stubs}"
    assert demo_corpus().questions, "the demo corpus must hold data, or none of this proves anything"
