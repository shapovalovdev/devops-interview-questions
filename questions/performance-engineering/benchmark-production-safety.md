---
title: How do you run performance experiments without endangering production?
theme: performance-engineering
difficulty: senior
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you run performance experiments without endangering production?

You need to measure a new caching layer at real traffic volume and the only realistic traffic is production. How do you run that experiment without causing an incident?

## Answer guide

- Choose the least invasive method that still answers the question. In increasing order of risk: shadow or replayed traffic mirrored to the candidate with responses discarded; a dark launch that executes the new path behind a flag but still returns the old result; a canary serving a small share of real requests; and only last, generated load against production. The deciding question is whether you need real request mix, real responses, or real state — each step up buys one of those and costs blast radius.
- Bound the blast radius on three axes at once: traffic fraction, duration, and population. Ramp 1 percent, then 5, then 25, with a defined soak at each step, exclude tenants under contractual latency terms, and hold the canary and its control on identical hardware and identical versions of everything except the change. Always compare the canary against a concurrently running control rather than against yesterday, so a diurnal shift or an unrelated incident cannot be read as the effect of your change.
- Write the abort criteria and the rollback path before the first request: the specific metric, the threshold, the evaluation window (for instance, canary p99 exceeding control by more than a set margin for two consecutive minutes, or any error-budget burn above an agreed rate), and a rollback that is one tested action rather than a deploy. Shadow traffic is only safe if the shadow path provably cannot write — mutations, emails, payments, counters, and fills into a shared cache all leak — and duplicated reads against a shared database are real load on that database.
- A clean 1 percent canary is not evidence for 100 percent: connection-pool ceilings on a shared database, cache-key contention, and fan-out amplification only appear at scale. Fresh instances also flatter the candidate, since they start with empty caches and no accumulated state. Watch the experiment's own instrumentation too — 100 percent trace sampling, an extra profiler, or a debug log level can add more latency than the change removes. Treat the run as a production change: an owner watching, an incident channel open, and the usual freeze and notification rules in force.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
