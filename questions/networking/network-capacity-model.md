---
title: Create a network capacity model
theme: networking
difficulty: staff
type: scenario
tags: [networking, monitoring, reliability, capacity-planning]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc5681.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create a network capacity model

How do you plan network capacity so a utilization graph does not hide saturation and user impact?

## Answer guide

- Model demand by traffic class, direction, region/zone, peak pattern, packet size, connection rate, and redundancy state—not only average bandwidth. Include bottlenecks such as NAT ports, load-balancer connections, firewall sessions, PPS, queues, and CPU.
- Relate capacity signals to user outcomes: latency, loss/retransmission, DNS/connect errors, and SLO burn. Congestion control responds to loss/marks and delay, so near-line-rate throughput can already be harmful to latency-sensitive traffic.
- Forecast growth and test the N-1 state: the remaining path must support critical load after a link, zone, appliance, or provider failure. Decide in advance which traffic is shed, rate-limited, or protected.
- Set alerts on leading saturation indicators and validate the model through load tests and incident postmortems. Capacity additions without route, security, and failure-domain review can simply move the bottleneck.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 5681: TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html)
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE Workbook: Addressing overload](https://sre.google/workbook/addressing-overload/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
