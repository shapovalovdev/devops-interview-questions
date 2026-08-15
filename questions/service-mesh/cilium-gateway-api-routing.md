---
title: Route ingress traffic with Cilium Gateway API
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, kubernetes, networking, traffic-management, security, cca, ckne]
sources:
  - url: https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gateway-api/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://gateway-api.sigs.k8s.io/
    source_type: official-docs
    verified_on: 2026-08-16
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Route ingress traffic with Cilium Gateway API

How would you expose two HTTP services through Cilium Gateway API while keeping backend access policy explicit?

## Answer guide

- Create a Gateway and HTTPRoutes with explicit hostnames and path matches, then bind only the intended Services and namespaces according to the Gateway API attachment rules.
- Cilium processes Gateway traffic through its Envoy integration and assigns the ingress identity at policy enforcement points, so allow both external-to-ingress and ingress-to-backend paths where required.
- Verify listener status, route acceptance, TLS configuration, and end-to-end requests before switching DNS or external load-balancer traffic.
- Treat Gateway migration as a security change. Incorrect attachment, missing policy for the ingress identity, or assumptions copied from another controller can create a 403/timeout outage or unexpectedly expose a backend.
- Attachment rules belong to the standard, enforcement to the controller: the same Gateway and HTTPRoute objects attach to Istio's or Envoy Gateway's implementations with identical hostname and namespace rules — only the policy identity semantics, like Cilium's ingress identity here, are implementation-specific.

## References

- [Cilium Gateway API support](https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gateway-api/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
- [Gateway API](https://gateway-api.sigs.k8s.io/)
