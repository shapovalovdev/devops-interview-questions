---
title: Trade cost against reliability
theme: finops
difficulty: senior
type: scenario
tags: [finops, reliability, sre, cost-optimization]
sources:
  - url: https://cloud.google.com/architecture/framework/cost-optimization
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles
    source_type: standard
    verified_on: 2026-08-11
---

# Trade cost against reliability

A proposal would cut a service's infrastructure cost by 40 percent by dropping from three availability zones to two and removing standby capacity. How do you evaluate it?

## Answer guide

- Convert the reliability side into the same currency as the cost side before comparing them. Estimate the change in expected unavailability, multiply by the cost of that unavailability — lost revenue, contractual credits, incident response effort, and the reputational or regulatory consequence where it is real — and compare that expected annual cost against the annual saving. A saving that is smaller than the expected loss is not a saving.
- Anchor the decision on the service's error budget rather than on intuition. If the service has been comfortably inside its budget for several quarters, some redundancy is genuinely surplus and removing it is a legitimate way to spend budget. If it has been burning the budget, the proposal is asking to spend money the service does not have.
- Analyse what the redundancy is actually protecting against. Losing a zone protects against a correlated infrastructure failure; standby capacity protects against a demand surge or a slow autoscaler. These fail independently, so evaluate them separately — the answer is frequently that one is worth keeping and the other is not, and a blanket 40 percent cut hides that.
- Look for changes that move the frontier instead of sliding along it: faster autoscaling or a warm pool that replaces standing standby capacity, load shedding and graceful degradation that reduce the cost of running closer to capacity, cheaper instance families or spot for the redundant tier, and reducing recovery time so less standing headroom is needed.
- Constraints and failure modes: two-zone deployments must survive losing one zone, meaning each remaining zone carries the full load, which often erases most of the modelled saving; commitments and quota may not follow the new topology; a cross-zone rebalance can increase transfer cost; and the failure being removed is rare, so the saving is visible every month while the risk is invisible until the one month it is not. Record the decision, its owner, and the conditions under which it should be revisited.

## References

- [Google Cloud Architecture Framework — cost optimization](https://cloud.google.com/architecture/framework/cost-optimization)
- [Azure Well-Architected cost optimization principles](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles)
- Further reading (blog): [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)

## What to learn next

- Official documentation: [Google Cloud Architecture Framework — cost optimization](https://cloud.google.com/architecture/framework/cost-optimization)
- Manual or specification: [Azure Well-Architected cost optimization principles](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [Netflix technology blog](https://netflixtechblog.com/)
- Hands-on guide: [AWS Builders' Library — using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
