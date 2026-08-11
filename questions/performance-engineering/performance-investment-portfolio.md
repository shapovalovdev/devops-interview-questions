---
title: How would a staff engineer prioritize a portfolio of performance work?
theme: performance-engineering
difficulty: staff
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How would a staff engineer prioritize a portfolio of performance work?

You have four engineers for a quarter and eleven proposed performance projects competing for them. How do you decide what gets funded, and how do you defend the decision afterwards?

## Answer guide

- Rank by expected user-visible or financial benefit per engineer-week, with the estimate written down before the work starts so it can be checked against the outcome. Convert every proposal into the same unit — error budget recovered, share of requests brought under the objective, or infrastructure cost removed — and discount each by confidence. A change that takes 100 ms off 40 percent of requests usually beats halving a path that 2 percent of traffic touches, and stating it arithmetically keeps the decision out of the hands of whoever argues hardest.
- Profile the portfolio the way you would profile a service. Aggregate where end-to-end time and cost genuinely go across the fleet before accepting proposals, because most candidate lists are assembled from what individual engineers happened to notice. Amdahl's law bounds every entry: a component worth 15 percent of the critical path caps its own win at 15 percent however elegant the fix. Prefer work that removes work — a query, a fan-out hop, a serialization round trip — over work that makes the same work faster, since removed work cannot regress later.
- Reserve part of the budget for capability rather than fixes: the missing per-tenant metric, a profiler that can run safely in production, a benchmark harness with a versioned dataset. A portfolio with no measurement investment reproduces the same unresolvable argument next quarter. Price carrying cost too, because a cache, a shard, or a precomputation pipeline adds permanent operational surface and its benefit has to clear both the build cost and that ongoing cost. Then sequence for risk, shipping reversible and independently deployable items first.
- Funding by loudest recent incident produces a quarter of tail-chasing; funding a rewrite produces a quarter with nothing shipped and no measurement either way. Benefits claimed but never re-measured get counted again in the next planning round, so make a post-hoc measurement against the pre-registered estimate part of the definition of done. And an item that improves an internal metric without moving a user-facing objective or a cost line should lose to one that does, however satisfying the internal number is.

## References

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
