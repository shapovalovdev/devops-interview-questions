---
title: Use strace safely to investigate a hung Linux process
theme: linux
difficulty: senior
type: troubleshooting
tags: [linux, debugging, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/strace.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use strace safely to investigate a hung Linux process

How can `strace` help diagnose a hung process, and what operational risks must you manage?

## Answer guide

- `strace` observes system calls and signals, so attaching can reveal whether a process is repeatedly failing a call, blocked in a syscall, waiting on a socket, or making unexpected file accesses. It cannot by itself explain all user-space deadlocks or prove a remote dependency is healthy.
- Limit scope and duration: attach only to the affected PID, filter relevant calls, write output to controlled storage, and avoid dumping sensitive arguments or high-volume traces. Tracing adds overhead and may distort a latency-sensitive failure.
- Correlate the syscall with process state, stack/profile data where permitted, logs, and dependency metrics. Reproduce under lower risk when possible, then remove tracing and verify the proposed fix under load.

## References

- [strace(1): system-call tracer](https://man7.org/linux/man-pages/man1/strace.1.html)
- Further reading: [proc_pid_stack(5): kernel stack for a process](https://man7.org/linux/man-pages/man5/proc_pid_stack.5.html)
