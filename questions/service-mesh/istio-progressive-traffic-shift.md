---
title: Shift traffic progressively with Istio
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, istio, kubernetes, ica, traffic-management, deployment, reliability]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/traffic-shifting/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Shift traffic progressively with Istio

How would you run a canary release using weighted Istio traffic shifting?

## Answer guide

- Deploy and prove the candidate version independently, then route a small percentage of traffic to a DestinationRule subset using a VirtualService. Keep the stable route explicit, ensure both versions meet readiness requirements, and distinguish an HTTP request split from a guarantee that every user or long-lived connection sees the same version.
- Establish pre-defined promotion and rollback signals: user-facing errors, latency, saturation, business correctness, and mesh policy failures. Increase weights only after an observation window that covers enough representative traffic; use header or cookie matching only when its stickiness and privacy implications are understood.
- Revert the routing weight first when a canary fails, preserve evidence, and investigate the application and dependency behavior. A successful traffic shift is not a database migration strategy: incompatible schemas, shared caches, sessions, and asynchronous consumers require their own compatibility and rollback design.

## References

- [Istio: Traffic shifting](https://istio.io/latest/docs/tasks/traffic-management/traffic-shifting/)
- [Istio: Request routing](https://istio.io/latest/docs/tasks/traffic-management/request-routing/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
