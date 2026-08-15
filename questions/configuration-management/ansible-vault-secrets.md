---
title: Protect secrets used by Ansible automation
theme: configuration-management
difficulty: middle
type: scenario
tags: [ansible, automation, configuration-management, security]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/vault_guide/vault.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Protect secrets used by Ansible automation

How should a team protect secrets consumed by Ansible playbooks?

## Answer guide

- Store encrypted values with Ansible Vault only when that fits the organization’s secret-management model; keep vault passwords outside the repository and restrict decryption capability to the deployment identity.
- Prefer a dedicated secret manager for dynamic, rotated, or broadly shared credentials, retrieving only the secret needed at execution time. Keep secret references distinct from ordinary configuration variables.
- Prevent disclosure through `no_log` where suitable, restricted CI logs, encrypted transport, and careful use of `--diff`. Test that failed tasks and debugging output do not print sensitive values.
- Encryption at rest does not replace rotation, least privilege, auditing, or revocation. Plan what happens if a vault password, controller, or rendered host configuration is compromised.
- Encrypted-in-repo secrets have direct equivalents: SOPS-encrypted files decrypted only by the deployment identity, or git-crypt, make the same trade — and carry the same rule that encryption at rest is not rotation, least privilege, or revocation.

## References

- [Ansible documentation: protecting sensitive data with Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/vault.html)
- Further reading (blog): [Spacelift: Ansible security automation](https://spacelift.io/blog/ansible-security)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
