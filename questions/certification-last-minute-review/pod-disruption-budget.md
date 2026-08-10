---
title: Use PodDisruptionBudgets without blocking maintenance
theme: certification-last-minute-review
difficulty: senior
type: scenario
tags: [kubernetes, availability, cka, reliability, rolling-update]
sources:
  - url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use PodDisruptionBudgets without blocking maintenance

How does a PodDisruptionBudget protect availability, and what does it not protect?

## Answer guide

- A PodDisruptionBudget limits voluntary disruptions such as drain or controller-initiated eviction by selecting Pods and setting `minAvailable` or `maxUnavailable`. It does not prevent involuntary loss from a node crash, kernel failure, or resource exhaustion.
- Size it against real replica count and failure tolerance. A single-replica workload with `minAvailable: 1` cannot be voluntarily evicted, which can correctly block maintenance until the service is redesigned or a maintenance decision is made.
- Inspect the budget's allowed disruptions and controller status before draining. Combine budgets with multiple replicas, topology-aware placement, graceful termination, and capacity; a PDB alone cannot make an application highly available.

## References

- [Kubernetes: configure a PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- Further reading (blog): [ScyllaDB engineering blog](https://www.scylladb.com/blog/)

## What to learn next

- Official documentation: [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- Manual or specification: [PDB API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)
- Maintainer or personal blog: [ScyllaDB engineering blog](https://www.scylladb.com/blog/)
- Technical blog: [Google Cloud — Pod affinity and anti-affinity](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-pod-affinity-and-anti-affinity)
- Hands-on guide: [Kubernetes safely drain a node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
