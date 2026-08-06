---
title: Build safe network change delivery
theme: networking
difficulty: staff
type: scenario
tags: [networking, deployment, automation, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1812.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://sre.google/sre-book/release-engineering/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build safe network change delivery

What delivery system would you use for high-impact routing, firewall, or DNS changes?

## Answer guide

- Treat intended network state as reviewed, versioned configuration with an owner, peer review, and an auditable change record. Validate syntax plus semantics: route overlap, prefix limits, policy conflicts, DNS delegation, and expected reachability.
- Roll out in bounded failure domains with pre-change baselines and machine-checkable success criteria. Use canaries, staged route preference, or small target cohorts where the technology permits; a simultaneous global update removes the ability to learn safely.
- Predefine rollback and its dependencies. Rollback must be executable even when the management network or control plane is impaired, and it must account for cache/state propagation such as DNS TTL and connection draining.
- Measure user and control-plane outcomes during and after the change, then automate recurring checks. Change gates should reduce demonstrable risk, not become a ritual that encourages emergency bypasses.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 1812: Router requirements](https://www.rfc-editor.org/rfc/rfc1812.html)
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/)
- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
