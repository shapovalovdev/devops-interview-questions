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

Open with the three-boxes picture — "Split QEMU's job from KVM's job", then
"What /dev/kvm exposes to QEMU" — because every later answer assumes you know
which layer owns what: the kernel runs guest code, QEMU builds the guest's
world, libvirt holds the domain's XML. "Why virtio beats emulated devices"
comes third, since its shared-ring mechanism is half the performance
vocabulary this Theme speaks, and "Read a libvirt domain's states" supplies
the operating grammar — what `virsh list` is actually telling you before you
act on it. Close the tier with "Choose raw or qcow2 for a disk image", the
first decision a new domain forces and the base every storage Question builds
on. "Diagnose a guest silently running under TCG" lands immediately after the
foundations because it is their inversion: the near-native story collapses
the moment /dev/kvm is missing, and working that incident is the foundations
rehearsed as a 3 a.m. page. "Pick bridged or macvtap guest networking"
follows with the other surprise every operator meets exactly once — the host
that cannot reach its own macvtap guests.

Take the guest-contract pair together — "Choose a libvirt CPU mode for a
fleet" and "Respect machine types when editing guests" — because both are the
same rule (do not silently change what the guest booted last time) and their
payoff arrives with migration. "Use the QEMU monitor without desyncing
libvirt" states the ownership rule that keeps every later procedure truthful.
The storage line then runs in dependency order — "Convert and rebase disk
images with qemu-img", "Model storage as libvirt pools and volumes", "Choose
internal or external disk snapshots" — image, then management, then
point-in-time. "Operate memory ballooning under host pressure" is the memory
lever pulled when host memory runs short, and "Decide when nested
virtualization is worth it" closes the middle tier by returning to the TCG
diagnosis's outer-hypervisor cause, this time with a cost model attached.

The senior band composes those levers into procedures. "Run a live migration
you can trust" first, because it consumes CPU modes, shared storage, and
downtime budgets in one motion; then "Find where virtualization steals your
performance" for the evidence discipline that settles the hypervisor-tax
argument; "Pin a latency-sensitive VM to NUMA and hugepages" for
topology-aware placement; "Design backups for running VMs" to join snapshots
with consistency; and "Secure libvirt and QEMU access on a shared host" for
the permissions model the TCG diagnosis only hinted at. Finish with the staff
Questions, which are the same mechanisms priced at fleet scale — "Design live
migration for a fleet with mixed CPU generations", "Set an honest overcommit
policy for a VM fleet", "Choose the storage architecture for a VM fleet",
"Harden a multi-tenant KVM host" — and let "Govern QEMU upgrades across a
fleet" close the Theme, because a governed upgrade is machine types,
migration, and hardening used as one maintenance motion: the whole course
rehearsed as a single change.
