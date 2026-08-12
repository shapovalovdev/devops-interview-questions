---
title: Read a cloud bill and find its drivers
theme: finops
difficulty: junior
type: theory
tags: [finops, cloud, cost-optimization, aws]
sources:
  - url: https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/billing/docs/how-to/export-data-bigquery
    source_type: official-docs
    verified_on: 2026-08-11
---

# Read a cloud bill and find its drivers

Given a monthly cloud bill that grew unexpectedly, how do you work out what actually drove the increase?

## Answer guide

- Start from the detailed billing export, not the console summary. AWS Cost and Usage Reports, Google Cloud billing exports to BigQuery, and Azure cost details all publish line items with usage quantity, unit price, resource identifier, and applied discounts, which is the only level at which price and quantity can be separated.
- The mechanism of the analysis is a decomposition: for each service, compare the current period against a baseline and split the delta into a usage change, a rate change, and a mix change. A bill can grow because you ran more hours, because a commitment expired and hours reverted to on-demand rates, or because traffic shifted to a more expensive region, instance family, or storage class.
- Material constraints: exports lag by hours to a day and are restated as the month closes, so mid-month numbers are provisional. Amortised and unblended views answer different questions, credits and refunds land asynchronously, and untagged or shared line items will not attribute cleanly no matter how you slice them.
- Failure modes: comparing a 31-day month against a 28-day month without normalising, reading unblended cost while a savings plan is being applied and concluding a service got cheaper, chasing the largest absolute service instead of the largest delta, and stopping at the service level when the growth is in one resource or one account.

## References

- [AWS Cost and Usage Reports user guide](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
- [Export Google Cloud billing data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)
- Further reading (blog): [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

## What to learn next

- Official documentation: [AWS Cost and Usage Reports user guide](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
- Manual or specification: [FOCUS — the FinOps Open Cost and Usage Specification](https://focus.finops.org/focus-specification/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [Vantage engineering blog](https://www.vantage.sh/blog)
- Hands-on guide: [Query Google Cloud billing exports in BigQuery](https://cloud.google.com/billing/docs/how-to/bq-examples)
