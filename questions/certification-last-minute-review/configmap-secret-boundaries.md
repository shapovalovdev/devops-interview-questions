---
title: Choose ConfigMaps and Secrets without overstating protection
theme: certification-last-minute-review
difficulty: middle
type: theory
tags: [kubernetes, security, cka, ckad, kcsa]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/secret/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose ConfigMaps and Secrets without overstating protection

What is the operational difference between ConfigMaps and Secrets?

## Answer guide

- ConfigMaps hold non-confidential configuration; Secrets are intended for sensitive data such as credentials and tokens. Both can be mounted or exposed to Pods, so access control and workload identity remain important.
- Base64 encoding is not encryption. Kubernetes documentation recommends encryption at rest for Secret data and least-privilege RBAC because anyone permitted to read a Secret can obtain its contents.
- Avoid injecting broad Secrets into every Pod. Scope data to the workload, rotate it deliberately, and consider a dedicated external secret system where audit, short-lived credentials, or provider identity is required.

## References

- [Kubernetes: Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- Further reading (blog): [Liz Rice's writing](https://www.lizrice.com/)

## What to learn next

- Official documentation: [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- Manual or specification: [Secret API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
- Maintainer or personal blog: [Liz Rice's writing](https://www.lizrice.com/)
- Technical blog: [Google Cloud — Secret Manager and GKE](https://cloud.google.com/blog/products/identity-security/how-to-use-secret-manager-with-gke)
- Hands-on guide: [Kubernetes configure a Pod to use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
