---
title: Operate NFS shared storage safely
theme: storage
difficulty: middle
type: scenario
tags: [storage, networking, linux, reliability, lfcs]
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
- Further reading (blog): [AWS Storage Blog: shared file storage patterns](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
