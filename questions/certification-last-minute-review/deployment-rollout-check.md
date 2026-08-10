---
title: Verify a Deployment rollout and recover safely
theme: certification-last-minute-review
difficulty: junior
type: scenario
tags: [kubernetes, deployment, cka, ckad, kcna, rolling-update]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Verify a Deployment rollout and recover safely

What do you check when a Deployment update does not become available?

## Answer guide

- A Deployment creates ReplicaSets and manages the transition according to its strategy. Use `kubectl rollout status`, inspect conditions, and compare the new ReplicaSet, desired replicas, ready replicas, and unavailable replicas.
- Read Pod events before retrying: image pull failures, failed scheduling, bad readiness probes, and quota limits can all prevent availability. A rollout can be progressing while no new Pod is ready.
- If the new revision is unsafe, use the recorded Deployment revision to undo it, then correct the declarative manifest. Do not delete ReplicaSets first: that removes rollback evidence and can reduce available capacity.

## References

- [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Further reading (blog): [Kubernetes blog](https://kubernetes.io/blog/)

## What to learn next

- Official documentation: [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Manual or specification: [Deployment API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes update a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
