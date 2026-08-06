---
title: Stop a cascading failure while preserving useful traffic
theme: troubleshooting
difficulty: middle
type: scenario
tags: [troubleshooting, reliability, dependencies, capacity-planning, incident-response]
sources:
  - url: https://sre.google/sre-book/addressing-cascading-failures/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Stop a cascading failure while preserving useful traffic
## Answer guide
- Identify the overloaded critical resource and feedback loop: retries, fan-out, queueing, connection exhaustion, or a dependency slowdown. Prioritize a small set of critical user operations using measured error and saturation signals.
- Shed optional traffic, cap retries, apply load balancing or admission control, and degrade nonessential features. Roll out mitigations gradually because a global toggle can shift overload to an adjacent service.
- Verify that queues drain and that recovery does not cause a reconnection stampede. Afterwards test the guardrails and capacity assumptions; a one-time capacity increase is not a complete cascade prevention strategy.
## References
- [Google SRE Book — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [Google SRE Book — Handling Overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Marc Brooker — distributed systems](https://brooker.co.za/blog/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [Envoy circuit breaking](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking)
- Official guide: [Kubernetes HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- Personal technical blog: [Marc Brooker](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders’ Library](https://aws.amazon.com/builders-library/)
