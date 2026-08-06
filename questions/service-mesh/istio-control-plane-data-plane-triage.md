---
title: Distinguish Istio control-plane and data-plane failures
theme: service-mesh
difficulty: senior
type: troubleshooting
tags: [service-mesh, istio, kubernetes, ica, troubleshooting, observability, reliability]
sources:
  - url: https://istio.io/latest/docs/ops/diagnostic-tools/istioctl-proxy-status/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish Istio control-plane and data-plane failures

Mesh requests are failing after a platform change. How do you determine whether the fault is in Istiod, a proxy, or the application path?

## Answer guide

- Establish scope with a known-good workload and a failing workload, then separate API/control-plane health, proxy connection and synchronization status, gateway health, service endpoints, DNS, TLS, and application responses. An unhealthy request can occur with a healthy control plane, and a proxy sync warning does not by itself prove the user-visible fault.
- Inspect Istiod logs and metrics, `istioctl proxy-status`, the target proxy's effective configuration, Envoy access logs, and the Kubernetes events and endpoints that underlie the route. Check recent installation revisions, certificate trust, network policy, resource pressure, and image changes before restarting components that may erase useful evidence.
- Restore the smallest verified broken dependency and monitor both mesh and application indicators through recovery. Repeatedly restarting proxies or Istiod without identifying the bad configuration, network path, certificate, or endpoint condition can broaden the outage and delay a rollback of the actual triggering change.

## References

- [Istio: Proxy status diagnostics](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl-proxy-status/)
- [Istio: Debugging Envoy and Istiod](https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/)
- Further reading (blog): [Istio: Troubleshooting Istio](https://istio.io/latest/blog/2021/proxy-config/)
