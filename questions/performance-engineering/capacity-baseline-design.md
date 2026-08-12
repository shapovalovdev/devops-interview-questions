---
title: How would you establish a capacity baseline for a service?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How would you establish a capacity baseline for a service?

You inherit a service with no capacity model and are asked how much traffic it can absorb before the next seasonal peak. How do you build a baseline you can defend?

## Answer guide

- A baseline is a measured relationship between a demand driver and resource consumption, not a snapshot of current utilization. Choose the driver the business can forecast — orders per minute, active sessions — and measure unit cost against it: CPU seconds, memory, database time, and IOPS per unit, all at a stated latency target. Headroom is then arithmetic in the business's own units. Derive it from at least one full weekly cycle so weekday and weekend shapes are included, and stamp it with the software version it was measured against.
- Capacity is set by the first resource that saturates at the latency target, so record utilization and saturation for every resource on the path: instance CPU and memory, thread and connection pools, database CPU and IOPS, cache memory and eviction rate, queue lag, and third-party rate limits. The limiting resource is often not the one you can scale — adding stateless replicas raises pressure on the shared database and past a point lowers total capacity rather than raising it.
- Use the peak minute, not the hourly mean, and record the peak-to-average ratio: a service averaging 30 percent CPU with a 3x daily peak has far less headroom than the average suggests. Capture the parts that do not scale linearly, because cache hit rate falls as the working set grows, query plans change at larger row counts, and per-instance overheads such as connection count and log volume grow with replica count. Note instance types, quotas, and dependency versions, since an instance-family change invalidates the model.
- Extrapolating a single load test into a seasonal forecast ignores that real growth changes data size and traffic mix as well as rate, so a 3x rate assumption with a 3x larger table is not the system you measured. A baseline captured while the autoscaler was reacting measures the autoscaler. And a baseline nobody refreshes rots quietly: pair it with a scheduled re-measurement and an alert on the driver-to-resource ratio drifting, so you learn about the change before the peak rather than during it.

## References

- [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
