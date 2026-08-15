---
title: Design live migration for a fleet with mixed CPU generations
theme: qemu-kvm
difficulty: staff
type: scenario
tags: [live-migration, capacity-planning, kvm, change-management]
sources:
  - url: https://libvirt.org/migration.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://libvirt.org/formatdomain.html#elementsCPU
    source_type: official-docs
    verified_on: 2026-08-15
---

# Design live migration for a fleet with mixed CPU generations

Your hardware refresh cycle means any host can be three Intel generations and one AMD swing away from any other. Design the migration strategy that keeps routine evacuation possible across that fleet.

## Answer guide

- Make CPU compatibility a fleet contract, not a per-migration prayer: baseline a named CPU model across every pool you intend to migrate within (hypervisor-cpu-baseline over the pool's capabilities), encode it in the mandatory domain template, ban host-passthrough outside a documented exception process for single-host-pinned VMs, and enforce it in the definition pipeline so a hand-edited XML cannot quietly strand a VM on one host forever. Vendor boundaries become pool boundaries: no Intel-to-AMD migrations, so placement policy must respect pools before any bandwidth discussion starts.
- Budget the shared resources like capacity planning, because migration is a load: a dedicated migration network (or VLAN with QoS), per-host incoming/outgoing concurrency limits — two concurrent migrations in, not eight, because memory bandwidth saturation degrades every guest on the target — and per-migration bandwidth caps so an evacuation cannot starve production traffic. Derive the numbers from measured dirty rates per workload class, not from a vendor slide.
- Set convergence and cutover policy per tier: auto-converge on by default (a migration that cannot converge is worse than one that throttles), postcopy as an explicit opt-in for tiers that prefer availability over a small consistency risk window, TLS mandatory across sites, and a scriptable cancel that leaves the source authoritative. The runbook for a failed mid-flight migration is written, rehearsed, and boring — that is the point.
- Run the strategy as a program: per-tier dashboards for downtime, convergence time, and post-migration guest health; canary waves before mass evacuations; a compatibility matrix regenerated whenever a new CPU generation joins; and a quarterly drill that migrates the nastiest workload (the 200 GB write-heavy database) across the oldest-to-newest pair in the fleet. The failure mode you are designing against is the one nobody rehearsed: a new server generation arriving, being declared "compatible enough", and turning the next maintenance window into an outage.

## References

- [libvirt migration documentation](https://libvirt.org/migration.html)
- [libvirt domain XML — CPU model and topology](https://libvirt.org/formatdomain.html#elementsCPU)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora quick docs — virtualization getting started](https://docs.fedoraproject.org/en-US/quick-docs/virtualization-getting-started/)
