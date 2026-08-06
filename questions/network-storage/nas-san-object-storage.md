---
title: Choose NAS, SAN, or object storage for a workload
theme: network-storage
difficulty: junior
type: theory
tags: [storage, networking, performance]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose NAS, SAN, or object storage for a workload

How do NAS, SAN, and object storage differ, and how would you select one for a workload?

## Answer guide

- NAS exposes a shared file namespace over a file protocol such as NFS or SMB; applications use paths, directories, and file permissions. SAN presents remote block devices, so a host or clustered filesystem owns formatting and filesystem semantics. Object stores use an API and object keys rather than POSIX files.
- Start with the application contract: use a supported shared filesystem for workloads requiring POSIX-like concurrent file access, block storage for a database that controls its own filesystem and latency, and object storage for durable immutable artifacts, backups, or web-scale data.
- Compare latency, IOPS, throughput, consistency, sharing, lifecycle, and recovery objectives using a realistic benchmark. Do not mount an object store as though it were a fully POSIX filesystem without validating its semantics; rename, locking, and metadata behavior can differ materially.

## References

- [Amazon S3 User Guide: object storage concepts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- Further reading (blog): [Ceph Blog: storage architecture and operations](https://ceph.io/en/news/blog/)

## What to learn next

- Official documentation: [Ceph architecture](https://docs.ceph.com/en/latest/architecture/)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Cloudflare Blog: R2 object storage](https://blog.cloudflare.com/introducing-r2-object-storage/)
- Hands-on guide: [Ceph RGW quick start](https://docs.ceph.com/en/latest/start/quick-rgw/)
