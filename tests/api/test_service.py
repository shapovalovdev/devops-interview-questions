"""What the tracer bullet actually does when a client calls it.

`test_contract.py` proves the service is shaped like the contract. This module
proves it behaves: the envelope, every documented filter, deterministic paging,
RFC 9457 problem documents for every failure, and a `501` from each operation
the contract marks `x-implementation: stub`.
"""

from __future__ import annotations

import json

import pytest

from support import (
    TEST_WRITE_CREDENTIAL,
    ExplodingStore,
    InMemoryStore,
    MalformedStore,
    QUESTION_WRITE,
    demo_corpus,
    send,
)

PROBLEM_MEDIA_TYPE = "application/problem+json"

#: The demo corpus in `id` order, which is the contract's default sort.
IDS_BY_ID = [
    "kubernetes/demo-admission-guardrails",
    "kubernetes/demo-pod-disruption",
    "linux/demo-exit-codes",
    "observability/demo-cardinality",
]

QUESTION_FIELDS = {
    "id", "theme", "slug", "title", "difficulty", "type", "tags", "sources",
    "prompt", "answer_guide", "body_markdown", "source_path", "content_hash",
    "updated_at",
}


def problem(response) -> dict:
    """Assert a response is an RFC 9457 problem document and return its body."""
    assert response.headers["content-type"].startswith(PROBLEM_MEDIA_TYPE), (
        f"{response.request.method} {response.request.url} answered "
        f"{response.headers.get('content-type')!r}, not {PROBLEM_MEDIA_TYPE}"
    )
    body = response.json()
    for member in ("type", "title", "status", "detail", "instance"):
        assert member in body, f"problem document is missing the RFC 9457 member {member!r}: {body}"
    assert body["status"] == response.status_code
    return body


# ------------------------------------------------------------------- health


def test_health_reports_the_service_and_the_contract_it_serves(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {
        "status": "ok",
        "service": "content-api",
        "contract_version": "v1",
    }


# ------------------------------------------------------- the list envelope


def test_questions_are_returned_in_the_epics_envelope(client):
    body = client.get("/api/v1/questions").json()
    assert set(body) == {"items", "total", "limit", "offset"}
    assert body["total"] == 4
    assert body["limit"] == 50
    assert body["offset"] == 0
    assert [item["id"] for item in body["items"]] == IDS_BY_ID


def test_each_question_carries_every_field_the_epic_pins(client):
    item = client.get("/api/v1/questions").json()["items"][0]
    assert set(item) == QUESTION_FIELDS
    assert item["source_path"] == "questions/kubernetes/demo-admission-guardrails.md"
    assert item["sources"][0]["source_type"] == "official-docs"


def test_total_counts_matches_before_the_page_is_cut(client):
    body = client.get("/api/v1/questions?limit=1").json()
    assert len(body["items"]) == 1
    assert body["total"] == 4, "total must count matches, not the size of the page"


# --------------------------------------------------------------------- sort


def test_the_default_sort_is_id_so_paging_is_deterministic(client):
    """Guards the defect the coordinator ruled on: the default was `-updated_at`.

    The demo corpus is built so the two orders disagree — by `-updated_at` the
    first item would be `kubernetes/demo-pod-disruption` — which is what makes
    this assertion catch a regression instead of passing by coincidence.
    """
    default = client.get("/api/v1/questions").json()["items"]
    explicit = client.get("/api/v1/questions?sort=id").json()["items"]
    newest_first = client.get("/api/v1/questions?sort=-updated_at").json()["items"]
    assert [item["id"] for item in default] == IDS_BY_ID
    assert default == explicit
    assert newest_first[0]["id"] == "kubernetes/demo-pod-disruption"
    assert default != newest_first


@pytest.mark.parametrize("key", ["id", "title", "difficulty", "updated_at"])
def test_every_sort_key_orders_both_ways(client, key):
    ascending = [i["id"] for i in client.get(f"/api/v1/questions?sort={key}").json()["items"]]
    descending = [i["id"] for i in client.get(f"/api/v1/questions?sort=-{key}").json()["items"]]
    assert len(ascending) == 4
    assert descending == list(reversed(ascending))


def test_difficulty_sorts_by_seniority(client):
    order = [i["difficulty"] for i in client.get("/api/v1/questions?sort=difficulty").json()["items"]]
    assert order == ["junior", "middle", "senior", "staff"]


# ------------------------------------------------------------------ paging


def test_limit_and_offset_walk_the_whole_corpus_without_repeating(client):
    seen: list[str] = []
    for offset in (0, 2):
        body = client.get(f"/api/v1/questions?limit=2&offset={offset}").json()
        assert body["limit"] == 2
        assert body["offset"] == offset
        assert body["total"] == 4
        seen += [item["id"] for item in body["items"]]
    assert seen == IDS_BY_ID


def test_an_offset_past_the_end_is_an_empty_page_not_an_error(client):
    body = client.get("/api/v1/questions?offset=99").json()
    assert body["items"] == []
    assert body["total"] == 4


# ----------------------------------------------------------------- filters


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("theme=kubernetes", ["kubernetes/demo-admission-guardrails", "kubernetes/demo-pod-disruption"]),
        ("difficulty=junior", ["linux/demo-exit-codes"]),
        ("difficulty=staff", ["kubernetes/demo-pod-disruption"]),
        ("type=theory", ["kubernetes/demo-pod-disruption", "linux/demo-exit-codes"]),
        ("type=troubleshooting", ["observability/demo-cardinality"]),
        ("tag=cks", ["kubernetes/demo-admission-guardrails"]),
        ("tag=linux", ["linux/demo-exit-codes"]),
        ("q=exit status", ["linux/demo-exit-codes"]),
        ("q=EXIT STATUS", ["linux/demo-exit-codes"]),
        ("theme=kubernetes&difficulty=senior", ["kubernetes/demo-admission-guardrails"]),
        ("theme=kubernetes&tag=reliability", ["kubernetes/demo-pod-disruption"]),
        ("theme=kubernetes&difficulty=junior", []),
    ],
)
def test_every_documented_filter_narrows_the_result(client, query, expected):
    body = client.get(f"/api/v1/questions?{query}").json()
    assert [item["id"] for item in body["items"]] == expected
    assert body["total"] == len(expected)


# -------------------------------------------------------- malformed input


@pytest.mark.parametrize(
    ("query", "field"),
    [
        ("limit=0", "limit"),
        ("limit=201", "limit"),
        ("limit=notanumber", "limit"),
        ("offset=-1", "offset"),
        ("sort=slug", "sort"),
        ("sort=-slug", "sort"),
        ("difficulty=expert", "difficulty"),
        ("type=quiz", "type"),
    ],
)
def test_out_of_range_and_unknown_parameters_are_422_problem_documents(client, query, field):
    response = client.get(f"/api/v1/questions?{query}")
    assert response.status_code == 422
    body = problem(response)
    assert body["instance"] == "/api/v1/questions"
    assert body["errors"], "a validation problem should name the fields that failed"
    assert any(field in error["field"] for error in body["errors"]), (
        f"no error names {field!r}: {body['errors']}"
    )


def test_the_boundary_values_of_limit_are_accepted(client):
    assert client.get("/api/v1/questions?limit=1").status_code == 200
    assert client.get("/api/v1/questions?limit=200").status_code == 200
    assert client.get("/api/v1/questions?offset=0").status_code == 200


def test_an_unknown_path_is_a_problem_document_too(client):
    response = client.get("/api/v1/questions/kubernetes")
    assert response.status_code == 404
    assert problem(response)["instance"] == "/api/v1/questions/kubernetes"


def test_a_method_the_contract_does_not_publish_is_405(client):
    response = client.post("/api/v1/health", json={})
    assert response.status_code == 405
    problem(response)


# ------------------------------------------------------------ server error


def test_a_store_failure_becomes_a_500_problem_document_without_a_trace(make_client):
    response = make_client(ExplodingStore()).get("/api/v1/questions")
    assert response.status_code == 500
    body = problem(response)
    assert body["instance"] == "/api/v1/questions"
    serialized = json.dumps(body)
    for leak in ("Traceback", "sqlite3", "RuntimeError", "api/app.py", "unreachable"):
        assert leak not in serialized, f"the problem document leaked {leak!r}: {serialized}"


def test_a_record_the_contract_cannot_describe_is_a_500_not_a_malformed_body(make_client):
    response = make_client(MalformedStore()).get("/api/v1/questions")
    assert response.status_code == 500
    assert problem(response)["status"] == 500


def test_an_empty_store_is_an_empty_page_not_a_failure(make_client):
    body = make_client(InMemoryStore()).get("/api/v1/questions").json()
    assert body == {"items": [], "total": 0, "limit": 50, "offset": 0}


# ------------------------------------------------- the headers writes depend on


def test_a_missing_credential_is_an_authorization_failure_not_a_schema_failure(client):
    """`X-API-Key` is optional in the schema so the service can answer `401`.

    Declared required, a missing credential would be a schema `422` and the
    contract's `401` could never be reached — the refusal would be about the
    shape of the request rather than about who sent it.
    """
    response = client.post("/api/v1/questions", json=QUESTION_WRITE)
    assert response.status_code == 401
    assert problem(response)["status"] == 401


def test_a_missing_if_match_is_a_precondition_failure_not_a_schema_failure(client):
    """Same reasoning for the validator: `428` is a precondition, not a shape."""
    response = client.delete(
        "/api/v1/questions/kubernetes/demo-admission-guardrails",
        headers={"X-API-Key": TEST_WRITE_CREDENTIAL},
    )
    assert response.status_code == 428
    assert problem(response)["status"] == 428


def test_a_malformed_write_body_is_still_a_422(client):
    response = client.post("/api/v1/questions", json={"theme": "kubernetes"})
    assert response.status_code == 422
    assert problem(response)["errors"]


def test_search_without_a_query_is_a_422(client):
    """The epic makes `q` required: a search with no query is meaningless."""
    response = client.get("/api/v1/search")
    assert response.status_code == 422
    assert any("q" in error["field"] for error in problem(response)["errors"])


def test_the_served_schema_is_downloadable_and_names_the_contract(client):
    schema = client.get("/openapi.json").json()
    assert schema["info"]["title"] == "Content API"
    assert schema["info"]["version"] == "1.0.0"
    assert "Problem" in schema["components"]["schemas"]


def test_the_demo_corpus_is_labelled_as_a_demo():
    """Nothing served by the fake may be mistaken for a Question from the corpus."""
    store = demo_corpus()
    for record in store.questions + store.labs:
        assert record["slug"].startswith("demo-"), record["id"]
