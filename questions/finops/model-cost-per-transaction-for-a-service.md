---
title: Model cost per transaction for a service
theme: finops
difficulty: senior
type: scenario
tags: [finops, unit-economics, architecture, cost-optimization]
sources:
  - url: https://www.finops.org/framework/capabilities/unit-economics/
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html
    source_type: standard
    verified_on: 2026-08-11
---

# Model cost per transaction for a service

Build a cost-per-transaction model for a service so the team can reason about the cost of a design change before shipping it.

## Answer guide

- A useful model is a marginal model, not an average one. Split cost into a fixed component that exists whether or not the next request arrives — reserved baseline capacity, standing databases, control plane, monitoring — and a variable component that scales with volume: incremental compute seconds, per-request managed-service charges, storage growth, and data transfer. The number that should drive design decisions is the variable cost of the next transaction.
- Derive it bottom-up from the request path. Measure CPU-seconds and memory-seconds per request at a representative concurrency, count the downstream calls each transaction makes and price them at their published unit rates, add bytes written and bytes egressed, and price any per-invocation or per-request managed-service charge directly. Then reconcile the bottom-up model against the actual bill for a period and explain the gap rather than hiding it.
- Say clearly how commitments and shared platform cost enter the model. Amortised commitment cost gives a stable rate but hides the marginal question, because the next transaction on already-committed capacity is nearly free until the commitment is exhausted. Carrying both an amortised view and an on-demand marginal view is normal, and confusing them is the most common analytical error.
- Constraints: cost per transaction is not constant across the volume range — it falls as fixed cost amortises and then steps up at capacity thresholds such as a new node, a shard, or a bigger database instance; it varies by transaction type, so a blended figure over a heterogeneous API is nearly meaningless; and it is sensitive to cache hit rate, retry rate, and payload size, which are all changeable.
- Failure modes: measuring in a load test whose cache is unrealistically warm or cold; omitting the cost of the observability the service generates, which is often a significant fraction; treating a step change as if it were linear when planning a launch; and building an elegant model that nobody recomputes after the architecture changes, so decisions are made against a number that is a year stale.

## References

- [FinOps Framework — unit economics capability](https://www.finops.org/framework/capabilities/unit-economics/)
- [AWS Well-Architected cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Further reading (blog): [Netflix technology blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [FinOps Framework — unit economics capability](https://www.finops.org/framework/capabilities/unit-economics/)
- Manual or specification: [AWS Well-Architected cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- Maintainer or personal blog: [Marc Brooker — the economics of scale](https://brooker.co.za/blog/2023/03/23/economics.html)
- Technical blog: [Netflix technology blog](https://netflixtechblog.com/)
- Hands-on guide: [Query Google Cloud billing exports in BigQuery](https://cloud.google.com/billing/docs/how-to/bq-examples)
