---
title: Triage TCP retransmissions on a Linux service
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, networking, tcp, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage TCP retransmissions on a Linux service

How would you investigate a rise in TCP retransmissions without masking packet loss?

## Answer guide

- Scope the affected flows, direction, network path, time window, and client-visible symptom. Compare socket statistics, retransmits, RTT, congestion behavior, interface errors and drops, packet captures where authorized, and application retry rates.
- Check host CPU and softirq capacity, NIC queues, MTU consistency, firewall or load-balancer behavior, and remote endpoint health. Preserve measurements from both sides or network telemetry before changing TCP sysctls.
- Retransmission is a recovery mechanism, not proof that one host is at fault. Increasing buffers, retries, or timeouts can hide loss and increase tail latency; make changes only after establishing the loss or delay domain and validating rollback.

## References

- [Linux kernel: IP and TCP sysctl documentation](https://www.kernel.org/doc/html/latest/networking/ip-sysctl.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux networking documentation](https://www.kernel.org/doc/html/latest/networking/index.html)
- Manual or specification: [tcp(7)](https://man7.org/linux/man-pages/man7/tcp.7.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [ss(8)](https://man7.org/linux/man-pages/man8/ss.8.html)
