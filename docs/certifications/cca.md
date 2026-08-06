# Cilium Certified Associate (CCA) coverage

This map aligns original practice Questions to the current [Cilium Certified Associate
(CCA) curriculum](https://training.linuxfoundation.org/certification/cilium-certified-associate-cca/).
It is a study map, not a reproduction of exam questions or confidential exam content.
The curriculum was reviewed on 2026-08-06. CCA is an entry-level certification for
connecting, securing, and observing Kubernetes clusters with Cilium; check the official
page before studying because objectives and product versions can change.

All mapped Questions carry the `cca` tag, remain in one canonical Theme folder, have
original wording, a full answer guide, structured primary-source metadata, and a separately
labeled complementary technical blog post.

| Official domain | Weight | Canonical practice Questions |
| --- | ---: | --- |
| Architecture | 20% | [Cilium component roles](../../questions/kubernetes/cilium-component-roles.md), [Cilium IPAM mode](../../questions/kubernetes/cilium-ipam-mode-selection.md), [kube-proxy replacement](../../questions/container-networking/cilium-kube-proxy-replacement.md) |
| Network Policy | 18% | [Cilium L7 policy](../../questions/container-networking/cilium-l7-network-policy.md), [policy enforcement modes](../../questions/kubernetes/cilium-policy-enforcement-modes.md), [Kubernetes NetworkPolicy](../../questions/kubernetes/network-policy-enforcement.md), [NetworkPolicy enforcement limits](../../questions/container-networking/network-policy-enforcement-limits.md) |
| Service Mesh | 16% | [Cilium Gateway API](../../questions/service-mesh/cilium-gateway-api-routing.md), [transparent workload encryption](../../questions/service-mesh/cilium-transparent-encryption.md), [ingress and gateway boundaries](../../questions/container-networking/ingress-gateway-boundary.md) |
| Network Observability | 10% | [Hubble flow observation](../../questions/observability/cilium-hubble-flow-observation.md), [network observability standards](../../questions/container-networking/network-observability-standard.md) |
| Installation and Configuration | 10% | [installation connectivity validation](../../questions/kubernetes/cilium-install-connectivity-validation.md), [component roles](../../questions/kubernetes/cilium-component-roles.md) |
| Cluster Mesh | 10% | [Cluster Mesh prerequisites](../../questions/container-networking/cilium-clustermesh-prerequisites.md), [multi-cluster connectivity strategy](../../questions/container-networking/multi-cluster-connectivity-strategy.md), [Kubernetes Service discovery](../../questions/kubernetes/service-discovery-basics.md) |
| eBPF | 10% | [eBPF datapath trade-offs](../../questions/container-networking/cilium-ebpf-datapath-tradeoffs.md), [Kubernetes Service traffic path](../../questions/container-networking/kubernetes-service-traffic-path.md) |
| BGP and External Networking | 6% | [Cilium BGP external routing](../../questions/container-networking/cilium-bgp-external-routing.md), [Cilium Egress Gateway](../../questions/container-networking/cilium-egress-gateway-design.md) |

The coverage map is a study index, not a claim that these Questions guarantee exam performance.
