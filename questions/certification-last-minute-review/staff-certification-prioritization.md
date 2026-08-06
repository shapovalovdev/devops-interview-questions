---
title: Prioritize certification review under a two-hour deadline
theme: certification-last-minute-review
difficulty: staff
type: scenario
tags: [kubernetes, cka, ckad, cks, kcna, reliability]
sources:
  - url: https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prioritize certification review under a two-hour deadline

How should an experienced engineer choose what to review when little time remains?

## Answer guide

- Start from the current official curriculum and your own observed gaps, not recalled or leaked items. Allocate short practice blocks to high-frequency operational primitives: workload inspection, scheduling, networking, storage, RBAC, and incident diagnosis.
- Use a timed loop: state the hypothesis, run a read-only command, make one manifest change, then verify the observable result. This reinforces safe command sequencing rather than memorising fragile command strings.
- Stop expanding scope when a topic has a repeatable workflow and move to a weak domain. Protect sleep, environment setup, identity/context checks, and calm error reading; those reduce avoidable mistakes more reliably than last-minute breadth.

## References

- [Linux Foundation: CKA certification](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- Further reading (blog): [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## What to learn next

- Official documentation: [CKA certification curriculum](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- Manual or specification: [Kubernetes documentation](https://kubernetes.io/docs/home/)
- Maintainer or personal blog: [Kelsey Hightower — Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- Technical blog: [CNCF — Kubernetes training](https://www.cncf.io/training/)
- Hands-on guide: [Kubernetes basics tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
