---
title: Design serverless function timeouts and deadlines
theme: serverless
difficulty: middle
type: scenario
tags: [cloud, reliability, performance, observability]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design serverless function timeouts and deadlines

How do you choose a serverless timeout without turning slow dependencies into opaque failures?

## Answer guide

- Derive the function timeout from the end-to-end request budget, then reserve time for retries, cleanup, and response propagation. The function limit must be shorter than an upstream deadline where one exists.
- Set explicit client connect, read, and retry deadlines below the function deadline. Otherwise a downstream call can consume all execution time and leave no room for a controlled error or metric flush.
- Record remaining execution time, dependency latency, timeout count, and retry outcomes. Raising the function timeout can increase cost and concurrent pressure; use it only after identifying the slow dependency or workload.

## References

- [AWS Lambda timeout configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)
- Further reading (blog): [AWS Compute Blog — Lambda performance](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)

## What to learn next

- Official documentation: [AWS Lambda timeout configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)
- Manual or specification: [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
