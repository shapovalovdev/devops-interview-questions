---
title: Simulate an availability-zone or region failure
theme: chaos-engineering
difficulty: senior
type: scenario
tags: [chaos-engineering, cloud, availability, capacity-planning]
sources:
  - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Simulate an availability-zone or region failure

How do you rehearse losing a whole zone, and what makes a region drill different?

## Answer guide

- A zone drill is primarily a capacity and correlation test. Removing one of three zones removes roughly a third of capacity at once, so the hypothesis must include the remaining zones absorbing the load without breaching latency or error objectives. Simulate it by shifting traffic away from the zone, then by isolating it — blocking cross-zone traffic and terminating its instances — because a zone that is unreachable but still advertising itself behaves worse than one cleanly removed.
- Static stability is what you are really checking: can the surviving zones serve without needing a control-plane action to succeed during the event? Pre-provisioned headroom, health-check-based routing, and zonal-aware load balancing survive; designs that must launch new capacity or call a scaling API mid-failure inherit the failure of whatever they depend on. Confirm quorum members, leader placement, and connection pools are distributed so that one zone is never decisive.
- A region drill is a different exercise. It is slower, involves data replication lag and therefore a recovery point objective, usually needs a deliberate decision rather than an automatic failover, and touches identity, DNS, artifact registries, CI, and secrets that may themselves be single-region. Run it as a scheduled evacuation with the business informed, and measure recovery time and data loss against the stated objectives rather than against hope.
- Failure modes: cross-zone data-transfer costs and quotas discovered mid-drill; autoscaling limited by instance-type availability in the surviving zones; a "multi-region" service whose configuration store, feature flags, or observability stack lives in one region; failback that is untested and more dangerous than the failover; and drills that are announced so thoroughly that teams pre-scale, which proves nothing about an unannounced event.

## References

- [AWS — regions and availability zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- Further reading (blog): [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [AWS — regions and availability zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- Manual or specification: [AWS Fault Injection Service targets and selection modes](https://docs.aws.amazon.com/fis/latest/userguide/targets.html)
- Maintainer or personal blog: [Adrian Cockcroft — architecture and resilience writing](https://adrianco.medium.com/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Builders' Library — static stability using availability zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
