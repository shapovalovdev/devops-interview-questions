---
title: Facilitate a game day
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, game-day, incident-response, operations]
sources:
  - url: https://sre.google/sre-book/accelerating-sre-on-call/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Facilitate a game day

How do you run a game day so that it produces findings rather than theatre?

## Answer guide

- A game day exercises the humans and the process as much as the system: detection, alert routing, escalation, runbooks, communication, and decision-making under uncertainty. Assign roles before the day — a facilitator who injects the fault and knows the answer, responders who do not, a scribe who timestamps everything, and an observer for each dependent team — and give the responders no more information than a real page would.
- Prepare a scenario with a written fault, a predicted response, a safety brief, and explicit abort criteria. Announce the window to anyone who might be paged by the side effects, but do not tell responders which fault is coming, or you measure recall rather than capability. Decide in advance whether the exercise is a tabletop, a rehearsal in staging, or a live injection in production, and state which systems are out of scope.
- Measure the timeline: time to detect, time to acknowledge, time to correct diagnosis, time to mitigate, and time to communicate to stakeholders. The gaps are the product — a runbook that assumes a dashboard that no longer exists, an alert routed to a team that disbanded, credentials nobody on call holds, a document only reachable through the service that is down.
- Failure modes: a facilitator who rescues the team too early, so the interesting part never happens; findings recorded as a list of complaints with no owner or due date; the same well-rehearsed scenario every quarter; running only during business hours so the actual on-call rotation is never exercised; and letting the exercise become a performance review, which guarantees people stop volunteering the mistakes that matter. Close every finding as a tracked action and re-run the scenario later to confirm the fix.

## References

- [Google SRE book — accelerating SRE on-call and disaster role-playing](https://sre.google/sre-book/accelerating-sre-on-call/)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [Google SRE book — accelerating SRE on-call](https://sre.google/sre-book/accelerating-sre-on-call/)
- Manual or specification: [Azure Well-Architected — failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis)
- Maintainer or personal blog: [John Allspaw — Kitchen Soap](https://www.kitchensoap.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [Google SRE workbook — incident response](https://sre.google/workbook/incident-response/)
