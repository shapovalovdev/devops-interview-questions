---
title: Design useful security event logging
theme: security
difficulty: junior
type: theory
tags: [security, logging, observability]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/92/final
    source_type: standard
    verified_on: 2026-08-06
---

# Design useful security event logging

Which events should a service log for security investigations, and what must never be logged?

## Answer guide

- Log security-relevant outcomes such as authentication, authorization denials, administrative changes, credential use, and high-value data actions with time, actor, target, request correlation, and result.
- Send structured events to protected, centrally retained storage so responders can correlate systems and detect tampering or gaps.
- Minimize collection and redact passwords, tokens, private keys, and unnecessary personal data; access to logs is itself privileged.
- Logs with unsynchronized clocks, mutable local-only storage, or no ownership are poor evidence. Test alerting and retrieval during exercises rather than assuming collection equals detection.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
- [OWASP: Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
