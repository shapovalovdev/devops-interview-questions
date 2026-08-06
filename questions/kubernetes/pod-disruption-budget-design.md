---
title: Use PodDisruptionBudgets for voluntary disruptions
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, availability, reliability, deployment]
sources:
  - url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use PodDisruptionBudgets for voluntary disruptions

How do you protect availability during node drain without blocking all maintenance?

## Answer guide

- A PodDisruptionBudget limits voluntary disruptions through the eviction API by declaring `minAvailable` or `maxUnavailable` for Pods selected by labels.
- Size it from the application quorum, replica count, topology, and recovery time; it should preserve service capacity while allowing planned replacement.
- It does not protect against involuntary failures such as a node crash, and direct deletion can bypass the eviction path.
- Overly strict budgets can make drains and upgrades stall, so monitor eviction behavior and rehearse node maintenance with realistic failure conditions.

## References

- [Kubernetes: Specifying a disruption budget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- [Kubernetes: Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
