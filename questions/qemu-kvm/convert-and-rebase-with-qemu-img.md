---
title: Convert and rebase disk images with qemu-img
theme: qemu-kvm
difficulty: middle
type: scenario
tags: [qemu, storage, migration, automation]
sources:
  - url: https://www.qemu.org/docs/master/tools/qemu-img.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Convert and rebase disk images with qemu-img

A team imports VMs from VMware and then keeps golden templates as qcow2 overlays for CI clones. Describe the qemu-img operations the pipeline needs and the mistakes that produce broken or bloated images.

## Answer guide

- Import is convert: read the source format (vmdk, vpc, vdi, raw), write the target — qcow2 or raw — with sparseness preserved and, where the destination filesystem wants it, preallocation chosen deliberately (metadata or falloc for fast allocation, full when you must avoid runtime first-write cost). Run it against a quiesced source or a snapshot of it, or you are converting a moving target and inheriting a crash-consistent-at-best disk.
- The CI template trick is backing files: create an overlay with -b pointing at the read-only golden image, and every clone writes only its own deltas. Discipline is the chain: a clone that gets re-cloned, or a commit that never finishes, builds backing chains whose read latency grows with depth. Flatten deliberately with rebase onto an empty base or commit the overlay in.
- rebase is the subtle one: safe rebase copies the delta the overlay holds so it can point at a new base; unsafe rebase just rewrites the pointer and lies about the content — valid only when the new base is byte-identical to the old one, for example after moving the file. Mixing the two up corrupts data quietly, which is the worst kind of corruption.
- Make check, info, and resize routine steps: qemu-img check (and its repair modes) after any abnormal exit, info to verify the backing chain and actual size you are about to ship, resize before the guest hits the last-allocated-byte wall you forgot to alert on.

## References

- [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [qemu-img manual](https://www.qemu.org/docs/master/tools/qemu-img.html)
- Manual or specification: [QEMU invocation reference](https://www.qemu.org/docs/master/system/invocation.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
