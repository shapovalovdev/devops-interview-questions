---
title: Handle Ansible task failures without concealing drift
theme: configuration-management
difficulty: middle
type: troubleshooting
tags: [ansible, automation, configuration-management, troubleshooting, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_error_handling.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle Ansible task failures without concealing drift

A configuration task fails on part of a fleet. How should the playbook handle that failure?

## Answer guide

- Let unexpected failures fail visibly and capture enough context to diagnose the host, task, and input. Use blocks with `rescue` and `always` for a deliberately designed cleanup, rollback, or evidence-collection path.
- Define `failed_when` and `changed_when` only when the module’s normal result cannot express the real contract. Base those conditions on stable result fields, not fragile output text.
- Do not set `ignore_errors: true` to keep a rollout green. That can hide drift and let later tasks run against an invalid prerequisite; record exceptions and decide whether to stop the batch.
- A rescue block does not restore every side effect. Make risky changes incrementally, validate after each batch, and keep a tested manual recovery procedure for partial success.

## References

- [Ansible documentation: error handling in playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_error_handling.html)
- Further reading (blog): [Red Hat: Ansible block and rescue patterns](https://www.redhat.com/en/blog/ansible-block-rescue-always)
