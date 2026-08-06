---
title: Explain a Kubernetes Deployment rollout and rollback
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, deployment, rolling-update, reliability]
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
