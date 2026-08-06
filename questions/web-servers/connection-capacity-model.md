---
title: Model web-server connection capacity
theme: web-servers
difficulty: senior
type: scenario
tags: [performance, capacity-planning, file-descriptors, nginx]
sources:
  - url: https://nginx.org/en/docs/ngx_core_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Model web-server connection capacity

How do you determine whether a web-server fleet has enough connection capacity for a traffic event?

## Answer guide

- Model concurrent connections from arrival rate and observed connection lifetime, then validate against worker limits, open-file limits, sockets, memory per connection, TLS CPU, upstream capacity and load-balancer limits. Load-test with realistic keep-alive, slow clients, WebSockets and error behavior rather than requests per second alone.
- Set alerts on utilization and saturation indicators such as accepted versus dropped connections, file descriptors, worker queues, handshake failures, retransmissions and upstream waits. Reserve headroom for a node or zone failure and prove scaling behavior through a controlled drill.
- Raising `worker_connections` without raising OS descriptor limits simply moves the failure. A benchmark with short local requests misses slow-client buffering and TLS cost. Autoscaling only on CPU can react too late when socket or upstream pools are exhausted; capacity includes dependencies, not just the proxy.

## References

- [NGINX core module worker settings](https://nginx.org/en/docs/ngx_core_module.html)
- Further reading (personal blog): [Brendan Gregg on performance](https://www.brendangregg.com/blog/)

## What to learn next

- Official documentation: [NGINX connection processing](https://nginx.org/en/docs/events.html)
- Manual or specification: [Linux file descriptor limits](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- Maintainer or personal blog: [Brendan Gregg's blog](https://www.brendangregg.com/blog/)
- Technical blog: [Cloudflare learning center](https://www.cloudflare.com/learning/)
- Hands-on guide: [NGINX tuning guide](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/)
