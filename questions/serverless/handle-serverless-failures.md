---
title: Handle serverless failures and poison events
theme: serverless
difficulty: senior
type: scenario
tags: [cloud, event-driven, reliability, incident-response]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Handle serverless failures and poison events

How do you prevent a permanently failing event from disappearing or repeatedly consuming capacity?

## Answer guide

- Classify retryable dependency failures separately from invalid or permanently incompatible events. Set bounded retries and maximum event age for asynchronous work, then retain failures in a destination with the original context.
- Alert on failure destination volume, event age, retry exhaustion, and backlog growth. A dead-letter destination is not a resolution: assign an owner, a replay procedure, and data-retention rules.
- Make remediation idempotent and rate-limited. Replaying an entire failure set without fixing the cause can create duplicate effects or overload a recovered dependency; test recovery with representative poisoned events.

## References

- [AWS Lambda asynchronous failure handling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)
- Further reading (blog): [AWS Compute Blog — Lambda failure handling](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda failure destinations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html)
- Manual or specification: [AWS Lambda retry behaviour](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
