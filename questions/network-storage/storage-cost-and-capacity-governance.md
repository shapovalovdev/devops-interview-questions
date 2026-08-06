---
title: Govern storage cost and capacity across teams
theme: network-storage
difficulty: staff
type: scenario
tags: [storage, capacity-planning, cost-optimization, governance, monitoring]
sources:
  - url: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern storage cost and capacity across teams

How would you govern storage growth without turning capacity planning into a manual gate?

## Answer guide

- Publish ownership metadata, budgets, quotas, retention defaults, tier prices, and chargeback or showback views at a useful tenant level. Forecast from growth, recovery reserve, replication factor, snapshots, and lifecycle transitions rather than allocated bytes alone.
- Automate safe defaults such as expiry for non-production data, storage-class recommendations, alerting before quotas, and review workflows for exceptions. Give teams a transparent request path when an RPO, performance, or retention need genuinely exceeds the default tier.
- Deleting data solely because it is old can breach recovery or legal requirements, while treating every byte as premium capacity causes waste. A quota without a forecasting and escalation process converts predictable growth into an availability incident.

## References

- [AWS Well-Architected: cost optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Further reading (blog): [AWS Storage Blog](https://aws.amazon.com/blogs/storage/)

## What to learn next

- Official documentation: [AWS cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Manual or specification: [FinOps Framework](https://www.finops.org/framework/)
- Maintainer or personal blog: [Brendan Gregg blog](https://www.brendangregg.com/blog/)
- Technical blog: [AWS Storage Blog](https://aws.amazon.com/blogs/storage/)
- Hands-on guide: [AWS storage cost management](https://aws.amazon.com/aws-cost-management/)
