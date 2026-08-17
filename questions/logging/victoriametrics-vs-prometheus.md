---
title: Explain VictoriaMetrics next to Prometheus
theme: logging
difficulty: middle
type: theory
tags: [logging, monitoring, prometheus, cost-optimization, observability]
sources:
  - url: https://docs.victoriametrics.com/
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://prometheus.io/docs/prometheus/latest/storage/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain VictoriaMetrics next to Prometheus

A colleague proposes "replacing Prometheus with VictoriaMetrics". Clarify, at concept level, what VictoriaMetrics is relative to Prometheus and when its cost story is real.

## Answer guide

- VictoriaMetrics is not a different monitoring philosophy: it is a metrics storage and query backend that speaks the Prometheus ecosystem's protocols. Prometheus servers (or vmagent) keep scraping exporters, and the samples are forwarded to VictoriaMetrics via the standard remote-write API, so dashboards, exporters, and alerting rules carry over with minimal change.
- Its query side is Prometheus-compatible: it accepts PromQL through the promoted querying interface and extends it with MetricsQL. Teams usually keep Grafana dashboards untouched and point them at the new datasource, which is why the migration is evaluated as a storage decision rather than a monitoring redesign.
- The cost claim is about scale: VictoriaMetrics is built for high ingestion rates, high cardinality, and long retention, with compression that typically stores the same series in less disk and memory than local TSDB, and cluster-mode partitioning for horizontal scale. Prometheus itself remains the reference single-node design and is often the simpler choice at moderate scale, with its local TSDB and no extra moving parts.
- Treat the decision like the Loki-versus-ELK one: name the pressure first (cardinality growth, multi-year retention, many Prometheus federating into one place) and only then introduce a remote-write backend. If nobody can name the pressure, adding a second storage system just adds operational surface.

## References

- [VictoriaMetrics documentation](https://docs.victoriametrics.com/)
- [Prometheus storage and remote write](https://prometheus.io/docs/prometheus/latest/storage/)
- Further reading (blog): [VictoriaMetrics blog](https://victoriametrics.com/blog/)

## What to learn next

- Official documentation: [VictoriaMetrics key concepts](https://docs.victoriametrics.com/keyconcepts/)
- Manual or specification: [Prometheus storage documentation](https://prometheus.io/docs/prometheus/latest/storage/)
- Maintainer or personal blog: [VictoriaMetrics blog](https://victoriametrics.com/blog/)
- Technical blog: [Prometheus blog](https://prometheus.io/blog/)
- Hands-on guide: [VictoriaMetrics quick start](https://docs.victoriametrics.com/quick-start/)
