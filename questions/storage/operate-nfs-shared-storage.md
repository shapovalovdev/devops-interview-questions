---
title: Operate NFS shared storage safely
theme: storage
difficulty: middle
type: scenario
tags: [storage, networking, linux, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8881.html
    source_type: standard
    verified_on: 2026-08-06
---

# Operate NFS shared storage safely

What operational checks are needed before placing a production shared workload on NFS?

## Answer guide

- Confirm the server, protocol version, export policy, identity mapping, mount options, network path, capacity, and performance behavior under representative concurrent access.
- Decide how clients should behave during server or network unavailability, and test locks, failover, and application retries rather than assuming local-disk semantics.
- Restrict exports and client access, monitor server latency/errors and client retransmits, and maintain backup/restore coverage independently of the share.
- A stale handle, split identity mapping, or an unavailable server can look like an application bug. Unsafe caching or lock assumptions may produce correctness failures, not only slow requests.

## References

- [RFC 8881: NFS version 4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Further reading (blog): [AWS Storage Blog: shared file storage patterns](https://aws.amazon.com/blogs/storage/)
