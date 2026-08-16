# QEMU/KVM related materials

These resources complement the qemu-kvm Theme's Question-level references.
They point at the primary documentation of the projects the Theme covers —
QEMU's own manual, [libvirt's driver and format
references](https://libvirt.org/docs.html), the kernel's KVM API, and the
[KVM project pages](https://www.linux-kvm.org/) — with maintainer and vendor
blogs listed only as further reading. Distribution packaging changes defaults,
so check each recommendation against the QEMU, libvirt, and kernel versions
actually in use.

## What to learn next

- Official documentation: [QEMU documentation](https://www.qemu.org/docs/master/)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)

## Suggested study order

The three-boxes picture opens the Theme because every later answer assumes you
know which layer owns what.

1. [Split QEMU's job from KVM's job](../../questions/qemu-kvm/split-qemu-from-kvm.html)
    — The three-boxes picture opens the Theme: kernel, QEMU, and libvirt each
    own a layer.
2. [What /dev/kvm exposes to QEMU](../../questions/qemu-kvm/what-dev-kvm-exposes.html)
    — What /dev/kvm exposes makes the kernel's half of that split concrete.
3. [Why virtio beats emulated devices](../../questions/qemu-kvm/why-virtio-beats-emulated-devices.html)
    — Virtio's shared-ring mechanism is half the performance vocabulary the
    Theme speaks.
4. [Read a libvirt domain's states](../../questions/qemu-kvm/read-libvirt-domain-states.html)
    — Domain states are the operating grammar you read before acting on any
    guest.
5. [Choose raw or qcow2 for a disk image](../../questions/qemu-kvm/choose-raw-or-qcow2.html)
    — Raw or qcow2 is the first decision a new domain actually forces.
6. [Diagnose a guest silently running under TCG](../../questions/qemu-kvm/diagnose-fallback-to-tcg.html)
    — The silent TCG fallback is the foundations inverted, rehearsed as a 3 a.m.
    page.
7. [Pick bridged or macvtap guest networking](../../questions/qemu-kvm/pick-bridged-or-macvtap.html)
    — Bridged versus macvtap carries the other surprise every operator meets
    exactly once.
8. [Use the QEMU monitor without desyncing libvirt](../../questions/qemu-kvm/use-the-qemu-monitor-without-desync.html)
    — The monitor ownership rule keeps every later procedure truthful with
    libvirt.
9. [Convert and rebase disk images with qemu-img](../../questions/qemu-kvm/convert-and-rebase-with-qemu-img.html)
    — The storage line runs image-first: convert and rebase with qemu-img.
10. [Model storage as libvirt pools and volumes](../../questions/qemu-kvm/model-storage-as-pools-and-volumes.html)
    — Pools and volumes manage what qemu-img just produced.
11. [Choose internal or external disk snapshots](../../questions/qemu-kvm/choose-internal-or-external-snapshots.html)
    — Snapshots are the point-in-time decision on top of managed storage.
12. [Operate memory ballooning under host pressure](../../questions/qemu-kvm/operate-memory-ballooning.html)
    — Ballooning is the memory lever pulled when host memory runs short.
13. [Decide when nested virtualization is worth it](../../questions/qemu-kvm/decide-on-nested-virtualization.html)
    — Nested virtualization returns to the TCG diagnosis's outer-hypervisor
    cause, priced this time.
14. [Run a live migration you can trust](../../questions/qemu-kvm/run-a-live-migration-you-trust.html)
    — The senior band opens with migration, which consumes CPU modes, shared
    storage, and downtime budgets in one motion.
15. [Choose a libvirt CPU mode for a fleet](../../questions/qemu-kvm/choose-a-libvirt-cpu-mode.html)
    — Migration silently assumes the target serves the exact CPU the guest
    booted with, so the fleet CPU-mode decision lands directly after it.
16. [Respect machine types when editing guests](../../questions/qemu-kvm/respect-machine-types.html)
    — Machine types obey the same rule as CPU modes: never silently change what
    the guest booted last time.
17. [Find where virtualization steals your performance](../../questions/qemu-kvm/find-virtualization-overhead.html)
    — The overhead investigation supplies the evidence discipline that settles
    the hypervisor-tax argument.
18. [Pin a latency-sensitive VM to NUMA and hugepages](../../questions/qemu-kvm/pin-a-vm-to-numa-and-hugepages.html)
    — NUMA pinning and hugepages buy latency by constraining placement.
19. [Design backups for running VMs](../../questions/qemu-kvm/design-running-vm-backups.html)
    — Backups for running VMs join the snapshot machinery with consistency.
20. [Secure libvirt and QEMU access on a shared host](../../questions/qemu-kvm/secure-libvirt-and-qemu-access.html)
    — The shared-host permissions model is the one the TCG diagnosis only hinted
    at.
21. [Design live migration for a fleet with mixed CPU generations](../../questions/qemu-kvm/migrate-a-fleet-with-mixed-cpus.html)
    — The staff band opens with fleet migration across mixed CPU generations.
22. [Set an honest overcommit policy for a VM fleet](../../questions/qemu-kvm/set-an-honest-overcommit-policy.html)
    — The overcommit policy makes fleet capacity a contract rather than a ratio.
23. [Choose the storage architecture for a VM fleet](../../questions/qemu-kvm/choose-fleet-vm-storage.html)
    — The fleet storage architecture is the storage line at fleet scale.
24. [Harden a multi-tenant KVM host](../../questions/qemu-kvm/harden-a-multi-tenant-kvm-host.html)
    — Hardening a shared host is isolation with adversaries, not just tenants.
25. [Govern QEMU upgrades across a fleet](../../questions/qemu-kvm/govern-qemu-upgrades.html)
    — A governed upgrade is machine types, migration, and hardening used as one
    maintenance motion: the whole course as a single change.
