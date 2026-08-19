"""Question and Lab must answer a bad write identically.

`api/app.py` states the order a write is checked in and calls it part of the
contract:

    Can this service write at all (503), did the client authenticate (401), is
    the credential right (403), does the record exist (404), did the client say
    which version it is replacing (428), is that still the current version
    (412), and only then: is the content legal (422).

That order was implemented twice -- once across the Question routes, once across
the Lab routes -- in two blocks of about 200 lines each that differ only in the
kind label, the store method, the record builder, and the response model.  A
correction applied to one could land nowhere near the other, and nothing would
notice: `test_writes.py` and `test_write_corpus.py` each assert a kind against
its own expectations, never against the other kind.

This module compares them.  Every case sends the *same* class of malformed
request at both surfaces and asserts they answer the same status, so the two
implementations cannot drift apart silently.

It is the deliverable of #182, not a side effect of it: it is written to pass
against the two hand-written blocks that exist today, and to keep passing when
they are replaced by one `resource_routes()` generated from a `ResourceSpec`.
If it only passed after the refactor it would be proving the refactor, not the
contract.

**Result on the day it was written: the two kinds agree on every case.**  The
duplication had not yet caused a divergence.  That is worth stating plainly
rather than implying this module rescued the service from one; what it does is
make the next divergence impossible to land quietly.

Writing it did surface something the contract's own wording hides.  There are
**two** different 422s, at opposite ends of the order:

* **Schema 422** -- FastAPI rejects the body against the write model before the
  route function runs at all, so it precedes even the 404.  A `PATCH` carrying a
  full write body, or a `difficulty` outside the enum, lands here.
* **Corpus-rule 422** -- `writes.WriteRejected`, raised inside the body after
  the precondition has been checked.  An undeclared Theme lands here.

So a `PUT` with no `If-Match` answers 422 when the body breaks the schema and
428 when it breaks a corpus rule, though both read as "invalid content" to a
client.  The order in `api/app.py`'s docstring describes only the second kind.
The cases below pin both, because that distinction is exactly what a
`ResourceSpec` could quietly change.
"""

from __future__ import annotations

import pytest

from support import (
    DEMO_SPARE_QUESTION,
    DEMO_WRITABLE_LAB,
    TEST_WRITE_CREDENTIAL,
    WRONG_WRITE_CREDENTIAL,
    demo_client,
    lab_body,
    question_body,
)

#: The two resource kinds, paired so every case runs against both.
#:
#: `collection` is the create surface; `item` is an existing record that may be
#: replaced, patched, or deleted; `body` builds a valid write for that item, so
#: a case that wants an *invalid* one starts from something that would have
#: worked and breaks exactly one thing.
#: A patch-shaped body per kind. PATCH publishes a different model from PUT, so
#: reusing the write body would test the schema rather than the check order.
PATCHES = {"question": {"difficulty": "senior"}, "lab": {"title": "A new title"}}

KINDS = {
    "question": {
        "name": "question",
        "collection": "/api/v1/questions",
        "item": f"/api/v1/questions/{DEMO_SPARE_QUESTION}",
        "body": lambda **kw: question_body(**{"slug": "demo-pod-disruption", **kw}),
    },
    "lab": {
        "name": "lab",
        "collection": "/api/v1/labs",
        "item": f"/api/v1/labs/{DEMO_WRITABLE_LAB}",
        "body": lambda **kw: lab_body(**{"slug": "demo-admission-guardrails", **kw}),
    },
}

NAMES = sorted(KINDS)


@pytest.fixture
def client():
    return demo_client()


@pytest.fixture
def read_only():
    """A service with no Write credential configured: every write is a 503."""
    return demo_client(credential=None)


def write(client, url, method, body=None, credential=TEST_WRITE_CREDENTIAL, if_match=None):
    """Send one write exactly as described, adding nothing.

    `support.send` is deliberately not used here: it looks a request up by
    contract path template and supplies the current `If-Match` for you, which is
    the right default for testing one kind and the wrong one for testing the
    check *order*. Several cases below need a request with no `If-Match` at all,
    which is what produces the 428 that must precede the 422.
    """
    headers = {}
    if credential is not None:
        headers["X-API-Key"] = credential
    if if_match is not None:
        headers["If-Match"] = if_match
    payload = {} if body is None else {"json": body}
    return client.request(method.upper(), url, headers=headers, **payload)


def statuses(client, case, credential=TEST_WRITE_CREDENTIAL):
    """Run one case against both kinds and return {kind: status}."""
    answers = {}
    for name in NAMES:
        url, method, body = case(KINDS[name])
        answers[name] = write(client, url, method, body, credential).status_code
    return answers


def assert_agree(answers, expected=None):
    question, lab = answers["question"], answers["lab"]
    assert question == lab, (
        f"Question answered {question} and Lab answered {lab} to the same class of request. "
        "The write-check order is part of the contract and must be one implementation."
    )
    if expected is not None:
        assert question == expected, f"both kinds answered {question}, expected {expected}"


# --------------------------------------------------------- the credential gate


def test_a_service_that_cannot_write_refuses_both_kinds_alike(read_only):
    answers = statuses(
        read_only,
        lambda kind: (kind["item"], "put", kind["body"]()),
        credential=None,
    )
    assert_agree(answers, 503)


def test_a_missing_credential_is_401_for_both_kinds(client):
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "put", kind["body"]()), credential=None),
        401,
    )


def test_a_wrong_credential_is_403_for_both_kinds(client):
    assert_agree(
        statuses(
            client,
            lambda kind: (kind["item"], "put", kind["body"]()),
            credential=WRONG_WRITE_CREDENTIAL,
        ),
        403,
    )


# ------------------------------------------------------------------- identity


@pytest.mark.parametrize("method", ["put", "delete"])
def test_a_record_that_does_not_exist_is_404_for_both_kinds(client, method):
    def case(kind):
        body = None if method == "delete" else kind["body"](slug="no-such-record")
        return f"{kind['collection']}/kubernetes/no-such-record", method, body

    assert_agree(statuses(client, case), 404)


def test_a_patch_at_a_missing_record_is_404_for_both_kinds(client):
    """PATCH takes a patch body, so the schema passes and identity is reached."""
    assert_agree(
        statuses(
            client,
            lambda kind: (
                f"{kind['collection']}/kubernetes/no-such-record", "patch", PATCHES[kind["name"]],
            ),
        ),
        404,
    )


def test_a_body_that_renames_its_record_waits_behind_the_precondition(client):
    """The rename is a corpus-rule refusal, so 428 comes first for both kinds."""
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "put", kind["body"](slug="a-different-slug"))),
        428,
    )


def test_a_body_naming_another_theme_waits_behind_the_precondition(client):
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "put", kind["body"](theme="linux"))),
        428,
    )


# --------------------------------------------------------- optimistic locking


@pytest.mark.parametrize("method", ["put", "delete"])
def test_a_missing_precondition_is_428_for_both_kinds(client, method):
    """404 is checked before 428: these records exist, so the answer is 428."""

    def case(kind):
        body = None if method == "delete" else kind["body"]()
        return kind["item"], method, body

    assert_agree(statuses(client, case), 428)


def test_a_patch_without_a_precondition_is_428_for_both_kinds(client):
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "patch", PATCHES[kind["name"]])), 428
    )


def test_a_full_body_sent_to_patch_is_a_schema_422_for_both_kinds(client):
    """The schema 422 precedes everything, including the precondition.

    PATCH publishes a patch model, not the write model, so a full write body is
    rejected before the route function runs -- which is why this answers 422
    where the same request shape at PUT answers 428.
    """
    assert_agree(statuses(client, lambda kind: (kind["item"], "patch", kind["body"]())), 422)


# ------------------------------------------------------------------- content


def test_an_undeclared_theme_is_refused_for_both_kinds(client):
    assert_agree(
        statuses(client, lambda kind: (kind["collection"], "post", kind["body"](theme="not-a-theme"))),
        422,
    )


def test_an_invalid_difficulty_is_refused_for_both_kinds(client):
    assert_agree(
        statuses(
            client,
            lambda kind: (kind["collection"], "post", kind["body"](difficulty="intermediate")),
        ),
        422,
    )


def test_a_body_missing_a_required_field_is_refused_for_both_kinds(client):
    def case(kind):
        body = kind["body"]()
        body.pop("title", None)
        return kind["collection"], "post", body

    assert_agree(statuses(client, case), 422)


# ------------------------------------------------------------------ the order


def test_authentication_is_checked_before_the_record_exists(client):
    """A missing credential on a missing record is 401, not 404 -- for both kinds."""
    assert_agree(
        statuses(
            client,
            lambda kind: (f"{kind['collection']}/kubernetes/no-such-record", "put", kind["body"]()),
            credential=None,
        ),
        401,
    )


def test_the_record_is_checked_before_the_precondition(client):
    """No If-Match on a record that does not exist is 404, not 428 -- for both kinds."""
    assert_agree(
        statuses(
            client,
            lambda kind: (
                f"{kind['collection']}/kubernetes/no-such-record",
                "put",
                kind["body"](slug="no-such-record"),
            ),
        ),
        404,
    )


def test_the_precondition_is_checked_before_a_corpus_rule(client):
    """An undeclared Theme with no If-Match is 428, not 422 -- for both kinds.

    This is the case most likely to diverge between two hand-written blocks,
    because it is the one where the "obvious" order (validate the body first)
    is the wrong one.
    """
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "put", kind["body"](theme="not-a-theme"))),
        428,
    )


def test_a_schema_violation_outranks_the_precondition_for_both_kinds(client):
    """...but a value outside the enum is rejected before the body runs.

    Same request shape as the case above, same missing `If-Match`, different
    answer -- because `difficulty` is constrained by the write model while
    `theme` is constrained by the corpus. A client cannot predict which it gets
    from the order in `api/app.py`'s docstring, which describes only the
    corpus-rule 422. Pinned here so a ResourceSpec cannot change it unnoticed.
    """
    assert_agree(
        statuses(client, lambda kind: (kind["item"], "put", kind["body"](difficulty="intermediate"))),
        422,
    )
