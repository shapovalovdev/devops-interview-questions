---
title: Adopt consumer-driven contracts
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Adopt consumer-driven contracts

How should a team make this testing strategy decision?

## Answer guide

- Define the risk and decision the check supports before selecting a tool or metric.
- Keep test data, dependencies, and ownership explicit so the result remains reproducible.
- Balance execution cost against feedback speed and failure diagnosis; use multiple signals for release decisions.
- Reassess after incidents and product changes because a useful test boundary can become misleading as systems evolve.
- Publish versioned expectations from real consumers, run provider verification in the delivery path, and agree on deprecation windows before removing fields or behavior. Contract checks complement—not replace—end-to-end evidence for authentication, deployment configuration, and production traffic behavior.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [Pact documentation](https://docs.pact.io/)
- Manual or specification: [Pact specification](https://github.com/pact-foundation/pact-specification)
- Maintainer or personal blog: [Ian Robinson — consumer-driven contracts, a service evolution pattern](https://martinfowler.com/articles/consumerDrivenContracts.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Pact — five-minute getting started guide](https://docs.pact.io/5-minute-getting-started-guide)
