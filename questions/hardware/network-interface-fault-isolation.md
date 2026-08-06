---
title: Isolate a server network-interface fault
theme: hardware
difficulty: middle
type: troubleshooting
tags: [hardware, networking, troubleshooting, monitoring, reliability]
sources:
  - url: https://docs.kernel.org/networking/statistics.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Isolate a server network-interface fault

How do you determine whether intermittent packet loss is caused by the host NIC, cable, switch port, or software configuration?

## Answer guide

- Compare host interface counters, link state, driver and firmware events, and packet captures with switch-port counters and errors at the same time boundary.
- Swap one controlled variable at a time—cable, transceiver, port, NIC function, or host—while preserving redundant connectivity and recording the outcome.
- Packet loss can be caused above the physical layer, so validate routing, MTU, congestion, and application behavior too. Replacing a NIC before correlating both ends can hide a failing port or configuration regression.

## References

- [Linux kernel networking statistics](https://docs.kernel.org/networking/statistics.html)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)
