---
title: Allocate shared and untaggable cost
theme: finops
difficulty: middle
type: scenario
tags: [finops, cost-allocation, chargeback, governance]
sources:
  - url: https://www.finops.org/framework/capabilities/allocation/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-cost-mgt-data
    source_type: official-docs
    verified_on: 2026-08-11
---

# Allocate shared and untaggable cost

Twenty percent of the bill sits in shared platform services and untaggable resources. How do you allocate it?

## Answer guide

- First split the twenty percent into three genuinely different problems: cost that is shared by design (a service mesh, a logging pipeline, a shared database cluster, support and enterprise agreement fees), cost that is untaggable because the provider does not expose a tag on that resource type, and cost that is simply untagged because governance failed. Only the third is fixable by better hygiene, and it should be fixed rather than allocated around.
- For genuinely shared cost, choose an apportionment key and defend it. Even split is simple and fair when the service is a fixed overhead everyone benefits from equally. Proportional to allocated spend is easy to compute and roughly tracks size. Usage-proportional — log lines ingested, mesh requests, storage bytes — is the most accurate and the most expensive to maintain, and it is the only one that creates a real incentive to consume less.
- The chosen key must be published, stable, and reproducible. Write it down with worked examples, version it, and announce changes a period ahead. An allocation rule that changes silently makes every trend line meaningless and destroys the credibility of the whole report.
- For untaggable resources, fall back to the coarser boundary that does exist: the account, project, subscription, or resource group. This is the strongest argument for putting cost boundaries into the account structure rather than relying on tags alone.
- Constraints and failure modes: an unallocated bucket that only ever grows because nobody owns reducing it; a usage-proportional key that costs more in engineering effort than the cost it distributes; allocating a shared platform's cost to teams that have no way to consume less of it; and double-counting when a shared service's own infrastructure is both charged directly and included in the shared pool.

## References

- [FinOps Framework — allocation capability](https://www.finops.org/framework/capabilities/allocation/)
- [Understand Azure Cost Management data](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-cost-mgt-data)
- Further reading (blog): [FinOps Foundation insights](https://www.finops.org/insights/)

## What to learn next

- Official documentation: [FinOps Framework — allocation capability](https://www.finops.org/framework/capabilities/allocation/)
- Manual or specification: [The FOCUS specification](https://focus.finops.org/focus-specification/)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Enable Azure Cost Management tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance)
