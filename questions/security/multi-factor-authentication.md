---
title: Choose multi-factor authentication for privileged access
theme: security
difficulty: junior
type: theory
tags: [security, iam, least-privilege]
sources:
  - url: https://pages.nist.gov/800-63-3/sp800-63b.html
    source_type: standard
    verified_on: 2026-08-06
---

# Choose multi-factor authentication for privileged access

Why should privileged access use MFA, and what must an implementation protect besides the login screen?

## Answer guide

- MFA requires distinct authentication factors, so a stolen password alone should not grant privileged access.
- Prefer phishing-resistant authenticators for high-impact roles, bind enrollment and recovery to strong identity proofing, and require MFA for both interactive administration and sensitive workflow changes.
- Protect sessions after login with secure cookies or tokens, expiry, reauthentication for risky actions, and revocation. Audit enrollment, recovery, and factor changes.
- Weak recovery channels, approval fatigue, shared administrator accounts, and unprotected API tokens can bypass MFA. Design an emergency path that is tightly authorized, monitored, and tested.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST SP 800-63B: Authentication and Lifecycle Management](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [OWASP: Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
