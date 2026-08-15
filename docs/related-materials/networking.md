# Networking: related materials

Use the RFCs and IANA registries referenced by each Question as factual authority.

## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)

## Suggested study order

Build the stack bottom-up: map a request to network layers, calculate CIDR
ranges, use private address space correctly, separate ports from sockets, and
choose TCP or UDP. Resolve names before connections — record types and TTLs,
then the lookup traced from application to authoritative answer, then the
delegation failure — because most service-down reports in this Theme start at
resolution. The transport group follows in dependency order: the failed
three-way handshake separating nothing-listening from something-dropping,
retransmissions and timeouts, the MTU black hole, and the TLS handshake failure
on top of a working transport. Routing diagnosis comes next — route selection,
asymmetric paths, NAT connection failures — and only then load-balancer
health-check design, which is undecidable until you know what a completed
handshake proves. Dual-stack planning and operation, segmentation, and egress
governance form the policy tier. The remainder — the capacity model, safe
change delivery, multi-region boundaries, the BGP route leak, DNS incident
response, the reliability strategy — are answered for a network rather than a
host.
