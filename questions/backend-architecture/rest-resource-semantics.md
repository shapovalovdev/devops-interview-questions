---
title: Design resource-oriented HTTP endpoints
theme: backend-architecture
difficulty: junior
type: theory
tags: [http, networking, dependencies]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9110
    source_type: standard
    verified_on: 2026-08-06
---

# Design resource-oriented HTTP endpoints

How should a backend map operations to HTTP resources and methods?

## Answer guide

- Model stable domain resources with clear identifiers and use HTTP method semantics deliberately: safe methods do not request state change, while PUT and DELETE are idempotent in the HTTP definition. Return status codes and representations that explain the result.
- Define validation errors, authorization behavior, pagination, conditional updates, and a consistent error shape before clients integrate. Document media types and required headers so clients do not infer behavior from one implementation.
- Do not assume a method automatically makes an implementation safe. A proxy retry, cache, or client can expose incorrect side effects; protect mutations with validation, concurrency control, and tests for duplicate or out-of-order requests.

## References

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Further reading (personal blog): [Stripe: idempotency](https://stripe.com/blog/idempotency)

## What to learn next

- Official documentation: [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Brandur Leach's blog](https://brandur.org/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [OpenAPI learning](https://learn.openapis.org/)
