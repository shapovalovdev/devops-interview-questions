---
title: Explain requests, limits, QoS, and a Pending Pod
theme: certification-last-minute-review
difficulty: middle
type: troubleshooting
tags: [kubernetes, cpu, memory, resource-limits, cka, ckad, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain requests, limits, QoS, and a Pending Pod

Why can a Pod remain Pending despite a node appearing lightly used?

## Answer guide

- The scheduler places Pods using requests, not current observed usage. A node can show idle CPU while its allocatable capacity cannot satisfy a new Pod's requested CPU, memory, ports, affinity, or taint constraints.
- A limit is a runtime bound; CPU is throttled when it reaches its limit, while memory pressure can cause an OOM kill. Kubernetes assigns QoS classes from request and limit combinations, affecting eviction preference.
- Inspect scheduling events, node allocatable resources, and existing requests. Right-size from measurement rather than setting limits to zero or raising node capacity blindly, which can hide contention and make failures less predictable.

## References

- [Kubernetes: resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Further reading (blog): [Robusta — Kubernetes resource requests and limits](https://home.robusta.dev/blog/kubernetes-memory-limit)

## What to learn next

- Official documentation: [Kubernetes resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Manual or specification: [Kubernetes QoS classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
- Maintainer or personal blog: [Robusta — memory limits](https://home.robusta.dev/blog/kubernetes-memory-limit)
- Technical blog: [Google Cloud — requests and limits](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits)
- Hands-on guide: [Kubernetes assign memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
