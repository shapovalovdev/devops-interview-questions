---
title: Apply least privilege to Ansible privilege escalation
theme: configuration-management
difficulty: senior
type: scenario
tags: [ansible, automation, configuration-management, security, least-privilege]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_privilege_escalation.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply least privilege to Ansible privilege escalation

How would you give automation the elevated access it needs without granting unrestricted root access?

## Answer guide

- Connect with a dedicated automation identity and use `become` only on tasks needing elevated privilege. Limit the remote account and sudo policy to approved commands or service responsibilities where the platform allows it.
- Separate controller credentials, transport authentication, and privilege-escalation credentials. Rotate them independently and ensure logs, process listings, and temporary files do not disclose passwords or tokens.
- Test the exact privilege boundary on each supported platform. PAM, sudo configuration, connection plugins, and temporary-module-file handling can differ across distributions and affect both security and execution.
- Broad passwordless root makes initial automation easy but enlarges blast radius. Pair minimum privilege with reviewed playbooks, audited execution, hardened controllers, and an emergency revocation path.

## References

- [Ansible documentation: privilege escalation](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_privilege_escalation.html)
- Further reading (blog): [Spacelift: Ansible security automation](https://spacelift.io/blog/ansible-security)
