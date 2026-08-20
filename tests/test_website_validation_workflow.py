"""Regression guard for the browser-validation job's bounded external work."""

from __future__ import annotations

from pathlib import Path


WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "validate-questions.yml"


def step_body(name: str, next_name: str) -> str:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    _, found, remainder = workflow.partition(f"      - name: {name}\n")
    assert found, f"workflow must retain the {name!r} step"
    body, next_step, _ = remainder.partition(f"      - name: {next_name}\n")
    assert next_step, f"workflow must retain the {next_name!r} step after {name!r}"
    return body


def test_browser_installation_has_a_bounded_actionable_failure() -> None:
    install = step_body("Install browser test dependencies", "Verify search, filters, and rendered Question links")
    assert "timeout-minutes: 10" in install
    assert "timeout --foreground 8m python -m playwright install chromium" in install
    assert "playwright install --with-deps chromium" not in install
    assert "Check the Playwright download service" in install


def test_browser_behavior_check_has_a_workflow_deadline() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    _, found, behavior = workflow.partition("      - name: Verify search, filters, and rendered Question links\n")
    assert found, "workflow must retain the browser behavior coverage"
    assert "timeout-minutes: 5" in behavior
    assert "run: python tests/site_check.py" in behavior
