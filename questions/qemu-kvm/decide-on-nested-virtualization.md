---
title: Decide when nested virtualization is worth it
theme: qemu-kvm
difficulty: middle
type: scenario
tags: [kvm, virtualization, performance, linux]
sources:
  - url: https://docs.kernel.org/virt/kvm/x86/index.html
    source_type: official-docs
    verified_on: 2026-08-15
  - url: https://docs.fedoraproject.org/en-US/quick-docs/enabling_nested_virtualization_in_kvm_guests/
    source_type: official-docs
    verified_on: 2026-08-15
---

# Decide when nested virtualization is worth it

Your CI team wants to run Kubernetes node VMs inside the VMs your platform already gives them, so they are asking for nested virtualization on the build agents. When is that request sound, and what should you check before granting it fleet-wide?

## Answer guide

- The mechanism: with the nested parameter enabled on the host's kvm_intel or kvm_amd module, the guest CPU gains vmx/svm, so a KVM hypervisor inside the guest can use hardware acceleration instead of falling back to TCG. Check and set the module parameter (/sys/module/kvm_intel/parameters/nested), and remember public cloud guests usually do not expose it at all.
- The request is sound when the inner virtualization is real infrastructure for a contained purpose — CI clusters that must exercise kubelet/container-runtime behaviour, training labs, testing hypervisor tooling — because the alternative (emulation or physical hosts) costs far more than the performance tax of L2 exits traversing two hypervisors.
- Grant it as a placement policy, not a checkbox: a dedicated host group with nested enabled, sized knowing inner VMs run measurably slower and timing-sensitive workloads degrade, and latency-critical production guests kept off those hosts. Live-migrating nested workloads between hosts with different nested settings is its own failure mode — treat it as unsupported in policy.
- The silent-failure trap to close: if nested is off, an inner KVM just falls back to software translation — nothing errors, tests merely time out and nobody knows why. Gate the CI agents on verifying /dev/kvm exists inside the guest image, so a mis-provisioned agent fails loudly at job start rather than mysteriously at hour three.

## References

- [Kernel KVM x86 documentation](https://docs.kernel.org/virt/kvm/x86/index.html)
- [Fedora quick docs — enabling nested virtualization in KVM guests](https://docs.fedoraproject.org/en-US/quick-docs/enabling_nested_virtualization_in_kvm_guests/)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [KVM project](https://www.linux-kvm.org/page/Main_Page)
- Manual or specification: [KVM API reference](https://docs.kernel.org/virt/kvm/api.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — KVM](https://wiki.archlinux.org/title/KVM)
