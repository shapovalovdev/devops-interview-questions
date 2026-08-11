---
title: Choose a guardrail over a gate
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, guardrails, policy-as-code, governance]
sources:
  - url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Choose a guardrail over a gate

Security wants every deployment reviewed before it reaches production. What do you build instead, and when is a hard block the right answer?

## Answer guide

- Replace the review with a machine-checked constraint that runs at the earliest point it can be decided, and reserve a hard block for rules whose violation is unrecoverable or externally mandated. A guardrail is enforced automatically, gives its verdict in seconds, names the exact offending field, and points at the fix; a gate is a human decision that inserts queue time and, because approvers cannot check every field, tends to approve without reading. Most "must be reviewed" rules are actually invariants, and invariants belong in code.
- Layer the enforcement so it fails at the cheapest point: a linter or template default in the developer's editor and pull request, an admission or policy check at the cluster boundary that cannot be bypassed, and a continuous scan that finds resources created before the rule existed. Kubernetes gives concrete primitives — a `ResourceQuota` caps aggregate consumption per namespace and, importantly, forces every pod in that namespace to declare requests and limits once a compute quota exists, so the quota is both a limit and a conformance rule.
- Constraints: an enforced guardrail must ship with a documented exception path, an owner who can grant it, and an expiry on every exception, or teams will route around it. Quotas are per namespace and evaluated at admission, so they stop new objects rather than reclaiming existing ones, and a quota tightened below current usage leaves running workloads alive but blocks the next deploy — roll changes out in audit mode first and measure what would have failed.
- Failure modes: enforcing a rule nobody can satisfy on the paved road, which converts the guardrail into an approval queue anyway; a policy whose message says "denied by policy" with no field or remediation; blanket exemptions granted to the loudest team and never reviewed; a quota that silently blocks a scale-up during an incident; and enforcement that exists only in CI, so anything applied directly to the cluster bypasses it entirely.

## References

- [Kubernetes resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- Further reading (blog): [Kubernetes blog](https://kubernetes.io/blog/)

## What to learn next

- Official documentation: [Kubernetes resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- Manual or specification: [Kubernetes limit ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes — share a cluster with namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)
