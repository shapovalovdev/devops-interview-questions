# CNPE coverage map

This map aligns original practice Questions with the public [Certified Cloud
Native Platform Engineer (CNPE) curriculum](https://training.linuxfoundation.org/certification/certified-cloud-native-platform-engineer-cnpe/)
and its [open-source curriculum repository](https://github.com/cncf/curriculum/blob/master/CNPE_Curriculum.pdf).
Both sources were reviewed on 2026-08-06. CNPE is a hands-on,
performance-based certification; this document is a learning map, **not** a
reproduction of exam questions, simulations, confidential material, or a
promise of exam coverage.

CNPE names five domains: Platform Architecture and Infrastructure (15%),
GitOps and Continuous Delivery (25%), Platform APIs and Self-Service
Capabilities (25%), Observability and Operations (20%), and Security and
Policy Enforcement (15%). The canonical Questions below are original and are
reused instead of being copied into a certification-specific folder.

The future `cnpe` certification tag must be applied only by the central
integration change, together with `TAGS.md`, `config/content-manifest.json`,
and `assets/questions.js`. Every linked Question already has its own
primary-source metadata and separately-labelled complementary blog reading;
the CNPE page is the curriculum authority, not the factual authority for each
technical answer.

## Official domain mapping

| Official domain and published competencies | Weight | Canonical original practice Questions | Coverage decision |
| --- | ---: | --- | --- |
| Platform Architecture and Infrastructure: platform networking, storage, compute; right-sizing and scaling; multi-tenant resource use | 15% | [Set a container-platform cost and capacity model](../../questions/containers/container-platform-cost-model.md); [Define multi-tenant Kubernetes platform boundaries](../../questions/kubernetes/multi-tenant-platform-boundaries.md); [Build a self-service storage platform with guardrails](../../questions/storage/build-self-service-storage-platform.md) | Covered by shared platform Questions. |
| GitOps and Continuous Delivery: GitOps for application and infrastructure deployment; Kubernetes-integrated CI/CD; progressive delivery | 25% | [Respond to Argo CD drift without masking an incident](../../questions/ci-cd/argo-cd-reconciliation-drift.md); [Design a multi-team pipeline architecture](../../questions/ci-cd/multi-team-pipeline-architecture.md); [Choose a progressive Argo Rollouts strategy](../../questions/ci-cd/argo-rollouts-progressive-delivery.md) | Covered by shared delivery Questions. |
| Platform APIs and Self-Service Capabilities: CRDs; platform-API provisioning workflows; operators; automation frameworks | 25% | [Operate a custom resource and its controller safely](../../questions/kubernetes/crd-operator-lifecycle.md); [Build a self-service storage platform with guardrails](../../questions/storage/build-self-service-storage-platform.md); [Design a multi-team pipeline architecture](../../questions/ci-cd/multi-team-pipeline-architecture.md) | Covered without adding a duplicate platform-API Question: together these cover CRD/controller lifecycle, guarded self-service requests, and automated multi-team workflows. |
| Observability and Operations: monitoring, alerting, logging, tracing; efficiency metrics; incident diagnosis and remediation | 20% | [Establish an observability platform product](../../questions/observability/establish-observability-platform.md); [Govern telemetry cost across teams](../../questions/observability/govern-telemetry-cost.md); [Triage a production incident](../../questions/sre/triage-production-incident.md) | Covered by shared operations Questions. |
| Security and Policy Enforcement: service-to-service security; RBAC; audit/compliance evidence; policy/admission; pipeline security checks | 15% | [Establish safe service-mesh platform guardrails](../../questions/service-mesh/service-mesh-platform-guardrails.md); [Design least-privilege Kubernetes RBAC](../../questions/kubernetes/rbac-least-privilege.md); [Design a Kubernetes audit policy for security detection](../../questions/kubernetes/audit-policy-runtime-detection.md); [Establish Kubernetes admission policy guardrails](../../questions/kubernetes/admission-policy-and-guardrails.md); [Verify container image provenance before deployment](../../questions/security/container-image-provenance.md) | Covered by shared security Questions. |

## Gap decision and integration requirements

No original Question is added in this mapping pass. The closest apparent gap,
"self-service provisioning", is already addressed at operational depth by the
storage platform Question and the CRD/operator Question; a nearly identical
CNPE-only prompt would violate the repository's one-canonical-Question policy.

Before CNPE becomes a published study filter, the coordinator must:

1. Add `cnpe` to the certification vocabulary and content manifest, with this
   map and a minimum reflecting the mapped Questions above.
2. Apply `cnpe` only to the linked canonical Question files after checking that
   their answer guides and source records still support the CNPE competency.
3. Regenerate/update the matching catalog records and run full content, site,
   and GitHub Actions validation.

Do not interpret the tag or this map as an endorsement, leaked material, or
prediction of an individual CNPE examination.
