---
title: Place Kubernetes workloads with affinity and taints
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, capacity-planning, reliability, security, cka, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Place Kubernetes workloads with affinity and taints

How would you isolate a latency-sensitive service while retaining scheduler flexibility?

## Answer guide

- Use node labels with required or preferred node affinity for eligible hardware/zone placement, and use pod anti-affinity or topology spread constraints to avoid correlated replica placement.
- Taints repel Pods unless they have matching tolerations; reserve them for nodes that require an explicit scheduling exception.
- Make hard requirements only for genuine constraints and use preferred rules for resilience goals, otherwise a small cluster change can leave Pods Pending.
- Account for resource requests, autoscaler behavior, and failure domains; placement policy cannot create capacity or guarantee a distinct physical failure domain by itself.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Kubernetes: Topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)

## What to learn next

- Official documentation: [Assigning Pods to nodes: node selectors and affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- Manual or specification: [kube-scheduler configuration v1 API reference](https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/)
- Maintainer or personal blog: [Daniele Polencic — how the Kubernetes scheduler filters and scores nodes](https://learnkube.com/kubernetes-scheduler-explained)
- Technical blog: [Kubernetes blog — introducing Pod topology spread constraints](https://kubernetes.io/blog/2020/05/introducing-podtopologyspread/)
- Hands-on guide: [Assign Pods to nodes using node affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
