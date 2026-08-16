# Networking: related materials

Use the RFCs and IANA registries referenced by each Question as factual authority.

## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)

## Suggested study order

Build the stack bottom-up and resolve names before connections, because most
service-down reports in this Theme start at resolution.

1. [Map a request to network layers](../../questions/networking/osi-and-tcp-ip-layers.html)
    — Mapping a request to network layers is the map every later diagnosis
    navigates.
2. [Calculate an IPv4 CIDR range](../../questions/networking/cidr-address-calculation.html)
    — CIDR arithmetic is the addressing vocabulary the map requires.
3. [Use private IPv4 address space safely](../../questions/networking/private-address-space.html)
    — Private address space used correctly keeps routing honest.
4. [Explain ports and sockets](../../questions/networking/ports-and-sockets.html)
    — Ports versus sockets separates names from actual endpoints.
5. [Choose between TCP and UDP](../../questions/networking/tcp-versus-udp.html)
    — TCP or UDP is the transport choice everything above enables.
6. [Select DNS record types and TTLs](../../questions/networking/dns-record-types-and-ttl.html)
    — Names before connections: record types and TTLs are DNS's own contract.
7. [Trace a DNS lookup from an application to an answer](../../questions/networking/dns-resolution-path.html)
    — The lookup traced from application to authoritative answer is the path
    most service-down reports start on.
8. [Debug an authoritative DNS delegation](../../questions/networking/authoritative-dns-delegation.html)
    — The delegation failure is name resolution breaking at its root.
9. [Diagnose a failed TCP three-way handshake](../../questions/networking/tcp-three-way-handshake.html)
    — The failed handshake separates a host with nothing listening from one
    silently dropping packets.
10. [Interpret TCP retransmissions and timeouts](../../questions/networking/tcp-retransmission-and-timeouts.html)
    — Retransmissions and timeouts quantify how much distress the transport is
    actually in.
11. [Diagnose a path MTU discovery black hole](../../questions/networking/path-mtu-discovery.html)
    — The MTU black hole fails only the big packets, found after transport
    works.
12. [Debug a TLS handshake failure](../../questions/networking/tls-handshake-failure.html)
    — TLS fails on top of a working transport, so it is diagnosed last in the
    group.
13. [Diagnose route selection and asymmetric paths](../../questions/networking/route-selection-and-asymmetry.html)
    — Routing diagnosis opens with selection and the asymmetric paths it hides.
14. [Troubleshoot NAT connection failures](../../questions/networking/nat-connection-troubleshooting.html)
    — NAT connection failures are routing's stateful cousin, diagnosed after
    plain selection is understood.
15. [Design load-balancer health checks](../../questions/networking/load-balancer-health-check-design.html)
    — Health-check design is undecidable until you know what a completed
    handshake actually proves.
16. [Operate a dual-stack service](../../questions/networking/ipv6-dual-stack-basics.html)
    — The policy tier opens with operating a dual-stack service.
17. [Plan a dual-stack migration](../../questions/networking/dual-stack-migration-plan.html)
    — The migration plan is the dual-stack strategy set in motion.
18. [Design network segmentation for a service](../../questions/networking/network-segmentation-design.html)
    — Segmentation decides what may talk to what, as policy.
19. [Govern production network egress](../../questions/networking/egress-governance.html)
    — Egress governance turns outbound traffic into policy with owners.
20. [Create a network capacity model](../../questions/networking/network-capacity-model.html)
    — The remainder opens with the capacity model, answered for a network rather
    than a host.
21. [Build safe network change delivery](../../questions/networking/network-change-management.html)
    — Safe change delivery keeps the network itself from being the outage.
22. [Design multi-region connectivity boundaries](../../questions/networking/multi-region-connectivity-architecture.html)
    — Multi-region boundaries spend the capacity and change tiers at scale.
23. [Respond to a BGP route leak risk](../../questions/networking/bgp-route-leak-response.html)
    — The BGP route leak is the internet's failure mode arriving at your door.
24. [Lead a DNS incident response](../../questions/networking/dns-incident-response.html)
    — DNS incident response is the resolution tier's worst day, rehearsed.
25. [Set a network reliability strategy](../../questions/networking/network-reliability-strategy.html)
    — The reliability strategy closes the Theme as a funded promise.
