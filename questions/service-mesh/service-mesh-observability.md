---
title: Use mesh telemetry without mistaking it for complete observability
theme: service-mesh
difficulty: junior
type: scenario
tags: [service-mesh, istio, observability, monitoring, logging, reliability]
sources:
  - url: https://istio.io/latest/docs/concepts/observability/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Use mesh telemetry without mistaking it for complete observability

What request information can a service mesh add, and what still needs application instrumentation?

## Answer guide

- A mesh can emit traffic-oriented metrics, access logs, and trace context or spans around captured requests. This helps correlate source, destination, response code, latency, TLS, and policy behavior across services.
- Application instrumentation remains necessary for business outcomes, database calls, queue work, internal errors, meaningful trace attributes, and operations that never traverse the mesh. Sampling and privacy requirements must be designed explicitly.
- Build dashboards from user-facing indicators and verify label cardinality, sampling, retention, and sensitive-data handling before enabling verbose telemetry broadly. High-cardinality labels or full request logging can increase cost and leak data while still failing to explain an application bug.

## References

- [Istio observability concepts](https://istio.io/latest/docs/concepts/observability/)
- [Istio standard metrics](https://istio.io/latest/docs/reference/config/metrics/)
- Further reading (blog): [Istio: Observability in a service mesh](https://istio.io/latest/blog/2020/addon-rework/)
