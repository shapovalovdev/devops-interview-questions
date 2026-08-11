---
title: Justify the cost of a chaos engineering programme
theme: chaos-engineering
difficulty: staff
type: scenario
tags: [chaos-engineering, cost-optimization, governance, leadership]
sources:
  - url: https://sre.google/sre-book/embracing-risk/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Justify the cost of a chaos engineering programme

An executive asks why you are deliberately breaking things that currently work. What is the argument?

## Answer guide

- Frame it as buying information about failures that will happen anyway, on a schedule you choose, at a scale you bound, with the experts awake and watching. The alternative is not "no failures" but the same failures at 03:00 on a peak trading day at full scale. Price the difference using your own history: the impact of past incidents in the failure classes the experiments target, and the fraction of that impact attributable to slow detection or an untested recovery path.
- Be honest about the full cost, because an argument that hides it loses credibility on the first bad day. It includes engineering time to design and run experiments, platform build and maintenance, spare capacity and redundancy the experiments prove you need, environment and data costs, the time to fix what is found — usually the largest line — and a real expected value of user-visible impact charged against the error budget. Present that expected impact as a budgeted number rather than a promise it will never happen.
- Tie the return to decisions the business already makes. Reliability targets, contractual availability commitments, launch readiness, and disaster-recovery obligations all require evidence, and an experiment is cheaper evidence than an outage or an audit finding. Reduced mean time to recovery, verified failover within the stated recovery time objective, and retired redundant capacity that testing proved unnecessary are all defensible outcomes.
- Failure modes: claiming avoided outages you cannot substantiate; measuring the programme by experiment count so it looks productive while finding nothing; running experiments while the fix backlog grows, which converts known risk into recorded, unmitigated risk and is worse than not knowing; and refusing to scale the programme down for services whose reliability target genuinely does not justify it. Right-size the investment per service tier and say so explicitly.

## References

- [Google SRE book — embracing risk](https://sre.google/sre-book/embracing-risk/)
- Further reading (blog): [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [Google SRE book — embracing risk](https://sre.google/sre-book/embracing-risk/)
- Manual or specification: [Azure Well-Architected — reliability design principles](https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles)
- Maintainer or personal blog: [Adrian Cockcroft — architecture and resilience writing](https://adrianco.medium.com/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [Google SRE workbook — error budget policy](https://sre.google/workbook/error-budget-policy/)
