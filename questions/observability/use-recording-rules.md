---
title: Use recording rules for expensive PromQL
theme: observability
difficulty: middle
type: scenario
tags: [observability, monitoring, prometheus, reliability, pca]
sources:
  - url: https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use recording rules for expensive PromQL

When should you create a Prometheus recording rule, and how do you operate it safely?

## Answer guide

- Use a recording rule to precompute a repeatedly used or computationally expensive query, especially a shared SLI or dashboard aggregate.
- Give the derived series a clear name, preserve only labels consumers need, set an appropriate evaluation interval, and version and test rules with the service configuration.
- Validate syntax with `promtool`, observe evaluation duration and missed iterations, and compare the recorded output to the source query before switching alerts or dashboards.
- Recording rules add storage and can hide a changed semantic behind a familiar name. Do not use them to paper over excessive raw metric cardinality or a wrong SLI definition.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Prometheus: Defining recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
- [Further reading: Prometheus recording-rule naming](https://prometheus.io/docs/practices/rules/)
