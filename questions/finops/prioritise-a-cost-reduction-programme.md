---
title: Prioritise a cost reduction programme
theme: finops
difficulty: staff
type: scenario
tags: [finops, leadership, governance, capacity-planning]
sources:
  - url: https://www.finops.org/framework/capabilities/workload-optimization/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://www.finops.org/framework/maturity-model/
    source_type: standard
    verified_on: 2026-08-11
---

# Prioritise a cost reduction programme

Leadership wants cloud spend cut by 25 percent within two quarters. How do you build and sequence that programme?

## Answer guide

- Sequence by time-to-value and risk, not by size of prize. The first wave is work with no architectural risk and a fast payback: deleting orphaned volumes, idle load balancers, unattached addresses, forgotten environments and stale snapshots; switching non-production to a schedule; applying storage lifecycle rules; and buying commitment coverage against the proven baseline. This typically lands a meaningful fraction of the target within weeks and buys credibility for the harder work.
- The second wave is rate and utilisation work that touches running systems but not their design: rightsizing, instance family modernisation, moving interruptible workloads to spot, reducing observability retention and cardinality, and fixing the top data-transfer paths. Each item needs a named owner, an estimated saving, a verification step in the billing data, and a rollback.
- The third wave is architectural and will not complete inside two quarters: caching, tiering, batching, algorithmic efficiency, consolidation of duplicated platforms, and re-platforming expensive services. Start it in parallel, but do not put its savings in the two-quarter commitment, and say so explicitly rather than letting the plan carry optimism it cannot deliver.
- Be honest about whether 25 percent is achievable, and negotiate on evidence. Build a bottom-up estimate with confidence bands per item, show what the realistic figure is, and identify what would have to change — a product decision to shut something down, a reliability trade-off, a headcount reallocation — to reach the rest. Committing to a number the analysis does not support is the most common way these programmes fail.
- Guard against the damage the programme itself can cause. Protect non-negotiables in writing before starting: security tooling, backup and disaster-recovery capability, patching cadence, and the observability needed to run an incident. Require a reliability review for any change to redundancy, and track a small set of counter-metrics — incident rate, error budget burn, deployment frequency, on-call load — alongside savings, so degradation shows up while it is still cheap to reverse.
- Verify savings in the invoice, not in the ticket. Each item is closed only when the corresponding line in the billing export moves, because a resized instance that never triggers a node removal, or a deleted resource that was already free-tier, produces a satisfying ticket and no money. Report realised run-rate reduction against forecast, and hold the run rate afterwards with policy, budgets, and anomaly detection or it will drift straight back.

## References

- [FinOps Framework — workload optimization capability](https://www.finops.org/framework/capabilities/workload-optimization/)
- [FinOps Framework maturity model](https://www.finops.org/framework/maturity-model/)
- Further reading (blog): [FinOps Foundation insights](https://www.finops.org/insights/)

## What to learn next

- Official documentation: [FinOps Framework — workload optimization capability](https://www.finops.org/framework/capabilities/workload-optimization/)
- Manual or specification: [AWS Well-Architected cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Analyse costs in Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
