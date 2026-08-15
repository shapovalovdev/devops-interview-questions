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
  - url: https://learn.microsoft.com/azure/load-balancer/load-balancer-custom-probe-overview
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/load-balancing/docs/health-checks
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design a cloud load-balancer health check

What should an Application Load Balancer health check prove before it receives production traffic?

## Answer guide

- Use a cheap endpoint that proves the instance can serve the dependency level required for safe traffic. Configure protocol, path, port, success codes, interval, timeout, and healthy/unhealthy thresholds explicitly.
- Keep liveness distinct from readiness. A process can be alive while unable to serve requests because it is warming, has no required configuration, or has exhausted a critical dependency.
- Monitor unhealthy target count and health-check failure reasons, then test deployment and dependency failures. Ensure the target group spans enough zones and capacity to tolerate removal of targets.
- Do not make the probe a deep, expensive transaction that can amplify an outage; conversely, a probe that only returns 200 from a stuck process creates false confidence.
- Probe design travels intact: Azure Load Balancer health probes and Google Cloud health checks expose the same interval, timeout, and unhealthy-threshold knobs, and Kubernetes readiness probes carry the identical liveness-versus-readiness distinction that keeps warming targets out of rotation.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [ALB target group health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
- [Further reading: ALB target health status](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/check-target-health.html)
- [Azure Load Balancer — health probe overview](https://learn.microsoft.com/azure/load-balancer/load-balancer-custom-probe-overview)
- [Google Cloud — health checks overview](https://cloud.google.com/load-balancing/docs/health-checks)

## What to learn next

- Official documentation: [ALB target-group health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
- Manual or specification: [ALB target health status](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/check-target-health.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- Hands-on guide: [AWS load-balancing workshops](https://catalog.workshops.aws/elastic-load-balancing/en-US)
