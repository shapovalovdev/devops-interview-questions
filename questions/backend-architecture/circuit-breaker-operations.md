---
title: Operate a circuit breaker
theme: backend-architecture
difficulty: middle
type: troubleshooting
tags: [reliability, availability, monitoring]
sources:
  - url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
    source_type: official-docs
    verified_on: 2026-08-06
---

# Operate a circuit breaker

What problem does a circuit breaker solve, and what must be configured around it?

## Answer guide

- A circuit breaker stops sending likely-to-fail calls to a dependency after a measured failure threshold, then probes recovery after a controlled interval. It protects caller resources and gives a failing dependency room to recover.
- Define the operation scope, failure signals, rolling window, open duration, half-open probe concurrency, fallback behavior, and alerts. Exclude caller validation errors from dependency-health calculations and expose state changes in telemetry.
- A breaker is not a substitute for capacity or a correct timeout. An overly broad breaker can take healthy operations down, while an unbounded fallback can corrupt data; simulate dependency latency, recovery, and uneven instance state.

## References

- [Microsoft: circuit breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
- Further reading (blog): [Netflix: Hystrix](https://netflixtechblog.com/hystrix-dashboard-turbine-stream-aggregator-60985a2e51b6)

## What to learn next

- Official documentation: [Envoy circuit breaking](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [Envoy fault injection sandbox](https://www.envoyproxy.io/docs/envoy/latest/start/sandboxes/fault-injection)
