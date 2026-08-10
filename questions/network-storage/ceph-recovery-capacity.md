---
title: Protect Ceph recovery capacity
theme: network-storage
difficulty: senior
type: scenario
tags: [storage, reliability, performance, capacity-planning, monitoring]
sources:
  - url: https://docs.ceph.com/en/latest/rados/operations/health-checks/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Protect Ceph recovery capacity

What capacity and observability policy keeps a Ceph cluster recoverable after a failure?

## Answer guide

- Maintain operational headroom for replication, backfill, rebalancing, snapshots, and the largest plausible failure domain. Track raw and usable capacity, per-pool placement behavior, near-full/full health warnings, degraded objects, recovery throughput, and client latency.
- Define thresholds linked to an approved action: slow ingestion, add capacity, throttle nonessential workloads, replace a failed device, or pause planned maintenance. Rehearse failure recovery with production-like data distribution rather than deriving a policy from nominal total capacity.
- A cluster that is merely “not full” may still lack space where CRUSH requires new replicas. Aggressively speeding recovery can overload disks and networks, increasing client latency and triggering additional failures; choose limits from tested service objectives.

## References

- [Ceph: health checks and capacity warnings](https://docs.ceph.com/en/latest/rados/operations/health-checks/)
- Further reading (blog): [Ceph developer blog](https://ceph.io/en/news/blog/)

## What to learn next

- Official documentation: [Ceph health checks](https://docs.ceph.com/en/latest/rados/operations/health-checks/)
- Manual or specification: [Ceph architecture](https://docs.ceph.com/en/latest/architecture/)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog)
- Hands-on guide: [Ceph operations guide](https://docs.ceph.com/en/latest/rados/operations/)
