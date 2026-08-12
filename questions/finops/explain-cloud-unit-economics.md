---
title: Explain cloud unit economics
theme: finops
difficulty: junior
type: theory
tags: [finops, unit-economics, cloud, cost-optimization]
sources:
  - url: https://www.finops.org/framework/capabilities/unit-economics/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/principles/
    source_type: standard
    verified_on: 2026-08-11
---

# Explain cloud unit economics

What is a cloud unit-economics metric, and why is total monthly spend on its own a poor way to judge whether a platform is efficient?

## Answer guide

- A unit-economics metric divides cloud cost by a business-meaningful denominator — cost per order, per active user, per thousand API requests, per gigabyte ingested — so efficiency can be judged independently of growth. Total spend rising 30 percent is good news if traffic doubled and bad news if traffic was flat, and only the ratio distinguishes those cases.
- The mechanism is a join between billing data and business telemetry: allocated cost for a service over a period, divided by the count of the chosen unit over the same period, using the same time boundaries and the same allocation rules every month. Both halves must be reproducible, or the metric silently drifts.
- Material constraints: the denominator must be a unit the team can actually influence, the numerator must include only cost that is genuinely attributable to that unit, and amortisation of commitments and shared platform cost has to be decided explicitly rather than left to whichever tool produced the number.
- Failure modes to name: picking a denominator that grows automatically so the ratio always improves, changing the allocation method mid-year and comparing across the break, reporting a blended average that hides an expensive minority of customers, and optimising the metric by moving cost into an unallocated bucket instead of removing it.

## References

- [FinOps Framework — unit economics capability](https://www.finops.org/framework/capabilities/unit-economics/)
- [FinOps Framework principles](https://www.finops.org/framework/principles/)
- Further reading (blog): [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)

## What to learn next

- Official documentation: [FinOps Framework — unit economics capability](https://www.finops.org/framework/capabilities/unit-economics/)
- Manual or specification: [FinOps Framework principles](https://www.finops.org/framework/principles/)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Query Google Cloud billing exports in BigQuery](https://cloud.google.com/billing/docs/how-to/bq-examples)
