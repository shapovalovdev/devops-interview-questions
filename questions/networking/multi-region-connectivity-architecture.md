---
title: Design multi-region connectivity boundaries
theme: networking
difficulty: staff
type: scenario
tags: [networking, cloud, reliability, security]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc4632.html
    source_type: standard
    verified_on: 2026-08-06
---

# Design multi-region connectivity boundaries

How do you choose connectivity and addressing boundaries for multi-region services without creating a global failure domain?

## Answer guide

- Begin with latency, data-residency, recovery, and trust requirements for each flow. Decide which calls must cross regions and which data/services should be regional; routing every internal dependency through a central hub can create latency and hub blast radius.
- Allocate non-overlapping address space and publish route ownership. CIDR overlap prevents unambiguous routing and becomes costly once VPN, peering, Kubernetes, or acquisitions need connectivity.
- Use least-privilege connectivity: explicit service flows, workload identity, encryption where the threat model requires it, and independently enforceable regional boundaries. Private reachability alone is not authorization.
- Design failure behavior before connectivity: DNS/global traffic steering, data consistency expectation, circuit breaking, and operator control. Test regional isolation, partial control-plane failure, and recovery; active-active is not automatically safer if writes or shared dependencies cannot tolerate it.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [RFC 4632: CIDR strategy](https://www.rfc-editor.org/rfc/rfc4632.html)
- [AWS Well-Architected: Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
