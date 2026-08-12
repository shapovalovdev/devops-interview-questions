---
title: Set test-suite execution policy
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.github.com/en/actions
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.pytest.org/en/stable/how-to/mark.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set test-suite execution policy

Your GitHub Actions pull-request job runs the whole 40-minute suite on every push, including the tests that need a live third-party sandbox. Write the policy for which tests run on which trigger, and how the pipeline knows.

## Answer guide

- Make the selection a property of the tests themselves rather than a list in the workflow file. Tag each test with a pytest marker declaring what it needs — `unit`, `db`, `external`, `slow` — register the markers in configuration so a typo fails rather than silently selecting nothing, and let each job choose with `-m`. The pull-request job runs `-m "not external and not slow"`, a merge-queue or main-branch job runs everything, and the sandbox-dependent tests run on a schedule. The workflow then never needs updating when a test is added.
- Design each trigger around a feedback budget and what a failure means there. A pull-request job should be fast enough that engineers wait for it — a target in the ten-minute range — because past that they context-switch and the signal stops changing behaviour, so shard across a matrix and cache dependencies to stay inside it. The main-branch or merge-queue job is where the expensive and less deterministic tests belong, since a failure there blocks a release rather than a review. Scheduled runs cover anything whose failure is not attributable to a single change.
- Say what happens when a stage is skipped or fails. Path filters that skip a suite must be conservative — a change to a shared library or a lockfile invalidates the filter — and required status checks have to be defined so a skipped job does not report success and let an unreviewed path merge. Concurrency groups should cancel superseded runs on the same pull request but never on the protected branch. Third-party sandboxes usually rate-limit or serialise, so those jobs need a concurrency limit of one and a documented owner for the credentials.
- Failure modes: markers that drift, so `slow` tests accumulate in the fast job until it is no longer fast; a scheduled job whose failures notify a channel nobody reads, meaning the expensive tier is effectively off; path filtering that hides a break until release day; and blanket retries at the job level, which convert a real intermittent product defect into a green run and destroy the flake statistics you would need to find it.

## References

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [pytest — how to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html)
- Further reading (blog): [Slack Engineering — handling flaky tests at scale](https://slack.engineering/handling-flaky-tests-at-scale-auto-detection-suppression/)

## What to learn next

- Official documentation: [GitHub Actions documentation](https://docs.github.com/en/actions)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler — on the diverse and fantastical shapes of testing](https://martinfowler.com/articles/2021-test-shapes.html)
- Technical blog: [Slack Engineering — handling flaky tests at scale](https://slack.engineering/handling-flaky-tests-at-scale-auto-detection-suppression/)
- Hands-on guide: [pytest — how to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html)
