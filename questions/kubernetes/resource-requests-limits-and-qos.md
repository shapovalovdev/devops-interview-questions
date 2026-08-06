---
title: Set Pod resource requests and limits
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, resource-limits, capacity-planning, reliability]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set Pod resource requests and limits

How do requests and limits affect scheduling and runtime behavior?

## Answer guide

- Requests are used by the scheduler to decide whether a node has enough allocatable resource; limits bound resource use enforced by the runtime and kernel mechanisms.
- CPU limit pressure usually throttles work, while exceeding a memory limit can result in an OOM kill; observe latency, throttling, and memory working set before selecting values.
- QoS classification depends on the request/limit configuration and influences eviction priority, but it is not a substitute for capacity planning.
- Start with measured demand and headroom, set namespace guardrails with LimitRanges and ResourceQuotas, and revisit values after load or application changes.

## References

- [Kubernetes: Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes: Pod QoS classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
