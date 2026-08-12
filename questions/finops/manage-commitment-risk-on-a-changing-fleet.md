---
title: Manage commitment risk on a changing fleet
theme: finops
difficulty: senior
type: scenario
tags: [finops, commitment-discounts, forecasting, governance]
sources:
  - url: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/capabilities/rate-optimization/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Manage commitment risk on a changing fleet

The platform is migrating to a different instance family and to managed services over the next year, while three-year commitments are already in place. How do you manage the risk?

## Answer guide

- Name the two risks separately, because they need different treatment. Under-commitment risk is paying on-demand rates for stable baseline usage, and it is visible, recoverable, and bounded. Over-commitment risk is paying for capacity you no longer use, and it is a sunk obligation that no engineering work can undo. Under a migration, deliberately accept some under-commitment.
- Track coverage and utilisation as two distinct, owned metrics. Coverage is the fraction of eligible usage receiving a discount; utilisation is the fraction of the commitment that is actually consumed. Falling utilisation is the leading indicator of a stranded commitment and should trigger action while there is still term left to act in.
- Prefer flexible instruments during structural change. Compute Savings Plans apply across instance family, size, region, and to Fargate and Lambda, which survives exactly this kind of migration at the price of a smaller discount; family- or resource-scoped commitments give a better rate and strand the moment the workload moves. Buy the flexible instrument for the part of the fleet that is moving and the scoped instrument only for what is provably stable.
- Use the levers the providers offer: exchange or modification where the contract allows it, the Reserved Instance marketplace for eligible instruments, shifting other workloads onto the committed footprint so the commitment is consumed by something, and staging the migration so on-demand usage falls only as commitments expire.
- Constraints and failure modes: exchange rules differ by provider and by instrument, and some purchases cannot be undone at all; commitments applied across a billing family benefit whoever the provider's ordering rules favour, which can make a team look efficient because someone else's commitment covered them; a migration to managed services can move usage into a category no commitment covers; and buying at the end of a quarter to hit a savings target, without checking the migration plan, is how most stranded commitments are created.

## References

- [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- [FinOps Framework — rate optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/)
- Further reading (blog): [Vantage engineering blog](https://www.vantage.sh/blog)

## What to learn next

- Official documentation: [AWS Savings Plans user guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
- Manual or specification: [FinOps Framework — rate optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Save costs with Azure reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)
