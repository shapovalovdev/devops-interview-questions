---
title: Govern telemetry cost across teams
theme: observability
difficulty: staff
type: scenario
tags: [observability, governance, cost-optimization, platform-engineering, prometheus, pca, cnpe, cnpa]
sources:
  - url: https://prometheus.io/docs/practices/naming/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern telemetry cost across teams

How should a platform team reduce rapidly increasing telemetry cost without making teams blind?

## Answer guide

- Attribute ingest, active series, storage, and query cost to service and tenant; identify the highest-cost dimensions and distinguish essential SLI data from diagnostic excess.
- Publish sensible defaults and budgets for label cardinality, log fields, trace sampling, retention, and query limits, with an exception process for justified critical workloads.
- Provide tools that show cost before and after instrumentation changes, and prioritize eliminating unbounded labels, duplicate pipelines, and useless payloads before reducing vital SLO data.
- Chargeback alone becomes a tax without remediation help. Global deletion rules may remove forensic or compliance evidence; pair controls with data classification and documented retention needs.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Prometheus: Metric and label naming](https://prometheus.io/docs/practices/naming/)
- [Further reading: Google SRE Workbook—Monitoring](https://sre.google/workbook/monitoring/)
