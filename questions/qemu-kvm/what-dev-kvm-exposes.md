---
title: What /dev/kvm exposes to QEMU
theme: qemu-kvm
difficulty: junior
type: theory
tags: [kvm, qemu, linux, kernel]
sources:
  - url: https://docs.kernel.org/virt/kvm/api.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# What /dev/kvm exposes to QEMU

A teammate asks why every virtual machine on the host is "just a QEMU process" yet runs at near-native speed. What is /dev/kvm and what does QEMU do with it?

## Answer guide

- /dev/kvm is the character device the KVM kernel modules (kvm plus kvm_intel or kvm_amd) create once the CPU's hardware virtualization extension is active. It is not a driver for a device the guest uses; it is the door QEMU opens to create guests.
- QEMU calls ioctls on that device — create a VM, add vCPUs and memory regions, run the guest — and the kernel executes guest instructions natively with hardware support, handing control back to QEMU only when the guest does something the kernel will not handle, such as touching an emulated disk.
- The guest therefore costs host CPU only when it exits to QEMU; that is why hardware-assisted virtualization is roughly native while pure emulation is not. Each VM is one ordinary userspace process you can see in ps, cgroup-limit, and oom-score.
- If /dev/kvm is missing or unreadable — module not loaded, virtualization disabled in firmware, wrong group membership — QEMU can still run the guest under its software translator (TCG), and the sudden 10-100x slowdown is the usual symptom.

## References

- [KVM API documentation](https://docs.kernel.org/virt/kvm/api.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [QEMU documentation](https://www.qemu.org/docs/master/)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
