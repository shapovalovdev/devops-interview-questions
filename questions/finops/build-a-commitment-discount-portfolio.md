---
title: Build a commitment discount portfolio
theme: finops
difficulty: middle
type: scenario
tags: [finops, commitment-discounts, forecasting, cost-optimization]
sources:
  - url: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/docs/cuds
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations
    source_type: official-docs
    verified_on: 2026-08-11
---

# Build a commitment discount portfolio

How would you decide how much compute to commit to for the next year, and how would you structure the commitments?

## Answer guide

- Commit to the durable baseline, not the peak and not the average. Take hourly usage over the last several months, take a low percentile of that distribution as the floor, and subtract any usage you already know is leaving — a migration, a decommission, a re-platform. The portion above that floor stays on-demand or spot.
- Structure the portfolio in layers with staggered expiry rather than one large purchase. Buying in monthly or quarterly tranches means no single renewal date exposes the whole fleet to a rate change, and it lets coverage follow growth instead of guessing at it a year ahead.
- Choose the instrument by how much flexibility you need. AWS Compute Savings Plans apply across families, sizes, regions, and even Fargate and Lambda, at a smaller discount than family-scoped or instance-scoped commitments; Google Cloud offers spend-based and resource-based committed use discounts; Azure reservations are scoped to a region and series with exchange rules. Flexibility is bought with discount, and it is usually worth it for a fleet that is still changing shape.
- Material constraints: commitments are a financial obligation for their full term whether or not you use them; discount rates differ by term and by payment option; resource-scoped commitments only apply to matching usage, so an architecture change can strand them; and shared commitments across a billing family are applied by the provider's own ordering rules, which decides who benefits.
- Failure modes and controls: coverage crossing 100 percent of real baseline usage so you pay for hours you do not run; buying against a forecast that assumed a launch which slipped; a team migrating to a managed service and silently stranding a plan; and no one monitoring utilisation and coverage as ongoing metrics with an owner and a review cadence.

## References

- [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- [Google Cloud committed use discounts](https://cloud.google.com/docs/cuds)
- [Save costs with Azure reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)
- Further reading (blog): [Vantage engineering blog](https://www.vantage.sh/blog)

## What to learn next

- Official documentation: [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- Manual or specification: [FinOps Framework — rate optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Save costs with Azure reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)
