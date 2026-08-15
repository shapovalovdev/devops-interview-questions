# QEMU/KVM related materials

Use these resources to connect the virtualization Questions to the primary
documentation of the three projects they cover: QEMU's own manual, libvirt's
driver and format references, and the kernel's KVM documentation.

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)

## Suggested study order

Start with the split of responsibilities — what /dev/kvm exposes, what QEMU
emulates, what libvirt manages — because every later answer assumes those three
layers. Read domain states and virtio next, since one describes how a VM is
operated and the other why it performs, then the raw-versus-qcow2 choice that
every disk decision builds on. Take the middle tier as operations: the silent
TCG fallback and macvtap's host blind spot are the two failures that surprise
everyone once, snapshots and ballooning are the levers pulled under pressure,
and CPU modes, qemu-img, storage pools, the QEMU monitor, machine types, and
nested virtualization each prevent a specific production mistake. The senior
band is joined practice: live migration, performance attribution, NUMA and
hugepage pinning, running-VM backups, and the permissions model all compose
those levers into procedures. Finish with the staff design Questions — fleet
migration strategy, QEMU upgrade governance, multi-tenant hardening,
overcommit policy, and storage architecture — because they are the same
mechanisms priced at fleet scale.
