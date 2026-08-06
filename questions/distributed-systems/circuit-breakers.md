---
title: Use a circuit breaker without masking failure
theme: distributed-systems
difficulty: middle
type: troubleshooting
tags: [reliability, availability, troubleshooting]
sources:
  - url: https://sre.google/sre-book/addressing-cascading-failures/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use a circuit breaker without masking failure

When should a caller stop sending work to an unhealthy dependency, and how should it recover?

## Answer guide

- Open the circuit based on a meaningful error or latency signal over a bounded window, then fail fast or use a declared degraded response. Protect the dependency with concurrency limits and timeouts as well; a breaker is not a replacement for correct capacity and overload control.
- Move to half-open using a small, controlled probe budget and close only after evidence of recovery. Expose state, reason, and rejected request counts so operators can distinguish a dependency outage from a local policy decision.
- A shared breaker can create a new single point of failure, while per-client breakers can recover in a synchronized stampede. Incorrect fallback data, bad thresholds, and silently open circuits can hide a prolonged outage and cause data correctness problems.

## References

- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Further reading (personal blog): [Michael Nygard: circuit breakers](https://www.michaelnygard.com/blog/2007/03/the-circuit-breaker-pattern.html)

## What to learn next

- Official documentation: [Envoy circuit breaking](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Michael Nygard's blog](https://www.michaelnygard.com/blog/)
- Technical blog: [AWS Builders' Library: load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
- Hands-on guide: [Envoy overload manager](https://www.envoyproxy.io/docs/envoy/latest/configuration/operations/overload_manager/overload_manager)
