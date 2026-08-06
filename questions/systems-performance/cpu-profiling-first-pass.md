---
title: What is a safe first pass for investigating unexpected CPU consumption?
theme: systems-performance
difficulty: junior
type: troubleshooting
tags: [linux, cpu, performance, debugging]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# What is a safe first pass for investigating unexpected CPU consumption?

## Answer guide

- Confirm the scope with per-process and per-thread CPU, request rate, and deployment changes. Distinguish user, system, interrupt, steal, and throttled time before assuming application code is at fault.
- Capture a bounded profile with appropriate privileges and overhead controls, then inspect hot functions, call paths, and symbols. Sampling identifies likely CPU consumers; it does not prove a causal fix by itself.
- Reproduce or corroborate the finding under representative load, then compare after a small change. Protect sensitive symbols and production capacity: profiling permissions, sampling frequency, and debug packages vary by host and kernel.

## References

- [Linux kernel: perf events security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- [perf-record manual](https://man7.org/linux/man-pages/man1/perf-record.1.html)
- Further reading (blog): [Brendan Gregg — perf Examples](https://www.brendangregg.com/perf.html)

## What to learn next

- Official documentation: [Linux perf security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Manual or specification: [perf record manual](https://man7.org/linux/man-pages/man1/perf-record.1.html)
- Maintainer or personal blog: [Brendan Gregg — perf](https://www.brendangregg.com/perf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [perf wiki](https://perf.wiki.kernel.org/)
