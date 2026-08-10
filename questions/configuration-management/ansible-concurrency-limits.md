---
title: Set safe Ansible concurrency for a fleet change
theme: configuration-management
difficulty: senior
type: troubleshooting
tags: [ansible, automation, configuration-management, reliability, troubleshooting]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set safe Ansible concurrency for a fleet change

An Ansible controller overloads targets and a shared API during a fleet run. How do you correct it?

## Answer guide

- Reduce forks and use `serial` to bound how many hosts progress through a disruptive play at once. Apply `throttle` to individual tasks that contend for a shared service even when other tasks can remain parallel.
- Size concurrency using measured target capacity, API quotas, connection limits, and service redundancy. Start with a canary batch and widen only after technical and service-level health checks pass.
- Inspect strategy choice carefully: the default linear strategy coordinates task stages, while the free strategy lets hosts progress independently and can make shared side effects harder to reason about.
- More parallelism shortens elapsed time but increases blast radius and hides causality during failures. Rate-limit retries and record per-batch results so a controller retry does not compound load.

## References

- [Ansible documentation: playbook strategies and execution controls](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html)
- Further reading (blog): [Spacelift: improve Ansible performance](https://spacelift.io/blog/how-to-improve-ansible-performance)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible community package documentation](https://docs.ansible.com/ansible/latest/community/)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Red Hat Ansible blog](https://www.redhat.com/en/blog/channel/ansible)
- Hands-on guide: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
