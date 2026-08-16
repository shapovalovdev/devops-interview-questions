# Performance engineering related materials

Use a measured workload and an explicit service objective before selecting a
tool. This page deliberately avoids linking unauthorized copies of commercial
performance books; the linked JMeter manual is a lawful, free hands-on guide.

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Brendan Gregg — Performance](https://www.brendangregg.com/perf.html)
- Technical blog: [Cloudflare Blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Apache JMeter user manual](https://jmeter.apache.org/usermanual/index.html)

## Suggested study order

Measurement literacy before optimization, diagnosis before capacity and
economics, and contracts and portfolios to close.

1. [Why use latency percentiles instead of an average?](../../questions/performance-engineering/measure-latency-percentiles.html)
    — Latency percentiles instead of averages is the literacy the whole Theme
    stands on.
2. [How should an engineer choose latency histogram buckets?](../../questions/performance-engineering/choose-histogram-buckets.html)
    — Histogram buckets chosen around objectives make the percentiles
    measurable.
3. [What makes a performance objective actionable?](../../questions/performance-engineering/define-performance-objectives.html)
    — An objective somebody can act on turns measurement into actual work.
4. [How do you select a load model for a production-facing service?](../../questions/performance-engineering/select-load-test-model.html)
    — The load model decides what the numbers will even mean before they are
    gathered.
5. [How are throughput, concurrency, and latency related during a load test?](../../questions/performance-engineering/throughput-and-concurrency.html)
    — How throughput, concurrency, and latency relate explains most reports that
    the service is slow.
6. [How do you find the critical path of a slow distributed request?](../../questions/performance-engineering/trace-critical-path.html)
    — The critical path of a slow distributed request localizes the blame
    honestly.
7. [What evidence distinguishes a bottleneck from a busy component?](../../questions/performance-engineering/identify-bottleneck-signals.html)
    — Bottleneck versus busy is the evidence question the diagnostic tier opens
    with.
8. [How do you investigate a CPU hotspot without optimizing the wrong code?](../../questions/performance-engineering/profile-cpu-hotspots.html)
    — CPU hotspots follow, investigated without optimizing the wrong code.
9. [How do you investigate a database query performance regression?](../../questions/performance-engineering/database-query-regression.html)
    — Query regressions are the database tier of the same diagnosis.
10. [How do you size a client connection pool safely?](../../questions/performance-engineering/connection-pool-sizing.html)
    — Pool sizing is the concurrency question the load model framed earlier.
11. [How do you evaluate whether a cache improves a service?](../../questions/performance-engineering/cache-performance-evaluation.html)
    — Whether the cache actually helps is asked before crediting it with the
    improvement.
12. [How would you establish a capacity baseline for a service?](../../questions/performance-engineering/capacity-baseline-design.html)
    — The capacity tier opens with a baseline that survives scrutiny.
13. [How should capacity economics influence performance governance?](../../questions/performance-engineering/capacity-economics-governance.html)
    — Capacity economics influence what the baseline can honestly recommend.
14. [How do you diagnose and mitigate noisy-neighbor performance?](../../questions/performance-engineering/multi-tenant-noisy-neighbor.html)
    — Noisy neighbours are the multi-tenant version of the capacity problem.
15. [When and how should a service shed load?](../../questions/performance-engineering/load-shedding-design.html)
    — Load shedding is a performance tool here, not only an emergency brake.
16. [What must stay controlled when you compare two performance runs?](../../questions/performance-engineering/benchmark-control-variables.html)
    — Experiment integrity opens with comparisons whose variables stayed
    controlled.
17. [How do you run performance experiments without endangering production?](../../questions/performance-engineering/benchmark-production-safety.html)
    — Production experiments run safely or they do not run at all.
18. [What should a performance regression check in CI actually prove?](../../questions/performance-engineering/performance-regression-ci.html)
    — A CI regression check must prove only what it can honestly prove.
19. [How do performance budgets change API and dependency design?](../../questions/performance-engineering/performance-budget-api.html)
    — Contracts open with performance budgets shaping API and dependency design.
20. [What cross-team contracts prevent performance regressions in a platform?](../../questions/performance-engineering/cross-team-performance-contracts.html)
    — Cross-team contracts keep regressions from crossing team borders
    unnoticed.
21. [How do you design a performance observability strategy across many services?](../../questions/performance-engineering/performance-observability-strategy.html)
    — Observability across services watches those contracts actually hold.
22. [How should a staff engineer evaluate resilience versus performance trade-offs?](../../questions/performance-engineering/resilience-performance-tradeoffs.html)
    — Resilience versus performance is the staff trade the contracts just
    priced.
23. [How would a staff engineer prioritize a portfolio of performance work?](../../questions/performance-engineering/performance-investment-portfolio.html)
    — The staff-level portfolio prioritizes all the work the contracts surfaced.
24. [How do you triage a p99 latency regression?](../../questions/performance-engineering/tail-latency-triage.html)
    — The p99 triage stays last as a dress rehearsal for the whole diagnostic
    tier above.
25. [Why can high-cardinality metrics become a performance incident?](../../questions/performance-engineering/avoid-metric-cardinality.html)
    — The high-cardinality incident is the other dress rehearsal, turning
    measurement itself into the outage.
