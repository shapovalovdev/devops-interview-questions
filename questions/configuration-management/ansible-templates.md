---
title: Deliver a configuration file with an Ansible template
theme: configuration-management
difficulty: junior
type: scenario
tags: [ansible, automation, configuration-management, reliability]
sources:
  - url: https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/template_module.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Deliver a configuration file with an Ansible template

How would you deliver a service configuration file that differs by environment?

## Answer guide

- Keep a versioned Jinja template for stable structure and pass environment-specific values through a small, validated variable interface. Use the template module to manage destination ownership, permissions, and content change detection.
- Validate the generated configuration before activating it when the service offers a syntax checker. Notify a restart or reload handler only after the file changes and validation succeeds.
- Do not put secret values in a template rendered to an uncontrolled workspace, in logs, or in a diff. Disable sensitive diffs and use an appropriate secret-delivery mechanism.
- Templating makes syntax easy to vary but can hide semantic differences. Test representative production values and make a bad configuration recoverable through a known previous version or rollback path.
- Template-then-validate-then-reload is portable: Puppet's EPP templates notify the managed service the same way, and the failure mode — valid syntax rendering a semantically wrong file — is engine-independent, so test rendered output with production-like values.

## References

- [Ansible documentation: template module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/template_module.html)
- Further reading (blog): [Spacelift: Ansible configuration management](https://spacelift.io/blog/ansible-configuration-management)

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible examples](https://github.com/ansible/ansible-examples)
