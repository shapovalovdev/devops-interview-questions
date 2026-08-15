---
title: Diagnose a guest silently running under TCG
theme: qemu-kvm
difficulty: middle
type: troubleshooting
tags: [kvm, qemu, troubleshooting, performance]
sources:
  - url: https://www.qemu.org/docs/master/system/invocation.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://docs.kernel.org/virt/kvm/index.html
    source_type: official-docs
    verified_on: 2026-08-15
---

# Diagnose a guest silently running under TCG

A newly provisioned VM compiles for minutes where its siblings take seconds. Its domain log contains a warning about the KVM accelerator not being usable. Walk the diagnosis.

## Answer guide

- Confirm the suspicion before touching anything: a TCG guest shows its QEMU process burning a full host core per busy vCPU, with the guest's own kernel time near zero; check that the QEMU process does not hold /dev/kvm open, and read the domain log, which states the accelerator fallback explicitly.
- Work the causes in order of frequency. Virtualization disabled in firmware — no vmx or svm flag in /proc/cpuinfo, so kvm_intel or kvm_amd fails to load with a dmesg message. Modules not loaded at all — fix with modprobe and a modules-load entry. This host is itself a VM on a hypervisor that does not expose nested virtualization, so /dev/kvm exists in the outer world but not here.
- Permissions are the sneaky one: the node exists, the modules are loaded, but libvirt spawns QEMU as its unprivileged service user, which cannot open /dev/kvm — the same silent fallback, this time caused by group membership or a udev rule rather than hardware.
- Make it a provisioning gate rather than a debugging session: run virt-host-validate on every new host, alert on any domain log line mentioning an accelerator fallback, and treat a TCG VM as a misconfiguration, because nobody who asked for that VM agreed to one-tenth of a computer.

## References

- [QEMU invocation and accelerator selection](https://www.qemu.org/docs/master/system/invocation.html)
- [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [Kernel virtualization (KVM) documentation](https://docs.kernel.org/virt/kvm/index.html)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
