---
title: Observe a serverless workload in production
theme: serverless
difficulty: senior
type: scenario
tags: [cloud, observability, monitoring, reliability]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Observe a serverless workload in production

What telemetry do you need to diagnose serverless failures across asynchronous and synchronous paths?

## Answer guide

- Define user and event outcomes first, then emit structured logs, request or event identifiers, traces, and metrics for invocation count, errors, duration, throttles, retries, age, and failure destinations.
- Correlate one business operation across the trigger, function, queue, and downstream service. Sampling and asynchronous handoffs can otherwise hide the link between an accepted event and its eventual effect.
- Alert on sustained user impact and backlog age alongside raw errors. High-cardinality fields, unbounded logs, and success-only dashboards increase cost while leaving retry storms, poison events, and permission failures invisible.

## References

- [AWS Lambda monitoring](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html)
- Further reading (blog): [AWS Compute Blog — Lambda observability articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda monitoring](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html)
- Manual or specification: [AWS X-Ray tracing](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
