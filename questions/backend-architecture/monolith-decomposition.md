---
title: Decompose a monolith without a rewrite
theme: backend-architecture
difficulty: senior
type: scenario
tags: [dependencies, deployment, reliability]
sources:
  - url: https://martinfowler.com/articles/break-monolith-into-microservices.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Decompose a monolith without a rewrite

How would you extract a service from a monolith while keeping delivery safe?

## Answer guide

- Choose a bounded business capability with clear ownership, a small dependency surface, and a measurable reason to change. Introduce an interface, move the capability and its data responsibility incrementally, and redirect callers after proving parity.
- Treat data ownership, authentication, observability, deployment, and incident response as part of the extraction, not cleanup work. Maintain a migration ledger, compatibility tests, rollback route, and SLO comparison while traffic is moved gradually.
- Splitting code while retaining shared tables and synchronous internal calls creates a distributed monolith. A big-bang rewrite delays feedback; use strangler steps and test failure, partial rollout, and reconciliation before deleting the old path.

## References

- [Martin Fowler: breaking a monolith into microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html)
- Further reading (personal blog): [Martin Fowler's blog](https://martinfowler.com/)

## What to learn next

- Official documentation: [Kubernetes service concepts](https://kubernetes.io/docs/concepts/services-networking/service/)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [Shopify Engineering](https://shopify.engineering/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
