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

Execution model and invocation semantics before idempotency and concurrency,
because the platform's delivery rules decide what correctness costs.

1. [Explain the serverless function execution model](../../questions/serverless/explain-serverless-execution-model.html)
    — The execution model comes first because everything disappears between
    requests.
2. [Explain serverless payload, memory, and duration limits](../../questions/serverless/explain-function-payload-limits.html)
    — Quotas are the platform's opinions, learned before they bite in
    production.
3. [Explain synchronous and asynchronous serverless invocation](../../questions/serverless/explain-invocation-delivery-semantics.html)
    — Synchronous, asynchronous, and poll-based invocation decide who owns the
    retry.
4. [Design idempotent serverless functions](../../questions/serverless/design-idempotent-functions.html)
    — Idempotency is practised against the delivery semantics established above.
5. [Design idempotent serverless event processing](../../questions/serverless/design-idempotent-serverless-events.html)
    — Event-processing idempotency separates the event key from the business
    key.
6. [Design serverless function timeouts and deadlines](../../questions/serverless/design-function-timeouts.html)
    — Timeouts and deadlines bound exactly what the platform will retry.
7. [Handle serverless failures and poison events](../../questions/serverless/handle-serverless-failures.html)
    — Failure and poison-event handling is where those retries finally surface.
8. [Manage serverless function concurrency safely](../../questions/serverless/manage-function-concurrency.html)
    — Concurrency controls protect the backing services from the whole fleet.
9. [Manage database connections from serverless functions](../../questions/serverless/manage-serverless-database-connections.html)
    — Connection management is the stateful dependency serverless starves.
10. [Reduce a serverless deployment package and its dependency weight](../../questions/serverless/reduce-function-package-size.html)
    — Packaging closes the practised tier with cold-start economics.
11. [Trace a request across ephemeral serverless components](../../questions/serverless/trace-ephemeral-function-requests.html)
    — Tracing ephemeral compute is the observability you cannot log into.
12. [Control serverless cost without hiding demand](../../questions/serverless/control-serverless-cost.html)
    — Cost attribution watches the demand the concurrency tier just throttled.
13. [Secure serverless function identity](../../questions/serverless/secure-function-identity.html)
    — Least-privilege execution roles bound what each function may touch.
14. [Decide between managed functions and long-running compute](../../questions/serverless/choose-serverless-versus-long-running-compute.html)
    — When managed functions beat long-running services is the platform-level
    close.
