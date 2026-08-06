---
title: Recover access to an unreachable server without physical presence
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, troubleshooting, availability]
sources:
  - url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.21.0.pdf
    source_type: standard
    verified_on: 2026-08-06
---

# Recover access to an unreachable server without physical presence

A production host no longer responds on its network interface. What out-of-band recovery path would you use and what evidence would you gather before restarting it?

## Answer guide

- Use a management controller such as IPMI, iDRAC, or iLO to inspect console output, health sensors, and power state.
- Preserve logs and assess blast radius before issuing a reset.
- Distinguish a host fault from an upstream network, DNS, or authentication failure.

## References

- [DMTF Redfish specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.21.0.pdf)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)
