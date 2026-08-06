---
title: Explain idempotence in an Ansible playbook
theme: configuration-management
difficulty: middle
type: theory
tags: [ansible, automation, configuration-management, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain idempotence in an Ansible playbook

What does it mean for an Ansible task to be idempotent, and why is that property important in operations?

## Answer guide

- An idempotent task converges a managed system on its declared desired state: after the first successful run, an unchanged input should report no change and should not keep altering the target.
- That property makes retries, scheduled drift correction, and change review safer because a transient controller failure does not turn a second run into a second mutation.
- Prefer state-aware modules and declare `state`; commands and shell tasks need an explicit guard such as `creates`, `removes`, or a reliable `changed_when`. Check mode is useful evidence, but not proof—modules and external commands can have limits.
- Do not hide non-idempotence by forcing `changed_when: false`: it loses audit signal and can conceal a repeated side effect. Test a play twice against a disposable target and investigate an unexpected second change.

## References

- [Ansible documentation: check mode and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- Further reading (blog): [Red Hat: Ansible idempotency](https://www.redhat.com/en/blog/ansible-when-true)
