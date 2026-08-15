# Troubleshooting: related materials

Use these public resources to practise a hypothesis-driven incident response. The Google SRE book is legally available online under CC BY-NC-N 4.0; it is a free book, not a download of a commercial text.

## What to learn next

- Official documentation: [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance material](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)

## Suggested study order

Begin the way a page begins: read the alert context before escalating — what it
measures and over what window — then establish impact before changing a failing
service, because those two habits preserve every option the rest of the Theme
depends on. Isolation skills come next: isolate the suspected change without
guessing, decide whether a restart is a safe diagnostic action, contain a bad
deployment while protecting evidence, and trace the dependency failure across
service boundaries. Then the specialist diagnoses — DNS from client to
authoritative data, the TLS handshake, authentication without weakening access
control, latency without averaging away the incident, the production data
mismatch, the growing asynchronous backlog, and the observability gap
mid-incident — with stopping a cascading failure while preserving useful
traffic as their synthesis. The error-budget burn alert and verifying recovery
rather than trusting a green dashboard close the single-incident arc, in the
order the SRE track teaches them. The final tier scales the method up: reliable
multi-team handoffs, leading a severe incident without uncontrolled changes,
governing risky mitigations, the regional outage and its traffic strategy,
timelines built from reliable evidence, designed troubleshooting experiments,
the learning loop, recurring-incident reduction, and the organization-wide
strategy.
