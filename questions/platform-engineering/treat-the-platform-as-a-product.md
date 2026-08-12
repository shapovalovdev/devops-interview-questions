---
title: Treat the platform as a product
theme: platform-engineering
difficulty: junior
type: theory
tags: [platform-engineering, product-management, adoption, developer-experience]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
    source_type: standard
    verified_on: 2026-08-11
---

# Treat the platform as a product

What does "platform as a product" actually change about how a platform team works?

## Answer guide

- It changes who decides what gets built. In a project or ticket model the platform team's backlog is whatever was escalated last; in a product model there is a named product owner, an identified set of internal users, a roadmap justified by user outcomes, and a decision to *not* build things that only one team needs. The CNCF platform engineering maturity model tracks exactly this as an axis, moving from ad-hoc and request-driven work through to a managed product with defined users and measured value.
- The working mechanism is a normal product loop applied internally: segment your users (a Java service team and a data-science team are different segments), discover their actual problems by watching them work rather than reading tickets, ship a thin capability, measure whether it is used, and iterate. Adoption is the signal that replaces revenue, which is why voluntary uptake is treated as evidence and mandated uptake is not.
- Constraints: your users are a captive audience, so satisfaction and adoption are weaker signals than in an external market, and you must go looking for dissatisfaction rather than waiting for churn. The maturity model is a self-assessment tool for finding the next investment, not a certification to score teams against, and the highest level is not the right target for every organization.
- Failure modes: a "product owner" with no authority to refuse work; a roadmap written from the platform team's technical interests rather than from user research; treating internal users as obligated to adopt, which hides the fact that the product is not good enough; counting shipped features instead of solved problems; and measuring satisfaction only through a yearly survey, so the feedback arrives long after the decision that caused it.

## References

- [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Further reading (blog): [Manuel Pais — writing on team interactions and platforms](https://medium.com/@manupaisable)

## What to learn next

- Official documentation: [CNCF platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- Manual or specification: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Maintainer or personal blog: [Manuel Pais — writing on team interactions and platforms](https://medium.com/@manupaisable)
- Technical blog: [CNCF blog](https://www.cncf.io/blog/)
- Hands-on guide: [Team Topologies key concepts](https://teamtopologies.com/key-concepts)
