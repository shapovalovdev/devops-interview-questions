---
title: Deploy a TLS certificate on a web server
theme: web-servers
difficulty: junior
type: scenario
tags: [tls, certificates, http, web-server, lfcs]
sources:
  - url: https://nginx.org/en/docs/http/configuring_https_servers.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Deploy a TLS certificate on a web server

What do you verify when deploying a renewed certificate for a public HTTPS site?

## Answer guide

- Install the certificate chain and matching private key in the virtual server selected for the site’s SNI name, validate configuration before reload, then make a fresh TLS connection using the public hostname. Confirm expiry, issuer chain, SAN coverage, protocol policy and that the new serial is served by every edge.
- Keep private-key access least-privileged and automate renewal with a monitored pre-expiry alert. A graceful reload can load a new certificate without dropping existing worker connections, but test the exact server implementation and deployment sequence.
- A valid leaf certificate alone is insufficient when intermediates are missing or a load balancer terminates TLS elsewhere. Never paste private keys into tickets or logs. Clock skew, incomplete rollout, wrong SNI and an old CDN configuration are common reasons a renewal appears inconsistent.

## References

- [NGINX: configuring HTTPS servers](https://nginx.org/en/docs/http/configuring_https_servers.html)
- Further reading (personal blog): [Scott Helme on TLS](https://scotthelme.co.uk/)

## What to learn next

- Official documentation: [Let's Encrypt documentation](https://letsencrypt.org/docs/)
- Manual or specification: [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- Maintainer or personal blog: [Scott Helme's blog](https://scotthelme.co.uk/)
- Technical blog: [Mozilla TLS configuration guidance](https://ssl-config.mozilla.org/)
- Hands-on guide: [Certbot instructions](https://certbot.eff.org/instructions)
