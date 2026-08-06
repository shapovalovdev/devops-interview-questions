---
title: Combine JWT authentication and authorization in Istio
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, istio, kubernetes, ica, jwt, security, least-privilege, ckne]
sources:
  - url: https://istio.io/latest/docs/tasks/security/authentication/authn-policy/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Combine JWT authentication and authorization in Istio

How would you require a valid JWT for an API and permit only a specific role to call its write endpoint?

## Answer guide

- Configure RequestAuthentication to validate tokens from the trusted issuer, including the expected JWT locations and claims, then use AuthorizationPolicy to require authenticated principals and allow only the intended method, path, and claim values. Authentication establishes token validity; authorization decides whether that identity may perform the request.
- Define issuer, audiences, signing-key retrieval, clock behavior, and failure semantics deliberately. Keep application authorization for domain-specific decisions that a proxy cannot safely express, and avoid forwarding sensitive claims or accepting arbitrary headers as an identity substitute.
- Test missing, expired, wrong-issuer, wrong-audience, and insufficient-role tokens as well as a valid request. An allow policy that is too broad, an unprotected alternate gateway, or a policy attached to the wrong workload can make the design appear secure while leaving the write endpoint reachable.

## References

- [Istio: Authentication policy](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/)
- [Istio: Authorization policy](https://istio.io/latest/docs/tasks/security/authorization/authz-http/)
- Further reading (blog): [Istio: Authorization policy security](https://istio.io/latest/blog/2021/better-external-authz/)
