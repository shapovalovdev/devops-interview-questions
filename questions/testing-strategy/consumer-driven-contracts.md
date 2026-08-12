---
title: Adopt consumer-driven contracts
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pact.io/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://github.com/pact-foundation/pact-specification
    source_type: standard
    verified_on: 2026-08-10
---

# Adopt consumer-driven contracts

Six client teams consume your payments API, and testing them together in shared staging is now the slowest step in every release. What does adopting Pact-style consumer-driven contracts actually change, and what must the provider run for the scheme to hold?

## Answer guide

- Each consumer tests against a mock provider, and the framework records the requests its code really made and the response fields it really read into a pact file — a per-consumer subset of the API, never the whole specification. The provider then replays every consumer's pact against a running instance during verification, using provider states such as `given("a customer with id 42 exists")` to establish the data each interaction assumes. Neither side needs the other deployed to get the signal.
- The scheme only works with a broker in the middle. Pact Broker or PactFlow stores pacts tagged by consumer version and branch, records verification results, and answers `can-i-deploy`: has every consumer version currently running in the target environment been verified against the provider version about to ship? That query, run as a pipeline gate before deploy, is what actually replaces shared staging. Without it you have a pile of mock-based tests and a false sense of coverage.
- Constraints follow from the model. A consumer-driven contract covers only interactions some consumer exercised, so unused endpoints, fields nobody reads, and error paths nobody mocked stay untested and the provider still needs its own functional suite. Matchers matter too: asserting concrete values instead of types, via `like`, `eachLike`, or a regex matcher, makes pacts break on unrelated fixture changes until everyone learns to ignore them. And because you must be able to enumerate consumers, the pattern fits internal services far better than a public API.
- Failure modes: consumers writing pacts against an idealised API rather than the calls their client code emits, so the pact passes and production does not; provider states that drift away from the fixtures real requests hit; new pacts left permanently in pending mode so they never block the provider; verification wired as an informational job whose red result nobody sees; and a provider changing a response the pact never described, which is invisible until a consumer parses it.

## References

- [Pact documentation](https://docs.pact.io/)
- [Pact specification](https://github.com/pact-foundation/pact-specification)
- Further reading (blog): [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)

## What to learn next

- Official documentation: [Pact documentation](https://docs.pact.io/)
- Manual or specification: [Pact specification](https://github.com/pact-foundation/pact-specification)
- Maintainer or personal blog: [Ian Robinson — consumer-driven contracts, a service evolution pattern](https://martinfowler.com/articles/consumerDrivenContracts.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Pact — five-minute getting started guide](https://docs.pact.io/5-minute-getting-started-guide)
