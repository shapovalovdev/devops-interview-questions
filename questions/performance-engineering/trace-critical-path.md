---
title: How do you find the critical path of a slow distributed request?
theme: performance-engineering
difficulty: middle
type: troubleshooting
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://opentelemetry.io/docs/concepts/signals/traces/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you find the critical path of a slow distributed request?

A trace of a two-second request contains 60 spans across eight services, most of them short. How do you work out which spans are actually on the critical path?

## Answer guide

- The critical path is the chain of spans whose durations account for the root span's duration — the work that, if shortened, shortens the request. Walk down from the root and at each level keep the children that are not overlapped by a concurrent sibling: a fan-out of three 300 ms calls issued in parallel costs 300 ms, not 900. Summing every span's duration across the trace is the standard misreading and produces a number with no relationship to user-visible latency.
- Compute self time — a span's duration minus the intervals its children cover — and treat a large unexplained gap as the finding rather than as noise. A gap at the start of a span is usually queue or connection-pool wait before the work began; a gap at the end is usually response serialization or an un-instrumented commit or flush; a gap in the middle is often a garbage-collection pause or scheduler wait. These gaps are where un-instrumented code hides, and they are frequently the largest single contributor.
- Span timestamps come from each host's own clock, so offsets of tens of milliseconds are routine and can make a child appear to start before its parent. Trust duration comparisons within one service and treat cross-service subtraction as approximate; the reliable way to attribute network and queue time is the client-side span wrapping the RPC. Context propagation is the other structural hazard — it breaks across thread pools, async continuations, and message queues, which detaches whole subtrees so they never appear on the path at all.
- With head-based sampling at one percent, the trace you need was probably never recorded; link exemplars from the slow histogram buckets or move to tail-based sampling so slow requests are kept by construction. One trace is an anecdote — a cold cache, a leader election, a single unlucky preemption — so confirm the pattern across a population of slow traces before rewriting anything. Adding spans is not free either: per-span creation and export cost is real inside a hot loop and can itself become the latency you are chasing.

## References

- [OpenTelemetry: Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
