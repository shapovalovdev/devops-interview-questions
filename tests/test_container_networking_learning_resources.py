"""First audited Container Networking slice for issue #66."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from validate_learning_resources import resource_links  # noqa: E402

QUESTIONS = [
    ROOT / "questions/container-networking" / name
    for name in (
        "multus-multi-interface-pod-troubleshooting.md",
        "cilium-bgp-external-routing.md",
        "cilium-clustermesh-prerequisites.md",
        "cilium-ebpf-datapath-tradeoffs.md",
        "cilium-egress-gateway-design.md",
        "cilium-kube-proxy-replacement.md",
        "bridge-traffic-path.md",
        "compose-network-contract.md",
        "container-dns-resolution.md",
    )
]
RELATED = ROOT / "docs/related-materials/container-networking.md"


def test_container_networking_batch_and_theme_materials_are_audited() -> None:
    for question in QUESTIONS:
        assert len(resource_links(question.read_text(), str(question))) == 5
    assert len(resource_links(RELATED.read_text(), str(RELATED))) == 5
    manifest = json.loads((ROOT / "docs/research/link-audit-manifest.json").read_text())
    entries = {item["question"]: item["related_materials"] for item in manifest["audited_questions"]}
    for question in QUESTIONS:
        assert entries[str(question.relative_to(ROOT))] == "docs/related-materials/container-networking.md"
