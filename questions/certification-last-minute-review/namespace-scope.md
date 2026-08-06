---
title: Distinguish namespaced and cluster-scoped Kubernetes resources
theme: certification-last-minute-review
difficulty: junior
type: theory
tags: [kubernetes, cka, ckad, kcna]
sources:
  - url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish namespaced and cluster-scoped Kubernetes resources

Why does namespace selection sometimes appear to have no effect?

## Answer guide

- Namespaces partition namespaced objects such as Pods, Services, ConfigMaps, and Deployments. A name need only be unique inside its namespace, and DNS, RBAC, quotas, and policies commonly use that boundary.
- Nodes, PersistentVolumes, StorageClasses, and ClusterRoles are cluster-scoped. Supplying `-n` does not isolate or rename them because their API identity is cluster-wide.
- Use `kubectl api-resources --namespaced=true|false` when unsure. During troubleshooting, check the object's namespace in metadata and the current namespace before concluding an object is missing or permissions are broken.

## References

- [Kubernetes: namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- Further reading (blog): [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- Manual or specification: [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google Cloud — namespaces best practices](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-organizing-with-namespaces)
- Hands-on guide: [Kubernetes task: set namespace preference](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)
