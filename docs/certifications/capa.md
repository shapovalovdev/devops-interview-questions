# CAPA coverage map

This map aligns original practice Questions with the current [Certified Argo
Project Associate (CAPA) curriculum](https://training.linuxfoundation.org/certification/certified-argo-project-associate-capa/).
It is a study map, not a reproduction of real, confidential, or leaked exam
content. The Linux Foundation curriculum was reviewed on 2026-08-06. It lists
four domains: Argo Workflows (36%), Argo CD (34%), Argo Rollouts (18%), and
Argo Events (12%). Check the official page before studying because the program
and product behavior can change.

Every mapped Question is original, carries the canonical `capa` tag, has a full
answer guide, structured primary-source metadata, and a separately labelled
complementary technical blog post. The Questions remain in the canonical
`ci-cd` Theme so Argo delivery concepts can be reused without copies.

| Official domain and objectives | Weight | Canonical practice Questions tagged `capa` |
| --- | ---: | --- |
| Argo Workflows: fundamentals, artifacts, templates, specs, DAGs, data-processing jobs | 36% | [Use Argo Workflows](../../questions/ci-cd/argo-workflows-fundamentals.md); [pass artifacts](../../questions/ci-cd/argo-workflow-artifacts.md); [reuse templates](../../questions/ci-cd/argo-workflow-template-reuse.md); [model a DAG](../../questions/ci-cd/argo-workflows-dag-failure.md) |
| Argo CD: fundamentals, synchronization, Applications, Helm/Kustomize, reconciliation patterns | 34% | [synchronize an Application](../../questions/ci-cd/argo-cd-application-sync.md); [set project boundaries](../../questions/ci-cd/argo-cd-application-project-boundaries.md); [choose Helm or Kustomize](../../questions/ci-cd/argo-cd-helm-kustomize-rendering.md); [respond to drift](../../questions/ci-cd/argo-cd-reconciliation-drift.md) |
| Argo Rollouts: fundamentals, progressive rollout strategies, AnalysisTemplate and AnalysisRun | 18% | [choose a progressive strategy](../../questions/ci-cd/argo-rollouts-progressive-delivery.md); [define an AnalysisTemplate](../../questions/ci-cd/argo-rollouts-analysis.md) |
| Argo Events: fundamentals, components, and architecture | 12% | [explain the event path](../../questions/ci-cd/argo-events-architecture.md); [design a Sensor](../../questions/ci-cd/argo-events-sensor-dependencies.md) |

The map intentionally uses practical, original prompts. It does not claim that
these are exam questions or that they predict an individual examination.
