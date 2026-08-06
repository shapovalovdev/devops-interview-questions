---
title: Explain an Ansible inventory and host groups
theme: configuration-management
difficulty: junior
type: theory
tags: [ansible, automation, configuration-management]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain an Ansible inventory and host groups

What is an Ansible inventory, and how should host groups be used safely?

## Answer guide

- An inventory maps names used by automation to managed hosts and can place those hosts in groups. A play targets a host pattern, so groups let one desired-state definition apply consistently to a service or environment.
- Keep membership authoritative and reviewable: generate dynamic inventory from a trusted platform or maintain static inventory in version control. Put shared settings in group variables and genuinely host-specific settings in host variables.
- Do not use broad groups such as `all` for routine production changes. Limit runs with explicit environment and service patterns, then inspect `--list-hosts` before an important execution.
- Inventory is an access boundary as well as an address book. Stale membership can apply a valid change to the wrong host, while duplicate or conflicting group variables make the intended state difficult to predict.

## References

- [Ansible documentation: inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html)
- Further reading (blog): [Red Hat: getting started with Ansible inventory](https://www.redhat.com/en/blog/ansible-inventory-files)
