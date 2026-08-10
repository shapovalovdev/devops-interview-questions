---
title: Diagnose HTTP routing through Ingress or Gateway APIs
theme: certification-last-minute-review
difficulty: middle
type: troubleshooting
tags: [kubernetes, networking, http, tls, cka, ckad, troubleshooting]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/ingress/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose HTTP routing through Ingress or Gateway APIs

How do you investigate an HTTP route that returns the wrong response in Kubernetes?

## Answer guide

- First identify the controller implementing the API and the external entry point. Ingress is an API object, not a proxy; without a compatible controller, an Ingress rule has no data-plane effect. Gateway API likewise requires a controller implementation.
- Check host and path matching, TLS secret reference, the selected backend Service and port, then that Service's EndpointSlices and ready Pods. A valid route can still return a backend error or no endpoints.
- Reproduce with the correct Host header from inside and outside the cluster and inspect controller events and logs. Avoid assuming annotations are portable: they are usually controller-specific and must be verified against that controller's documentation.

## References

- [Kubernetes: Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Kubernetes: Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)
- Further reading (blog): [Matt Butcher's writing](https://technosophos.com/)

## What to learn next

- Official documentation: [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- Manual or specification: [Gateway API documentation](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Matt Butcher's writing](https://technosophos.com/)
- Technical blog: [Google Cloud — Gateway API](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gateway-api)
- Hands-on guide: [Kubernetes Ingress tutorial](https://kubernetes.io/docs/concepts/services-networking/ingress/#the-ingress-resource)
