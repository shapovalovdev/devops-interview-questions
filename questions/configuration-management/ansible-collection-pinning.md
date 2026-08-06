---
title: Pin and update Ansible collections safely
theme: configuration-management
difficulty: senior
type: scenario
tags: [ansible, automation, configuration-management, supply-chain, security]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/collections_guide/collections_installing.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Pin and update Ansible collections safely

How should a platform team consume Ansible collections without making production dependent on an unreviewed latest version?

## Answer guide

- Declare collection names and version constraints in a requirements file, resolve them in a controlled build, and promote the tested artifact through environments. Use fully qualified collection names so module provenance is clear.
- Review release notes, dependency changes, supported Ansible-core versions, and any plugin behavior that affects credentials, inventory, or remote execution. Test upgrades against representative infrastructure before rollout.
- Use an approved internal mirror or verified automation-hub policy when supply-chain controls require it. The controller must not install arbitrary content during a production run.
- Pinning alone is not a security strategy: a pinned vulnerable version remains vulnerable. Maintain an update cadence, integrity/provenance checks, and a fast rollback path for a faulty collection release.

## References

- [Ansible documentation: installing collections](https://docs.ansible.com/projects/ansible/latest/collections_guide/collections_installing.html)
- Further reading (blog): [Spacelift: Ansible best practices](https://spacelift.io/blog/ansible-best-practices)
