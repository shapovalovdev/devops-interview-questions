---
title: Standardize configuration management without blocking teams
theme: configuration-management
difficulty: staff
type: scenario
tags: [ansible, automation, configuration-management, platform-engineering, governance, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Standardize configuration management without blocking teams

How would you standardize configuration management across teams while preserving delivery autonomy?

## Answer guide

- Define a small supported platform: versioned role interfaces, approved collections, inventory conventions, test templates, and execution policies. Offer it as a product with documentation, migration help, and compatibility commitments.
- Standardize outcomes that reduce shared risk—identity, secret handling, auditability, rollback evidence, and service health checks—while allowing teams to own application-specific desired state.
- Track adoption, unsupported customizations, time-to-change, and incidents from configuration drift. Use these metrics and user feedback to decide which abstractions deserve investment.
- A forced rewrite often freezes delivery and creates shadow automation. Phase standards in with interoperability, deprecation dates, and justified exception paths; remove old paths only after replacement capabilities are proven.

## References

- [Ansible documentation: roles and reusable content](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
- Further reading (blog): [Spacelift: Ansible configuration management](https://spacelift.io/blog/ansible-configuration-management)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
