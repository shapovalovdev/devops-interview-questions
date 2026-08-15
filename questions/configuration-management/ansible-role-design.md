---
title: Design a reusable Ansible role
theme: configuration-management
difficulty: middle
type: scenario
tags: [ansible, automation, configuration-management, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a reusable Ansible role

What makes an Ansible role reusable without making it impossible to understand?

## Answer guide

- A role packages related tasks, defaults, handlers, templates, files, and metadata behind a documented input contract. It should represent one cohesive capability, such as configuring a web service, rather than an entire environment.
- Provide safe defaults and explicit required variables; validate inputs and document supported platforms and side effects. Keep role variables narrow so callers can reason about what customization changes.
- Separate high-precedence implementation constants from user-overridable defaults deliberately. Unbounded variable indirection and hidden dependencies make a role difficult to test and unsafe to upgrade.
- Test the role against each supported platform and version. Version it like an internal product, because changing a default, handler, or variable name can alter many fleets at once.
- A versioned, interface-driven role is the configuration-management-generic unit of reuse: Puppet modules and Terraform modules make the same safe-defaults-versus-explicit-inputs trade, and breaking a default breaks every consumer in all three.

## References

- [Ansible documentation: roles](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
- Further reading (blog): [Spacelift: Ansible best practices](https://spacelift.io/blog/ansible-best-practices)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
