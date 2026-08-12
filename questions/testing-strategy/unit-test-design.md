---
title: Design a focused unit test
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://abseil.io/resources/swe-book/html/ch12.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.pytest.org/en/stable/how-to/fixtures.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design a focused unit test

A test calls the function under test, then asserts on six unrelated fields, and its setup is a helper shared with twenty other tests that nobody dares change. Rewrite the design rules that would have prevented this, and say where they conflict with DRY.

## Answer guide

- One test should establish one behaviour, so its failure names the defect. Keep the arrange, act, assert structure visible, act exactly once, and assert on the one outcome the test exists to protect; the six unrelated assertions are six tests wearing one name, and when the second fails you never learn whether the fourth would have. Assert on observable behaviour — the return value, the raised exception, the message published — not on how the code reached it, or the test blocks the refactor it was supposed to make safe.
- Test code optimises for a different property than production code: it should be obvious in isolation, which is why the guidance is DAMP rather than DRY. The shared setup helper that nobody dares change is the standard end state of applying DRY to fixtures — a reader must open it to know what the test assumes, and a change for one test silently alters twenty. Prefer inlining the values that matter to the assertion, keep the fixture for genuinely expensive or incidental setup, and use small builders with defaults so each test overrides only the field it cares about.
- Use fixtures for what they are good at: pytest fixtures are dependency injection with a scope, so a session-scoped fixture can hold an expensive resource while a function-scoped one hands each test its own data. Compose them rather than growing one god fixture, and prefer `tmp_path` and monkeypatching over globals so nothing leaks between tests. Determinism is a design requirement, not a nice-to-have — inject the clock, seed the randomness, and avoid real sleeps, because a test that depends on timing will eventually fail for a reason unrelated to the code.
- Failure modes: mocking every collaborator until the test asserts only that the mocks were called, so it passes against a broken implementation; asserting on log output or private attributes, which makes an internal rename a red build; a helper that both sets up and asserts, hiding the actual expectation from the test body; and conditionals or loops inside a test, which mean either the test can pass without testing anything or it is really several tests that should be parametrised.

## References

- [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- Further reading (blog): [Google Testing Blog — tests too DRY? make them DAMP!](https://testing.googleblog.com/2019/12/testing-on-toilet-tests-too-dry-make.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Maintainer or personal blog: [Martin Fowler — unit test](https://martinfowler.com/bliki/UnitTest.html)
- Technical blog: [Google Testing Blog — tests too DRY? make them DAMP!](https://testing.googleblog.com/2019/12/testing-on-toilet-tests-too-dry-make.html)
- Hands-on guide: [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
