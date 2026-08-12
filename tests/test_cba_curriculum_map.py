"""Guard the public CBA curriculum map without reproducing exam material.

CBA is unusually product-specific: three separate official sources publish the
same four domains and weights, and this map is only defensible while it quotes
them accurately.  So the test pins the sources, the review date, every domain
name and weight, the no-exam-material statement, and the per-domain gap
decision, then checks that every Question the map links actually exists and is
source-verified.
"""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "cba.md"
QUESTION_PATHS = [
    # Backstage Development Workflow (24%)
    ROOT / "questions/ci-cd/backstage-app-build-and-image.md",
    ROOT / "questions/version-control/monorepo-decision.md",
    ROOT / "questions/ci-cd/cache-dependencies-safely.md",
    ROOT / "questions/security/dependency-vulnerability-management.md",
    ROOT / "questions/containers/multi-stage-runtime-image.md",
    ROOT / "questions/containers/build-cache-ordering.md",
    ROOT / "questions/containers/dockerfile-build-context.md",
    # Backstage Infrastructure (22%)
    ROOT / "questions/backend-architecture/backstage-production-configuration.md",
    ROOT / "questions/backend-architecture/stateless-service-design.md",
    ROOT / "questions/backend-architecture/authentication-authorization-boundary.md",
    ROOT / "questions/kubernetes/configmap-delivery.md",
    ROOT / "questions/kubernetes/secrets-access-and-rotation.md",
    ROOT / "questions/kubernetes/deployment-rollout-and-rollback.md",
    ROOT / "questions/sre/run-production-readiness-review.md",
    # Backstage Catalog (22%)
    ROOT / "questions/backend-architecture/backstage-catalog-ingestion-triage.md",
    ROOT / "questions/backend-architecture/developer-portal-catalog-contract.md",
    ROOT / "questions/sre/establish-service-ownership.md",
    ROOT / "questions/kubernetes/labels-selectors-and-annotations.md",
    ROOT / "questions/backend-architecture/data-governance-architecture.md",
    # Customizing Backstage (32%)
    ROOT / "questions/backend-architecture/backstage-plugin-boundaries.md",
    ROOT / "questions/backend-architecture/backstage-ui-customization-upgrades.md",
    ROOT / "questions/backend-architecture/evolutionary-architecture-governance.md",
    ROOT / "questions/backend-architecture/api-versioning-policy.md",
]
GAP_QUESTIONS = [
    ROOT / "questions/ci-cd/backstage-app-build-and-image.md",
    ROOT / "questions/backend-architecture/backstage-production-configuration.md",
    ROOT / "questions/backend-architecture/backstage-catalog-ingestion-triage.md",
    ROOT / "questions/backend-architecture/backstage-plugin-boundaries.md",
    ROOT / "questions/backend-architecture/backstage-ui-customization-upgrades.md",
]


def test_cba_map_quotes_the_three_official_sources_and_their_review_date() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/certification/certified-backstage-associate-cba/",
        "https://www.cncf.io/training/certification/cba/",
        "https://github.com/cncf/curriculum/blob/master/CBA_Curriculum.pdf",
        "reviewed on 2026-08-12",
        "not** a reproduction of exam questions",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"CBA curriculum map is missing: {', '.join(missing)}"


def test_cba_map_publishes_every_official_domain_and_weight() -> None:
    text = MAP.read_text(encoding="utf-8")
    domains = {
        "Backstage Development Workflow: build and run Backstage projects locally": "| 24% |",
        "Backstage Infrastructure: understand the Backstage framework": "| 22% |",
        "Backstage Catalog: understand how/why to use Backstage Catalog": "| 22% |",
        "Customizing Backstage: understand frontend versus backend plugins": "| 32% |",
    }
    for domain, weight in domains.items():
        assert domain in text, f"CBA map does not state the official domain: {domain}"
        assert weight in text, f"CBA map does not state the weight {weight} for {domain}"
    assert text.count("| 22% |") == 2, "two CBA domains are weighted 22%"


def test_cba_map_states_an_explicit_gap_decision_for_every_domain() -> None:
    """A map that quietly tags existing Questions is the failure mode here."""
    gap = MAP.read_text(encoding="utf-8").split("## Gap decision", 1)
    assert len(gap) == 2, "CBA map requires an explicit gap decision section"
    decision = gap[1].split("## ", 1)[0]
    for domain in (
        "Backstage Development Workflow",
        "Backstage Infrastructure",
        "Backstage Catalog",
        "Customizing Backstage",
    ):
        assert domain in decision, f"gap decision does not cover the {domain} domain"
    assert "No further Question is added." in decision, "the map must close the gap decision"
    for path in GAP_QUESTIONS:
        assert path.name in decision, f"{path.name}: a new gap Question must be justified in the decision"


def test_cba_mapped_questions_are_source_verified_and_tagged() -> None:
    """Each mapped canonical Question must actually carry the certification."""
    map_text = MAP.read_text(encoding="utf-8")
    assert len(QUESTION_PATHS) == len(set(QUESTION_PATHS)) == 23
    for path in QUESTION_PATHS:
        assert path.is_file(), f"missing CBA-mapped Question: {path}"
        text = path.read_text(encoding="utf-8")
        assert "sources:" in text, f"{path}: missing structured source metadata"
        assert "source_type:" in text, f"{path}: missing source type"
        assert "verified_on:" in text, f"{path}: missing verification date"
        assert "## Answer guide" in text and "## References" in text
        assert re.search(r"^- Further reading \((?:blog|personal blog)\): ", text, re.MULTILINE), (
            f"{path}: missing complementary blog"
        )
        assert "cba" in text.split("---", 2)[1], f"{path}: must carry the cba tag"
        assert path.name in map_text, f"{path}: must be linked by the CBA map"


def main() -> None:
    test_cba_map_quotes_the_three_official_sources_and_their_review_date()
    test_cba_map_publishes_every_official_domain_and_weight()
    test_cba_map_states_an_explicit_gap_decision_for_every_domain()
    test_cba_mapped_questions_are_source_verified_and_tagged()
    print(f"Validated the public CBA curriculum map over {len(QUESTION_PATHS)} mapped Questions.")


if __name__ == "__main__":
    main()
