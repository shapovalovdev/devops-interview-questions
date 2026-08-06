---
title: Debug a TLS handshake failure
theme: networking
difficulty: middle
type: troubleshooting
tags: [tls, http, networking, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8446.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc6066.html
    source_type: standard
    verified_on: 2026-08-06
---

# Debug a TLS handshake failure

A client cannot establish HTTPS with a service. Which parts of the TLS handshake do you inspect first?

## Answer guide

- Capture the client and server error first, then establish whether TCP connects. A TCP refusal, timeout, or proxy error is below TLS and needs a different investigation.
- For a reached TLS endpoint, verify the requested hostname against the certificate subject alternative names, the certificate validity interval, the chain supplied by the server, and the client's configured trust store. A certificate may be valid yet be wrong for the hostname or omit an intermediate.
- Compare the ClientHello and server choice: protocol version, supported cipher suites/signature algorithms, and (where applicable) ALPN. TLS 1.3 has a different cipher-suite model from TLS 1.2, so changing a single cipher setting can have version-specific effects.
- Check SNI: a shared IP or reverse proxy can serve the wrong certificate or virtual host if the client does not send the intended server name. Avoid disabling verification as a fix; it hides an identity failure and creates an interception risk.

## References

- [RFC 8446: The Transport Layer Security Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446.html)
- [RFC 6066: TLS extensions, including Server Name Indication](https://www.rfc-editor.org/rfc/rfc6066.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
