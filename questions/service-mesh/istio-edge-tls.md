---
title: Secure edge traffic at an Istio gateway
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, istio, kubernetes, ica, tls, security, networking]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://gateway-api.sigs.k8s.io/guides/tls/
    source_type: official-docs
    verified_on: 2026-08-16
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Secure edge traffic at an Istio gateway

How would you terminate TLS for `api.example.com` at an Istio ingress gateway without exposing a default insecure route?

## Answer guide

- Configure a Gateway listener for the intended hostname and HTTPS port with a supported TLS mode and a credential reference that the gateway workload can read. Pair it with a VirtualService whose hosts and gateway attachment match the external request, then direct only approved routes to ready backend services.
- Manage certificates through a controlled issuer and renewal process, including the private-key access boundary, SAN coverage, expiration alerts, and a tested renewal path. Decide explicitly whether TLS terminates at the gateway, is re-encrypted to the backend, or is passed through; each choice changes which component can inspect and enforce HTTP policy.
- Test correct and incorrect SNI/host names, expired or untrusted certificates, plaintext requests, backend failure, and renewal. Do not use a catch-all listener or disable verification as a shortcut: shared gateways can otherwise serve the wrong certificate or unintentionally expose a service through a default route.
- Edge TLS is exactly what Gateway API standardized: listener TLS mode plus a certificate reference on the Gateway object, rendered alike by Istio's own gateway, Envoy Gateway, and Cilium — hostname coverage and terminate-versus-passthrough decisions live in the listener either way.

## References

- [Istio: Secure ingress traffic](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/)
- [Istio: Gateway reference](https://istio.io/latest/docs/reference/config/networking/gateway/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
- [Gateway API: TLS](https://gateway-api.sigs.k8s.io/guides/tls/)
