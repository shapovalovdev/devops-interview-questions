---
title: Operate a custom resource and its controller safely
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, cka, ckad, automation, reliability, security, cnpe, cnpa]
sources:
  - url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Operate a custom resource and its controller safely

What must an administrator verify before installing or upgrading an operator that introduces CustomResourceDefinitions (CRDs)?

## Answer guide

- A CRD extends the Kubernetes API with a new resource shape, while a controller/operator watches those resources and reconciles desired state. Installing only the CRD creates an API object but does not create the controller behavior users normally expect.
- Review scope, schema validation, defaulting, conversion strategy, versions served/stored, status fields, ownership, RBAC, admission webhooks, and the controller’s external permissions. Apply least privilege because an operator often receives powerful cluster-wide access.
- Treat the CRD, controller, and existing custom resources as one lifecycle unit. Back up relevant objects, test compatibility in a representative cluster, and follow the publisher’s documented order; removing a CRD can delete its custom resources.
- Monitor reconciliation errors, queue latency, API errors, and controller resource usage after rollout. A controller that is crash-looping, over-privileged, or unable to reach an external dependency can leave workloads partly reconciled even though the API accepts the custom resource.

## References

- [Kubernetes: Custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [Kubernetes: Extend the Kubernetes API with CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
- Further reading (blog): [Kubernetes: Extending Kubernetes APIs with CRDs](https://kubernetes.io/blog/2017/06/introducing-extensible-admission-control/)

## What to learn next

- Official documentation: [Extend the Kubernetes API with CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
- Manual or specification: [CustomResourceDefinition v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/)
- Maintainer or personal blog: [Ahmet Alp Balkan — pitfalls when writing Kubernetes controllers](https://ahmet.im/blog/controller-pitfalls/)
- Technical blog: [CNCF — Kubernetes operators 101](https://www.cncf.io/blog/2020/10/02/kubernetes-operators-101/)
- Hands-on guide: [The Kubebuilder book: build an operator step by step](https://book.kubebuilder.io/)
