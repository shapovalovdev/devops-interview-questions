# Testing strategy: related materials

Use these alongside the testing-strategy Questions. They orient the whole Theme rather than any single Question: where the boundaries between unit, integration, and end-to-end tests fall, what a suite costs to run, and when confidence has to come from production evidence instead of a pre-merge gate. The per-Question links go deeper into contract testing, test data, release gates, and quality investment. "Software Engineering at Google" is free to read from its publisher; this repository does not link to unauthorized copies of commercial books.

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [Testcontainers — getting started](https://testcontainers.com/getting-started/)

## Suggested study order

Grow outward from the unit test: design one focused test, name it so it
diagnoses, and set pyramid boundaries that say where it stops. Coverage as a
signal and mutation-testing trade-offs calibrate that layer before it grows;
isolated test data and safe data management keep it honest. Integration is the
next ring — boundaries first, then data contracts, then contract tests between
services and consumer-driven contracts, which only have something to verify
once the boundaries exist. End-to-end scope control, ephemeral environments,
shared-environment policy, and the flaky-test quarantine govern the ring where
cost explodes. Then release: gates as risk controls, performance tests placed
in CI, shadow traffic, production experiment guardrails, security boundaries,
and accessibility strategy — different risks, the same shape of decision. Close
with what keeps suites alive for years: making test failures observable,
modelling execution cost, suite policy and ownership, and the
quality-investment portfolio.
