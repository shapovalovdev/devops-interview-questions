---
title: Debug process visibility across PID namespaces
theme: linux
difficulty: senior
type: troubleshooting
tags: [linux, containers, debugging, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man7/pid_namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug process visibility across PID namespaces

Why might a process have different PIDs inside and outside a container, and how does that affect incident investigation?

## Answer guide

- PID namespaces isolate the process-ID view. A process can have a PID in its namespace and one in each ancestor namespace in which it is visible; tools and signals resolve IDs from the caller’s namespace perspective.
- Establish the namespace and host PID before inspecting `/proc`, sending signals, or correlating logs. The namespace init process has special signal behavior, and a process in a child namespace cannot see parent-namespace processes.
- Use the runtime’s supported debugging path and apply least privilege. Joining namespaces or exposing host process views can bypass isolation and should be bounded, audited, and removed after the investigation.

## References

- [pid_namespaces(7): PID namespace semantics](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- Further reading: [namespaces(7): Linux namespace overview](https://man7.org/linux/man-pages/man7/namespaces.7.html)
