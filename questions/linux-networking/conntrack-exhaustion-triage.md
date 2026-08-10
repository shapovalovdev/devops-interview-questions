---
title: Triage Linux connection-tracking exhaustion
theme: linux-networking
difficulty: senior
type: troubleshooting
tags: [linux, networking, tcp, troubleshooting, monitoring]
sources:
  - url: https://docs.kernel.org/networking/nf_conntrack-sysctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage Linux connection-tracking exhaustion

How do you investigate suspected conntrack exhaustion without simply raising limits?

## Answer guide

- Establish whether the host actually uses Netfilter connection tracking for the affected path, then measure table count, limit, allocation failures, flow churn, and packet drops. Correlate the timing with NAT, firewall, load balancer, or workload changes.
- Identify the traffic shape: many short connections, asymmetric routing, long idle flows, scans, or an application retry loop have different remedies. Inspect representative entries and protocol timeouts while respecting the sensitivity of connection metadata.
- Raising capacity may consume memory and hide a leak or attack; reducing timeouts can terminate legitimate idle sessions. Combine a bounded capacity change with flow-control, application pooling, sane timeouts, telemetry, and a rollback threshold. Validate both new and existing connections after the change.

## References

- [Linux kernel: nf_conntrack sysctl settings](https://docs.kernel.org/networking/nf_conntrack-sysctl.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
