---
title: Contain a noisy neighbour on a shared platform
theme: platform-engineering
difficulty: middle
type: troubleshooting
tags: [platform-engineering, multi-tenancy, resource-limits, kubernetes]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Contain a noisy neighbour on a shared platform

One tenant's batch job is making every other workload on the shared cluster slow. How do you diagnose and contain it?

## Answer guide

- Diagnose by asking which shared resource is saturated and whether the victims were promised protection from it. Check node-level pressure first — CPU throttling counters, memory working set against the node allocatable, disk and network saturation — then map the pressure back to pods by namespace. The immediate containment is a limit on the offender, but the durable fix depends on the resource class: CPU is compressible so the offender gets throttled, while memory is not, so an over-consuming pod is killed rather than slowed.
- The Kubernetes mechanism is requests and limits per container: requests drive scheduling and the CPU shares a container gets under contention, limits cap consumption through cgroup quota for CPU and a hard ceiling for memory. Quality of Service class follows from them — Guaranteed when every container sets equal requests and limits, Burstable when requests are set but lower than limits, BestEffort when neither is set — and that class decides eviction order when the node comes under pressure. A BestEffort batch job on the same node as a Guaranteed serving workload is the configuration that produces this incident.
- Constraints: limits alone do not solve resources the kernel does not partition per pod, so page cache, disk IOPS, network bandwidth, conntrack entries, and shared control-plane API quota still leak between tenants; for those you need separate node pools, storage classes with IOPS guarantees, or client-side API rate limits. Setting a CPU limit where you only needed a request causes throttling on latency-sensitive services that would otherwise burst harmlessly, so the fix for the noisy neighbour must not be applied indiscriminately to its victims.
- Failure modes: raising the offender's limit to make it finish faster, which just moves the saturation; a memory limit set from steady-state usage so the pod is killed during its once-a-day peak; scheduling batch and serving workloads onto the same nodes with no taint or priority separation; and an eviction cascade where the node reclaims memory by killing the BestEffort pods, the batch job restarts, and the cycle repeats until someone notices the crash loop.

## References

- [Kubernetes — resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Further reading (blog): [Kubernetes blog](https://kubernetes.io/blog/)

## What to learn next

- Official documentation: [Kubernetes — resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Manual or specification: [Kubernetes node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes — configure quality of service for pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)
