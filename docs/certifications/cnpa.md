# CNPA coverage map

This map aligns original practice Questions with the public [Certified Cloud
Native Platform Engineering Associate (CNPA) domains and competencies](https://training.linuxfoundation.org/certification/certified-cloud-native-platform-engineering-associate-cnpa/)
published by Linux Foundation Education. The page was reviewed on 2026-08-06.
It is a study map, **not** a reconstruction of examination items, confidential
material, a prediction of scored content, or a guarantee of a result. CNPA is
a beginner-level, online multiple-choice certification; the Questions below are
original interview and learning prompts, not sample exam questions.

CNPA publishes six domains: Platform Engineering Core Fundamentals (36%),
Platform Observability, Security, and Conformance (20%), Continuous Delivery &
Platform Engineering (16%), Platform APIs and Provisioning Infrastructure
(12%), IDPs and Developer Experience (8%), and Measuring your Platform (8%).
Each Question remains in one canonical Theme; the future `cnpa` certification
tag will be a cross-cutting study filter, never a duplicate certification
folder. The program page is the curriculum authority; every linked Question
retains its own primary technical source and complementary blog reading.

## Official domain mapping

| Official public domain and competencies | Weight | Canonical original practice Questions | Coverage decision |
| --- | ---: | --- | --- |
| Platform Engineering Core Fundamentals: declarative resource management; DevOps practices; application environments and infrastructure; platform architecture; platform goals; CI; CD and GitOps | 36% | [Set platform and product-service boundaries](../../questions/backend-architecture/platform-boundary-strategy.md); [Establish a governed cloud landing zone](../../questions/cloud/landing-zone-governance.md); [Define tenant isolation boundaries for a container platform](../../questions/containers/tenant-isolation-boundaries.md); [Set a container-platform cost and capacity model](../../questions/containers/container-platform-cost-model.md); [Deliver secure platform defaults at scale](../../questions/security/secure-platform-defaults.md) | Covered by shared canonical platform Questions. |
| Platform Observability, Security, and Conformance: traces, metrics, logs, events; secure service communication; policy engines; Kubernetes security; CI/CD security | 20% | [Establish an observability platform product](../../questions/observability/establish-observability-platform.md); [Establish safe service-mesh platform guardrails](../../questions/service-mesh/service-mesh-platform-guardrails.md); [Design least-privilege Kubernetes RBAC](../../questions/kubernetes/rbac-least-privilege.md); [Establish Kubernetes admission policy guardrails](../../questions/kubernetes/admission-policy-and-guardrails.md); [Verify supply-chain provenance before deployment](../../questions/ci-cd/supply-chain-provenance.md) | Covered by shared observability, policy, identity, and delivery-security Questions. |
| Continuous Delivery & Platform Engineering: CI pipelines; incident response; CI/CD relationship; GitOps workflows; GitOps application environments | 16% | [Respond to Argo CD drift without masking an incident](../../questions/ci-cd/argo-cd-reconciliation-drift.md); [Synchronize an Argo CD application safely](../../questions/ci-cd/argo-cd-application-sync.md); [Design a multi-team pipeline architecture](../../questions/ci-cd/multi-team-pipeline-architecture.md); [Triage a production incident](../../questions/sre/triage-production-incident.md) | Covered by shared delivery and operational Questions. |
| Platform APIs and Provisioning Infrastructure: Kubernetes reconciliation loop; self-service APIs/CRDs; provisioning with Kubernetes; operator pattern | 12% | [Operate a custom resource and its controller safely](../../questions/kubernetes/crd-operator-lifecycle.md); [Build a self-service storage platform with guardrails](../../questions/storage/build-self-service-storage-platform.md); [Establish configuration-management platform guardrails](../../questions/configuration-management/cm-platform-guardrails.md) | Covered by shared API, controller, provisioning, and automation Questions. |
| IDPs and Developer Experience: simplified capability access; API-driven service catalogs; developer portals; AI/ML platform automation | 8% | [Establish service ownership and reliability accountability](../../questions/sre/establish-service-ownership.md); [Design a developer-portal catalog contract teams can trust](../../questions/backend-architecture/developer-portal-catalog-contract.md) | One original gap Question added for the direct portal/catalog contract objective; the service-ownership Question covers catalog accountability. AI/ML automation is covered as a platform decision rather than inventing vendor-specific certification content. |
| Measuring your Platform: platform efficiency, team productivity, DORA metrics | 8% | [Govern telemetry cost across teams](../../questions/observability/govern-telemetry-cost.md); [Set a container-platform cost and capacity model](../../questions/containers/container-platform-cost-model.md); [Measure platform impact with DORA metrics without gaming teams](../../questions/sre/measure-platform-impact-with-dora.md) | One original gap Question added for direct DORA-based platform measurement; existing Questions cover efficiency/cost trade-offs. |

## Completed original gap Questions

The IDP catalog and DORA measurement objectives needed direct treatment that
would not be supplied by tagging a broad platform-design prompt. These two
original canonical Questions are source-verified individually, are not copied
from certification material, and carry separately labelled complementary blog
reading:

1. [**Design a developer-portal catalog contract teams can trust.**](../../questions/backend-architecture/developer-portal-catalog-contract.md)
   Uses upstream Backstage catalog documentation to cover schema, ownership,
   metadata freshness, integration boundaries, action authorization, and task
   success rather than treating a portal as an inventory spreadsheet.
2. [**Measure platform impact with DORA metrics without gaming teams.**](../../questions/sre/measure-platform-impact-with-dora.md)
   Uses the Google Cloud DORA program's public metric and platform-engineering
   guidance to cover comparable baselines, balanced interpretation, adoption
   and developer-experience context, and Goodhart-style failure modes.

## Central publication handoff

The coordinator must make these shared-file changes atomically after reviewing
the two additions:

1. Add `cnpa` under `## Certifications` in `TAGS.md`.
2. Add `{"tag": "cnpa", "map": "docs/certifications/cnpa.md", "minimum_questions": 20}` to `config/content-manifest.json`.
3. Set `backend-architecture` and `sre` to `in-progress` during additive
   integration, because each receives one certification-specific gap Question
   beyond its completed 25-Question core.
4. Apply `cnpa` to all 22 Questions linked in the map, including the two new
   gap Questions, then regenerate `assets/questions.js` so every Markdown path
   appears exactly once as a Pages-rendered `.html` record.
5. Let the existing manifest contract enforce that the map exists, `cnpa` is
   documented, and at least 20 active Questions carry the tag. Do not add a
   one-off hard-coded validator branch.

## Publication gate

Do not expose a CNPA filter until the tag vocabulary, manifest entry, map,
canonical tags, catalog records, local validation, and GitHub Actions checks
pass together. This prevents a public certification label from overstating
study coverage.
