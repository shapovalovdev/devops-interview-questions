---
title: Test Kyverno policy changes with the CLI in CI
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, policy-as-code, kyverno, kca, ci-cd, automation]
sources:
  - url: https://kyverno.io/docs/kyverno-cli/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Test Kyverno policy changes with the CLI in CI

How would you use the Kyverno CLI to keep a policy change from surprising application teams after it reaches a cluster?

## Answer guide

- Version-pin the CLI with the policy repository and execute policy tests against representative resource fixtures in pull requests. Include allowed and denied cases, namespace and user context where relevant, existing-resource behavior when used, and expected mutations or generated output. Commit the fixtures so reviewers can see the intended contract rather than relying on a developer laptop or a live production cluster.
- Treat CLI evaluation as an early feedback layer, then validate rendered manifests and exercise admission behavior in an integration environment matching the target Kyverno and Kubernetes versions. Feed policy reports and CI failures back to the policy owner with a clear remediation path; `apply`, `test`, and query tools answer different questions and should not be conflated.
- Fixtures can become stale when CRDs, controllers, image metadata, or configuration change. Do not let a green offline test prove that a webhook is reachable, that RBAC permits a generate action, or that a background controller will converge. Preserve negative tests and run regression cases when a policy exception or failure occurs.

## References

- [Kyverno CLI reference](https://kyverno.io/docs/kyverno-cli/)
- [Kyverno CLI `test` command reference](https://kyverno.io/docs/kyverno-cli/reference/kyverno_test/)
- [Kyverno CLI `test` command reference](https://kyverno.io/docs/kyverno-cli/reference/kyverno_test/)
- Further reading (blog): [Kyverno community blog](https://kyverno.io/blog/)

## What to learn next

- Official documentation: [Kyverno CLI documentation](https://kyverno.io/docs/kyverno-cli/)
- Manual or specification: [kyverno test command reference](https://kyverno.io/docs/kyverno-cli/reference/kyverno_test/)
- Maintainer or personal blog: [Chip Zoller — preserving authorship in a GitOps world with Kyverno](https://neonmirrors.net/post/2023-03/preserving-authorship-in-a-gitops-world-with-kyverno/)
- Technical blog: [CNCF — GitOps policy-as-code with Argo CD and Kyverno](https://www.cncf.io/blog/2026/04/02/gitops-policy-as-code-securing-kubernetes-with-argo-cd-and-kyverno/)
- Hands-on guide: [Testing Kyverno policies with the CLI](https://kyverno.io/docs/guides/testing-policies/)
