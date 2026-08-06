---
title: Triage a degrading production disk
theme: hardware
difficulty: middle
type: troubleshooting
tags: [hardware, storage, troubleshooting, reliability]
sources:
  - url: https://www.smartmontools.org/wiki/FAQ
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a degrading production disk

A host reports I/O errors and worsening disk health. What do you do before replacing hardware?

## Answer guide

- Confirm the affected device, workload, redundancy state, error history, and backups; distinguish drive errors from a cable, HBA, enclosure, filesystem, or network-storage fault.
- Reduce risk first: drain workloads or fail over if the service design permits, verify an independently recoverable copy, and preserve logs and device diagnostics.
- Follow the vendor and array procedure for replacement, then watch rebuild, error counters, latency, and replica health. Forcing a replacement without identifying the array member can degrade or destroy a healthy set.

## References

- [smartmontools FAQ](https://www.smartmontools.org/wiki/FAQ)
- Further reading (blog): [Backblaze: Using machine learning to predict hard-drive failures](https://www.backblaze.com/blog/using-machine-learning-to-predict-hard-drive-failures/)
