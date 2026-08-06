---
title: Define process observability without exposing secrets
theme: processes
difficulty: staff
type: scenario
tags: [linux, processes, observability, monitoring, security]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define process observability without exposing secrets

What process-level telemetry should a platform standardize, and how do you prevent it from becoming a sensitive-data leak?

## Answer guide

- Standardize useful, low-cardinality signals: service/unit identity, start time, restart reason, process count, CPU and memory accounting, file-descriptor utilization, cgroup pressure and limit events, and bounded exit-code categories. Tie them to workload and deployment identity so teams can compare behavior across releases.
- Keep raw process inspection privileged and short-lived. Command arguments, environment, paths, socket endpoints, and memory dumps may include secrets or customer data; redact, restrict retention and access, and publish aggregated indicators by default.
- Separate host, cgroup, and application perspectives. A healthy host can hide a cgroup limit failure, while process metrics without request outcomes can mislead; correlate with latency, errors, queue depth, and infrastructure pressure.
- Set cost and reliability guardrails: sampling budgets, cardinality limits, retention, and an incident-only escalation path for deeper tracing. Review whether telemetry actually changes detection, diagnosis, and recovery rather than collecting every `/proc` field.

## References

- [proc(5): process information pseudo-filesystem](https://man7.org/linux/man-pages/man5/proc.5.html)
- [cgroup v2: resource accounting and events](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [systemd.resource-control: cgroup resource data](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
- Free book: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Further reading (blog): [Brendan Gregg: Linux performance tools](https://www.brendangregg.com/blog/2015-12-03/linux-perf-tools-in-500-lines.html)

## What to learn next

- Official documentation: [man7 proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Manual or specification: [Linux cgroup v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Google SRE — monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
