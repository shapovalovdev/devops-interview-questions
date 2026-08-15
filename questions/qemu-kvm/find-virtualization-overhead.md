---
title: Find where virtualization steals your performance
theme: qemu-kvm
difficulty: senior
type: troubleshooting
tags: [kvm, performance, troubleshooting, observability]
sources:
  - url: https://docs.kernel.org/virt/kvm/index.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Find where virtualization steals your performance

A service that did 40k requests per second bare-metal does 18k in a VM, and the team is split between "hypervisor tax is normal" and "the VM is broken". Lay out the diagnosis path that settles it with evidence.

## Answer guide

- Start by locating the steal, not guessing it: guest-side metrics split the loss into CPU (steal per cent, scheduler latency), I/O (await on virtio disks), network (retransmits, context switches), or memory (major faults, ballooning you did not ask for). A guest at 5% steal and 40 ms disk await is telling you host contention and storage, not CPU emulation, ate the requests.
- On the host, look through QEMU at the same instant: which vCPU threads are runnable and which are running (host scheduler wait), what perf and kvm-style exit counters say about why the guest keeps trapping, whether the emulator thread competes with vCPUs for the same cores, and whether virtio-net is served by vhost in-kernel or falling back through userspace. High host system time inside QEMU with modest guest progress means exits, not useful work.
- The I/O half of the hunt: double caching (guest page cache over host page cache) inflating latency, qcow2 copy-on-write metadata on first writes, deep backing chains, and cache modes whose flush semantics turn each guest fsync into a slow host flush. Compare raw versus qcow2 and cache=none versus writeback on a scratch clone — one variable at a time — before blaming "the hypervisor".
- Close with attribution, not folklore: express the finding as a number (X% lost to host CPU contention, Y ms added by storage flushes), fix what it names — placement, pinning, iothreads, queue depth, format — and keep the benchmark in CI so the tax cannot creep back silently. "Virtualization tax is normal" is a hypothesis that dies to a flame graph.

## References

- [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Further reading (blog): [Brendan Gregg — systems performance](https://www.brendangregg.com/)

## What to learn next

- Official documentation: [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
