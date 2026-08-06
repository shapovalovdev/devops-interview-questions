---
title: Coordinate a configuration change with Ansible delegation
theme: configuration-management
difficulty: middle
type: scenario
tags: [ansible, automation, configuration-management, deployment, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_delegation.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Coordinate a configuration change with Ansible delegation

When should an Ansible task use `delegate_to`, and what can go wrong?

## Answer guide

- Use delegation when a task concerning a target must execute on another system, such as removing that target from a load balancer through a controller API. The original host remains the logical item being processed.
- Combine delegation with a bounded serial rollout when the shared control plane has side effects. Understand that delegated tasks use the delegated host’s connection context unless you explicitly reference the original host through `hostvars`.
- Do not assume delegation serializes shared writes. Multiple forks can still update the same file or API concurrently; use `run_once`, throttling, or an external concurrency control where required.
- Validate both directions of the change: an instance must be removed before a disruptive action and restored only after health checks pass. Failure to restore traffic is an availability incident, not merely an automation error.

## References

- [Ansible documentation: delegation and local actions](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_delegation.html)
- Further reading (blog): [Spacelift: Ansible performance and delegation](https://spacelift.io/blog/how-to-improve-ansible-performance)
