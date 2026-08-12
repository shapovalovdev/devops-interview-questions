---
title: How do you triage a p99 latency regression?
theme: performance-engineering
difficulty: senior
type: troubleshooting
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you triage a p99 latency regression?

At 14:05 the p99 of one endpoint jumped from 180 ms to 900 ms while p50 and the error rate stayed flat. How do you triage it?

## Answer guide

- A moved p99 with an unchanged p50 means a subset of requests got slow, not the service as a whole, so the first job is to find the dimension that separates that subset. Slice the histogram by endpoint, tenant, region and zone, instance, deployment version, request size class, and cache hit versus miss. A regression confined to one shard, one node pool, or one client version is a completely different investigation from one spread evenly across all of them.
- Line the 14:05 boundary up against the change record before theorising: deploys, feature-flag flips, config pushes, schema migrations, dependency releases, node rotations, and scale events. Then line it up against saturation signals in the same window — run queue and cgroup throttling, garbage-collection pause time, connection-pool wait, disk `await`, and each downstream's own p99. You are trying to prove a specific chain: requests are queueing, and this is the resource they are queueing for.
- Pull traces from the slow histogram buckets through exemplars, and always diff a slow trace against a fast one for the same operation rather than reading slow traces alone; the difference — an extra downstream call, a retry, a cold cache, a lock wait, a larger payload — is the finding. Cross-host clock skew of tens of milliseconds is normal, so do not build an argument on cross-service span arithmetic, and check that sampling actually captured slow requests before concluding they look ordinary.
- Mitigations regularly fake a recovery. Raising the timeout makes errors vanish while raising in-flight concurrency and lengthening the queue; adding replicas helps only when the bottleneck is per-instance rather than a shared database, cache, or partition leader; and if retries are driving the tail, retrying harder amplifies it. After any mitigation, check that request volume held steady, because a p99 also improves when traffic drops and the sample count collapses.

## References

- [Google SRE: Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
