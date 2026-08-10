---
title: Manage a libvirt virtual machine change safely
theme: linux
difficulty: senior
type: scenario
tags: [linux, virtualization, operations, change-management, lfcs]
sources:
  - url: https://libvirt.org/formatdomain.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.libvirt.org/manpages/virsh.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Manage a libvirt virtual machine change safely

How do persistent and running libvirt domain configuration differ, and how would you make a safe virtual-machine resource or device change?

## Answer guide

- Treat a libvirt domain's persistent XML definition and its live runtime configuration as related but distinct states. Determine whether the requested device or resource setting supports live update, persistent update, or both; a successful live change can disappear after reboot if the persistent definition was not updated.
- Capture the current definition and guest/application health before change, validate host capacity and device compatibility, then apply the smallest supported change using the libvirt API or `virsh` with explicit live/config scope. Follow the relevant domain XML semantics rather than editing generated state blindly, especially for disks, interfaces, CPU topology, and memory settings.
- Verify effective runtime state, persistent definition, guest boot behavior, network/storage attachment, and service SLOs. Have a rollback based on the saved known-good definition and tested backups; do not assume detaching a device is harmless when the guest may still be using it.

## References

- [libvirt: domain XML format](https://libvirt.org/formatdomain.html)
- [libvirt: virsh manual](https://www.libvirt.org/manpages/virsh.html)
- Further reading (blog): [Seth Kenlon — use Vagrant with libvirt](https://opensource.com/article/21/10/vagrant-libvirt)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [virsh command reference](https://www.libvirt.org/manpages/virsh.html)
- Maintainer or personal blog: [Lennart Poettering — systemd and Linux articles](https://0pointer.net/blog/)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
