# Troubleshooting: related materials

Use these public resources to practise a hypothesis-driven incident response. The Google SRE book is legally available online under CC BY-NC-N 4.0; it is a free book, not a download of a commercial text.

## What to learn next

- Official documentation: [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance material](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

Begin the way a page begins — alert context, then impact — because those two
habits preserve every option the rest of the Theme depends on.

1. [Read alert context before escalating](../../questions/troubleshooting/read-alert-context.html)
    — Begin the way a page begins: what the alert measures, over what window.
2. [Establish impact before changing a failing service](../../questions/troubleshooting/establish-impact.html)
    — Impact is established before changing anything, or every option is lost.
3. [Isolate a suspected change without guessing](../../questions/troubleshooting/isolate-change.html)
    — Isolating a suspected change without guessing is the first diagnostic act.
4. [Decide whether a restart is a safe diagnostic action](../../questions/troubleshooting/safe-restart.html)
    — Whether a restart is a safe diagnostic action is decided, never assumed.
5. [Contain a bad deployment while protecting evidence](../../questions/troubleshooting/handle-bad-deployment.html)
    — Containing a bad deployment while protecting evidence keeps both options
    open.
6. [Trace a dependency failure across service boundaries](../../questions/troubleshooting/trace-dependency-failure.html)
    — The dependency failure is traced across the boundaries it hides behind.
7. [Diagnose DNS failure from client to authoritative data](../../questions/troubleshooting/diagnose-dns.html)
    — The specialist diagnoses open with DNS from client to authoritative data.
8. [Diagnose a TLS handshake failure safely](../../questions/troubleshooting/debug-tls.html)
    — The TLS handshake is diagnosed safely rather than disabled in frustration.
9. [Debug an authentication failure without weakening access control](../../questions/troubleshooting/debug-auth-failure.html)
    — Authentication is debugged without weakening the access control around it.
10. [Debug latency without averaging away the incident](../../questions/troubleshooting/debug-latency.html)
    — Latency is debugged without averaging away the incident.
11. [Investigate a production data mismatch safely](../../questions/troubleshooting/investigate-data-mismatch.html)
    — The data mismatch is investigated safely across its stores.
12. [Triage a growing asynchronous work backlog](../../questions/troubleshooting/debug-queue-backlog.html)
    — The growing backlog is the asynchronous tier's fever chart.
13. [Debug an observability gap during an active incident](../../questions/troubleshooting/debug-observability-gap.html)
    — The observability gap mid-incident is a failure in its own right.
14. [Stop a cascading failure while preserving useful traffic](../../questions/troubleshooting/reduce-cascading-failure.html)
    — Stopping the cascade while preserving useful traffic is the specialists'
    synthesis.
15. [Triage an error-budget burn alert](../../questions/troubleshooting/debug-error-budget.html)
    — The burn alert is triaged by validating its own arithmetic first.
16. [Verify recovery rather than trusting a green deployment](../../questions/troubleshooting/verify-recovery.html)
    — Recovery is verified rather than trusted from a green dashboard.
17. [Design reliable multi-team incident handoffs](../../questions/troubleshooting/design-multi-team-handoff.html)
    — The final tier opens with handoffs that survive shift changes.
18. [Lead a severe incident without uncontrolled changes](../../questions/troubleshooting/lead-sev-incident.html)
    — Leading a severe incident means controlling the changes, not just the
    communications.
19. [Govern risky mitigations during a business-critical outage](../../questions/troubleshooting/govern-risky-mitigation.html)
    — Risky mitigations are governed during the business-critical outage itself.
20. [Triage a regional outage with a safe traffic strategy](../../questions/troubleshooting/triage-regional-outage.html)
    — The regional outage pairs diagnosis with a safe traffic strategy.
21. [Build an incident timeline from reliable evidence](../../questions/troubleshooting/collect-timeline.html)
    — Timelines are built from reliable evidence or not at all.
22. [Design a production troubleshooting experiment](../../questions/troubleshooting/design-runbook-experiment.html)
    — Designed troubleshooting experiments turn hypotheses into repeatable
    practice.
23. [Build a learning loop from production troubleshooting](../../questions/troubleshooting/build-learning-loop.html)
    — The learning loop makes each incident improve the system itself.
24. [Reduce recurring incidents across a platform portfolio](../../questions/troubleshooting/portfolio-recurrence.html)
    — Recurring incidents are reduced across the portfolio, not one service at a
    time.
25. [Define an organization-wide troubleshooting strategy](../../questions/troubleshooting/define-troubleshooting-strategy.html)
    — The organization-wide strategy is the same method at fleet scale.
