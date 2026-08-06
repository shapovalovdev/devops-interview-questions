---
title: Explain Linux process states during an incident
theme: linux
difficulty: junior
type: theory
tags: [linux, debugging, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/ps.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Linux process states during an incident

What do common process states mean, and why should an operator inspect them before restarting a service?

## Answer guide

- `ps` reports process state using a primary code plus optional modifiers. A runnable task may be executing or waiting for CPU; interruptible sleep usually waits for an event, while uninterruptible sleep commonly indicates a kernel wait such as I/O.
- A stopped task has been suspended; a zombie has exited but remains until its parent reaps its status. A zombie consumes a process-table entry, not the original process memory, but persistent zombies can expose a broken parent/reaping design.
- State is evidence, not a diagnosis. Correlate it with wait channel, parent process, resource latency, logs, and duration before terminating a process; an uninterruptible task often cannot be cleanly killed until its kernel wait returns.

## References

- [ps(1): process status codes](https://man7.org/linux/man-pages/man1/ps.1.html)
- Further reading: [proc(5): process information pseudo-filesystem](https://man7.org/linux/man-pages/man5/proc.5.html)
