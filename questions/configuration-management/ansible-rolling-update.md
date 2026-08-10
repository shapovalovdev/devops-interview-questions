---
title: Perform an Ansible rolling configuration update
theme: configuration-management
difficulty: middle
type: scenario
tags: [ansible, automation, configuration-management, deployment, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Perform an Ansible rolling configuration update

How would you apply a service configuration change to a fleet without taking all instances down?

## Answer guide

- Use a bounded `serial` batch and a linear, observable sequence: remove an instance from traffic if required, apply and validate the change, reload or restart it, run a health check, then restore traffic before the next batch.
- Choose batch size from redundancy, recovery time, and error budget—not controller speed. Keep a capacity margin so one failed batch cannot make the remaining service unhealthy.
- Stop on failures and investigate before widening the rollout. `max_fail_percentage` and forks change blast radius but do not make an application-level health check optional.
- Make load-balancer changes explicit and concurrency-safe. Delegated tasks can race when multiple forks write shared control-plane state, so serialize or centralize that operation.

## References

- [Ansible documentation: controlling playbook execution](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html)
- Further reading (blog): [Spacelift: Ansible best practices](https://spacelift.io/blog/ansible-best-practices)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Red Hat Ansible blog](https://www.redhat.com/en/blog/channel/ansible)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
