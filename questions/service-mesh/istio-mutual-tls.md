---
title: Enforce Istio mutual TLS incrementally
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, istio, kubernetes, ica, mtls, security, reliability]
sources:
  - url: https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Enforce Istio mutual TLS incrementally

How would you move a mixed workload namespace toward strict mutual TLS without breaking unmeshed clients?

## Answer guide

- Inventory callers, servers, gateways, VMs, and unmeshed or legacy endpoints before changing policy. PeerAuthentication defines the receiving side's mTLS posture, while DestinationRule client TLS settings influence how workload proxies originate traffic; the two must be compatible with the actual traffic path.
- Begin with a mode that permits the required transition traffic, verify that workload identities and certificates are issued and rotated correctly, then enforce strict mTLS in bounded namespaces or services after all legitimate callers are prepared. Test ingress, egress, health probes, batch jobs, and cross-namespace calls because they often reveal unaccounted clients.
- Monitor TLS handshake and policy failures during each step and retain a controlled rollback path. Strict mTLS improves workload authentication but does not authorize requests or secure an endpoint that bypasses the mesh, and a premature global switch can create a broad availability outage.

## References

- [Istio: mTLS migration](https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)
- [Istio: PeerAuthentication reference](https://istio.io/latest/docs/reference/config/security/peer_authentication/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
