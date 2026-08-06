---
title: Preserve client identity behind proxies
theme: web-servers
difficulty: middle
type: troubleshooting
tags: [http, nginx, security, logging]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_realip_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Preserve client identity behind proxies

How do you log and rate-limit the real client safely when a CDN or load balancer is in front of the web server?

## Answer guide

- Define the trusted proxy network boundary and configure the server to accept forwarded client information only from those addresses. Preserve the proxy chain and use the normalized client address consistently for access logs, abuse controls and application context.
- Prefer a documented header convention or the PROXY protocol where every hop supports it. Test direct access, IPv4 and IPv6, multiple forwarding hops, and spoofed headers. Keep the transport peer address separately so an incident can distinguish the CDN from the claimed client.
- Trusting `X-Forwarded-For` from arbitrary clients lets attackers choose their logged identity and bypass per-client limits. Conversely, forgetting a new proxy range can rate-limit an entire edge. Header parsing and “first versus last address” semantics must match the actual proxy append policy.

## References

- [NGINX real IP module](https://nginx.org/en/docs/http/ngx_http_realip_module.html)
- Further reading (personal blog): [Scott Helme's web-security writing](https://scotthelme.co.uk/)

## What to learn next

- Official documentation: [NGINX real IP module](https://nginx.org/en/docs/http/ngx_http_realip_module.html)
- Manual or specification: [RFC 7239: Forwarded HTTP extension](https://www.rfc-editor.org/rfc/rfc7239)
- Maintainer or personal blog: [Scott Helme's blog](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare restoring visitor IPs](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/)
- Hands-on guide: [NGINX behind a proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
