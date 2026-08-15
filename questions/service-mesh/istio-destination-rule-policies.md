---
title: Apply traffic policies with a DestinationRule
theme: service-mesh
difficulty: middle
type: theory
tags: [service-mesh, istio, kubernetes, ica, traffic-management, reliability]
sources:
  - url: https://istio.io/latest/docs/concepts/traffic-management/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://gateway-api.sigs.k8s.io/geps/gep-1748/
    source_type: official-docs
    verified_on: 2026-08-16
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Apply traffic policies with a DestinationRule

What belongs in an Istio DestinationRule, and how should it relate to routing?

## Answer guide

- A DestinationRule defines policies applied after traffic is routed to a service, including named subsets and traffic policy such as load balancing, connection pools, outlier detection, and TLS settings. A VirtualService chooses where matching traffic goes; a DestinationRule describes how traffic is treated for that chosen destination.
- Create subsets from stable workload labels and ensure every routed subset actually has eligible, ready workloads. Apply policies at the narrowest suitable scope and use explicit naming, because a service-wide policy can affect callers beyond the rollout that motivated it.
- Validate the rendered proxy configuration and service metrics after change. A subset with no matching endpoints, contradictory TLS configuration, or overly aggressive ejection and connection limits can make a healthy version unreachable or amplify a dependency incident rather than improve resilience.
- Per-destination policy has named equivalents: Linkerd's ServiceProfile carries per-route retries and timeouts, and Gateway API's BackendTrafficPolicy (GEP-1748) standardizes timeout, retry, and load-balancing attachment to backends — a subset with no endpoints is the failure mode to test in each.

## References

- [Istio: Traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- [Istio: DestinationRule reference](https://istio.io/latest/docs/reference/config/networking/destination-rule/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
- [Gateway API: GEP-1748 BackendTrafficPolicy](https://gateway-api.sigs.k8s.io/geps/gep-1748/)
