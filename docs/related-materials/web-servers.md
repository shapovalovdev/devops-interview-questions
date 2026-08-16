# Web servers: related materials

Use upstream server documentation and HTTP standards as factual authority. Learn
one server deeply enough to debug its request path, then practice the boundary
between browser, CDN or load balancer, reverse proxy, application and upstream
dependencies.

## What to learn next

- Official documentation: [NGINX documentation](https://nginx.org/en/docs/)
- Manual or specification: [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Mark Nottingham's HTTP blog](https://www.mnot.net/blog/)
- Technical blog: [NGINX engineering blog](https://www.nginx.com/blog/)
- Hands-on guide: [NGINX admin guide](https://docs.nginx.com/nginx/admin-guide/)

## Legal free books

- [High Performance Browser Networking](https://hpbn.co/) is a lawfully free,
  practical book by Ilya Grigorik covering transport, TLS and HTTP performance.
- [The Site Reliability Engineering book](https://sre.google/sre-book/table-of-contents/)
  is freely published by Google and is useful for capacity, overload and
  incident-response decisions at the edge.

## Suggested study order

Serve and log first, then proxy and deliberately break it, then run the edge
like a platform.

1. [Configure virtual-host routing safely](../../questions/web-servers/virtual-host-routing.html)
    — Virtual hosts are the first routing decision a web server ever makes.
2. [Serve static content with correct cache control](../../questions/web-servers/static-content-cache-control.html)
    — Static content with correct cache control is the first thing served at
    scale.
3. [Deploy a TLS certificate on a web server](../../questions/web-servers/tls-certificate-deployment.html)
    — TLS deployment secures what the routing just exposed.
4. [Design useful web-server access logs](../../questions/web-servers/access-log-design.html)
    — Request logging is designed before an incident needs it.
5. [Debug a 502 response from a reverse proxy](../../questions/web-servers/reverse-proxy-502-debugging.html)
    — Proxying begins by deliberately breaking DNS and upstream connectivity and
    reading the resulting 502.
6. [Establish a TLS security baseline at the edge](../../questions/web-servers/tls-security-baseline.html)
    — The edge TLS baseline hardens what the deployment step merely made work.
7. [Prevent a reverse-proxy cache from serving the wrong response](../../questions/web-servers/cache-proxy-correctness.html)
    — Breaking cache keys teaches exactly what a proxy must never serve wrong.
8. [Set reverse-proxy timeouts from a request budget](../../questions/web-servers/proxy-timeout-budget.html)
    — Timeouts are allocated from a request budget rather than set as
    independent knobs.
9. [Model web-server connection capacity](../../questions/web-servers/connection-capacity-model.html)
    — Capacity drills model what the proxy tier can actually hold.
10. [Reload and drain a web server without dropping traffic](../../questions/web-servers/graceful-reload-and-drain.html)
    — Deployment draining reloads the server without dropping live traffic.
11. [Define WAF and application-security boundaries](../../questions/web-servers/waf-and-application-boundaries.html)
    — Security boundaries assign what the edge owes versus what the application
    owes.
12. [Design multi-tenant isolation at the web edge](../../questions/web-servers/multi-tenant-edge-isolation.html)
    — Multi-tenant platform decisions close the Theme at edge scale.
