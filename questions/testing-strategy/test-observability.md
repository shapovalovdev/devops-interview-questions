---
title: Make test failures observable
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/
    source_type: standard
    verified_on: 2026-08-10
  - url: https://opentelemetry.io/docs/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Make test failures observable

A test fails in CI, passes locally, and the only artifact is `AssertionError: expected 200, got 500`. What should the pipeline have captured so the next failure is diagnosable without a rerun?

## Answer guide

- Treat a test run as a traced operation rather than a log stream. Emit an OpenTelemetry span per test with the suite, test name, outcome, and duration as attributes, and let the spans the application produces during that test nest under it, so a red result links directly to the request that failed inside it. Propagate the trace context from the test into the system under test through the usual `traceparent` header and stamp the test's identity into baggage, which is what turns "a 500 happened somewhere" into the exact handler, query, and downstream call that produced it.
- Then capture the state a rerun would give you, at failure time. Persist the server-side logs of every process the test touched, the response body and headers rather than just the status code, the database state or the specific query result the assertion depended on, the seed used for any randomisation, and the resolved dependency versions and image digests. For browser and API suites, attach the framework's own trace, video, or HAR. All of it belongs in the run's artifacts, keyed by test identity, because a failure whose evidence exists only in a container that has already exited is not diagnosable.
- Make the aggregate visible too. Store one structured record per test execution — name, outcome, duration, commit, branch, runner, attempt number — in something queryable, and you can answer the questions that matter across runs: which tests fail only on one runner class, which have started getting slower, which pass on a retry, and whether this failure is new or the eleventh occurrence. A single test's failure is ambiguous; its history usually is not, and "passes locally" is a hypothesis you can test against the runner dimension directly.
- Constraints and failure modes: instrumentation costs runtime and storage, so sample successful runs and keep full detail on failures; secrets and personal data flow into logs and traces, so redaction has to be part of the capture path rather than an afterthought; artifacts uploaded only on a green run, or on a step that is skipped when the previous one fails, are the most common reason evidence is missing; and per-test tracing that shares one exporter across parallel workers can interleave spans so badly that the trace is worse than no trace.

## References

- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Further reading (blog): [Honeycomb — what observability-driven development is not](https://www.honeycomb.io/blog/observability-driven-development)

## What to learn next

- Official documentation: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Manual or specification: [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Maintainer or personal blog: [Pete Hodgson — domain-oriented observability](https://martinfowler.com/articles/domain-oriented-observability.html)
- Technical blog: [Honeycomb — what observability-driven development is not](https://www.honeycomb.io/blog/observability-driven-development)
- Hands-on guide: [OpenTelemetry — Python getting started](https://opentelemetry.io/docs/languages/python/getting-started/)
