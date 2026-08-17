#!/usr/bin/env python3
"""Validate staged, curated learning resources and optionally check their URLs.

This validator deliberately does not invent links or infer their category from a
domain.  A maintainer adds a Question to the audit manifest only after reviewing
its five resources.  The same parser is used for Question learning sections and
Theme related-material pages.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import errno
import json
import re
import socket
import ssl
import sys
import threading
import time
from collections import Counter
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/research/link-audit-manifest.json"
UNVERIFIABLE_HOSTS = ROOT / "docs/research/unverifiable-hosts.json"
LABS = ROOT / "labs"
REQUIRED_CATEGORIES = {
    "official documentation",
    "manual or specification",
    "maintainer or personal blog",
    "technical blog",
    "hands-on guide",
}
LINK_PATTERN = re.compile(r"^- ([^:]+): \[[^]]+\]\((https://[^)\s]+)\)\s*$", re.MULTILINE)
# Labs cite links in prose, fenced commands, and Markdown links rather than in a
# curated five-category list, so their URLs are matched directly.
LAB_LINK_PATTERN = re.compile(r"https://[^\s`\"'()<>\\]+")
USER_AGENT = "DevOpsQuestionDatabaseLinkAudit/1.0 (+https://github.com/shapovalovdev/devops-interview-questions)"
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)
MAX_ATTEMPTS = 3
DEFAULT_RETRY_DELAY_SECONDS = 0.5
MAX_RETRY_AFTER_SECONDS = 30.0
# One request per second per host. A link checker that fires five requests a
# second at one host gets throttled, and csrc.nist.gov expresses throttling as
# 404 rather than 429 — indistinguishable from a dead page by status alone.
HOST_REQUEST_INTERVAL_SECONDS = 1.0
CONFIRMATION_DELAYS_SECONDS = (2.0, 5.0, 15.0)
# Workers check distinct hosts, not distinct URLs: one worker owns one host's
# queue at a time, so the only pace interval it ever waits out is its own. With
# a URL-per-worker pool, eight workers drawing from a URL list sorted by host
# all queued behind the same host lock while the other 300 hosts sat idle, and
# the 1,600-URL manifest took 25-30 minutes against a three-minute floor.
LIVE_CHECK_HOST_WORKERS = 32
TRANSIENT_STATUSES = {403, 418, 429}
GITHUB_BLOB_URL_PATTERN = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$")


@dataclass(frozen=True)
class FetchResult:
    status: int
    headers: object


@dataclass(frozen=True)
class LinkCheck:
    url: str
    category: str
    detail: str
    attempts: int


class HostPacer:
    """Serialize requests per host without blocking checks for other hosts."""

    def __init__(self, interval: float, clock=time.monotonic, sleeper=time.sleep) -> None:
        self.interval = interval
        self.clock = clock
        self.sleeper = sleeper
        self.last_request: dict[str, float] = {}
        self.host_locks: dict[str, threading.Lock] = {}
        self.lock = threading.Lock()

    def pace(self, url: str) -> None:
        host = urlparse(url).netloc
        with self.lock:
            host_lock = self.host_locks.setdefault(host, threading.Lock())
        with host_lock:
            now = self.clock()
            delay = max(0.0, self.interval - (now - self.last_request.get(host, float("-inf"))))
            if delay:
                self.sleeper(delay)
            self.last_request[host] = self.clock()


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    assert match, f"missing '## {heading}' section"
    return match.group(1).strip()


def resource_links(text: str, context: str) -> list[tuple[str, str]]:
    links = LINK_PATTERN.findall(section(text, "What to learn next"))
    assert len(links) == 5, f"{context}: requires exactly five curated learning links"
    categories = {category.strip().lower() for category, _ in links}
    assert categories == REQUIRED_CATEGORIES, (
        f"{context}: categories must be {sorted(REQUIRED_CATEGORIES)}, got {sorted(categories)}"
    )
    urls = [url for _, url in links]
    assert len(urls) == len(set(urls)), f"{context}: learning links must be unique"
    return links


def load_manifest() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data.get("version") == 1, "link-audit manifest must use version 1"
    audited = data.get("audited_questions")
    assert isinstance(audited, list) and audited, "link-audit manifest needs audited Questions"
    return data


def audit_scope(manifest: dict) -> list[tuple[Path, Path]]:
    scope: list[tuple[Path, Path]] = []
    seen_questions: set[str] = set()
    for item in manifest["audited_questions"]:
        question = ROOT / item["question"]
        related = ROOT / item["related_materials"]
        assert question.is_file(), f"manifest Question does not exist: {question}"
        assert related.is_file(), f"manifest related-materials page does not exist: {related}"
        assert item["question"] not in seen_questions, f"manifest duplicates: {item['question']}"
        seen_questions.add(item["question"])
        scope.append((question, related))
    return scope


def lab_urls() -> set[str]:
    """Every URL cited by a hands-on lab, on the same liveness terms as a Question link.

    Question membership in this audit is staged, because a Question enters it
    only after a maintainer has curated five categorized resources.  Labs need
    no such curation, so their scope is the whole of `labs/` read from disk:
    there is no list to forget to update, and a new lab is audited the moment it
    is committed.  `tests/validate_labs.py` validates the surrounding schema.
    """
    urls: set[str] = set()
    for lab in sorted(LABS.glob("*/*.md")):
        urls.update(url.rstrip(".,;:") for url in LAB_LINK_PATTERN.findall(lab.read_text(encoding="utf-8")))
    return urls


def validate_scope(manifest: dict) -> set[str]:
    urls: set[str] = set(lab_urls())
    for question, related in audit_scope(manifest):
        question_links = resource_links(question.read_text(encoding="utf-8"), str(question.relative_to(ROOT)))
        related_links = resource_links(related.read_text(encoding="utf-8"), str(related.relative_to(ROOT)))
        urls.update(url for _, url in question_links)
        urls.update(url for _, url in related_links)
    return urls


def coverage_report(manifest: dict) -> str:
    """Return a truthful count of curated Questions, grouped by canonical Theme."""
    all_questions = sorted((ROOT / "questions").glob("*/*.md"))
    audited = {ROOT / item["question"] for item in manifest["audited_questions"]}
    assert audited <= set(all_questions), "link-audit manifest contains a non-active Question"
    by_theme = Counter(path.parent.name for path in audited)
    total_by_theme = Counter(path.parent.name for path in all_questions)
    theme_counts = ", ".join(
        f"{theme} {by_theme[theme]}/{total_by_theme[theme]}"
        for theme in sorted(total_by_theme)
        if by_theme[theme]
    ) or "none"
    percent = (len(audited) / len(all_questions) * 100) if all_questions else 0
    return (
        f"Learning-resource audit coverage: {len(audited)}/{len(all_questions)} Questions "
        f"({percent:.1f}%). Audited Themes: {theme_counts}."
    )


def fetch_result(url: str, timeout: float, user_agent: str = USER_AGENT) -> FetchResult:
    """Use HEAD first, then GET for hosts which do not implement HEAD correctly."""
    headers = {"User-Agent": user_agent}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return FetchResult(response.status, response.headers)
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in {403, 405, 406, 501}:
                continue
            return FetchResult(error.code, error.headers or {})
    return FetchResult(599, {})


def fetch_status(url: str, timeout: float) -> int:
    """Compatibility wrapper for callers that only need the HTTP status."""
    return fetch_result(url, timeout).status


def is_transient_status(status: int) -> bool:
    return status in TRANSIENT_STATUSES or 500 <= status < 600


def unverifiable_hosts() -> set[str]:
    """Hosts that cannot be liveness-checked from CI, with recorded evidence.

    `csrc.nist.gov` answers GitHub-hosted runners with `404` for documents that
    exist, and the failing set changes run to run. Retrying harder does not fix
    that, and replacing fifteen NIST Special Publication citations with weaker
    sources would degrade the database to suit a checker limitation.

    So a permanent status from a listed host is reported as unverifiable instead
    of broken. The entry carries evidence and a manual verification date that
    `tests/test_unverifiable_hosts.py` requires to stay current, and every
    occurrence is printed on each run, so this cannot quietly hide link rot.
    """
    data = json.loads(UNVERIFIABLE_HOSTS.read_text(encoding="utf-8"))
    return {entry["host"] for entry in data["hosts"]}


def github_blob_raw_url(url: str) -> str | None:
    """The raw.githubusercontent.com equivalent of a github.com blob URL.

    Returns None for anything that is not a `github.com/<org>/<repo>/blob/
    <ref>/<path>` URL, so callers can gate the raw recheck on it.
    """
    match = GITHUB_BLOB_URL_PATTERN.match(url)
    if match is None:
        return None
    org, repo, ref, path = match.groups()
    return f"https://raw.githubusercontent.com/{org}/{repo}/{ref}/{path}"


def recheck_against_raw(raw_url: str, timeout: float, *, pacer: HostPacer) -> tuple[str, str]:
    """Re-verify a github.com 404 once against raw.githubusercontent.com.

    GitHub secondary rate limiting answers anonymous requests on github.com
    with `404`, indistinguishable from a removed file, while
    raw.githubusercontent.com is a separate rate-limit pool and returns `404`
    only for content that is genuinely absent (including a missing ref).

    Returns `("reachable", detail)`, `("missing", detail)`, or
    `("inconclusive", detail)` for any other outcome — rate-limiting, server
    errors, transport failures — which must never be read as a dead link.
    Never raises.
    """
    try:
        pacer.pace(raw_url)
        result = fetch_result(raw_url, timeout)
    except (OSError, urllib.error.URLError) as error:
        return ("inconclusive", str(error))
    if 200 <= result.status < 400:
        return ("reachable", f"HTTP {result.status}")
    if result.status == 404:
        return ("missing", "HTTP 404")
    return ("inconclusive", f"HTTP {result.status}")


def confirm_permanent_failure(url: str, timeout: float, *, sleeper=time.sleep) -> FetchResult | None:
    """Re-check an apparently permanent failure with a browser User-Agent.

    Some hosts answer an unrecognised agent with `404` rather than `403`, and do
    it only once they have seen a few requests — `csrc.nist.gov` failed a
    different pair of URLs on each CI run while the other thirteen NIST
    citations passed, and every one of them served `200` to a browser agent.
    A status alone therefore cannot distinguish a withdrawn document from a
    bot-blocked one.

    So a permanent status is confirmed with further, differently shaped requests
    before the link is declared dead, spaced out because the blocking is
    rate-driven. A genuinely removed page answers `404` to any agent however long
    you wait, so this does not weaken the gate: returns the failing result when
    the failure is real, and `None` when the resource is actually reachable.
    """
    result = None
    for delay in CONFIRMATION_DELAYS_SECONDS:
        sleeper(delay)
        result = fetch_result(url, timeout, user_agent=BROWSER_USER_AGENT)
        if 200 <= result.status < 400:
            return None
    return result


def is_retryable_transport_error(error: BaseException) -> bool:
    """Retry only temporary transport errors, never DNS or certificate failures."""
    cause = error.reason if isinstance(error, urllib.error.URLError) else error
    if isinstance(cause, ssl.SSLCertVerificationError | socket.gaierror):
        return False
    if isinstance(cause, ssl.SSLError):
        # A truncated handshake (UNEXPECTED_EOF_WHILE_READING) is a dropped
        # connection, which is how a throttling host sheds load. Only a
        # certificate failure is a permanent verdict about the resource.
        return True
    if isinstance(cause, (TimeoutError, ConnectionResetError, ConnectionAbortedError)):
        return True
    return isinstance(cause, OSError) and cause.errno in {
        errno.ETIMEDOUT,
        errno.ECONNRESET,
        errno.ECONNABORTED,
    }


def is_unroutable_network_error(error: BaseException) -> bool:
    """True when the checking host could not route to the target at all.

    A runner without IPv6 connectivity reports ENETUNREACH for a dual-stack host
    that is perfectly healthy over IPv4 — gnu.org is the recurring example. That
    is a fact about the checker's network, not evidence that the resource is
    gone, so it must not be reported as a broken link. A host that has actually
    disappeared fails DNS resolution (socket.gaierror) instead, and that stays a
    hard failure.
    """
    cause = error.reason if isinstance(error, urllib.error.URLError) else error
    if isinstance(cause, socket.gaierror):
        return False
    return isinstance(cause, OSError) and cause.errno in {
        errno.ENETUNREACH,
        errno.EHOSTUNREACH,
        errno.ENETDOWN,
    }


def retry_delay(headers: object, retry_index: int, now=time.time) -> float:
    """Respect Retry-After where possible, then use bounded exponential backoff."""
    retry_after = headers.get("Retry-After") if hasattr(headers, "get") else None
    if retry_after:
        try:
            return min(float(retry_after), MAX_RETRY_AFTER_SECONDS)
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(retry_after).timestamp()
                return min(max(0.0, retry_at - now()), MAX_RETRY_AFTER_SECONDS)
            except (TypeError, ValueError, OverflowError):
                pass
    return DEFAULT_RETRY_DELAY_SECONDS * (2**retry_index)


def check_url(
    url: str,
    timeout: float,
    *,
    sleeper=time.sleep,
    pacer: HostPacer | None = None,
) -> LinkCheck:
    """Classify a link after bounded, host-paced checks.

    Exhausted rate-limit responses are reported separately because they do not
    establish that the resource is dead. Permanent HTTP and transport failures
    remain hard failures for the live audit.
    """
    pacer = pacer or HostPacer(HOST_REQUEST_INTERVAL_SECONDS, sleeper=sleeper)
    for attempt in range(MAX_ATTEMPTS):
        try:
            pacer.pace(url)
            result = fetch_result(url, timeout)
        except (OSError, urllib.error.URLError) as error:
            if is_retryable_transport_error(error) or is_unroutable_network_error(error):
                if attempt < MAX_ATTEMPTS - 1:
                    sleeper(DEFAULT_RETRY_DELAY_SECONDS * (2**attempt))
                    continue
                category = "network unreachable" if is_unroutable_network_error(error) else "temporarily unavailable"
                return LinkCheck(url, category, str(error), MAX_ATTEMPTS)
            return LinkCheck(url, "network error", str(error), attempt + 1)
        if 200 <= result.status < 400:
            return LinkCheck(url, "ok", f"HTTP {result.status}", attempt + 1)
        if not is_transient_status(result.status):
            raw_url = github_blob_raw_url(url) if result.status == 404 else None
            if raw_url is not None:
                verdict, detail = recheck_against_raw(raw_url, timeout, pacer=pacer)
                if verdict == "reachable":
                    return LinkCheck(url, "ok", f"HTTP 404 on github.com, {detail} on raw.githubusercontent.com", attempt + 1)
                if verdict == "missing":
                    return LinkCheck(url, "broken", "HTTP 404 on github.com and raw.githubusercontent.com", attempt + 1)
                return LinkCheck(url, "indeterminate", f"HTTP 404 on github.com; raw recheck {detail}", attempt + 1)
            confirmed = confirm_permanent_failure(url, timeout, sleeper=sleeper)
            if confirmed is None:
                return LinkCheck(url, "ok", f"HTTP {result.status} for the audit agent, 2xx for a browser agent", attempt + 1)
            if urlparse(url).netloc in unverifiable_hosts():
                return LinkCheck(url, "unverifiable host", f"HTTP {result.status}", attempt + 1)
            return LinkCheck(url, "broken", f"HTTP {result.status}", attempt + 1)
        if attempt < MAX_ATTEMPTS - 1:
            sleeper(retry_delay(result.headers, attempt))
    return LinkCheck(url, "rate limited", f"HTTP {result.status}", MAX_ATTEMPTS)


def host_queues(urls: set[str]) -> list[list[str]]:
    """Group every URL by host, busiest host first.

    Scheduling by host is what keeps the pool busy. A worker holds one host's
    queue for as long as it takes, so the only interval it ever waits out is the
    one its own next request owes — never another host's. The busiest queue is
    started first because the run cannot finish before that queue does, which is
    the classic longest-processing-time-first ordering.

    Grouping only reorders the work: every URL appears in exactly one queue, so
    the audited set is unchanged.
    """
    grouped: dict[str, list[str]] = {}
    for url in sorted(urls):
        grouped.setdefault(urlparse(url).netloc, []).append(url)
    return sorted(grouped.values(), key=len, reverse=True)


def check_host_queue(
    urls: list[str],
    timeout: float,
    *,
    sleeper=time.sleep,
    pacer: HostPacer | None = None,
) -> list[LinkCheck]:
    """Check one host's URLs in sequence, which is the pace the host is owed."""
    return [check_url(url, timeout, sleeper=sleeper, pacer=pacer) for url in urls]


def validate_live(
    urls: set[str],
    timeout: float,
    *,
    sleeper=time.sleep,
    pacer: HostPacer | None = None,
    workers: int = LIVE_CHECK_HOST_WORKERS,
) -> None:
    shared_pacer = pacer or HostPacer(HOST_REQUEST_INTERVAL_SECONDS, sleeper=sleeper)
    queues = host_queues(urls)
    if not queues:
        return
    with ThreadPoolExecutor(max_workers=min(workers, len(queues))) as executor:
        results = executor.map(
            lambda queue: check_host_queue(queue, timeout, sleeper=sleeper, pacer=shared_pacer),
            queues,
        )
        checks = sorted((check for queue in results for check in queue), key=lambda check: check.url)

    transient = [
        check
        for check in checks
        if check.category in {"rate limited", "temporarily unavailable", "network unreachable", "unverifiable host", "indeterminate"}
    ]
    failures = [check for check in checks if check.category in {"broken", "network error"}]
    if transient:
        print("Liveness-indeterminate learning-resource URLs (retried, not declared broken):")
        for check in transient:
            print(f"{check.url}: {check.category} after {check.attempts} attempts ({check.detail})")
    assert not failures, "Broken learning-resource links:\n" + "\n".join(
        f"{check.url}: {check.category} ({check.detail})" for check in failures
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-live", action="store_true", help="perform HTTP checks after schema validation")
    parser.add_argument("--report", action="store_true", help="print staged-audit coverage without HTTP requests")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    urls = validate_scope(load_manifest())
    if args.check_live:
        validate_live(urls, args.timeout)
    print(
        f"Validated {len(urls)} unique curated learning-resource URLs, "
        f"including {len(lab_urls())} cited by labs."
    )
    if args.report or args.check_live:
        print(coverage_report(load_manifest()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
