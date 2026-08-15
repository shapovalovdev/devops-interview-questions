---
title: Verify sidecar enrollment before troubleshooting mesh policy
theme: service-mesh
difficulty: junior
type: troubleshooting
tags: [service-mesh, istio, kubernetes, containers, troubleshooting, observability]
sources:
  - url: https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://linkerd.io/2.18/tasks/adding-your-service/
    source_type: official-docs
    verified_on: 2026-08-16
---

## What to learn next

- Official documentation: [Istio overview](https://istio.io/latest/docs/overview/what-is-istio/)
- Manual or specification: [Gateway API specification](https://gateway-api.sigs.k8s.io/)
- Maintainer or personal blog: [Buoyant engineering blog](https://buoyant.io/blog/)
- Technical blog: [Tetrate service-mesh articles](https://www.tetrate.io/blog/)
- Hands-on guide: [Istio Bookinfo example](https://istio.io/latest/docs/examples/bookinfo/)

# Verify sidecar enrollment before troubleshooting mesh policy

A new workload does not appear in mesh telemetry and its routing policy has no effect. What do you check first?

## Answer guide

- Confirm the intended data-plane mode and verify that the namespace or workload is enrolled. In sidecar mode, inspect the Pod for the proxy container and confirm the injection labels, revision, admission webhook, and restart timing are correct.
- Check that the application exposes traffic on a protocol and port the mesh can identify, then inspect proxy status and effective configuration. A Kubernetes Service can work normally even if its Pods were never captured by the mesh.
- Correct the narrow enrollment cause, redeploy the affected Pod, and then recheck telemetry and policy. Do not label an entire production namespace or restart unrelated workloads to make a single test work: injection changes traffic interception and can affect probes, startup, and resource use.
- Enrollment mechanics differ by mesh: Linkerd injects on the `linkerd.io/inject` annotation through its webhook, and Cilium enrolls by running on the node with no sidecar at all — verify-capture-before-blaming-policy is the portable triage rule.

## References

- [Istio: Installing sidecars](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/)
- [Istio: Verify sidecar injection](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl-analyze/)
- Further reading (blog): [Buoyant engineering blog](https://buoyant.io/blog/)
- [Linkerd: adding your service](https://linkerd.io/2.18/tasks/adding-your-service/)
