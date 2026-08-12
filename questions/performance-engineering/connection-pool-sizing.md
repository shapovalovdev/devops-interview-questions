---
title: How do you size a client connection pool safely?
theme: performance-engineering
difficulty: middle
type: scenario
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you size a client connection pool safely?

A service runs 200 request-handling threads against one PostgreSQL primary with a 200-connection pool, and p99 latency is climbing. How do you choose the pool size, and how do you tell pool exhaustion from a slow query?

## Answer guide

- Size the pool for the concurrency the database can usefully absorb, not for the concurrency the application offers. Little's law gives the floor: 500 queries per second holding a connection for 4 ms is 2 connections in flight on average, and headroom for variance and bursts puts a realistic pool in the low tens. HikariCP's sizing guidance lands in the same place from the other direction, deriving a small number from core count plus effective storage parallelism rather than from thread count.
- Beyond the server's real parallelism, extra connections add context switching, buffer and lock contention, and per-connection memory instead of throughput — PostgreSQL forks a backend per connection and `work_mem` is charged per sort or hash per backend. A pool smaller than the thread pool is the point, not a limitation: it converts overload into a short, measurable wait at a place that has a timeout and a metric, rather than letting every in-flight query degrade together inside the database.
- Pool size is per instance and multiplies by replica count against `max_connections`; 40 pods holding 50 connections each needs 2000 server slots, and autoscaling raises that ceiling silently. That arithmetic is the usual reason to put PgBouncer in transaction pooling mode in front, which in turn forbids session-scoped state — `SET` outside a transaction, session advisory locks, and server-side prepared statements need explicit handling. Also keep the acquisition timeout well below the request deadline, or a caller gives up while still holding its slot in the queue.
- The signatures differ cleanly. Exhaustion adds latency before any SQL runs: pool wait time and pending-acquire count rise while database CPU and per-statement mean time in `pg_stat_statements` stay flat. A slow query is the mirror image — flat pool wait, rising statement time, a changed plan. A third case is a connection pinned by a transaction left `idle in transaction`, which starves the pool with no slow query anywhere. Enlarging the pool to relieve exhaustion usually just relocates the queue into the database, where nothing bounds it.

## References

- [HikariCP: About pool sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
