---
title: Explain Linux permissions and umask
theme: linux
difficulty: junior
type: theory
tags: [linux, security, least-privilege]
sources:
  - url: https://man7.org/linux/man-pages/man2/umask.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Linux permissions and umask

How do owner, group, other permissions and umask affect a newly created file, and what can make this model insufficient?

## Answer guide

- Traditional discretionary access checks select owner, group, or other permission bits based on the caller's effective IDs. Directories additionally need search/execute permission to traverse them; read permission alone is not enough to access an entry by name.
- A process umask clears requested permission bits when creating files and directories. It is a default restriction, not an access-control policy: an application can request modes, later change them, or inherit a deliberately configured umask from its service manager.
- Check ownership, mode, parent-directory traversal, ACLs, mount options, and mandatory security policy when access is surprising. Do not solve a deployment failure with broad `chmod 777`; grant the smallest required identity and path permissions.

## References

- [umask(2): file creation mask](https://man7.org/linux/man-pages/man2/umask.2.html)
- Further reading: [path_resolution(7): pathname permission checks](https://man7.org/linux/man-pages/man7/path_resolution.7.html)
