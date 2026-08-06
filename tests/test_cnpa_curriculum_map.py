"""Guard the public CNPA map and its original-gap policy."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "cnpa.md"


def main() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/certification/certified-cloud-native-platform-engineering-associate-cnpa/",
        "reviewed on 2026-08-06",
        "not** a reconstruction of examination items",
        "Platform Engineering Core Fundamentals (36%)",
        "Platform Observability, Security, and Conformance (20%)",
        "Continuous Delivery &\nPlatform Engineering (16%)",
        "Platform APIs and Provisioning Infrastructure\n(12%)",
        "IDPs and Developer Experience (8%)",
        "Measuring your Platform (8%)",
        "one canonical Theme",
        "two\noriginal canonical Questions",
        "`cnpa`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"CNPA curriculum map is missing: {', '.join(missing)}"
    print("Validated public CNPA curriculum map and original-gap policy.")


def test_cnpa_map_links_source_verified_canonical_questions() -> None:
    question_paths = [
        "questions/backend-architecture/platform-boundary-strategy.md",
        "questions/cloud/landing-zone-governance.md",
        "questions/containers/tenant-isolation-boundaries.md",
        "questions/containers/container-platform-cost-model.md",
        "questions/security/secure-platform-defaults.md",
        "questions/observability/establish-observability-platform.md",
        "questions/service-mesh/service-mesh-platform-guardrails.md",
        "questions/kubernetes/rbac-least-privilege.md",
        "questions/kubernetes/admission-policy-and-guardrails.md",
        "questions/ci-cd/supply-chain-provenance.md",
        "questions/ci-cd/argo-cd-reconciliation-drift.md",
        "questions/ci-cd/argo-cd-application-sync.md",
        "questions/ci-cd/multi-team-pipeline-architecture.md",
        "questions/sre/triage-production-incident.md",
        "questions/kubernetes/crd-operator-lifecycle.md",
        "questions/storage/build-self-service-storage-platform.md",
        "questions/configuration-management/cm-platform-guardrails.md",
        "questions/sre/establish-service-ownership.md",
        "questions/backend-architecture/developer-portal-catalog-contract.md",
        "questions/observability/govern-telemetry-cost.md",
        "questions/sre/measure-platform-impact-with-dora.md",
    ]
    map_text = MAP.read_text(encoding="utf-8")
    for relative in question_paths:
        path = ROOT / relative
        assert path.is_file(), f"CNPA map references a missing Question: {relative}"
        text = path.read_text(encoding="utf-8")
        assert "sources:" in text and "## References" in text, f"{relative}: source verification is required"
        assert "Further reading (blog):" in text, f"{relative}: complementary blog reading is required"
        assert path.name in map_text, f"{relative}: must be represented in the CNPA map"


if __name__ == "__main__":
    main()
