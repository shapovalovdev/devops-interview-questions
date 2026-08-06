---
title: Investigate a Linux out-of-memory kill
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, debugging, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/mm/oom.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a Linux out-of-memory kill

What evidence distinguishes an OOM kill from an ordinary process crash, and what remediation is safe?

## Answer guide

- Inspect kernel logs for the OOM report and victim selection, then correlate time, process/container identity, memory limits, allocation rate, and host or cgroup pressure. An application exit code alone does not establish the cause.
- OOM handling is a last-resort response to failed memory reclaim; it can occur for the host or a memory cgroup. Check working set, cache, leaks, concurrency, limits, and swap policy rather than assuming that adding RAM is sufficient.
- Mitigate with an application-level memory bound, correct requests/limits or cgroup configuration, controlled shedding, and capacity validated under peak load. Avoid arbitrarily protecting every process with OOM adjustments: that can leave the kernel with no recoverable victim.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [Linux kernel: out-of-memory handling](https://www.kernel.org/doc/html/latest/mm/oom.html)
- Further reading: [Linux kernel: cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
