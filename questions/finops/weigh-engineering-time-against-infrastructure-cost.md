---
title: Weigh engineering time against infrastructure cost
theme: finops
difficulty: staff
type: theory
tags: [finops, leadership, platform-engineering, cost-optimization]
sources:
  - url: https://www.finops.org/framework/capabilities/architecting-for-cloud/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/
    source_type: standard
    verified_on: 2026-08-11
---

# Weigh engineering time against infrastructure cost

When is it correct to spend more on infrastructure in order to spend less engineering time, and how do you argue that case?

## Answer guide

- The comparison is between a recurring, elastic, precisely measured cost and a scarce, lumpy, poorly measured one. Fully loaded engineer cost is large and the supply is fixed in the short term; infrastructure can usually be bought instantly and released later. That asymmetry means the default should lean toward buying infrastructure, and the burden of proof belongs on the proposal to spend engineering time instead.
- The clearest cases for paying more infrastructure: using a managed service instead of operating your own, where the premium buys away an on-call rotation and an upgrade treadmill; over-provisioning modestly rather than building precise autoscaling for a workload that is a small fraction of the bill; buying a vendor product instead of building an internal one that will need permanent staffing; and running redundant capacity rather than writing bespoke failover machinery.
- The cases that flip: when the workload is a large enough share of spend that the efficiency multiplies across the fleet; when the inefficiency compounds with growth so the gap widens every quarter; when the vendor introduces a lock-in or a data-gravity risk you cannot accept; and when the operational burden of the paid option is not actually lower once compliance, integration, and observability are counted.
- Make the argument in the finance organisation's own terms. Engineering time is largely fixed headcount cost, often capitalised differently from cloud spend, and a proposal that reduces cloud spend while consuming headcount can look like a saving in one budget and a cost in another. Say which budget each side lands in, and get the comparison agreed before the debate is about the number.
- Constraints and failure modes: fully loaded cost figures are estimates and should be presented as ranges rather than false precision; the maintenance tail of a build decision is systematically underestimated and should be modelled over several years; teams routinely rebuild something to avoid a visible line item while consuming far more invisible headcount; and "we can build it in two weeks" almost never accounts for the years of operating it afterwards.

## References

- [FinOps Framework — architecting for cloud capability](https://www.finops.org/framework/capabilities/architecting-for-cloud/)
- [Azure Well-Architected cost optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/)
- Further reading (blog): [Charity Majors — engineering leadership and cost of ownership](https://charity.wtf/)

## What to learn next

- Official documentation: [FinOps Framework — architecting for cloud capability](https://www.finops.org/framework/capabilities/architecting-for-cloud/)
- Manual or specification: [Azure Well-Architected cost optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/)
- Maintainer or personal blog: [Charity Majors — engineering leadership and cost of ownership](https://charity.wtf/)
- Technical blog: [Slack engineering blog](https://slack.engineering/)
- Hands-on guide: [FinOps on Microsoft Cloud](https://learn.microsoft.com/en-us/cloud-computing/finops/)
