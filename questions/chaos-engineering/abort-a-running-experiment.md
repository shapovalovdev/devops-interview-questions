---
title: Abort a running chaos experiment
theme: chaos-engineering
difficulty: junior
type: troubleshooting
tags: [chaos-engineering, incident-response, blast-radius, operations]
sources:
  - url: https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Abort a running chaos experiment

An experiment is degrading a real user journey. How do you stop it, and what has to be true beforehand?

## Answer guide

- Stop the injection first and diagnose afterwards. Every experiment needs a documented halt action that the person watching can run in seconds without approval — a stop command in the chaos tool, deletion of the fault custom resource, or a feature flag that disables injection globally. Halting is not a decision to debate mid-incident; the person on watch is pre-authorised to use it.
- The mechanism should also be automatic. AWS Fault Injection Service stop conditions bind an experiment to CloudWatch alarms so the platform ends the experiment when an alarm fires, and equivalent controls exist elsewhere: Chaos Mesh experiments are removed by deleting the object, and Litmus probes fail a workflow when a health check breaks. Automatic halting matters because a human may be the slowest component in the loop.
- Material constraints: stopping the injection is not the same as recovery. A terminated instance still has to be replaced, a filled disk still has to be cleared, a poisoned cache still has to expire, and connections dropped during a partition may need to be drained. Write the recovery step next to the halt step and rehearse it.
- Failure modes: a halt path that runs through the failing component, a stop condition wired to a metric that only updates after several minutes, an operator that immediately re-creates the fault it was told to remove, and a team that declines to abort because it wants the experiment to finish. Treat any user-visible harm as an incident, declare it, and write it up.

## References

- [AWS Fault Injection Service stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html)
- Further reading (blog): [Gremlin blog](https://www.gremlin.com/blog)

## What to learn next

- Official documentation: [AWS Fault Injection Service stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html)
- Manual or specification: [Chaos Mesh — define the scope of an experiment](https://chaos-mesh.org/docs/define-chaos-experiment-scope/)
- Maintainer or personal blog: [John Allspaw — Kitchen Soap](https://www.kitchensoap.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [Google SRE book — emergency response](https://sre.google/sre-book/emergency-response/)
