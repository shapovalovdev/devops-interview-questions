# Backend architecture: related materials

Use the question-level links for a focused route through API, persistence, and reliability topics. The Google SRE Book is free to read from its publisher; this repository does not link to unauthorized copies of commercial books.

## What to learn next

- Official documentation: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

The reading spine is the one the backend path walks first: what a stateless
service keeps out of the request process, then the
synchronous-versus-asynchronous fork, because every later pattern is
coordination of state that already left. Settle the API surface next —
resource-oriented endpoints, authentication separated from authorization —
before its failure modes arrive. The transaction sequence then runs in strict
order: transaction boundaries, safe retries, idempotency keys, the
transactional outbox, and saga compensation, since a retry is only affordable
once the unit it repeats is short and keyed, and an outbox only makes sense
once you have felt the dual-write it fixes. Operate the circuit breaker after
the retries it judges. Then widen to the boundary questions — the API gateway,
versioning and deprecation, rate limiting, cursor pagination, multi-tenant
isolation, the durable background job contract, and the developer-portal
catalog — and finish with the portfolio tier: monolith decomposition, platform
and product-service boundaries, cache invalidation for mutable data, and the
architecture-decision, evolutionary-governance, and resilience-investment
questions that presuppose a running system to govern.
