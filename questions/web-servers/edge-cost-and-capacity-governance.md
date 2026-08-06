---
title: Govern edge cost and capacity across products
theme: web-servers
difficulty: staff
type: scenario
tags: [capacity-planning, cost-optimization, governance, web-server]
sources:
  - url: https://sre.google/sre-book/capacity-planning/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern edge cost and capacity across products

How would you make web-edge capacity and cost decisions transparent across many product teams?

## Answer guide

- Build a demand model that connects traffic, connection duration, response size, cache hit rate, TLS CPU, egress, regional redundancy and dependency capacity to product forecasts. Publish per-service and fleet headroom, unit costs and reliability risks, then review material launches and campaigns before they consume shared capacity.
- Use guardrails such as cacheability standards, payload budgets, rate controls, retention limits and capacity reservations, while retaining an exception process for revenue or safety-critical needs. Track forecast accuracy, saturation events, wasted reservation, hit rate and cost per successful request.
- Cutting cache or regional redundancy solely to reduce spend can violate availability objectives. Shared-cost allocation must not encourage teams to hide traffic or avoid useful telemetry. Forecast normal peaks, failure redistribution and abuse events; average traffic is not an adequate capacity signal.

## References

- [Google SRE: capacity planning](https://sre.google/sre-book/capacity-planning/)
- Further reading (personal blog): [Brendan Gregg on capacity and performance](https://www.brendangregg.com/blog/)

## What to learn next

- Official documentation: [Google SRE capacity planning](https://sre.google/sre-book/capacity-planning/)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Brendan Gregg's blog](https://www.brendangregg.com/blog/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Prometheus capacity planning](https://prometheus.io/docs/practices/instrumentation/)
