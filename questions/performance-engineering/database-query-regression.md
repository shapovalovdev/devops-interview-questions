---
title: How do you investigate a database query performance regression?
theme: performance-engineering
difficulty: middle
type: troubleshooting
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://www.postgresql.org/docs/current/using-explain.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you investigate a database query performance regression?

A query that returned in 40 ms yesterday now takes six seconds, and no application code was deployed. How do you find out what changed?

## Answer guide

- Get the plan the database actually used rather than the one it predicts. `EXPLAIN (ANALYZE, BUFFERS)` on PostgreSQL reports estimated versus actual rows for every node, and a large discrepancy there explains most plan flips — the planner chose a nested loop expecting five rows and received five hundred thousand. Cross-check `pg_stat_statements` to confirm this statement is the regression, when its mean time moved, and whether call volume changed at the same moment.
- Plans change without code changing. Common causes are table growth crossing a cost threshold, statistics that went stale after a bulk load before autovacuum caught up, an index created or dropped by another team, index or heap bloat making a scan look cheaper, and parameter sniffing — PostgreSQL may switch a prepared statement from a custom plan to a generic one after five executions. Reproduce with the parameter values the slow calls actually used, because a plan is usually only bad for part of the value distribution.
- `EXPLAIN ANALYZE` executes the statement, so wrap anything that writes in a transaction you roll back, and remember that per-row timing instrumentation inflates reported time on plans with many rows — use `TIMING OFF` when that dominates, and enable `track_io_timing` if you need I/O attribution. A plan captured on a replica or a staging copy with different statistics, `work_mem`, or major version proves nothing about the primary. Prefer statistics fixes such as `ANALYZE`, a higher `default_statistics_target`, or extended statistics on correlated columns before reaching for a new index.
- Adding an index to force the old plan back taxes every write on that table and can silently change plans for statements nobody checked. Confirm the query is executing rather than waiting first: a lock wait shows up in `pg_stat_activity.wait_event_type`, not in the plan, and no amount of index tuning fixes it. Keep the slow plan captured so the improvement is provable, and weigh the fix against total time rather than per-call time — a six-second query invoked twice an hour is a different priority from one on the request path.

## References

- [PostgreSQL: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
