---
title: Design service-mesh boundaries across multiple clusters
theme: service-mesh
difficulty: staff
type: scenario
tags: [service-mesh, istio, kubernetes, networking, security, reliability, cloud]
sources:
  - url: https://istio.io/latest/docs/setup/install/multicluster/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Design service-mesh boundaries across multiple clusters

How would you decide whether and how two Kubernetes clusters should participate in one service mesh?

## Answer guide

- Start with ownership, regulatory boundary, network reachability, latency, failure-domain, and identity requirements. A shared mesh can simplify consistent policy and discovery, but it also couples trust, upgrade, and control-plane decisions across clusters.
- Choose and document a supported topology such as multi-primary or primary-remote, then validate cross-network gateways, trust-domain strategy, service discovery, DNS, certificates, and failure behavior. Keep a cluster-local path for critical traffic where a remote dependency is not justified.
- Establish staged onboarding and rollback, plus clear SLOs for east-west gateways and remote discovery. Treating two clusters as one flat network can expand an outage or identity compromise; treating them as isolated without tested connectivity can produce asymmetric routing and silent failover failures.
- Multicluster coupling is a mesh-generic trade: Linkerd mirrors remote services behind per-cluster gateways without sharing a control plane, trading Istio's shared-identity reach for weaker blast coupling — ownership and trust-domain boundaries must be drawn explicitly in either model.

## References

- [Istio: Multicluster installation](https://istio.io/latest/docs/setup/install/multicluster/)
- [Istio: Multicluster deployment models](https://istio.io/latest/docs/ops/deployment/deployment-models/)
- Further reading (blog): [Istio: Multicluster service mesh](https://istio.io/latest/blog/2020/multi-cluster-mesh-automation/)
