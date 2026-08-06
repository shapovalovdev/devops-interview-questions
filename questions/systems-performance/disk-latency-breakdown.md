---
title: How do you break down elevated disk I/O latency?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, storage, performance, debugging]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/iostats.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you break down elevated disk I/O latency?

## Answer guide

- First locate the latency boundary: application call, filesystem, block device, storage network, or remote service. Pair request latency percentiles with queue depth, throughput, errors, and device utilization.
- Linux block statistics aggregate useful counters but do not fully explain individual requests. Use tracing carefully to distinguish queueing, device service time, flushes, filesystem contention, and remote-storage delays.
- Compare reads and writes, size distribution, sync behavior, and baseline. Increasing queue depth can raise throughput while worsening tail latency; cache, RAID, cloud volume limits, and virtualization make device-level interpretations provider-dependent.

## References

- [Linux kernel: I/O statistics fields](https://www.kernel.org/doc/html/latest/admin-guide/iostats.html)
- [iostat manual](https://man7.org/linux/man-pages/man1/iostat.1.html)
- Further reading (personal blog): [Brendan Gregg — iosnoop for Linux](https://www.brendangregg.com/blog/2014-07-16/iosnoop-for-linux.html)

## What to learn next

- Official documentation: [Linux block layer documentation](https://www.kernel.org/doc/html/latest/block/index.html)
- Manual or specification: [iostat manual](https://man7.org/linux/man-pages/man1/iostat.1.html)
- Maintainer or personal blog: [Brendan Gregg — iosnoop](https://www.brendangregg.com/blog/2014-07-16/iosnoop-for-linux.html)
- Technical blog: [AWS Storage Blog](https://aws.amazon.com/blogs/storage/)
- Hands-on guide: [fio documentation](https://fio.readthedocs.io/en/latest/)
