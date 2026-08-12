---
title: How do you diagnose and mitigate noisy-neighbor performance?
theme: performance-engineering
difficulty: senior
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you diagnose and mitigate noisy-neighbor performance?

One tenant's bulk import is degrading every other tenant's p99 on a shared Kubernetes cluster. How do you prove that is the cause, and how do you contain it?

## Answer guide

- Establish attribution before mitigation. Break requests, CPU seconds, database time, and bytes down by tenant and compare the affected window with a control period; where per-tenant telemetry does not exist, correlate the suspect's activity against the victims' latency and then confirm with a controlled throttle. Identify the contended layer as well, because node CPU, the shared database, a cache whose working set one tenant has evicted, and a rate-limited third-party dependency all present as "the neighbours are slow" and have different fixes.
- In Kubernetes, requests and limits do different jobs. CPU requests set the cgroup weight and drive scheduling, so they decide what a pod receives when the node is contended; CPU limits set CFS quota per period and cause hard throttling visible in `container_cpu_cfs_throttled_seconds_total` even when the node is otherwise idle. Memory limits are enforced by OOM kill, not throttling. A latency-sensitive pod sharing a node with a batch pod that declares no requests loses by default, so give it Guaranteed QoS and separate the workloads physically with taints, node pools, or spread constraints.
- Cgroups isolate CPU and memory reasonably well and isolate almost nothing else: shared last-level cache, memory bandwidth, disk queues, and NIC capacity are not partitioned, so a co-tenant saturating NVMe or the network is invisible in CPU metrics. Below the cluster, hypervisor steal time and burst-credit exhaustion produce identical symptoms with no local cause at all. The loudest shared resource is usually the database, which cannot see pods — isolation there means per-tenant-class connection pools, statement timeouts, and application-level quotas.
- Applying CPU limits everywhere in the name of fairness is the most common self-inflicted version of this incident: it throttles latency-sensitive services that were comfortably within node capacity. Per-tenant limits counted in requests ignore cost, since one expensive query outweighs a thousand cheap ones, so quota should track work such as CPU time or rows scanned. And relocating the batch job to another node without attaching a quota to it simply hands the problem to that node's tenants.

## References

- [Kubernetes: Resource management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
