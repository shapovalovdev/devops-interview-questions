---
title: Orchestrate a serverless workflow safely
theme: serverless
difficulty: senior
type: scenario
tags: [cloud, event-driven, architecture, reliability]
sources:
  - url: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Orchestrate a serverless workflow safely

When should you use workflow orchestration instead of chaining functions directly?

## Answer guide

- Use an explicit workflow for multi-step state, branching, compensation, waiting, and approval. It makes progress and retry policy visible rather than scattering control flow across event handlers.
- Define per-step timeouts, retries, idempotency, and compensating actions. A retry-safe function does not automatically make a workflow safe when a prior external side effect succeeded but its acknowledgement was lost.
- Emit business state transitions and retain execution history with appropriate access controls. Large payloads, unbounded retries, and implicit fan-out can create cost, duplicated work, and difficult incident recovery.

## References

- [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- Further reading (blog): [AWS Compute Blog — orchestration](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- Manual or specification: [AWS Step Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Step Functions tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/tutorials.html)
