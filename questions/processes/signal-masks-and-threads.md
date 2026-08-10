---
title: Reason about signal masks in a multithreaded service
theme: processes
difficulty: middle
type: theory
tags: [linux, processes, signals, debugging]
sources:
  - url: https://man7.org/linux/man-pages/man7/signal.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reason about signal masks in a multithreaded service

Why can a signal handler appear unreliable in a multithreaded Linux process?

## Answer guide

- Signal disposition is process-wide, but each thread has its own signal mask. A process-directed signal can be delivered to any eligible thread; if different threads mask it differently, assuming a particular worker receives it creates nondeterministic behavior.
- Establish signal policy before starting worker threads. A common design blocks administrative signals in all threads and has one dedicated control thread consume them with `sigwaitinfo` or `signalfd`, then coordinates shutdown through ordinary synchronization primitives.
- Keep asynchronous handlers minimal. Most library functions are not async-signal-safe, so logging, allocation, locks, and complex cleanup in a handler can deadlock or corrupt state. Convert the event into a safe control-path action instead.
- Test termination under load, with blocked workers and repeated signals. Standard signals do not queue, so a “one signal equals one event” design loses information; use an explicit control protocol when every event must be recorded.

## References

- [signal(7): masks, pending signals, and threads](https://man7.org/linux/man-pages/man7/signal.7.html)
- [signal-safety(7): async-signal-safe functions](https://man7.org/linux/man-pages/man7/signal-safety.7.html)
- [signalfd(2): read signals from a file descriptor](https://man7.org/linux/man-pages/man2/signalfd.2.html)
- Free book: [POSIX Threads Programming](https://hpc-tutorials.llnl.gov/posix/)
- Further reading (blog): [Thomas Trapp: Graceful shutdowns with POSIX signals](https://thomastrapp.com/blog/signal-handlers-for-multithreaded-cpp/)

## What to learn next

- Official documentation: [man7 signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)
- Manual or specification: [man7 signal-safety(7)](https://man7.org/linux/man-pages/man7/signal-safety.7.html)
- Maintainer or personal blog: [Thomas Trapp — signal handlers](https://thomastrapp.com/blog/signal-handlers-for-multithreaded-cpp/)
- Technical blog: [Red Hat — Linux signals](https://www.redhat.com/en/blog/linux-signals)
- Hands-on guide: [Advanced Bash-Scripting Guide — signals](https://www.gnu.org/software/bash/manual/html_node/Signals.html)
