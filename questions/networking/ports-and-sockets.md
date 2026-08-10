---
title: Explain ports and sockets
theme: networking
difficulty: junior
type: theory
tags: [networking, tcp, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9293.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain ports and sockets

Why can many clients connect to the same HTTPS port, and what identifies one TCP connection?

## Answer guide

- A port identifies a transport-layer application endpoint on a host; IANA maintains the service-name and port-number registry, but a registered port does not itself configure access or security.
- A TCP connection is distinguished by protocol plus local address/port and remote address/port. Therefore a server can listen on one local port (such as 443) while each client has a different source address and usually an ephemeral source port.
- A listening socket is not the same as an established connection. Inspect both the process/listener and the connection state when debugging a refused connection, backlog pressure, or port conflict.
- Binding to `127.0.0.1`, `0.0.0.0`, `::1`, or `::` changes which address families and interfaces can receive traffic; dual-stack behavior is operating-system and socket-option dependent.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 9293: TCP ports and connection identifiers](https://www.rfc-editor.org/rfc/rfc9293.html)
- [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [man7: socket(7)](https://man7.org/linux/man-pages/man7/socket.7.html)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
