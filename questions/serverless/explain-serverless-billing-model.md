---
title: Explain how serverless billing differs from always-on compute
theme: serverless
difficulty: junior
type: theory
tags: [cloud, cost-optimization, capacity, architecture]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-pricing.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain how serverless billing differs from always-on compute

Why can the same workload be dramatically cheaper or dramatically more expensive on functions than on a reserved instance?

## Answer guide

- Always-on compute bills for provisioned capacity over wall-clock time whether or not requests arrive. Function billing is request-driven: you pay per invocation plus allocated memory multiplied by billed duration, so idle time costs nothing and the unit of spend is work actually performed.
- That flips the economics on utilisation. Spiky, bursty, or low-duty-cycle workloads win, because a reserved instance sized for the peak sits mostly idle. Steady high-throughput workloads with predictable utilisation usually lose, because per-request overhead is charged on every single request rather than amortised across a saturated instance.
- Memory allocation is the hidden multiplier. Because cost is memory multiplied by duration, and memory also buys CPU, a larger setting can cost less overall when it shortens duration—and can cost far more when the function is I/O-bound and duration does not shrink.
- The bill is not the whole cost. Downstream charges dominate many real serverless systems: API gateway requests, queue and stream operations, log ingestion and retention, NAT gateway data processing, and the tracing backend. Compare total system cost, not the function line item.
- Failure modes to expect: a retry storm or recursive trigger that multiplies invocations without any user-visible work, verbose debug logging whose ingestion charge exceeds compute, and idle-but-billed features such as reserved warm capacity left enabled after a launch.

## References

- [AWS Lambda pricing and billing model](https://docs.aws.amazon.com/lambda/latest/dg/lambda-pricing.html)
- Further reading (blog): [Datadog — State of Serverless research](https://www.datadoghq.com/state-of-serverless/)

## What to learn next

- Official documentation: [AWS Lambda pricing and billed duration](https://docs.aws.amazon.com/lambda/latest/dg/lambda-pricing.html)
- Manual or specification: [AWS Lambda API reference — UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html)
- Maintainer or personal blog: [Jeremy Daly — serverless architecture writing](https://www.jeremydaly.com/)
- Technical blog: [Datadog — State of Serverless](https://www.datadoghq.com/state-of-serverless/)
- Hands-on guide: [Cloud Run quickstarts](https://cloud.google.com/run/docs/quickstarts)
