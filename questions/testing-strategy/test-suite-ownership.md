---
title: Assign test suite ownership
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://backstage.io/docs/features/software-catalog/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Assign test suite ownership

A cross-cutting end-to-end suite has been failing for nine days. Every team says the failing test is not theirs, and the platform team that built the harness has no context on the assertion. How do you make ownership real?

## Answer guide

- Ownership has to resolve to a team with an on-call route, and it has to be derivable from the failing artifact without a conversation. Put it in two places that cannot drift apart: CODEOWNERS entries covering the test directories so a change requires the owning team's review, and a service catalog such as Backstage where the suite is a component with an owner, a lifecycle, and declared dependencies on the services it exercises. A failure notification that names a team and a channel is the difference between nine days and one.
- Split ownership by concern rather than by file. The platform team owns the harness — runners, fixtures, environment provisioning, reporting, flake detection — and is accountable for the suite being runnable and its results trustworthy. The team owning the behaviour under test owns each individual assertion and is accountable for it passing. Cross-cutting journeys that genuinely span teams need a single named owner for the journey, chosen deliberately, because a test owned by everyone is owned by no one and that is the exact state described.
- Back it with a service level and a policy that fires automatically. State a maximum time a test may stay red before it is quarantined or deleted, route the alert to the owner rather than to a shared channel, and escalate on a schedule rather than waiting for someone to notice. Publish per-suite health — pass rate, flake rate, runtime, mean time to green — attributed to the owning team, since ownership without a visible metric decays back to the loudest engineer taking it on.
- Failure modes: CODEOWNERS pointing at a team that was reorganised away, so review requests go nowhere and merges bypass the intent; a catalog entry with an owner field nobody maintains; ownership assigned to an individual who then leaves; the platform team absorbing assertion failures because it is faster than chasing the owner, which permanently removes the incentive to fix them; and blocking every team's merges on a suite none of them owns, which reliably ends with the gate being made advisory.

## References

- [GitHub Docs — about code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Backstage — software catalog](https://backstage.io/docs/features/software-catalog/)
- Further reading (blog): [Google Testing Blog — flaky tests at Google and how we mitigate them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html)

## What to learn next

- Official documentation: [Backstage — software catalog](https://backstage.io/docs/features/software-catalog/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — Conway's law](https://martinfowler.com/bliki/ConwaysLaw.html)
- Technical blog: [Google Testing Blog — flaky tests at Google and how we mitigate them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html)
- Hands-on guide: [GitHub Docs — about code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
