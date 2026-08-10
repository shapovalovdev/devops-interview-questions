---
title: Explain the role of an API gateway
theme: backend-architecture
difficulty: junior
type: theory
tags: [http, networking, security]
sources:
  - url: https://gateway-api.sigs.k8s.io/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the role of an API gateway

When is an API gateway useful, and what should it not become?

## Answer guide

- An API gateway is an edge component that applies shared HTTP concerns before requests reach backend services: routing, TLS termination, authentication integration, request limits, and telemetry. It gives clients one stable entry point while services can change behind it.
- Keep business rules and ownership with the service that owns the domain. The gateway needs explicit routes, timeouts, authentication failure behavior, and observability so operators can tell whether a failure occurred at the edge or downstream.
- It can become a harmful central monolith when it aggregates unrelated domain logic or synchronously calls many services for every request. That creates a coupled bottleneck and a large blast radius; use bounded edge policies and test gateway failure, latency, and rollback paths.

## References

- [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/)
- Further reading (personal blog): [Martin Fowler: microservice prerequisites](https://martinfowler.com/articles/microservice-prerequisites.html)

## What to learn next

- Official documentation: [Kubernetes Gateway API concepts](https://gateway-api.sigs.k8s.io/concepts/)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [Google Cloud API Gateway quickstarts](https://docs.cloud.google.com/api-gateway/docs/quickstarts)
