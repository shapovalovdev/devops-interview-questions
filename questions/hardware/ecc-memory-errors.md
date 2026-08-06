---
title: Respond to corrected and uncorrected memory errors
theme: hardware
difficulty: middle
type: troubleshooting
tags: [hardware, memory, troubleshooting, reliability]
sources:
  - url: https://www.kernel.org/doc/html/latest/driver-api/edac.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to corrected and uncorrected memory errors

How should you respond when a server reports corrected or uncorrected ECC memory errors?

## Answer guide

- Corrected errors mean hardware detected and corrected an error; trend them by DIMM, channel, and host because rising errors can be a precursor to failure. Uncorrected errors can cause application crashes, corruption, or a host failure and require urgent containment.
- Collect EDAC, firmware, and management-controller events, then compare the physical location with the server vendor’s mapping before replacing a DIMM.
- Drain critical workloads and coordinate replacement under maintenance controls. Clearing alerts or swapping a DIMM without checking seating, firmware, CPU memory channel, and recurrence can miss the actual fault.

## References

- [Linux kernel EDAC documentation](https://www.kernel.org/doc/html/latest/driver-api/edac.html)
- Further reading (blog): [Backblaze Drive Stats](https://www.backblaze.com/blog/category/cloud-storage/hard-drive-stats/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
