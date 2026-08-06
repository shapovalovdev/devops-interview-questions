---
title: Diagnose a full filesystem with free-looking space
theme: linux-performance
difficulty: junior
type: troubleshooting
tags: [linux, performance, filesystem, storage, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/df.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a full filesystem with free-looking space

Why can a process receive “No space left on device” when `df -h` appears healthy?

## Answer guide

- Check both block and inode availability: `df -h` reports allocated blocks while `df -i` reports inode counts. A filesystem with many small files can exhaust inodes before its byte capacity is full.
- Confirm the exact mount namespace and filesystem used by the failing process, then inspect quotas, reserved blocks, deleted-but-open files, and the directory creating files. Capture the error, path, mount, and tenant before deleting anything.
- Do not remove files blindly during an incident: a deleted file held open still consumes blocks until its process closes it, and deleting logs can lose evidence. Fix retention, quotas, or file-creation behavior and test the recovery path.

## References

- [df(1): report filesystem space and inode usage](https://man7.org/linux/man-pages/man1/df.1.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux VFS documentation](https://www.kernel.org/doc/html/latest/filesystems/vfs.html)
- Manual or specification: [df(1)](https://man7.org/linux/man-pages/man1/df.1.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [GitLab Handbook — infrastructure](https://handbook.gitlab.com/handbook/engineering/infrastructure/)
- Hands-on guide: [lsof manual](https://man7.org/linux/man-pages/man8/lsof.8.html)
