---
title: How should a staff engineer evaluate resilience versus performance trade-offs?
theme: performance-engineering
difficulty: staff
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/addressing-cascading-failures/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How should a staff engineer evaluate resilience versus performance trade-offs?

A team wants to delete the retry policy and circuit breaker from a hot path because together they add 8 ms per request. How do you evaluate that trade-off?

## Answer guide

- Price both sides in the same unit. The 8 ms is a certain cost paid on every request forever; the mechanism buys a reduction in the probability and duration of a failure whose cost is error budget. Work the expectation: if removing them adds an hour of unavailability per quarter, weigh that against the budget freed by 8 ms across the same quarter's traffic. More often than not the mechanism survives and the real answer is making it cheaper — a cached breaker-state check, a per-host limiter instead of a shared lock, a hedge issued only above a latency threshold.
- The argument runs both ways, because retries and breakers are also amplifiers. Retries add load exactly when a dependency is degraded, and independent retry policies at three layers turn one failure into eight requests, which is a cascading-failure mechanism rather than a safety net unless bounded by a retry budget and jittered backoff. A circuit breaker converts a slow failure into a fast one, which only helps if the caller has a meaningful degraded response to give. Evaluate both under overload, not in the steady state where the 8 ms figure was measured.
- Resilience mechanisms usually cost tail latency rather than median, so any evaluation reported as an average misprices them: a hedged request improves p99 while raising total load, timeout-plus-retry doubles the worst case, and half-open probing injects a periodic slow request by design. Redundancy has the same shape — quorum writes and cross-region replication buy durability at a latency floor set by the slowest required participant and by propagation delay, which no amount of tuning removes.
- Deleting a mechanism whose value is invisible because it has been working is the classic error, so require evidence of what it caught — breaker trips, retries that succeeded, requests that a bounded queue rejected — before removing it. Keeping an untested mechanism is the mirror error, since a breaker that has never opened and a fallback nobody exercises fail together on first use. Decide with explicit ownership: record the failure being accepted, its expected frequency, and who accepted it, and re-test the degraded path on a schedule so the trade-off stays the one that was actually agreed.

## References

- [Google SRE: Addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
