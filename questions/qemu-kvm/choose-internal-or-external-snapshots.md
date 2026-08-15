---
title: Choose internal or external disk snapshots
theme: qemu-kvm
difficulty: middle
type: scenario
tags: [snapshots, qemu, libvirt, storage]
sources:
  - url: https://libvirt.org/formatsnapshot.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://www.qemu.org/docs/master/tools/qemu-img.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Choose internal or external disk snapshots

Before a risky in-place upgrade you want a rollback point for a running domain. libvirt offers disk snapshots that live inside the image and ones that create a new overlay file. Which do you take, and what does each cost you later?

## Answer guide

- An internal snapshot folds the point-in-time state into the existing qcow2 file — one artifact, one command, and libvirt can snap disk plus memory together for a consistent paused state. The price: your image is now simultaneously the live disk, the snapshot store, and the thing every future write passes through, so corruption risk and restore granularity both live in one file, and long snapshot histories degrade I/O.
- An external snapshot flips the domain onto a fresh qcow2 overlay whose backing file is the current disk frozen at the moment of the snap. The base becomes read-only — which is exactly what makes it copyable for backup, and what makes rollback a pivot rather than a merge. Cleanup is explicit: blockcommit folds the overlay back, blockpull flattens the chain.
- Chains are the failure mode to respect: every external snapshot adds an overlay, reads walk the whole chain to find data, and a botched commit leaves you with five-deep backing stacks and degraded random I/O. Set a chain-depth limit and a commit schedule, and remember memory snapshots are version-tied to the QEMU that took them — they are a pause button, not an archive.
- For the upgrade case, take the external overlay, upgrade, and either commit on success or pivot back on failure; reserve internal snapshots for quick throwaway checkpoints on images you can afford to lose.

## References

- [libvirt snapshot XML format](https://libvirt.org/formatsnapshot.html)
- [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Manual or specification: [QEMU dirty bitmaps and incremental backup](https://www.qemu.org/docs/master/interop/bitmaps.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [libvirt kbase — full disk backup of a running guest](https://libvirt.org/kbase/live_full_disk_backup.html)
