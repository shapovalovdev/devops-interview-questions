---
title: Roll out HTTP/2 or HTTP/3 safely
theme: web-servers
difficulty: middle
type: scenario
tags: [http, tls, performance, web-server]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_v2_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Roll out HTTP/2 or HTTP/3 safely

How would you enable a newer HTTP protocol without losing compatibility or observability?

## Answer guide

- Keep HTTP/1.1 available as a fallback, enable the protocol at a controlled edge, and measure negotiation, protocol mix, handshake failures, connection reuse, errors and tail latency by client population. Confirm the TLS and load-balancer capabilities that the chosen implementation requires.
- HTTP/2 multiplexes streams on one connection, so tune concurrency, flow control and resource limits with real client behavior rather than treating each browser request as a separate TCP connection. HTTP/3 uses QUIC over UDP and needs firewall, observability and connection-migration consideration.
- A protocol upgrade does not automatically improve every workload: head-of-line effects, packet loss, buggy intermediaries and CPU cost may change. Avoid silently dropping UDP or relying on a CDN setting that the origin does not support. Roll back by stopping advertisement, not by invalidating active traffic blindly.

## References

- [NGINX HTTP/2 module](https://nginx.org/en/docs/http/ngx_http_v2_module.html)
- Further reading (personal blog): [Ilya Grigorik on HTTP performance](https://www.igvita.com/)

## What to learn next

- Official documentation: [NGINX HTTP/2 module](https://nginx.org/en/docs/http/ngx_http_v2_module.html)
- Manual or specification: [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)
- Maintainer or personal blog: [Ilya Grigorik's blog](https://www.igvita.com/)
- Technical blog: [Cloudflare HTTP/3 documentation](https://developers.cloudflare.com/speed/optimization/protocol/http3/)
- Hands-on guide: [curl HTTP version options](https://curl.se/docs/manpage.html)
