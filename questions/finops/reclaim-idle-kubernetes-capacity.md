---
title: Reclaim idle Kubernetes capacity
theme: finops
difficulty: middle
type: scenario
tags: [finops, kubernetes, rightsizing, resource-limits]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler
    source_type: official-docs
    verified_on: 2026-08-11
---

# Reclaim idle Kubernetes capacity

A cluster's nodes are 70 percent requested but only 15 percent used. Where does that gap come from and how do you close it?

## Answer guide

- The gap is the difference between what pods reserve and what they consume. The scheduler places pods by requests, so requested-but-unused CPU and memory is capacity you pay for and nobody can use. Closing it means moving requests down toward real usage, not adding more nodes or tightening limits.
- Measure per container over a representative window: CPU at a high percentile of actual usage and memory at the working-set peak, since memory is not compressible and an under-request that leads to eviction is far more damaging than an over-request. The Vertical Pod Autoscaler and equivalent recommenders compute exactly this and can run in recommendation-only mode so a human applies the change.
- Distinguish the three separate sources of waste before acting: inflated requests on individual workloads, bin-packing loss where the remaining space on each node is too small for any pending pod, and deliberately reserved headroom for failover and burst. Only the first is pure waste; the second is fixed by node sizing and topology, and the third is a reliability decision you should preserve consciously.
- Material constraints: lowering CPU requests changes the CFS share a container gets under contention, so a latency-sensitive service can degrade even though it never hits a limit; quality-of-service class depends on the relationship between requests and limits, and dropping out of Guaranteed changes eviction ordering; and in-place resize support varies by version, so most changes still restart the pod.
- Failure modes: applying a recommender's output automatically to a workload whose peak falls outside the observation window; shrinking requests on a daemonset that has to survive node pressure; and reporting the reclaimed capacity as a saving when no node was ever removed — the bill only falls when the cluster autoscaler or Karpenter actually consolidates nodes away.

## References

- [Managing resources for containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [GKE Vertical Pod Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)
- Further reading (blog): [Kubecost — Kubernetes cost analysis](https://www.kubecost.com/kubernetes-cost-analysis/)

## What to learn next

- Official documentation: [Managing resources for containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Manual or specification: [OpenCost cost allocation specification](https://opencost.io/docs/specification)
- Maintainer or personal blog: [Marc Brooker — on scale and system design](https://brooker.co.za/blog/2024/06/04/scale.html)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Monitor cluster resource usage](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
