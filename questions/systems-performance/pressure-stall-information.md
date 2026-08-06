---
title: What does Linux pressure stall information add to resource monitoring?
theme: systems-performance
difficulty: middle
type: theory
tags: [linux, cpu, memory, performance]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# What does Linux pressure stall information add to resource monitoring?

## Answer guide

- PSI reports time tasks are delayed by CPU, memory, or I/O resource pressure. It complements utilization because it measures waiting experienced by work, including periods where a resource is not simply 100% busy.
- Use the some and full averages with workload latency, cgroup scope, and a baseline. Some pressure means at least one task stalled; full pressure has stricter semantics and should not be conflated with general utilization.
- PSI is a sampled aggregate signal, not a root-cause tool. A threshold should trigger investigation or controlled admission decisions, then tracing or subsystem metrics must identify the contended resource and workload.

## References

- [Linux kernel: PSI](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- [Linux kernel: cgroup v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading (blog): [Brendan Gregg — Linux Pressure Stall Information](https://www.brendangregg.com/blog/2018-08-31/linux-psi.html)

## What to learn next

- Official documentation: [Linux PSI](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Manual or specification: [proc pressure interface](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Maintainer or personal blog: [Brendan Gregg — PSI](https://www.brendangregg.com/blog/2018-08-31/linux-psi.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [Prometheus node exporter](https://github.com/prometheus/node_exporter)
