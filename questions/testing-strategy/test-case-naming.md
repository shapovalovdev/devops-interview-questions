---
title: Name test cases for diagnosis
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pytest.org/en/stable/explanation/goodpractices.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch12.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Name test cases for diagnosis

A CI run fails with `test_process_2 FAILED` in a file of forty similar names, and the on-call engineer has to open the source and read the fixtures to find out what broke. What should the name have told them, and how do you get there?

## Answer guide

- A failing test's name is the first line of the incident report, so it should carry the unit under test, the condition, and the expected behaviour without anyone opening the file: `test_refund_rejects_amount_greater_than_original_charge` rather than `test_refund_2`. Read as a sentence it states the requirement, which means the name doubles as the specification and a reviewer can tell from the list alone which behaviours are covered and which are missing. Names describing mechanics — `test_happy_path`, `test_process_2`, `test_bug_4471` — force the reader back into the source every time.
- Get the rest of the diagnosis from structure rather than from a longer name. Group related cases in a class or module named after the unit so the fully qualified `TestRefund::test_rejects_amount_over_original` reads as a path, and use parametrisation with explicit case identifiers — pytest's `ids` argument, or an `id` per entry — so a failing case reports `[amount_zero]` instead of `[3]`. Assertion messages carry the values; the name carries the intent, and mixing the two produces names nobody maintains.
- Constraints worth stating: names are code and drift like code, so a test named for a behaviour that was renamed two refactors ago is worse than a vague one. Keep the name coupled to observable behaviour rather than to internal function names, so a refactor does not invalidate every name. Ticket numbers belong in a docstring or comment where the context lives, not in the identifier, because the tracker they point at outlives neither the ticket nor the reader's access to it.
- Failure modes: names that describe the setup instead of the assertion, so two tests with different expectations end up nearly identically named; a `should_work` suffix pattern that survives long enough to become house style; parametrised cases with generated indices, which make a flaky case impossible to reference in a bug report; and long descriptive names on tests that assert five unrelated things, where no name could be accurate because the test itself has no single subject.

## References

- [pytest — good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Further reading (blog): [Google Testing Blog — writing descriptive test names](https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Maintainer or personal blog: [Vladimir Khorikov — you are naming your tests wrong](https://enterprisecraftsmanship.com/posts/you-naming-tests-wrong/)
- Technical blog: [Google Testing Blog — writing descriptive test names](https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html)
- Hands-on guide: [pytest — good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
