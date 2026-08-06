---
title: Route LLM inference traffic with Gateway API controls
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, kubernetes, networking, gateway-api, traffic-management, llm, inference, routing, observability, ckne]
sources:
  - url: https://gateway-api-inference-extension.sigs.k8s.io/concepts/api-overview/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://gateway-api-inference-extension.sigs.k8s.io/guides/implementers/
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Gateway API Inference Extension introduction](https://gateway-api-inference-extension.sigs.k8s.io/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Envoy AI Gateway blog](https://aigateway.envoyproxy.io/blog/)
- Technical blog: [Kubernetes: introducing Gateway API Inference Extension](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)
- Hands-on guide: [Inference Extension implementer guide](https://gateway-api-inference-extension.sigs.k8s.io/guides/implementers/)

# Route LLM inference traffic with Gateway API controls

How would you expose self-hosted LLM inference through Gateway API while using
model-aware endpoint selection safely and retaining a usable fallback when the
inference-routing extension is unavailable?

## Answer guide

- Start with normal Gateway API ownership and policy: a Gateway listener and an `HTTPRoute` deliberately select the inference backend, with TLS, authentication, authorization, rate limits, request-size/time limits, and observability defined at the appropriate gateway/platform layer. Core Gateway API determines route attachment and ordinary backend forwarding; it does **not** define portable model-aware, token-aware, or LLM-specific routing semantics.
- Where the selected Gateway implementation supports the Gateway API Inference Extension, point the route at an `InferencePool`. The controller discovers the pool's endpoints and invokes a compatible Endpoint Picker (EPP), which chooses from a supplied eligible subset or the pool's endpoints using signals such as health, availability, model capability, cache state, or scheduler-provided metrics. Validate endpoint readiness, model/version compatibility, selection latency, request identifiers, and the controller's per-Gateway status rather than assuming a Service-style load balancer understands those signals.
- Design a bounded failure policy. The extension protocol can return `503` when no endpoint is ready or `429` when it should shed a request, and can provide a fallback endpoint. Permit a fallback only when its model, data boundary, capacity, cost, and response-quality contract are acceptable; otherwise return a clear retryable failure with back-pressure. Do not silently retry non-idempotent streaming or tool-calling requests across endpoints without an application-level contract.
- Treat this as an implementation-dependent extension, not a generic Gateway API promise. Confirm that the specific controller/data plane implements the extension and its relevant conformance profile, pin compatible versions, test EPP timeout/unavailability, stale metrics, endpoint churn, and overload in staging, and retain a plain-Service/HTTPRoute or controlled maintenance path. The project's lightweight EPP is for testing/conformance, not a production scheduler.

## References

- [Gateway API Inference Extension: API overview and InferencePool](https://gateway-api-inference-extension.sigs.k8s.io/concepts/api-overview/)
- [Gateway API Inference Extension: endpoint tracking, EPP responses, and testing](https://gateway-api-inference-extension.sigs.k8s.io/guides/implementers/)
- [Gateway API Inference Extension conformance model](https://gateway-api-inference-extension.sigs.k8s.io/concepts/conformance/)
- Further reading (blog): [Envoy AI Gateway blog](https://aigateway.envoyproxy.io/blog/)
