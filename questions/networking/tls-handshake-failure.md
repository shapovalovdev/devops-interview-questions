---
title: Debug a TLS handshake failure
theme: networking
difficulty: middle
type: troubleshooting
tags: [tls, http, networking, troubleshooting]
---

# Debug a TLS handshake failure

A client cannot establish HTTPS with a service. Which parts of the TLS handshake do you inspect first?

## Answer guide

- Verify hostname, certificate validity, chain, and trusted issuer.
- Compare supported protocol versions and cipher suites between client and server.
- Check SNI routing and capture the exact handshake error before changing configuration.
