---
title: Create a risk-based configuration change model
theme: configuration-management
difficulty: staff
type: scenario
tags: [ansible, automation, configuration-management, governance, deployment, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create a risk-based configuration change model

How would you scale configuration-change controls across both low-risk and high-risk services?

## Answer guide

- Classify changes by blast radius, reversibility, data and security impact, and service criticality—not by the team submitting them. Attach controls such as peer review, tests, approval, canary size, and rollback evidence to that classification.
- Make the routine safe path fast: automated validation, small batches, observable health checks, and a durable audit record should be default capabilities rather than special paperwork.
- Require higher assurance for identity, network, persistence, and shared-platform changes. Define who can accept residual risk and what evidence is needed before and after deployment.
- Avoid a universal approval queue that delays urgent repairs while offering little technical assurance. Review outcomes—incidents, rollbacks, and exceptions—and tune the model when controls do not predict real risk.

## References

- [Ansible documentation: controlling playbook execution](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html)
- Further reading (blog): [Spacelift: Ansible best practices](https://spacelift.io/blog/ansible-best-practices)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Red Hat Ansible blog](https://www.redhat.com/en/blog/channel/ansible)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
