---
title: Design safe configuration drift remediation
theme: configuration-management
difficulty: senior
type: scenario
tags: [ansible, automation, configuration-management, reliability, security, cgoa]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://csrc.nist.gov/pubs/sp/800/128/final
    source_type: standard
    verified_on: 2026-08-16
---

# Design safe configuration drift remediation

How should a team detect and remediate configuration drift without overwriting a necessary emergency change?

## Answer guide

- Define the desired state in reviewed version control, then measure drift with scheduled check-mode reports or purpose-built compliance checks. Classify drift by risk and owner before automatically changing critical systems.
- Investigate whether drift is unauthorized, an unrecorded emergency repair, provider behavior, or an incomplete automation model. Legitimate changes should be incorporated into the source of truth rather than repeatedly overwritten.
- Automate low-risk, reversible convergence with audit records and alerting. Require approval and a canary for changes affecting access, data, network boundaries, or high-availability controls.
- Continuous remediation can fight a human incident response or propagate a bad desired state quickly. Provide pause controls, exception expiry, and post-remediation validation that confirms service behavior as well as file content.
- Drift detection is the model's other half: `terraform plan` against refreshed state reports out-of-band edits and Puppet run reports expose the same divergence — classify-before-converge is identical there, and NIST's configuration-management guidance frames it as baseline monitoring.

## References

- [Ansible documentation: check mode and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- Further reading (blog): [Spacelift: Ansible configuration drift management](https://spacelift.io/blog/ansible-configuration-drift-management)
- [NIST SP 800-128: Configuration Management for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/128/final)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
