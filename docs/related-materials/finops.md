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

Start with the billing data model — line items, usage quantity versus rate,
amortised versus unblended cost — and the vocabulary of allocation, showback,
and chargeback. Then work through tagging and account structure, rightsizing
and utilisation, commitment discounts and their risk, spot strategy, storage
tiering, and egress. Move on to Kubernetes cost attribution, idle capacity, and
autoscaling economics, then to budgets, anomaly detection, and forecasting.
Finish with the trade-offs a senior engineer is actually asked to make: cost
against reliability and latency, engineering time against infrastructure spend,
and the governance and incentives that keep a FinOps practice honest.
