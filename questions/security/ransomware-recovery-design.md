---
title: Design recoverable backups for ransomware
theme: security
difficulty: senior
type: scenario
tags: [security, storage, incident-response, reliability]
sources:
  - url: https://www.cisa.gov/stopransomware/ransomware-guide
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design recoverable backups for ransomware

What properties must a backup and recovery design have to support a ransomware incident?

## Answer guide

- Keep versioned backups separated from normal production credentials and administration, encrypt them, restrict deletion, and retain copies that an attacker in the primary environment cannot alter.
- Define recovery objectives, prioritize critical systems and identities, and regularly restore representative data into an isolated environment to measure actual recovery time and integrity.
- Protect backup metadata, audit destructive actions, and maintain an emergency recovery process with named owners.
- A successful backup job does not prove recovery; compromised credentials can encrypt or delete online backups too. Untested restores, missing dependencies, and restoring into an infected environment can extend the incident.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide)
- [NIST SP 800-34: Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/final)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
