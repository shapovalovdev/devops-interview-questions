---
title: Set Pod resource requests and limits
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, resource-limits, capacity-planning, reliability, kcsa, cka, ckad, kcna]
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

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes: Pod QoS classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)

## What to learn next

- Official documentation: [Resource management for Pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Manual or specification: [LimitRange v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/limit-range-v1/)
- Maintainer or personal blog: [Santhosh Nagaraj — setting the right requests and limits in Kubernetes](https://learnkube.com/setting-cpu-memory-limits-requests)
- Technical blog: [CNCF — Kubernetes resource management: QoS, quota and LimitRange](https://www.cncf.io/blog/2020/06/10/kubernetes-resources-management-qos-quota-and-limitrangeb/)
- Hands-on guide: [Assign memory resources to containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
