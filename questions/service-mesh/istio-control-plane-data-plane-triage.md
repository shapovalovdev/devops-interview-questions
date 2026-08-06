---
title: Distinguish Istio control-plane and data-plane failures
theme: service-mesh
difficulty: staff
type: troubleshooting
tags: [service-mesh, istio, kubernetes, ica, troubleshooting, observability, reliability]
sources:
  - url: https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Distinguish Istio control-plane and data-plane failures

Mesh requests are failing after a platform change across several teams. How do you coordinate determination of whether the fault is in Istiod, a proxy, or the application path?

## Answer guide

- Establish scope with a known-good workload and a failing workload, then separate API/control-plane health, proxy connection and synchronization status, gateway health, service endpoints, DNS, TLS, and application responses. An unhealthy request can occur with a healthy control plane, and a proxy sync warning does not by itself prove the user-visible fault.
- Inspect Istiod logs and metrics, `istioctl proxy-status`, the target proxy's effective configuration, Envoy access logs, and the Kubernetes events and endpoints that underlie the route. Check recent installation revisions, certificate trust, network policy, resource pressure, and image changes before restarting components that may erase useful evidence.
- Restore the smallest verified broken dependency with the affected owners and monitor both mesh and application indicators through recovery. Repeatedly restarting proxies or Istiod without identifying the bad configuration, network path, certificate, or endpoint condition can broaden the outage and delay a rollback of the actual triggering change.

## References

- [Istio: Proxy diagnostics](https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/)
- [Istio: Debugging Envoy and Istiod](https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
