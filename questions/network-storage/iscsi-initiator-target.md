---
title: Explain iSCSI initiators and targets
theme: network-storage
difficulty: junior
type: theory
tags: [storage, networking, security, filesystem]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc7143.html
    source_type: standard
    verified_on: 2026-08-06
---

# Explain iSCSI initiators and targets

What are an iSCSI initiator and target, and what is the main safety concern after login?

## Answer guide

- iSCSI transports SCSI commands over IP. The initiator is the host-side client that discovers and logs in; the target exports one or more logical units (LUNs) that the initiator sees as block devices.
- Authenticate and authorize initiators, isolate storage traffic, use redundant paths where supported, and identify LUNs by stable identifiers. Before formatting or mounting, verify which host owns the filesystem and whether a clustered filesystem is required for concurrent writers.
- A LUN is not a shared filesystem. Mounting a conventional filesystem read-write from multiple independent hosts can corrupt it; accidental LUN presentation or weak CHAP secrets can also create data-exposure and destructive-operation risk.

## References

- [RFC 7143: iSCSI protocol](https://www.rfc-editor.org/rfc/rfc7143.html)
- Further reading (blog): [Red Hat Blog: storage](https://www.redhat.com/en/blog/channel/storage)

## What to learn next

- Official documentation: [Linux open-iscsi project](https://github.com/open-iscsi/open-iscsi)
- Manual or specification: [RFC 7143: iSCSI](https://www.rfc-editor.org/rfc/rfc7143.html)
- Maintainer or personal blog: [Ceph developer blog](https://ceph.io/en/news/blog/)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog/channel/storage)
- Hands-on guide: [RHEL: managing storage devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/index)
