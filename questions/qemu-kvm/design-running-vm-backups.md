---
title: Design backups for running VMs
theme: qemu-kvm
difficulty: senior
type: scenario
tags: [snapshots, storage, libvirt, qemu, reliability]
sources:
  - url: https://libvirt.org/kbase/live_full_disk_backup.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://www.qemu.org/docs/master/interop/bitmaps.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Design backups for running VMs

Design the backup pipeline for VMs that are never shut down: how you get a consistent copy without a maintenance window, how you make it incremental, and how you prove it restores.

## Answer guide

- Pick your consistency level explicitly. A raw image copied while the guest writes is crash-consistent at best — journaled filesystems survive, but in-flight database transactions may not. The qemu-guest-agent closes that gap: quiesce freezes guest filesystems for the snapshot instant, giving filesystem-level consistency; application-consistent backups additionally use in-guest hooks (pre/post scripts around the freeze).
- The standard full-backup shape is snapshot, copy, pivot: with the guest frozen, create an external snapshot so writes divert to an overlay, copy the now-stable base to the backup target, then blockcommit to fold the overlay back and keep the freeze window to seconds. Keep the freeze short and measured — a long-frozen database is an outage in disguise.
- Incremental lives one layer below: QEMU persistent dirty bitmaps record which clusters changed since a checkpoint, so each backup ships only those clusters plus a fresh bitmap, turning a nightly full into weekly-full-plus-daily-deltas. Watch the operational sharp edges: bitmaps are per-disk and must be tracked across the chain, a failed backup needs a defined bitmap reset policy, and restores must replay the base plus increments in order — automate that, because a human will not.
- The design is only finished when restores are routine: schedule quarterly restore drills that boot the recovered image, verify application-level integrity (does the database open, do the tables checksum), and measure both freeze duration and backup wall-clock as first-class metrics. An unrestorable backup is a screenshot of your data, and every VM tier should carry an explicit RPO/RTO you can defend.

## References

- [libvirt kbase — live full disk backup](https://libvirt.org/kbase/live_full_disk_backup.html)
- [QEMU dirty bitmaps and incremental backup](https://www.qemu.org/docs/master/interop/bitmaps.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [QEMU dirty bitmaps and incremental backup](https://www.qemu.org/docs/master/interop/bitmaps.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [libvirt kbase — live full disk backup of a running guest](https://libvirt.org/kbase/live_full_disk_backup.html)
