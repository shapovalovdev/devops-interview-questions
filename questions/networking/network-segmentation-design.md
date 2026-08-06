---
title: Design network segmentation for a service
theme: networking
difficulty: senior
type: scenario
tags: [networking, security, least-privilege, reliability]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design network segmentation for a service

How do you segment a new production service without making its network topology the only security control?

## Answer guide

- Start from concrete flows: caller identity, destination, protocol/port, data classification, and operational dependencies (DNS, time, telemetry, package/artifact access). Default-deny boundaries then allow only required, observable paths.
- Segment by trust and blast radius—such as public ingress, application, data, and management planes—while using workload identity and application authorization for sensitive operations. NIST zero-trust guidance explicitly avoids granting implicit trust solely because of network location.
- Make policy bidirectional and test return paths, DNS, health checks, upgrade paths, and emergency access. A rule that permits the request but blocks a dependency or response can fail intermittently.
- Treat rules as versioned code with owner, expiry/review, logging, and rollback. Excessively coarse shared subnets simplify routing but enlarge lateral-movement and outage blast radius.

## References

- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA: Zero Trust Maturity Model](https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model)
