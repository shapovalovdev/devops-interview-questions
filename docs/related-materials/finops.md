# FinOps: related materials

Treat the FinOps Foundation Framework as the authority for the practice —
its capabilities, phases, and personas — and the FOCUS specification as the
authority for what a normalised billing record actually contains. For anything
about a specific rate, discount mechanism, or billing dimension, the provider's
own billing and pricing documentation is the only evidence that counts, because
rates, commitment scopes, and storage-class transition rules change on the
vendor's schedule and no third-party summary tracks them reliably.

Cost questions almost always decompose into three independent decisions: what
the unit of work is, how cost is allocated to it, and which of price, quantity,
and mix you are actually changing. Read the specification for the data model,
the vendor manuals for the mechanics, and the individual-author blogs below for
judgement and war stories — the blogs are context, not evidence.

## What to learn next

- Official documentation: [FinOps Framework capabilities](https://www.finops.org/framework/capabilities/)
- Manual or specification: [FOCUS — the FinOps Open Cost and Usage Specification](https://focus.finops.org/focus-specification/)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Query Google Cloud billing exports in BigQuery](https://cloud.google.com/billing/docs/how-to/bq-examples)

## Legal free books

No commercial FinOps title is linked here: avoid unauthorized copies. The
FinOps Foundation Framework, the FOCUS specification, the OpenCost
documentation, the AWS Well-Architected cost optimization pillar, the Google
Cloud Architecture Framework, the Azure Well-Architected cost optimization
guidance, and the freely published Google SRE books are all lawfully free to
read and cover the same ground for interview preparation.

## Suggested study order

The billing data model before allocation, allocation before optimisation,
optimisation before the trade-offs a senior engineer is actually asked to make.

1. [Read a cloud bill and find its drivers](../../questions/finops/read-a-cloud-bill-and-find-its-drivers.html)
    — Line items, usage quantity versus rate, amortised versus unblended — the
    data model everything else reads.
2. [Normalise multi-cloud billing data with FOCUS](../../questions/finops/normalise-multi-cloud-billing-data-with-focus.html)
    — FOCUS normalisation makes multi-cloud bills comparable before any analysis
    begins.
3. [Explain showback and chargeback](../../questions/finops/explain-showback-and-chargeback.html)
    — Showback and chargeback are the vocabulary of allocation the billing model
    feeds.
4. [Allocate shared and untaggable cost](../../questions/finops/allocate-shared-and-untaggable-cost.html)
    — Shared and untaggable cost is where honest allocation actually gets hard.
5. [Tag resources for cost allocation](../../questions/finops/tag-resources-for-cost-allocation.html)
    — Tagging is the mechanism the whole allocation vocabulary depends on.
6. [Design account structure for cost visibility](../../questions/finops/design-account-structure-for-cost-visibility.html)
    — Account structure decides whether the tags can even do their job.
7. [Rightsize overprovisioned compute](../../questions/finops/rightsize-overprovisioned-compute.html)
    — Rightsizing is the first optimisation, and it presumes allocation that is
    already visible.
8. [Compare on-demand, committed, and spot pricing](../../questions/finops/compare-on-demand-committed-and-spot-pricing.html)
    — On-demand, committed, and spot are the trade every commitment decision
    makes.
9. [Build a commitment discount portfolio](../../questions/finops/build-a-commitment-discount-portfolio.html)
    — A portfolio prices commitment risk instead of chasing the maximum
    discount.
10. [Manage commitment risk on a changing fleet](../../questions/finops/manage-commitment-risk-on-a-changing-fleet.html)
    — A changing fleet makes yesterday's commitments a liability to be managed.
11. [Run production work on spot capacity](../../questions/finops/run-production-work-on-spot-capacity.html)
    — Spot strategy spends the pricing knowledge on work that genuinely
    tolerates eviction.
12. [Tier object storage with lifecycle rules](../../questions/finops/tier-object-storage-with-lifecycle-rules.html)
    — Storage tiering is the same commitment logic applied to bytes.
13. [Trace an unexplained data transfer bill](../../questions/finops/trace-an-unexplained-data-transfer-bill.html)
    — Egress archaeology closes the optimisation tier with its most surprising
    bill.
14. [Attribute Kubernetes cluster cost to teams](../../questions/finops/attribute-kubernetes-cluster-cost-to-teams.html)
    — Kubernetes attribution extends allocation to where the bill is densest.
15. [Reclaim idle Kubernetes capacity](../../questions/finops/reclaim-idle-kubernetes-capacity.html)
    — Idle capacity is the Kubernetes bill's silent majority.
16. [Tune autoscaling for cost and latency](../../questions/finops/tune-autoscaling-for-cost-and-latency.html)
    — Autoscaling economics trade latency against spend with every step size.
17. [Set a cloud budget and alert](../../questions/finops/set-a-cloud-budget-and-alert.html)
    — Budgets convert spend into a decision someone actually gets woken by.
18. [Investigate a cost anomaly alert](../../questions/finops/investigate-a-cost-anomaly-alert.html)
    — Anomaly investigation is the budget alert's diagnostic sequel.
19. [Forecast next quarter cloud spend](../../questions/finops/forecast-next-quarter-cloud-spend.html)
    — Forecasting makes the spend a plan rather than a quarterly surprise.
20. [Trade cost against reliability](../../questions/finops/trade-cost-against-reliability.html)
    — The senior trade-offs open exactly where reliability and latency meet the
    bill.
21. [Weigh engineering time against infrastructure cost](../../questions/finops/weigh-engineering-time-against-infrastructure-cost.html)
    — Engineering time is the other currency every optimisation above spent
    silently.
22. [Set incentives for cost accountability](../../questions/finops/set-incentives-for-cost-accountability.html)
    — Incentives keep the practice honest when its metrics are gameable.
23. [Stand up a FinOps practice](../../questions/finops/stand-up-a-finops-practice.html)
    — Standing up the practice is the organizational capstone the tiers above
    justify.
