---
title: What evidence distinguishes a bottleneck from a busy component?
theme: performance-engineering
difficulty: junior
type: troubleshooting
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.brendangregg.com/usemethod.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# What evidence distinguishes a bottleneck from a busy component?

CPU utilization sits at 85 percent on a service whose latency has doubled. What evidence tells you the CPU is the bottleneck rather than merely busy?

## Answer guide

- Utilization says a resource is in use; saturation says work is queued waiting for it. A component is the bottleneck only when the queue for it is growing and relieving that queue moves the end-to-end metric. Eighty-five percent CPU with a near-empty run queue is busy. The same 85 percent with load average above core count and `/proc/pressure/cpu` `some avg10` climbing is saturated, and only the second one explains doubled latency.
- That is the USE method: for each resource check utilization, saturation, and errors, and let the saturation counter decide. Each resource has its own — run-queue length and CPU pressure for CPU, refault rate and memory pressure for memory, `aqu-sz` and `await` from `iostat -x` for disk, interface drops and retransmit counters for the network, and acquisition wait time for logical resources such as connection or thread pools. Errors deserve their own look, because NIC drops or storage retries produce latency that utilization never reflects.
- Averaging destroys this signal. A 60-second sample showing 50 percent CPU is compatible with being pinned at 100 percent in 10 ms bursts that are exactly what a p99 feels. Inside a container the host figure is the wrong one entirely: the meaningful evidence is the cgroup's `cpu.stat`, where `nr_throttled` and `throttled_time` can show hard quota throttling every period on a pod using 40 percent of the node. Steal time on a shared hypervisor breaks the mapping in the other direction.
- Optimising a component that is merely busy changes nothing and costs the team's confidence in the investigation. Fixing the real bottleneck relocates the queue to whatever is next, so re-measure after every change rather than assuming the win holds. And a resource can be almost idle and still be the bottleneck when it is serialized — a single-threaded event loop, one global lock, one partition leader. Lock contention is invisible in `top` and shows up only in contention counters or off-CPU profiling.

## References

- [Brendan Gregg: The USE method](https://www.brendangregg.com/usemethod.html)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
