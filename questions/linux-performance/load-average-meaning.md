---
title: Interpret Linux load average correctly
theme: linux-performance
difficulty: junior
type: theory
tags: [linux, performance, cpu, monitoring, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc_loadavg.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Interpret Linux load average correctly

What does Linux load average measure, and why is it not a CPU-usage percentage?

## Answer guide

- Load average is the moving average of tasks that are runnable or in uninterruptible sleep, reported over one, five, and fifteen minutes. It is therefore a demand and waiting signal, not the fraction of CPU time currently used.
- Compare it with the number of CPUs, but then inspect runnable tasks, I/O waits, CPU utilization, and application latency. A load above CPU count can be normal during a short burst; sustained growth plus queueing needs investigation.
- Do not diagnose CPU saturation from load alone. Disk or remote-filesystem waits can raise load while CPUs are idle, and virtual machines may have scheduling delay that is invisible in a single load value.

## References

- [proc_loadavg(5): Linux load average fields](https://man7.org/linux/man-pages/man5/proc_loadavg.5.html)
- Further reading (blog): [Brendan Gregg — Linux Load Averages: Solving the Mystery](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [proc_loadavg(5)](https://man7.org/linux/man-pages/man5/proc_loadavg.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux load averages](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
