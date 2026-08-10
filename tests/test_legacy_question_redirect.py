"""Regression tests for legacy Markdown URL compatibility on GitHub Pages."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "assets" / "legacy-question-redirect.js"


def redirect_target(pathname: str, search: str = "", hash_fragment: str = "") -> str | None:
    """Run the browser redirect function in a minimal, deterministic JS context."""
    input_value = json.dumps(
        {
            "pathname": pathname,
            "search": search,
            "hash": hash_fragment,
        }
    )
    node_program = f"""
const fs = require('fs');
const vm = require('vm');
const input = {input_value};
const context = {{
  window: {{}},
  document: {{ currentScript: {{ dataset: {{ basePath: '/devops-interview-questions' }} }} }},
}};
vm.runInNewContext(fs.readFileSync({json.dumps(str(SCRIPT))}, 'utf8'), context);
const result = context.window.LegacyQuestionRedirect.questionHtmlTarget(
  input.pathname, input.search, input.hash, '/devops-interview-questions',
);
process.stdout.write(JSON.stringify(result));
"""
    completed = subprocess.run(
        ["node", "-e", node_program],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_legacy_question_markdown_redirects_to_html_with_url_state() -> None:
    assert redirect_target(
        "/devops-interview-questions/questions/linux/linux-boot-sequence.md",
        "?difficulty=middle",
        "#answer-guide",
    ) == (
        "/devops-interview-questions/questions/linux/linux-boot-sequence.html"
        "?difficulty=middle#answer-guide"
    )


def test_non_question_and_malformed_paths_remain_not_found() -> None:
    for pathname in (
        "/devops-interview-questions/questions.md",
        "/devops-interview-questions/docs/guide.md",
        "/devops-interview-questions/questions/linux/",
        "/devops-interview-questions/questions/linux/../private.md",
        "/devops-interview-questions/not-found",
    ):
        assert redirect_target(pathname) is None


def test_404_script_only_navigates_legacy_question_urls() -> None:
    node_program = f"""
const fs = require('fs');
const vm = require('vm');
function run(pathname) {{
  let replacement = null;
  const context = {{
    window: {{ location: {{ pathname, search: '?source=old', hash: '#details', replace: (url) => replacement = url }} }},
    document: {{ currentScript: {{ dataset: {{ basePath: '/devops-interview-questions' }} }} }},
  }};
  vm.runInNewContext(fs.readFileSync({json.dumps(str(SCRIPT))}, 'utf8'), context);
  return replacement;
}}
process.stdout.write(JSON.stringify([
  run('/devops-interview-questions/questions/linux/linux-boot-sequence.md'),
  run('/devops-interview-questions/missing-page'),
]));
"""
    completed = subprocess.run(
        ["node", "-e", node_program],
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(completed.stdout) == [
        "/devops-interview-questions/questions/linux/linux-boot-sequence.html?source=old#details",
        None,
    ]


def test_custom_404_has_accessible_fallback_and_project_scoped_script() -> None:
    page = (ROOT / "404.html").read_text(encoding="utf-8")
    assert "<h1>Page not found</h1>" in page
    assert 'href="/devops-interview-questions/"' in page
    assert 'data-base-path="/devops-interview-questions"' in page
    assert 'src="/devops-interview-questions/assets/legacy-question-redirect.js"' in page
