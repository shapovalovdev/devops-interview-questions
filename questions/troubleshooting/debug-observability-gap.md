---
title: Debug an observability gap during an active incident
theme: troubleshooting
difficulty: senior
type: troubleshooting
tags: [troubleshooting, observability, monitoring, logs, metrics]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Debug an observability gap during an active incident
## Answer guide
- State precisely what decision lacks evidence: impact, failing cohort, dependency, or recovery. Use independent signals such as synthetic probes, access logs, audit events, and client telemetry before adding high-cardinality instrumentation under load.
- Validate telemetry pipeline health separately from service health: sampling, clocks, exporters, collectors, storage quotas, query permissions, and dashboard variables can all make healthy events invisible.
- Add temporary, privacy-reviewed and rate-bounded instrumentation only when it changes a decision, then remove or formalize it. Do not log secrets, identifiers unnecessarily, or turn on expensive debug logging fleetwide during saturation.
## References
- [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Further reading (blog): [Charity Majors — observability](https://charity.wtf/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Hands-on guide: [Prometheus instrumentation](https://prometheus.io/docs/practices/instrumentation/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Honeycomb blog](https://www.honeycomb.io/blog)
