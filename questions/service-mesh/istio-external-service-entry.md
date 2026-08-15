---
title: Connect a mesh workload to an external service
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, istio, kubernetes, ica, networking, security]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/egress/egress-control/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Connect a mesh workload to an external service

How would you permit an in-mesh service to call a third-party HTTPS API without making outbound traffic unmanaged?

## Answer guide

- First identify the external hostnames, ports, protocol, owner, data classification, DNS behavior, and availability dependency. Configure the mesh egress policy and ServiceEntry or equivalent registration according to the chosen outbound traffic mode so the destination is known rather than relying on a broad, invisible escape route.
- Route through an egress gateway when centralized control, audit, fixed source identity, or TLS handling is needed. Preserve the application's end-to-end TLS and hostname validation requirements; proxying traffic does not make a third-party endpoint trustworthy or remove the need for least-privilege application credentials.
- Test resolution, certificate validation, timeout and retry budgets, denied destinations, and gateway loss. An allow rule that assumes static IPs, omits dependencies such as DNS, or silently disables TLS verification can create both outages and a security bypass.
- Registration versus enforcement is mesh-specific: Linkerd passes outbound traffic through by default and governs it with policy rather than a registry, and Cilium models the same intent as CiliumNetworkPolicy egress rules — making dependencies visible survives either mechanism.

## References

- [Istio: Control egress traffic](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-control/)
- [Istio: ServiceEntry reference](https://istio.io/latest/docs/reference/config/networking/service-entry/)
- Further reading (blog): [Istio: Monitoring external service traffic](https://istio.io/latest/blog/2019/monitoring-external-service-traffic/)
