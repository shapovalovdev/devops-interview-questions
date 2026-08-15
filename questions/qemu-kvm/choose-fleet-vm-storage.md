---
title: Choose the storage architecture for a VM fleet
theme: qemu-kvm
difficulty: staff
type: scenario
tags: [libvirt, storage, snapshots, architecture, performance]
sources:
  - url: https://libvirt.org/storage.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://www.qemu.org/docs/master/tools/qemu-img.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Choose the storage architecture for a VM fleet

You are designing storage for a new 400-VM platform: general workloads, a latency-critical database tier, and a CI farm that clones hundreds of short-lived guests a day. Weigh the realistic options and commit to an architecture.

## Answer guide

- Put the options on their real axes. qcow2 on shared NFS: simplest operations, native snapshots and overlays, one filer to run — and a metadata bottleneck plus a coherency and locking story that surfaces at exactly the wrong moment, like synchronized morning boots off a shared template. LVM on shared SAN: raw performance and predictable latency, thick volumes unless you commit to thin pools, snapshots at extent level, and the most operator-intensive path. RBD on Ceph: thin provisioning, clones, snapshots, replication, and natural live migration over distance — bought with a distributed system you must staff, tune, and network properly. Local NVMe: unbeatable latency, no shared-storage migration (you are moving disks, not just RAM), and backups become strictly your problem.
- Map tiers to axes instead of averaging them: the database tier earns local raw volumes or a dedicated LVM group with pinned, measured latency; CI earns qcow2 overlays on shared storage — one golden image, hundreds of copy-on-write clones that exist for minutes, with a mandatory flatten-or-delete policy so backing chains never outlive the job; the general fleet earns the shared pool whose snapshots feed the backup pipeline. A single storage choice for all three tiers optimizes someone's procurement story, not the fleet.
- Make the cross-cutting consequences explicit: live migration assumes shared storage, so a tier's storage choice is its maintenance-window policy; the backup design must fit the storage primitives (external snapshots on qcow2, LVM snaps, RBD snaps — you cannot design one and hope for the other); and thin provisioning anywhere needs pool-level quota and usage alerting, because a thin pool that runs dry at 2 p.m. converts one careless tenant into an outage for everyone on it.
- Commit with numbers and review gates: prototype the two finalists under your actual boot-storm and database I/O profiles before signing, define the capacity model including metadata and snapshot overhead (not just GB), and set quarterly review triggers — clone churn, chain depth, pool utilization, p99 I/O — that force an architecture conversation before the fleet outgrows the decision. The classic failure is not choosing wrong; it is choosing once and never re-examining while the workload mix drifts underneath.

## References

- [libvirt storage management](https://libvirt.org/storage.html)
- [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt QEMU driver](https://libvirt.org/drvqemu.html)
- Manual or specification: [QEMU invocation reference](https://www.qemu.org/docs/master/system/invocation.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
