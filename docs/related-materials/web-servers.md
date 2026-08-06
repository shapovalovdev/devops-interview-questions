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

Begin with virtual hosts, static content, TLS and request logging. Then proxy a
small application and deliberately break DNS, certificates, upstream
connectivity, cache keys and timeouts. Finish with capacity drills, deployment
draining, security boundaries and multi-tenant platform decisions.
