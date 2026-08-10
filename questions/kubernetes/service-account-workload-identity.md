---
title: Give a Kubernetes workload the least-privilege ServiceAccount
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, least-privilege, deployment, ckad]
sources:
  - url: https://kubernetes.io/docs/concepts/security/service-accounts/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Give a Kubernetes workload the least-privilege ServiceAccount

How should an application use a Kubernetes ServiceAccount without granting every Pod broad cluster access?

## Answer guide

- Create a dedicated ServiceAccount for the workload and set `serviceAccountName` in its Pod template. Bind only the required verbs and resources with a Role and RoleBinding in the workload namespace; use cluster-wide permissions only when the application genuinely operates cluster-wide.
- Disable automatic token mounting for workloads that do not call the Kubernetes API, and use projected, short-lived credentials when an API credential is needed. Review the resulting permissions with the same care as application credentials, including any cloud-workload identity integration.
- Do not rely on the namespace default ServiceAccount or broad built-in roles for convenience. Those defaults make privilege review difficult and turn a compromised application container into a wider control-plane risk. Test authorization failures deliberately and monitor denied requests while narrowing permissions.

## References

- [Kubernetes: Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [Kubernetes: RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- Further reading (blog): [Kubernetes ServiceAccount token improvements](https://kubernetes.io/blog/2020/12/24/introducing-bound-service-account-tokens/)

## What to learn next

- Official documentation: [Kubernetes concepts: service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- Manual or specification: [TokenRequest v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
- Maintainer or personal blog: [Rory McCune — anonymous access to the Kubernetes API](https://raesene.github.io/blog/2023/03/18/lets-talk-about-anonymous-access-to-Kubernetes/)
- Technical blog: [Kubernetes blog — service account token integration for image pulls](https://kubernetes.io/blog/2025/09/03/kubernetes-v1-34-sa-tokens-image-pulls-beta/)
- Hands-on guide: [Configure service accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
