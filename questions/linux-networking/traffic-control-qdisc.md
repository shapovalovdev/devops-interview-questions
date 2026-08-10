---
title: Select a Linux traffic-control investigation path
theme: linux-networking
difficulty: senior
type: scenario
tags: [linux, networking, performance, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/tc.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Select a Linux traffic-control investigation path

A host has latency spikes under egress load. When should you investigate Linux traffic control?

## Answer guide

- Traffic control governs packet scheduling, shaping, policing, and classification on Linux network devices. Inspect current qdiscs and counters with `tc` before assuming the default queue or a configured class is responsible for application latency.
- Correlate queue statistics with interface rate, drops, retransmissions, application latency, CPU, and upstream device telemetry. A local queue can be empty while the bottleneck is a NIC, hypervisor, tunnel, switch, or remote receiver.
- Treat shaping and policing as product decisions: they can protect latency-sensitive traffic but may intentionally drop or delay bulk traffic. Define classes and burst assumptions, test under realistic load, and deploy reversible changes; an incorrect classifier can silently starve critical flows.

## References

- [tc(8): Linux traffic-control utility](https://man7.org/linux/man-pages/man8/tc.8.html)
- Further reading (blog): [Cloudflare: how to drop 10 million packets](https://blog.cloudflare.com/how-to-drop-10-million-packets/)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
