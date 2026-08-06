---
title: Design a cloud load-balancer health check
theme: cloud
difficulty: middle
type: scenario
tags: [aws, cloud, availability, reliability, monitoring]
sources:
  - url: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a cloud load-balancer health check

What should an Application Load Balancer health check prove before it receives production traffic?

## Answer guide

- Use a cheap endpoint that proves the instance can serve the dependency level required for safe traffic. Configure protocol, path, port, success codes, interval, timeout, and healthy/unhealthy thresholds explicitly.
- Keep liveness distinct from readiness. A process can be alive while unable to serve requests because it is warming, has no required configuration, or has exhausted a critical dependency.
- Monitor unhealthy target count and health-check failure reasons, then test deployment and dependency failures. Ensure the target group spans enough zones and capacity to tolerate removal of targets.
- Do not make the probe a deep, expensive transaction that can amplify an outage; conversely, a probe that only returns 200 from a stuck process creates false confidence.

## References

- [ALB target group health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
- [Further reading: ALB target health status](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/check-target-health.html)
