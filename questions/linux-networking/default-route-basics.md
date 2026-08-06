---
title: Explain a Linux default route
theme: linux-networking
difficulty: junior
type: theory
tags: [linux, networking]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip-route.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain a Linux default route

What is a default route on Linux, and when is it used?

## Answer guide

- A default route is the fallback route for destinations not matched by a more-specific prefix. Linux routing normally prefers the longest matching prefix, so a default route is not necessarily the path for every outbound connection.
- Inspect it with `ip route` and test a concrete choice using `ip route get <destination>`. The selected route includes an output interface, next hop where applicable, and often a selected source address.
- A valid-looking default route still requires a reachable next hop and an interface that can transmit. Multiple defaults, route metrics, VRFs, policy rules, and VPN-installed routes can deliberately change the result, so do not delete one during an incident without understanding its traffic class.

## References

- [ip-route(8): Linux routing-table management](https://man7.org/linux/man-pages/man8/ip-route.8.html)
- Further reading (blog): [Red Hat: configuring IP networking with ip commands](https://www.redhat.com/en/blog/configuring-ip-networking-with-ip-commands)
