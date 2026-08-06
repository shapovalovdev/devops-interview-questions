---
title: Choose timeouts, retries, and backoff
theme: distributed-systems
difficulty: junior
type: troubleshooting
tags: [reliability, latency, troubleshooting]
sources:
  - url: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose timeouts, retries, and backoff

How should a service retry a remote dependency without amplifying an incident?

## Answer guide

- Set deadlines from measured end-to-end latency and the caller's remaining budget, then propagate cancellation to downstream work. Retry only failures that are demonstrably transient and only operations whose effects are safe to repeat or protected by idempotency.
- Use bounded attempts, exponential backoff with jitter, and a retry budget or admission control. Instrument attempted, successful, abandoned, and late responses separately so that retries do not make an unhealthy dependency appear healthy.
- Avoid synchronized retries and nested retry loops: they multiply load after a dependency slows. Too-short timeouts cause false failures; too-long ones exhaust pools, and unlimited retries can turn a partial outage into congestion collapse.

## References

- [AWS Builders' Library: timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- Further reading (personal blog): [Marc Brooker: jitter](https://brooker.co.za/blog/2015/03/21/backoff.html)

## What to learn next

- Official documentation: [gRPC deadlines](https://grpc.io/docs/guides/deadlines/)
- Manual or specification: [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- Maintainer or personal blog: [Marc Brooker: backoff](https://brooker.co.za/blog/2015/03/21/backoff.html)
- Technical blog: [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Hands-on guide: [Envoy retry policy](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_routing#retry-policy)
