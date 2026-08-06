---
title: Design production network segmentation
theme: security
difficulty: senior
type: scenario
tags: [security, networking, least-privilege, reliability]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: standard
    verified_on: 2026-08-06
---

# Design production network segmentation

How would you limit lateral movement between production services without breaking legitimate traffic?

## Answer guide

- Inventory real flows, define trust zones and service identities, then allow only required ingress, egress, ports, and protocols with default-deny boundaries where the platform supports them.
- Combine network policy with strong workload identity and application authorization; segment management paths and data stores separately from general application traffic.
- Observe denied flows before enforcement, roll out in stages, and make policy changes reviewable and reversible.
- IP-based segmentation alone cannot establish user or service intent, while an untested deny policy can cause an outage. Shared services such as DNS, telemetry, identity, and updates need explicit dependencies.

## References

- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [NIST SP 800-41: Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final)
