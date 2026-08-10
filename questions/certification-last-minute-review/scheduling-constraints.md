---
title: Combine node selectors, affinity, taints, and tolerations
theme: certification-last-minute-review
difficulty: middle
type: scenario
tags: [kubernetes, cka, ckad, availability, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Combine node selectors, affinity, taints, and tolerations

How do you place a workload while keeping unsuitable Pods off dedicated nodes?

## Answer guide

- Node selectors and required node affinity constrain where a Pod may schedule; preferred affinity expresses a scoring preference. Pod anti-affinity can spread replicas but may reduce schedulability in a small cluster.
- A taint repels Pods unless they have a matching toleration. A toleration permits placement but does not guarantee it, so pair it with an appropriate selector or affinity for dedicated nodes.
- Start with the simplest constraint and read the scheduler's failed-scheduling event. Labels are trusted only if controlled by cluster operators; avoid mutable or user-controlled labels for isolation decisions.

## References

- [Kubernetes: assigning Pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- Further reading (blog): [Ian Lewis and David Oppenheimer — advanced scheduling in Kubernetes](https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/)

## What to learn next

- Official documentation: [Assign Pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- Manual or specification: [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- Maintainer or personal blog: [Ian Lewis and David Oppenheimer — advanced scheduling in Kubernetes](https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes/)
- Technical blog: [Google Cloud — Pod affinity](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-pod-affinity-and-anti-affinity)
- Hands-on guide: [Kubernetes assign Pods using node affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
