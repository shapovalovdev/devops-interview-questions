---
title: Diagnose a Linux TCP accept-backlog overflow
theme: linux-networking
difficulty: senior
type: troubleshooting
tags: [linux, networking, tcp, troubleshooting, performance]
sources:
  - url: https://docs.kernel.org/networking/ip-sysctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a Linux TCP accept-backlog overflow

A service accepts connections intermittently during a traffic spike. How do you investigate backlog pressure?

## Answer guide

- Measure connection rates, listen queue state, application accept latency, CPU, file descriptors, and TCP counters before changing sysctls. The effective queue is constrained by both application `listen` behavior and kernel limits, and overload may originate upstream.
- Use socket statistics and captures to distinguish SYN pressure, completed handshakes waiting for application accept, and downstream application stalls. Check reverse proxies and load balancers because retries can amplify a saturated listener.
- Tune only after the bottleneck is known. A larger queue can absorb a short burst but does not increase application capacity and may increase latency or memory use; SYN cookies and timeouts have trade-offs. Load-test the chosen limits, alert on saturation, and retain safe connection shedding.

## References

- [Linux kernel: IP and TCP sysctl documentation](https://docs.kernel.org/networking/ip-sysctl.html)
- Further reading (blog): [Cloudflare: how to drop 10 million packets](https://blog.cloudflare.com/how-to-drop-10-million-packets/)
