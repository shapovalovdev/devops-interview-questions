"""First audited Container Networking slice for issue #66."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from validate_learning_resources import resource_links  # noqa: E402

QUESTION = ROOT / "questions/container-networking/multus-multi-interface-pod-troubleshooting.md"
RELATED = ROOT / "docs/related-materials/container-networking.md"


def test_multus_question_and_theme_materials_are_audited() -> None:
    assert len(resource_links(QUESTION.read_text(), str(QUESTION))) == 5
    assert len(resource_links(RELATED.read_text(), str(RELATED))) == 5
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text())
    entries = {item["question"]: item["related_materials"] for item in manifest["audited_questions"]}
    assert entries["questions/container-networking/multus-multi-interface-pod-troubleshooting.md"] == "docs/related-materials/container-networking.md"
