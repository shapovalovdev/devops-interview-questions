---
title: Diagnose thermal throttling on a server
theme: hardware
difficulty: middle
type: troubleshooting
tags: [hardware, sensors, cpu, troubleshooting, monitoring]
sources:
  - url: https://docs.kernel.org/hwmon/index.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose thermal throttling on a server

Application latency rises under load while CPU utilization looks normal. How would you investigate possible thermal throttling?

## Answer guide

- Compare CPU frequency and throttling counters with temperatures, fan state, power limits, and workload timing; utilization alone does not show reduced effective clock speed.
- Inspect host and management-controller sensors, air flow, inlet temperature, failed fans, heatsink installation, and rack-level cooling conditions.
- Reduce load or move traffic before a thermal emergency, then fix the physical cause and validate under controlled load. Raising alert thresholds or disabling protections risks shutdown and component damage.

## References

- [Linux kernel hardware monitoring documentation](https://docs.kernel.org/hwmon/index.html)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
