import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from validate_learning_resources import REQUIRED_CATEGORIES, coverage_report, fetch_status, load_manifest, resource_links


class Response:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


class LearningResourcesParserTests(unittest.TestCase):
    def test_accepts_all_five_required_categories_once(self) -> None:
        bullets = "\n".join(
            f"- {category.title()}: [resource](https://example.test/{index})"
            for index, category in enumerate(sorted(REQUIRED_CATEGORIES))
        )
        links = resource_links(f"# Question\n\n## What to learn next\n\n{bullets}\n", "fixture")
        self.assertEqual(5, len(links))

    def test_rejects_duplicate_urls(self) -> None:
        bullets = "\n".join(
            f"- {category.title()}: [resource](https://example.test/same)"
            for category in sorted(REQUIRED_CATEGORIES)
        )
        with self.assertRaisesRegex(AssertionError, "unique"):
            resource_links(f"## What to learn next\n\n{bullets}\n", "fixture")

    def test_rejects_missing_category(self) -> None:
        bullets = "\n".join(
            f"- Official documentation: [resource](https://example.test/{index})"
            for index in range(5)
        )
        with self.assertRaisesRegex(AssertionError, "categories"):
            resource_links(f"## What to learn next\n\n{bullets}\n", "fixture")

    def test_coverage_report_states_audited_scope(self) -> None:
        report = coverage_report(load_manifest())
        self.assertRegex(report, r"Learning-resource audit coverage: \d+/\d+ Questions")
        self.assertIn("Audited Themes:", report)

    def test_live_check_retries_get_when_host_rejects_head(self) -> None:
        head_rejected = HTTPError("https://example.test", 403, "forbidden", None, None)
        with patch("urllib.request.urlopen", side_effect=[head_rejected, Response()]) as open_url:
            self.assertEqual(200, fetch_status("https://example.test", 1))
        self.assertEqual(["HEAD", "GET"], [call.args[0].method for call in open_url.call_args_list])


if __name__ == "__main__":
    unittest.main()
