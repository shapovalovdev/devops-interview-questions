---
title: Choose Helm or Kustomize rendering in Argo CD
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-cd, capa, configuration-management]
sources:
  - url: https://argo-cd.readthedocs.io/en/stable/user-guide/helm/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose Helm or Kustomize rendering in Argo CD

When an Argo CD Application needs environment-specific manifests, how do Helm and Kustomize fit into the design?

## Answer guide

- Argo CD can render Helm charts and Kustomize configurations from the declared source. Choose Helm when a chart’s value-driven package interface is useful; choose Kustomize when overlays and patches against plain manifests make the variation clearer.
- Keep rendered inputs in reviewed source control, pin chart or Git revisions, and inspect the generated manifests in the target context. Avoid hidden value injection that makes Git cease to be the explainable desired state.
- Treat plugins and external dependencies as supply-chain inputs. Rendering differences, chart upgrades, or overlay patches can change resources unexpectedly, so test and diff before syncing production.

## References

- [Argo CD: Helm](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/)
- [Argo CD: Kustomize](https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/)
- Further reading (blog): [GitHub Blog: managing Kubernetes manifests](https://github.blog/enterprise-software/ci-cd/gitops-with-github-actions/)
