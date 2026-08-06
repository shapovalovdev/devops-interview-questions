---
title: Reload and drain a web server without dropping traffic
theme: web-servers
difficulty: middle
type: scenario
tags: [nginx, deployment, availability, web-server]
sources:
  - url: https://nginx.org/en/docs/control.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reload and drain a web server without dropping traffic

How would you deploy a configuration change while requests and long connections are active?

## Answer guide

- Render and syntax-test the configuration, capture the previous artifact, then use the server’s graceful reload mechanism so new workers receive the new configuration while old workers finish eligible work. Remove the node from new load-balancer selection first when a host replacement or disruptive change is required.
- Set a bounded drain period based on normal request and long-connection behavior, monitor old-worker count, active connections and error rate, and have a tested rollback that restores a known-good configuration. Automate the same validation in CI and deployment hooks.
- A reload is not magic: a syntax error can leave the old process running, a forced stop drops connections, and indefinitely streaming requests can prevent drain completion. Changing certificates, listeners or kernel limits may have different semantics; document which changes require restart and notify callers of maintenance risk.

## References

- [NGINX control signals](https://nginx.org/en/docs/control.html)
- Further reading (personal blog): [John Allspaw on operations](https://www.kitchensoap.com/)

## What to learn next

- Official documentation: [NGINX control signals](https://nginx.org/en/docs/control.html)
- Manual or specification: [systemd service management](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- Maintainer or personal blog: [John Allspaw's blog](https://www.kitchensoap.com/)
- Technical blog: [NGINX deployment guidance](https://www.nginx.com/blog/)
- Hands-on guide: [NGINX beginner's guide](https://nginx.org/en/docs/beginners_guide.html)
