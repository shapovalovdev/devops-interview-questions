---
title: Prevent secrets from entering logs
theme: logging
difficulty: junior
type: scenario
tags: [logging, security, incident-response, troubleshooting]
sources:
  - url: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent secrets from entering logs

How would you keep credentials and personal data out of application logs?

## Answer guide

- Establish an allowlist of fields that may be logged for each event and make logging helpers redact known secret keys, authorization headers, cookies, tokens, and sensitive request bodies before serialization. Preventing emission is safer than relying only on a downstream processor.
- Apply defense in depth in collectors and backends: scan or transform common patterns, limit who can query raw data, encrypt transport and storage, and set retention by data classification. These controls reduce blast radius but cannot reliably reconstruct every secret after it was indexed.
- Test redaction with representative failures and review logs after library or schema changes. If a secret is emitted, rotate it, restrict access, assess replicas and backups, and document the incident; deleting one visible record does not guarantee downstream copies disappeared.

## References

- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Further reading (blog): [GitGuardian engineering blog](https://blog.gitguardian.com/)

## What to learn next

- Official documentation: [OWASP logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- Manual or specification: [NIST SP 800-92 Rev. 1 (initial public draft) — guide to computer security log management](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [GitGuardian engineering blog](https://blog.gitguardian.com/)
- Hands-on guide: [GitHub secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
