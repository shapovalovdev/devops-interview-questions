import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from urllib.error import HTTPError

from validate_learning_resources import (
    HostPacer,
    REQUIRED_CATEGORIES,
    check_url,
    coverage_report,
    fetch_status,
    load_manifest,
    resource_links,
    validate_live,
)


class Response:
    status = 200

    def __init__(self, headers=None):
        self.headers = headers or {}

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

    def test_retries_transient_status_and_honours_retry_after(self) -> None:
        throttled = HTTPError(
            "https://example.test",
            429,
            "too many requests",
            {"Retry-After": "3"},
            None,
        )
        delays = []
        with patch("urllib.request.urlopen", side_effect=[throttled, Response()]) as open_url:
            result = check_url(
                "https://example.test/resource",
                1,
                sleeper=delays.append,
                pacer=HostPacer(0, sleeper=delays.append),
            )
        self.assertEqual("ok", result.category)
        self.assertEqual(2, result.attempts)
        self.assertEqual([3.0], delays)
        self.assertEqual(["HEAD", "HEAD"], [call.args[0].method for call in open_url.call_args_list])

    def test_pacer_spaces_requests_to_the_same_host_only(self) -> None:
        clock = iter([0.0, 0.0, 0.1, 0.1, 0.1, 0.1])
        delays = []
        pacer = HostPacer(1.0, clock=lambda: next(clock), sleeper=delays.append)
        pacer.pace("https://one.example/first")
        pacer.pace("https://two.example/first")
        pacer.pace("https://one.example/second")
        self.assertEqual([0.9], delays)

    def test_rate_limited_url_is_reported_separately_but_dead_url_fails(self) -> None:
        def response_for(request, timeout):
            if request.full_url == "https://rate.example":
                raise HTTPError(request.full_url, 418, "rate limited", {}, None)
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        output = io.StringIO()
        with patch("urllib.request.urlopen", side_effect=response_for):
            with redirect_stdout(output):
                with self.assertRaisesRegex(AssertionError, r"broken \(HTTP 404\)"):
                    validate_live(
                        {"https://rate.example", "https://dead.example"},
                        1,
                        sleeper=lambda _: None,
                        pacer=HostPacer(0),
                        workers=1,
                    )
        self.assertIn("https://rate.example: rate limited after 3 attempts", output.getvalue())


if __name__ == "__main__":
    unittest.main()
