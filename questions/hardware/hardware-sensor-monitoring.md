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
