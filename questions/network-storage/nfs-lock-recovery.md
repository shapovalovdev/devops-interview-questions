---
title: Plan NFS lock recovery
theme: network-storage
difficulty: middle
type: scenario
tags: [storage, networking, reliability, filesystem]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8881.html
    source_type: standard
    verified_on: 2026-08-06
---

# Plan NFS lock recovery

What should happen to an application’s NFS locks after an NFS server restart?

## Answer guide

- NFSv4 tracks state including opens and locks, and defines recovery periods in which clients reclaim state after a server restart. The exact outcome depends on server persistence, client behavior, protocol version, lease timing, and whether the client can reconnect.
- Test planned and unplanned restart recovery with the real application, including its retry policy and any external leader election. Monitor server recovery messages, client RPC errors, lock acquisition latency, and duplicate or abandoned worker behavior.
- Do not simply restart application nodes concurrently with the storage service. A failed reclaim or split-brain application leader can result in conflicting writers; application-level fencing and durable coordination may be needed beyond filesystem locks.

## References

- [RFC 8881: NFS state and crash recovery](https://www.rfc-editor.org/rfc/rfc8881.html)
- Further reading (blog): [linux-nfs mailing list archive](https://lore.kernel.org/linux-nfs/)

## What to learn next

- Official documentation: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [linux-nfs mailing list archive](https://lore.kernel.org/linux-nfs/)
- Technical blog: [Red Hat Blog: NFS](https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux)
- Hands-on guide: [Ubuntu Server: NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/)
