# SRE related materials

These are legitimately public learning materials for SRE practice. They do not
replace a Question's primary source; use them to deepen judgement about service
level objectives, incident response, and sustainable operations.

## What to learn next

- Official documentation: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Manual or specification: [Google SRE Book — free online edition](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Charity Majors — Observability and SRE](https://charity.wtf/)
- Technical blog: [Google Cloud Blog — DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google Cloud — SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring)

## Suggested study order

Take the promise first — what service reliability means and what an SRE is for
— then the user-journey SLI and the error budget, in that order, because the
budget is arithmetic on the SLI and the SLI is a claim about users. Alerting
follows definitions: classify the alert as page, ticket, or log, then design
the multi-window burn-rate alert that spends the budget's maths. The incident
arc reads like a shift — the on-call handoff, incident roles, triage, the
cross-team major incident, the actionable runbook, and the blameless postmortem
— with evidence preservation the thread from first triage to final write-up.
Then reliability engineering proper: preventing cascading failures, protecting
a service from overload, managing critical state, testing the disaster-recovery
plan, planning capacity, and the production-readiness review that walks all of
it. Toil reduction and DORA measurement come after the incident work, since you
can only price toil you have felt and only trust metrics you have seen teams
game. Close with governance — the error-budget policy, the engagement model,
ownership and accountability, the incident-management program, the reliable
product launch, and the reliability roadmap that turns everything above into
funded work.
