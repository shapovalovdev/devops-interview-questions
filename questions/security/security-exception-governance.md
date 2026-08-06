---
title: Govern security-control exceptions
theme: security
difficulty: staff
type: scenario
tags: [security, governance, delivery, reliability, kcsa]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
    source_type: standard
    verified_on: 2026-08-06
---

# Govern security-control exceptions

What makes a security exception process safe enough to unblock a production delivery?

## Answer guide

- Require a bounded request describing the control, asset, business need, threat, compensating controls, accountable owner, approval, and expiry date.
- Make exceptions visible in a reviewable register, monitor the compensating controls, and automatically re-open or revoke access at expiry unless explicitly renewed.
- Use the data to improve the platform: recurring exceptions indicate a missing supported pattern, not merely noncompliance.
- Permanent blanket waivers and undocumented verbal approvals silently become policy. Excessive approval friction creates shadow deployments, while a fast path without risk evidence creates unowned exposure.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST SP 800-53 Rev. 5: Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
