# Platform engineering: related materials

Treat the CNCF Platforms White Paper as the definition of what an internal
platform is and what it is for, and the upstream manuals — Backstage, Crossplane,
Score, and the Kubernetes API conventions — as the authority for what a given
platform interface actually does. Platform-engineering questions almost always
reduce to four separate decisions: who the platform's users are and what they are
trying to do, which capability the platform owns versus which it leaves to the
stream-aligned team, how a golden path is made attractive rather than merely
mandatory, and what the platform promises when it breaks. Read the white paper
and the platform maturity model for the method, the tool manuals for the
mechanism, the Team Topologies key concepts for the organizational vocabulary —
stream-aligned team, platform team, cognitive load, interaction mode — and the
DORA research and the Google SRE books for how the outcome is measured. The
individual-author and vendor blogs below give context and field experience; they
are not evidence for factual claims about a product's behaviour.

## What to learn next

- Official documentation: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Manual or specification: [Score specification reference](https://docs.score.dev/docs/score-specification/score-spec-reference/)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [Backstage blog](https://backstage.io/blog)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)

## Legal free books

No commercial platform-engineering or Team Topologies title is linked here:
avoid unauthorized copies. The CNCF Platforms White Paper and platform
engineering maturity model, the Team Topologies key-concepts pages, the
Backstage, Crossplane and Score manuals, the freely published DORA reports, and
the Google SRE book and SRE workbook are all lawfully free to read and cover the
same ground for interview preparation.

## Suggested study order

Start with what an internal developer platform is, what a paved road and a golden
path mean, and why platform-as-a-product is a different operating model from a
central ticket queue. Then work through self-service with safe defaults,
guardrails versus gates, platform interface versioning and deprecation, platform
service level objectives and support models, onboarding, migration, and adoption
measurement. Finish with the judgement calls: developer-experience measurement,
cognitive load and Team Topologies interaction modes, build versus buy,
multi-tenancy and noisy neighbours, platform incident response and blast radius,
the cost and staffing of a platform team, and the staff-level question of when a
platform team is the wrong answer.
