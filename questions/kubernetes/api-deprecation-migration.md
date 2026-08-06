---
title: Migrate an application away from a deprecated Kubernetes API
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, deployment, reliability, automation, ckad]
sources:
  - url: https://kubernetes.io/docs/reference/using-api/deprecation-policy/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Migrate an application away from a deprecated Kubernetes API

How do you move an application and its manifests off a Kubernetes API version that will be removed?

## Answer guide

- Identify the exact resource and API version used by rendered manifests, Helm values, generated clients, and controllers. Read the Kubernetes deprecation guide for the target cluster release, then update to the supported API and semantic field model rather than only replacing a version string.
- Validate the rendered objects against a cluster matching the target version, deploy through a reversible environment, and observe admission errors, reconciliation, and application behavior. Update CI to reject the removed version so a transitive chart or stale template cannot reintroduce it.
- Plan the change before upgrading control planes. Deprecated APIs may work for a period but removal turns creation, update, or controller behavior into an outage. Preserve a tested rollback compatible with both clusters where possible, and inventory third-party add-ons that submit the same resource.

## References

- [Kubernetes API deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
- [Kubernetes: Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)
- Further reading (blog): [Kubernetes API removals in v1.25](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25/)
