---
title: Define WAF and application-security boundaries
theme: web-servers
difficulty: senior
type: scenario
tags: [security, web-server, http, governance]
sources:
  - url: https://owasp.org/www-project-web-security-testing-guide/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define WAF and application-security boundaries

What can a web application firewall at the edge reduce, and what security controls remain application responsibilities?

## Answer guide

- Use the edge for protocol normalization, known attack-pattern detection, request-size limits, rate controls, bot or abuse signals and virtual patching, with monitored rules in detection mode before enforcement where safe. Keep ownership for rules, exceptions, updates, logging and incident response explicit.
- The application still owns authentication, authorization, tenant isolation, business validation, output encoding, secrets and secure data access. Test the composed request path, including CDN, WAF, proxy and application parsing, because inconsistent normalization can create bypasses.
- A WAF cannot make an insecure authorization decision safe, and blocking rules can deny legitimate traffic during a release. Logging sensitive payloads to investigate a rule can create a new exposure. Treat bypass headers, direct-origin access and stale signatures as threat-model inputs, not afterthoughts.

## References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- Further reading (personal blog): [Troy Hunt's security blog](https://www.troyhunt.com/)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [Cloudflare WAF documentation](https://developers.cloudflare.com/waf/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
