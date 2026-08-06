---
title: Explain what a service mesh does and does not replace
theme: service-mesh
difficulty: junior
type: theory
tags: [service-mesh, istio, kubernetes, networking, security, observability]
sources:
  - url: https://istio.io/latest/docs/overview/what-is-istio/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Explain what a service mesh does and does not replace

What problem does a service mesh solve, and which application and platform controls still remain necessary?

## Answer guide

- A service mesh provides a consistent traffic layer between services. Its proxies or node-level components can apply service identity, mutual TLS, routing policy, telemetry, and selected resilience behavior without every service implementing the same plumbing.
- It complements rather than replaces application authentication and authorization, input validation, secure code, Kubernetes admission controls, NetworkPolicy, DNS, load-balancer configuration, and an incident process. The exact capabilities depend on the mesh and data-plane mode.
- Start with a clear problem such as workload identity or request telemetry, then enroll a small service boundary and measure behavior. A mesh adds components, configuration, and failure modes; adopting it for every cluster without ownership and observability can make simple traffic failures harder to diagnose.

## References

- [Istio: What is Istio?](https://istio.io/latest/docs/overview/what-is-istio/)
- [Linkerd: What is a service mesh?](https://linkerd.io/2.18/overview/)
- Further reading (blog): [Buoyant: Service mesh resources](https://buoyant.io/blog/)
