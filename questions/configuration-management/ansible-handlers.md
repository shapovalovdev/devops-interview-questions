---
title: Use Ansible handlers for service reloads
theme: configuration-management
difficulty: junior
type: theory
tags: [ansible, automation, configuration-management, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use Ansible handlers for service reloads

When should an Ansible task notify a handler instead of restarting a service directly?

## Answer guide

- A handler is a task run after notification, normally once at the end of a play. Use it for actions such as reload or restart that are required only when configuration actually changed.
- Notify a clearly named handler from every task that can affect the same service. This avoids repeated restarts when several files change in one run and keeps mutation tied to its cause.
- Use `meta: flush_handlers` only where subsequent tasks truly require the new state. Early flushing changes ordering and can create an outage if later validation fails.
- A handler is not a transaction. If a later task fails, a deferred restart may be skipped or inappropriate; validate configuration first and explicitly design remediation for partial rollout failures.
- Refresh-on-change exists across engines: Puppet resources trigger service reloads through `notify`/`subscribe` refresh events, so defer-the-restart-to-the-thing-that-changed is the portable pattern, with the same starvation risk when a later resource fails.

## References

- [Ansible documentation: handlers](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html)
- Further reading (blog): [Spacelift: Ansible configuration management](https://spacelift.io/blog/ansible-configuration-management)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
