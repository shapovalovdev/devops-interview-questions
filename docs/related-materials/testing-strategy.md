# Testing strategy: related materials

Use these alongside the testing-strategy Questions. They orient the whole Theme rather than any single Question: where the boundaries between unit, integration, and end-to-end tests fall, what a suite costs to run, and when confidence has to come from production evidence instead of a pre-merge gate. The per-Question links go deeper into contract testing, test data, release gates, and quality investment. "Software Engineering at Google" is free to read from its publisher; this repository does not link to unauthorized copies of commercial books.

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [Testcontainers — getting started](https://testcontainers.com/getting-started/)

## Suggested study order

Grow outward from the unit test: each ring only earns its cost once the ring
inside it is honest.

1. [Design a focused unit test](../../questions/testing-strategy/unit-test-design.html)
    — Grow outward from the unit test: one focused test is the atom of the
    suite.
2. [Name test cases for diagnosis](../../questions/testing-strategy/test-case-naming.html)
    — A test named for diagnosis fails helpfully instead of mysteriously.
3. [Define test-pyramid boundaries](../../questions/testing-strategy/test-pyramid-boundaries.html)
    — Pyramid boundaries say where the unit layer stops and cost begins.
4. [Treat coverage as a testing signal](../../questions/testing-strategy/test-coverage-signal.html)
    — Coverage as a signal calibrates the layer before it grows any further.
5. [Evaluate mutation testing trade-offs](../../questions/testing-strategy/mutation-testing-tradeoffs.html)
    — Mutation testing prices what the coverage number actually proves.
6. [Design isolated test data](../../questions/testing-strategy/test-data-isolation.html)
    — Isolated test data keeps the unit layer honest under repetition.
7. [Manage test data safely](../../questions/testing-strategy/test-data-management.html)
    — Safe data management governs everything the tests consume.
8. [Choose integration test boundaries](../../questions/testing-strategy/integration-test-boundaries.html)
    — Integration is the next ring, with boundaries chosen first.
9. [Define integration test data contracts](../../questions/testing-strategy/integration-test-data-contract.html)
    — Data contracts make those integration boundaries actually testable.
10. [Use contract tests between services](../../questions/testing-strategy/contract-testing-boundaries.html)
    — Contract tests verify a boundary from both of its sides.
11. [Adopt consumer-driven contracts](../../questions/testing-strategy/consumer-driven-contracts.html)
    — Consumer-driven contracts only have something to verify once the
    boundaries exist.
12. [Control end-to-end test scope](../../questions/testing-strategy/end-to-end-test-scope.html)
    — Scope control keeps the expensive ring from exploding.
13. [Design ephemeral test environments](../../questions/testing-strategy/ephemeral-test-environments.html)
    — Ephemeral environments give every run its own disposable world.
14. [Set shared test environment policy](../../questions/testing-strategy/shared-test-environment-policy.html)
    — The shared-environment policy governs the world that cannot be ephemeral.
15. [Define a flaky-test quarantine policy](../../questions/testing-strategy/flaky-test-quarantine-policy.html)
    — The flaky quarantine keeps the suite's confidence measurable.
16. [Design release gates as risk controls](../../questions/testing-strategy/release-gate-design.html)
    — Release opens with gates treated as risk controls rather than rituals.
17. [Place performance tests in CI](../../questions/testing-strategy/performance-tests-in-ci.html)
    — Performance tests in CI prove only what they can honestly prove.
18. [Use shadow traffic safely](../../questions/testing-strategy/shadow-traffic-testing.html)
    — Shadow traffic rehearses production without betting the production on it.
19. [Set production experiment guardrails](../../questions/testing-strategy/production-experiment-guardrails.html)
    — Production experiments run inside guardrails or they do not run.
20. [Set security testing boundaries](../../questions/testing-strategy/security-test-boundaries.html)
    — Security testing boundaries keep the tests from becoming the attack.
21. [Design accessibility testing strategy](../../questions/testing-strategy/accessibility-test-strategy.html)
    — Accessibility strategy is a different risk with the same shape of
    decision.
22. [Make test failures observable](../../questions/testing-strategy/test-observability.html)
    — Suites stay alive for years only when failures are observable.
23. [Model test execution cost](../../questions/testing-strategy/test-execution-cost-model.html)
    — Execution cost is modelled rather than discovered at release time.
24. [Set test-suite execution policy](../../questions/testing-strategy/test-suite-execution-policy.html)
    — Execution policy decides what runs when, and who waits for it.
25. [Assign test suite ownership](../../questions/testing-strategy/test-suite-ownership.html)
    — Ownership assigns who answers when the policy fires red.
26. [Prioritize quality investment portfolio](../../questions/testing-strategy/quality-investment-portfolio.html)
    — The quality-investment portfolio closes the Theme by pricing all of it.
