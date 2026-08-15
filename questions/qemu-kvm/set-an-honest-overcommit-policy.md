---
title: Set an honest overcommit policy for a VM fleet
theme: qemu-kvm
difficulty: staff
type: scenario
tags: [kvm, memory, cpu, capacity-planning, slo]
sources:
  - url: https://docs.kernel.org/admin-guide/mm/ksm.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://docs.kernel.org/virt/kvm/index.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Set an honest overcommit policy for a VM fleet

Leadership quotes a 10:1 CPU and 2:1 memory overcommit ratio from a vendor deck and asks why your platform "wastes" hardware. Write the policy that makes overcommit a per-tier contract instead of a fleet-wide bet.

## Answer guide

- Reframe the number: an overcommit ratio is only meaningful per workload class, because the mechanisms differ. CPU overcommit spends scheduler wait — fine at 5:1+ for bursty dev and CI guests whose cores idle between builds, corrosive at even 1.5:1 for latency-tier guests, where vCPU queuing turns into lock-holder stalls and guest-visible jitter that no benchmark in the vendor deck measured.
- Memory overcommit spends someone else's latency, and every tool has a price: guest memory is handed out lazily so the lie holds until pages are touched; ballooning needs in-guest cooperation and can force paging inside a guest that never agreed to it; KSM dedups identical pages (real savings on a template fleet, CPU cost always, and a side-channel you switch off for hostile tenants); host-level swapping of QEMU memory is not a technique, it is an outage. The policy line is hard: guarantees for prod tiers, honest burst ceilings for the rest, and never a promise the host cannot keep at 3 a.m.
- Make it a contract with admission control and instrumentation: each tier carries a commitment (guaranteed vCPU and memory, allowed burst, priority under contention), placement refuses a VM whose guarantee the host cannot honour — a rejected deploy is honest, an accepted one that cannot perform is a lie with a support ticket — and you monitor both sides (guest steal, major faults, balloon current versus target; host ksmd CPU, reclaim rates, cgroup ceilings) with per-tier alerts.
- Tie the ratios to capacity planning and review: publish actual per-tier utilization and the derived safe ratios quarterly, model the failure mode explicitly (what happens when ten bursting tenants plus a ballooned database meet one host — the host OOM killer picking a QEMU process is the wrong tenant being sacrificed), and keep headroom as a named budget line so "waste" has a competing number in the meeting. The failure mode of this policy is arithmetic drift: ratios quoted as one fleet-wide figure while the workload mix quietly changes underneath.

## References

- [Linux kernel KSM administration](https://docs.kernel.org/admin-guide/mm/ksm.html)
- [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Manual or specification: [Linux kernel KSM administration](https://docs.kernel.org/admin-guide/mm/ksm.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
