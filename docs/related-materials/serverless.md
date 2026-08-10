# Serverless: related materials

Treat the provider's own quota, invocation, and pricing pages as factual
authority, because serverless behaviour is defined by the platform rather than
by your process. Serverless removes server lifecycle work; it does not remove
concurrency limits, delivery semantics, connection budgets, least-privilege
identity, or the need to observe ephemeral compute you cannot log into.

## What to learn next

- Official documentation: [AWS Lambda developer guide — concepts](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html)
- Manual or specification: [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md)
- Maintainer or personal blog: [Marc Brooker — serverless and distributed systems internals](https://brooker.co.za/blog/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Knative getting started](https://knative.dev/docs/getting-started/)

## Legal free books

- [The Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/)
  is freely published by Google and supplies the service-level, overload, and
  incident foundations that serverless workloads still need.
- [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)
  is a freely published companion with practical guidance on error budgets and
  overload handling. Apply it alongside your provider's version-specific quota
  and invocation documentation.

## Suggested study order

Start with the execution model, quotas, and the difference between synchronous,
asynchronous, and poll-based invocation. Then practise idempotency, retries,
dead-letter handling, concurrency controls, and connection management against a
real backing store. Finish with packaging, tracing of ephemeral compute, cost
attribution, least-privilege execution roles, and the platform-level decisions
about when managed functions beat long-running services.
