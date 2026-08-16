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

Take the promise first — reliability, user-journey SLI, error budget — because
alerting, incidents, and governance are all arithmetic on it.

1. [Define service reliability and the role of an SRE](../../questions/sre/define-service-reliability.html)
    — The promise comes first: reliability as a measured user outcome, SRE as
    shared ownership of it.
2. [Choose a user-journey SLI](../../questions/sre/define-user-journey-sli.html)
    — The user-journey SLI makes the promise arithmetic, which is why it
    precedes any budget.
3. [Explain an error budget](../../questions/sre/explain-error-budget.html) —
    The budget is arithmetic on the SLI, and the SLI is a claim about users.
4. [Classify an alert as a page, ticket, or log](../../questions/sre/classify-alert-urgency.html)
    — Alerting follows definitions: page, ticket, or log is the cheapest filter
    in the Theme.
5. [Design a multi-window burn-rate alert](../../questions/sre/design-multiwindow-burn-alert.html)
    — The multi-window burn alert spends the budget's maths the definitions
    built.
6. [Establish an effective on-call handoff](../../questions/sre/establish-oncall-handoff.html)
    — The incident arc reads like a shift, and it opens with a real handoff.
7. [Assign incident-management roles](../../questions/sre/assign-incident-roles.html)
    — Roles keep the incident organized before the pressure actually arrives.
8. [Triage a production incident](../../questions/sre/triage-production-incident.html)
    — Triage is the single-responder method running inside a declared incident.
9. [Coordinate a major incident across teams](../../questions/sre/coordinate-major-incident.html)
    — The cross-team major incident scales the same method across organizations.
10. [Write an actionable runbook](../../questions/sre/write-actionable-runbook.html)
    — The actionable runbook makes the recurring work of the arc repeatable.
11. [Write a blameless postmortem](../../questions/sre/write-blameless-postmortem.html)
    — The blameless postmortem closes the arc on the evidence every step
    preserved.
12. [Prevent cascading failures](../../questions/sre/prevent-cascading-failures.html)
    — Reliability engineering proper opens with cascades contained as one
    compatible system.
13. [Protect a service from overload](../../questions/sre/protect-service-from-overload.html)
    — Overload protection is admission control at the service's own limits.
14. [Manage critical state for reliability](../../questions/sre/manage-critical-state.html)
    — Critical state is named and protected, never discovered mid-failure.
15. [Test a disaster-recovery plan](../../questions/sre/test-disaster-recovery.html)
    — The disaster-recovery plan is tested, or it is only a document.
16. [Plan service capacity](../../questions/sre/plan-service-capacity.html) —
    Capacity planning turns forecast demand into provisioned headroom with a
    defensible margin.
17. [Run a production-readiness review](../../questions/sre/run-production-readiness-review.html)
    — The readiness review walks every earlier step for a service you did not
    build.
18. [Measure and reduce toil](../../questions/sre/measure-and-reduce-toil.html)
    — Toil is priced after the incident work, because you can only price what
    you have felt.
19. [Measure platform impact with DORA metrics without gaming teams](../../questions/sre/measure-platform-impact-with-dora.html)
    — DORA metrics are trusted only once you have watched teams try to game
    them.
20. [Govern an error-budget policy](../../questions/sre/govern-error-budget-policy.html)
    — The budget policy is the organizational decision the arithmetic was always
    heading toward.
21. [Define an SRE engagement model](../../questions/sre/define-sre-engagement-model.html)
    — The engagement model decides how SRE meets its partner teams.
22. [Establish service ownership and reliability accountability](../../questions/sre/establish-service-ownership.html)
    — Ownership and accountability name who answers for reliability in the end.
23. [Design an organizational incident-management program](../../questions/sre/design-organizational-incident-program.html)
    — The incident program scales the whole arc beyond one team's shift.
24. [Design a reliable product launch](../../questions/sre/design-reliable-launch.html)
    — The reliable launch applies every prior habit to a brand-new service.
25. [Build a reliability investment roadmap](../../questions/sre/build-reliability-roadmap.html)
    — The roadmap closes the Theme by turning everything above into funded work.
