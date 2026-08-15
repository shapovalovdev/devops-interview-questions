---
title: Operate memory ballooning under host pressure
theme: qemu-kvm
difficulty: middle
type: theory
tags: [kvm, memory, virtio, monitoring]
sources:
  - url: https://libvirt.org/formatdomain.html#elementsMemBalloon
    source_type: official-docs
    verified_on: 2026-08-15
---

# Operate memory ballooning under host pressure

Host memory runs short and someone suggests "just balloon a few guests". Explain what the virtio balloon actually does, why a guest might refuse to shrink, and what can go wrong for the workload inside.

## Answer guide

- The balloon is a virtio device plus a guest driver: when the host asks for memory back, the guest driver allocates pages inside the guest and hands them to the balloon, effectively pinning them so guest workloads cannot use them; the host can then reclaim the physical pages for other guests. In libvirt terms, current memory drops toward a new target while max memory stays fixed.
- It is a request, not a command. The guest only has free memory to give if its kernel has reclaimable pages; a guest running mlocked or hugepage-backed workloads, or one already near its own limit, inflates poorly or not at all — the honest check is watching the balloon's current value versus the target you set.
- Reclaim is not free to the guest: pages it can return may first need swapping out or dropping from cache inside the guest, so a ballooned database can take latency spikes precisely when the host is already in trouble. Never treat ballooning as an elasticity mechanism for latency-critical guests.
- Run it as a measured loop, not an emergency lever: enable the balloon and periodic memory stats, set per-domain floors with memtune so a host-pressure event cannot squeeze a guest below what it needs, and watch dommemstat's actual versus RSS — if RSS never falls, the balloon is theatre and you need placement changes instead.

## References

- [libvirt domain XML — memory balloon device](https://libvirt.org/formatdomain.html#elementsMemBalloon)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [virsh command reference](https://libvirt.org/manpages/virsh.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
