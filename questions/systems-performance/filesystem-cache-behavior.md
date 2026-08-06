---
title: How does the Linux page cache affect filesystem performance measurements?
theme: systems-performance
difficulty: middle
type: theory
tags: [linux, filesystem, memory, performance]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How does the Linux page cache affect filesystem performance measurements?

## Answer guide

- The page cache retains file-backed data in memory, so repeated buffered reads may measure RAM and cache state rather than storage latency. Writes can complete into cache before later writeback reaches the device.
- State whether a test uses buffered or direct I/O, its working-set size, cache temperature, fsync behavior, and filesystem. Cache hit ratios and dirty-page pressure help explain whether observed throughput is durable or transient.
- Avoid dropping caches casually on production systems because it disrupts workloads and changes the experiment. For durable-write guarantees, use the application and filesystem semantics rather than assuming a write call means media persistence.

## References

- [Linux kernel: memory management concepts](https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html)
- [fsync manual](https://man7.org/linux/man-pages/man2/fsync.2.html)
- Further reading (personal blog): [Brendan Gregg — Linux Page Cache Hit Ratio](https://www.brendangregg.com/blog/2014-12-31/linux-page-cache-hit-ratio.html)

## What to learn next

- Official documentation: [Linux filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/index.html)
- Manual or specification: [open manual](https://man7.org/linux/man-pages/man2/open.2.html)
- Maintainer or personal blog: [Brendan Gregg — page cache](https://www.brendangregg.com/blog/2014-12-31/linux-page-cache-hit-ratio.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [fio documentation](https://fio.readthedocs.io/en/latest/)
