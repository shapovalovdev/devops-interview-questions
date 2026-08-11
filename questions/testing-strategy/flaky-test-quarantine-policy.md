---
title: Define a flaky-test quarantine policy
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pytest.org/en/stable/how-to/skipping.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Define a flaky-test quarantine policy

Engineers have started adding `@pytest.mark.skip` to any test that fails intermittently, and the main suite is green again. Write the quarantine policy that replaces this, and say what stops quarantine from becoming a graveyard.

## Answer guide

- Quarantine is a routing decision, not a delete. A test entering quarantine is removed from the merge-blocking job and moved to a separate scheduled job that still runs it, records pass and fail history, and reports the flake rate. `skip` erases the signal entirely; a quarantine marker such as a `flaky` mark selected out of the gating run with `-m "not flaky"` keeps it. Record the entry with an owner, the linked defect, the observed failure rate, and an expiry date in the same commit, because an unowned quarantine is indistinguishable from a deletion.
- Entry needs a threshold rather than a judgement call: a test whose failure rate on unchanged code exceeds some small percentage over a rolling window — measured by rerunning the suite on the same commit, not by memory — qualifies. Exit needs one too: a fixed number of consecutive clean scheduled runs restores it to the gate. Expiry is the important half. When the deadline passes with no fix, the policy must force a decision, and deleting a test nobody will repair is a legitimate outcome as long as the risk it covered is written down.
- Cap the blast radius. Enforce a maximum share of the suite that may sit in quarantine at once and fail the pipeline when it is exceeded, otherwise quarantine absorbs regressions faster than anyone fixes them. Exclude tests covering the journeys you would page for: if the only coverage of checkout is quarantined, the correct action is to fix or replace it, not to ship without it. Never let quarantine status be set outside version control, because a dashboard toggle leaves no review trail.
- Failure modes: a flaky test that was reporting a genuine race, quarantined and then closed as a test defect; retries layered on top of quarantine so a test has to fail three times to be noticed at all; quarantine growth that tracks release pressure rather than test quality; and the scheduled quarantine job itself going unwatched, so nothing observes the tests that were supposed to still be running.

## References

- [pytest — how to skip tests and mark expected failures](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Further reading (blog): [Google Testing Blog — test flakiness, one of the main challenges of automated testing](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — eradicating non-determinism in tests](https://martinfowler.com/articles/nonDeterminism.html)
- Technical blog: [Google Testing Blog — test flakiness, one of the main challenges of automated testing](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html)
- Hands-on guide: [pytest — how to skip tests and mark expected failures](https://docs.pytest.org/en/stable/how-to/skipping.html)
