---
title: Explain Loki architecture and label design
theme: logging
difficulty: middle
type: theory
tags: [logging, loki, grafana, observability]
sources:
  - url: https://grafana.com/docs/loki/latest/get-started/architecture/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://grafana.com/docs/loki/latest/get-started/labels/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://grafana.com/docs/loki/latest/get-started/labels/cardinality/
    source_type: official-docs
    verified_on: 2026-08-17
---

# Explain Loki architecture and label design

Walk the path of a log line from a collector such as Grafana Alloy or Promtail through Loki into Grafana, and explain why the choice of labels decides both the size of the index and the cost of every query.

## Answer guide

- A collector (Grafana Alloy, the deprecated Promtail, the Docker driver, or the OpenTelemetry Collector) tails, parses, and enriches log lines, then pushes them to Loki's distributor; the distributor hashes each stream's label set against a consistent-hash ring and replicates the write to ingesters, which acknowledge after a quorum so a lost replica does not lose the line.
- The ingester appends lines to a compressed chunk per stream and flushes filled chunks to cheap object storage (S3, GCS, Azure); the index stores only the mapping from label sets to chunks. On read, the query frontend splits a LogQL query into shards that queriers fan out across ingesters for recent data and the object store for cold data, so query speed is bought with parallelism rather than a fat index.
- Loki indexes only labels, never log content: every unique combination of label names and values is a stream. Labels must therefore be low-cardinality descriptors of the log's source (cluster, namespace, app, environment), bounded in value, and few — roughly ten to fifteen is the working ceiling.
- High cardinality (an `ip`, `user_id`, or `pod_name` label, or too many labels) multiplies streams, bloats the index, and flushes thousands of tiny chunks, which is the classic way to make Loki slow and expensive. Content that changes per line belongs in structured metadata or in the line itself, reachable with line filters like `|= "error"` and parsed at query time with `| json`.

## References

- [Loki architecture](https://grafana.com/docs/loki/latest/get-started/architecture/)
- [Understand labels](https://grafana.com/docs/loki/latest/get-started/labels/)
- [Cardinality in Loki](https://grafana.com/docs/loki/latest/get-started/labels/cardinality/)
- Further reading (blog): [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)

## What to learn next

- Official documentation: [Loki architecture](https://grafana.com/docs/loki/latest/get-started/architecture/)
- Manual or specification: [Understand labels](https://grafana.com/docs/loki/latest/get-started/labels/)
- Maintainer or personal blog: [Loki: Prometheus-inspired, open source logging for cloud natives](https://grafana.com/blog/2018/12/12/loki-prometheus-inspired-open-source-logging-for-cloud-natives/)
- Technical blog: [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)
- Hands-on guide: [Send data to Loki and query it back](https://grafana.com/docs/loki/latest/send-data/)
