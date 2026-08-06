---
title: Proxy WebSocket connections correctly
theme: web-servers
difficulty: middle
type: scenario
tags: [http, nginx, tcp, web-server]
sources:
  - url: https://nginx.org/en/docs/http/websocket.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Proxy WebSocket connections correctly

What changes are required when a reverse proxy fronts a WebSocket application?

## Answer guide

- Forward the HTTP Upgrade and Connection headers as required by the proxy, use HTTP/1.1 on the upstream hop when applicable, and configure an idle timeout compatible with the application’s ping or heartbeat interval. Authenticate and authorize the upgrade just like any other request.
- Model WebSockets as long-lived connections: monitor concurrent connections, memory, file descriptors, upstream disconnects and reconnect rates. Drain an instance before deployment, publish retry guidance with exponential backoff, and test intermediary support from CDN through load balancer to application.
- A default short read timeout can close otherwise healthy idle connections, while unlimited connections can exhaust worker or upstream capacity. Do not use a generic HTTP retry after an upgrade: application messages may already have side effects and reconnection must restore state safely.

## References

- [NGINX WebSocket proxying](https://nginx.org/en/docs/http/websocket.html)
- Further reading (personal blog): [Ilya Grigorik on networking](https://www.igvita.com/)

## What to learn next

- Official documentation: [NGINX WebSocket proxying](https://nginx.org/en/docs/http/websocket.html)
- Manual or specification: [RFC 6455: WebSocket protocol](https://www.rfc-editor.org/rfc/rfc6455)
- Maintainer or personal blog: [Ilya Grigorik's blog](https://www.igvita.com/)
- Technical blog: [NGINX WebSocket guidance](https://www.nginx.com/blog/)
- Hands-on guide: [NGINX reverse proxy guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
