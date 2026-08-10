---
title: Choose a progressive Argo Rollouts strategy
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-rollouts, capa, deployment, reliability, cnpe]
sources:
  - url: https://argo-rollouts.readthedocs.io/en/stable/features/canary/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a progressive Argo Rollouts strategy

How would you use Argo Rollouts to reduce risk when releasing an API with uncertain latency impact?

## Answer guide

- Replace the ordinary Deployment rollout with an Argo Rollout and choose a canary or blue-green strategy appropriate to the traffic and rollback needs. A canary advances a bounded portion of traffic through explicit steps and pauses.
- Define stable and candidate services or routing integration as required by the chosen traffic-management provider, and make promotion contingent on meaningful latency, error, and business signals.
- Progressive delivery limits exposure; it does not validate a poor metric or incompatible data change. Ensure rollback behavior, session handling, capacity, and timeouts are tested before relying on automated promotion.

## References

- [Argo Rollouts: canary deployment strategy](https://argo-rollouts.readthedocs.io/en/stable/features/canary/)
- Further reading (blog): [Google Cloud Blog: canary deployment strategies](https://cloud.google.com/blog/products/devops-sre/canary-deployments-using-kubernetes)

## What to learn next

- Official documentation: [Argo Rollouts traffic management](https://argo-rollouts.readthedocs.io/en/stable/features/traffic-management/)
- Manual or specification: [Argo Rollouts specification reference](https://argo-rollouts.readthedocs.io/en/stable/features/specification/)
- Maintainer or personal blog: [Martin Fowler — canary release](https://martinfowler.com/bliki/CanaryRelease.html)
- Technical blog: [Akuity — Argo maintainers' engineering blog](https://akuity.io/blog/)
- Hands-on guide: [Argo Rollouts getting started](https://argo-rollouts.readthedocs.io/en/stable/getting-started/)
