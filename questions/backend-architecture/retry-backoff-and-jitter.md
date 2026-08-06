---
title: Make backend retries safe
theme: backend-architecture
difficulty: middle
type: troubleshooting
tags: [reliability, availability, http]
sources:
  - url: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Make backend retries safe

How should a service retry a transient dependency failure without amplifying an incident?

## Answer guide

- Retry only failures that are plausibly transient and only operations with idempotent semantics or a durable idempotency key. Use bounded exponential backoff with jitter, a deadline, an attempt budget, and metrics for retries and final outcomes.
- Set timeouts from a service-level latency budget and propagate cancellation or deadlines downstream. Separate client retry policy from server overload protection, and prefer a queue or explicit repair process for work that outlives the request.
- Retrying every error turns a dependency outage into a retry storm and can duplicate side effects. Fixed synchronized delays create a thundering herd; exercise failures such as timeout-after-success, rate limiting, and partial network partition.

## References

- [AWS Builders' Library: retries and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- Further reading (personal blog): [Stripe: idempotency](https://stripe.com/blog/idempotency)

## What to learn next

- Official documentation: [gRPC deadlines](https://grpc.io/docs/guides/deadlines/)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
