---
title: Design idempotent serverless event processing
theme: serverless
difficulty: senior
type: scenario
tags: [cloud, event-driven, reliability, architecture]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design idempotent serverless event processing

How do you make event-driven serverless processing safe when delivery can repeat?

## Answer guide

- Treat the event identifier and business operation as separate keys. Store a durable idempotency record with an atomic conditional write before making irreversible effects, and return the prior result for a duplicate.
- Choose retry, expiry, and ordering behavior per source. At-least-once delivery, timeouts, and producer retries can create duplicates; do not infer exactly-once business effects from one transport setting.
- Send exhausted failures to an observable recovery path and test replay. A too-short idempotency window or a non-atomic read-then-write can still duplicate charges, notifications, or state changes.

## References

- [AWS Lambda error handling and retries](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)
- Further reading (blog): [AWS Compute Blog — idempotent Lambda](https://aws.amazon.com/blogs/compute/handling-lambda-functions-idempotency-with-aws-lambda-powertools/)

## What to learn next

- Official documentation: [AWS Lambda retry behaviour](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)
- Manual or specification: [AWS Lambda event invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
