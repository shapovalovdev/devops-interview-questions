# CGOA coverage map

This map aligns original canonical practice Questions with the public
[Certified GitOps Associate (CGOA) program page](https://training.linuxfoundation.org/certification/certified-gitops-associate-cgoa/)
published by Linux Foundation Education and the CNCF's public
[CGOA curriculum outline](https://github.com/cncf/curriculum/tree/master/cgoa).
Both sources were reviewed on 2026-08-12. This is a study map, **not** a
reproduction of exam questions, confidential material, leaked content, or a
promise of exam coverage. Check the Linux Foundation program page before using
the map: it is the current public authority for exam domains and weights.

The Linux Foundation program page publishes five weighted domains: GitOps
Principles (30%), GitOps Patterns (20%), GitOps Terminology (20%), Related
Practices (16%), and Tooling (14%). The CNCF `cncf/curriculum` repository's
public CGOA outline presents the same subject area as four equally weighted
content areas (GitOps Fundamentals, GitOps Principles & Practices, GitOps
Tooling & Implementation, and GitOps Security & Observability). This map uses
the current Linux Foundation five-domain weighting because it is the more
specific published breakdown, and it keeps the CNCF repository's security and
observability emphasis discoverable through the linked Questions on secret
delivery and reconciliation feedback. CGOA is a beginner-level, 90-minute,
online, proctored, multiple-choice exam.

Every linked Question is an original learning prompt. Its own Markdown file,
not this certification map, provides its answer guide, primary-source metadata,
and complementary technical blog reading. Questions stay in their canonical
`ci-cd`, `version-control`, `infrastructure-as-code`, `configuration-management`,
`kubernetes`, `security`, or `troubleshooting` Theme, so the database never
duplicates material into a CGOA-only folder. The `cgoa` tag is a cross-cutting
study filter, not a second copy of a Question.

## Official domain mapping

| Current official domain and published competencies | Weight | Canonical original practice Questions | Coverage decision |
| --- | ---: | --- | --- |
| GitOps Principles: declarative; versioned and immutable; pulled automatically; continuously reconciled | 30% | [Explain the four GitOps principles](../../questions/ci-cd/gitops-principles.md); [Explain Argo CD Application synchronization](../../questions/ci-cd/argo-cd-application-sync.md); [Respond to Argo CD drift without masking an incident](../../questions/ci-cd/argo-cd-reconciliation-drift.md); [Why should CI publish immutable release artifacts?](../../questions/ci-cd/immutable-release-artifacts.md); [Explain Git's object model](../../questions/version-control/git-object-model.md); [Create an auditable release tag](../../questions/version-control/release-tags.md); [Operate a custom resource and its controller safely](../../questions/kubernetes/crd-operator-lifecycle.md) | One original gap Question added, because no existing Question named the four principles as a set or explained what partial adoption costs. The remaining principles are covered by existing content-addressed history, immutability, pull-driven synchronization, and controller-reconciliation Questions. |
| GitOps Patterns: deployment and release patterns; progressive delivery patterns; pull vs. event-driven; architecture patterns (in-cluster and external reconciler, state store management) | 20% | [Choose a pull-based reconciler or a push-based deployment pipeline](../../questions/ci-cd/gitops-pull-versus-push-delivery.md); [Choose a progressive Argo Rollouts strategy](../../questions/ci-cd/argo-rollouts-progressive-delivery.md); [Define an Argo Rollouts AnalysisTemplate safely](../../questions/ci-cd/argo-rollouts-analysis.md); [Decide whether to advance or stop a canary deployment](../../questions/ci-cd/canary-deployment-decision.md); [Plan a blue-green production cutover](../../questions/ci-cd/blue-green-cutover.md); [Explain the Argo Events event path](../../questions/ci-cd/argo-events-architecture.md); [Set Argo CD Application project boundaries](../../questions/ci-cd/argo-cd-application-project-boundaries.md) | One original gap Question added for the pull-versus-event-driven and reconciler-placement objective, which the existing release-pattern Questions did not decide. Deployment, release, and progressive-delivery patterns are already covered at operational depth. |
| GitOps Terminology: continuous; declarative description; desired state; state drift; state reconciliation; GitOps managed software system; state store; feedback loop; rollback | 20% | [Structure a Git state store for GitOps environments](../../questions/version-control/gitops-state-store-layout.md); [Design a deployment rollback](../../questions/ci-cd/roll-back-a-deployment.md); [Respond to Argo CD drift without masking an incident](../../questions/ci-cd/argo-cd-reconciliation-drift.md); [Detect and handle infrastructure drift](../../questions/infrastructure-as-code/infrastructure-drift.md); [Design safe configuration drift remediation](../../questions/configuration-management/configuration-drift-remediation.md); [Why does Terraform use state?](../../questions/infrastructure-as-code/terraform-state-purpose.md); [Contain a bad deployment while protecting evidence](../../questions/troubleshooting/handle-bad-deployment.md) | One original gap Question added for the state-store term, which had no Question about how desired state is laid out, pinned, and promoted. Drift, reconciliation, desired state, and rollback are covered by existing Questions. |
| Related Practices: Configuration as Code (CaC); Infrastructure as Code (IaC); DevOps and DevSecOps; CI and CD | 16% | [Deliver secrets to a GitOps-reconciled cluster](../../questions/security/gitops-secret-delivery.md); [Distinguish continuous integration, delivery, and deployment](../../questions/ci-cd/ci-versus-cd.md); [Govern infrastructure drift at organization scale](../../questions/infrastructure-as-code/iac-drift-governance.md); [Design policy-as-code gates for Terraform delivery](../../questions/infrastructure-as-code/policy-as-code-gates.md); [Explain idempotence in an Ansible playbook](../../questions/configuration-management/ansible-idempotence.md); [Verify supply-chain provenance before deployment](../../questions/ci-cd/supply-chain-provenance.md); [Design CI/CD quality gates for a service](../../questions/ci-cd/pipeline-quality-gates.md) | One original gap Question added for the DevSecOps competency, because plaintext secrets are the single practice that a Git state store makes worse and no existing Question answered it. CaC, IaC, CI, and CD are covered by existing Questions. |
| Tooling: manifest format and packaging; state store systems (Git and alternatives); reconciliation engines (Argo CD, Flux, and alternatives); interoperability with notifications, observability, and continuous integration tools | 14% | [Explain how Flux reconciles a cluster from a source](../../questions/ci-cd/flux-reconciliation-engine.md); [Close the feedback loop for a GitOps deployment](../../questions/ci-cd/gitops-feedback-loop.md); [Choose Helm or Kustomize rendering in Argo CD](../../questions/ci-cd/argo-cd-helm-kustomize-rendering.md); [Install a cluster component with Helm or Kustomize safely](../../questions/kubernetes/helm-kustomize-component-installation.md); [Design an Argo Events Sensor for a production trigger](../../questions/ci-cd/argo-events-sensor-dependencies.md) | Two original gap Questions added. The database covered only one reconciliation engine, so a Flux Question was required for the "and alternatives" competency, and nothing covered the notification/observability interoperability that closes the loop. Manifest format and packaging are covered by the existing Helm and Kustomize Questions. |

## Gap decision

Six original canonical Questions are added in this pass, one for each published
competency that had no existing coverage and none merely to inflate the map:

1. [**Explain the four GitOps principles.**](../../questions/ci-cd/gitops-principles.md)
   Domain 1 is the largest weight at 30% and its objectives are the four
   OpenGitOps v1.0.0 principles by name. No existing Question stated them as a
   set or explained why a CI job that pushes `kubectl apply` satisfies only one
   of them. Sourced from the OpenGitOps site and the `open-gitops/documents`
   principles document.
2. [**Choose a pull-based reconciler or a push-based deployment pipeline.**](../../questions/ci-cd/gitops-pull-versus-push-delivery.md)
   Domain 2 names "pull vs. event-driven" and in-cluster versus external
   reconciler placement as architecture patterns. The existing Argo CD and Argo
   Events Questions assume a reconciler is already chosen and placed; this one
   makes the decision, including who holds cluster credentials. Sourced from
   the Argo CD architecture page and the Flux concepts page.
3. [**Structure a Git state store for GitOps environments.**](../../questions/version-control/gitops-state-store-layout.md)
   "State store" is a published Domain 3 term and a Domain 5 tooling
   competency. The database had 25 Git Questions and none about laying out a
   repository as the desired-state store for environments, pinning revisions,
   or promoting between them. Sourced from the Flux repository-structure guide
   and the Argo CD best-practices page.
4. [**Deliver secrets to a GitOps-reconciled cluster.**](../../questions/security/gitops-secret-delivery.md)
   Domain 4 names DevSecOps, and the CNCF outline's fourth content area is
   GitOps Security & Observability. Existing secret Questions cover CI secrets,
   Kubernetes Secret access, and Ansible Vault, but none covers the specific
   problem of a state store that keeps every committed value forever. Sourced
   from the Flux SOPS guide, the Kubernetes Secret concept page, and the
   External Secrets Operator documentation.
5. [**Explain how Flux reconciles a cluster from a source.**](../../questions/ci-cd/flux-reconciliation-engine.md)
   Domain 5 names "reconciliation engines (ArgoCD, Flux, and alternatives)".
   Every existing reconciliation Question was Argo CD-specific, so a candidate
   studying from this database would have seen exactly one engine. Sourced from
   the Flux components and concepts documentation.
6. [**Close the feedback loop for a GitOps deployment.**](../../questions/ci-cd/gitops-feedback-loop.md)
   "Feedback loop" is a published Domain 3 term and Domain 5 requires
   interoperability with notifications, observability, and CI tools. The
   existing drift Question reacts to a reported difference; none explained how
   the reported result gets back to the people who merged the change. Sourced
   from the Argo CD health and notifications documentation and the Flux
   monitoring documentation.

No other published competency needed a new Question. Adding a CGOA-only prompt
for progressive delivery, rollback, drift, CI/CD boundaries, or manifest
packaging would repeat an existing canonical Question rather than close a gap.
Revisit this decision if the Linux Foundation page changes its domains or
weights, or if the CNCF outline gains a competency that the linked material
does not represent.

## Focused verification plan and evidence

`tests/test_cgoa_curriculum_map.py` is the narrow regression gate for this map.
It verifies the two official curriculum URLs, the review date, the current
five-domain weights, the explicit no-exam-material statement, the presence of
an explicit gap decision, and that every mapped canonical Markdown file exists,
carries the `cgoa` tag, and has structured primary-source metadata, an answer
guide, references, and a labelled complementary blog. The test also requires
every mapped filename to be linked by this document.

The focused check was run locally with:

```sh
python3 tests/test_cgoa_curriculum_map.py
```

The repository-wide content validator, the originality gate, the manifest
contract, the site check, and the live learning-resource audit were run before
publication, and GitHub Actions is the final publication gate.

## Central integration record

These shared changes were made together so the public site never advertises a
CGOA filter it cannot satisfy:

1. `cgoa` is documented in the certification vocabulary in `TAGS.md`.
2. `{"tag": "cgoa", "map": "docs/certifications/cgoa.md", "minimum_questions": 32}`
   is registered in `config/content-manifest.json`, keeping the list sorted by
   tag.
3. The `cgoa` tag is applied to exactly the 32 canonical Questions linked
   above, including the six new gap Questions. No Question is tagged merely for
   being in the `ci-cd` or `version-control` Theme.
4. `assets/questions.js` is regenerated so every Markdown Question appears
   exactly once as a Pages-rendered `.html` catalog record.
5. The six new Questions are registered in
   `docs/research/link-audit-manifest.json` so their curated learning links are
   live-checked with the rest of the database.

This preserves the one-canonical-Question policy and keeps the published CGOA
study coverage honest.
