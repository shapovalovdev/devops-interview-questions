"""Quality guardrails for the controlled must-know collection."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from validate_learning_resources import resource_links  # noqa: E402


def test_must_know_questions_are_audited_and_cross_theme() -> None:
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text())
    audited = {item["question"] for item in manifest["audited_questions"]}
    selected = []
    for path in (ROOT / "questions").glob("*/*.md"):
        if "must-know" in path.read_text().split("---", 2)[1]:
            selected.append(path)
    assert len(selected) >= 10
    assert len({path.parent.name for path in selected}) >= 8
    assert all(str(path.relative_to(ROOT)) in audited for path in selected)
    for path in selected:
        assert len(resource_links(path.read_text(), str(path))) == 5
