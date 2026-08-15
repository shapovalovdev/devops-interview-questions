---
title: Read a libvirt domain's states
theme: qemu-kvm
difficulty: junior
type: theory
tags: [libvirt, kvm, linux, operations]
sources:
  - url: https://libvirt.org/manpages/virsh.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Read a libvirt domain's states

`virsh list --all` shows one domain as running, one as paused, one as "in shutdown", and two as shut off. What do these states mean, and which one would make you hesitate before issuing a destroy?

## Answer guide

- A domain is libvirt's object for one virtual machine — its persistent XML plus, when powered, a live QEMU process. The list states describe the QEMU process and guest execution: running, paused means suspended to memory with vCPUs stopped but RAM retained, "in shutdown" is the transient window while the guest is reacting to a graceful shutdown request, and shut off means no process exists.
- Two shut-off domains can still differ in an operationally important way: a persistent domain keeps its XML and will start again, a transient one disappears on shutdown, and a domain with a managed-save image will resume its previous memory state on next start instead of booting fresh.
- Graceful shutdown asks the guest (ACPI or agent) to quiesce; destroy pulls the power, with the same data-loss consequences as a bare-metal power cut. The state that demands care is paused: a shutdown request will sit pending until you resume, and destroying it discards the memory state a user may have expected to keep.
- `virsh domstate --reason` is the honest source, because the reason code — crashed, migrated, saved, failed, or user request — tells you what happened before you decide what to do next.

## References

- [virsh manual](https://libvirt.org/manpages/virsh.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [virsh command reference](https://libvirt.org/manpages/virsh.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
