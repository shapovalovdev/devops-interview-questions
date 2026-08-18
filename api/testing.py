"""An in-memory `Store` for tests and for the demo entrypoint.

This is a fake, and it is named so that nothing mistakes it for the Content
store. `create_app()` deliberately refuses to fall back to it: serving invented
Questions from a production entrypoint would be a correctness bug, because a
client cannot tell fabricated content from the corpus. The only two places it
belongs are the test suite and `api/demo.py`, which announces in its name what
it is serving.

Like the real store, this one keeps plain mappings and hands back plain
mappings — dates and timestamps as ISO 8601 strings, the way SQLite will store
them — so the tests exercise the same seam slice 3 will implement.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from typing import Any

from api.store import Record, SORT_KEYS, LabQuery, Page, QuestionQuery, RecordInUse, SearchQuery
from api.writes import timestamp

#: Difficulty sorts by seniority, not alphabetically; the two happen to agree
#: today, but the corpus should not depend on that coincidence.
DIFFICULTY_ORDER = {"junior": 0, "middle": 1, "senior": 2, "staff": 3}


def _sort_value(record: Record, key: str) -> Any:
    if key == "difficulty":
        return DIFFICULTY_ORDER.get(str(record.get("difficulty")), len(DIFFICULTY_ORDER))
    return record.get(key, "")


def sorted_records(records: Iterable[Record], sort: str) -> list[Record]:
    """Order records by the contract's sort vocabulary, `id` breaking every tie.

    The tie-break is what makes `limit`/`offset` paging total: without it, two
    records sharing a `title` could swap places between requests and a client
    would miss one.
    """
    descending = sort.startswith("-")
    key = sort.removeprefix("-")
    if key not in SORT_KEYS:
        raise ValueError(f"unsupported sort key: {sort!r}")
    ascending = sorted(records, key=lambda record: (_sort_value(record, key), record["id"]))
    return list(reversed(ascending)) if descending else ascending


def _contains(record: Record, needle: str, fields: Sequence[str]) -> bool:
    lowered = needle.lower()
    return any(lowered in str(record.get(name, "")).lower() for name in fields)


def _matches_question(record: Record, query: QuestionQuery) -> bool:
    if query.theme is not None and record["theme"] != query.theme:
        return False
    if query.difficulty is not None and record["difficulty"] != query.difficulty:
        return False
    if query.type is not None and record["type"] != query.type:
        return False
    if query.tag is not None and query.tag not in record["tags"]:
        return False
    if query.q is not None and not _contains(record, query.q, ("title", "prompt", "body_markdown")):
        return False
    return True


def _matches_lab(record: Record, query: LabQuery) -> bool:
    if query.theme is not None and record["theme"] != query.theme:
        return False
    if query.difficulty is not None and record["difficulty"] != query.difficulty:
        return False
    if query.tag is not None and query.tag not in record["tags"]:
        return False
    if query.question_ref is not None and record["question_ref"] != query.question_ref:
        return False
    if query.q is not None and not _contains(record, query.q, ("title", "why", "body_markdown")):
        return False
    return True


def _window(records: Sequence[Record], limit: int, offset: int) -> Page:
    return Page(items=list(records[offset : offset + limit]), total=len(records))


@dataclass
class InMemoryStore:
    """A `Store` backed by dictionaries, for tests and the demo service."""

    questions: list[Record] = field(default_factory=list)
    labs: list[Record] = field(default_factory=list)
    themes: list[Record] = field(default_factory=list)
    tags: list[Record] = field(default_factory=list)
    learning_paths: list[Record] = field(default_factory=list)
    #: The append-only write trail, matching what the real store keeps in its
    #: `content_writes` table. The fake carries it for the same reason it
    #: carries counts: a test that passes here and fails against SQLite is a
    #: fake that has stopped standing in for the real thing.
    writes: list[Record] = field(default_factory=list)

    def list_questions(self, query: QuestionQuery) -> Page:
        matched = sorted_records(
            [record for record in self.questions if _matches_question(record, query)], query.sort
        )
        return _window(matched, query.limit, query.offset)

    def get_question(self, question_id: str) -> Record | None:
        return next((record for record in self.questions if record["id"] == question_id), None)

    def list_labs(self, query: LabQuery) -> Page:
        matched = sorted_records(
            [record for record in self.labs if _matches_lab(record, query)], query.sort
        )
        return _window(matched, query.limit, query.offset)

    def get_lab(self, lab_id: str) -> Record | None:
        return next((record for record in self.labs if record["id"] == lab_id), None)

    def list_themes(self) -> Page:
        return _window(self.themes, len(self.themes) or 1, 0)

    def get_theme(self, name: str) -> Record | None:
        return next((record for record in self.themes if record["name"] == name), None)

    def list_tags(self) -> Page:
        return _window(self.tags, len(self.tags) or 1, 0)

    def list_learning_paths(self) -> Page:
        return _window(self.learning_paths, len(self.learning_paths) or 1, 0)

    def get_learning_path(self, slug: str) -> Record | None:
        return next((record for record in self.learning_paths if record["slug"] == slug), None)

    def search(self, query: SearchQuery) -> Page:
        """Rank matches the way the seam documents: hits, not bare items.

        A hit nests its item under `item` and carries the `kind` that says which
        of the two resources it is, because one ranked list holds both. The
        score is derived from rank — the contract only promises it is comparable
        within one response — which is also what the real store does, since
        SQLite's bm25 score does not cross the seam.
        """
        matched: list[tuple[str, Record]] = []
        if query.kind in (None, "question"):
            matched += [("question", r) for r in self.questions if _contains(r, query.q, ("title", "prompt"))]
        if query.kind in (None, "lab"):
            matched += [("lab", r) for r in self.labs if _contains(r, query.q, ("title", "why"))]
        # A stable sort by `id` keeps Questions ahead of the Labs that share
        # their id, so a hit list never reorders between two identical requests.
        ranked = sorted(matched, key=lambda pair: pair[1]["id"])
        hits: list[Record] = [
            {"kind": kind, "score": 1.0 / (1.0 + rank), "item": record}
            for rank, (kind, record) in enumerate(ranked)
        ]
        return _window(hits, query.limit, query.offset)

    # -- Writes ------------------------------------------------------------
    #
    # The fake implements the write seam so the demo entrypoint and the fast
    # half of the suite can exercise it, and it implements it *the same way* the
    # SQLite store does — replacing rather than appending, recounting Themes and
    # tags from the records rather than adjusting them, and refusing to delete a
    # Question something still points at. A fake that were merely permissive
    # would let a test pass that the real store rejects, which is precisely the
    # class of divergence the committed-corpus sweep exists to catch.

    def write_question(self, record: Record, method: str) -> Record:
        self._replace(self.questions, record)
        self._recount()
        self._record_write("question", record, method)
        return self.get_question(str(record["id"]))

    def delete_question(self, question_id: str, method: str) -> None:
        references = [lab["id"] for lab in self.labs if lab["question_ref"] == question_id]
        references += [
            path["slug"]
            for path in self.learning_paths
            if any(step["question_id"] == question_id for step in path["steps"])
        ]
        if references:
            raise RecordInUse(
                f"{question_id} cannot be deleted while the corpus still points at it: "
                f"{', '.join(references)}.",
                references,
            )
        self._remove(self.questions, question_id)
        self._recount()
        self._record_write("question", {"id": question_id}, method)

    def write_lab(self, record: Record, method: str) -> Record:
        self._replace(self.labs, record)
        self._recount()
        self._record_write("lab", record, method)
        return self.get_lab(str(record["id"]))

    def delete_lab(self, lab_id: str, method: str) -> None:
        self._remove(self.labs, lab_id)
        self._recount()
        self._record_write("lab", {"id": lab_id}, method)

    def audit_trail(self, identifier: str | None = None) -> list[Record]:
        if identifier is None:
            return list(self.writes)
        return [entry for entry in self.writes if entry["id"] == identifier]

    @staticmethod
    def _replace(records: list[Record], record: Record) -> None:
        for position, existing in enumerate(records):
            if existing["id"] == record["id"]:
                records[position] = dict(record)
                return
        records.append(dict(record))

    @staticmethod
    def _remove(records: list[Record], identifier: str) -> None:
        records[:] = [record for record in records if record["id"] != identifier]

    def _record_write(self, kind: str, record: Record, method: str) -> None:
        self.writes.append(
            {
                "sequence": len(self.writes) + 1,
                "kind": kind,
                "id": record["id"],
                "method": method,
                "written_at": timestamp(),
                "content_hash": record.get("content_hash"),
            }
        )

    def _recount(self) -> None:
        """Rebuild the Theme and tag catalogues from the records, as the store does."""
        for theme in self.themes:
            owned = [record for record in self.questions if record["theme"] == theme["name"]]
            theme["question_count"] = len(owned)
            theme["lab_count"] = sum(1 for lab in self.labs if lab["theme"] == theme["name"])
            theme["difficulty_counts"] = {
                difficulty: sum(1 for record in owned if record["difficulty"] == difficulty)
                for difficulty in DIFFICULTY_ORDER
            }
        used: dict[str, list[int]] = {}
        for record in self.questions:
            for tag in record["tags"]:
                used.setdefault(tag, [0, 0])[0] += 1
        for record in self.labs:
            for tag in record["tags"]:
                used.setdefault(tag, [0, 0])[1] += 1
        self.tags[:] = [
            {"name": name, "question_count": counts[0], "lab_count": counts[1]}
            for name, counts in sorted(used.items())
        ]


def question_record(
    theme: str,
    slug: str,
    title: str,
    difficulty: str,
    type: str,
    tags: list[str],
    prompt: str,
    updated_at: str,
) -> dict[str, Any]:
    """A Question record shaped exactly as the epic pins the resource.

    The body is a real corpus document, not a placeholder: `prompt` is the
    paragraph under the `# ` heading and `answer_guide` is the `- ` points under
    `## Answer guide`, because that is where `contentdb.corpus` reads them from.
    A fake whose records could not survive a write would make every write test
    against it a test of the fake.
    """
    guide = f"Name the trade-off behind {title.lower()}."
    return {
        "id": f"{theme}/{slug}",
        "theme": theme,
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "type": type,
        "tags": tags,
        "sources": [
            {
                "url": "https://kubernetes.io/docs/home/",
                "source_type": "official-docs",
                "verified_on": "2026-08-01",
            }
        ],
        "prompt": prompt,
        "answer_guide": [guide],
        "body_markdown": f"\n# {title}\n\n{prompt}\n\n## Answer guide\n\n- {guide}",
        "source_path": f"questions/{theme}/{slug}.md",
        "content_hash": f"sha256:{theme}-{slug}",
        "updated_at": updated_at,
    }


def lab_record(
    theme: str,
    slug: str,
    title: str,
    difficulty: str,
    tags: list[str],
    question_ref: str,
    why: str,
    updated_at: str,
) -> dict[str, Any]:
    """A Lab record shaped exactly as the epic pins the resource.

    A Lab's fields are all front matter, so its body is carried through
    verbatim; it still gets a real one, so that rendering a Lab from this fake
    produces the document a corpus file would.
    """
    step = f"Work through {title.lower()} on a throwaway cluster."
    return {
        "id": f"{theme}/{slug}",
        "theme": theme,
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "tags": tags,
        "question_ref": question_ref,
        "why": why,
        "checklist": [step],
        "body_markdown": f"\n# {title}\n\n{why}\n\n## Steps\n\n- {step}",
        "source_path": f"labs/{theme}/{slug}.md",
        "content_hash": f"sha256:{theme}-{slug}",
        "updated_at": updated_at,
    }


def demo_corpus() -> InMemoryStore:
    """A handful of obviously-fake records, enough to exercise every filter.

    Every id carries a `demo-` prefix so that a record served by the demo
    entrypoint can never be mistaken for a Question from the corpus.
    """
    questions = [
        question_record(
            "kubernetes", "demo-admission-guardrails", "Design admission guardrails",
            "senior", "scenario", ["kubernetes", "security", "cks"],
            "How would you stop an unsafe workload manifest reaching production?",
            "2026-08-01T09:00:00Z",
        ),
        question_record(
            "kubernetes", "demo-pod-disruption", "Reason about PodDisruptionBudgets",
            "staff", "theory", ["kubernetes", "reliability"],
            "When does a PodDisruptionBudget block a node drain?",
            "2026-08-10T09:00:00Z",
        ),
        question_record(
            "linux", "demo-exit-codes", "Explain process exit codes",
            "junior", "theory", ["linux", "processes"],
            "What does an exit status of 127 tell you?",
            "2026-07-20T09:00:00Z",
        ),
        question_record(
            "observability", "demo-cardinality", "Control metric cardinality",
            "middle", "troubleshooting", ["observability", "prometheus"],
            "Your series count exploded overnight. How do you bring it back?",
            "2026-08-05T09:00:00Z",
        ),
    ]
    labs = [
        lab_record(
            "kubernetes", "demo-admission-guardrails", "Break and repair an admission policy",
            "senior", ["kubernetes", "security"], "kubernetes/demo-admission-guardrails",
            "Practice writing a policy that rejects privileged pods.",
            "2026-08-03T09:00:00Z",
        ),
        lab_record(
            "linux", "demo-exit-codes", "Hunt a failing process by its exit code",
            "junior", ["linux"], "linux/demo-exit-codes",
            "Reproduce exit statuses 127 and 139 and diagnose each.",
            "2026-07-22T09:00:00Z",
        ),
    ]
    themes = [
        {
            "name": "kubernetes", "state": "active", "question_count": 2, "lab_count": 1,
            "difficulty_counts": {"senior": 1, "staff": 1},
        },
        {
            "name": "linux", "state": "active", "question_count": 1, "lab_count": 1,
            "difficulty_counts": {"junior": 1},
        },
        {
            "name": "observability", "state": "active", "question_count": 1, "lab_count": 0,
            "difficulty_counts": {"middle": 1},
        },
    ]
    tags = [
        {"name": "kubernetes", "question_count": 2, "lab_count": 1},
        {"name": "linux", "question_count": 1, "lab_count": 1},
    ]
    learning_paths = [
        {
            "slug": "demo-kubernetes-basics",
            "title": "Kubernetes basics",
            "description": "A first sequence through the Kubernetes Theme.",
            "steps": [
                {
                    "question_id": "kubernetes/demo-admission-guardrails",
                    "why": "Admission control is the guardrail every later step assumes.",
                }
            ],
        }
    ]
    return InMemoryStore(
        questions=questions,
        labs=labs,
        themes=themes,
        tags=tags,
        learning_paths=learning_paths,
    )


def demo_store() -> InMemoryStore:
    """Factory form of `demo_corpus`, usable as a `CONTENT_API_STORE` target."""
    return demo_corpus()
