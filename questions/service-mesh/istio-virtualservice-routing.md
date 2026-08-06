---
title: Route mesh traffic with a VirtualService
theme: service-mesh
difficulty: middle
type: scenario
tags: [service-mesh, istio, kubernetes, ica, traffic-management, reliability]
sources:
  - url: https://istio.io/latest/docs/concepts/traffic-management/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Route mesh traffic with a VirtualService

How would you send `/v2` requests to a new application version while retaining a safe default route?

## Answer guide

- Define a VirtualService that binds to the intended host or gateway and contains ordered HTTP match rules. Put the specific `/v2` match before a default route, select an explicit destination subset or service port where required, and avoid using a transient Pod address as the routing target.
- Verify the resource is attached to the correct gateway or mesh context and that its host names match the request authority. Routing rules describe desired proxy behavior; they do not create ready endpoints, repair DNS, or override an unrelated route with a more specific attachment or match.
- Test representative paths, headers, retries, and an unavailable version before rollout, then inspect proxy configuration and request telemetry. A broad match, wrong host, missing subset, or route applied to the wrong gateway can send traffic unexpectedly or leave the new version unused without an obvious API error.

## References

- [Istio: Traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- [Istio: Request routing](https://istio.io/latest/docs/tasks/traffic-management/request-routing/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
