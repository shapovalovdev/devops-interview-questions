---
title: Use RuntimeClass for higher-risk workload isolation
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, containers, platform-engineering, cks]
sources:
  - url: https://kubernetes.io/docs/concepts/containers/runtime-class/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use RuntimeClass for higher-risk workload isolation

When should a platform use a sandboxed runtime through RuntimeClass, and how would you deploy it safely for untrusted tenant workloads?

## Answer guide

- Use a distinct runtime handler only when the threat model justifies stronger isolation than the default container runtime, such as selected multi-tenant or untrusted-code workloads. Install and validate the handler on every eligible node, then create a RuntimeClass whose handler name matches the container runtime configuration.
- Constrain scheduling with RuntimeClass scheduling rules or node labels so a Pod cannot land on a node without that handler. Pilot representative workloads, measure startup, resource, networking, storage, and debugging differences, and make the isolation tier visible to service owners.
- Apply the RuntimeClass in an explicit Pod spec and verify the admitted Pod, assigned node, and runtime behavior. Combine it with RBAC, Pod Security Admission, network policy, image controls, and resource limits; a sandbox runtime is one boundary, not a complete security program.
- The stronger boundary has cost and compatibility trade-offs. Missing handlers cause scheduling or startup failures, while a default RuntimeClass can unexpectedly change unrelated workloads; do not use it as a substitute for keeping hosts and runtimes patched.

## References

- [Kubernetes: RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/)
- [Kubernetes: Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- Further reading (blog): [gVisor: Kubernetes quick start](https://gvisor.dev/docs/user_guide/quick_start/kubernetes/)

## What to learn next

- Official documentation: [Kubernetes concepts: RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/)
- Manual or specification: [KEP-585: RuntimeClass enhancement proposal](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/585-runtime-class/README.md)
- Maintainer or personal blog: [Tim Allclair — introducing RuntimeClass](https://kubernetes.io/blog/2018/10/10/kubernetes-v1.12-introducing-runtimeclass/)
- Technical blog: [Kubernetes blog — running agents on Kubernetes with sandboxed runtimes](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)
- Hands-on guide: [Run gVisor sandboxed containers on Kubernetes](https://gvisor.dev/docs/user_guide/quick_start/kubernetes/)
