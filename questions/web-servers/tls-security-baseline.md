---
title: Establish a TLS security baseline at the edge
theme: web-servers
difficulty: senior
type: scenario
tags: [tls, certificates, security, web-server]
sources:
  - url: https://nginx.org/en/docs/http/configuring_https_servers.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish a TLS security baseline at the edge

How do you set and continuously verify a TLS baseline for many web-server endpoints?

## Answer guide

- Define owned policy for protocol versions, cipher suites, certificate issuance, OCSP behavior, HSTS applicability, SNI routing and key protection. Encode it in a reusable edge configuration, inventory every hostname and automate certificate-expiry, handshake and configuration compliance checks from outside the deployment network.
- Keep the policy versioned with an exception process and test representative clients before removing legacy support. TLS configuration is deployment-specific: a CDN, ingress and origin can each terminate TLS, so determine which layer owns the browser-facing policy and which protects internal hops.
- Enabling HSTS prematurely can lock users out if all subdomains are not HTTPS-ready; removing old algorithms without client data can break essential integrations. A green internal probe does not prove public SNI or chain correctness. Treat private-key exposure and misissued certificates as incident scenarios with rehearsed rotation.

## References

- [NGINX HTTPS configuration](https://nginx.org/en/docs/http/configuring_https_servers.html)
- Further reading (personal blog): [Scott Helme's TLS writing](https://scotthelme.co.uk/)

## What to learn next

- Official documentation: [Mozilla SSL configuration generator](https://ssl-config.mozilla.org/)
- Manual or specification: [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- Maintainer or personal blog: [Scott Helme's blog](https://scotthelme.co.uk/)
- Technical blog: [Let's Encrypt documentation](https://letsencrypt.org/docs/)
- Hands-on guide: [SSL Labs server test](https://www.ssllabs.com/ssltest/)
