---
title: Diagnose a TLS handshake failure safely
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, tls, security, networking, certificates]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8446
    source_type: standard
    verified_on: 2026-08-06
---
# Diagnose a TLS handshake failure safely
## Answer guide
- Capture the client error, server-side handshake log, hostname, protocol version, cipher suite, certificate chain, and time. Distinguish TCP reachability from TLS negotiation and HTTP authorization.
- Validate SNI routing, certificate validity and chain, trusted roots, clock, key usage, client-certificate requirements, and supported versions. Compare a failing client with a known-good client without exporting private keys.
- Renew or deploy the correct certificate through the controlled path and test hostname validation end to end. Never “fix” production by disabling certificate verification, accepting expired certificates, or lowering protocol security globally.
## References
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [Mozilla Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS)
- Further reading (blog): [Scott Helme — TLS](https://scotthelme.co.uk/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)
- Hands-on guide: [Let’s Encrypt documentation](https://letsencrypt.org/docs/)
- Maintainer or personal blog: [Scott Helme](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare TLS](https://blog.cloudflare.com/tag/tls/)
