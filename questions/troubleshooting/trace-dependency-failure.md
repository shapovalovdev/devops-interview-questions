---
title: Trace a dependency failure across service boundaries
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, dependencies, logs, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/effective-troubleshooting/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Trace a dependency failure across service boundaries

## Answer guide

- Identify the failed operation, caller, dependency, endpoint, timeout, error class, and affected traffic cohort. Follow a request or correlation ID across logs and traces; do not infer the failed hop from an HTTP 500 alone.
- Compare dependency latency, error rate, saturation, and connection pools with the caller’s retry and timeout behavior. A healthy dependency dashboard can still hide a specific tenant, region, credential, or protocol failure.
- Bound retries, shed optional work, and use documented fallback only if it preserves correctness. Unbounded retries and synchronized reconnects amplify an outage; capture evidence before escalating to the owning team.

## References

- [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Google SRE Book — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Further reading (blog): [Cindy Sridharan — Distributed systems](https://copyconstruct.medium.com/)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [OpenTelemetry context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- Hands-on guide: [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Cindy Sridharan](https://copyconstruct.medium.com/)
- Technical blog: [Grafana Labs blog](https://grafana.com/blog/)
