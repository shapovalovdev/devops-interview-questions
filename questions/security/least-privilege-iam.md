---
title: Apply least privilege to a workload identity
theme: security
difficulty: middle
type: scenario
tags: [security, iam, least-privilege, cloud]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: standard
    verified_on: 2026-08-06
---

# Apply least privilege to a workload identity

How would you give a service access to one production queue without granting broad cloud credentials?

## Answer guide

- Give the workload a distinct non-human identity and a policy limited to the queue, required actions, environment, and conditions; deny unrelated administrative operations.
- Issue short-lived credentials through the platform identity mechanism instead of embedding a long-lived key. Bind trust to the specific workload and deployment context.
- Test allowed and denied paths, log use, and review permissions after service changes. Separate deployment identity from runtime identity.
- Wildcards, shared roles, or credentials copied into CI turn a narrow grant into broad compromise. A policy that is too narrow can also cause outage-driven privilege escalation, so provide a reviewed exception route.

## References

- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [AWS IAM: Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
