---
title: Enforce Kubernetes Pod Security Standards
theme: security
difficulty: middle
type: scenario
tags: [security, kubernetes, containers, least-privilege]
sources:
  - url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Enforce Kubernetes Pod Security Standards

How would you prevent risky Pod configurations while preserving a path for justified exceptions?

## Answer guide

- Apply the Kubernetes Pod Security Standards at an appropriate baseline or restricted level through admission labels, then test workloads before moving enforcement from warn/audit mode.
- Require explicit security context choices such as non-root execution and restricted privilege escalation where the chosen standard demands them; use namespace boundaries and RBAC with the admission control.
- Document exception owners, scope, reason, expiry, and compensating controls; audit exceptions and remove them after migration.
- Admission does not secure images, RBAC, nodes, or network traffic. An abrupt restrictive rollout can block critical workloads, while permanent broad exemptions nullify the standard.

## References

- [Kubernetes: Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Kubernetes: Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
