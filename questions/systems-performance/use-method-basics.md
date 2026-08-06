---
title: How do you apply the USE method to a production resource?
theme: systems-performance
difficulty: junior
type: troubleshooting
tags: [linux, performance, monitoring, debugging]
sources:
  - url: https://www.brendangregg.com/usemethod.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you apply the USE method to a production resource?

## Answer guide

- Start with every relevant resource: CPUs, memory, disks, network interfaces, and application queues. For each, measure utilization, saturation, and errors rather than starting from a favorite tool.
- Utilization means busy time, saturation means work waiting for service, and errors mean failed operations. A busy resource is not automatically the bottleneck; sustained queueing or errors changes the priority.
- Record the interval, workload, host, and counters together. Compare a healthy baseline, then drill into the resource with the largest sustained saturation or error signal. Missing metrics and transient bursts are important limitations.

## References

- [Brendan Gregg: The USE Method](https://www.brendangregg.com/usemethod.html)
- Further reading (blog): [Brendan Gregg — Linux Performance Analysis in 60 Seconds](https://www.brendangregg.com/blog/2015-12-03/linux-perf-analysis-in-60s.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [procps vmstat manual](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Maintainer or personal blog: [Brendan Gregg — USE Method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [Linux perf tools tutorial](https://www.brendangregg.com/perf.html)
