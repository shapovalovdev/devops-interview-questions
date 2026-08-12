---
title: "SRE Chaos Sandbox: Chaos on a Leash"
theme: "sre"
difficulty: "senior"
question_ref: "chaos-engineering/exhaust-disk-and-file-descriptors.md"
tags: [sre, troubleshooting, alerts, monitoring, chaos]
why: "Real SRE operations involve responding to live alarms and diagnosing unknown state changes under pressure. Setting up a time-leashed chaos sandbox teaches how to manage on-call alerts, query journals, isolate latency, and build self-healing service definitions."
checklist:
  - "Clone the devops-chaos-sandbox repository on the app server VM."
  - "Run the installer.sh script with sudo and configure Telegram Webhook credentials."
  - "Verify the chaos-alerts systemd daemon is active and running."
  - "Trigger a manual failure scenario by setting FORCE_CHAOS=1 and running chaos_scheduler.py."
  - "Verify that a downtime alert is delivered to the configured Telegram Chat."
  - "Resolve the outage using the appropriate restoration recipe and verify recovery alerts."
---

# Lab: DevOps Chaos Sandbox (Phase 1)

## Setup & Bootstrap

1. Log in to your application host VM (e.g. `vm3-app` or equivalent sandbox instance).
2. Download and run the automated installer:
   ```bash
   sudo bash -c "$(curl -sSL https://raw.githubusercontent.com/shapovalovdev/devops-chaos-sandbox/main/installer.sh)"
   ```
3. Enter your **Telegram Bot Token**, **Chat ID**, and **Target Application URL** when prompted. The installer will write these to `/etc/chaos-sandbox.env` and set up the systemd timers.
4. Confirm both services are configured:
   ```bash
   systemctl status chaos-alerts.service
   systemctl status chaos-scheduler.timer
   ```

---

## Triage Exercises

### Outage Scenario 1: Port Latency
* **Symptom:** Webpage loading times exceed 5 seconds or requests drop.
* **Diagnosis:**
  1. Inspect network sockets on the VM: `ss -nltp` or test endpoint responsiveness with curl timing headers.
  2. Look for active traffic control queuing disciplines: `tc qdisc show dev lo`.
* **Fix:** Clear latency rules:
  ```bash
  sudo tc qdisc del dev lo root
  ```

### Outage Scenario 2: Service Crash
* **Symptom:** 502 Bad Gateway / Application Unreachable.
* **Diagnosis:**
  1. Check unit state: `systemctl status postgresql` or inspect running Docker containers `docker ps`.
  2. Query logs: `journalctl -u postgresql -e` or `docker logs postgres`.
* **Fix:** Restore the daemon and configure it to auto-restart on failures.

### Outage Scenario 3: Disk Exhaustion
* **Symptom:** Database inserts fail, disk writes blocked, health check fails.
* **Diagnosis:**
  1. Inspect free disk space: `df -h /var/log`.
  2. Locate large temporary files: `sudo find /var/log -type f -size +100M`.
* **Fix:** Delete the junk file `/var/log/system-journal-cache.tmp` to clear headroom.
