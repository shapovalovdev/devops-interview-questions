#!/usr/bin/env python3
"""Validate staged, curated learning resources and optionally check their URLs.

This validator deliberately does not invent links or infer their category from a
domain.  A maintainer adds a Question to the audit manifest only after reviewing
its five resources.  The same parser is used for Question learning sections and
Theme related-material pages.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/research/link-audit-manifest.json"
REQUIRED_CATEGORIES = {
    "official documentation",
    "manual or specification",
    "maintainer or personal blog",
    "technical blog",
    "hands-on guide",
}
LINK_PATTERN = re.compile(r"^- ([^:]+): \[[^]]+\]\((https://[^)\s]+)\)\s*$", re.MULTILINE)
USER_AGENT = "DevOpsQuestionDatabaseLinkAudit/1.0 (+https://github.com/shapovalovdev/devops-interview-questions)"


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


def validate_scope(manifest: dict) -> set[str]:
    urls: set[str] = set()
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


def fetch_status(url: str, timeout: float) -> int:
    """Use HEAD first, then GET for hosts which do not implement HEAD correctly."""
    headers = {"User-Agent": USER_AGENT}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in {403, 405, 406, 501}:
                continue
            return error.code
    return 599


def validate_live(urls: set[str], timeout: float) -> None:
    failures: list[str] = []
    for url in sorted(urls):
        try:
            status = fetch_status(url, timeout)
        except (OSError, urllib.error.URLError) as error:
            failures.append(f"{url}: network error: {error}")
            continue
        if not 200 <= status < 400:
            failures.append(f"{url}: HTTP {status}")
    assert not failures, "Broken learning-resource links:\n" + "\n".join(failures)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-live", action="store_true", help="perform HTTP checks after schema validation")
    parser.add_argument("--report", action="store_true", help="print staged-audit coverage without HTTP requests")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    urls = validate_scope(load_manifest())
    if args.check_live:
        validate_live(urls, args.timeout)
    print(f"Validated {len(urls)} unique curated learning-resource URLs.")
    if args.report or args.check_live:
        print(coverage_report(load_manifest()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
