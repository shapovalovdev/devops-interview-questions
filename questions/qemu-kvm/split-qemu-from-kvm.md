---
title: Split QEMU's job from KVM's job
theme: qemu-kvm
difficulty: junior
type: theory
tags: [qemu, kvm, libvirt, virtualization]
sources:
  - url: https://www.qemu.org/docs/master/system/index.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://docs.kernel.org/virt/kvm/index.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Split QEMU's job from KVM's job

An interviewer draws three boxes — KVM, QEMU, libvirt — and asks you to fill in what each one actually does when a guest boots and writes to disk.

## Answer guide

- KVM is the kernel side: a module that turns the CPU's virtualization extension into a facility for running guest code natively, exposed through /dev/kvm. It owns nothing a guest can see — no disks, no screens.
- QEMU is the machine: a userspace emulator that builds the guest's world — CPU when running without KVM, memory map, firmware, chipset, and every device model. With KVM, QEMU hands guest execution to the kernel and handles the exits, so it emulates the disk write the guest just made rather than translating every instruction.
- libvirt is the operator's layer above both: it stores domain XML definitions, launches and supervises QEMU processes, wires networks, storage pools, firewall rules, and security labels, and exposes one API so tooling does not shell out to QEMU arguments directly.
- A useful consequence of the split: QEMU can run with no KVM at all (slow, but works anywhere), and libvirt can manage QEMU's cousins; the failure signatures also split cleanly — guest slowness is usually the QEMU/KVM handoff, while "VM will not start" is usually libvirt configuration or permissions.

## References

- [QEMU system emulation documentation](https://www.qemu.org/docs/master/system/index.html)
- [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [QEMU invocation reference](https://www.qemu.org/docs/master/system/invocation.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
