"""Guard the public CNPE map and its no-duplicate coverage decision."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "cnpe.md"


def main() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/certification/certified-cloud-native-platform-engineer-cnpe/",
        "https://github.com/cncf/curriculum/blob/master/CNPE_Curriculum.pdf",
        "reviewed on 2026-08-06",
        "performance-based certification",
        "not** a\nreproduction of exam questions",
        "Platform Architecture and Infrastructure (15%)",
        "GitOps and Continuous Delivery (25%)",
        "Platform APIs and Self-Service\nCapabilities (25%)",
        "Observability and Operations (20%)",
        "Security and\nPolicy Enforcement (15%)",
        "No original Question is added",
        "one-canonical-Question policy",
        "`cnpe`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"CNPE curriculum map is missing: {', '.join(missing)}"
    print("Validated public CNPE curriculum map and no-duplicate gap policy.")


def test_cnpe_map_links_existing_source_verified_canonical_questions() -> None:
    question_paths = [
        "questions/containers/container-platform-cost-model.md",
        "questions/kubernetes/multi-tenant-platform-boundaries.md",
        "questions/storage/build-self-service-storage-platform.md",
        "questions/ci-cd/argo-cd-reconciliation-drift.md",
        "questions/ci-cd/multi-team-pipeline-architecture.md",
        "questions/ci-cd/argo-rollouts-progressive-delivery.md",
        "questions/kubernetes/crd-operator-lifecycle.md",
        "questions/observability/establish-observability-platform.md",
        "questions/observability/govern-telemetry-cost.md",
        "questions/sre/triage-production-incident.md",
        "questions/service-mesh/service-mesh-platform-guardrails.md",
        "questions/kubernetes/rbac-least-privilege.md",
        "questions/kubernetes/audit-policy-runtime-detection.md",
        "questions/kubernetes/admission-policy-and-guardrails.md",
        "questions/security/container-image-provenance.md",
    ]
    map_text = MAP.read_text(encoding="utf-8")
    for relative in question_paths:
        path = ROOT / relative
        assert path.is_file(), f"CNPE map references a missing Question: {relative}"
        text = path.read_text(encoding="utf-8")
        assert "sources:" in text and "## References" in text, f"{relative}: source verification is required"
        assert "Further reading (blog):" in text, f"{relative}: complementary blog reading is required"
        assert path.name in map_text, f"{relative}: must be represented in the CNPE map"


if __name__ == "__main__":
    main()
