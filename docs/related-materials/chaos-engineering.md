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

Definition and hypothesis before faults, faults before programmes: the order
starts with what chaos engineering claims, ends with what it costs to run across
many teams.

1. [Define chaos engineering and what it is for](../../questions/chaos-engineering/define-chaos-engineering.html)
    — The definition, including why an experiment is not a test, anchors every
    experiment the Theme later runs.
2. [State a steady-state hypothesis](../../questions/chaos-engineering/state-a-steady-state-hypothesis.html)
    — An experiment needs a falsifiable steady-state claim before it needs a
    fault or a tool.
3. [Design a hypothesis-driven chaos experiment](../../questions/chaos-engineering/design-a-hypothesis-driven-experiment.html)
    — Designing the full experiment turns the hypothesis into a procedure with a
    written result.
4. [Control the blast radius of an experiment](../../questions/chaos-engineering/control-the-blast-radius.html)
    — Bounding the fault comes before injecting any, because every later fault
    assumes the bound holds.
5. [Abort a running chaos experiment](../../questions/chaos-engineering/abort-a-running-experiment.html)
    — Abort criteria are the other half of blast-radius control: what makes you
    stop.
6. [Simulate a downstream dependency failure](../../questions/chaos-engineering/simulate-a-downstream-dependency-failure.html)
    — A single dependency fault is the smallest experiment the bounds above can
    safely hold.
7. [Inject latency into a single dependency](../../questions/chaos-engineering/inject-latency-into-a-dependency.html)
    — Latency exposes the timeout and retry behaviour that hard failure hides
    completely.
8. [Inject packet loss and network partitions](../../questions/chaos-engineering/inject-packet-loss-and-partitions.html)
    — Packet loss and partitions add the partial failure shapes between latency
    and outright outage.
9. [Exhaust CPU and memory deliberately](../../questions/chaos-engineering/exhaust-cpu-and-memory.html)
    — Resource exhaustion moves the fault vocabulary from the network onto the
    host's own capacity.
10. [Exhaust disk space and file descriptors](../../questions/chaos-engineering/exhaust-disk-and-file-descriptors.html)
    — Disk and descriptor exhaustion complete the resource tier with slower and
    subtler saturation.
11. [Run pod-level chaos in Kubernetes](../../questions/chaos-engineering/run-pod-level-chaos-in-kubernetes.html)
    — Pod-level chaos applies the fault vocabulary to the platform most teams
    actually run.
12. [Terminate a node and verify real recovery](../../questions/chaos-engineering/terminate-a-node-and-verify-recovery.html)
    — Node termination verifies real recovery rather than a briefly green
    dashboard.
13. [Simulate an availability-zone or region failure](../../questions/chaos-engineering/simulate-a-zone-or-region-failure.html)
    — Zone failure is the widest blast radius the earlier bounds make
    survivable.
14. [Decide whether to experiment in production or staging](../../questions/chaos-engineering/choose-production-or-staging.html)
    — Production versus staging is a trade-off question that only exists once
    the faults themselves are known.
15. [Run data-layer chaos without risking the data](../../questions/chaos-engineering/run-data-layer-chaos-safely.html)
    — Data-layer risk deserves its own care tier after the compute and network
    tiers are rehearsed.
16. [Facilitate a game day](../../questions/chaos-engineering/facilitate-a-game-day.html)
    — Game days make experimentation a team practice rather than a solo
    technique.
17. [Select experiments from incident history](../../questions/chaos-engineering/select-experiments-from-incident-history.html)
    — Incident history chooses the next experiments better than curiosity ever
    does.
18. [Govern consent and ethics for production experiments](../../questions/chaos-engineering/govern-consent-for-production-experiments.html)
    — Consent and ethics govern who may run what in production, and with whose
    permission.
19. [Justify the cost of a chaos engineering programme](../../questions/chaos-engineering/justify-the-cost-of-a-chaos-programme.html)
    — Cost justification prices the programme the practice has by now become.
20. [Run a chaos engineering programme across many teams](../../questions/chaos-engineering/run-a-chaos-engineering-programme.html)
    — Running the programme across many teams is the governance capstone the
    whole order built toward.
