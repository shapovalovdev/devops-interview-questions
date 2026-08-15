---
title: Gather and use Ansible facts deliberately
theme: configuration-management
difficulty: middle
type: theory
tags: [ansible, automation, configuration-management, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_vars_facts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Gather and use Ansible facts deliberately

What are Ansible facts, and what are the operational trade-offs of using them?

## Answer guide

- Facts are data Ansible gathers or sets about managed hosts and exposes as variables. They allow a role to adapt to operating system, network, or hardware characteristics instead of duplicating task files.
- Gather only facts required by the play or use subsets/caching where fleet scale makes collection expensive. Treat cached facts as potentially stale when a change depends on current state.
- Use explicit validation before branching on a fact. An absent package, restricted connection, or platform difference can produce missing or differently shaped data.
- Facts are not a trust boundary: remote systems provide much of the data. Do not use an unverified fact alone to grant access or make a destructive decision, and avoid logging facts that may reveal sensitive topology.
- Automatic node data has named equivalents: Chef gathers it with Ohai and Salt exposes grains — carrying the same caution that remote-provided data is input to validate, never a trust boundary.

## References

- [Ansible documentation: vars, facts, and magic variables](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_vars_facts.html)
- Further reading (blog): [Spacelift: Ansible performance and fact gathering](https://spacelift.io/blog/how-to-improve-ansible-performance)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
