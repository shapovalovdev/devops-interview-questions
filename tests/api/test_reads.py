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

    linked = fixture_client.get("/api/v1/labs?question_ref=kubernetes/admission-policy").json()
    assert [lab["id"] for lab in linked["items"]] == ["kubernetes/admission-lab"]
    assert linked["total"] == 1


def test_a_lab_points_back_at_a_question_the_api_can_serve(fixture_client):
    """The other direction: `question_ref` is resolved, not left as a string."""
    lab = fixture_client.get(FIXTURE_LAB)
    assert lab.status_code == 200
    reference = lab.json()["question_ref"]
    assert reference == "kubernetes/admission-policy"
    assert f"</api/v1/questions/{reference}>" in lab.headers["Link"]
    assert fixture_client.get(f"/api/v1/questions/{reference}").status_code == 200


def test_a_lab_whose_reference_dangles_is_still_served_without_a_link(make_client):
    """A broken `question_ref` is a corpus defect, not a reason to hide the Lab."""
    from api.testing import demo_corpus, lab_record

    store = demo_corpus()
    store.labs.append(
        lab_record(
            "kubernetes", "demo-orphan", "A Lab pointing nowhere", "middle",
            ["kubernetes"], "kubernetes/nothing-here", "It references a Question that is gone.",
            "2026-08-11T09:00:00Z",
        )
    )
    response = make_client(store).get("/api/v1/labs/kubernetes/demo-orphan")
    assert response.status_code == 200
    assert response.json()["question_ref"] == "kubernetes/nothing-here"
    assert "Link" not in response.headers, "a link that 404s is worse than no link"


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


# ---------------------------------------------------------------- Labs


def test_a_lab_is_served_with_every_field_the_contract_requires(fixture_client):
    body = fixture_client.get(FIXTURE_LAB).json()
    assert set(body) == {
        "id", "theme", "slug", "title", "difficulty", "tags", "question_ref", "why",
        "checklist", "body_markdown", "source_path", "content_hash", "updated_at",
    }
    assert body["checklist"], "a Lab without a checklist is not a Lab"


def test_the_lab_etag_and_conditional_read_behave_like_the_questions(fixture_client):
    first = fixture_client.get(FIXTURE_LAB)
    assert first.headers["ETag"] == f'"{first.json()["content_hash"]}"'
    again = fixture_client.get(FIXTURE_LAB, headers={"If-None-Match": first.headers["ETag"]})
    assert again.status_code == 304
    assert again.content == b""


def test_an_unknown_lab_is_a_404_problem_document(fixture_client):
    response = fixture_client.get("/api/v1/labs/kubernetes/nothing-here")
    assert response.status_code == 404
    assert "kubernetes/nothing-here" in problem(response)["detail"]


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("", ["kubernetes/admission-lab", "linux/disk-lab", "linux/systemd-lab"]),
        ("theme=linux", ["linux/disk-lab", "linux/systemd-lab"]),
        ("difficulty=junior", ["linux/disk-lab"]),
        ("tag=security", ["kubernetes/admission-lab"]),
        ("question_ref=linux/disk-full", ["linux/disk-lab"]),
        ("q=systemd", ["linux/systemd-lab"]),
        ("theme=linux&difficulty=senior", ["linux/systemd-lab"]),
        ("theme=linux&tag=security", []),
        ("sort=-id", ["linux/systemd-lab", "linux/disk-lab", "kubernetes/admission-lab"]),
    ],
)
def test_every_documented_lab_filter_narrows_the_result(fixture_client, query, expected):
    body = fixture_client.get(f"/api/v1/labs?{query}").json()
    assert [item["id"] for item in body["items"]] == expected
    assert body["total"] == len(expected)


def test_the_lab_page_uses_the_same_envelope_and_pages_deterministically(fixture_client):
    body = fixture_client.get("/api/v1/labs?limit=2").json()
    assert set(body) == {"items", "total", "limit", "offset"}
    assert body["total"] == 3 and body["limit"] == 2 and body["offset"] == 0
    second = fixture_client.get("/api/v1/labs?limit=2&offset=2").json()
    assert [item["id"] for item in body["items"]] + [item["id"] for item in second["items"]] == [
        "kubernetes/admission-lab",
        "linux/disk-lab",
        "linux/systemd-lab",
    ]


def test_every_committed_lab_prepares_a_learner_for_a_question_that_exists(corpus_client):
    """The link is the reason Labs are in the API; a dangling one is a defect."""
    labs = corpus_client.get("/api/v1/labs?limit=200").json()
    assert labs["total"] == len(labs["items"]), "the corpus holds fewer Labs than one page"
    assert labs["items"], "the committed corpus holds Labs"
    for lab in labs["items"]:
        reference = corpus_client.get(f"/api/v1/questions/{lab['question_ref']}")
        assert reference.status_code == 200, f"{lab['id']} points at {lab['question_ref']}"


# ------------------------------------------------------------- taxonomy


def test_the_theme_catalogue_is_returned_whole_in_the_shared_envelope(fixture_client):
    body = fixture_client.get("/api/v1/themes").json()
    assert set(body) == {"items", "total", "limit", "offset"}
    assert body["total"] == len(body["items"]), "a bounded catalogue is one page"
    assert body["limit"] == len(body["items"]) and body["offset"] == 0
    assert [item["name"] for item in body["items"]] == ["kubernetes", "linux", "queue-messaging"]
    for item in body["items"]:
        assert set(item) == {"name", "state", "question_count", "lab_count", "difficulty_counts"}


def test_a_theme_reports_the_counts_the_corpus_supports(fixture_client):
    body = fixture_client.get("/api/v1/themes/kubernetes").json()
    assert body["name"] == "kubernetes"
    assert body["question_count"] == sum(body["difficulty_counts"].values())
    assert body["lab_count"] == 1


def test_a_theme_has_an_etag_even_though_no_file_backs_it(fixture_client):
    """Themes are derived, so their validator is a digest of what is served."""
    first = fixture_client.get("/api/v1/themes/kubernetes")
    other = fixture_client.get("/api/v1/themes/linux")
    assert first.headers["ETag"].startswith('"sha256:')
    assert first.headers["ETag"] != other.headers["ETag"]
    assert fixture_client.get("/api/v1/themes/kubernetes").headers["ETag"] == first.headers["ETag"]
    again = fixture_client.get(
        "/api/v1/themes/kubernetes", headers={"If-None-Match": first.headers["ETag"]}
    )
    assert again.status_code == 304 and again.content == b""


def test_an_unknown_theme_is_a_404_problem_document(fixture_client):
    response = fixture_client.get("/api/v1/themes/atlantis")
    assert response.status_code == 404
    assert "atlantis" in problem(response)["detail"]


def test_the_tag_catalogue_counts_both_kinds(fixture_client):
    body = fixture_client.get("/api/v1/tags").json()
    assert body["total"] == len(body["items"]) == body["limit"]
    names = [item["name"] for item in body["items"]]
    assert names == sorted(names), "a catalogue nobody can page must at least be ordered"
    security = next(item for item in body["items"] if item["name"] == "security")
    assert security["question_count"] >= 1 and security["lab_count"] >= 1


def test_the_theme_counts_match_a_filesystem_scan_of_the_committed_corpus(corpus_client):
    """Derived counts are only useful if they are the corpus's own counts."""
    body = corpus_client.get("/api/v1/themes").json()
    assert body["items"]
    for theme in body["items"]:
        scanned = scan_front_matter(ROOT / "questions" / theme["name"])
        assert theme["question_count"] == len(scanned), theme["name"]
        assert sum(theme["difficulty_counts"].values()) == theme["question_count"]


# -------------------------------------------------------- learning paths


def test_a_learning_path_lists_its_steps_in_order(fixture_client):
    listed = fixture_client.get("/api/v1/learning-paths").json()
    assert listed["total"] == len(listed["items"]) == listed["limit"]
    slugs = [path["slug"] for path in listed["items"]]
    assert "kubernetes-track" in slugs

    body = fixture_client.get("/api/v1/learning-paths/kubernetes-track").json()
    assert set(body) == {"slug", "title", "description", "steps"}
    assert [step["question_id"] for step in body["steps"]] == [
        "kubernetes/pod-scheduling",
        "kubernetes/admission-policy",
    ]
    assert all(step["why"] for step in body["steps"]), "a step without a why is just an ordering"


def test_a_learning_path_is_conditional_too(fixture_client):
    first = fixture_client.get("/api/v1/learning-paths/kubernetes-track")
    again = fixture_client.get(
        "/api/v1/learning-paths/kubernetes-track", headers={"If-None-Match": first.headers["ETag"]}
    )
    assert again.status_code == 304 and again.content == b""


def test_an_unknown_learning_path_slug_is_a_404(fixture_client):
    response = fixture_client.get("/api/v1/learning-paths/nothing-here")
    assert response.status_code == 404
    assert "nothing-here" in problem(response)["detail"]


def test_every_committed_learning_path_step_resolves_to_a_question(corpus_client):
    paths = corpus_client.get("/api/v1/learning-paths").json()["items"]
    assert paths, "the committed corpus holds learning paths"
    for path in paths:
        assert path["steps"], f"{path['slug']} has no steps"
        for step in path["steps"]:
            assert corpus_client.get(f"/api/v1/questions/{step['question_id']}").status_code == 200


# ---------------------------------------------------------------- search


def test_search_returns_both_kinds_in_one_ranked_list(fixture_client):
    body = fixture_client.get("/api/v1/search?q=admission").json()
    assert set(body) == {"items", "total", "limit", "offset"}
    assert body["total"] >= 2
    kinds = {hit["kind"] for hit in body["items"]}
    assert kinds == {"question", "lab"}, "one list, two kinds, or the endpoint is pointless"
    for hit in body["items"]:
        assert set(hit) == {"kind", "score", "item"}
        assert hit["item"]["id"]
        if hit["kind"] == "question":
            assert hit["item"]["type"], "a Question hit carries a whole Question"
        else:
            assert hit["item"]["question_ref"], "a Lab hit carries a whole Lab"


def test_hits_are_ranked_and_the_score_never_rises_down_the_page(fixture_client):
    scores = [hit["score"] for hit in fixture_client.get("/api/v1/search?q=admission").json()["items"]]
    assert scores == sorted(scores, reverse=True)


@pytest.mark.parametrize("kind", ["question", "lab"])
def test_kind_restricts_the_result_to_one_resource(fixture_client, kind):
    body = fixture_client.get(f"/api/v1/search?q=admission&kind={kind}").json()
    assert body["items"], f"the fixture corpus has an admission {kind}"
    assert {hit["kind"] for hit in body["items"]} == {kind}
    whole = fixture_client.get("/api/v1/search?q=admission").json()
    assert body["total"] <= whole["total"]


def test_the_two_kinds_together_account_for_the_whole_result(fixture_client):
    questions = fixture_client.get("/api/v1/search?q=admission&kind=question").json()
    labs = fixture_client.get("/api/v1/search?q=admission&kind=lab").json()
    both = fixture_client.get("/api/v1/search?q=admission").json()
    assert questions["total"] + labs["total"] == both["total"]


def test_search_pages_without_repeating_a_hit(fixture_client):
    first = fixture_client.get("/api/v1/search?q=kubernetes&limit=1").json()
    second = fixture_client.get("/api/v1/search?q=kubernetes&limit=1&offset=1").json()
    assert first["limit"] == 1 and second["offset"] == 1
    assert first["items"][0]["item"]["id"] != second["items"][0]["item"]["id"]
    assert first["items"][0]["score"] > second["items"][0]["score"]


def test_a_search_that_matches_nothing_is_an_empty_page(fixture_client):
    body = fixture_client.get("/api/v1/search?q=zzzznothingmatchesthis").json()
    assert body == {"items": [], "total": 0, "limit": 50, "offset": 0}


def test_an_unparseable_search_is_a_422_naming_the_parameter(fixture_client):
    """FTS5 syntax the client got wrong is a bad request, not a server fault."""
    response = fixture_client.get('/api/v1/search?q="unbalanced')
    assert response.status_code == 422
    body = problem(response)
    assert any(error["field"] == "q" for error in body["errors"])


def test_an_unparseable_free_text_filter_is_a_422_on_the_lists_too(fixture_client):
    for url in ('/api/v1/questions?q="unbalanced', '/api/v1/labs?q="unbalanced'):
        response = fixture_client.get(url)
        assert response.status_code == 422, url
        assert problem(response)["errors"][0]["field"] == "q"


@pytest.mark.parametrize("query", ["", "kind=quiz&q=admission", "q=admission&limit=0"])
def test_a_malformed_search_request_is_a_422(fixture_client, query):
    assert fixture_client.get(f"/api/v1/search?{query}").status_code == 422


def test_search_over_the_committed_corpus_finds_real_content(corpus_client):
    body = corpus_client.get("/api/v1/search?q=kubernetes&limit=10").json()
    assert body["total"] > 10, "the committed corpus says plenty about Kubernetes"
    assert len(body["items"]) == 10
    for hit in body["items"]:
        assert hit["item"]["content_hash"]
