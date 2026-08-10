---
title: Respond to Argo CD drift without masking an incident
theme: ci-cd
difficulty: senior
type: troubleshooting
tags: [ci-cd, kubernetes, argo, argo-cd, capa, troubleshooting, reliability, cnpe, cnpa]
sources:
  - url: https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to Argo CD drift without masking an incident

An Application is OutOfSync immediately after an operator changed a live resource during an outage. What should happen next?

## Answer guide

- Determine whether the live change is emergency mitigation, a controller-owned field, or an unintended mutation; compare desired and live manifests and record the incident context before forcing reconciliation.
- Make the intended durable change in Git, review it, then synchronize using the project’s approved policy. If automation is enabled, temporarily control it through the documented operational process rather than repeatedly fighting the controller.
- Do not normalize all differences blindly. Pruning, admission defaults, mutable controllers, and a bad Git commit can cause disruption; preserve evidence and verify service health after the desired state is restored.

## References

- [Argo CD: automated sync policy](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- Further reading (blog): [GitHub Blog: operating GitOps safely](https://github.blog/enterprise-software/ci-cd/what-is-gitops/)

## What to learn next

- Official documentation: [Argo CD diffing and drift detection](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/)
- Manual or specification: [OpenGitOps Principles v1.0.0](https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md)
- Maintainer or personal blog: [Arthur Koziel — setting up Argo CD with Helm](https://www.arthurkoziel.com/setting-up-argocd-with-helm/)
- Technical blog: [Codefresh — Argo CD engineering blog](https://codefresh.io/blog/)
- Hands-on guide: [Argo CD resource tracking and ownership](https://argo-cd.readthedocs.io/en/stable/user-guide/resource_tracking/)
