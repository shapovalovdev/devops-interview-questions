---
title: Pick bridged or macvtap guest networking
theme: qemu-kvm
difficulty: middle
type: theory
tags: [libvirt, networking, kvm, linux]
sources:
  - url: https://libvirt.org/formatdomain.html#elementsNICS
    source_type: official-docs
    verified_on: 2026-08-15
---

# Pick bridged or macvtap guest networking

Two hosts run identical guests: one attaches them to a Linux bridge, the other uses direct macvtap attachment onto the physical NIC. A script on the host needs to talk to the guests over the network. Which setup wins, and why does the faster-looking option have a hole?

## Answer guide

- With a Linux bridge, the physical NIC, the host's own IP stack, and every guest's tap device join one L2 switch. Guests are peers of the host: host-to-guest and guest-to-guest traffic on that bridge works like any other LAN, at the cost of configuring bridging on the host and one more hop of kernel forwarding.
- macvtap skips the bridge: each guest gets a tap endpoint bound straight onto the parent physical interface, which is simpler to deploy and avoids a layer of switching — but the host itself cannot reach its own guests through that parent interface, because frames the host sends to a guest's MAC leave via the NIC instead of looping back. The host is, by construction, off that network segment.
- Guest-to-guest on one host in macvtap mode has the same blind spot in bridge/vepa modes unless the physical switch hairpins the frames back, which most access ports refuse; private mode isolates guests from each other entirely.
- Decision rule: if anything on the host must talk to the guests, take the bridge or add a separate host-side macvtap interface for management traffic. If guests only serve the outside world and you want minimum moving parts, macvtap is the cleaner trade. Neither choice should be made silently — the failure surfaces later as "the backup agent cannot reach the database VM".

## References

- [libvirt domain XML — network interfaces](https://libvirt.org/formatdomain.html#elementsNICS)
- Further reading (blog): [Red Hat blog](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [libvirt documentation](https://libvirt.org/docs.html)
- Manual or specification: [libvirt API reference](https://libvirt.org/html/index.html)
- Maintainer or personal blog: [Daniel P. Berrangé — virtualization engineering](https://www.berrange.com/)
- Technical blog: [Red Hat blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Wiki — libvirt](https://wiki.archlinux.org/title/Libvirt)
