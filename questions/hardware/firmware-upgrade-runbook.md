---
title: Plan a production server firmware upgrade
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, firmware, deployment, reliability, security]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/193/final
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan a production server firmware upgrade

How do you upgrade BIOS, BMC, storage-controller, or NIC firmware safely in production?

## Answer guide

- Establish the exact platform, component versions, vendor-approved target, release notes, dependencies, maintenance window, and tested recovery path before changing anything.
- Canary the upgrade on representative noncritical hosts, drain workloads, retain power and management connectivity, record results, then roll out in controlled batches with health gates.
- Firmware is platform-specific and some updates are irreversible or change defaults. Never treat it like an ordinary package update; a failed flash or incompatible sequence can leave a host unreachable.

## References

- [NIST SP 800-193: Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
