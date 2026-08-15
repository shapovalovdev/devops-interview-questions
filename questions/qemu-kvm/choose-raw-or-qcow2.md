---
title: Choose raw or qcow2 for a disk image
theme: qemu-kvm
difficulty: junior
type: theory
tags: [qemu, storage, disk, virtualization]
sources:
  - url: https://www.qemu.org/docs/master/tools/qemu-img.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Choose raw or qcow2 for a disk image

You are about to create a 100 GB boot disk for a new domain and must pick the format. What do raw and qcow2 each give up, and what does qcow2 buy with that sacrifice?

## Answer guide

- raw is the honest image: guest block 0 is file offset 0. There is no metadata to consult, nothing to corrupt, and essentially no per-I/O overhead; on a filesystem supporting sparse files it also starts small even though the guest sees 100 GB.
- qcow2 (QEMU copy-on-write, version 2/3) inserts a layer of indirection: the guest's blocks live in clusters whose physical locations are tracked in lookup tables. That buys sparse allocation, internal snapshots, compressed images, encryption lineage, and — the operational superpower — backing files, where a new overlay records only what differs from its base image.
- The cost of that indirection is real: metadata updates on first write to each cluster, slightly more work per request, and a format that needs qemu-img check when a process dies mid-operation. A raw image has nothing to check.
- The practical rule of thumb: raw when the image is the final artifact and the storage layer below (LVM, ZFS, an array) already provides snapshots; qcow2 when you need overlays, snapshots, or compact transfer — templates, CI clones, laptop-grade virtualization. `qemu-img info` tells you which you have, including the backing chain.

## References

- [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Manual or specification: [QEMU invocation reference](https://www.qemu.org/docs/master/system/invocation.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
