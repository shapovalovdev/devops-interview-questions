---
title: Use process priorities without hiding a capacity problem
theme: linux
difficulty: junior
type: scenario
tags: [linux, reliability, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man7/sched.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use process priorities without hiding a capacity problem

When can nice levels help a production host, and what should you verify before changing them?

## Answer guide

- Nice values influence scheduling priority for normal scheduling policies; they do not reserve CPU, fix blocked I/O, or guarantee latency. Raising priority generally requires privilege because it can deny CPU to other work.
- Use lower priority for explicitly best-effort jobs only after identifying CPU contention. Protect latency-critical work with capacity, workload isolation, and cgroup controls where appropriate rather than relying on one global host priority tweak.
- Measure scheduling delay and user impact before and after the change. Real-time policies are especially risky: an incorrectly configured real-time task can starve ordinary work and impair host recovery.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [sched(7): Linux scheduling overview](https://man7.org/linux/man-pages/man7/sched.7.html)
- Further reading: [nice(1): adjust scheduling priority](https://man7.org/linux/man-pages/man1/nice.1.html)
