---
title: Design an Istio resilience policy
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, istio, kubernetes, ica, traffic-management, reliability]
sources:
  - url: https://istio.io/latest/docs/concepts/traffic-management/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design an Istio resilience policy

How would you introduce timeouts, retries, and outlier detection for a flaky downstream service without worsening an outage?

## Answer guide

- Set an end-to-end request deadline from the caller's user-facing objective, then allocate bounded connection, attempt, and retry time inside it. Configure retries only for operations that are safe to retry or have an idempotency design, and limit retry count, conditions, and per-try timeout so retrying cannot outlive the caller's useful work.
- Use connection-pool and outlier-detection policy only after measuring downstream capacity and failure behavior. Ejection can protect callers from a consistently failing endpoint, but it reduces available capacity and must leave enough healthy instances to meet demand; failover needs a compatible, tested alternate destination.
- Observe retry volume, timeout rate, ejections, saturation, and user outcomes during a canary. Mesh resilience settings cannot fix a broken dependency, and aggressive retries or ejections can create retry storms, overload healthy replicas, or turn a localized failure into an availability incident.

## References

- [Istio: Traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- [Istio: Request timeouts](https://istio.io/latest/docs/tasks/traffic-management/request-timeouts/)
- Further reading (blog): [Istio: Resilience and failure handling](https://istio.io/latest/blog/2017/0.1-using-istio/)
