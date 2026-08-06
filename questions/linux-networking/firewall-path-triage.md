---
title: Triage a Linux host firewall path
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, security, troubleshooting]
sources:
  - url: https://docs.kernel.org/networking/netfilter-sysctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a Linux host firewall path

An application listens locally but remote clients time out. How do you test the host firewall hypothesis safely?

## Answer guide

- First establish the intended tuple: protocol, source network, destination address, port, and interface. Confirm the listener and route, then inspect the active firewall manager and ruleset rather than assuming a distribution uses a particular legacy command.
- Capture on the ingress and egress interfaces while making a controlled test. This distinguishes packets never reaching the host, packets dropped before the application, and application replies blocked or routed incorrectly.
- Do not disable the firewall as a diagnostic shortcut on a shared host. Add a narrow, time-bounded test rule only through the configuration owner, log the result, and remove it. Stateful connection tracking, namespace boundaries, and cloud security controls can also be part of the path.

## References

- [Linux kernel: Netfilter sysctl variables](https://docs.kernel.org/networking/netfilter-sysctl.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
