---
title: Select an NFS protocol version
theme: network-storage
difficulty: middle
type: scenario
tags: [storage, networking, security, performance]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8881.html
    source_type: standard
    verified_on: 2026-08-06
---

# Select an NFS protocol version

How would you select and roll out an NFS version for a mixed client estate?

## Answer guide

- Inventory client kernel, operating-system, identity, locking, and encryption capabilities, then choose a version explicitly rather than negotiating silently. NFSv4 has a stateful protocol model and a single well-known port; NFSv4.1 adds sessions and parallel-NFS capabilities specified by the standard.
- Pilot against representative clients and workloads, exercising failover, lock recovery, permission mapping, backup, and maintenance. Pin the version and relevant mount options in configuration management, and retain a tested rollback path while monitoring latency and RPC errors.
- Do not treat “newer” as automatically compatible. Old appliances, firewall rules, id-mapping configuration, or an application depending on a particular lock behavior can fail after a default-version change; mixing versions also complicates incident diagnosis.

## References

- [RFC 8881: NFSv4.1 protocol](https://www.rfc-editor.org/rfc/rfc8881.html)
- Further reading (blog): [Linux NFS project resources](https://www.spinics.net/lists/linux-nfs/)

## What to learn next

- Official documentation: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [Linux NFS project resources](https://www.spinics.net/lists/linux-nfs/)
- Technical blog: [Red Hat Blog: NFS](https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux)
- Hands-on guide: [Ubuntu Server: NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/)
