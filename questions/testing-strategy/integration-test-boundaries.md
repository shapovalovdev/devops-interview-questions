---
title: Choose integration test boundaries
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://testcontainers.com/guides/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch13.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Choose integration test boundaries

An order service talks to Postgres, a payment provider, and a Kafka topic. For each dependency you must choose a real instance, a fake, or a mock. How do you decide, and what does each choice cost?

## Answer guide

- Use the real thing when the dependency's own behaviour is part of what you are testing. Postgres qualifies: transaction isolation, constraint violations, `ON CONFLICT` semantics, JSON operators, and query plans are exactly what a double will get wrong, so run it as a container against the same image digest production uses. Kafka is a middle case — a real broker is worth it when you test consumer group rebalancing, offset commit behaviour, or ordering guarantees, and overkill when you are only checking that a serialiser produces the right bytes.
- Prefer a fake over a mock for anything you cannot run. A fake is a working implementation with a shortcut, such as an in-memory ledger for the payment provider that enforces the same idempotency-key and state-machine rules; it is testable in its own right and can be verified against the provider's sandbox on a schedule. A mock asserting the exact call sequence is the last resort, because it encodes your current belief about the collaborator rather than its behaviour and passes happily after the real API changes.
- Constraints follow from ownership. Anything owned by another team should be reached through a contract test rather than pulled into your integration test, so the shared external dependency stays outside your boundary. Where you must use a fake for a third party, the fake becomes something you own and can be wrong about, so pin the provider's sandbox to a nightly job as the thing that detects drift. Keep each test's boundary small enough that a failure names one collaborator, not five.
- Failure modes: a mock returning a response shape the provider stopped sending two releases ago, so every test passes while production 500s; a fake whose error behaviour is too polite, hiding the timeout and rate-limit paths that dominate real incidents; a suite that runs the whole dependency graph and becomes a slow, flaky pseudo end-to-end test; and truncating tables between tests instead of rolling back, which silently serialises a parallel run.

## References

- [Testcontainers — guides](https://testcontainers.com/guides/)
- [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Further reading (blog): [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)

## What to learn next

- Official documentation: [Testcontainers — guides](https://testcontainers.com/guides/)
- Manual or specification: [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Maintainer or personal blog: [Martin Fowler — integration test](https://martinfowler.com/bliki/IntegrationTest.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Testcontainers — getting started](https://testcontainers.com/getting-started/)
