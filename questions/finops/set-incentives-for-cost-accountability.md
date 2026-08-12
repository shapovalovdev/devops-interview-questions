---
title: Set incentives for cost accountability
theme: finops
difficulty: staff
type: scenario
tags: [finops, leadership, governance, chargeback]
sources:
  - url: https://www.finops.org/framework/principles/
    source_type: standard
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/capabilities/cloud-policy-governance/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Set incentives for cost accountability

How do you make engineering teams genuinely accountable for cloud cost without making them optimise the wrong thing?

## Answer guide

- Accountability requires three things together, and any one of them missing makes the other two counterproductive: visibility into their own cost at a useful granularity and cadence, authority to change the thing that drives it, and a metric that reflects efficiency rather than size. Holding a team accountable for a number it cannot influence produces resentment and creative accounting, not savings.
- Choose the metric carefully, because teams optimise what is measured. Absolute spend punishes the teams that are growing and rewards the ones that are stagnating. Cost per unit of business value — per order, per user, per thousand requests — rewards efficiency and is neutral to growth, which is what you actually want. Publish both, but hold teams to the ratio.
- Put the incentive where the decision is. Efficiency work has to appear in team planning with real capacity, not as a side quest done after hours; a target with no allocated time is a statement of intent, not an incentive. Recognising the teams that improved their unit metric, and making the ratio visible in the same review as reliability and delivery, does more than a chargeback line ever will.
- Constraints: chargeback creates the strongest incentive and needs the most accurate allocation, so sequence it after allocation coverage is high; teams operating a shared platform cannot be held to a unit metric they do not control; and a cost target that competes with a reliability or security obligation must have an explicit precedence rule, decided in advance, or engineers will resolve the conflict silently and inconsistently.
- Failure modes to name and design against: teams cutting non-production environments and losing test coverage; deferring upgrades and patching because the migration costs money this quarter; sampling observability down until incidents cannot be diagnosed; moving workloads into an untagged shared account to make their own number look better; and gaming the denominator of a unit metric. Each of these is a rational response to a badly chosen incentive, so treat their appearance as evidence the incentive is wrong rather than as a discipline problem.

## References

- [FinOps Framework principles](https://www.finops.org/framework/principles/)
- [FinOps Framework — cloud policy and governance capability](https://www.finops.org/framework/capabilities/cloud-policy-governance/)
- Further reading (blog): [FinOps Foundation insights](https://www.finops.org/insights/)

## What to learn next

- Official documentation: [FinOps Framework — cloud policy and governance capability](https://www.finops.org/framework/capabilities/cloud-policy-governance/)
- Manual or specification: [FinOps Framework principles](https://www.finops.org/framework/principles/)
- Maintainer or personal blog: [Charity Majors — engineering leadership and cost of ownership](https://charity.wtf/)
- Technical blog: [FinOps Foundation insights](https://www.finops.org/insights/)
- Hands-on guide: [Analyse costs in Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
