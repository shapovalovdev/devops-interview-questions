---
title: Set web security headers deliberately
theme: security
difficulty: middle
type: scenario
tags: [security, http, web-server]
sources:
  - url: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set web security headers deliberately

Which security headers would you evaluate for a web application, and why must they be tested with the application?

## Answer guide

- Use headers appropriate to the application, such as a restrictive Content Security Policy, transport-security policy after HTTPS is correct, frame-embedding controls, and safe cookie attributes.
- These controls constrain browser behavior; they complement server authorization, input handling, and TLS rather than replacing them.
- Start CSP in report-only mode when needed, inventory legitimate resource origins, and test login, payments, embeds, APIs, and error pages before enforcement.
- A broad wildcard policy offers little protection; an incorrect policy can block critical scripts or lock users out. HSTS can make a mistaken HTTPS configuration persistent, so rollout and rollback require care.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [OWASP: HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [MDN: HTTP headers](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
