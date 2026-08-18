"""The `Store` seam, and the rules that let `contentdb` implement it later.

Slice 1 is building the real Content store in parallel, standard-library only.
It can only implement this protocol if the seam stays free of Pydantic and of
`api/` itself, so those two rules are asserted here rather than left as a
comment nobody runs.
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections.abc import Mapping

import pytest

from support import ROOT, demo_corpus

from api.store import DEFAULT_SORT, SORT_KEYS, LabQuery, Page, QuestionQuery, SearchQuery, Store
from api.testing import InMemoryStore, sorted_records

QUESTION_FIELDS = {
    "id", "theme", "slug", "title", "difficulty", "type", "tags", "sources",
    "prompt", "answer_guide", "body_markdown", "source_path", "content_hash",
    "updated_at",
}
LAB_FIELDS = {
    "id", "theme", "slug", "title", "difficulty", "tags", "question_ref", "why",
    "checklist", "body_markdown", "source_path", "content_hash", "updated_at",
}


# ------------------------------------------------- what crosses the seam


def test_only_plain_mappings_come_back_from_the_store():
    page = demo_corpus().list_questions(QuestionQuery())
    assert isinstance(page, Page)
    for record in page.items:
        assert isinstance(record, Mapping)
        assert type(record) is dict, (
            "the seam carries plain mappings; a model here would force contentdb "
            f"to import api/, but got {type(record)!r}"
        )
        assert set(record) == QUESTION_FIELDS


def test_lab_records_carry_the_epics_lab_fields():
    for record in demo_corpus().list_labs(LabQuery()).items:
        assert set(record) == LAB_FIELDS


def test_every_record_is_json_shaped():
    """Timestamps cross as ISO 8601 strings, exactly as SQLite will store them."""
    store = demo_corpus()
    for record in store.list_questions(QuestionQuery()).items:
        json.dumps(record)
        assert record["updated_at"].endswith("Z")
        assert record["sources"][0]["verified_on"] == "2026-08-01"


def test_the_seam_module_imports_nothing_third_party():
    """`api.store` must be importable in the interpreter `contentdb` runs in.

    A subprocess is the only honest way to check: by the time this test module
    is running, Pydantic is long since imported by something else.
    """
    program = (
        "import sys; import api.store; "
        "leaked = sorted(m for m in sys.modules "
        "if m.split('.')[0] in {'pydantic', 'pydantic_core', 'fastapi', 'starlette', 'yaml'}); "
        "print(leaked)"
    )
    completed = subprocess.run(
        [sys.executable, "-c", program],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.strip() == "[]", (
        f"importing api.store dragged in third-party modules: {completed.stdout.strip()}"
    )


def test_a_standard_library_only_class_satisfies_the_protocol():
    """What slice 3 will do: implement the protocol without importing `api/`."""

    class Contentdb:
        def list_questions(self, query): return Page(items=[], total=0)
        def get_question(self, question_id): return None
        def list_labs(self, query): return Page(items=[], total=0)
        def get_lab(self, lab_id): return None
        def list_themes(self): return Page(items=[], total=0)
        def get_theme(self, name): return None
        def list_tags(self): return Page(items=[], total=0)
        def list_learning_paths(self): return Page(items=[], total=0)
        def get_learning_path(self, slug): return None
        def search(self, query): return Page(items=[], total=0)

    assert isinstance(Contentdb(), Store)


def test_a_class_missing_a_method_does_not_satisfy_the_protocol():
    class Partial:
        def list_questions(self, query): return Page(items=[], total=0)

    assert not isinstance(Partial(), Store)


# ---------------------------------------------------------------- the query


def test_the_default_sort_on_the_query_is_id():
    assert DEFAULT_SORT == "id"
    assert QuestionQuery().sort == "id"
    assert LabQuery().sort == "id"
    assert SORT_KEYS == ("id", "title", "difficulty", "updated_at")


def test_the_query_is_immutable_so_a_store_cannot_rewrite_it():
    query = QuestionQuery(theme="linux")
    with pytest.raises(Exception):
        query.theme = "kubernetes"  # type: ignore[misc]


# ------------------------------------------------- the in-memory reference


@pytest.mark.parametrize("key", SORT_KEYS)
def test_sorting_is_total_in_both_directions(key):
    records = demo_corpus().questions
    ascending = [r["id"] for r in sorted_records(records, key)]
    descending = [r["id"] for r in sorted_records(records, f"-{key}")]
    assert sorted(ascending) == sorted(r["id"] for r in records)
    assert descending == list(reversed(ascending))


def test_id_breaks_every_tie_so_paging_never_repeats_or_skips():
    records = [
        {"id": "b/two", "title": "Same", "difficulty": "junior", "updated_at": "2026-01-01T00:00:00Z"},
        {"id": "a/one", "title": "Same", "difficulty": "junior", "updated_at": "2026-01-01T00:00:00Z"},
    ]
    assert [r["id"] for r in sorted_records(records, "title")] == ["a/one", "b/two"]


def test_an_unsupported_sort_key_is_refused_by_the_store():
    with pytest.raises(ValueError, match="unsupported sort key"):
        sorted_records(demo_corpus().questions, "slug")


def test_the_page_reports_the_total_before_the_window():
    page = demo_corpus().list_questions(QuestionQuery(limit=1, offset=1))
    assert page.total == 4
    assert [record["id"] for record in page.items] == ["kubernetes/demo-pod-disruption"]


def test_reads_by_id_find_and_miss():
    store = demo_corpus()
    assert store.get_question("linux/demo-exit-codes")["title"] == "Explain process exit codes"
    assert store.get_question("linux/nothing-here") is None
    assert store.get_lab("linux/demo-exit-codes")["question_ref"] == "linux/demo-exit-codes"
    assert store.get_lab("linux/nothing-here") is None
    assert store.get_theme("kubernetes")["question_count"] == 2
    assert store.get_theme("nothing-here") is None
    assert store.get_learning_path("demo-kubernetes-basics")["title"] == "Kubernetes basics"
    assert store.get_learning_path("nothing-here") is None


def test_the_taxonomy_reads_come_back_enveloped():
    store = demo_corpus()
    assert store.list_themes().total == 3
    assert store.list_tags().total == 2
    assert store.list_learning_paths().total == 1


def test_an_empty_store_answers_every_read():
    store = InMemoryStore()
    assert store.list_themes() == Page(items=[], total=0)
    assert store.list_tags() == Page(items=[], total=0)
    assert store.list_learning_paths() == Page(items=[], total=0)
    assert store.list_questions(QuestionQuery()) == Page(items=[], total=0)


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        (LabQuery(theme="linux"), ["linux/demo-exit-codes"]),
        (LabQuery(difficulty="senior"), ["kubernetes/demo-admission-guardrails"]),
        (LabQuery(tag="security"), ["kubernetes/demo-admission-guardrails"]),
        (LabQuery(question_ref="linux/demo-exit-codes"), ["linux/demo-exit-codes"]),
        (LabQuery(q="privileged"), ["kubernetes/demo-admission-guardrails"]),
        (LabQuery(theme="linux", tag="security"), []),
    ],
)
def test_the_lab_query_filters_the_way_the_contract_describes(query, expected):
    """Slice 3 serves these; the seam already answers them correctly."""
    assert [r["id"] for r in demo_corpus().list_labs(query).items] == expected


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        (SearchQuery(q="admission"), ["kubernetes/demo-admission-guardrails", "kubernetes/demo-admission-guardrails"]),
        (SearchQuery(q="admission", kind="question"), ["kubernetes/demo-admission-guardrails"]),
        (SearchQuery(q="admission", kind="lab"), ["kubernetes/demo-admission-guardrails"]),
        (SearchQuery(q="nothing matches this"), []),
    ],
)
def test_search_spans_questions_and_labs(query, expected):
    assert [hit["item"]["id"] for hit in demo_corpus().search(query).items] == expected


def test_a_search_hit_says_which_kind_it_is_and_ranks_descending():
    """One ranked list carries both kinds, so a hit has to name its own."""
    hits = demo_corpus().search(SearchQuery(q="admission")).items
    assert [hit["kind"] for hit in hits] == ["question", "lab"]
    assert [hit["score"] for hit in hits] == sorted((h["score"] for h in hits), reverse=True)
    assert set(hits[0]) == {"kind", "score", "item"}
