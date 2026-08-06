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

- Official documentation: [Kyverno CLI `apply`](https://kyverno.io/docs/kyverno-cli/reference/kyverno_apply/)
- Official documentation: [Kyverno policy reports](https://kyverno.io/docs/guides/reports/)
- Manual or specification: [Kubernetes dry-run](https://kubernetes.io/docs/reference/using-api/api-concepts/#dry-run)
- Maintainer or personal blog: [Kyverno community blog](https://kyverno.io/blog/)
- Free learning material: [Kyverno policy examples](https://github.com/kyverno/policies)
