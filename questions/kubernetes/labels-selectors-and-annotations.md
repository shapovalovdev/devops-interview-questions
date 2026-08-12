---
title: Distinguish labels, selectors, and annotations
theme: kubernetes
difficulty: junior
type: theory
tags: [kubernetes, deployment, automation, cka, ckad, kcna, cba]
sources:
  - url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish labels, selectors, and annotations

How should labels, selectors, and annotations be used safely in Kubernetes?

## Answer guide

- Labels are identifying key-value metadata intended for grouping and selecting objects; controllers and Services commonly rely on them.
- A selector is a query over labels, so changing a selector or its expected labels can disconnect a Service or controller from Pods.
- Annotations carry non-identifying metadata and are not designed for selection; controller-specific annotations need documented ownership.
- Treat selector labels as an API contract: use a stable, documented scheme and review label changes as carefully as traffic-routing changes.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
- [Kubernetes: Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

## What to learn next

- Official documentation: [Kubernetes concepts: labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
- Manual or specification: [Well-known labels, annotations and taints reference](https://kubernetes.io/docs/reference/labels-annotations-taints/)
- Maintainer or personal blog: [Ahmet Alp Balkan — why label selectors make Kubernetes list calls expensive](https://ahmet.im/blog/kubernetes-list-performance/)
- Technical blog: [Kirby Drumm — Kubernetes labels: 11 things to know](https://www.redhat.com/en/blog/kubernetes-labels-best-practices)
- Hands-on guide: [kubectl quick reference for selecting and filtering objects](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
