---
title: Define a standard hardware platform without blocking product teams
theme: hardware
difficulty: staff
type: scenario
tags: [hardware, platform-engineering, governance, reliability, security]
sources:
  - url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.21.0.pdf
    source_type: standard
    verified_on: 2026-08-06
---

# Define a standard hardware platform without blocking product teams

How would you standardize server hardware across teams while allowing justified workload-specific exceptions?

## Answer guide

- Publish supported reference platforms with tested firmware, management APIs, operating-system images, observability, spare parts, capacity characteristics, and a clear support contract.
- Use an exception process that requires a measurable workload need, total-cost and operational analysis, owner, and expiry/review date; feed repeated exceptions back into the platform roadmap.
- Standardization improves automation and incident response, but a mandate that ignores GPU, storage, latency, or compliance needs creates shadow infrastructure. Avoid allowing permanent exceptions without ownership.

## References

- [DMTF Redfish specification](https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.21.0.pdf)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)
