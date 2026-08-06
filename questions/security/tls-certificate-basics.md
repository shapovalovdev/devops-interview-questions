---
title: Explain TLS certificate validation
theme: security
difficulty: junior
type: theory
tags: [security, tls, networking]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc5280
    source_type: standard
    verified_on: 2026-08-06
---

# Explain TLS certificate validation

What must a client validate before trusting a TLS server certificate?

## Answer guide

- Build a chain from the presented certificate to a configured trust anchor and verify signatures, validity intervals, key usage constraints, and the requested server name.
- TLS provides an authenticated protected channel only if the client actually validates the peer; blindly accepting certificates defeats that property.
- Automate renewal and alert before expiry. Keep trust-store changes controlled because adding a trust anchor expands who can authenticate servers.
- Expired certificates, incorrect names, missing intermediates, clock skew, and disabled verification commonly cause outages or insecure workarounds. Do not "fix" a failure by disabling validation.

## References

- [RFC 5280: Internet X.509 Public Key Infrastructure Certificate Profile](https://www.rfc-editor.org/rfc/rfc5280)
- [OWASP: Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
