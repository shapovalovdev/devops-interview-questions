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
  - url: https://linkerd.io/2.18/reference/service-profiles/
    source_type: official-docs
    verified_on: 2026-08-16
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Design an Istio resilience policy

How would you introduce timeouts, retries, and outlier detection for a flaky downstream service without worsening an outage?

## Answer guide

- Set an end-to-end request deadline from the caller's user-facing objective, then allocate bounded connection, attempt, and retry time inside it. Configure retries only for operations that are safe to retry or have an idempotency design, and limit retry count, conditions, and per-try timeout so retrying cannot outlive the caller's useful work.
- Use connection-pool and outlier-detection policy only after measuring downstream capacity and failure behavior. Ejection can protect callers from a consistently failing endpoint, but it reduces available capacity and must leave enough healthy instances to meet demand; failover needs a compatible, tested alternate destination.
- Observe retry volume, timeout rate, ejections, saturation, and user outcomes during a canary. Mesh resilience settings cannot fix a broken dependency, and aggressive retries or ejections can create retry storms, overload healthy replicas, or turn a localized failure into an availability incident.
- Retry and timeout policy has direct equivalents: Linkerd expresses per-route retry budgets and timeouts in ServiceProfiles, and Gateway API's BackendTrafficPolicy standardizes the same attachment to backends — 'retries must not outlive the caller's deadline' holds in each.

## References

- [Istio: Traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- [Istio: Request timeouts](https://istio.io/latest/docs/tasks/traffic-management/request-timeouts/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
- [Linkerd: service profiles](https://linkerd.io/2.18/reference/service-profiles/)
