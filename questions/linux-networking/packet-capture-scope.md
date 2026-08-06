---
title: Capture Linux packets without losing diagnostic value
theme: linux-networking
difficulty: middle
type: scenario
tags: [linux, networking, troubleshooting, security, ckne]
sources:
  - url: https://www.tcpdump.org/manpages/tcpdump.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Capture Linux packets without losing diagnostic value

How do you take a useful packet capture during a production connectivity incident?

## Answer guide

- State the exact question first: for example, whether SYN packets arrive, whether DNS replies leave, or whether retransmissions occur. Select the relevant interface, narrow BPF filter, bounded duration, and packet limit so the capture answers that question without exhausting disk or exposing unrelated traffic.
- Capture at the right points in the path when possible: client-side, host ingress/egress, and proxy or load-balancer boundary. Record timestamps, interface names, route choice, and test identifiers so packets can be correlated with logs.
- Treat captures as sensitive data because payloads and credentials may be present. Restrict access, redact or encrypt stored evidence, and delete it under the incident-retention policy. A missing packet may result from an offload, namespace, mirror, or capture-point choice, so corroborate before concluding a network device dropped it.

## References

- [tcpdump(1): packet capture and BPF filtering](https://www.tcpdump.org/manpages/tcpdump.1.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
