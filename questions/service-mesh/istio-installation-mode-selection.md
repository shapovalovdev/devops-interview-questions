---
title: Select an Istio data-plane mode
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, istio, kubernetes, ica, security, observability]
sources:
  - url: https://istio.io/latest/docs/overview/dataplane-modes/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Select an Istio data-plane mode

How would you choose between Istio sidecar and ambient mode for a new Kubernetes workload?

## Answer guide

- Start with the workload's required capabilities and migration constraints. Sidecar mode runs an Envoy proxy alongside each enrolled workload and supports L4 and L7 features there; ambient mode provides shared per-node L4 processing and uses waypoint proxies when a namespace or service needs L7 features. Neither mode should be selected just because it is newer.
- Choose ambient when the initial goal is broadly applied transport security and basic telemetry with lower per-workload proxy overhead, then add a waypoint where HTTP routing, L7 policy, tracing, or access logs are needed. Choose sidecars when the supported feature set, workload environment, or existing operational practice requires their per-workload proxy model.
- Pilot the chosen mode in a bounded namespace, measure application latency, resource use, policy enforcement, telemetry, and rollback behavior. Mixed modes can interoperate, but a mode migration changes traffic capture and operational debugging, so validate NetworkPolicy, probes, exclusions, and failure paths before enrolling critical workloads.
- The per-workload-versus-shared trade is mesh-generic: Cilium made sidecar-less eBPF its only mode and Linkerd remains sidecar-only, so ambient is Istio's entry in the same design space — judge capability per unit of proxy overhead, not novelty.

## References

- [Istio: Sidecar or ambient data-plane modes](https://istio.io/latest/docs/overview/dataplane-modes/)
- Further reading (blog): [Istio: Introducing ambient mesh](https://istio.io/latest/blog/2022/introducing-ambient-mesh/)
