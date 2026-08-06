---
title: Set Argo CD Application project boundaries
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-cd, capa, security, least-privilege]
sources:
  - url: https://argo-cd.readthedocs.io/en/stable/user-guide/projects/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set Argo CD Application project boundaries

How would you prevent one product team’s Argo CD Application from deploying arbitrary repositories and cluster resources?

## Answer guide

- Put the Application in an AppProject that limits permitted source repositories, destination clusters and namespaces, and allowed resource kinds. Use Argo CD RBAC so people and automation can act only on the project they own.
- Pair those controls with Kubernetes RBAC and namespace boundaries; an Argo CD project is an admission boundary in the delivery system, not a replacement for cluster authorization.
- Review wildcard rules and cluster-scoped resource permissions carefully. Broad source or destination allowlists can turn a compromised repository or token into a cross-team deployment path.

## References

- [Argo CD: Projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/)
- Further reading (blog): [GitHub Blog: least privilege for CI/CD](https://github.blog/security/application-security/secure-your-software-supply-chain-and-build-faster-with-github-actions/)
