---
title: "Configure database readiness wait-for logic in Ansible"
theme: "configuration-management"
difficulty: "middle"
question_ref: "configuration-management/ansible-role-design.md"
tags: [ansible, automation, configuration-management, reliability]
why: "Distributed services start up at different speeds. If the application server starts up before the database is ready, it will fail to connect and crash. Automating readiness checks via Ansible ensures playbooks execute smoothly without dependency race conditions."
checklist:
  - "Configure wait_for task in the Ansible webapp role targeting database port 5432."
  - "Configure wait_for timeout and interval delays for robust execution."
  - "Verify playbook runs: Test database availability checks during a clean startup simulation."
---

# Lab: Ansible Database Readiness Wait-For Logic

## Instructions
1. Open your web application deployment role in the Ansible repository.
2. Before the task that starts the Flask web service, add an `ansible.builtin.wait_for` task.
3. Configure the task to target:
   * Host: `{{ db_host }}` (points to `vm2-db`'s IP address `192.168.56.20`).
   * Port: `5432` (PostgreSQL standard port).
   * Timeout: `60` seconds.
   * State: `started` (waits for the port to open).
4. Run the full playbook and verify that it pauses during startup until the database service is fully ready to accept sockets, then proceeds to spawn the application service.
