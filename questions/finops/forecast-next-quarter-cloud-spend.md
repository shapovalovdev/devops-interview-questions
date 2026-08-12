---
title: Forecast next quarter cloud spend
theme: finops
difficulty: middle
type: scenario
tags: [finops, forecasting, budgeting, capacity-planning]
sources:
  - url: https://www.finops.org/framework/capabilities/forecasting/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html
    source_type: official-docs
    verified_on: 2026-08-11
---

# Forecast next quarter cloud spend

Finance needs a cloud spend forecast for next quarter. How do you build one you can defend?

## Answer guide

- Build it in three separable parts: a run-rate baseline extrapolated from recent history, a set of named deltas for known changes, and an explicit uncertainty range. Presenting one number with no decomposition means every variance discussion turns into an argument about the whole forecast instead of the one component that was wrong.
- The baseline should be driven by a demand signal rather than by calendar trend alone. If cost per unit of business volume is stable, forecast volume and multiply; that makes the forecast auditable and it separates "we grew" from "we got less efficient". Cost Explorer's forecast and the equivalent provider tools give a statistical extrapolation that is a useful cross-check, not a substitute.
- Named deltas cover everything the trend cannot see: launches and migrations with dates, decommissions, commitment purchases and expiries, price or contract changes, seasonal peaks, and one-off events such as a data backfill or a region build-out. Each delta gets an owner, a size, and a confidence, and a slipped launch then explains itself.
- Constraints: the further out you go the more the forecast is a plan rather than a prediction; amortised and cash views diverge sharply around a commitment purchase, so state which one you are forecasting; and credits, private pricing agreements, and enterprise discount tiers apply on their own schedule.
- Failure modes: extrapolating a month that contained a one-off backfill; ignoring that the current low rate depends on a commitment that expires mid-quarter; forecasting only compute when storage and transfer are growing faster; and never comparing the forecast against actuals afterwards, which is the only thing that improves the next one.

## References

- [FinOps Framework — forecasting capability](https://www.finops.org/framework/capabilities/forecasting/)
- [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- Further reading (blog): [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

## What to learn next

- Official documentation: [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- Manual or specification: [FinOps Framework — forecasting capability](https://www.finops.org/framework/capabilities/forecasting/)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [Vantage engineering blog](https://www.vantage.sh/blog)
- Hands-on guide: [Query Google Cloud billing exports in BigQuery](https://cloud.google.com/billing/docs/how-to/bq-examples)
