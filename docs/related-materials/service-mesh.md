# Service mesh: related materials

Use upstream project documentation as factual authority. A service mesh changes
how traffic, identity, policy, and telemetry are implemented; it does not make
application authorization, network design, or incident ownership disappear.

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

Learn the control-plane/data-plane and workload-identity model first. Then
practice enrollment, mutual TLS, traffic management, gateways, and telemetry in
a disposable cluster. Finish with upgrades, policy lifecycle, multicluster
boundaries, and the platform ownership decisions that determine whether a mesh
improves rather than complicates reliability.
