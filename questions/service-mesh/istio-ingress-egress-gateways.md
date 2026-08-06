---
title: Configure Istio ingress and egress boundaries
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, istio, kubernetes, ica, networking, security]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure Istio ingress and egress boundaries

How do Istio ingress and egress gateways help define a service-mesh boundary?

## Answer guide

- Use an ingress gateway to receive traffic entering the mesh and configure the matching Gateway and routing resources deliberately for hostnames, ports, TLS, and backends. The gateway is a managed proxy boundary; it does not replace application authentication, authorization, rate limits, or the underlying Kubernetes and cloud network controls.
- Use an egress gateway when outbound traffic needs a controlled, observable enforcement point, such as for fixed source addresses, TLS policy, audit, or network controls. Register external destinations according to the mesh configuration so operators can distinguish intentional dependencies from unknown outbound traffic.
- Test both the allowed and denied paths, including DNS, TLS, identity, timeouts, and gateway failure. A gateway policy that omits DNS, certificate validation, health checks, or required third-party endpoints causes fragile production behavior, while an unrestricted egress rule silently defeats the intended boundary.

## References

- [Istio: Ingress gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/)
- [Istio: Egress gateways](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-gateway/)
- Further reading (blog): [Istio: Egress traffic control](https://istio.io/latest/blog/2019/monitoring-external-service-traffic/)
