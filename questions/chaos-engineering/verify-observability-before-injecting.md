---
title: Verify observability before injecting a fault
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, observability, monitoring, metrics]
sources:
  - url: https://prometheus.io/docs/practices/histograms/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Verify observability before injecting a fault

What has to be instrumented before an experiment is worth running?

## Answer guide

- You need three things in place: an output metric that expresses the steady state in user terms, a signal that proves the fault was actually applied, and enough resolution to see harm before the abort threshold is crossed. Without the second, a green result may simply mean the injection silently failed — a selector that matched nothing looks exactly like perfect resilience.
- Check the mechanics of the metrics themselves. Latency must be a histogram or summary so tail quantiles are meaningful; averaging hides exactly the behaviour a fault produces. Scrape interval, alert `for` duration, and dashboard aggregation window must all be shorter than the experiment, or the graph will still be rising when you declare the run finished. Distributed traces and structured logs identify which dependency absorbed the fault.
- Material constraints: metrics need labels that match the blast radius — per zone, per cell, per tenant, per version — otherwise a severe local failure is diluted into a healthy global average. Retain the raw data long enough to compare the run against its baseline, and record the experiment's start and stop times as annotations so the analysis is not archaeology.
- Failure modes: telemetry that travels over the same path you are breaking, so the evidence disappears exactly when it matters; alerting that is tuned so loosely it never fires; cardinality limits dropping the labels you needed; and treating "no alert fired" as the result rather than checking the metric you named in the hypothesis. If an experiment reveals an observability gap, that gap is a legitimate finding and should be fixed before the fault is widened.

## References

- [Prometheus — histograms and quantiles](https://prometheus.io/docs/practices/histograms/)
- Further reading (blog): [Grafana Labs blog](https://grafana.com/blog/)

## What to learn next

- Official documentation: [Prometheus — histograms and quantiles](https://prometheus.io/docs/practices/histograms/)
- Manual or specification: [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Grafana Labs blog](https://grafana.com/blog/)
- Hands-on guide: [Google SRE book — monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
