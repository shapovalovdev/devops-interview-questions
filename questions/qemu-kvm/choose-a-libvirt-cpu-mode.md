---
title: Choose a libvirt CPU mode for a fleet
theme: qemu-kvm
difficulty: middle
type: scenario
tags: [libvirt, cpu, live-migration, kvm]
sources:
  - url: https://libvirt.org/formatdomain.html#elementsCPU
    source_type: official-docs
    verified_on: 2026-08-15
---

# Choose a libvirt CPU mode for a fleet

You are defining the domain template every new VM will inherit. The hosts span three CPU generations, and you want live migration to keep working. Which CPU mode do you standardize on, and what do the alternatives trade away?

## Answer guide

- mode='host-passthrough' hands the guest the exact CPU it stands on: maximum instruction sets, best niche performance — and a migration landmine, because the target host must, in the general case, be able to present the identical CPU the guest booted with. Fine for a single-host pinned VM, wrong for a fleet template.
- mode='host-model' asks libvirt to pick the closest named model this host can provide. Convenient and mostly migratable, but what "closest" means differs across generations, so the guest can still end up with features the next host cannot serve — the failure appears only on the migration you needed at 3 a.m.
- mode='custom' with an explicit named model and feature policy is the fleet answer: compute the baseline across every host you migrate between (virsh hypervisor-cpu-baseline over the pool's capabilities), name it once in the template, and every guest is migratable by construction, sacrificing the newest instructions nobody has migrated to yet.
- Remember topology and vendor are separate axes from features: sockets/cores/threads choices are guest-visible and stable, while crossing an Intel-to-AMD boundary is generally a wall regardless of mode. Revisit the baseline when a genuinely new generation joins the pool — an old baseline keeps compatibility but quietly caps performance.

## References

- [libvirt domain XML — CPU model and topology](https://libvirt.org/formatdomain.html#elementsCPU)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora quick docs — virtualization getting started](https://docs.fedoraproject.org/en-US/quick-docs/virtualization-getting-started/)
