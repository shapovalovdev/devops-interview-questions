---
title: "Diagnose a systemd service that repeatedly fails"
theme: "linux"
difficulty: "middle"
question_ref: "linux/systemd-service-failure.md"
tags: [linux, debugging, troubleshooting, lfcs]
why: "Linux system processes are managed through systemd unit configurations. If a service crashes or rate-limits, you must be able to navigate dependencies, file sockets, environment contexts, and boot journals to isolate unit flaws from runtime exceptions."
checklist:
  - "Inspect unit status and identify the exit status using systemctl status."
  - "Query systemd journals for the target unit, capturing the initial boot-up error."
  - "Create a custom systemd unit configuration file with Restart parameters."
  - "Enable, start, and verify the service lifecycle states using systemctl."
---

# Lab: Troubleshooting and Managing systemd Services

## Instructions
1. Navigate to the application sandbox node `vm3-app`.
2. Inspect the Flask application's `app.service` status using `systemctl status app.service`. Identify the unit result and exit code if the service has crashed.
3. Review log logs using `journalctl -u app.service -e`. Note the startup context, dependency state, and initial traceback.
4. Modify the service unit configuration `/etc/systemd/system/app.service`:
   * Set `Restart=on-failure` and `RestartSec=5s` to configure recovery guardrails.
   * Verify permissions, executable path (`ExecStart`), and `WorkingDirectory`.
5. Run `systemctl daemon-reload` to load the updated configuration.
6. Enable and start the service, then verify that it remains in the `active (running)` state.
