---
title: Select experiments from incident history
theme: chaos-engineering
difficulty: senior
type: scenario
tags: [chaos-engineering, incident-management, experimentation, reliability]
sources:
  - url: https://sre.google/sre-book/postmortem-culture/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Select experiments from incident history

You have a year of postmortems and limited time. How do you choose which experiments to run?

## Answer guide

- Mine the corpus for mechanisms rather than for individual bugs. Group incidents by the contributing failure mode — retry amplification, missing timeout, unbounded queue, single point of failure, cache dependency, saturation without shedding, slow failover — and count how many incidents each mechanism produced and how much impact it caused. The mechanisms that recur across different services are the ones worth an experiment, because a fix there generalises.
- Prefer experiments that verify a remediation actually works. Every postmortem action item is an untested claim: "we added a circuit breaker", "the timeout is now two seconds", "the fallback serves cached data". Turn the highest-impact of those claims into a recurring experiment so the assertion is checked continuously rather than trusted until the next outage. This also converts postmortem follow-up from a paperwork exercise into evidence.
- Weigh candidates by expected value: incident frequency and impact for that mechanism, the number of services sharing it, the cost and risk of the experiment, and whether the result would change a decision. Include near misses and degraded-mode events, which are more numerous than severe incidents and often reveal the same mechanism earlier. Also look for the absence of incidents in an area that has never been tested — silence is not evidence of resilience.
- Failure modes: rehearsing only the last outage, which is the one already fixed and least likely to recur; drawing conclusions from a postmortem corpus that records only severe incidents, so the sample is biased; treating human-factor findings, such as an unreachable runbook or unclear escalation path, as out of scope when they are exactly what a game day tests; and letting the backlog grow without ever retiring experiments whose finding has been fixed and re-verified.

## References

- [Google SRE book — postmortem culture](https://sre.google/sre-book/postmortem-culture/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Google SRE book — postmortem culture](https://sre.google/sre-book/postmortem-culture/)
- Manual or specification: [Azure Well-Architected — failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis)
- Maintainer or personal blog: [Nora Jones — resilience engineering writing](https://medium.com/@NoraJones)
- Technical blog: [Slack Engineering](https://slack.engineering/)
- Hands-on guide: [Google SRE workbook — postmortem culture in practice](https://sre.google/workbook/postmortem-culture/)
