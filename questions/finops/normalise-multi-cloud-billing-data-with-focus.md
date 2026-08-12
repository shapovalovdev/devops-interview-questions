---
title: Normalise multi-cloud billing data with FOCUS
theme: finops
difficulty: middle
type: theory
tags: [finops, cost-allocation, cloud, architecture]
sources:
  - url: https://focus.finops.org/focus-specification/
    source_type: standard
    verified_on: 2026-08-11
  - url: https://focus.finops.org/what-is-focus/
    source_type: standard
    verified_on: 2026-08-11
---

# Normalise multi-cloud billing data with FOCUS

Why is comparing spend across two cloud providers hard, and what does the FOCUS specification change?

## Answer guide

- Each provider publishes billing data in its own schema with its own vocabulary: different column names, different granularity, different definitions of a charge, and different ways of representing discounts, credits, taxes, and amortisation. Two numbers that both look like "compute cost last month" may be measured on incompatible bases, so a naive union of the exports produces a report that is confidently wrong.
- FOCUS — the FinOps Open Cost and Usage Specification — is an open specification that defines a common set of columns and semantics for billing data: consistent identifiers for the billing account, service, resource, and region, consistent handling of pricing and quantity, and, critically, consistent definitions for billed, effective, list, and contracted cost. Providers publish exports conforming to it, so a FinOps tool can read one schema instead of many.
- The practical benefit is that allocation and unit-economics logic becomes portable. Rules for tagging, shared-cost apportionment, and cost per unit can be written once against the specification's columns rather than reimplemented per provider and silently diverging.
- Constraints: FOCUS normalises the shape of the data, not the underlying commercial reality — discount structures, commitment mechanics, and what a provider chooses to meter still differ, and a provider's conformance may lag the current specification version. Provider-specific columns remain, and some semantics are best-effort mappings.
- Failure modes: assuming that identical column names mean identical business meaning across providers; comparing effective cost on one side against billed cost on the other; ignoring that resource identifiers are unique per provider so a cross-provider join needs your own inventory key; and building reports against a specification version without pinning it, so a schema revision quietly changes last quarter's numbers.

## References

- [The FOCUS specification](https://focus.finops.org/focus-specification/)
- [What is FOCUS?](https://focus.finops.org/what-is-focus/)
- Further reading (blog): [FinOps Foundation insights](https://www.finops.org/insights/)

## What to learn next

- Official documentation: [FinOps Framework capabilities](https://www.finops.org/framework/capabilities/)
- Manual or specification: [The FOCUS specification](https://focus.finops.org/focus-specification/)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [Vantage engineering blog](https://www.vantage.sh/blog)
- Hands-on guide: [Export Google Cloud billing data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)
