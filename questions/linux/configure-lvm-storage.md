---
title: Configure LVM storage for a growing service
theme: linux
difficulty: middle
type: scenario
tags: [linux, storage, filesystem, operations, lfcs]
sources:
  - url: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/basic-logical-volume-management
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure LVM storage for a growing service

A service needs more capacity without changing its mount path. How would you extend its LVM-backed filesystem safely, and what must you verify before and after the change?

## Answer guide

- First identify the mounted filesystem, backing logical volume (LV), volume group (VG), physical volumes, filesystem type, and real capacity demand. Confirm that the VG has free extents or plan an approved new physical volume; an LV cannot be extended from capacity that does not exist in its VG.
- Take or verify a tested backup and any application-consistency requirement before changing storage. Extend the LV and filesystem using the distribution-supported tooling, and distinguish online-growth support from shrink operations: many common filesystems can grow online, while reducing a filesystem or LV has stricter offline and recovery requirements.
- Verify the intended mount, ownership, quota, and free space after the change, then observe application errors, latency, and storage alerts. Do not treat LVM snapshots as a backup: snapshot space can fill, copy-on-write activity can affect performance, and a rollback changes data visible to the application.

## References

- [Red Hat Enterprise Linux: basic logical volume management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/basic-logical-volume-management)
- Further reading (blog): [Seth Kenlon — manage storage with LVM](https://opensource.com/article/18/11/manage-storage-lvm)

## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Vidar Holen — Linux Ate My RAM](https://www.linuxatemyram.com/)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
