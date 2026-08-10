---
title: Recover storage held by deleted open files
theme: storage
difficulty: middle
type: troubleshooting
tags: [linux, storage, filesystem, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man2/unlink.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Recover storage held by deleted open files

Why can `df` show a full filesystem after a large log was deleted, and how do you recover safely?

## Answer guide

- Removing a pathname unlinks it; space is not released while a process still holds the file open. Find deleted-but-open files with an appropriate privileged open-file inspection and identify the owning service.
- Prefer the service's supported log rotation or restart procedure so it closes and reopens the descriptor, then confirm free blocks return. Preserve required logs before restarting.
- Add bounded rotation, disk alerts, and a runbook that distinguishes pathname usage from allocated blocks.
- Truncating a live descriptor can lose evidence or confuse applications. Killing arbitrary processes can turn a storage incident into an availability incident.

## References

- [unlink(2) manual](https://man7.org/linux/man-pages/man2/unlink.2.html)
- Further reading (blog): [AWS Storage Blog: monitor storage performance](https://aws.amazon.com/blogs/storage/valuable-tips-for-monitoring-and-understanding-amazon-ebs-performance-using-amazon-cloudwatch/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
