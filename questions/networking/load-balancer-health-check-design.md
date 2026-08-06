---
title: Design load-balancer health checks
theme: networking
difficulty: senior
type: scenario
tags: [networking, http, reliability, availability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9110.html
    source_type: standard
    verified_on: 2026-08-06
---

# Design load-balancer health checks

How should health checks avoid both sending traffic to broken instances and removing healthy ones during a dependency incident?

## Answer guide

- Define what the check proves. A TCP check proves a listener can complete a handshake; an HTTP check can prove routing and a bounded application response; neither necessarily proves every downstream dependency is healthy.
- Use distinct liveness, readiness/traffic, and deep diagnostic signals where the platform permits. Make the traffic-admission check fast, authenticated only when necessary, and independent enough that a shared dependency outage does not evict all otherwise healthy instances.
- Set interval, timeout, and success/failure thresholds from service recovery and failure-detection objectives. Short aggressive checks can create synchronized eviction and reconnection storms; long thresholds delay removal of truly failed endpoints.
- Monitor healthy-target count, check latency/status, client errors, and balancing distribution. Test failure modes including slow responses, partial zones, and connection draining before treating a status endpoint as production protection.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 9110: HTTP semantics and status codes](https://www.rfc-editor.org/rfc/rfc9110.html)
- [AWS Elastic Load Balancing health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
