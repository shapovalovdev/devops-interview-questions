---
title: Diagnose an RBAC denial without broadening access
theme: certification-last-minute-review
difficulty: middle
type: troubleshooting
tags: [kubernetes, security, iam, least-privilege, cka, ckad, cks, kcsa]
sources:
  - url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an RBAC denial without broadening access

What is a safe method for resolving `forbidden` from the Kubernetes API?

## Answer guide

- Identify the authenticated subject, verb, API group, resource, subresource, name, and namespace in the error. RBAC decisions are request-specific, so a role that lists Pods need not allow logs, exec, or updates.
- Use `kubectl auth can-i` with the same identity and scope to test the intended request. Then bind the smallest Role or ClusterRole rule that grants the required verb and resource.
- Prefer namespace-scoped Roles when possible and avoid binding `cluster-admin` as a quick fix. Re-test after the change, record why the permission exists, and account for service accounts and impersonation used by automation.

## References

- [Kubernetes: RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- Further reading (blog): [Rory McCune — Kubernetes RBAC](https://rorymccune.com/2021/01/04/kubernetes-rbac/)

## What to learn next

- Official documentation: [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- Manual or specification: [Authorization overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
- Maintainer or personal blog: [Rory McCune — RBAC](https://rorymccune.com/2021/01/04/kubernetes-rbac/)
- Technical blog: [Google Cloud — RBAC best practices](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa)
- Hands-on guide: [Kubernetes RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
