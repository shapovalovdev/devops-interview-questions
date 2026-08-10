import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_shell_scripting_is_fully_audited() -> None:
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text())
    audited = {item["question"] for item in manifest["audited_questions"]}
    questions = sorted((ROOT / "questions/shell-scripting").glob("*.md"))
    assert len(questions) == 25
    assert {str(path.relative_to(ROOT)) for path in questions} <= audited
