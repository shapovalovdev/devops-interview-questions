---
title: Design isolated test data
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pytest.org/en/stable/how-to/fixtures.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch13.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design isolated test data

You enable `pytest -n 16` and the suite starts failing randomly: unique-constraint violations, tests seeing rows they did not create, and a fixture that passes alone and fails in a full run. What is colliding, and how do you make each test's data its own?

## Answer guide

- Three things collide under parallelism: fixed identifiers, shared mutable rows, and shared global state such as a cache, a temp directory, or a clock. Fix the first by generating identifiers per test rather than hardcoding `user@example.com` or `id=1`. Fix the second by choosing an isolation mechanism rather than a cleanup convention — truncating tables between tests is the classic mistake, because in a parallel run one worker's truncate deletes another worker's rows, which is exactly the pattern that passes alone and fails in a full run.
- Two mechanisms work, with different costs. Transactional rollback wraps each test in a transaction the fixture never commits: fast, needs no per-test setup, but it breaks when the code under test manages its own transactions or relies on committed visibility across connections. A schema or database per worker is heavier — pytest-xdist exposes the worker ID so the fixture can pick `test_gw3` — but it survives real commits and lets you test migrations. Pick one deliberately, run the migration once per schema rather than per test, and use function-scoped fixtures for the data with session-scoped fixtures for the expensive container.
- Isolation has to extend past the database. Give each worker its own Redis logical database or key prefix, its own temp directory via `tmp_path`, its own message-queue topic or consumer group, and monkeypatch anything reading a real clock or `random` without a seed. Ordering dependence is the residual symptom: randomise test order with a plugin such as pytest-randomly, reproduce any failure by pinning the reported seed, and treat a test whose result depends on its position as broken rather than as a parallelism problem.
- Fixtures also carry a data-protection obligation. Seeding from a production dump so the fixtures look realistic puts personal data on every developer machine and in CI logs, where it is neither inventoried nor deleted. Generate synthetic data with a factory, or use a masked extract produced by an owned job. Failure modes to expect: a factory that reuses a sequence across workers so identifiers still collide, a shared object cached at module import so the second test in a worker sees the first's state, and per-test container startup that makes the parallel suite slower than the serial one it replaced.

## References

- [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Further reading (blog): [Google Testing Blog — keep tests focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html)

## What to learn next

- Official documentation: [Testcontainers — guides](https://testcontainers.com/guides/)
- Manual or specification: [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Maintainer or personal blog: [Martin Fowler — object mother](https://martinfowler.com/bliki/ObjectMother.html)
- Technical blog: [Google Testing Blog — keep tests focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html)
- Hands-on guide: [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
