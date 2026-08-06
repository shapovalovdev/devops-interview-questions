---
title: Choose NFS failure behavior
theme: network-storage
difficulty: middle
type: scenario
tags: [storage, networking, reliability, performance]
sources:
  - url: https://man7.org/linux/man-pages/man5/nfs.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose NFS failure behavior

What trade-off does an NFS hard or soft mount make during a server outage?

## Answer guide

- A hard mount keeps retrying an unavailable server, preserving the expectation that an I/O either eventually completes or remains blocked. A soft-style policy can return an error after retransmission limits, letting an application react but making incomplete or failed operations visible sooner.
- Choose behavior from the application’s correctness contract, not convenience. Document timeouts, retry policy, health checks, service stop behavior, and how operators distinguish a blocked remote I/O from a local application deadlock.
- Soft failure can cause applications not designed for I/O errors to mishandle or corrupt work, while hard retry can exhaust worker pools and make shutdown appear stuck. Test a real server loss and recovery before declaring either setting safe.

## References

- [nfs(5): soft, hard, and timeout options](https://man7.org/linux/man-pages/man5/nfs.5.html)
- Further reading (blog): [Linux NFS project resources](https://wiki.linux-nfs.org/wiki/index.php/Main_Page)

## What to learn next

- Official documentation: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Manual or specification: [nfs(5) manual](https://man7.org/linux/man-pages/man5/nfs.5.html)
- Maintainer or personal blog: [Linux NFS project resources](https://wiki.linux-nfs.org/wiki/index.php/Main_Page)
- Technical blog: [Red Hat Blog: NFS](https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux)
- Hands-on guide: [Ubuntu Server: NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/)
