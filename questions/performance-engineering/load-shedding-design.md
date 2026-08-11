---
title: When and how should a service shed load?
theme: performance-engineering
difficulty: senior
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# When and how should a service shed load?

Your service is offered three times its capacity, every request now times out, and nobody is being served. What should it drop, on what signal, and at which layer?

## Answer guide

- Past capacity the question is not whether requests fail but which ones, and shedding early is what turns total failure into partial service. Reject at admission, before the request takes a thread, a connection, or a downstream call, and reject cheaply — a 503 or 429 with `Retry-After` costs almost nothing, while a request that times out after 30 seconds has held the resource for all 30. Choose victims deliberately: background and batch work before interactive traffic, low tier before high, using a priority carried in the request rather than inferred at the edge.
- Trigger on a queueing signal rather than on utilization. Queue depth, queue wait time, or the ratio of in-flight concurrency to a measured limit all move before CPU does and do not need a hand-tuned threshold; adaptive concurrency controllers infer the limit from observed latency instead. Pair shedding with a bounded queue, because an unbounded queue converts overload into unbounded latency, and drop any request whose deadline expired while it waited — serving it consumes capacity to produce a response nobody is still listening for.
- Shedding only helps if clients cooperate. They must back off with jitter, honour `Retry-After`, and hold a retry budget, or the shed load returns immediately and amplifies the overload it was meant to relieve; a circuit breaker on the caller is part of the same design. Make every rejection attributable with metrics by class and reason, or you cannot tell a healthy shed from an outage. And keep the reject path genuinely cheap — if it still authenticates, queries a database, or writes an audit record per request, the rejection path becomes the new bottleneck.
- Shedding a uniform percentage of requests is usually the wrong shape: a page that issues ten backend calls will show an error to nearly every user at a ten percent uniform shed rate, so dropping whole low-priority classes or whole sessions serves more people. Shedding also conceals its own cause and can mask a capacity shortfall for months, so treat shed rate as an objective-affecting signal that pages, not as a success metric. Placing the control upstream of a queue that other consumers drain can starve them, so put it where the whole priority order is visible.

## References

- [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
