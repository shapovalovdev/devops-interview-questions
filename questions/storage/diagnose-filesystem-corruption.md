---
title: Respond to suspected filesystem corruption
theme: storage
difficulty: middle
type: troubleshooting
tags: [storage, filesystem, linux, incident-response, troubleshooting, lfcs]
sources:
  - url: https://www.kernel.org/doc/html/latest/filesystems/ext4/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to suspected filesystem corruption

Kernel logs report filesystem metadata errors. What is your safe response sequence?

## Answer guide

- Protect data and evidence first: identify the affected mount and workload, capture relevant logs and device health, stop or fence writes when the filesystem or vendor guidance requires it, and declare the incident.
- Determine whether the symptom is a filesystem, device, controller, network-storage, or application issue. Restore service from a known-good replica or backup when that has lower risk than in-place repair.
- Run the filesystem-specific check or repair only with the correct unmounted/offline conditions and an approved recovery plan; validate recovered data before returning traffic.
- Repair tools can discard or alter damaged metadata. Repeated remount/retry behavior may worsen corruption, so do not run destructive repair commands on a mounted production filesystem without evidence and authorization.

## References

- [Linux ext4 documentation](https://www.kernel.org/doc/html/latest/filesystems/ext4/)
- Further reading (blog): [Red Hat: managing file systems](https://www.redhat.com/en/blog/managing-storage-linux)
