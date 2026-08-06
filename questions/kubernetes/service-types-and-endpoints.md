---
title: Expose an application with the right Service type
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, cka, ckad, networking, availability, troubleshooting, ckne]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/service/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Expose an application with the right Service type

How do ClusterIP, NodePort, and LoadBalancer Services differ, and how would you diagnose a Service that has no reachable backends?

## Answer guide

- Use ClusterIP for in-cluster virtual addressing and discovery, NodePort when each node must expose a port, and LoadBalancer when the platform can provision or integrate a load balancer. The latter two do not turn an unhealthy application into a healthy one and provider behavior is implementation-specific.
- Select Pods with deliberate labels and named ports where useful. Kubernetes normally creates EndpointSlices from that selector; inspect the Service selector, EndpointSlices, Pod readiness, target port, protocol, and namespace before changing network policy or recreating workloads.
- A Service can resolve in DNS while routing no ready endpoints. Readiness removes Pods from ordinary load-balancing endpoints, and a selector mismatch, wrong targetPort, terminating Pods, or application listener bound to the wrong interface can produce connection failures.
- Do not use NodePort as an ungoverned shortcut around ingress, firewall, TLS, or network policy. Define exposure ownership, health checks, source restrictions, and an escalation path because load balancer allocation, source-IP behavior, and traffic policies vary by implementation.

## References

- [Kubernetes: Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes: EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
- Further reading (blog): [Kubernetes: Topology-aware routing with EndpointSlices](https://kubernetes.io/blog/2021/04/22/topology-aware-hints/)
