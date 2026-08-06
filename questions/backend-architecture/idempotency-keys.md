---
title: Implement idempotency keys for mutations
theme: backend-architecture
difficulty: middle
type: scenario
tags: [http, databases, reliability]
sources:
  - url: https://docs.stripe.com/api/idempotent_requests
    source_type: official-docs
    verified_on: 2026-08-06
---

# Implement idempotency keys for mutations

How should a payment-like mutation remain safe when a client retries after an ambiguous failure?

## Answer guide

- Require a client-generated key scoped to the authenticated caller and operation, persist it with a request fingerprint and final outcome before exposing a result. A retry with the same key and equivalent payload returns the recorded outcome instead of repeating a side effect.
- Set an explicit retention period, collision behavior, concurrency rule, and observability fields. Couple the idempotency record transactionally to the business write where possible, or document the recovery process for a crash between them.
- Never silently accept the same key with changed parameters. Missing atomicity or premature expiry can double-charge or duplicate work; test simultaneous retries, timeout-after-commit, and a worker restart.

## References

- [Stripe: idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- Further reading (personal blog): [Stripe: designing with idempotency](https://stripe.com/blog/idempotency)

## What to learn next

- Official documentation: [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Brandur Leach's blog](https://brandur.org/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [Stripe API request guide](https://docs.stripe.com/api)
