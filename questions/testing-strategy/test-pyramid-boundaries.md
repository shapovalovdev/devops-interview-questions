---
title: Define test-pyramid boundaries
theme: testing-strategy
difficulty: junior
type: theory
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Define test-pyramid boundaries

Two engineers disagree about whether a test that starts a real Postgres container is a unit test or an integration test. What is the pyramid actually claiming, and what rule decides which layer a given test belongs in?

## Answer guide

- The pyramid is a claim about cost and about where a failure points, not a rule about counts. Tests lower down run faster, cost less, and localise a defect to a small amount of code; tests higher up exercise more real integration but are slower, more failure-prone, and tell you only that something in the system is wrong. The advice that follows is to write the cheapest test that can observe the failure you actually care about; the triangular shape is a consequence of doing that, not a target to hit.
- The unit-versus-integration argument is unproductive because the terms have no agreed definition. Google's size taxonomy replaces them with something mechanically checkable: a small test runs in one process with no sleeps, no network I/O, and no filesystem access; a medium test may span processes on localhost; a large test may reach remote machines. Under that rule the Postgres container is a medium test and the disagreement disappears. The classification is useful precisely because it predicts the two things you care about — runtime and flakiness — instead of describing intent.
- So pick the layer from the failure you are trying to catch. If the defect is in one module's logic and is visible without a collaborator, it belongs in a small test. If it only appears against a real dependency's semantics — SQL constraint behaviour, serialisation, framework wiring — a medium test is the cheapest thing that can see it, and using a mock there simply moves the bug out of view. Reserve large tests for risks that are genuinely properties of the assembled system: routing, authentication, configuration, deployment topology.
- Failure modes: the ice-cream cone, where a slow browser suite does the work the middle layer should, so every regression costs a full run to diagnose; small tests that mock every collaborator until they assert only that the mocks were called, producing a healthy-looking pyramid over a broken integration; deleting valuable higher-level tests to fix the ratio, which optimises the picture rather than the risk; and applying the canonical shape to a thin orchestration service whose real risk is integration, where the middle layer legitimately dominates.

## References

- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [pytest — how-to guides](https://docs.pytest.org/en/stable/how-to/index.html)
