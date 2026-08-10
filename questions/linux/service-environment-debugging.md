---
title: Debug an application that works in a shell but fails as a service
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, debugging, troubleshooting, lfcs]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug an application that works in a shell but fails as a service

An executable succeeds interactively but fails under systemd. What differences do you compare?

## Answer guide

- Compare the service’s executable path, user/group, working directory, environment, inherited file descriptors, resource limits, and filesystem/network sandboxing with the interactive session. A shell profile is not normally the service environment.
- Inspect the unit’s effective settings and journaled failure, then reproduce with the service identity and minimal environment where safe. Pay particular attention to credentials, writable paths, locale, `PATH`, and access denied by service hardening.
- Make dependencies explicit in the unit or application configuration rather than relying on a login shell. Keep secrets out of broad environment dumps and verify the hardened configuration still permits required operations.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [systemd.exec: execution environment and sandboxing](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html)
- Further reading: [systemd.service: service unit configuration](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)

## What to learn next

- Official documentation: [systemd.exec(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html)
- Manual or specification: [systemd.service(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Maintainer or personal blog: [Lennart Poettering — systemd and Linux articles](https://0pointer.net/blog/)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora guide to systemd](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/)
