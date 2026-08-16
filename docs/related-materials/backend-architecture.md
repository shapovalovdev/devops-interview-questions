# Backend architecture: related materials

Use the question-level links for a focused route through API, persistence, and reliability topics. The Google SRE Book is free to read from its publisher; this repository does not link to unauthorized copies of commercial books.

## What to learn next

- Official documentation: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

The reading spine walks the backend path first — stateless service, the API
fork, the transaction sequence — before widening to the boundary questions and
the portfolio tier that presupposes a running system.

1. [Design a stateless backend service](../../questions/backend-architecture/stateless-service-design.html)
    — The spine opens by naming what stays out of the request process, because
    every later pattern coordinates state that already left.
2. [Choose synchronous versus asynchronous API processing](../../questions/backend-architecture/synchronous-versus-asynchronous-api.html)
    — The synchronous-asynchronous fork is the first real design decision, and
    the queueing and outbox stages live on its asynchronous branch.
3. [Design resource-oriented HTTP endpoints](../../questions/backend-architecture/rest-resource-semantics.html)
    — Resource-oriented endpoints settle the API surface before its failure
    modes arrive.
4. [Separate authentication from authorization](../../questions/backend-architecture/authentication-authorization-boundary.html)
    — Separating authentication from authorization completes the surface and
    prevents the conflation the boundary questions would inherit.
5. [Choose a transaction boundary](../../questions/backend-architecture/transaction-boundaries.html)
    — The transaction sequence starts here because the unit it defines is what
    retries and idempotency keys repeat.
6. [Make backend retries safe](../../questions/backend-architecture/retry-backoff-and-jitter.html)
    — A retry is only affordable once the unit it repeats is short, which is
    exactly why boundaries come first.
7. [Implement idempotency keys for mutations](../../questions/backend-architecture/idempotency-keys.html)
    — Keys turn safe retries into a production contract for mutations, directly
    after the retry discipline they serve.
8. [Use a transactional outbox for event publication](../../questions/backend-architecture/transactional-outbox.html)
    — The outbox only makes sense once you have felt the dual-write it fixes, so
    it follows boundaries, retries, and keys.
9. [Coordinate a saga with compensations](../../questions/backend-architecture/saga-compensation.html)
    — Compensation extends atomicity across services and presumes the outbox's
    guaranteed events as its transport.
10. [Operate a circuit breaker](../../questions/backend-architecture/circuit-breaker-operations.html)
    — Operating the breaker after the retries it judges keeps the operator
    honest about what it masks.
11. [Explain the role of an API gateway](../../questions/backend-architecture/api-gateway-basics.html)
    — The gateway is the first boundary question, consuming the API surface
    settled at the start of the spine.
12. [Govern API versioning and deprecation](../../questions/backend-architecture/api-versioning-policy.html)
    — Versioning and deprecation govern how the surface may change without
    breaking the contracts above.
13. [Design an API rate-limiting policy](../../questions/backend-architecture/rate-limiting-policy.html)
    — Rate limiting protects the settled surface under load, a policy question
    once gateway and versioning exist.
14. [Design cursor pagination](../../questions/backend-architecture/cursor-pagination.html)
    — Cursor pagination fixes the one read pattern offset paging quietly breaks
    at scale.
15. [Design multi-tenant isolation](../../questions/backend-architecture/multi-tenancy-isolation.html)
    — Tenant isolation widens the boundary questions from per-request
    correctness to per-customer state.
16. [Design a durable background job contract](../../questions/backend-architecture/background-job-contract.html)
    — The durable background job gives the asynchronous fork from step two its
    own operable contract.
17. [Design a developer-portal catalog contract teams can trust](../../questions/backend-architecture/developer-portal-catalog-contract.html)
    — The catalog makes service boundaries discoverable, which only matters once
    those boundaries exist to publish.
18. [Decompose a monolith without a rewrite](../../questions/backend-architecture/monolith-decomposition.html)
    — Decomposition opens the portfolio tier by re-cutting a running system
    along the seams the spine taught.
19. [Set platform and product-service boundaries](../../questions/backend-architecture/platform-boundary-strategy.html)
    — Platform and product-service boundaries decide which side of each seam
    owns what, after decomposition shows what bad seams cost.
20. [Design cache invalidation for mutable data](../../questions/backend-architecture/cache-invalidation-strategy.html)
    — Invalidation for mutable data is the hardest boundary to hold and presumes
    the seam that owns the data.
21. [Manage an architecture decision portfolio](../../questions/backend-architecture/architecture-decision-portfolio.html)
    — A decision portfolio governs the record of choices the tiers above kept
    making implicitly.
22. [Govern evolutionary backend architecture](../../questions/backend-architecture/evolutionary-architecture-governance.html)
    — Evolutionary governance makes change itself a managed process rather than
    a series of surprises.
23. [Prioritize backend resilience investments](../../questions/backend-architecture/resilience-investment-model.html)
    — Prioritizing resilience investments is last because it prices everything
    the Theme has built.
