---
title: Why should CI publish immutable release artifacts?
theme: ci-cd
difficulty: middle
type: theory
tags: [ci-cd, delivery, supply-chain, security]
---

# Why should CI publish immutable release artifacts?

Why is rebuilding “the same version” at deployment time risky, and what traceability should a release artifact provide?

## Answer guide

- Build once and promote the exact artifact through environments.
- Use an immutable digest or identifier linked to the source revision and build metadata.
- This supports reproducible rollback, auditability, and supply-chain verification.
