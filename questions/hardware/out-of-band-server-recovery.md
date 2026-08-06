---
title: Recover access to an unreachable server without physical presence
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, troubleshooting, availability]
---

# Recover access to an unreachable server without physical presence

A production host no longer responds on its network interface. What out-of-band recovery path would you use and what evidence would you gather before restarting it?

## Answer guide

- Use a management controller such as IPMI, iDRAC, or iLO to inspect console output, health sensors, and power state.
- Preserve logs and assess blast radius before issuing a reset.
- Distinguish a host fault from an upstream network, DNS, or authentication failure.
