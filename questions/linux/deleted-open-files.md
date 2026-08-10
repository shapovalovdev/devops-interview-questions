---
title: Recover disk space held by deleted open files
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, filesystem, troubleshooting, lfcs]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Recover disk space held by deleted open files

Why can a filesystem remain full after a large log file is deleted, and how do you recover safely?

## Answer guide

- Removing a pathname unlinks it from the directory; storage is not reclaimed while a process still has an open reference to that file. This commonly occurs when log rotation deletes a file a long-running process continues to write.
- Identify the holding process through its file-descriptor entries and confirm the deleted target and filesystem. Prefer the service’s documented log-reopen mechanism or a controlled restart so the descriptor is closed; truncating through a descriptor is a riskier last resort that can surprise the process.
- Fix rotation coordination, retention, and disk alerts. Validate free blocks and inode availability after cleanup, because “disk full” can also be quota, reservation, or inode exhaustion.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [proc_pid_fd(5): file descriptors for a process](https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html)
- Further reading: [unlink(2): removing a directory entry](https://man7.org/linux/man-pages/man2/unlink.2.html)

## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Vidar Holen — Linux Ate My RAM](https://www.linuxatemyram.com/)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
