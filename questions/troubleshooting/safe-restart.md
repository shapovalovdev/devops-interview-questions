---
title: Decide whether a restart is a safe diagnostic action
theme: troubleshooting
difficulty: junior
type: scenario
tags: [troubleshooting, recovery, deployment, reliability]
sources:
  - url: https://sre.google/sre-book/effective-troubleshooting/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Decide whether a restart is a safe diagnostic action

## Answer guide

- Treat a restart as a mitigation with side effects, not a root-cause analysis. Check quorum, replica health, connection draining, persistent state, startup migrations, and whether the component is already crash-looping.
- Capture logs, metrics, process state, and configuration before restarting when that evidence is cheap to preserve. Restart one instance or an isolated canary first, then verify the defined user-facing success metric and error budget impact.
- Have a rollback and escalation path. Restarting every replica together can turn a partial degradation into an outage, discard forensic evidence, or overload a recovering dependency through synchronized reconnects.

## References

- [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Google SRE Book — Handling Overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Google Cloud — Graceful shutdown](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Kubernetes termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-flow)
- Hands-on guide: [systemd service manager](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Maintainer or personal blog: [Brendan Gregg’s blog](https://www.brendangregg.com/blog/)
- Technical blog: [Google Cloud blog](https://cloud.google.com/blog/)
