# Linux Networking: related materials

Use the kernel and Linux manual pages attached to each Question as authority for
host behaviour. These resources offer complementary practice and operational
context; distribution defaults, firewall stacks, and network-manager behavior
must still be checked on the actual host.

## What to learn next

- Official documentation: [Linux kernel networking documentation](https://www.kernel.org/doc/html/latest/networking/)
- Manual or specification: [netlink(7) Linux manual](https://man7.org/linux/man-pages/man7/netlink.7.html)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)

## Legal free books

No Linux networking book is listed here. The linked kernel documentation,
manuals, and author-published articles are free to read; this avoids directing
learners to unauthorized copies of commercial networking texts.

## Suggested study order

Interfaces, addresses, and routes before MTU and packet capture, and the
namespace and policy tier only once single-host diagnosis is reliable.

1. [Inspect Linux interface state and addresses](../../questions/linux-networking/interface-state-and-addresses.html)
    — Interfaces and addresses are the first facts every later diagnosis reads.
2. [Explain a Linux default route](../../questions/linux-networking/default-route-basics.html)
    — The default route decides where everything unmentioned actually goes.
3. [Debug a Linux route with ip route get](../../questions/linux-networking/route-get-debugging.html)
    — ip route get shows the kernel's routing decision for one packet, the route
    tier's tool.
4. [Explain Linux DNS resolver configuration](../../questions/linux-networking/dns-resolver-configuration.html)
    — Resolver configuration decides which names the host can even ask about.
5. [Identify the process listening on a Linux port](../../questions/linux-networking/socket-listener-inspection.html)
    — Socket state answers who is listening, the question before any
    connectivity debugging.
6. [Triage TCP connection states on Linux](../../questions/linux-networking/tcp-connection-state-triage.html)
    — Connection states show the handshake's aftermath from the host's side.
7. [Diagnose an MTU mismatch on Linux](../../questions/linux-networking/mtu-mismatch-triage.html)
    — MTU mismatches fail only for large packets, so they follow the state tier
    that can prove it.
8. [Triage a failed Linux neighbour entry](../../questions/linux-networking/neighbour-table-triage.html)
    — Neighbour discovery is layer-two reachability, the tier underneath
    routing.
9. [Triage a Linux host firewall path](../../questions/linux-networking/firewall-path-triage.html)
    — Firewall paths are where correct routes still silently drop packets.
10. [Capture Linux packets without losing diagnostic value](../../questions/linux-networking/packet-capture-scope.html)
    — Capturing with the right scope keeps evidence without drowning the reader.
11. [Diagnose a Linux TCP accept-backlog overflow](../../questions/linux-networking/tcp-backlog-overflow.html)
    — The accept-backlog overflow is the socket tier's saturation failure.
12. [Debug connectivity across a Linux network namespace](../../questions/linux-networking/network-namespace-connectivity.html)
    — Namespaces reopen every earlier tool from a different vantage point.
13. [Diagnose Linux policy routing rules](../../questions/linux-networking/policy-routing-with-rules.html)
    — Policy routing answers why the seemingly wrong interface answered.
14. [Select a Linux traffic-control investigation path](../../questions/linux-networking/traffic-control-qdisc.html)
    — The qdisc investigation shows shaping and queueing the routes never
    mentioned.
15. [Build a Linux network capacity strategy](../../questions/linux-networking/linux-network-capacity-strategy.html)
    — The capacity strategy prices the host network the diagnostics kept honest.
16. [Lead a Linux networking incident response](../../questions/linux-networking/linux-network-incident-command.html)
    — Incident command spends the whole diagnostic stack under real pressure.
17. [Set zero-trust Linux host network boundaries](../../questions/linux-networking/zero-trust-host-network-boundaries.html)
    — Zero-trust boundaries close the Theme by removing the trusted-host
    assumption everything above leaned on.
