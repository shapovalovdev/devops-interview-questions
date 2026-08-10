---
title: Explain NFS cache coherency
theme: network-storage
difficulty: middle
type: theory
tags: [storage, networking, performance, filesystem]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8881.html
    source_type: standard
    verified_on: 2026-08-06
---

# Explain NFS cache coherency

Why might one NFS client not immediately observe another client’s update?

## Answer guide

- NFS clients cache file data and attributes to reduce RPC traffic. The protocol has cache-coherency mechanisms such as attribute validation and, in NFSv4, delegations, but an application cannot assume that independent clients observe every metadata or data change at the same instant.
- Establish whether the workload needs close-to-open behavior, explicit synchronization, a lock, a database, or a different coordination primitive. Measure the selected client and server mount/export configuration under concurrent writers and readers.
- Disabling caches globally can damage performance and still does not create transactional application semantics. Conversely, an application that polls a shared file without synchronization can serve stale data or race with a partial write.

## References

- [RFC 8881: NFS client-side caching](https://www.rfc-editor.org/rfc/rfc8881.html)
- Further reading (blog): [Linux NFS project resources](https://www.spinics.net/lists/linux-nfs/)

## What to learn next

- Official documentation: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [Linux NFS project resources](https://www.spinics.net/lists/linux-nfs/)
- Technical blog: [Red Hat Blog: NFS](https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux)
- Hands-on guide: [Ubuntu Server: NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/)
