"""The read surface, served from a real Content store built by Ingest.

`test_service.py` proves the tracer bullet behaves against the in-memory fake.
This module is the other half: every read the contract publishes, answered from
a store that Ingest built out of Markdown, so a field the corpus stopped
producing fails here rather than in a client.

Two corpora appear below, and the difference matters:

- the **fixture corpus** (`tests/contentdb_fixtures.py`) is small and fixed, so
  a test can say "this filter matches exactly one Question" and still be true
  next week;
- the **committed corpus** is the real one, and the tests that use it assert
  against a filesystem scan rather than a number typed into the test. A hard
  number would be wrong the day somebody writes a Question, and would be
  "fixed" by editing the expectation, which proves nothing.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from support import (
    ROOT,
    UNKNOWN_QUESTION,
)

PROBLEM_MEDIA_TYPE = "application/problem+json"

#: A Question the fixture corpus always holds; see `tests/contentdb_fixtures.py`.
FIXTURE_QUESTION = "/api/v1/questions/kubernetes/admission-policy"
FIXTURE_LAB = "/api/v1/labs/kubernetes/admission-lab"


def problem(response) -> dict:
    """Assert a response is an RFC 9457 problem document and return its body."""
    assert response.headers["content-type"].startswith(PROBLEM_MEDIA_TYPE), (
        f"{response.request.method} {response.request.url} answered "
        f"{response.headers.get('content-type')!r}"
    )
    body = response.json()
    for member in ("type", "title", "status", "detail", "instance"):
        assert member in body, f"problem document is missing {member!r}: {body}"
    assert body["status"] == response.status_code
    return body


def scan_front_matter(directory: Path) -> list[dict[str, str]]:
    """Read `theme` and `difficulty` straight out of the Markdown front matter.

    Deliberately not `contentdb.frontmatter`: an assertion about the corpus that
    used the same reader as the code under test would agree with a bug.
    """
    scanned = []
    for path in sorted(directory.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        front_matter = text.split("---", 2)[1]
        fields = dict(
            re.findall(r"^(theme|difficulty|type):\s*(\S+)\s*$", front_matter, flags=re.MULTILINE)
        )
        fields["id"] = f"{path.parent.name}/{path.stem}"
        scanned.append(fields)
    return scanned


# ----------------------------------------------------- one Question by id


def test_a_question_is_served_with_every_field_the_contract_requires(fixture_client):
    response = fixture_client.get(FIXTURE_QUESTION)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == "kubernetes/admission-policy"
    assert set(body) == {
        "id", "theme", "slug", "title", "difficulty", "type", "tags", "sources",
        "prompt", "answer_guide", "body_markdown", "source_path", "content_hash",
        "updated_at",
    }
    assert body["source_path"] == "questions/kubernetes/admission-policy.md"
    assert body["answer_guide"], "the answer guide is what makes a Question useful"


def test_the_etag_is_the_questions_content_hash(fixture_client):
    response = fixture_client.get(FIXTURE_QUESTION)
    assert response.headers["ETag"] == f'"{response.json()["content_hash"]}"'


def test_an_unknown_question_is_a_404_problem_document_naming_the_id(client):
    response = client.get(UNKNOWN_QUESTION)
    assert response.status_code == 404
    body = problem(response)
    assert "kubernetes/nothing-here" in body["detail"]
    assert body["instance"] == UNKNOWN_QUESTION


def test_an_unknown_theme_is_a_404_too(fixture_client):
    assert fixture_client.get("/api/v1/questions/atlantis/anything").status_code == 404


# --------------------------------------------- the Question to Lab link


def test_a_question_reports_the_labs_that_prepare_a_learner_for_it(fixture_client):
    """The link is served, not implied: `question_ref` points both ways.

    A Question's fields are pinned by the epic and none of them is a list of
    Labs, so the reverse direction is published as an RFC 8288 `Link` header
    naming the collection query and every Lab that answers it today.
    """
    response = fixture_client.get(FIXTURE_QUESTION)
    links = response.headers["Link"]
    assert "/api/v1/labs?question_ref=kubernetes%2Fadmission-policy" in links
    assert "</api/v1/labs/kubernetes/admission-lab>" in links, links


def test_a_question_with_no_labs_still_advertises_the_query(fixture_client):
    response = fixture_client.get("/api/v1/questions/kubernetes/pod-scheduling")
    assert response.status_code == 200
    assert "question_ref=kubernetes%2Fpod-scheduling" in response.headers["Link"]
    assert "/api/v1/labs/kubernetes/pod-scheduling>" not in response.headers["Link"]


# ------------------------------------------------------------- conditional


def test_a_matching_if_none_match_is_a_304_with_no_body(fixture_client):
    first = fixture_client.get(FIXTURE_QUESTION)
    second = fixture_client.get(FIXTURE_QUESTION, headers={"If-None-Match": first.headers["ETag"]})
    assert second.status_code == 304
    assert second.content == b"", "a 304 must not carry the body it just saved sending"
    assert second.headers["ETag"] == first.headers["ETag"]


@pytest.mark.parametrize("header", ['"sha256:something-else"', "", '"a", "b"'])
def test_a_stale_if_none_match_is_a_full_200(fixture_client, header):
    response = fixture_client.get(FIXTURE_QUESTION, headers={"If-None-Match": header})
    assert response.status_code == 200
    assert response.json()["id"] == "kubernetes/admission-policy"


def test_a_weak_or_wildcard_validator_still_matches(fixture_client):
    """RFC 9110: `*` matches anything that exists, and `W/` is the same tag."""
    etag = fixture_client.get(FIXTURE_QUESTION).headers["ETag"]
    assert fixture_client.get(FIXTURE_QUESTION, headers={"If-None-Match": "*"}).status_code == 304
    weak = fixture_client.get(FIXTURE_QUESTION, headers={"If-None-Match": f"W/{etag}"})
    assert weak.status_code == 304
    listed = fixture_client.get(
        FIXTURE_QUESTION, headers={"If-None-Match": f'"other", {etag}'}
    )
    assert listed.status_code == 304


def test_if_none_match_on_something_that_does_not_exist_is_still_a_404(fixture_client):
    """A validator cannot conjure a representation the corpus does not hold."""
    response = fixture_client.get(
        "/api/v1/questions/kubernetes/nothing-here", headers={"If-None-Match": "*"}
    )
    assert response.status_code == 404


# ------------------------------------------------------ the real corpus


def test_the_committed_corpus_answers_the_filter_the_epic_names(corpus_client):
    """The acceptance criterion, asserted against the corpus rather than a number.

    A hard-coded count would be wrong the next time somebody writes a Question,
    and correcting it would prove nothing; scanning the front matter keeps the
    expectation tied to what is actually committed.
    """
    scanned = [
        entry
        for entry in scan_front_matter(ROOT / "questions" / "kubernetes")
        if entry.get("difficulty") == "senior"
    ]
    assert scanned, "the corpus is expected to hold senior Kubernetes Questions"

    body = corpus_client.get(
        "/api/v1/questions?theme=kubernetes&difficulty=senior&limit=200"
    ).json()
    assert body["total"] == len(scanned)
    assert {item["id"] for item in body["items"]} == {entry["id"] for entry in scanned}
    for item in body["items"]:
        assert item["theme"] == "kubernetes"
        assert item["difficulty"] == "senior"


def test_every_committed_question_still_satisfies_the_contract(corpus_client):
    """Schema drift in real content fails here, not in a client.

    Serving a page validates every item against the response model, so a
    Question whose front matter grew a value the contract does not describe
    turns this into a `500`.
    """
    body = corpus_client.get("/api/v1/questions?limit=200").json()
    assert body["total"] > 200, "the committed corpus is larger than one page"
    assert len(body["items"]) == 200
    for item in body["items"]:
        assert item["id"] and re.fullmatch(r"[0-9a-f]{64}", item["content_hash"]), item
