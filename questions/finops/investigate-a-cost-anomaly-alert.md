---
title: Investigate a cost anomaly alert
theme: finops
difficulty: middle
type: troubleshooting
tags: [finops, anomaly-detection, monitoring, incident-response]
sources:
  - url: https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/capabilities/anomaly-management/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Investigate a cost anomaly alert

An anomaly detector reports that one account's spend jumped 400 percent overnight. Walk through the investigation.

## Answer guide

- Treat it like an incident with a lower urgency: confirm the signal, scope it, find the change, decide whether to act, and record the outcome. The first question is whether the anomaly is real cost or a data artefact — a delayed line item landing in one day, a credit expiring, a refund, or a newly linked account will all look like a spike.
- Scope it by narrowing the dimensions in order: account, then service, then usage type, then region, then resource. Anomaly detectors such as AWS Cost Anomaly Detection monitor a chosen segment and give you the root-cause dimensions in the alert itself; use those as the starting hypothesis rather than the conclusion.
- Correlate the timestamp against change history: deployments, Terraform applies, feature flags, a new customer onboarding, a retry storm, a runaway batch job, a log pipeline that started shipping debug level, or a misconfigured autoscaler minimum. Cost spikes almost always have a change behind them and the change log is usually faster than the billing data.
- Consider the security case explicitly. A sudden spike in compute in an unusual region, in outbound transfer, or in a service the team does not use is a credible indicator of credential compromise, and that path has a different escalation and a different clock.
- Constraints and failure modes: billing data lags, so an alert always arrives after cost is incurred and a same-day fix still leaves a bill; percentage-based thresholds are extremely noisy on small accounts and blind on large ones, so pair a relative threshold with an absolute floor; and closing an anomaly as "expected" without recording why guarantees the next person repeats the whole investigation.

## References

- [Get started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [FinOps Framework — anomaly management capability](https://www.finops.org/framework/capabilities/anomaly-management/)
- Further reading (blog): [Vantage engineering blog](https://www.vantage.sh/blog)

## What to learn next

- Official documentation: [Get started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- Manual or specification: [FinOps Framework — anomaly management capability](https://www.finops.org/framework/capabilities/anomaly-management/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Analyse costs in Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
