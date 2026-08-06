---
title: Diagnose a full filesystem when free space remains
theme: storage
difficulty: middle
type: troubleshooting
tags: [linux, storage, filesystem, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/df.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a full filesystem when free space remains

`df` reports free disk capacity, but creating a new file fails with “No space left on device.” What resource could be exhausted and how would you confirm it?

## Answer guide

- An inode is filesystem metadata for an object, so a filesystem can have free data blocks but no inodes available for a new file. This is common with caches, mail queues, and other small-file workloads.
- Confirm the distinction with `df -h` and `df -i` for the affected mount, then count files by subtree without crossing mounts. Check quotas too; an inode quota can produce a similar symptom for one user.
- Stop or bound the file-producing workload, remove data according to its retention policy, and verify inode headroom afterwards. Reformatting or changing inode allocation is a migration decision, not an emergency cleanup command.
- Deleting blindly can destroy queues or evidence. A capacity-only alert misses this failure mode, so alert separately on inode consumption and growth rate.

## References

- [GNU df manual](https://man7.org/linux/man-pages/man1/df.1.html)
- Further reading (blog): [Managing file systems in Red Hat Enterprise Linux](https://www.redhat.com/en/blog/linux-filesystem-management)
