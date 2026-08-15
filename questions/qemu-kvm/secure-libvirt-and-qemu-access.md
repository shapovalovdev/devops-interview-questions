---
title: Secure libvirt and QEMU access on a shared host
theme: qemu-kvm
difficulty: senior
type: scenario
tags: [libvirt, security, permissions, selinux, least-privilege]
sources:
  - url: https://libvirt.org/auth.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://www.qemu.org/docs/master/system/security.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Secure libvirt and QEMU access on a shared host

Several teams share one virtualization host. Design the access model: who may manage domains, how the QEMU processes are contained, and how guest disks stay isolated from each other.

## Answer guide

- Model the two privilege boundaries honestly. The system libvirt daemon is root-adjacent: membership in the libvirt group, or a polkit grant on the system connection's manage action, is effectively the ability to define a domain whose disk points at any file on the host — treat it as root, hand it to almost no one, and use polkit rules or the read-only socket for teams that only need to observe their own domains.
- The QEMU processes themselves run unprivileged: libvirt drops each domain to a dedicated identity and confines it with cgroup device/memory/CPU limits, namespaces, seccomp syscall filtering, and — the piece doing per-VM isolation — dynamic LSM labels. Under SELinux sVirt each running domain gets its own MCS category and its disk images get matching labels, so VM A's process cannot open VM B's image even if both run as the same nominal user; AppArmor provides the equivalent confinement on those distributions.
- Keep the labelling automatic and in-band: images provisioned through libvirt get correct contexts; out-of-band copies need restorecon before a domain will start, and "fixing" denials by disabling SELinux or chmod 777-ing images is removing the isolation the whole design rests on. Reserve host-device passthrough (VFIO) for cases that justify widening the boundary, because a passed-through device is trusted like the guest is root.
- Audit the model in operation: libvirt connection logs, LSM denial logs, image label checks, and periodic review of who holds the libvirt group. The classic failure is quiet accretion — the one contractor added to the group during an incident who is still there two years later, with a domain XML that can read /etc/shadow as a raw disk.

## References

- [libvirt access control](https://libvirt.org/auth.html)
- [QEMU security documentation](https://www.qemu.org/docs/master/system/security.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [libvirt QEMU driver](https://libvirt.org/drvqemu.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
