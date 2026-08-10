---
title: Roll out Kyverno enforcement using policy reports
theme: kubernetes
difficulty: middle
type: troubleshooting
tags: [kubernetes, security, policy-as-code, kyverno, kca, monitoring, troubleshooting]
sources:
  - url: https://kyverno.io/docs/guides/reports/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Roll out Kyverno enforcement using policy reports

How do you move a Kyverno policy from observation to enforcement without turning policy violations into an uncontrolled production outage?

## Answer guide

- First establish the intended resource population, policy owner, violation taxonomy, and success criteria. Use policy reports and inventory to quantify violations, identify false positives, and separate legacy debt from new delivery. Report data is evidence for a rollout decision, not proof that every workload has been evaluated under every admission path.
- Pilot a narrow scope, provide developers with a remediation example and deadline, and progressively enforce once the observed violations are understood. Track policy result counts, webhook latency and errors, rejected API requests, and business delivery impact. Keep a time-bounded rollback or scoped exception path that is auditable and does not silently broaden the policy.
- Avoid treating audit-like visibility as equivalent to protection: resources can remain noncompliant until enforcement applies. Conversely, immediate broad enforcement can block controllers and deployments. Policy-report availability and background scans also depend on the deployed Kyverno components, RBAC, and version, so verify those prerequisites before setting operational expectations.

## References

- [Kyverno policy reports](https://kyverno.io/docs/guides/reports/)
- [Kyverno policy settings and failure behavior](https://kyverno.io/docs/policy-types/cluster-policy/policy-settings/)
- [Kubernetes admission webhook good practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
- Further reading (blog): [Kyverno community blog](https://kyverno.io/blog/)

## What to learn next

- Official documentation: [Kyverno policy reports guide](https://kyverno.io/docs/guides/reports/)
- Manual or specification: [PolicyReport custom resource specification (Kubernetes policy working group)](https://github.com/kubernetes-sigs/wg-policy-prototypes/blob/master/policy-report/README.md)
- Maintainer or personal blog: [Chip Zoller — automating cleanup and reporting of non-conformant resources](https://neonmirrors.net/post/2023-12-18/cleanup-bad-resources/)
- Technical blog: [Nirmata — Kyverno engineering blog](https://nirmata.com/blog/)
- Hands-on guide: [Applying Kyverno policies in audit and enforce mode](https://kyverno.io/docs/guides/applying-policies/)
