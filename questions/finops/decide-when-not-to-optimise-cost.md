---
title: Decide when not to optimise cost
theme: finops
difficulty: staff
type: scenario
tags: [finops, leadership, cost-optimization, architecture]
sources:
  - url: https://www.finops.org/framework/capabilities/workload-optimization/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/architecture/framework/cost-optimization
    source_type: official-docs
    verified_on: 2026-08-11
---

# Decide when not to optimise cost

An engineer proposes six weeks of work to cut a service's cost by 30 thousand dollars a year. How do you decide whether to approve it, and how do you say no well?

## Answer guide

- Compare the fully loaded cost of the work against the durable value of the saving, not against the headline number. Six engineer-weeks is a substantial fraction of a person-quarter of fully loaded cost, plus review, testing, migration risk, and the ongoing maintenance of whatever complexity the change adds. Against thirty thousand a year that is roughly break-even in year one and only clearly positive if the saving persists.
- Ask whether the saving persists. Optimisations against a workload that is being replaced, a product still finding its market, or a usage pattern that is about to change are frequently worthless within a year. Optimisations that scale with growth — a fixed reduction in cost per unit — are worth far more than the same absolute saving on a flat workload, and that difference should dominate the decision.
- Weigh the opportunity cost explicitly. The right comparison is not "saving versus zero", it is "saving versus what those six weeks would otherwise produce". Reliability work that prevents an outage, or feature work that moves revenue, routinely dominates a mid-size cost saving, and a staff engineer's job is to make that comparison visible rather than letting the saving win because it has a number attached.
- Weigh added complexity as a real, recurring cost. A cheaper architecture that is harder to reason about, adds a failure mode, or concentrates knowledge in one person imposes a permanent tax on everyone who operates it. Some savings are not worth the operational surface they create at any price.
- Check the cheaper alternatives first: a rate change, a commitment purchase, a lifecycle rule, deleting something unused, or a configuration change may capture most of the benefit for days rather than weeks of effort. Take the cheap version of the win now and defer the expensive version.
- Say no in a way that keeps the person engaged: acknowledge the analysis, show the comparison you actually made, record the idea with its estimated value so it can be revisited when the workload grows or priorities change, and name the condition that would make it a yes. A rejected proposal with a documented threshold is a much better outcome than an unexplained refusal.

## References

- [FinOps Framework — workload optimization capability](https://www.finops.org/framework/capabilities/workload-optimization/)
- [Google Cloud Architecture Framework — cost optimization](https://cloud.google.com/architecture/framework/cost-optimization)
- Further reading (blog): [Marc Brooker — on simplicity and system design](https://brooker.co.za/blog/2022/05/03/simplicity.html)

## What to learn next

- Official documentation: [FinOps Framework — workload optimization capability](https://www.finops.org/framework/capabilities/workload-optimization/)
- Manual or specification: [Azure Well-Architected cost optimization principles](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles)
- Maintainer or personal blog: [Marc Brooker — on simplicity and system design](https://brooker.co.za/blog/2022/05/03/simplicity.html)
- Technical blog: [Google Cloud developers and practitioners blog](https://cloud.google.com/blog/topics/developers-practitioners)
- Hands-on guide: [Google Cloud Architecture Framework — cost optimization](https://cloud.google.com/architecture/framework/cost-optimization)
