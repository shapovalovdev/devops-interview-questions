---
title: Investigate Linux memory pressure without immediately adding RAM
theme: linux-troubleshooting
difficulty: junior
type: troubleshooting
tags: [linux, memory, oom, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate Linux memory pressure without immediately adding RAM

## Answer guide

- Establish whether the symptom is allocation failure, reclaim latency, swapping, cgroup pressure, or an OOM kill. Read `dmesg`/journal evidence, `/proc/meminfo`, process RSS, and the workload's request rate together.
- Separate page cache from unreclaimable memory and check cgroup limits when the workload is containerized. High used memory alone is not proof of a leak because Linux uses spare memory for cache.
- Capture evidence before restarting the process, set safe limits or reduce load, and verify after mitigation. Do not disable the OOM killer globally; it can turn a contained failure into a host-wide stall.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

