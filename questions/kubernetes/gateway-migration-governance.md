---
title: Govern a migration from Ingress to Gateway API
theme: kubernetes
difficulty: staff
type: scenario
tags: [kubernetes, networking, deployment, governance, reliability]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/gateway/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern a migration from Ingress to Gateway API

How would you lead a migration from controller-specific Ingress configuration to Gateway API without disrupting customers?

## Answer guide

- Inventory routes, TLS, authentication, annotations, traffic policy, ownership, and controller-specific behavior before selecting supported Gateway API implementations and conformance expectations.
- Establish reusable Gateway and Route ownership boundaries, policy defaults, and tenant delegation so teams can self-serve without owning shared edge infrastructure.
- Migrate incrementally with equivalent routing tests, traffic and certificate observability, rollback-able DNS or listener cutovers, and explicit handling for features that do not map one-to-one.
- Ingress remains stable but is frozen, and Gateway behavior depends on the implementation; do not assume a manifest migration produces identical data-plane behavior.

## References

- [Kubernetes: Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)
- [Kubernetes: Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
