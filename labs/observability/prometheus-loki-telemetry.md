---
title: "Monitoring and logs on an existing stand: Prometheus + Alertmanager + Loki + Grafana"
theme: "observability"
difficulty: "middle"
question_ref: "observability/build-an-actionable-alert.md"
tags: [observability, monitoring, logging, prometheus, ansible]
why: "Monitoring is named in nearly every infrastructure job description and logging in most; Loki covers the practical logging side more cheaply and simply than ELK, and correlating metrics with logs in a single dashboard is a standing interview theme. The lab closes the common gap for anyone arriving with Zabbix or Grafana experience but only pet-level Prometheus: transferring that experience onto the Prometheus stack and learning to tie an alert to its cause through logs."
checklist:
  - "Prometheus and node_exporter are up on all 3 VMs; every target shows UP in /targets."
  - "Scrape configs are declared declaratively (an Ansible role or docker-compose) and reproduce on a second run."
  - "2-3 alert rules are configured: instance down, disk usage > 85%, Flask 5xx/latency; the rules load without errors (check /rules)."
  - "Alertmanager delivers an alert to a real channel (email/webhook/Telegram), not only to the UI."
  - "Every alert has been proven by generating a real event: stop an exporter, fill a disk, generate 5xx."
  - "Loki + Promtail are running; journald and the Flask/PostgreSQL logs genuinely arrive in Loki."
  - "LogQL queries work: filter by service, grep for an error, count the rate over an interval."
  - "A single Grafana dashboard shows metrics and logs side by side; correlation by time works."
  - "Break-and-fix: a downed exporter raises an alert, and the cause is found from the logs in Loki rather than from a hint."
  - "A repeat deploy through Ansible (or docker-compose up) is idempotent: nothing changed, and containers are not recreated without reason."
---

# Lab: Monitoring and logs on an existing stand: Prometheus + Alertmanager + Loki + Grafana

## Context and environment

The stand from the previous labs: 3 Ubuntu VMs — `vm1` (Flask application + nginx), `vm2` (PostgreSQL), `vm3` (Ansible control + app host). Everything is managed through Ansible. The task is to fit a full observability stack onto a live stand without breaking the application.

**The key decision you have to defend:** deploy the stack through an Ansible role (systemd services) or through docker-compose on a dedicated node. Both have a price: Ansible means more roles and templates but keeps one management story for the whole stand; docker-compose is faster to stand up but introduces a second deployment system. Argue the choice rather than taking one by default.

Time for the lab: 6-8 hours. Machines: 3 VMs, 2 vCPU / 2-4 GB RAM each.

---

## Exercise 1: Prometheus + node_exporter on all 3 VMs

1. Install Prometheus (the server) and node_exporter (on all 3 VMs) by your chosen method.
2. Write the scrape config: static targets for all 3 VMs (`:9100`), plus the Flask app metrics (`/metrics`, or through an exporter — if Flask does not expose them, add `prometheus_client` to the application or put blackbox_exporter in front of the HTTP endpoint).
3. Check: `http://<prometheus>:9090/targets` — every target UP.
4. Arrange things so the target list does not have to be edited by hand when a VM is added (Ansible inventory → a `prometheus.yml.j2` template, or file-based SD).

## Exercise 2: Meaningful alerts through Alertmanager

1. Stand up Alertmanager and connect it to Prometheus.
2. Write 2-3 alert rules, each of which passes the "actionable alert" test (see question_ref):
   - `instance down` — `up == 0` for more than 1-2 minutes;
   - disk usage > 85% — `node_filesystem_avail_bytes / node_filesystem_size_bytes`;
   - Flask 5xx rate or p95 latency — from the application metrics.
3. For each alert: a severity, a description carrying the first diagnostic step, and routing in Alertmanager (for example, critical → Telegram/webhook, warning → email).
4. **Checking is not done by eye:** every alert must fire from a real event (see Exercise 5). An alert that has never fired counts as one that does not exist.

## Exercise 3: Loki + Promtail: journald and service logs

1. Stand up Loki (single-binary is enough) and Promtail on each VM.
2. Configure Promtail: a `journal` scrape (the Flask, PostgreSQL and node_exporter units) plus the file logs of Flask/nginx if they are written to files. Add the labels `host`, `unit`, `service`.
3. Confirm the data arrives: query in Grafana Explore — `{job="journal", host="vm1"}` and `{service="flask"}`.
4. Answer the defence question: why labels in Loki are not the same thing as labels in Prometheus, and what happens to Loki under high-cardinality labels such as user_id.

## Exercise 4: A single Grafana dashboard: metrics and logs side by side

1. Connect Grafana to both sources: Prometheus and Loki.
2. Build one dashboard for the stand: CPU/memory/disk per VM, Flask availability, 5xx rate — and beside them a log panel showing the application logs over the same time window.
3. Check the correlation: during the incident from Exercise 5, one click should show the metric spike and the corresponding log lines in the same time window.
4. Practise ad-hoc LogQL: find every 5xx in the last hour, count the error `rate` per service, find one specific traceback.

## Exercise 5: Break-and-fix (the bridge to chaos-sandbox Phase 2)

1. Drop node_exporter on one of the VMs: `sudo systemctl stop node_exporter`.
2. Walk the whole response cycle: the alert arrives → Grafana shows which target disappeared → the journald logs in Loki (`{unit="node_exporter"}`) give you the reason it stopped.
3. Repeat with a harder scenario: break Flask so that nginx returns 5xx (or generate errors by loading the broken backend) — the 5xx alert must arrive, and the cause must be found in the logs rather than guessed.
4. Record the TTR (time to recovery) for both incidents. This is direct preparation for chaos-sandbox Phase 2: reconstructing an incident from Grafana/Loki and writing a blameless post-mortem.
5. Fix it. Confirm the resolved alert arrives through the same channel.

## Exercise 6: Idempotence of the whole monitoring stack

1. The entire monitoring stack must come up from scratch on clean VMs in a single Ansible playbook run (or `docker-compose up -d`).
2. Run the deploy again against the live stand: services must not restart, configs must not change, dashboards must not duplicate. Grafana dashboards and data sources are declarative (provisioning, not clicked into the UI).
3. Check: `ansible-playbook ... --check --diff` shows no changes; the alert rules and Promtail configs are templated.
4. Defence: what happens to the monitoring stack when the stand is recreated from nothing, and where you recorded that in code rather than in your memory.

---

## Completion criteria

- Every checklist item is closed with a screenshot or command output.
- The Ansible vs docker-compose choice is argued (at least 2 sound arguments for, and 1 against, your own choice).
- Exercise 5 is shown end to end: alert → dashboard → logs → fix → resolved.
