---
title: "Live-Migrate a libvirt Domain and Measure the Real Downtime"
theme: "qemu-kvm"
difficulty: "senior"
question_ref: "qemu-kvm/run-a-live-migration-you-trust.md"
tags: [kvm, libvirt, live-migration, migration, networking, performance, troubleshooting]
why: "Pre-copy live migration looks like one command until a maintenance window depends on it. This lab builds the two-host preconditions yourself — shared storage, a writable domain, a budgeted migration — then forces the failure modes (uncontrolled bandwidth, a runaway dirty rate) and measures actual cutover downtime with ping, so you learn why convergence settings exist and what a trusted migration window really contains."
checklist:
  - "Provision two libvirt hosts (kvm1, kvm2) with nested virtualization enabled and verify each reports virt-type kvm via virt-host-validate qemu-kvm."
  - "Export shared guest storage from a helper with NFS, mount it at /var/lib/libvirt/images on both hosts, and confirm both hosts see the same qcow2 volume."
  - "Define and start a guest on kvm1 whose disk path resolves identically on both hosts, with virtio devices and a workload dirtying memory (e.g. a loop writing to tmpfs)."
  - "Baseline the guest: run a continuous ping from an external machine and a curl loop against a service inside the guest, logging timestamps."
  - "Migrate with a deliberate bandwidth cap and observe iterative pre-copy passes with virsh domjobinfo until downtime is entered and the job completes on kvm2."
  - "Break convergence on purpose: raise the dirtying workload, start a migration without auto-converge, and watch remaining dirty bytes stall instead of shrinking."
  - "Re-run the stalled migration with --auto-converge --comp-effects xbzrle and a --bandwidth cap, and compare convergence time against the uncontrolled run."
  - "Measure cutover downtime from the ping log and reconcile it with virsh domjobinfo downtime; confirm the guest's service answered every request or note which were lost."
  - "Drill cancellation: start a migration, virsh domjobabort it, and verify the guest keeps running on kvm1 as the authoritative copy."
  - "Fail over back to kvm1 to restore the starting state and record your measured downtime, transfer time, and dirty rate as the numbers you would quote in a maintenance plan."
---

# Lab: Live-Migrate a Domain and Measure the Downtime

## Goal

Evacuate a running guest from `kvm1` to `kvm2` with zero manual intervention inside the guest, watch pre-copy converge, force it to stall, and walk away with measured downtime numbers instead of a feeling that it "seemed fine". The lab follows the trust model from the Question [Run a live migration you can trust](https://github.com/shapovalovdev/devops-interview-questions/blob/main/questions/qemu-kvm/run-a-live-migration-you-trust.md): a migration you have not measured and never failed on purpose is a hypothesis, not a runbook.

## Topology

Three machines you can reach over SSH:

| Host | Role | Notes |
| ---- | ---- | ----- |
| `kvm1`, `kvm2` | libvirt + QEMU/KVM hypervisors | Identical distro and package versions; nested virtualization enabled if these are themselves VMs |
| `store` | NFS server for shared guest storage | Any machine with a few GB free; can be `kvm1`'s host or your workstation |
| your workstation | external observer | Runs the ping and curl probes that measure downtime |

If `kvm1`/`kvm2` are cloud or workstation VMs, enable nested virtualization first (on a KVM host: `virt-xml kvm1 --edit --cpu host-passthrough` or set the CPU mode accordingly). Verify on each hypervisor:

```bash
sudo virt-host-validate qemu-kvm
```

You want `virt-type: kvm` and no storage/networking warnings you cannot explain. If KVM acceleration is unavailable the lab still runs on TCG emulation, but convergence numbers will not resemble production.

## Step 1 — Shared storage both hosts see identically

Pre-copy migration moves RAM, not disks, unless you explicitly copy storage. Give both hosts the same view of the disk:

```bash
# on store
sudo mkdir -p /srv/libvirt/images
sudo chown libvirt-qemu:kvm /srv/libvirt/images   # naming varies by distro
echo "/srv/libvirt/images *(rw,sync,no_subtree_check,fsid=42)" | sudo tee -a /etc/exports
sudo exportfs -ra

# on kvm1 and kvm2
sudo mkdir -p /var/lib/libvirt/images
sudo mount store:/srv/libvirt/images /var/lib/libvirt/images
sudo qemu-img create -f qcow2 /var/lib/libvirt/images/lab-guest.qcow2 10G
```

Confirm the identity of the volume from both hosts (`ls -i`, or write a marker file next to it and read it from the other host). A migration that fails with "cannot find disk" is almost always two hosts resolving the same path to different storage. The libvirt [migration documentation](https://libvirt.org/migration.html) calls this precondition shared storage; you have just built the cheapest version of it.

## Step 2 — Guest with an honest dirty rate

Install a minimal guest once (Debian/Alma/Fedora netinst is fine) using `virt-install` with a virtio disk and virtio NIC on the path above:

```bash
sudo virt-install --name lab-guest --memory 1024 --vcpus 1 \
  --disk path=/var/lib/libvirt/images/lab-guest.qcow2,bus=virtio,format=qcow2 \
  --network network=default,model=virtio \
  --os-variant detect=on,name=generic --console pty,target_type=serial --noautoconsole
```

Inside the guest, start a memory-dirtying workload so pre-copy has something to chase:

```bash
# in the guest: rewrite a tmpfs file forever
while true; do dd if=/dev/urandom of=/dev/shm/churn bs=1M count=256 2>/dev/null; done &
```

Run a small HTTP service (`python3 -m http.server 8000`) so the observer has something meaningful to probe, not just ICMP.

## Step 3 — Baseline the observer

From your workstation, log continuously through the whole lab:

```bash
ping -D -i 0.2 <guest-ip> | tee ping-baseline.log
while true; do curl -s -o /dev/null -w '%{s} %{time_total}\n' http://<guest-ip>:8000/ ; sleep 0.2; done | tee curl-baseline.log
```

`ping -D` prints ICMP timestamps; this log is your downtime measurement instrument. Everything `virsh` reports must be reconcilable against it.

## Step 4 — First migration, budgeted

```bash
# on kvm1
sudo virsh migrate lab-guest qemu+ssh://kvm2/system --live \
  --persistent --undefinesource --bandwidth 100
watch -n1 'sudo virsh domjobinfo lab-guest'
```

Watch `Memory remaining` shrink in passes while `Memory processed` climbs — that is iterative pre-copy with KVM dirty-page logging feeding each pass. When the dirty set fits inside the downtime budget, the guest pauses, the final delta and device state transfer, and it resumes on `kvm2`. After the job completes, inspect `downtime` in the final `virsh domjobinfo` output and match it against gaps in `ping-baseline.log`.

## Step 5 — Break convergence on purpose

Migrate back to `kvm1`, then raise the churn (bigger `count`, or several loops). Start a migration with no convergence aids and a generous bandwidth cap, and watch `Memory remaining` plateau: the guest dirties pages faster than the wire drains them, so the source never reaches a cutover-able dirty set. Kill the churn loop, watch convergence snap forward, then cancel cleanly:

```bash
sudo virsh domjobabort lab-guest
sudo virsh list --all   # guest still running on the source: source stays authoritative until cutover
```

This is the drill that makes auto-converge and xbzrle settings non-optional: you have now personally watched the failure mode the [libvirt migration guide](https://libvirt.org/migration.html) warns about, not read about it.

## Step 6 — Migration you would put in a runbook

Re-run with the convergence trio set deliberately:

```bash
sudo virsh migrate lab-guest qemu+ssh://kvm2/system --live \
  --persistent --undefinesource \
  --bandwidth 100 --auto-converge --comp-methods xbzrle --comp-effects xbzrle
```

Compare convergence time against Step 5's stalled run, then measure real downtime from the ping log and reconcile with `virsh domjobinfo`. Verify with post-migration health checks — the curl log and `virsh domstate` on both hosts — because "virsh says running" is not the same as "the service answered". The [virsh manual](https://libvirt.org/manpages/virsh.html) documents every flag used here; the [QEMU QMP reference](https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html) is where the underlying migration commands live when you outgrow virsh.

## What to record

A migration you trust is a migration with numbers attached. Finish with:

- transfer time and total bytes for the budgeted run;
- measured ping-gap downtime vs `virsh domjobinfo` downtime;
- the dirty rate at which convergence stalled without auto-converge;
- which curl requests, if any, were lost at cutover.

Those four numbers are the difference between a runbook and a hope. When you can produce them on demand, revisit the Question [Run a live migration you can trust](https://github.com/shapovalovdev/devops-interview-questions/blob/main/questions/qemu-kvm/run-a-live-migration-you-trust.md) and check whether your answers changed.
