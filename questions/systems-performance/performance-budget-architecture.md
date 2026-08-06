---
title: How do you use performance budgets in architecture governance?
theme: systems-performance
difficulty: staff
type: theory
tags: [performance, capacity-planning, governance, reliability]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you use performance budgets in architecture governance?

## Answer guide

- Translate user objectives into explicit latency, throughput, concurrency, availability, and cost envelopes at key request boundaries. Allocate budgets across dependencies with a measurable owner and testable degradation behavior.
- Require design changes to state workload assumptions, expected resource demand, observability, and rollback plan. Review real percentile data and saturation during launch, then update assumptions after traffic or dependency changes.
- Budgets guide trade-offs rather than become vanity targets. Strict per-hop allocations can fail under correlated tails, and optimizing one component may increase total cost or reduce resilience; retain system-level outcomes as the decision authority.

## References

- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Brendan Gregg — Performance Methodologies](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [Google SLO guidance](https://sre.google/sre-book/service-level-objectives/)
- Manual or specification: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Maintainer or personal blog: [Brendan Gregg — methodology](https://www.brendangregg.com/methodology.html)
- Technical blog: [Stripe Engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [Prometheus alerting](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
