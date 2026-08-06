---
title: Install a cluster component with Helm or Kustomize safely
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, cka, ckad, deployment, configuration-management, security]
sources:
  - url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Install a cluster component with Helm or Kustomize safely

You need to deploy an ingress controller or metrics component. How do Helm and Kustomize fit into a safe installation workflow?

## Answer guide

- Use Helm when the upstream component publishes a maintained chart and its values expose the configuration contract you need; use Kustomize to compose declared Kubernetes resources and environment-specific patches. Both are delivery mechanisms, not substitutes for reviewing what will reach the API server.
- Pin chart, repository, and image versions; inspect rendered output before applying it, including namespace, ServiceAccount, RBAC, CRDs, webhook settings, resource requests, Services, and host/network access. Verify artifact provenance according to the organization’s supply-chain policy.
- Keep environment-specific changes in version control and run render/diff/validation in CI. Prefer explicit values or overlays over manual edits to release-owned objects, because the next reconciliation or upgrade can overwrite untracked changes.
- Plan CRD and controller upgrades together where the publisher requires it, and retain a tested rollback or recovery procedure. A generic `helm rollback` does not guarantee reversal of data migrations, immutable fields, externally created resources, or CRD schema changes.

## References

- [Kubernetes: Managing Kubernetes objects with Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
- [Helm: Chart best practices](https://helm.sh/docs/chart_best_practices/)
- Further reading (blog): [Kubernetes: Kustomize comes to kubectl](https://kubernetes.io/blog/2018/05/29/kustomize-coming-to-kubernetes/)
