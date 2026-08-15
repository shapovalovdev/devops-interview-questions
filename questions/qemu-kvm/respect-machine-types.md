---
title: Respect machine types when editing guests
theme: qemu-kvm
difficulty: middle
type: theory
tags: [qemu, virtualization, boot, linux]
sources:
  - url: https://www.qemu.org/docs/master/system/i386/pc.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Respect machine types when editing guests

A colleague "modernized" a fleet of older VMs by flipping their domain XML from pc-i440fx to pc-q35 machine types, and the next maintenance reboot brought a wave of complaints. What is a machine type, what did that change actually do, and what is the upgrade rule?

## Answer guide

- The machine type names the emulated chipset a guest boots on: i440fx with legacy PCI, q35 with PCIe (ICH9), versioned per QEMU release. That versioned name is QEMU's compatibility contract — it pins device set, slot layout, firmware behaviour, and quirks so a guest sees identical hardware across QEMU upgrades.
- Changing it is re-plugging the guest's motherboard: PCI slots renumber, devices move, NIC slots and thus predictable interface names can shift, multi-path storage device paths may re-order, and licensed or udev-rule-bound software notices it is "on new hardware". Nothing is conceptually broken — the guest just re-enumerates a machine it did not expect, which is precisely what you do not want during an unrelated maintenance window.
- The rule: a VM keeps its machine type for life; new VMs start on the newest q35 (or aarch64 virt) with UEFI where appropriate, old ones stay on their pinned type until deliberately rebuilt or migrated through a planned re-platform. Machine-type changes are a project with guest-side validation, never a find-and-replace in XML.
- Corollaries worth stating: the version suffix is what makes rolling QEMU upgrades safe for running-and-restarted guests; mixed firmware (BIOS versus OVMF/UEFI) is a separate axis that also changes boot behaviour and must not be flipped casually; and cloning a template means inheriting its machine type — decide it once, centrally.

## References

- [QEMU x86 machine types (i440fx and q35)](https://www.qemu.org/docs/master/system/i386/pc.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [QEMU system emulation documentation](https://www.qemu.org/docs/master/system/index.html)
- Manual or specification: [QEMU invocation reference](https://www.qemu.org/docs/master/system/invocation.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
