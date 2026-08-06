---
title: Design a maintainable Kyverno policy set
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, policy-as-code, kyverno, kca, supply-chain]
sources:
  - url: https://kyverno.io/docs/policy-types/validating-policy/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://kyverno.io/docs/policy-types/mutating-policy/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://kyverno.io/docs/policy-types/generating-policy/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a maintainable Kyverno policy set

How would you author and review a Kyverno policy set that validates workload security, applies safe defaults, and generates required supporting configuration?

## Answer guide

- Model each policy as a small, versioned contract: state the resources it selects, the compliant and noncompliant examples, enforcement mode, message, owner, and the exact invariant. Prefer validation for non-negotiable security requirements, narrow mutation for deterministic defaults, and generation only where the generated resource's ownership, synchronization, and RBAC are explicit. Test every rule with positive and negative fixtures before rollout.
- Design selectors and preconditions defensively. Account for namespace scope, controller-created Pods, defaulted fields, background processing, and resource version differences. Keep policy logic reviewable; use reusable values or variables only when their failure and change semantics are understood. Image verification must specify what identity, signature, and digest properties are actually trusted.
- Avoid a single catch-all policy that mixes unrelated controls and becomes impossible to stage or roll back. Mutations can obscure a bad application manifest, generated resources can overwrite locally managed configuration, and broad matching can impact system workloads. Review policy changes like production code with security, platform, and application owners.

## References

- [Kyverno validating policies](https://kyverno.io/docs/policy-types/validating-policy/)
- [Kyverno mutating policies](https://kyverno.io/docs/policy-types/mutating-policy/)
- [Kyverno generating policies](https://kyverno.io/docs/policy-types/generating-policy/)
- [Kyverno image-validating policies](https://kyverno.io/docs/policy-types/image-validating-policy/)
- Further reading (blog): [Kyverno community blog](https://kyverno.io/blog/)

## What to learn next

- Official documentation: [Kyverno policy library](https://kyverno.io/policies/)
- Official documentation: [Kyverno variables](https://kyverno.io/docs/policy-types/cluster-policy/variables/)
- Manual or specification: [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- Maintainer or personal blog: [Kyverno maintainers' blog](https://kyverno.io/blog/)
- Free learning material: [Kyverno policy samples](https://github.com/kyverno/policies)
