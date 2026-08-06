---
title: Explain plays, tasks, and modules in Ansible
theme: configuration-management
difficulty: junior
type: theory
tags: [ansible, automation, configuration-management]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_playbook.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain plays, tasks, and modules in Ansible

How do plays, tasks, and modules work together in an Ansible playbook?

## Answer guide

- A playbook is YAML containing plays. Each play selects inventory hosts and lists ordered tasks; a task invokes a module or action to move a target toward a declared result.
- Prefer fully qualified, state-aware modules such as package, service, template, and user over arbitrary shell commands. Modules expose meaningful inputs and can report whether they changed the managed state.
- Give each task a clear name and keep a play focused on one operational outcome. Split repeated, reusable configuration into roles rather than creating one unreviewable site playbook.
- Task order is observable behavior. An imperative sequence can still leave partial state after a failure, so identify prerequisites, validate inputs, and include rollback or repair steps for consequential changes.

## References

- [Ansible documentation: creating a playbook](https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_playbook.html)
- Further reading (blog): [Red Hat: how Ansible playbooks work](https://www.redhat.com/en/blog/ansible-playbooks)
