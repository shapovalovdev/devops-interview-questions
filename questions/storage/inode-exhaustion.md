---
title: Diagnose a full filesystem when free space remains
theme: storage
difficulty: middle
type: troubleshooting
tags: [linux, storage, filesystem, troubleshooting]
---

# Diagnose a full filesystem when free space remains

`df` reports free disk capacity, but creating a new file fails with “No space left on device.” What resource could be exhausted and how would you confirm it?

## Answer guide

- Inodes can be exhausted independently of data blocks, especially with many small files.
- Inspect inode usage separately from capacity, then identify the directories creating excessive file counts.
- Remediate safely and choose an appropriate filesystem or inode strategy for the workload.
