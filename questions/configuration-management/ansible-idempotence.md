---
title: Explain idempotence in an Ansible playbook
theme: configuration-management
difficulty: middle
type: theory
tags: [ansible, automation, configuration-management, reliability]
---

# Explain idempotence in an Ansible playbook

What does it mean for an Ansible task to be idempotent, and why is that property important in operations?

## Answer guide

- Repeated application reaches the desired state without unnecessary additional changes.
- Idempotence makes retries, drift correction, and change review safer.
- Use state-aware modules where possible; make imperative commands explicitly guarded.
