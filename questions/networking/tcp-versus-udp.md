---
title: Choose between TCP and UDP
theme: networking
difficulty: junior
type: theory
tags: [tcp, networking, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9293.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc768.html
    source_type: standard
    verified_on: 2026-08-06
---

# Choose between TCP and UDP

What guarantees does TCP provide that UDP does not, and when can UDP still be appropriate?

## Answer guide

- TCP is connection-oriented and gives an application a reliable, in-order **byte stream**. Sequence numbers, acknowledgements, checksums, retransmission, flow control, and congestion control are the mechanisms behind that service; TCP does not preserve application message boundaries.
- UDP supplies datagrams: each receive corresponds to a datagram, but the protocol does not establish a connection or provide delivery, ordering, duplicate suppression, congestion control, or retransmission. An application that needs those properties over UDP must design them explicitly.
- Choose TCP when correctness depends on complete ordered delivery, such as most HTTP APIs, database protocols, and SSH. Choose UDP when message boundaries and timeliness matter more than retransmitting old data, or when the application has a suitable reliability/congestion design (for example DNS, real-time media, or QUIC).
- A common failure is treating UDP as "faster TCP": loss, reordering, fragmentation, and receiver overload still occur. Conversely, TCP head-of-line blocking can make a single lost segment delay later bytes, so it can be a poor match for latency-sensitive independent messages.

## References

- [RFC 9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html)
- [Cloudflare learning: What is UDP?](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)
