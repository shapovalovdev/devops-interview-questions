---
title: Design a graceful shutdown contract
theme: processes
difficulty: senior
type: scenario
tags: [linux, processes, signals, reliability, deployment]
sources:
  - url: https://man7.org/linux/man-pages/man7/signal.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a graceful shutdown contract

Design a graceful-shutdown contract for a service with HTTP requests and background jobs.

## Answer guide

- Define a bounded sequence: stop accepting new work, remove readiness or traffic registration, allow in-flight work a documented deadline, checkpoint or hand off durable jobs, close listeners, flush only necessary state, and exit with an observable result. Idempotency is essential because supervisors may resend termination signals.
- Translate that contract through every layer: load balancer drain timing, orchestrator or systemd stop signal and timeout, application signal handling, worker queues, database transaction limits, and client retry policy. A graceful application cannot compensate for a proxy that continues sending traffic.
- Choose failure semantics explicitly. At deadline, either abort work that is safely retryable or extend through an approved operator decision; never silently claim completion for work whose external side effect is uncertain. Measure rejected requests, drain duration, forced kills, and duplicate-job rate.
- Test rollouts, node termination, configuration reloads, and dependency failure under production-like load. SIGKILL or timeout is a safety backstop, not evidence that graceful shutdown works.

## References

- [signal(7): signal semantics](https://man7.org/linux/man-pages/man7/signal.7.html)
- [systemd.service: timeout and stop behavior](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd.kill: KillSignal and KillMode](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- Free book: [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Kelsey Hightower: Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [man7 signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)
- Manual or specification: [systemd.kill manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [Google SRE — handling overload](https://sre.google/sre-book/handling-overload/)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
