---
title: Diagnose too many open files in a Linux service
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, debugging, troubleshooting, lfcs]
sources:
  - url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose too many open files in a Linux service

An application reports “too many open files.” How do you find the leaking resource and choose a safe remedy?

## Answer guide

- Confirm the failing process and its soft and hard `RLIMIT_NOFILE` values; the soft limit is the enforced current limit and a process cannot raise its hard limit without the relevant privilege.
- Inspect `/proc/<pid>/fd` or an equivalent tool to classify descriptors as regular files, sockets, pipes, or deleted files still held open. Compare growth over time and request/connection churn to distinguish a leak from an undersized, legitimate concurrency limit.
- Correct the application close/error-path or connection-pool lifecycle first. Raising a service limit can be appropriate after capacity testing, but it only delays failure if descriptors grow unbounded and can move pressure to system-wide file limits.
- Validate the fix under sustained realistic traffic and add a descriptor-count metric with a limit-relative alert.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [getrlimit(2): resource limits](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- Further reading: [proc_pid_fd(5): process file-descriptor directory](https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html)

## What to learn next

- Official documentation: [Linux kernel administration guide](https://docs.kernel.org/admin-guide/)
- Manual or specification: [proc(5) Linux manual](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance analysis](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
