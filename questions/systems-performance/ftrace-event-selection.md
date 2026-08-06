---
title: How do you select ftrace events for a latency investigation?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, debugging, observability]
sources:
  - url: https://www.kernel.org/doc/html/latest/trace/ftrace.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you select ftrace events for a latency investigation?

## Answer guide

- Start from the suspected boundary and select the smallest event set that can establish a timeline, for example scheduler wakeup-to-run events or block request issue-to-complete events.
- Filter by PID, CPU, device, or duration where supported, capture briefly, and compare to a baseline. Tracepoints expose defined kernel events; function tracing is broader and can add more overhead or volume.
- Confirm clocks and event semantics before calculating latency. Tracing can perturb a busy system and missed context across user space, remote services, or asynchronous queues can leave a partial timeline.

## References

- [Linux kernel: ftrace](https://www.kernel.org/doc/html/latest/trace/ftrace.html)
- [Linux kernel: trace events](https://www.kernel.org/doc/html/latest/trace/events.html)
- Further reading (personal blog): [Brendan Gregg — Choosing a Linux tracer](https://www.brendangregg.com/blog/2015-07-08/choosing-a-linux-tracer.html)

## What to learn next

- Official documentation: [Linux ftrace](https://www.kernel.org/doc/html/latest/trace/ftrace.html)
- Manual or specification: [trace-cmd documentation](https://trace-cmd.org/)
- Maintainer or personal blog: [Brendan Gregg — tracing](https://www.brendangregg.com/blog/2015-07-08/choosing-a-linux-tracer.html)
- Technical blog: [Datadog Engineering](https://www.datadoghq.com/blog/engineering/)
- Hands-on guide: [trace-cmd](https://trace-cmd.org/)
