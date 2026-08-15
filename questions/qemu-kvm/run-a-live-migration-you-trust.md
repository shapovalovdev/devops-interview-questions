---
title: Run a live migration you can trust
theme: qemu-kvm
difficulty: senior
type: scenario
tags: [live-migration, kvm, libvirt, networking]
sources:
  - url: https://libvirt.org/migration.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Run a live migration you can trust

You must evacuate a host for firmware maintenance without stopping its hundred-odd guests. Explain how pre-copy live migration actually works, what can make it fail or stall, and how you make the cutover safe enough to run unattended.

## Answer guide

- Pre-copy is iterative: with the guest running, QEMU streams all RAM to the target while KVM's dirty-page logging records what the guest rewrites; each pass transfers only the newly dirtied pages. When the remaining dirty set is small enough to copy inside the configured downtime window, the guest is paused, the final delta plus device state moves, and it resumes on the target — downtime is typically tens to hundreds of milliseconds, not the total transfer time.
- Convergence is the failure mode to design for: a guest dirtying pages faster than the wire can carry them never reaches cutover and loops forever. auto-converge throttles the guest's vCPUs to force the dirty rate down, xbzrle compression helps write-heavy working sets, and a hard cap on bandwidth protects production traffic — set all three deliberately instead of discovering the stuck migration during the maintenance window.
- The preconditions are strict and worth scripting: shared storage both hosts see (or an explicit copy-storage decision), CPU features the target can honour (fleet baseline, or the migration refuses at start), compatible QEMU/libvirt on the target, cache modes that permit migration, and a network path with the bandwidth you budgeted. The source remains authoritative until cutover, so a failed migration is a cancellation, not an outage — but a half-configured target that accepted the domain definition can still surprise you later.
- Earn trust with measurements before you need them: per-tier downtime and convergence dashboards, a scripted cancel-and-resume drill, TLS for cross-site moves, and post-migration health checks that verify the guest's services, not just that virsh says running. An evacuation runbook that has never been rehearsed on a 200 GB database VM is a hypothesis, not a procedure.

## References

- [libvirt migration documentation](https://libvirt.org/migration.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [QEMU QMP reference](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora quick docs — virtualization getting started](https://docs.fedoraproject.org/en-US/quick-docs/virtualization-getting-started/)
