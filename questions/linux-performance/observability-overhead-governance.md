---
title: Govern performance-observability overhead
theme: linux-performance
difficulty: staff
type: scenario
tags: [linux, performance, observability, governance, security]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern performance-observability overhead

How should a platform team balance deep Linux observability against performance and security risk?

## Answer guide

- Classify instrumentation by privilege, target scope, data sensitivity, expected overhead, and operational value. Use low-cost fleet signals for detection, time-bounded targeted profiling for diagnosis, and explicit approvals for tools that access kernel events or potentially sensitive process metadata.
- Set sampling budgets, rate limits, retention and redaction controls, rollback procedures, and before/after overhead tests. Provide reusable, least-privileged runbooks so incident responders do not need broad permanent access during an outage.
- More telemetry can increase CPU, I/O, network cost, and attack surface while obscuring the signal with noise. Do not approve a collector merely because it is popular; review kernel compatibility, multi-tenant isolation, and the decision it will actually support.

## References

- [Linux kernel: perf security considerations](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Further reading (blog): [Brendan Gregg — perf Examples](https://www.brendangregg.com/perf.html)

## What to learn next

- Official documentation: [Linux perf security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Manual or specification: [perf_event_open(2)](https://man7.org/linux/man-pages/man2/perf_event_open.2.html)
- Maintainer or personal blog: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux tracing documentation](https://www.kernel.org/doc/html/latest/trace/index.html)
