---
title: Design a useful service dashboard
theme: observability
difficulty: junior
type: scenario
tags: [observability, monitoring, reliability, troubleshooting, prometheus, pca]
sources:
  - url: https://sre.google/workbook/monitoring/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a useful service dashboard

What should the landing dashboard for an on-call service contain?

## Answer guide

- Put user-impact SLI status, error-budget consumption, request volume, error rate, and latency at the top so an alert can be assessed quickly.
- Add dependency, saturation, deployment, and regional breakdowns that help explain why the SLI changed, with links to the relevant logs and traces.
- Use a consistent time range and make units, aggregation, and missing-data behavior explicit. Design it around a responder's decisions rather than every available metric.
- A dashboard cannot replace an alert runbook or an SLO. Too many panels, averages without percentiles, and no traffic context make an incident harder rather than easier.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE Workbook: Monitoring](https://sre.google/workbook/monitoring/)
- [Further reading: Google SRE—Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)

## What to learn next

- Official documentation: [Grafana dashboards documentation](https://grafana.com/docs/grafana/latest/dashboards/)
- Manual or specification: [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- Maintainer or personal blog: [Brendan Gregg — the USE method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Grafana Labs engineering blog](https://grafana.com/blog/)
- Hands-on guide: [Grafana dashboard design best practices](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/)
