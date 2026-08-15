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

Measurement literacy before optimization: latency percentiles instead of
averages, histogram buckets chosen around objectives, an objective written so
somebody can act on it. Then the load model — how throughput, concurrency, and
latency relate — and the critical path of a slow distributed request, which
together explain most of 'the service is slow.' Diagnose in increasing order of
stubbornness: the bottleneck-versus-busy evidence question, CPU hotspots,
database query regressions, connection-pool sizing, and whether the cache
actually helps, each assuming the percentile vocabulary. Capacity and economics
form the next tier — the capacity baseline, capacity economics in governance,
noisy neighbours, and load shedding as a performance tool — followed by
experiment integrity: controlled comparisons, production experiments run
safely, and what a CI regression check can honestly prove. Close with contracts
and portfolios — performance budgets in API and dependency design, cross-team
regression contracts, observability across services,
resilience-versus-performance trade-offs, the staff-level portfolio — keeping
the p99 triage and high-cardinality-incident questions as dress rehearsals for
everything above.
