---
title: Compare Loki and ELK for log platform cost
theme: logging
difficulty: middle
type: theory
tags: [logging, loki, grafana, cost-optimization]
sources:
  - url: https://grafana.com/docs/loki/latest/get-started/architecture/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
    source_type: official-docs
    verified_on: 2026-08-17
---

# Compare Loki and ELK for log platform cost

Your team is choosing between an ELK stack (Elasticsearch, Logstash/Beats, Kibana) and Grafana Loki for log aggregation. Compare the two cost models and name the situations where ELK still wins.

## Answer guide

- The core trade is indexing: Elasticsearch builds and stores a rich inverted index over every field of every line, which makes arbitrary full-text search fast but typically costs as much to store and keep in memory as the logs themselves; Loki indexes only a small set of labels and pushes compressed chunks into object storage, so its static footprint is usually an order of magnitude smaller for the same log volume.
- With ELK you pay that index cost continuously, whether or not anyone queries; with Loki the fixed cost is low and query performance is bought at runtime by sharding queries across more queriers, which suits the "metrics alert, then grep the logs" debugging flow of Prometheus-first teams.
- Operationally, a large Elasticsearch cluster asks for tuned JVM nodes, careful shard and lifecycle management, and warm/hot tiering, while Loki's simple-scalable deployment leans on an object store and a handful of stateless services — but Loki then asks for label discipline, because high cardinality destroys its cost advantage.
- ELK still wins when the primary workload is exploratory full-text analytics over unstructured logs, Kibana-style dashboards and aggregations on arbitrary fields, frequent relevance-ranked search, or compliance-grade retention with per-field security; teams that cannot constrain their label design or that need instant arbitrary-field search should stay on a full-text engine rather than fight Loki's model.

## References

- [Loki architecture](https://grafana.com/docs/loki/latest/get-started/architecture/)
- [Elasticsearch reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- Further reading (blog): [Loki: Prometheus-inspired, open source logging for cloud natives](https://grafana.com/blog/2018/12/12/loki-prometheus-inspired-open-source-logging-for-cloud-natives/)

## What to learn next

- Official documentation: [Loki architecture](https://grafana.com/docs/loki/latest/get-started/architecture/)
- Manual or specification: [Elasticsearch reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- Maintainer or personal blog: [Grafana Labs blog](https://grafana.com/blog/)
- Technical blog: [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)
- Hands-on guide: [Send data to Loki and query it back](https://grafana.com/docs/loki/latest/send-data/)
