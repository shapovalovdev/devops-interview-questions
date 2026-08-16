# Service mesh: related materials

Use upstream project documentation as factual authority. A service mesh changes
how traffic, identity, policy, and telemetry are implemented; it does not make
application authorization, network design, or incident ownership disappear.

## Vendor bias

Istio is this Theme's working example: most Questions describe Istio's CRDs
and tooling from `istio.io`, and only a few use Cilium or Gateway API
directly. The concepts themselves — control plane versus data plane, workload
identity, mutual TLS, traffic policy, progressive delivery — are mesh-generic.
Linkerd expresses them with a smaller Rust-proxy data plane and mTLS by
default, and the Kubernetes Gateway API standardizes the north-south routing
half across implementations. Each vendor-neutral Question's answer guide maps
its concept onto at least one of those, while Questions about Istio's own
mechanics (revision-canary upgrades, ambient versus sidecar modes) keep Istio
framing.

## What to learn next

- Official documentation: [Istio documentation](https://istio.io/latest/docs/)
- Manual or specification: [Kubernetes Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

## Legal free books

- [The Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/)
  is freely published by Google and provides useful foundations for service
  reliability, monitoring, and incident response.
- [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)
  is a freely published companion for implementing reliability practices. Apply
  its recommendations alongside the mesh project's version-specific guidance.

## Suggested study order

The control-plane, data-plane, and identity model first, practice in a
disposable cluster second, ownership decisions last.

1. [Distinguish a mesh control plane from its data plane](../../questions/service-mesh/service-mesh-control-data-plane.html)
    — The control-plane and data-plane split explains what a mesh actually adds.
2. [Explain workload identity in a service mesh](../../questions/service-mesh/service-mesh-identity.html)
    — Workload identity is the foundation everything else the mesh promises
    stands on.
3. [Verify sidecar enrollment before troubleshooting mesh policy](../../questions/service-mesh/service-mesh-sidecar-injection.html)
    — Enrollment is verified before policy, or nothing downstream can even be
    debugged.
4. [Enforce Istio mutual TLS incrementally](../../questions/service-mesh/istio-mutual-tls.html)
    — Mutual TLS is enforced incrementally once enrollment is trustworthy.
5. [Route mesh traffic with a VirtualService](../../questions/service-mesh/istio-virtualservice-routing.html)
    — Traffic management opens with the routing rules a mesh can express.
6. [Apply traffic policies with a DestinationRule](../../questions/service-mesh/istio-destination-rule-policies.html)
    — DestinationRules carry the traffic and resilience policies routing depends
    on.
7. [Shift traffic progressively with Istio](../../questions/service-mesh/istio-progressive-traffic-shift.html)
    — Progressive traffic shifts are traffic management with a safety contract.
8. [Configure Istio ingress and egress boundaries](../../questions/service-mesh/istio-ingress-egress-gateways.html)
    — Gateways govern where mesh traffic meets the outside world.
9. [Use mesh telemetry without mistaking it for complete observability](../../questions/service-mesh/service-mesh-observability.html)
    — Mesh telemetry is used without mistaking it for complete observability.
10. [Upgrade Istio with a bounded canary](../../questions/service-mesh/istio-canary-upgrade.html)
    — Upgrades come late because they risk everything above them at once.
11. [Design service-mesh boundaries across multiple clusters](../../questions/service-mesh/service-mesh-multicluster-boundaries.html)
    — Multicluster boundaries extend the identity and policy model across
    clusters.
12. [Make a service-mesh adoption decision with measurable outcomes](../../questions/service-mesh/service-mesh-adoption-decision.html)
    — The adoption decision is made with measurable outcomes, after the
    mechanics are known.
13. [Establish safe service-mesh platform guardrails](../../questions/service-mesh/service-mesh-platform-guardrails.html)
    — Platform guardrails close the Theme: whether the mesh improves reliability
    or merely complicates it.
