---
title: Explain showback and chargeback
theme: finops
difficulty: junior
type: theory
tags: [finops, chargeback, cost-allocation, governance]
sources:
  - url: https://www.finops.org/framework/capabilities/allocation/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/capabilities/reporting-analytics/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Explain showback and chargeback

What is the difference between showback and chargeback, and when would you choose one over the other?

## Answer guide

- Showback reports each team's cloud cost back to it without moving money; the central budget still pays the bill. Chargeback actually transfers the cost onto the consuming team's or business unit's budget, so it appears in their financial results.
- The mechanism is the same allocation pipeline in both cases: billing line items are attributed to owners using tags, accounts, or projects, shared costs are apportioned by an agreed rule, and the result is published on a fixed cadence. Chargeback simply adds a finance step that treats the output as an internal invoice, which raises the accuracy bar sharply.
- Choose showback while allocation coverage is still incomplete, while the organisation is learning the data, or where teams have no real authority over their architecture. Choose chargeback when allocation is trustworthy, when teams control their own spend, and when you need cost to compete with other priorities inside a real budget.
- Constraints and failure modes: chargeback on top of poor tag coverage produces disputes that destroy trust in the data faster than any technical error; an unallocated bucket that keeps growing quietly shifts cost onto whoever is easiest to charge; a rule that changes without notice makes month-over-month comparison meaningless; and chargeback with no lever to reduce cost just makes teams resent a number they cannot move.

## References

- [FinOps Framework — allocation capability](https://www.finops.org/framework/capabilities/allocation/)
- [FinOps Framework — reporting and analytics capability](https://www.finops.org/framework/capabilities/reporting-analytics/)
- Further reading (blog): [Vantage engineering blog](https://www.vantage.sh/blog)

## What to learn next

- Official documentation: [FinOps Framework — allocation capability](https://www.finops.org/framework/capabilities/allocation/)
- Manual or specification: [FinOps Framework maturity model](https://www.finops.org/framework/maturity-model/)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Analyse costs in Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
