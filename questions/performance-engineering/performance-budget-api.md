---
title: How do performance budgets change API and dependency design?
theme: performance-engineering
difficulty: senior
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.w3.org/TR/server-timing/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do performance budgets change API and dependency design?

A page must render in 500 ms and calls a gateway that fans out to six services. How do you turn that number into per-service budgets, and what does having a budget change about the API design?

## Answer guide

- Allocate the end-to-end target across the call graph so each hop owns a number it can be held to. Reserve network and client render time from the 500 ms, then divide the remaining server budget along the critical path: sequential hops add, parallel hops cost the slowest branch, so deciding which of the six calls must be sequential is the design decision the budget forces. Each service publishes a p99 budget for its endpoint, and the longest sequential chain plus expected retries must fit inside the parent's allocation with margin left over.
- A budget is only real if the deadline travels with the request. Propagate remaining time explicitly — a gRPC deadline, a deadline header, a context with a timeout — so a downstream can refuse work it cannot complete in the time left, and cancel downstream work when the caller abandons the request. `Server-Timing` lets a service report its own segments back so real-user monitoring can attribute where the budget went. Without propagation each hop applies its own static timeout and the sum silently exceeds the target nobody is measuring.
- Budgets push directly against chatty interfaces: if one hop costs 20 ms and a view needs thirty objects, per-object endpoints are excluded by arithmetic and a batch endpoint becomes a requirement rather than an optimisation. They also make optionality explicit — a non-critical enrichment call has to be parallel, cancellable, and degradable to a default instead of able to hold the response — and they favour precomputation, mandatory pagination limits, and response-size caps written into the contract itself. Retry behaviour must fit the allocation too, or it must not exist.
- Budgets set from current behaviour are self-ratifying and never bind. Budgets stated as averages are unenforceable, because a parent's p99 is not assembled from its children's p50s: fan out to six services with independent one-percent tails and roughly six percent of requests meet at least one slow dependency, which makes fan-out width itself a budgeted quantity. And a budget with no owner, no per-endpoint measurement, and no consequence for exceeding it stops constraining anything within a quarter.

## References

- [W3C Server-Timing](https://www.w3.org/TR/server-timing/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
