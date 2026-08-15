---
title: Pin a latency-sensitive VM to NUMA and hugepages
theme: qemu-kvm
difficulty: senior
type: scenario
tags: [numa, cpu, memory, kvm, performance]
sources:
  - url: https://libvirt.org/formatdomain.html#elementsNUMATopology
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://docs.kernel.org/admin-guide/mm/hugetlbpage.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Pin a latency-sensitive VM to NUMA and hugepages

A trading-ish workload in a VM shows jitter that disappears on the same hardware bare-metal. The host is two-socket. Describe the pinning and memory configuration you would apply, how you verify it took effect, and what it costs you in fleet flexibility.

## Answer guide

- Diagnose the NUMA split first: on a two-socket host, a large unpinned VM gets vCPUs and memory scattered across nodes, and every cross-node access pays higher latency and lower bandwidth. Confirm with host numastat and per-node memory accounting before configuring anything — jitter has other causes, and pinning the wrong one is expensive religion.
- Configure alignment rather than just affinity: define the guest's NUMA topology to mirror the host's, pin vCPUs (vcpupin) to pCPUs on the matching nodes, bind guest memory with numatune in strict mode to those nodes, and pin the QEMU emulator and iothreads (emulatorpin, iothreadpin) so housekeeping threads cannot land on the vCPUs' cores mid-burst.
- Add explicit hugepages via memoryBacking (2 MiB or 1 GiB) to cut TLB pressure and stabilise allocation — reserved at boot on the host, because fragmented hugepage pools fail VM starts at the worst time. Prefer explicit hugepages over transparent ones for this class of guest, whose defrag stalls are exactly the jitter you are hunting.
- Verify and price it: vcpuinfo and numatune output versus the plan, guest-side benchmarks for tail latency, then accept the trade — strict pinning strands capacity, blocks consolidation, complicates maintenance (a pinned VM needs a planned re-pinning window, not an opportunistic migration), and one badly pinned VM can be worse than none. This is a scalpel for specific workloads, never a fleet default.

## References

- [libvirt domain XML — NUMA topology and tuning](https://libvirt.org/formatdomain.html#elementsNUMATopology)
- [Linux kernel hugepages administration](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [Linux kernel hugepages administration](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
