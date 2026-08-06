---
title: Handle log rotation without duplicate or missing events
theme: logging
difficulty: middle
type: scenario
tags: [logging, linux, reliability, troubleshooting]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle log rotation without duplicate or missing events

How do rotation and a file tailer create duplicate or missing log records?

## Answer guide

- A tailer needs a durable identity and offset for the file it is reading. Rotation can rename an inode, truncate a path in place, or create a replacement before the tailer has read the old bytes; simplistic path-only tracking loses the distinction.
- Configure the producer and collector as a pair: retain rotated files long enough, persist checkpoints, detect truncation, and use multiline parsing only where record boundaries are unambiguous. Test copy-truncate and rename-create because operating systems and log rotation tools differ.
- Most file pipelines are at-least-once, not exactly-once. Include timestamps and event identifiers where practical, tolerate duplicates in search and alerts, and monitor parser errors, read lag, checkpoint health, and dropped bytes after a deployment or node restart.

## References

- [OpenTelemetry logging: file collection considerations](https://opentelemetry.io/docs/specs/otel/logs/)
- Further reading (blog): [Datadog engineering blog](https://www.datadoghq.com/blog/)

## What to learn next

- Official documentation: [Fluent Bit tail input](https://docs.fluentbit.io/manual/pipeline/inputs/tail)
- Manual or specification: [logrotate manual](https://man7.org/linux/man-pages/man8/logrotate.8.html)
- Maintainer or personal blog: [Fluent Bit blog](https://fluentbit.io/blog/)
- Technical blog: [Datadog engineering blog](https://www.datadoghq.com/blog/)
- Hands-on guide: [OpenTelemetry filelog receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/filelogreceiver)
