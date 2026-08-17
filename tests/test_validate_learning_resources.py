import errno
import io
import socket
import ssl
import threading
import time
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

from validate_learning_resources import (
    HostPacer,
    REQUIRED_CATEGORIES,
    check_url,
    coverage_report,
    fetch_status,
    github_blob_raw_url,
    host_queues,
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

    def test_retries_timeout_then_accepts_a_reachable_url(self) -> None:
        delays = []
        with patch("urllib.request.urlopen", side_effect=[TimeoutError("read timed out"), Response()]) as open_url:
            result = check_url(
                "https://temporary.example/resource",
                1,
                sleeper=delays.append,
                pacer=HostPacer(0, sleeper=delays.append),
            )
        self.assertEqual("ok", result.category)
        self.assertEqual(2, result.attempts)
        self.assertEqual([0.5], delays)
        self.assertEqual(2, open_url.call_count)

    def test_dns_and_tls_errors_are_hard_failures_without_retry(self) -> None:
        for error in (
            URLError(socket.gaierror("name resolution failed")),
            URLError(ssl.SSLCertVerificationError("certificate verify failed")),
        ):
            with self.subTest(error=error):
                with patch("urllib.request.urlopen", side_effect=error) as open_url:
                    result = check_url(
                        "https://permanent.example/resource",
                        1,
                        sleeper=lambda _: None,
                        pacer=HostPacer(0),
                    )
                self.assertEqual("network error", result.category)
                self.assertEqual(1, result.attempts)
                self.assertEqual(1, open_url.call_count)

    def test_truncated_tls_handshake_is_retried_not_declared_dead(self) -> None:
        """UNEXPECTED_EOF is a dropped connection — how a throttling host sheds load."""
        truncated = URLError(ssl.SSLError("[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol"))
        with patch("urllib.request.urlopen", side_effect=[truncated, Response()]) as open_url:
            result = check_url("https://kubernetes.io/docs/", 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("ok", result.category)
        self.assertEqual(2, open_url.call_count)

    def test_unroutable_network_is_indeterminate_not_broken(self) -> None:
        """A runner without IPv6 must not declare a healthy dual-stack host dead."""
        unreachable = URLError(OSError(errno.ENETUNREACH, "Network is unreachable"))
        with patch("urllib.request.urlopen", side_effect=unreachable) as open_url:
            result = check_url("https://www.gnu.org/software/bash/manual/", 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("network unreachable", result.category)
        self.assertEqual(3, open_url.call_count)

        output = io.StringIO()
        with patch("urllib.request.urlopen", side_effect=unreachable), redirect_stdout(output):
            validate_live(
                {"https://www.gnu.org/software/bash/manual/"},
                1,
                sleeper=lambda _: None,
                pacer=HostPacer(0),
                workers=1,
            )
        self.assertIn("network unreachable", output.getvalue())

    def test_bot_blocked_404_is_confirmed_with_a_browser_agent_before_failing(self) -> None:
        """csrc.nist.gov answers an unknown agent with 404 and a browser with 200."""

        def response_for(request, timeout):
            if "Mozilla" in request.headers.get("User-agent", ""):
                return Response()
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        with patch("urllib.request.urlopen", side_effect=response_for):
            result = check_url("https://csrc.nist.gov/pubs/sp/800/92/r1/ipd", 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("ok", result.category)
        self.assertIn("browser agent", result.detail)

    def test_a_genuinely_removed_page_still_fails_after_confirmation(self) -> None:
        def gone(request, timeout):
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        with patch("urllib.request.urlopen", side_effect=gone):
            result = check_url("https://example.test/removed", 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("broken", result.category)
        self.assertEqual("HTTP 404", result.detail)

    def test_dns_failure_is_still_broken_even_though_it_is_an_oserror(self) -> None:
        with patch("urllib.request.urlopen", side_effect=URLError(socket.gaierror(-2, "Name or service not known"))):
            result = check_url("https://gone.example/resource", 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("network error", result.category)

    def test_github_blob_404_with_raw_200_is_not_broken(self) -> None:
        """Secondary rate limiting on github.com must not read as a dead file."""

        def response_for(request, timeout):
            if request.full_url.startswith("https://raw.githubusercontent.com/"):
                return Response()
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        with patch("urllib.request.urlopen", side_effect=response_for):
            result = check_url(
                "https://github.com/shapovalovdev/devops-interview-questions/blob/main/questions/qemu-kvm/run-a-live-migration-you-trust.md",
                1,
                sleeper=lambda _: None,
                pacer=HostPacer(0),
            )
        self.assertEqual("ok", result.category)
        self.assertIn("raw.githubusercontent.com", result.detail)

    def test_github_blob_404_with_raw_404_is_broken(self) -> None:
        def response_for(request, timeout):
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        with patch("urllib.request.urlopen", side_effect=response_for):
            result = check_url(
                "https://github.com/shapovalovdev/devops-interview-questions/blob/main/questions/removed.md",
                1,
                sleeper=lambda _: None,
                pacer=HostPacer(0),
            )
        self.assertEqual("broken", result.category)
        self.assertEqual("HTTP 404 on github.com and raw.githubusercontent.com", result.detail)

    def test_github_blob_404_with_raw_rate_limited_is_indeterminate_not_broken(self) -> None:
        def response_for(request, timeout):
            if request.full_url.startswith("https://raw.githubusercontent.com/"):
                raise HTTPError(request.full_url, 403, "rate limited", {}, None)
            raise HTTPError(request.full_url, 404, "not found", {}, None)

        url = "https://github.com/shapovalovdev/devops-interview-questions/blob/main/README.md"
        with patch("urllib.request.urlopen", side_effect=response_for):
            result = check_url(url, 1, sleeper=lambda _: None, pacer=HostPacer(0))
        self.assertEqual("indeterminate", result.category)

        output = io.StringIO()
        with patch("urllib.request.urlopen", side_effect=response_for), redirect_stdout(output):
            validate_live({url}, 1, sleeper=lambda _: None, pacer=HostPacer(0), workers=1)
        self.assertIn("indeterminate", output.getvalue())
        self.assertNotIn(": broken", output.getvalue())

    def test_blob_to_raw_rewrite_handles_refs_and_nested_paths(self) -> None:
        self.assertEqual(
            "https://raw.githubusercontent.com/org/repo/main/docs/deep/nested/file.md",
            github_blob_raw_url("https://github.com/org/repo/blob/main/docs/deep/nested/file.md"),
        )
        self.assertEqual(
            "https://raw.githubusercontent.com/org/repo/v1.2.3/guide.md",
            github_blob_raw_url("https://github.com/org/repo/blob/v1.2.3/guide.md"),
        )
        self.assertIsNone(github_blob_raw_url("https://github.com/org/repo/tree/main/docs"))
        self.assertIsNone(github_blob_raw_url("https://example.com/org/repo/blob/main/file.md"))


class LiveCheckSchedulingTests(unittest.TestCase):
    """The audit is scheduled by host, so raising concurrency cannot raise the per-host rate.

    These run real threads against a stubbed transport, never the network. The
    pace interval is shortened so the assertions cost tenths of a second, and
    gaps are compared with a small tolerance because the timestamp is taken just
    after the pacer releases the request, which the scheduler can delay by a
    millisecond or two. A pacer that had stopped working would produce gaps two
    orders of magnitude below the interval, so the tolerance cannot hide one.
    """

    INTERVAL = 0.1
    TOLERANCE = 0.01
    HOSTS = 24
    PER_HOST = 4

    @staticmethod
    def recording_transport():
        """A stub urlopen that answers 200 and records (host, time) per request."""
        requests: list[tuple[str, float]] = []
        lock = threading.Lock()

        def respond(request, timeout):
            with lock:
                requests.append((urlparse(request.full_url).netloc, time.monotonic()))
            return Response()

        return requests, respond

    @classmethod
    def urls_for(cls, hosts: int, per_host: int) -> set[str]:
        return {f"https://host{host}.example/page{page}" for host in range(hosts) for page in range(per_host)}

    def check_all(self, urls: set[str], workers: int) -> tuple[list[tuple[str, float]], float]:
        requests, respond = self.recording_transport()
        started = time.monotonic()
        with patch("urllib.request.urlopen", side_effect=respond):
            validate_live(urls, 1, pacer=HostPacer(self.INTERVAL), workers=workers)
        return requests, time.monotonic() - started

    def test_host_queues_group_every_url_busiest_first(self) -> None:
        urls = {"https://a.example/1", "https://a.example/2", "https://b.example/1", "https://c.example/1"}
        queues = host_queues(urls)
        self.assertEqual([2, 1, 1], [len(queue) for queue in queues])
        self.assertEqual(urls, {url for queue in queues for url in queue})

    def test_per_host_rate_holds_when_many_hosts_run_at_once(self) -> None:
        urls = self.urls_for(self.HOSTS, self.PER_HOST)
        requests, _ = self.check_all(urls, workers=32)

        self.assertEqual(len(urls), len(requests), "every URL is checked exactly once")
        by_host: dict[str, list[float]] = {}
        for host, at in requests:
            by_host.setdefault(host, []).append(at)
        self.assertEqual(self.HOSTS, len(by_host))
        for host, times in sorted(by_host.items()):
            ordered = sorted(times)
            gaps = [later - earlier for earlier, later in zip(ordered, ordered[1:])]
            self.assertEqual(self.PER_HOST - 1, len(gaps))
            self.assertGreaterEqual(
                min(gaps),
                self.INTERVAL - self.TOLERANCE,
                f"{host} was requested faster than one request per interval: {gaps}",
            )

    def test_a_paced_host_does_not_starve_the_others(self) -> None:
        """The run is bounded by the busiest host's queue, not by the total URL count."""
        urls = self.urls_for(self.HOSTS, self.PER_HOST)
        _, elapsed = self.check_all(urls, workers=32)

        one_host_queue = (self.PER_HOST - 1) * self.INTERVAL
        self.assertGreaterEqual(elapsed, one_host_queue, "the pace interval was skipped")
        self.assertLess(
            elapsed,
            self.HOSTS * one_host_queue / 4,
            "hosts waited on each other's pace intervals instead of being checked at once",
        )


if __name__ == "__main__":
    unittest.main()
