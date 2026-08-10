"""Public behavior checks for the static interview-session simulator."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "assets" / "interview-session.js"


def run_session_script(program: str) -> str:
    completed = subprocess.run(["node", "-e", program], check=True, capture_output=True, text=True)
    return completed.stdout


def test_session_selection_is_unique_restricted_and_exact() -> None:
    questions = [
        {"title": f"Linux {index}", "theme": "linux", "path": f"linux-{index}.html"}
        for index in range(8)
    ] + [
        {"title": f"Kubernetes {index}", "theme": "kubernetes", "path": f"kubernetes-{index}.html"}
        for index in range(8)
    ]
    program = f"""
const fs = require('fs'); const vm = require('vm');
const context = {{ window: {{}}, document: undefined, URLSearchParams }};
vm.runInNewContext(fs.readFileSync({json.dumps(str(SCRIPT))}, 'utf8'), context);
const questions = {json.dumps(questions)};
const session = context.window.InterviewSession.createSession(questions, ['linux', 'kubernetes'], 6, 'fixed-seed');
process.stdout.write(JSON.stringify(session));
"""
    session = json.loads(run_session_script(program))
    assert len(session) == 6
    assert len({question["path"] for question in session}) == 6
    assert {question["theme"] for question in session} == {"linux", "kubernetes"}


def test_balancing_and_url_state_are_restorable() -> None:
    program = f"""
const fs = require('fs'); const vm = require('vm');
const context = {{ window: {{}}, document: undefined, URLSearchParams }};
vm.runInNewContext(fs.readFileSync({json.dumps(str(SCRIPT))}, 'utf8'), context);
const api = context.window.InterviewSession;
const state = {{ themes: ['linux', 'kubernetes', 'logging'], total: 10, allocations: {{ linux: 3, kubernetes: 4, logging: 3 }}, seed: 'share-me', index: 4, revealed: true }};
process.stdout.write(JSON.stringify({{ allocations: api.balanceAllocations(state.themes, state.total), restored: api.readState(api.writeState(state)) }}));
"""
    result = json.loads(run_session_script(program))
    assert result["allocations"] == {"linux": 4, "kubernetes": 3, "logging": 3}
    assert result["restored"] == {
        "themes": ["linux", "kubernetes", "logging"],
        "total": 10,
        "allocations": {"linux": 3, "kubernetes": 4, "logging": 3},
        "seed": "share-me",
        "index": 4,
        "revealed": True,
    }


def test_manual_allocation_is_used_when_it_matches_the_total() -> None:
    questions = [
        {"title": f"Linux {index}", "theme": "linux", "path": f"linux-{index}.html"}
        for index in range(8)
    ] + [
        {"title": f"Logging {index}", "theme": "logging", "path": f"logging-{index}.html"}
        for index in range(8)
    ]
    program = f"""
const fs = require('fs'); const vm = require('vm');
const context = {{ window: {{}}, document: undefined, URLSearchParams }};
vm.runInNewContext(fs.readFileSync({json.dumps(str(SCRIPT))}, 'utf8'), context);
const session = context.window.InterviewSession.createSession({json.dumps(questions)}, ['linux', 'logging'], 6, 'manual', {{ linux: 3, logging: 3 }});
process.stdout.write(JSON.stringify(session.reduce((counts, question) => (counts[question.theme] = (counts[question.theme] || 0) + 1, counts), {{}})));
"""
    assert json.loads(run_session_script(program)) == {"linux": 3, "logging": 3}
