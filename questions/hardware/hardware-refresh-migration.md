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
