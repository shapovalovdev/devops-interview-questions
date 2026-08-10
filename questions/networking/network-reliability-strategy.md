---
title: Set a network reliability strategy
theme: networking
difficulty: staff
type: scenario
tags: [networking, reliability, availability, monitoring]
sources:
  - url: https://sre.google/sre-book/service-level-objectives/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc1812.html
    source_type: standard
    verified_on: 2026-08-06
---

# Set a network reliability strategy

How would you turn recurring network incidents into a reliability strategy shared by platform and application teams?

## Answer guide

- Define user-visible objectives for connectivity: successful request rate, latency by critical path, DNS success, and failure detection/recovery time. Segment them by region, provider, address family, and dependency so aggregate success cannot hide a broken cohort.
- Build an error budget and decision rule with service owners: when to halt risky network changes, invest in redundancy, or accept planned degradation. SLOs are a product/reliability agreement, not merely infrastructure availability percentages.
- Establish layered telemetry and drills: synthetic probes from outside each failure domain, flow/route/DNS metrics, packet evidence, and practiced failover. Measure whether detection and routing changes actually improve the user objective.
- Make architecture trade-offs explicit: multi-path/multi-provider resilience costs money and complexity; a single shared control plane reduces operations but expands blast radius. Fund the risks shown by incident and SLO data rather than treating every link equally.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [RFC 1812: Requirements for IPv4 routers](https://www.rfc-editor.org/rfc/rfc1812.html)
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
