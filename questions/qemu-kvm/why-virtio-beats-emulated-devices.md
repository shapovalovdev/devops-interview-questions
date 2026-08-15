---
title: Why virtio beats emulated devices
theme: qemu-kvm
difficulty: junior
type: theory
tags: [virtio, qemu, performance, linux]
sources:
  - url: https://docs.kernel.org/driver-api/virtio/index.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://www.qemu.org/docs/master/system/device-emulation.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Why virtio beats emulated devices

A guest moved from an emulated Intel e1000 NIC to virtio-net and its throughput tripled while host CPU per gigabit dropped. Explain the mechanism a candidate should give, not just the benchmark.

## Answer guide

- An emulated device makes the guest believe real 1990s silicon exists: the guest driver pokes registers on a fake PCI card, and every poke traps the vCPU out of the kernel into QEMU, which simulates what the register write would do. Correct, compatible — and expensive, because a single network packet can cost many such exits.
- A virtio device drops the pretense: the guest loads a driver that knows it is in a virtual machine, and both sides exchange I/O through shared memory descriptor rings. Work moves in batches, so one exit can carry a whole queue of packets instead of one register write at a time.
- The host side of the ring can be served either by QEMU in userspace or by a kernel backend such as vhost-net, which handles network traffic without re-entering QEMU at all — that is where the second tranche of CPU savings comes from.
- The trade to state honestly: virtio needs a guest driver (present in modern Linux and Windows virtio drivers), while emulated hardware boots anywhere. Emulated devices still earn their keep for legacy guests, PXE quirks, and maximum compatibility, not for performance.

## References

- [Linux kernel virtio driver API](https://docs.kernel.org/driver-api/virtio/index.html)
- [QEMU device emulation overview](https://www.qemu.org/docs/master/system/device-emulation.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [QEMU system emulation documentation](https://www.qemu.org/docs/master/system/index.html)
- Manual or specification: [Linux kernel virtio specification and driver API](https://docs.kernel.org/driver-api/virtio/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
