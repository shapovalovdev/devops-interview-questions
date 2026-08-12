"""Guard the public CGOA curriculum map without reproducing exam material."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "cgoa.md"
MANIFEST = ROOT / "config" / "content-manifest.json"

# The five domains published on the Linux Foundation CGOA program page, with the
# weights reviewed on 2026-08-12. A change here must be driven by the official
# page, never by what the database happens to cover.
OFFICIAL_DOMAINS = {
    "GitOps Principles: declarative": "30%",
    "GitOps Patterns: deployment and release patterns": "20%",
    "GitOps Terminology: continuous": "20%",
    "Related Practices: Configuration as Code": "16%",
    "Tooling: manifest format and packaging": "14%",
}

QUESTION_PATHS = [
    # GitOps Principles (30%)
    ROOT / "questions/ci-cd/gitops-principles.md",
    ROOT / "questions/ci-cd/argo-cd-application-sync.md",
    ROOT / "questions/ci-cd/argo-cd-reconciliation-drift.md",
    ROOT / "questions/ci-cd/immutable-release-artifacts.md",
    ROOT / "questions/version-control/git-object-model.md",
    ROOT / "questions/version-control/release-tags.md",
    ROOT / "questions/kubernetes/crd-operator-lifecycle.md",
    # GitOps Patterns (20%)
    ROOT / "questions/ci-cd/gitops-pull-versus-push-delivery.md",
    ROOT / "questions/ci-cd/argo-rollouts-progressive-delivery.md",
    ROOT / "questions/ci-cd/argo-rollouts-analysis.md",
    ROOT / "questions/ci-cd/canary-deployment-decision.md",
    ROOT / "questions/ci-cd/blue-green-cutover.md",
    ROOT / "questions/ci-cd/argo-events-architecture.md",
    ROOT / "questions/ci-cd/argo-cd-application-project-boundaries.md",
    # GitOps Terminology (20%)
    ROOT / "questions/version-control/gitops-state-store-layout.md",
    ROOT / "questions/ci-cd/roll-back-a-deployment.md",
    ROOT / "questions/infrastructure-as-code/infrastructure-drift.md",
    ROOT / "questions/configuration-management/configuration-drift-remediation.md",
    ROOT / "questions/infrastructure-as-code/terraform-state-purpose.md",
    ROOT / "questions/troubleshooting/handle-bad-deployment.md",
    # Related Practices (16%)
    ROOT / "questions/security/gitops-secret-delivery.md",
    ROOT / "questions/ci-cd/ci-versus-cd.md",
    ROOT / "questions/infrastructure-as-code/iac-drift-governance.md",
    ROOT / "questions/infrastructure-as-code/policy-as-code-gates.md",
    ROOT / "questions/configuration-management/ansible-idempotence.md",
    ROOT / "questions/ci-cd/supply-chain-provenance.md",
    ROOT / "questions/ci-cd/pipeline-quality-gates.md",
    # Tooling (14%)
    ROOT / "questions/ci-cd/flux-reconciliation-engine.md",
    ROOT / "questions/ci-cd/gitops-feedback-loop.md",
    ROOT / "questions/ci-cd/argo-cd-helm-kustomize-rendering.md",
    ROOT / "questions/kubernetes/helm-kustomize-component-installation.md",
    ROOT / "questions/ci-cd/argo-events-sensor-dependencies.md",
]

# The six original Questions written because a published competency had no
# canonical coverage. Each must be named by the map's gap decision.
GAP_QUESTIONS = [
    "questions/ci-cd/gitops-principles.md",
    "questions/ci-cd/gitops-pull-versus-push-delivery.md",
    "questions/version-control/gitops-state-store-layout.md",
    "questions/security/gitops-secret-delivery.md",
    "questions/ci-cd/flux-reconciliation-engine.md",
    "questions/ci-cd/gitops-feedback-loop.md",
]


def main() -> None:
    """The map must cite both official sources and every published domain weight."""
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/certification/certified-gitops-associate-cgoa/",
        "https://github.com/cncf/curriculum/tree/master/cgoa",
        "reviewed on 2026-08-12",
        "not** a\nreproduction of exam questions",
        "## Gap decision",
        "`cgoa`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"CGOA curriculum map is missing: {', '.join(missing)}"

    for domain, weight in OFFICIAL_DOMAINS.items():
        assert domain in text, f"CGOA map does not carry the official domain '{domain}'"
        row = next(line for line in text.splitlines() if domain in line)
        assert f"| {weight} |" in row, f"CGOA domain '{domain}' must be weighted {weight}"
    print("Validated the public CGOA curriculum map and its five official domain weights.")


def test_cgoa_gap_decision_is_explicit() -> None:
    """The map must justify each added Question, not just list links."""
    text = MAP.read_text(encoding="utf-8")
    decision = text.split("## Gap decision", 1)[1].split("## Focused verification plan", 1)[0]
    assert "original canonical Questions are added" in decision, "gap decision must state how many Questions were added"
    for question in GAP_QUESTIONS:
        assert question.rsplit("/", 1)[-1] in decision, f"{question}: gap decision must name the added Question"
    assert "No other published competency needed a new Question." in decision, (
        "gap decision must state explicitly that the remaining domains need no new Question"
    )
    # Every mapped Question that is not a declared gap Question must be reused
    # existing material, so the count of new files stays honest.
    assert len(GAP_QUESTIONS) < len(QUESTION_PATHS), "the map must reuse canonical Questions, not only add new ones"


def test_cgoa_mapped_questions_exist_and_are_source_verified() -> None:
    """Each mapped canonical Question must carry the tag and the house standard."""
    map_text = MAP.read_text(encoding="utf-8")
    assert len(QUESTION_PATHS) == len(set(QUESTION_PATHS)), "the CGOA map must not list a Question twice"
    for path in QUESTION_PATHS:
        assert path.is_file(), f"missing CGOA-mapped Question: {path}"
        text = path.read_text(encoding="utf-8")
        tags = re.search(r"^tags: \[([^\]]*)\]$", text, re.MULTILINE)
        assert tags, f"{path}: missing tags"
        assert "cgoa" in {tag.strip() for tag in tags.group(1).split(",")}, f"{path}: must carry the cgoa tag"
        assert "sources:" in text, f"{path}: missing structured source metadata"
        assert "source_type:" in text, f"{path}: missing source type"
        assert "verified_on:" in text, f"{path}: missing verification date"
        assert "## Answer guide" in text and "## References" in text, f"{path}: missing answer guide or references"
        assert re.search(r"^- Further reading \((?:blog|personal blog)\): ", text, re.MULTILINE), (
            f"{path}: missing complementary blog"
        )
        assert path.name in map_text, f"{path}: must be linked by the CGOA map"


def test_cgoa_is_registered_in_the_content_manifest() -> None:
    """The manifest minimum must match what the map actually maps."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    certifications = {item["tag"]: item for item in manifest["certifications"]}
    assert "cgoa" in certifications, "cgoa must be registered in the content manifest"
    entry = certifications["cgoa"]
    assert entry["map"] == "docs/certifications/cgoa.md", "cgoa must point at its curriculum map"
    assert entry["minimum_questions"] == len(QUESTION_PATHS), (
        f"cgoa minimum_questions must equal the {len(QUESTION_PATHS)} mapped Questions, "
        f"got {entry['minimum_questions']}"
    )
    tags = [item["tag"] for item in manifest["certifications"]]
    assert tags == sorted(tags), "the certification list must stay sorted by tag"


if __name__ == "__main__":
    main()
    test_cgoa_gap_decision_is_explicit()
    test_cgoa_mapped_questions_exist_and_are_source_verified()
    test_cgoa_is_registered_in_the_content_manifest()
