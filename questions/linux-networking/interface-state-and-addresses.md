---
title: Inspect Linux interface state and addresses
theme: linux-networking
difficulty: junior
type: troubleshooting
tags: [linux, networking, troubleshooting, lfcs]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Inspect Linux interface state and addresses

An application cannot reach its gateway after a host change. What Linux networking facts do you check first?

## Answer guide

- Start with `ip link show` and `ip address show`: identify the intended interface, its administrative and carrier state, and whether the expected IPv4 or IPv6 address and prefix are present. A link shown UP can still lack carrier, while an address can exist on the wrong interface.
- Use `ip route get <gateway-or-service>` rather than assuming the default route is selected. It shows the kernel's current routing decision; also check `ip route` for unexpected more-specific routes, duplicate addresses, or an incorrect source address.
- Separate temporary diagnosis from a persistent repair. `ip` changes can be overwritten by NetworkManager, systemd-networkd, cloud-init, or a configuration-management agent; establish the owning service before changing state. Do not bounce a production interface until a console or out-of-band recovery path exists.

## References

- [ip(8): inspect addresses, links, routes, and neighbours](https://man7.org/linux/man-pages/man8/ip.8.html)
- Further reading (blog): [Red Hat: Linux network troubleshooting commands](https://www.redhat.com/en/blog/linux-network-troubleshooting-commands)
