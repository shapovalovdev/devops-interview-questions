# CKNE coverage map

This map aligns original practice Questions with the public [Certified Kubernetes
Network Engineer (CKNE) program domains](https://training.linuxfoundation.org/kubernetes-network-engineer-program/)
published by Linux Foundation Education. The source was reviewed on 2026-08-06.
At that date CKNE is still in development, so this is a curriculum-oriented study
map, **not** a reproduction of exam questions, beta material, confidential content,
or implied exam coverage. Recheck the official page before using this map for a
future exam preparation plan.

Each linked Question has a canonical Theme and will carry the `ckne` certification
tag after central catalog integration. Shared fundamentals are tagged rather than
copied into a certification-specific folder.

## Official domain mapping

| Official domain | Weight | Canonical original practice Questions | Mapping status |
| --- | ---: | --- | --- |
| Core Infrastructure and CNI | 15% | [Cilium installation validation](../../questions/kubernetes/cilium-install-connectivity-validation.md); [Cilium IPAM mode selection](../../questions/kubernetes/cilium-ipam-mode-selection.md); [debug CoreDNS and Service resolution](../../questions/kubernetes/coredns-service-debugging.md); [capture Linux packets](../../questions/linux-networking/packet-capture-scope.md); [debug a Linux network namespace](../../questions/linux-networking/network-namespace-connectivity.md) | Partial: a distinct multi-interface Pod configuration Question is required. |
| Service Networking and DNS | 25% | [choose a Service type and inspect endpoints](../../questions/kubernetes/service-types-and-endpoints.md); [trace Kubernetes Service traffic](../../questions/container-networking/kubernetes-service-traffic-path.md); [evaluate kube-proxy replacement](../../questions/container-networking/cilium-kube-proxy-replacement.md); [debug CoreDNS and Service resolution](../../questions/kubernetes/coredns-service-debugging.md); [govern an Ingress-to-Gateway migration](../../questions/kubernetes/gateway-migration-governance.md); [route ingress with Gateway API](../../questions/service-mesh/cilium-gateway-api-routing.md) | Covered by shared canonical Questions. |
| Advanced Traffic Management | 20% | [define ingress and gateway boundaries](../../questions/container-networking/ingress-gateway-boundary.md); [design controlled egress](../../questions/container-networking/cilium-egress-gateway-design.md); [define multi-cluster connectivity](../../questions/container-networking/multi-cluster-connectivity-strategy.md) | Partial: a distinct LLM-traffic routing Question is required. |
| Network Security and Policy | 25% | [restrict Pod traffic with NetworkPolicy](../../questions/kubernetes/network-policy-enforcement.md); [validate NetworkPolicy enforcement](../../questions/container-networking/network-policy-enforcement-limits.md); [plan transparent workload encryption](../../questions/service-mesh/cilium-transparent-encryption.md); [route ingress with Gateway API](../../questions/service-mesh/cilium-gateway-api-routing.md); [combine JWT authentication and authorization](../../questions/service-mesh/istio-jwt-authorization.md) | Covered by shared canonical Questions. |
| Observability | 15% | [establish container network observability standards](../../questions/container-networking/network-observability-standard.md); [design Linux host network observability](../../questions/linux-networking/linux-network-observability.md); [use mesh telemetry](../../questions/service-mesh/service-mesh-observability.md) | Covered by shared canonical Questions. |

## Required original gap Questions

The official scope names two objectives that existing Questions do not address at
the required configuration depth. They must be added as original canonical
Questions before this map is declared complete:

1. **Configure and troubleshoot a multi-interface Pod.** Put it in the
   `container-networking` Theme and verify it against the upstream
   [Multus CNI documentation](https://github.com/k8snetworkplumbingwg/multus-cni/tree/master/docs).
   It must explain default-route selection, NetworkAttachmentDefinition ownership,
   IPAM/routing validation, and the blast radius of changing a live workload's
   network attachments.
2. **Route LLM inference traffic with Gateway API controls.** Put it in the
   `service-mesh` Theme and verify it against the upstream
   [Gateway API Inference Extension documentation](https://gateway-api-inference-extension.sigs.k8s.io/).
   It must distinguish the extension's implementation and maturity constraints
   from core Gateway API, cover routing/endpoint signals and safe fallback, and
   avoid claiming portable LLM traffic semantics.

Both additions require `ckne` plus documented technical tags, a complete answer
guide, primary-source metadata, and a separate complementary blog. They must be
catalogued centrally and counted only after `tests/validate_questions.py` passes.

## Publication gate

The `ckne` tag and this map become active only when the content manifest, tag
vocabulary, website catalog records, and curriculum-map validation are updated
together. This avoids a misleading certification filter that appears to cover
unpublished or incomplete objectives.
