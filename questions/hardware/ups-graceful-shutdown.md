---
title: Plan graceful shutdown for loss of utility power
theme: hardware
difficulty: junior
type: scenario
tags: [hardware, power, availability, reliability]
sources:
  - url: https://www.nist.gov/publications/guide-industrial-control-systems-ics-security
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan graceful shutdown for loss of utility power

How would you use UPS-backed power to protect a server during a prolonged power outage?

## Answer guide

- Size and monitor the UPS so it provides enough runtime for an orderly response, not an assumption that every outage will be short. Account for the whole dependency chain, including storage and network equipment.
- On a sustained outage, stop traffic, quiesce and flush stateful workloads, then shut down hosts in a tested dependency order before batteries are exhausted.
- Test alarms, shutdown automation, and recovery periodically. An untested UPS, exhausted batteries, or a hard power-off of storage can turn a power event into data loss or a long restart.

## References

- [NIST guide to industrial control systems security](https://www.nist.gov/publications/guide-industrial-control-systems-ics-security)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)
