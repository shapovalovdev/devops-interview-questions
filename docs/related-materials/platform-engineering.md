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

Definition, road, and product before self-service mechanics, and the judgement
calls only after the operating model exists.

1. [Define an internal developer platform](../../questions/platform-engineering/define-an-internal-developer-platform.html)
    — What an internal developer platform is names the product everything else
    serves.
2. [Explain a paved road and a golden path](../../questions/platform-engineering/explain-a-paved-road-and-a-golden-path.html)
    — The paved road and golden path give the platform its central metaphor.
3. [Treat the platform as a product](../../questions/platform-engineering/treat-the-platform-as-a-product.html)
    — Platform-as-a-product is the operating model that separates it from a
    ticket queue.
4. [Offer self-service with safe defaults](../../questions/platform-engineering/offer-self-service-with-safe-defaults.html)
    — Self-service with safe defaults is the mechanism that makes the road real.
5. [Choose a guardrail over a gate](../../questions/platform-engineering/choose-a-guardrail-over-a-gate.html)
    — Guardrails versus gates decides how the defaults treat every deviation.
6. [Version a platform interface](../../questions/platform-engineering/version-a-platform-interface.html)
    — Interface versioning and deprecation keep the road's promises honest over
    time.
7. [Publish platform SLOs and a support model](../../questions/platform-engineering/publish-platform-slos-and-a-support-model.html)
    — SLOs and a support model publish what tenants may actually depend on.
8. [Onboard a team onto the platform](../../questions/platform-engineering/onboard-a-team-onto-the-platform.html)
    — Onboarding is the first lifecycle moment those promises must survive.
9. [Plan a migration onto the paved road](../../questions/platform-engineering/plan-a-migration-onto-the-paved-road.html)
    — Migration moves existing teams onto the road without coercion.
10. [Measure platform adoption](../../questions/platform-engineering/measure-platform-adoption.html)
    — Adoption measurement says what a number can and cannot prove.
11. [Measure developer experience](../../questions/platform-engineering/measure-developer-experience.html)
    — The judgement calls open with developer experience measured honestly.
12. [Reduce cognitive load with team topologies](../../questions/platform-engineering/reduce-cognitive-load-with-team-topologies.html)
    — Cognitive load and interaction modes decide what the platform should
    absorb.
13. [Decide build versus buy for a capability](../../questions/platform-engineering/decide-build-versus-buy-for-a-capability.html)
    — Build versus buy prices each capability the platform might own.
14. [Contain a noisy neighbour on a shared platform](../../questions/platform-engineering/contain-a-noisy-neighbour-on-a-shared-platform.html)
    — Noisy neighbours are the multi-tenancy judgement the sharing model
    creates.
15. [Run a platform-wide incident](../../questions/platform-engineering/run-a-platform-wide-incident.html)
    — Platform incident response and blast radius are the judgement under
    pressure.
16. [Size and staff a platform team](../../questions/platform-engineering/size-and-staff-a-platform-team.html)
    — Cost and staffing size the team all the decisions above implied.
17. [Recognise when a platform team is the wrong answer](../../questions/platform-engineering/recognise-when-a-platform-team-is-the-wrong-answer.html)
    — Knowing when a platform team is the wrong answer is the staff-level close.
