---
title: Design actionable server hardware sensor monitoring
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, sensors, monitoring, troubleshooting, reliability]
sources:
  - url: https://docs.kernel.org/hwmon/index.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design actionable server hardware sensor monitoring

Which hardware sensors should be monitored, and how do you avoid an alert stream that operators cannot act on?

## Answer guide

- Collect temperatures, fan state, power-supply status, voltages, storage/controller health, memory errors, and management-controller reachability with component identity and host context.
- Alert on state changes, sustained threshold breaches, error trends, and loss of monitoring; link alerts to a runbook that names the evidence to collect and the safe containment action.
- Tune thresholds using vendor limits and production history, but do not suppress repeated errors without investigation. A sensor may be absent, stale, or model-specific, so validate collection after hardware changes.

## References

- [Linux kernel hardware monitoring documentation](https://docs.kernel.org/hwmon/index.html)
- Further reading (blog): [Backblaze Drive Stats](https://www.backblaze.com/blog/category/cloud-storage/hard-drive-stats/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
