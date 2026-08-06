---
title: Interpret TCP retransmissions and timeouts
theme: networking
difficulty: middle
type: troubleshooting
tags: [tcp, networking, monitoring, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc6298.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc5681.html
    source_type: standard
    verified_on: 2026-08-06
---

# Interpret TCP retransmissions and timeouts

What does a rising TCP retransmission rate mean, and what evidence do you need before changing timeouts?

## Answer guide

- TCP retransmits when acknowledgements do not arrive before its retransmission timer, but a retransmission is evidence of missing acknowledgement—not a direct measurement of physical packet loss. Delay, reordering, receiver pressure, and a broken reverse path can also trigger it.
- RFC 6298 bases the retransmission timeout on measured round-trip time and variance; modern stacks implement details and limits of their own. Congestion control reduces sending after inferred loss, so aggressive retransmission or retry tuning can worsen a congested path.
- Correlate client and server packet traces, RTT, interface errors/drops, queue metrics, and load-balancer/firewall counters. Determine whether original data, acknowledgements, or both disappear and whether it is tied to a path, destination, or time window.
- Application timeouts must include DNS, connect, TLS, request, and retry budgets deliberately. Blindly increasing them hides faults and consumes concurrency; blindly decreasing them turns transient delay into avoidable failures.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 6298: Computing TCP's Retransmission Timer](https://www.rfc-editor.org/rfc/rfc6298.html)
- [RFC 5681: TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html)
- [Cloudflare learning: What is packet loss?](https://www.cloudflare.com/learning/performance/what-is-packet-loss/)
