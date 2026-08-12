---
title: Secure Kubernetes Secret access and rotation
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, least-privilege, automation, cks, kcsa, cka, ckad, kcna, cba]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/secret/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Secure Kubernetes Secret access and rotation

How would you give a workload a credential and rotate it without overexposing it?

## Answer guide

- Use a Secret for confidential data, grant only the workload identity and operators that need it permission to read it, and enable encryption at rest for the cluster.
- Prefer a volume or a purpose-built external secret integration when the application can reload credentials; avoid broad environment exposure and never commit secret values to manifests.
- Rotate by issuing a new credential, updating the Secret through the approved delivery path, rolling or reloading consumers, then revoking the old credential after verification.
- Kubernetes Secret encoding is not encryption, and a mounted Secret through `subPath` does not receive updates; audit RBAC and application logs for accidental disclosure.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes: Good practices for Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/)

## What to learn next

- Official documentation: [Kubernetes concepts: Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- Manual or specification: [Secret v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
- Maintainer or personal blog: [Omer Levi Hevroni — how to keep Kubernetes Secrets safely in Git](https://learnkube.com/kubernetes-secrets-in-git)
- Technical blog: [Kubernetes blog — KMS v2 envelope encryption and key rotation](https://kubernetes.io/blog/2023/05/16/kms-v2-moves-to-beta/)
- Hands-on guide: [Encrypt confidential data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
