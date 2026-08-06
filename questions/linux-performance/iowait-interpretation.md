---
title: Interpret iowait without blaming storage immediately
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, storage, monitoring, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/iostats.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Interpret iowait without blaming storage immediately

What does high iowait suggest, and how do you investigate it safely?

## Answer guide

- Iowait is CPU accounting time while the CPU has idle tasks and waits for outstanding I/O; it is a clue, not a disk-latency measurement. Inspect device I/O statistics, queue depth, latency, throughput, filesystem errors, and the processes issuing I/O.
- Compare the signal by device and interval with application latency and storage limits. Check for page-cache misses, writeback, network filesystems, throttling, and a single noisy tenant before changing an I/O scheduler or storage tier.
- Iowait can be zero during a storage problem on a busy CPU, and high iowait can arise from workloads that are not user-visible. Avoid concluding “the disk is slow” without measured completion latency and a known workload baseline.

## References

- [Linux kernel: I/O statistics](https://www.kernel.org/doc/html/latest/admin-guide/iostats.html)
- Further reading (blog): [Brendan Gregg — Linux Disk I/O](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux block layer documentation](https://www.kernel.org/doc/html/latest/block/index.html)
- Manual or specification: [iostat(1)](https://man7.org/linux/man-pages/man1/iostat.1.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux kernel I/O statistics](https://www.kernel.org/doc/html/latest/admin-guide/iostats.html)
