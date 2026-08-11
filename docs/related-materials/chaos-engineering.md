# Chaos engineering: related materials

Treat the Principles of Chaos Engineering as the definition of the discipline and
the upstream tool manuals — AWS Fault Injection Service, LitmusChaos, Chaos Mesh,
and Azure Chaos Studio — as the authority for what a given fault actually does to
a target. Chaos engineering questions almost always reduce to four separate
decisions: what steady state you claim to hold, which fault you inject, how far
the damage is allowed to spread, and what makes you stop. Read the principles for
the method, the tool manuals for the mechanism and the safety controls, and the
Google SRE books for the reliability vocabulary — service level objectives, error
budgets, cascading failure — that experiments are measured against. The
individual-author and vendor blogs below give context and field experience; they
are not evidence for factual claims about a product's behaviour.

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [AWS Fault Injection Service actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Chaos Mesh quick start](https://chaos-mesh.org/docs/quick-start/)

## Legal free books

No commercial chaos-engineering title is linked here: avoid unauthorized copies.
The Principles of Chaos Engineering, the LitmusChaos, Chaos Mesh, Chaos Toolkit,
AWS Fault Injection Service and Azure Chaos Studio manuals, the AWS Builders'
Library, and the freely published Google SRE book and SRE workbook are all
lawfully free to read and cover the same ground for interview preparation.

## Suggested study order

Start with the definition, the steady-state hypothesis, and why an experiment is
not a test. Then work through blast-radius control, abort criteria, single
dependency faults, latency and packet loss, resource exhaustion, and pod, node,
and zone failure in Kubernetes and the cloud. Finish with production versus
staging trade-offs, data-layer risk, game-day facilitation, incident-informed
experiment selection, consent and ethics for production experimentation, and the
cost and governance of running a chaos programme across many teams.
