---
title: Model storage as libvirt pools and volumes
theme: qemu-kvm
difficulty: middle
type: theory
tags: [libvirt, storage, volumes, linux]
sources:
  - url: https://libvirt.org/storage.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Model storage as libvirt pools and volumes

Your team currently creates LVM volumes and image files by hand and pastes paths into domain XML. What does libvirt's pool and volume model add, and when is it the wrong abstraction?

## Answer guide

- A storage pool is libvirt's typed handle on a place volumes can live: a directory of image files, an LVM volume group, NFS or iSCSI exports, RBD, ZFS datasets. A volume is an allocation libvirt can create, inspect, clone, resize, and delete inside that pool — with capacity, allocation, and format tracked as first-class facts rather than folklore in someone's runbook.
- The payoff is operational: provisioning becomes an API call (vol-create from an XML description or directly from a template), clones of golden images are native, capacity reporting is queryable across the fleet, and authenticated pools can keep their secrets in libvirt's secret store instead of a world-readable XML file.
- Pool choice encodes real trade-offs — a dir pool gives you qcow2 files with overlays and snapshots; a logical pool gives raw volumes with LVM-side snapshots and online resize but no qcow2 backing chains; shared pools (NFS, iSCSI, RBD) are what make live migration cheap because both hosts see the same storage. Choose by what your migration and backup story needs, not by what is fastest to set up.
- The abstraction leaks when you work behind its back: volumes created or resized with lvcreate or by hand make libvirt's view stale until a refresh, and pool metadata can drift from reality on NFS where the server is the authority. If the storage system already has a strong API you drive from your platform (a Ceph deployment with its own tooling), using libvirt pools as a thin pass-through is legitimate — pick one source of truth per operation.

## References

- [libvirt storage management](https://libvirt.org/storage.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
