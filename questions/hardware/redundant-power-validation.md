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

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
