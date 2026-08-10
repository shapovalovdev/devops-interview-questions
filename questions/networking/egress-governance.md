---
title: Govern production network egress
theme: networking
difficulty: staff
type: scenario
tags: [networking, security, observability, least-privilege]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc1918.html
    source_type: standard
    verified_on: 2026-08-06
---

# Govern production network egress

How would you let workloads reach necessary external services while controlling data-exfiltration and supply-chain risk?

## Answer guide

- Inventory and classify outbound dependencies by workload, destination, protocol, owner, data sensitivity, and business criticality. An allow-list is useful only when it is maintained, observable, and supports the destinations' real addressing and TLS behaviour.
- Enforce egress at a boundary that can identify the workload and log decisions; combine network policy with workload identity, DNS controls where appropriate, proxy/TLS policy, and application authorization. Network location is not sufficient trust under zero-trust principles.
- Provide a governed path for package registries, artifact stores, SaaS APIs, time/DNS, certificate validation, and incident access. A blanket deny without these dependencies creates shadow bypasses and unsafe emergency exceptions.
- Track denied traffic, policy drift, byte volume, new destinations, and exceptions with expiry/owner. Evaluate trade-offs: TLS interception can increase visibility but changes trust, privacy, and operational failure modes.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [RFC 1918: Private addressing boundaries](https://www.rfc-editor.org/rfc/rfc1918.html)
- [CISA: Zero Trust Maturity Model](https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
