---
title: Validate redundant server power paths
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, power, availability, reliability]
sources:
  - url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0268_2025.2.pdf
    source_type: standard
    verified_on: 2026-08-06
---

# Validate redundant server power paths

How do you verify that a dual-power-supply server actually tolerates the loss of one power path?

## Answer guide

- Verify that each supply is connected to a distinct, correctly sized power distribution path and that both report healthy input and output through the management plane.
- Perform a scheduled, observed single-path test with workload and power telemetry, respecting facility change controls and the remaining path’s capacity.
- Redundant supplies on the same PDU, circuit, or maintenance domain are not end-to-end redundancy. Do not test both feeds together or assume a green power LED proves upstream diversity.

## References

- [DMTF Redfish data model specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0268_2025.2.pdf)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)
