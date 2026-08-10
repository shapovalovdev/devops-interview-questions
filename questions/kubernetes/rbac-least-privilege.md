---
title: Design least-privilege Kubernetes RBAC
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, least-privilege, governance, cks, kcsa, cka, ckad, kcna, cnpe, cnpa]
sources:
  - url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design least-privilege Kubernetes RBAC

How would you authorize a workload and an operator without granting broad cluster access?

## Answer guide

- Bind a ServiceAccount or authenticated subject to a Role for namespace-scoped permissions, or to a tightly limited ClusterRole only when cluster-scoped access is necessary.
- Grant explicit verbs on the smallest required resource set; `list`, `watch`, secret reads, impersonation, and wildcard permissions are often much broader than they appear.
- Keep workload identities separate from human and automation identities, and validate access with authorization checks and audit logs.
- RBAC only decides API authorization: combine it with namespace, admission, secret, and network controls, and review grants when controllers or APIs change.

## References

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Kubernetes: Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)

## What to learn next

- Official documentation: [Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- Manual or specification: [Role v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/)
- Maintainer or personal blog: [Rory McCune — auditing Kubernetes RBAC, redux](https://raesene.github.io/blog/2022/08/14/auditing-rbac-redux/)
- Technical blog: [Kubernetes blog — 11 ways (not) to get hacked](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/)
- Hands-on guide: [RBAC good practices for least privilege](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
