---
title: Serve static content with correct cache control
theme: web-servers
difficulty: junior
type: scenario
tags: [http, web-server, performance]
sources:
  - url: https://nginx.org/en/docs/http/ngx_http_headers_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Serve static content with correct cache control

How would you cache JavaScript and image assets without making releases difficult to roll back?

## Answer guide

- Give immutable versioned assets content-derived filenames and serve them with a long `Cache-Control: max-age` and `immutable` policy. Serve the HTML entry point with a short revalidation policy, because it selects which asset versions clients should load.
- Set headers at the server or CDN deliberately and inspect the actual response after a deploy. ETag and Last-Modified support conditional requests, but should not be the only rollback mechanism; a new HTML document must reference the intended previous or new asset set.
- A long cache lifetime on unversioned `/app.js` creates stale clients and inconsistent behavior. Conversely, no caching increases origin load and tail latency. Account for intermediary caches, service workers, negative caching and CDN invalidation delay in the release plan.

## References

- [NGINX headers module](https://nginx.org/en/docs/http/ngx_http_headers_module.html)
- Further reading (personal blog): [Jake Archibald on caching](https://jakearchibald.com/)

## What to learn next

- Official documentation: [Apache mod_expires](https://httpd.apache.org/docs/2.4/mod/mod_expires.html)
- Manual or specification: [RFC 9111: HTTP caching](https://www.rfc-editor.org/rfc/rfc9111)
- Maintainer or personal blog: [Jake Archibald's blog](https://jakearchibald.com/)
- Technical blog: [Cloudflare cache documentation](https://developers.cloudflare.com/cache/)
- Hands-on guide: [NGINX static content guide](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/)
