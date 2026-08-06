---
title: Secure Kubernetes Secret access and rotation
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, least-privilege, automation]
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
