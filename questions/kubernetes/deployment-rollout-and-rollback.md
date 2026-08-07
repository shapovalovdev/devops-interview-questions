---
title: Explain a Kubernetes Deployment rollout and rollback
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, deployment, rolling-update, reliability, cka, ckad, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a Kubernetes Deployment rollout and rollback

How does a Deployment replace application Pods safely, and what would make you roll it back?

## Answer guide

- A Deployment manages ReplicaSets and changes Pods toward the declared template and replica count; a rolling update is the default strategy.
- Readiness controls whether a Pod is considered ready for Service traffic, while the Deployment's availability calculation and rollout progress need separate observation.
- `maxSurge` and `maxUnavailable` bound temporary extra capacity and unavailable replicas. Choose them from application capacity, startup time, and failure tolerance rather than using defaults blindly.
- Pause or roll back for a verified regression in correctness, availability, latency, security, or a rollout that cannot make progress. Inspect ReplicaSets, Pod events, probe failures, and capacity first because rollback cannot cure an external dependency failure.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes: Rolling update Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

## What to learn next

- Official documentation: [Kubernetes concepts: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Manual or specification: [Deployment v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
- Maintainer or personal blog: [Gergely Risko — how Kubernetes rollbacks work with ReplicaSet revisions](https://learnkube.com/kubernetes-rollbacks)
- Technical blog: [CNCF — mastering deployment strategies: blue-green, canary and more](https://www.cncf.io/blog/2023/05/04/mastering-deployment-strategies-a-comprehensive-guide-to-blue-green-canary-and-more/)
- Hands-on guide: [Perform a rolling update tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
