---
title: Parse multiline exception logs safely
theme: logging
difficulty: middle
type: scenario
tags: [logging, debugging, troubleshooting, observability]
sources:
  - url: https://docs.fluentbit.io/manual/data-pipeline/parsers/multiline-parsing
    source_type: official-docs
    verified_on: 2026-08-06
---

# Parse multiline exception logs safely

Why is multiline parsing risky, and how would you deploy it?

## Answer guide

- A stack trace spans physical lines but represents one event; without a multiline parser, search and severity extraction split it into unrelated records. Prefer structured exception fields when the language supports them, because a heuristic cannot perfectly recognize every trace format.
- Scope parser rules to a known container, file, or source and anchor them to a documented first-line pattern. Set maximum size and timeout limits so malformed input cannot retain an unbounded buffer or merge unrelated records during high concurrency.
- Validate against normal exceptions, nested causes, interleaved process output, partial writes, rotation, and restarts. Export parser failures and flush counts; an apparently successful pipeline can silently turn a useful error into megabyte-sized records or lose causal context.

## References

- [Fluent Bit multiline parsing](https://docs.fluentbit.io/manual/data-pipeline/parsers/multiline-parsing)
- Further reading (blog): [Better Stack logging guides](https://betterstack.com/community/guides/logging/)

## What to learn next

- Official documentation: [Fluent Bit multiline parsing](https://docs.fluentbit.io/manual/data-pipeline/parsers/multiline-parsing)
- Manual or specification: [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Maintainer or personal blog: [Fluent Bit blog](https://fluentbit.io/blog/)
- Technical blog: [Better Stack logging guides](https://betterstack.com/community/guides/logging/)
- Hands-on guide: [Fluent Bit parser configuration](https://docs.fluentbit.io/manual/data-pipeline/parsers/configuring-parser)
