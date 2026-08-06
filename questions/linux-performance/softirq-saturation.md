---
title: Diagnose network softirq saturation
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, networking, cpu, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/networking/scaling.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose network softirq saturation

What evidence indicates packet-processing work is saturating Linux CPUs?

## Answer guide

- Examine per-CPU softirq activity, packet drops, interface queues, interrupt distribution, packet rate, and application latency. Linux networking scaling mechanisms such as RSS, RPS, and RFS affect where receive processing occurs and must be assessed with the NIC and CPU topology.
- Identify whether a few CPUs, queues, or IRQs are overloaded, then correct affinity or queue configuration in a controlled rollout. Confirm NIC driver settings, virtualization limits, and the cost of filtering, encryption, or observability programs.
- Do not equate total bandwidth with packet-processing load: small packets can consume much more CPU. Blindly spreading interrupts can damage cache locality or conflict with other workloads, so capture a baseline and validate throughput plus tail latency.

## References

- [Linux kernel: scaling in the networking stack](https://www.kernel.org/doc/html/latest/networking/scaling.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux networking scaling](https://www.kernel.org/doc/html/latest/networking/scaling.html)
- Manual or specification: [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [ethtool(8)](https://man7.org/linux/man-pages/man8/ethtool.8.html)
