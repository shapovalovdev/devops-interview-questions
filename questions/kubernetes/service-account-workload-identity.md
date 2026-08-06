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
