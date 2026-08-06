---
title: Design spares and failure-domain strategy for physical infrastructure
theme: hardware
difficulty: staff
type: scenario
tags: [hardware, capacity-planning, availability, reliability, incident-response]
sources:
  - url: https://sre.google/sre-book/addressing-cascading-failures/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design spares and failure-domain strategy for physical infrastructure

How would you decide spare inventory and failure domains for a fleet whose services must survive hardware faults?

## Answer guide

- Identify correlated failures—rack, power feed, network domain, firmware cohort, storage enclosure, supplier lot, and region—then place replicas so one credible event cannot remove the required quorum or capacity.
- Hold and test spares based on replacement lead time, failure-rate data, criticality, and the time to safely deploy them; include controllers, optics, and power components, not only whole servers.
- Exercise failover and replacement paths. Counting raw spare servers without compatible firmware, racks, power, or qualified staff gives false resilience and can amplify a cascading incident.

## References

- [Google SRE Book: Addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
