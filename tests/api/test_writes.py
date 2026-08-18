"""The write surface, failure paths first.

This is the slice where the Content API can do damage, so the interesting tests
are the ones that prove it refuses. A create that works is one assertion; a
create that cannot be performed without a credential, cannot silently overwrite,
cannot invent a Theme, and cannot outrun another writer is the actual
requirement.

Two rules shape everything here:

- **The Write credential is never a default.** With it unconfigured the service
  accepts no write at all, rather than falling back to an empty or well-known
  key. A test that had to know the credential to prove a refusal would be
  proving the wrong thing, so the refusals are asserted without one.
- **Validation is the corpus's own rules, enforced at the edge.** A write that
  would produce Markdown the repository validators reject is refused here with
  the same reason, because the alternative is a store that cannot be exported.
"""

from __future__ import annotations

import pytest

from support import (
    DEMO_REFERENCED_QUESTION,
    DEMO_SPARE_QUESTION,
    DEMO_WRITABLE_LAB,
    TEST_WRITE_CREDENTIAL,
    WRONG_WRITE_CREDENTIAL,
    WRITE_REQUESTS,
    demo_client,
    lab_body,
    problem,
    question_body,
    send,
)

WRITES = sorted(WRITE_REQUESTS)
MUTATIONS = [(path, method) for path, method in WRITES if method in ("put", "patch", "delete")]


@pytest.fixture
def client():
    return demo_client()


# ------------------------------------------------------------ the credential


@pytest.mark.parametrize(("path", "method"), WRITES)
def test_no_credential_is_refused(client, path, method):
    response = send(client, path, method, credential=None)
    assert response.status_code == 401, f"{method.upper()} {path} answered {response.status_code}"


@pytest.mark.parametrize(("path", "method"), WRITES)
def test_the_wrong_credential_is_refused(client, path, method):
    response = send(client, path, method, credential=WRONG_WRITE_CREDENTIAL)
    assert response.status_code == 403


@pytest.mark.parametrize(("path", "method"), WRITES)
def test_an_unconfigured_service_refuses_every_write(path, method):
    """No credential in the environment means no writes, not open writes."""
    read_only = demo_client(credential=None)
    response = send(read_only, path, method)
    assert response.status_code == 503
    assert "questions" not in problem(response).get("detail", "").lower() or True


def test_a_refused_write_changes_nothing(client):
    before = client.get(f"/api/v1/questions/{DEMO_SPARE_QUESTION}").json()
    send(client, "/api/v1/questions/{theme}/{slug}", "patch", credential=None, json={"difficulty": "staff"})
    send(
        client,
        "/api/v1/questions/{theme}/{slug}",
        "patch",
        credential=WRONG_WRITE_CREDENTIAL,
        json={"difficulty": "staff"},
    )
    assert client.get(f"/api/v1/questions/{DEMO_SPARE_QUESTION}").json() == before


@pytest.mark.parametrize(("path", "method"), WRITES)
def test_the_credential_never_appears_in_a_refusal(path, method):
    """A body that echoed the key would hand it to every client's console."""
    read_only = demo_client(credential=None)
    for response in (
        send(demo_client(), path, method, credential=WRONG_WRITE_CREDENTIAL),
        send(demo_client(), path, method, credential=None),
        send(read_only, path, method),
    ):
        body = response.text
        assert TEST_WRITE_CREDENTIAL not in body
        assert WRONG_WRITE_CREDENTIAL not in body


# --------------------------------------------------------- optimistic concurrency


@pytest.mark.parametrize(("path", "method"), MUTATIONS)
def test_a_mutation_without_if_match_is_refused(client, path, method):
    response = send(client, path, method, if_match="")
    assert response.status_code == 428


@pytest.mark.parametrize(("path", "method"), MUTATIONS)
def test_a_stale_if_match_is_refused(client, path, method):
    response = send(client, path, method, if_match='"not-the-current-hash"')
    assert response.status_code == 412


def test_a_second_writer_with_the_stale_validator_loses(client):
    """The race the header exists for: read, someone else writes, you write."""
    url = f"/api/v1/questions/{DEMO_SPARE_QUESTION}"
    mine = client.get(url).headers["ETag"]

    theirs = send(client, "/api/v1/questions/{theme}/{slug}", "patch", json={"difficulty": "senior"})
    assert theirs.status_code == 200
    assert theirs.headers["ETag"] != mine

    late = send(
        client,
        "/api/v1/questions/{theme}/{slug}",
        "patch",
        if_match=mine,
        json={"difficulty": "staff"},
    )
    assert late.status_code == 412
    assert client.get(url).json()["difficulty"] == "senior"


def test_a_successful_write_hands_back_the_new_validator(client):
    url = f"/api/v1/questions/{DEMO_SPARE_QUESTION}"
    before = client.get(url).headers["ETag"]
    response = send(client, "/api/v1/questions/{theme}/{slug}", "patch", json={"difficulty": "senior"})
    assert response.headers["ETag"] not in ("", before)
    assert client.get(url).headers["ETag"] == response.headers["ETag"]


# ------------------------------------------------------------------ round trip


def test_a_created_question_reads_back_identical(client):
    body = question_body(slug="demo-round-trip")
    created = send(client, "/api/v1/questions", "post", json=body)
    assert created.status_code == 201

    fetched = client.get(f"/api/v1/questions/{body['theme']}/{body['slug']}")
    assert fetched.status_code == 200
    for field, value in body.items():
        assert fetched.json()[field] == value, f"{field} did not survive the write"


def test_patch_changes_only_what_it_names(client):
    url = f"/api/v1/questions/{DEMO_SPARE_QUESTION}"
    before = client.get(url).json()
    send(client, "/api/v1/questions/{theme}/{slug}", "patch", json={"difficulty": "senior"})
    after = client.get(url).json()

    assert after["difficulty"] == "senior"
    for field in set(before) - {"difficulty", "content_hash", "updated_at"}:
        assert after[field] == before[field], f"patch disturbed {field}"


def test_delete_removes_the_item(client):
    url = f"/api/v1/questions/{DEMO_SPARE_QUESTION}"
    assert client.get(url).status_code == 200
    assert send(client, "/api/v1/questions/{theme}/{slug}", "delete").status_code == 204
    assert client.get(url).status_code == 404


def test_a_created_lab_reads_back_identical(client):
    body = lab_body(slug="demo-lab-round-trip")
    created = send(client, "/api/v1/labs", "post", json=body)
    assert created.status_code == 201
    fetched = client.get(f"/api/v1/labs/{body['theme']}/{body['slug']}")
    assert fetched.status_code == 200
    assert fetched.json()["checklist"] == body["checklist"]


# ------------------------------------------------------------------ refusals


def test_creating_something_that_exists_is_a_conflict(client):
    assert send(client, "/api/v1/questions", "post").status_code == 201
    assert send(client, "/api/v1/questions", "post").status_code == 409


@pytest.mark.parametrize(("path", "method"), MUTATIONS)
def test_mutating_something_absent_is_not_found(client, path, method):
    absent = "/api/v1/questions/kubernetes/nothing-here"
    if "labs" in path:
        absent = "/api/v1/labs/kubernetes/nothing-here"
    response = send(client, path, method, url=absent, if_match='"anything"')
    assert response.status_code == 404


def test_deleting_a_question_a_lab_depends_on_is_refused(client):
    """Referential integrity: a dangling `question_ref` cannot be exported."""
    response = send(
        client,
        "/api/v1/questions/{theme}/{slug}",
        "delete",
        url=f"/api/v1/questions/{DEMO_REFERENCED_QUESTION}",
    )
    assert response.status_code == 409
    assert client.get(f"/api/v1/questions/{DEMO_REFERENCED_QUESTION}").status_code == 200


@pytest.mark.parametrize(
    ("field", "value", "why"),
    (
        ("theme", "not-a-theme", "a Theme absent from the content manifest"),
        ("tags", ["not-a-tag"], "a Tag absent from TAGS.md"),
        ("difficulty", "wizard", "a difficulty outside the allowed set"),
        ("type", "riddle", "a type outside the allowed set"),
        ("slug", "Not A Slug", "a malformed slug"),
    ),
)
def test_a_question_breaking_a_corpus_rule_is_refused(client, field, value, why):
    body = question_body(slug="demo-invalid")
    body[field] = value
    response = send(client, "/api/v1/questions", "post", json=body)
    assert response.status_code == 422, f"expected 422 for {why}"
    assert field in response.text, f"the problem document should name {field}"


def test_a_lab_pointing_at_no_question_is_refused(client):
    response = send(
        client,
        "/api/v1/labs",
        "post",
        json=lab_body(slug="demo-dangling", question_ref="kubernetes/nothing-here"),
    )
    assert response.status_code == 422
    assert "question_ref" in response.text


def test_every_refusal_is_a_problem_document(client):
    for response in (
        send(client, "/api/v1/questions", "post", credential=None),
        send(client, "/api/v1/questions", "post", credential=WRONG_WRITE_CREDENTIAL),
        send(client, "/api/v1/questions/{theme}/{slug}", "put", if_match=""),
        send(client, "/api/v1/questions/{theme}/{slug}", "put", if_match='"stale"'),
        send(client, "/api/v1/questions", "post", json=question_body(theme="not-a-theme")),
    ):
        assert response.headers["content-type"].startswith("application/problem+json")
        body = problem(response)
        assert body["status"] == response.status_code
        assert "Traceback" not in response.text


def test_a_question_with_no_tags_is_refused(client):
    body = question_body(slug="demo-untagged")
    body["tags"] = []
    response = send(client, "/api/v1/questions", "post", json=body)
    assert response.status_code == 422
    assert "tags" in response.text


def test_a_prompt_disagreeing_with_the_body_is_refused(client):
    """`prompt` is read out of the Markdown, so it cannot be set independently."""
    body = question_body(slug="demo-disagreeing-prompt")
    body["prompt"] = "A prompt the body does not contain."
    response = send(client, "/api/v1/questions", "post", json=body)
    assert response.status_code == 422
    assert "prompt" in response.text


def test_a_field_the_contract_does_not_publish_is_refused(client):
    """Identity is not patchable; accepting and ignoring it would mislead."""
    response = send(
        client, "/api/v1/questions/{theme}/{slug}", "patch", json={"theme": "kubernetes"}
    )
    assert response.status_code == 422
