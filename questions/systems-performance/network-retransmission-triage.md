---
title: How do TCP retransmissions inform a latency investigation?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, networking, tcp, performance]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9293
    source_type: standard
    verified_on: 2026-08-06
---

# How do TCP retransmissions inform a latency investigation?

## Answer guide

- Retransmissions indicate that TCP did not receive an acknowledgement within its loss-recovery logic or received duplicate acknowledgements; they are a symptom, not proof of one network fault.
- Correlate retransmissions with RTT, congestion window, interface drops, NIC errors, packet captures, peer behavior, and application latency. Inspect both endpoints and the path when possible because loss can occur before, after, or outside the host.
- Do not tune TCP timers first. Congestion, overloaded receivers, MTU mismatch, middleboxes, and packet loss have different remedies, while encrypted or sampled capture data can leave uncertainty that must be recorded.

## References

- [RFC 9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [ss manual](https://man7.org/linux/man-pages/man8/ss.8.html)
- Further reading (blog): [Brendan Gregg — TCP Performance](https://www.brendangregg.com/blog/2016-09-01/linux-tcp-bcc.html)

## What to learn next

- Official documentation: [IETF TCP RFC index](https://www.rfc-editor.org/rfc/rfc9293)
- Manual or specification: [ss manual](https://man7.org/linux/man-pages/man8/ss.8.html)
- Maintainer or personal blog: [Brendan Gregg — TCP tools](https://www.brendangregg.com/blog/2016-09-01/linux-tcp-bcc.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Wireshark TCP analysis](https://www.wireshark.org/docs/)
