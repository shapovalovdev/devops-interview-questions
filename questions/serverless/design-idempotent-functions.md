---
title: Design idempotent serverless functions
theme: serverless
difficulty: middle
type: scenario
tags: [cloud, event-driven, reliability, architecture]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design idempotent serverless functions

How do you ensure a retried function invocation does not repeat a business effect?

## Answer guide

- Define the business operation’s idempotency key before writing the handler. Persist a durable record using an atomic create-or-return operation so simultaneous retries cannot both perform the effect.
- Store enough response state to return a consistent result for duplicates, with an expiry aligned to the source’s replay horizon and business risk. A function request ID alone may not survive client retries or event re-delivery.
- Test duplicate, concurrent, late, and partially failed invocations. Idempotency does not repair a non-atomic downstream side effect, so use transactional APIs, an outbox, or an explicit recovery workflow where required.

## References

- [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- Further reading (blog): [AWS Compute Blog — idempotency](https://aws.amazon.com/blogs/compute/handling-lambda-functions-idempotency-with-aws-lambda-powertools/)

## What to learn next

- Official documentation: [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- Manual or specification: [AWS Lambda asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
