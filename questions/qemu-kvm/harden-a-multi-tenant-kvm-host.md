---
title: Harden a multi-tenant KVM host
theme: qemu-kvm
difficulty: staff
type: scenario
tags: [kvm, security, multi-tenancy, selinux, least-privilege]
sources:
  - url: https://www.qemu.org/docs/master/system/security.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://libvirt.org/auth.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Harden a multi-tenant KVM host

You are opening a virtualization platform to tenants you do not fully trust — internal teams today, possibly externals later. Design the isolation architecture and name the trade-offs you are consciously accepting.

## Answer guide

- Start from a threat model, not a checklist: tenant-to-host escape through the QEMU device emulation attack surface, tenant-to-tenant data access through shared storage or memory, and host resource abuse. QEMU has a CVE history worth respecting, so the design question is blast radius per host, not whether escape is possible: cap tenants per host, diversify placement, and make each compromise cost one tenant's slice, not the platform.
- Layer the confinement so no single mechanism is load-bearing: unprivileged per-domain identity with dynamic LSM labelling (SELinux sVirt MCS categories or AppArmor profiles) so VM A cannot open VM B's disks; seccomp filtering of the QEMU process's syscalls; cgroup ceilings on CPU, memory, and I/O; per-tenant network separation (bridges or networks with firewall policy) rather than one shared segment; and management access through polkit-scoped read-write, never blanket libvirt group membership.
- Minimize and harden the guest-facing surface: prefer virtio over legacy emulated devices (less parsing of foreign register-level protocols), disable every device a guest does not need, expose consoles only through authenticated, TLS-protected channels, and treat host-device passthrough as a separate, dedicated-host tier because a passed-through device is root-equivalent trust. Tenant-supplied disk images are untrusted input to QEMU's parsers — sanitize or pre-convert them on disposable staging hosts rather than the production compute fabric.
- Name the trade-offs out loud, because they are policy decisions: KSM reclaims real memory by merging identical pages across tenants, and you disable it for hostile multi-tenancy because page-merging is a known side-channel surface; tight per-VM identities complicate live migration unless the identity model is shared; and shared-storage labelling on NFS has real limitations, so the storage design must respect what the LSM can actually enforce there. Publish what residual risk you accepted — the honest answer to "is this secure?" is a documented blast-radius boundary and the monitoring that watches for it being crossed.

## References

- [QEMU security documentation](https://www.qemu.org/docs/master/system/security.html)
- [libvirt access control](https://libvirt.org/auth.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [QEMU documentation](https://www.qemu.org/docs/master/)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
