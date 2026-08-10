---
title: Design a graceful Linux service shutdown
theme: linux
difficulty: junior
type: scenario
tags: [linux, reliability, deployment]
sources:
  - url: https://man7.org/linux/man-pages/man7/signal.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a graceful Linux service shutdown

What should a Linux service do when it receives a termination request during deployment?

## Answer guide

- Treat `SIGTERM` as a request to begin controlled shutdown: stop accepting new work, allow bounded in-flight work to finish or transfer it safely, flush durable state, then exit with a meaningful status.
- `SIGKILL` cannot be caught, blocked, or ignored, so it is a last-resort deadline mechanism rather than a graceful-shutdown hook. The supervisor’s timeout must exceed the service’s documented drain time but remain bounded to protect rollout and recovery.
- Test shutdown under live connections and slow dependencies. Ensure the load balancer removes the instance before the process exits, and make cleanup idempotent because signals, retries, and abrupt termination can race.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [signal(7): signal dispositions and delivery](https://man7.org/linux/man-pages/man7/signal.7.html)
- Further reading: [systemd.service: service stop behavior](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)

## What to learn next

- Official documentation: [systemd kill behaviour](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- Manual or specification: [systemd.service(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Maintainer or personal blog: [Lennart Poettering — systemd and Linux articles](https://0pointer.net/blog/)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora guide to systemd](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/)
