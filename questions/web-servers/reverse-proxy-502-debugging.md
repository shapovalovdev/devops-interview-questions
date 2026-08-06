---
title: Debug a 502 response from a reverse proxy
theme: web-servers
difficulty: middle
type: troubleshooting
tags: [http, nginx, web-server, troubleshooting]
---

# Debug a 502 response from a reverse proxy

An NGINX reverse proxy returns 502 while the page itself is reachable. How do you isolate the failing layer?

## Answer guide

- Confirm the upstream process is running and listening on the configured address and protocol.
- Inspect proxy and application logs with the same request identifier or time window.
- Check upstream timeouts, TLS settings, name resolution, permissions, and network policy.
