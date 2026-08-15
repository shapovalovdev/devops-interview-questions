---
title: Use the QEMU monitor without desyncing libvirt
theme: qemu-kvm
difficulty: middle
type: theory
tags: [qemu, libvirt, debugging, kernel]
sources:
  - url: https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://libvirt.org/drvqemu.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Use the QEMU monitor without desyncing libvirt

You can reach a running QEMU's monitor directly — or through virsh qemu-monitor-command. Explain what the monitor is for, why it is dangerous under libvirt, and what to do instead when libvirt has a first-class operation.

## Answer guide

- QEMU speaks two control protocols: the human monitor (HMP), an interactive console built for debugging, and QMP, the JSON machine protocol libvirt itself uses. The monitor can hotplug devices, dump memory, inspect registers, and drive live block jobs — it is the control surface of the process, not just a status window.
- The hazard is ownership: libvirt tracks domain state as XML plus what it did through QMP. A device you attach directly through the monitor exists in the running QEMU but not in libvirt's model, so the next libvirt operation — migrate, snapshot, dump, config edit — reasons about a machine that is not the one actually running. The mismatch surfaces later as a migration failure or a device that vanishes on the next start.
- Prefer the wrapped path whenever one exists: virsh blockcopy, blockcommit, attach-device, and friends drive the same QMP machinery but keep libvirt's state truthful. Reserve raw monitor work for read-only inspection (info registers, info block, memory dumps during crash analysis) and for last-resort intervention on a domain you have already decided to restart.
- Keep the qemu-guest-agent out of this confusion: it is a service inside the guest, not a path into QEMU's control plane, and it exists so the host can request things only the guest can do — freeze filesystems, report memory stats. Enabling the agent channel is an operations win with none of the desync risk.

## References

- [QEMU QMP reference](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html)
- [libvirt QEMU driver](https://libvirt.org/drvqemu.html)
- Further reading (blog): [ServeTheHome](https://www.servethehome.com/)

## What to learn next

- Official documentation: [libvirt QEMU driver](https://libvirt.org/drvqemu.html)
- Manual or specification: [QEMU QMP reference](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Arch Wiki — QEMU](https://wiki.archlinux.org/title/QEMU)
