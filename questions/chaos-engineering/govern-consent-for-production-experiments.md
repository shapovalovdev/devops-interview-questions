---
title: Govern consent and ethics for production experiments
theme: chaos-engineering
difficulty: staff
type: scenario
tags: [chaos-engineering, governance, security, experimentation]
sources:
  - url: https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-permissions-security
    source_type: official-docs
    verified_on: 2026-08-10
---

# Govern consent and ethics for production experiments

Real customers are affected by production experiments. Who has to agree, and what are the limits?

## Answer guide

- Establish who can consent to what. Service owners consent to faults inside their own boundary; dependent teams must be consulted when the blast radius crosses into theirs; the business owns the decision about customer-visible impact, because error budget spend is a product decision, not an engineering one. Legal, compliance, and privacy teams are needed where regulated data, contractual availability commitments, or safety-relevant systems are in scope. Record the agreement, its scope, and its expiry rather than relying on a conversation.
- Customers do not consent individually, so the obligation is to keep impact proportionate, bounded, disclosed where it matters, and honest. Publish the standing policy that reliability is tested in production, hold experiments to the same error budget as any other risk, tell affected customers when impact was real, and never describe an experiment-caused outage as something else. An organisation that hides self-inflicted impact loses the internal trust the practice depends on.
- Enforce consent in the platform rather than by policy document. Role-based access decides who may run which fault class against which targets, as Azure Chaos Studio's permission model and Chaos Mesh's role bindings do; targets must be explicitly enabled; every run is audited with an identity, a scope, and a timestamp; and the dangerous fault classes require a second approver. Employees are participants too, so on-call load, timing outside working hours, and the psychological safety of responders during a surprise exercise all belong in the same governance.
- Failure modes: consent obtained once and treated as permanent while the system's dependencies change underneath it; a shared platform team authorising faults on tenants who never agreed; experiments used to make a political point about another team's quality; and an approval process so heavy that teams stop asking and start testing informally, which produces the same risk with none of the controls.

## References

- [Azure Chaos Studio — permissions and security](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-permissions-security)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Azure Chaos Studio — permissions and security](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-permissions-security)
- Manual or specification: [Chaos Mesh — manage user permissions](https://chaos-mesh.org/docs/manage-user-permissions/)
- Maintainer or personal blog: [Nora Jones — resilience engineering writing](https://medium.com/@NoraJones)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — embracing risk and error budgets](https://sre.google/sre-book/embracing-risk/)
