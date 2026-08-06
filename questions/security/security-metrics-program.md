---
title: Define security metrics that drive engineering decisions
theme: security
difficulty: staff
type: scenario
tags: [security, governance, monitoring, platform-engineering]
sources:
  - url: https://www.nist.gov/cyberframework
    source_type: standard
    verified_on: 2026-08-06
---

# Define security metrics that drive engineering decisions

Which metrics should a staff engineer use to improve a security platform without encouraging misleading behavior?

## Answer guide

- Measure outcomes and coverage: critical-asset inventory completeness, control adoption, exposed known-exploited vulnerabilities, mean time to remediate by risk, credential rotation coverage, and restore-test success.
- Segment metrics by service tier and ownership, publish trends with definitions, and pair leading indicators with incident and audit evidence.
- Use metrics to prioritize investment and remove friction, not to rank teams. Audit data quality and document exclusions.
- Raw finding counts reward suppression and ignore exploitability; a single averaged score can conceal unacceptable high-risk assets. Metrics without a decision owner become dashboards rather than control loops.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
