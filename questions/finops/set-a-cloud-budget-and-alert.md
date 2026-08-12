---
title: Set a cloud budget and alert
theme: finops
difficulty: junior
type: scenario
tags: [finops, budgeting, monitoring, cloud]
sources:
  - url: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/billing/docs/how-to/budgets
    source_type: official-docs
    verified_on: 2026-08-11
---

# Set a cloud budget and alert

A team has been asked to keep a new project under a monthly cloud budget. How do you set that budget up so the alert is actually useful?

## Answer guide

- Scope the budget to something the team owns end to end — a dedicated account, project, or subscription is far more reliable than a tag filter — and set the amount from measured usage plus a deliberate headroom, not from a round number someone liked.
- The mechanism is threshold evaluation against periodically refreshed cost data. AWS Budgets and Google Cloud budgets both support alerts on actual spend and on forecast spend, and both let you notify at several percentages of the budget. Route notifications to a channel the team reads, and include the owner and the runbook link in the message.
- Add at least one forecast-based threshold. An actual-spend alert at 100 percent fires when the money is already gone; a forecast alert at 90 percent gives the team time to act within the same billing period.
- Material constraints: billing data lags by hours, so budgets detect a sustained trend rather than a spike in the last few minutes; a budget is a notification, not an enforcement mechanism, unless you deliberately wire an action to it; and monthly budgets reset, which hides a problem that began late in one month and continues into the next.
- Failure modes: alerting only the central FinOps mailbox so nobody with authority to change anything sees it; setting thresholds so tight they fire every month and are muted; scoping to a tag with poor coverage so half the project's cost never counts; and treating an automated budget action that stops resources as safe without checking what it would stop in production.

## References

- [Manage costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Create and manage Google Cloud budgets](https://cloud.google.com/billing/docs/how-to/budgets)
- Further reading (blog): [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

## What to learn next

- Official documentation: [Manage costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- Manual or specification: [FinOps Framework — budget management capability](https://www.finops.org/framework/capabilities/budget-management/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [Vantage engineering blog](https://www.vantage.sh/blog)
- Hands-on guide: [Create an Azure Cost Management budget](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
