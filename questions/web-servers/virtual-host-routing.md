---
title: Configure virtual-host routing safely
theme: web-servers
difficulty: junior
type: theory
tags: [http, dns, nginx, web-server]
sources:
  - url: https://nginx.org/en/docs/http/server_names.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure virtual-host routing safely

How does a web server select the site for `api.example.com`, and what should the default site do?

## Answer guide

- Configure an explicit virtual server for each accepted name and bind it to the intended address and port. NGINX first selects by address and port, then uses the request Host name to choose a matching server; certificates are selected during TLS before an HTTP request is available.
- Make the default server an intentional reject or minimal safe site, rather than a production application. Test both correct and unknown Host headers, including direct-IP access, and ensure DNS records, load-balancer listeners, SNI names and server configuration agree.
- Catch-all applications can turn typos, domain takeover remnants, and Host-header attacks into cross-tenant routing. Wildcards should be narrow and documented; a wildcard certificate does not authorize every hostname, and HTTPS requests can fail before Host routing on an SNI mismatch.

## References

- [NGINX server names](https://nginx.org/en/docs/http/server_names.html)
- Further reading (personal blog): [Scott Helme on web security](https://scotthelme.co.uk/)

## What to learn next

- Official documentation: [Apache name-based virtual hosts](https://httpd.apache.org/docs/2.4/vhosts/name-based.html)
- Manual or specification: [RFC 9112: HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112)
- Maintainer or personal blog: [Scott Helme's blog](https://scotthelme.co.uk/)
- Technical blog: [NGINX server-name guidance](https://www.nginx.com/blog/)
- Hands-on guide: [NGINX server blocks](https://nginx.org/en/docs/beginners_guide.html#conf_structure)
