---
title: "Explain idempotence in an Ansible playbook"
theme: "configuration-management"
difficulty: "middle"
question_ref: "configuration-management/ansible-idempotence.md"
tags: [ansible, automation, configuration-management, reliability]
why: "An idempotent automation run behaves predictably. If a task executes twice, it must not mutate the target or trigger duplicate changes. This ensures that scheduled runs and retries can occur safely without risk of configuration drift or service interruption."
checklist:
  - "Configure Ansible playbook with check mode and diff mode enabled."
  - "Refactor raw shell/command modules to use state-aware Ansible modules (file, copy, apt)."
  - "Add changed_when rules to remaining command/shell tasks to prevent false changes."
  - "Verify idempotency: Running the playbook twice in succession returns changed=0."
---

# Lab: Ansible Idempotency and Convergent States

## Instructions
1. Clone your local setup roles repository. Identify all occurrences of raw `shell` or `command` tasks in your roles (`webapp`, `postgresql`, `router`).
2. Replace these tasks with native Ansible state-aware modules:
   * Use `ansible.builtin.copy` or `ansible.builtin.template` instead of `shell: echo "..." > config`.
   * Use `ansible.builtin.apt` instead of `command: apt-get install`.
3. For tasks that must run shell commands, add explicit guards:
   * Use the `creates` or `removes` arguments to check if file outputs exist before running.
   * Add a `changed_when` conditional based on command output or exit code.
4. Run the full playbook in **Check Mode** (`--check --diff`) to review pending mutations before committing.
5. Execute the playbook twice on a disposable virtual machine. Validate that the second run returns exactly `changed=0`.
