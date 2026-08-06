---
title: Design zero-trust service access
theme: security
difficulty: senior
type: scenario
tags: [security, iam, networking, least-privilege]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/207/a/final
    source_type: standard
    verified_on: 2026-08-06
---

# Design zero-trust service access

How would you replace network-location trust between services with explicit access decisions?

## Answer guide

- Give each service a verifiable workload identity, authenticate peers, and authorize each requested resource/action using identity and contextual policy rather than source subnet alone.
- Enforce policies at practical points such as gateways, proxies, and application authorization; rotate credentials and collect decision telemetry.
- Roll out incrementally by mapping flows, starting with observability and high-value paths, then denying unneeded access. Keep availability objectives and emergency access explicit.
- Mutual TLS without authorization still permits overbroad access; identity systems can become a shared dependency. Design for policy mistakes, identity outages, and revocation propagation.

## References

- [NIST SP 800-207A: Zero Trust for Cloud-Native Applications](https://csrc.nist.gov/pubs/sp/800/207/a/final)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
