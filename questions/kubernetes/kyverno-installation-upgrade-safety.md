---
title: Install or upgrade Kyverno without blocking the cluster
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, policy-as-code, kyverno, kca, rolling-update]
sources:
  - url: https://kyverno.io/docs/installation/installation/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Install or upgrade Kyverno without blocking the cluster

How would you install or upgrade Kyverno in production while preserving both policy enforcement and API-server availability?

## Answer guide

- Pin and review the chart and Kyverno release against the supported Kubernetes version, render the configuration in CI, and test the upgrade on a representative non-production cluster. Keep Kyverno in its dedicated namespace, verify CRDs and webhook resources, and inspect the controller roles, replica plan, resource requests, and compatibility notes rather than treating a Helm upgrade as a stateless application rollout.
- Before enabling fail-closed rules, verify admission-controller readiness, multiple replicas where the availability objective requires them, disruption and placement controls, monitoring, and a safe namespace-exclusion design. The admission controller is required; background, reports, and cleanup controllers have different responsibilities and should be sized and validated separately.
- Stage policy changes and retain a tested rollback and break-glass procedure. If a fail-closed webhook is unreachable, matching API requests can fail; excluding every system namespace improves recovery but deliberately leaves those namespaces outside those policies. Do not upgrade the controller and introduce broad new enforcement in the same unreviewed change.

## References

- [Kyverno installation and controller components](https://kyverno.io/docs/installation/installation/)
- [Kyverno upgrading guidance](https://kyverno.io/docs/installation/upgrading/)
- [Kubernetes admission webhook good practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
- Further reading (blog): [Kyverno community blog](https://kyverno.io/blog/)

## What to learn next

- Official documentation: [Kyverno installation](https://kyverno.io/docs/installation/installation/)
- Official documentation: [Kyverno monitoring](https://kyverno.io/docs/monitoring/)
- Manual or specification: [Kubernetes webhook configuration](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
- Maintainer or personal blog: [Kyverno release notes](https://github.com/kyverno/kyverno/releases)
- Free learning material: [Kyverno Helm chart source](https://github.com/kyverno/kyverno/tree/main/charts/kyverno)
