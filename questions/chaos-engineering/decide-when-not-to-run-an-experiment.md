---
title: Decide when not to run a chaos experiment
theme: chaos-engineering
difficulty: staff
type: scenario
tags: [chaos-engineering, governance, change-management, reliability]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Decide when not to run a chaos experiment

When is the right answer to cancel the experiment?

## Answer guide

- Do not run when you already know the system will fail. An experiment buys information, and if the outcome is not in doubt you are paying an outage for a fact you could have written down. Fix the known weakness first and use the experiment afterwards to verify the fix. This is the single most common waste in immature programmes: injecting a fault into a service with one replica and no timeout, then reporting the obvious.
- Do not run when the preconditions are missing: no owner, no instrumented steady-state metric, no abort path independent of the target, no bounded blast radius, an unhealthy system or an active incident, a change freeze, a peak business event, or a team already over its error budget. Also stop when the cost of being wrong is not recoverable — irreversible data operations, anything touching financial settlement, safety-critical control paths, or regulated systems where the experiment would itself be the compliance breach.
- Do not run when a cheaper method answers the same question. Architecture review, dependency analysis, load tests, failover drills in an isolated copy, and reading the last three postmortems are all faster and safer for some hypotheses. Reserve production experiments for questions that only production can answer, and note that some hypotheses about third-party providers cannot be tested at all — model those with mocked failures at your boundary instead.
- The judgement to demonstrate is that cancelling is a legitimate outcome and not a lost argument. Say plainly which precondition is missing, what would have to change to make the experiment safe, and what you will do instead in the meantime. Failure modes: running anyway because the game day is on the calendar and people travelled for it; treating a veto as obstruction rather than as a finding; and quietly weakening the fault until it is safe but no longer tests the hypothesis, which yields a green result with no meaning.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [Azure Well-Architected — reliability testing strategy](https://learn.microsoft.com/en-us/azure/well-architected/reliability/testing-strategy)
- Maintainer or personal blog: [John Allspaw — Kitchen Soap](https://www.kitchensoap.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [Google SRE workbook — error budget policy](https://sre.google/workbook/error-budget-policy/)
