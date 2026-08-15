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
- State-aware modules are this model's resource types: Terraform resources and Puppet declared resources play the same converge-and-report role, and each tool's shell escape — provisioners, `exec` — loses change reporting the same way `command` does here.

## References

- [Ansible documentation: creating a playbook](https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_playbook.html)
- Further reading (blog): [Spacelift: Ansible configuration management](https://spacelift.io/blog/ansible-configuration-management)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
