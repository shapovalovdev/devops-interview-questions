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
---

# Apply traffic policies with a DestinationRule

What belongs in an Istio DestinationRule, and how should it relate to routing?

## Answer guide

- A DestinationRule defines policies applied after traffic is routed to a service, including named subsets and traffic policy such as load balancing, connection pools, outlier detection, and TLS settings. A VirtualService chooses where matching traffic goes; a DestinationRule describes how traffic is treated for that chosen destination.
- Create subsets from stable workload labels and ensure every routed subset actually has eligible, ready workloads. Apply policies at the narrowest suitable scope and use explicit naming, because a service-wide policy can affect callers beyond the rollout that motivated it.
- Validate the rendered proxy configuration and service metrics after change. A subset with no matching endpoints, contradictory TLS configuration, or overly aggressive ejection and connection limits can make a healthy version unreachable or amplify a dependency incident rather than improve resilience.

## References

- [Istio: Traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- [Istio: DestinationRule reference](https://istio.io/latest/docs/reference/config/networking/destination-rule/)
- Further reading (blog): [Istio: Destination rule inheritance](https://istio.io/latest/blog/2021/proxy-config/)
