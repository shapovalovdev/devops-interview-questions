---
title: Use Kubernetes namespaces and resource scope correctly
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, security, governance, cka, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use Kubernetes namespaces and resource scope correctly

What do namespaces isolate, and what do they not isolate?

## Answer guide

- Namespaces scope names for namespaced API objects and provide a boundary to attach policies, quotas, and RBAC rules.
- They do not by themselves isolate network traffic, CPU and memory, node access, or secrets; add NetworkPolicies, ResourceQuotas, RBAC, and admission controls as needed.
- Cluster-scoped resources such as Nodes, PersistentVolumes, and ClusterRoles are not namespaced and require cluster-wide governance.
- Do not use namespaces as a complete tenant-security boundary without validating the workload threat model and the controls enforced by the cluster.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- [Kubernetes: Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
