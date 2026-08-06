---
title: Plan a hardware refresh without service interruption
theme: hardware
difficulty: senior
type: scenario
tags: [hardware, deployment, capacity-planning, reliability, availability]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan a hardware refresh without service interruption

How do you migrate a service fleet to new server hardware while preserving availability?

## Answer guide

- Qualify the new platform for performance, drivers, firmware, observability, security controls, and workload compatibility; start with a canary and define health and rollback thresholds.
- Add capacity before removing old hosts, move traffic gradually across independent failure domains, and retain the old fleet until the new one has proven stable under expected peaks.
- A synchronized refresh concentrates risk in a new platform and supply chain. Plan for mixed fleets, data migration, license constraints, spare capacity, and a reversible traffic path.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
