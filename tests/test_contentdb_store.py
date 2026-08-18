"""The read seam slice 3 will code against, held to its documented answers.

`Store` is the one part of this slice another slice depends on, so these checks
are written the way a consumer would use it: build the fixture corpus once,
open the store, and ask questions whose answers are known by counting the
fixture rather than by trusting the implementation.

What is worth asserting here, beyond "the query runs":

- **Filters combine.** Each filter alone is easy; the bug lives in `theme` and
  `difficulty` together, so the combinations are checked explicitly.
- **Pagination is total-preserving.** `total` must describe the whole result,
  not the page, and an `offset` past the end must be an empty page with a true
  `total` rather than an error or a wrapped-around page.
- **Order is deterministic.** The epic makes `id` the default sort precisely so
  paging cannot skip or repeat a record; `difficulty` has to sort by rank, not
  alphabetically, or `junior` would outrank `staff`.
- **Records are plain mappings.** The seam is dictionaries keyed by the epic's
  field names. A test that accepts `sqlite3.Row` would let an object that only
  looks like a mapping leak into the API.
"""

from __future__ import annotations

import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import ingest, store  # noqa: E402  - needs the path above
from contentdb.models import LabQuery, QuestionQuery, SearchQuery  # noqa: E402

import contentdb_fixtures as fixtures  # noqa: E402  - a tests/ sibling


class StoreFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="contentdb-store-"))
        cls.root = fixtures.write_corpus(cls.tmp / "corpus")
        cls.database = cls.tmp / "content.db"
        cls.summary = ingest.build(cls.root, cls.database, **fixtures.PROVENANCE)
        cls.store = store.Store(cls.database)

    @classmethod
    def tearDownClass(cls):
        cls.store.close()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def ids(self, page) -> list[str]:
        return [item["id"] for item in page.items]


class ReadsQuestions(StoreFixture):
    def test_default_query_returns_every_question_sorted_by_id(self):
        page = self.store.list_questions()
        self.assertEqual(page.total, len(fixtures.QUESTIONS))
        self.assertEqual(len(page.items), len(fixtures.QUESTIONS))
        self.assertEqual(self.ids(page), sorted(self.ids(page)))

    def test_a_record_is_a_plain_mapping_with_the_pinned_fields(self):
        record = self.store.get_question("kubernetes/admission-policy")
        self.assertIs(type(record), dict)
        self.assertEqual(
            set(record),
            {
                "id", "theme", "slug", "title", "difficulty", "type", "tags", "sources",
                "prompt", "answer_guide", "body_markdown", "source_path", "content_hash", "updated_at",
            },
        )
        # The fixture writes these tags as `[kubernetes, security, cks]`, and the
        # store hands them back in that order: Export has to reproduce the source
        # file byte for byte, so author order is preserved rather than sorted.
        self.assertEqual(record["tags"], ["kubernetes", "security", "cks"])
        self.assertEqual(record["sources"][0]["source_type"], "official-docs")
        self.assertIs(type(record["sources"][0]), dict)
        self.assertEqual(len(record["answer_guide"]), 3)

    def test_unknown_id_is_none_not_an_error(self):
        self.assertIsNone(self.store.get_question("kubernetes/no-such"))

    def test_filter_by_theme(self):
        page = self.store.list_questions(QuestionQuery(theme="linux"))
        self.assertEqual(page.total, 4)
        self.assertTrue(all(item["theme"] == "linux" for item in page.items))

    def test_filter_by_difficulty_type_and_tag(self):
        self.assertEqual(self.store.list_questions(QuestionQuery(difficulty="staff")).total, 2)
        self.assertEqual(self.store.list_questions(QuestionQuery(type="theory")).total, 3)
        self.assertEqual(self.store.list_questions(QuestionQuery(tag="storage")).total, 2)

    def test_filters_combine_conjunctively(self):
        page = self.store.list_questions(QuestionQuery(theme="linux", difficulty="staff"))
        self.assertEqual(self.ids(page), ["linux/capacity-planning"])
        page = self.store.list_questions(QuestionQuery(theme="kubernetes", tag="storage"))
        self.assertEqual(self.ids(page), ["kubernetes/etcd-backup"])
        page = self.store.list_questions(QuestionQuery(theme="kubernetes", difficulty="staff", type="theory"))
        self.assertEqual(page.total, 0)
        self.assertEqual(page.items, ())

    def test_unknown_filter_value_returns_an_empty_page_not_an_error(self):
        page = self.store.list_questions(QuestionQuery(theme="no-such-theme"))
        self.assertEqual((page.total, page.items), (0, ()))

    def test_sort_by_difficulty_uses_rank_not_the_alphabet(self):
        page = self.store.list_questions(QuestionQuery(theme="linux", sort="difficulty"))
        self.assertEqual(
            [item["difficulty"] for item in page.items], ["junior", "middle", "senior", "staff"]
        )
        page = self.store.list_questions(QuestionQuery(theme="linux", sort="-difficulty"))
        self.assertEqual(
            [item["difficulty"] for item in page.items], ["staff", "senior", "middle", "junior"]
        )

    def test_sort_by_title_and_descending_id(self):
        page = self.store.list_questions(QuestionQuery(sort="title"))
        self.assertEqual([item["title"] for item in page.items], sorted(item["title"] for item in page.items))
        page = self.store.list_questions(QuestionQuery(sort="-id"))
        self.assertEqual(self.ids(page), sorted(self.ids(page), reverse=True))

    def test_an_unsupported_sort_is_refused(self):
        with self.assertRaises(ValueError):
            self.store.list_questions(QuestionQuery(sort="theme"))

    def test_full_text_filter_narrows_the_list(self):
        page = self.store.list_questions(QuestionQuery(q="CrashLoopBackOff"))
        self.assertEqual(self.ids(page), ["kubernetes/crashloop-debug"])
        page = self.store.list_questions(QuestionQuery(q="CrashLoopBackOff", theme="linux"))
        self.assertEqual(page.total, 0)


class Paginates(StoreFixture):
    def test_a_window_reports_the_whole_total(self):
        page = self.store.list_questions(QuestionQuery(limit=3))
        self.assertEqual((page.total, page.limit, page.offset), (len(fixtures.QUESTIONS), 3, 0))
        self.assertEqual(len(page.items), 3)

    def test_windows_tile_the_result_without_gaps_or_repeats(self):
        seen: list[str] = []
        for offset in range(0, len(fixtures.QUESTIONS), 3):
            seen.extend(self.ids(self.store.list_questions(QuestionQuery(limit=3, offset=offset))))
        self.assertEqual(seen, sorted(item["id"] for item in self.store.list_questions().items))

    def test_offset_on_the_last_boundary_returns_the_remainder(self):
        page = self.store.list_questions(QuestionQuery(limit=3, offset=6))
        self.assertEqual(len(page.items), 2)
        self.assertEqual(page.total, len(fixtures.QUESTIONS))

    def test_offset_past_the_end_is_an_empty_page_with_the_true_total(self):
        page = self.store.list_questions(QuestionQuery(offset=10_000))
        self.assertEqual(page.items, ())
        self.assertEqual(page.total, len(fixtures.QUESTIONS))
        self.assertEqual(page.offset, 10_000)

    def test_limit_is_capped_and_reported_as_applied(self):
        page = self.store.list_questions(QuestionQuery(limit=10_000))
        self.assertEqual(page.limit, 200)
        page = self.store.list_questions(QuestionQuery(limit=0))
        self.assertEqual((page.items, page.total), ((), len(fixtures.QUESTIONS)))

    def test_a_negative_window_is_refused(self):
        with self.assertRaises(ValueError):
            self.store.list_questions(QuestionQuery(offset=-1))
        with self.assertRaises(ValueError):
            self.store.list_questions(QuestionQuery(limit=-1))


class ReadsLabs(StoreFixture):
    def test_every_lab_is_listed_with_the_pinned_fields(self):
        page = self.store.list_labs()
        self.assertEqual(page.total, len(fixtures.LABS))
        record = self.store.get_lab("kubernetes/admission-lab")
        self.assertEqual(
            set(record),
            {
                "id", "theme", "slug", "title", "difficulty", "question_ref", "why", "checklist",
                "tags", "body_markdown", "source_path", "content_hash", "updated_at",
            },
        )
        self.assertEqual(record["question_ref"], "kubernetes/admission-policy")
        self.assertEqual(len(record["checklist"]), 3)

    def test_filter_by_question_ref_theme_difficulty_and_tag(self):
        page = self.store.list_labs(LabQuery(question_ref="linux/disk-full"))
        self.assertEqual(self.ids(page), ["linux/disk-lab"])
        self.assertEqual(self.store.list_labs(LabQuery(theme="linux")).total, 2)
        self.assertEqual(self.store.list_labs(LabQuery(difficulty="senior")).total, 1)
        self.assertEqual(self.store.list_labs(LabQuery(tag="storage")).total, 1)
        self.assertEqual(self.store.list_labs(LabQuery(theme="linux", difficulty="junior")).total, 1)

    def test_unknown_lab_id_is_none(self):
        self.assertIsNone(self.store.get_lab("linux/no-such"))


class ReadsThemesTagsAndPaths(StoreFixture):
    def test_themes_carry_their_counts_including_the_planned_one(self):
        themes = {theme["name"]: theme for theme in self.store.list_themes()}
        self.assertEqual(set(themes), set(fixtures.THEMES))
        self.assertEqual(themes["kubernetes"]["question_count"], 4)
        self.assertEqual(themes["kubernetes"]["lab_count"], 1)
        self.assertEqual(themes["queue-messaging"]["state"], "planned")
        self.assertEqual(themes["queue-messaging"]["question_count"], 0)
        self.assertEqual(
            themes["linux"]["difficulty_counts"], {"junior": 1, "middle": 1, "senior": 1, "staff": 1}
        )

    def test_get_theme_by_name(self):
        self.assertEqual(self.store.get_theme("linux")["state"], "complete")
        self.assertIsNone(self.store.get_theme("no-such-theme"))

    def test_tags_carry_question_and_lab_counts(self):
        tags = {tag["name"]: tag for tag in self.store.list_tags()}
        self.assertEqual(tags["storage"], {"name": "storage", "question_count": 2, "lab_count": 1})
        self.assertEqual(tags["cks"]["question_count"], 1)
        # `TAGS.md` is the permitted vocabulary, not an inventory: a Tag nothing
        # uses must not be advertised as a filter that returns something.
        self.assertIn("unused-tag", fixtures.TAGS_MD)
        self.assertNotIn("unused-tag", tags)

    def test_learning_paths_resolve_their_steps_in_order(self):
        paths = self.store.list_learning_paths()
        self.assertEqual([path["slug"] for path in paths], ["kubernetes-track"])
        path = self.store.get_learning_path("kubernetes-track")
        self.assertEqual(path["description"], fixtures.LEARNING_PATHS["paths"][0]["audience"])
        self.assertEqual(
            [step["question_id"] for step in path["steps"]],
            ["kubernetes/pod-scheduling", "kubernetes/admission-policy"],
        )
        self.assertEqual(
            [step["why"] for step in path["steps"]],
            [step["why"] for step in fixtures.LEARNING_PATHS["paths"][0]["steps"]],
        )
        self.assertEqual(path["prerequisites"], ["linux basics"])
        self.assertIsNone(self.store.get_learning_path("no-such-path"))


class Searches(StoreFixture):
    def test_search_spans_questions_and_labs(self):
        page = self.store.search(SearchQuery(q="admission"))
        kinds = {item["kind"] for item in page.items}
        self.assertEqual(kinds, {"question", "lab"})
        self.assertEqual(
            set(page.items[0]), {"kind", "id", "theme", "title", "snippet"}
        )

    def test_a_title_match_outranks_a_body_only_match(self):
        page = self.store.search(SearchQuery(q="admission"))
        order = [item["id"] for item in page.items]
        self.assertEqual(order[0], "kubernetes/admission-policy")
        self.assertIn("linux/kernel-tuning", order)
        self.assertLess(order.index("kubernetes/admission-policy"), order.index("linux/kernel-tuning"))

    def test_kind_narrows_the_search(self):
        page = self.store.search(SearchQuery(q="admission", kind="lab"))
        self.assertEqual([item["id"] for item in page.items], ["kubernetes/admission-lab"])
        self.assertEqual(page.total, 1)

    def test_search_paginates_like_the_lists(self):
        everything = self.store.search(SearchQuery(q="admission"))
        window = self.store.search(SearchQuery(q="admission", limit=1, offset=1))
        self.assertEqual(window.total, everything.total)
        self.assertEqual([item["id"] for item in window.items], [everything.items[1]["id"]])
        beyond = self.store.search(SearchQuery(q="admission", offset=99))
        self.assertEqual((beyond.items, beyond.total), ((), everything.total))

    def test_a_query_matching_nothing_is_an_empty_page(self):
        page = self.store.search(SearchQuery(q="zzzznotinthecorpus"))
        self.assertEqual((page.items, page.total), ((), 0))

    def test_a_malformed_search_query_is_refused_clearly(self):
        with self.assertRaises(store.SearchError):
            self.store.search(SearchQuery(q='"unbalanced'))


class WithoutFullTextSearch(unittest.TestCase):
    """A store built by a SQLite without FTS5 must still read, and say why it cannot search."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="contentdb-nofts-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        root = fixtures.write_corpus(self.tmp / "corpus")
        self.database = self.tmp / "content.db"
        ingest.build(root, self.database, **fixtures.PROVENANCE)
        connection = sqlite3.connect(self.database)
        connection.execute("DROP TABLE content_search")
        connection.commit()
        connection.close()

    def test_lists_still_work_but_search_raises_a_clear_error(self):
        with store.Store(self.database) as opened:
            self.assertEqual(opened.list_questions().total, len(fixtures.QUESTIONS))
            self.assertFalse(opened.search_available)
            with self.assertRaises(store.SearchUnavailable) as caught:
                opened.search(SearchQuery(q="admission"))
            self.assertIn("FTS5", str(caught.exception))
            with self.assertRaises(store.SearchUnavailable):
                opened.list_questions(QuestionQuery(q="admission"))


class RefusesToOpenNonsense(unittest.TestCase):
    def test_a_missing_database_says_so(self):
        with self.assertRaises(FileNotFoundError):
            store.Store(Path(tempfile.gettempdir()) / "contentdb-does-not-exist.db")

    def test_the_store_is_read_only(self):
        tmp = Path(tempfile.mkdtemp(prefix="contentdb-ro-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        root = fixtures.write_corpus(tmp / "corpus")
        database = tmp / "content.db"
        ingest.build(root, database, **fixtures.PROVENANCE)
        with store.Store(database) as opened:
            with self.assertRaises(sqlite3.OperationalError):
                opened.connection.execute("DELETE FROM questions")
