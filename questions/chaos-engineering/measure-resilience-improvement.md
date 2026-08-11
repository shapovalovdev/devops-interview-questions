---
title: Measure whether resilience actually improved
theme: chaos-engineering
difficulty: staff
type: scenario
tags: [chaos-engineering, resilience, metrics, reliability]
sources:
  - url: https://sre.google/workbook/implementing-slos/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Measure whether resilience actually improved

Two years into a chaos programme, how do you show the system is more resilient than it was?

## Answer guide

- Distinguish activity from outcome. Experiments run, faults injected, and services onboarded are activity metrics and are trivially gameable. The outcome measures are the ones that describe behaviour under failure: the fraction of tier-one services that survive their named fault classes with the objective intact, verified recovery time and recovery point against the stated targets, the share of experiments whose result contradicted the team's prediction, and the time from a finding to a verified fix.
- Build a resilience matrix as the programme's ledger: services down one axis, failure classes across the other, each cell recording the last verified date, the result, and the objective it was measured against. Re-verification has an expiry, because a service that survived a zone loss eighteen months and forty deployments ago has not been tested recently. Falling coverage or ageing cells are as meaningful as a red result.
- Corroborate with production evidence rather than relying on the experiments alone. Compare incident rate and impact within the specific failure classes you targeted, mean time to detect and to mitigate for those classes, the proportion of incidents whose contributing mechanism had already been tested, and the count of severe incidents whose failure mode was genuinely novel. A programme that is working should shift incidents from unknown mechanisms toward known and bounded ones, and should shorten the ones that still happen.
- Failure modes: attributing every reliability gain to chaos engineering when architecture changes, capacity increases, and better deployment practice ran in parallel — use the targeted failure classes to make the attribution narrower and defensible; a surprise rate near zero, which means the experiments have become too easy; measuring only the services that opted in, so coverage looks better than it is; and reporting a green matrix built from faults weakened until nothing could fail.

## References

- [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Google SRE workbook — implementing SLOs](https://sre.google/workbook/implementing-slos/)
- Manual or specification: [Azure Well-Architected — failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — tracking outages](https://sre.google/sre-book/tracking-outages/)
