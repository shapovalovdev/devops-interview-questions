---
title: Stand up a FinOps practice
theme: finops
difficulty: staff
type: scenario
tags: [finops, governance, leadership, platform-engineering]
sources:
  - url: https://www.finops.org/framework/
    source_type: standard
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/phases/
    source_type: standard
    verified_on: 2026-08-11
---

# Stand up a FinOps practice

You have been asked to build a FinOps practice in an engineering organisation of several hundred people. What do you build, in what order, and how do you know it is working?

## Answer guide

- Start with data quality, not with savings. Nothing downstream is defensible until allocation coverage is high, the reporting cadence is fixed, and the numbers reconcile with the invoice. Publishing a savings target on top of data engineers do not trust produces argument rather than action, and it is very hard to recover that credibility.
- Follow the inform, optimise, operate progression the FinOps Framework describes. Inform: allocation, tagging and account hygiene, showback, and unit metrics that mean something to each team. Optimise: rightsizing, rate optimisation, waste removal, and architectural change, each with a named owner. Operate: budgets, anomaly response, forecast-versus-actual review, and policy that keeps the gains from eroding.
- Staff it as a small central team that builds capability rather than performs the work. The central function owns the data pipeline, the allocation rules, the commitment portfolio, and the vendor relationship, because those genuinely need central ownership and specialist knowledge. Engineering teams own their own usage. A central team that files optimisation tickets for other teams does not scale past its own headcount.
- Make it a cross-functional practice with finance and procurement from the start. Finance owns the budget model, the amortisation policy, and the chargeback mechanics; procurement owns the enterprise agreement and the negotiation; engineering owns architecture and usage. FinOps fails most often as an organisational problem, not a technical one.
- Measure the practice by leading indicators, not by a cumulative savings number that can never be verified: allocation coverage, commitment coverage and utilisation, forecast accuracy, time to acknowledge an anomaly, the fraction of teams with a live unit metric, and the trend in cost per unit. Cumulative savings claims double-count, take credit for workloads that shrank on their own, and cannot be reconciled with the invoice.
- Failure modes to name: a savings target that pushes teams to defer necessary reliability work; efficiency work with no capacity allocated to it in team planning; a dashboard nobody opens; and a practice that captures the easy 20 percent, declares success, and is disbanded before the operate phase makes the gains durable.

## References

- [The FinOps Framework](https://www.finops.org/framework/)
- [FinOps Framework phases](https://www.finops.org/framework/phases/)
- Further reading (blog): [FinOps Foundation insights](https://www.finops.org/insights/)

## What to learn next

- Official documentation: [The FinOps Framework](https://www.finops.org/framework/)
- Manual or specification: [FinOps Framework maturity model](https://www.finops.org/framework/maturity-model/)
- Maintainer or personal blog: [Charity Majors — engineering leadership and cost of ownership](https://charity.wtf/)
- Technical blog: [FinOps Foundation insights](https://www.finops.org/insights/)
- Hands-on guide: [FinOps on Microsoft Cloud](https://learn.microsoft.com/en-us/cloud-computing/finops/)
