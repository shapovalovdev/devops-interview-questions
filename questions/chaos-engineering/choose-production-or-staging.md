---
title: Decide whether to experiment in production or staging
theme: chaos-engineering
difficulty: senior
type: scenario
tags: [chaos-engineering, experimentation, governance, reliability]
sources:
  - url: https://principlesofchaos.org/
    source_type: standard
    verified_on: 2026-08-10
---

# Decide whether to experiment in production or staging

Leadership is uncomfortable with production experiments. How do you decide where each experiment belongs?

## Answer guide

- The honest answer is that both are needed and they answer different questions. Staging validates the tooling, the permissions, the abort path, and the mechanics of the fault. Production is the only place with real traffic mix, real data volume, real cache hit rates, real third-party dependencies, real hardware heterogeneity, and real people responding — which is why the discipline's principles put running in production at the centre. Confidence gained in staging transfers only as far as staging resembles production.
- Make the decision per experiment on evidence rather than by policy. Ask what specifically differs between the environments for this fault: if the hypothesis depends on traffic volume, connection-pool saturation, data skew, or an external provider, staging cannot falsify it. If the hypothesis is about a code path or a configuration mechanism, staging is enough and cheaper. Progress through environments — staging, then a production canary cell, then a small production share, then the full scope.
- Material constraints for production runs: bounded blast radius, an automatic stop condition, an owner watching, a rollback that does not depend on the component under test, and an agreed maximum error budget spend. Publish the schedule, treat any user-visible harm as an incident, and count the impact against the error budget so the cost is visible rather than hidden.
- Failure modes: a staging environment scaled down so far that every experiment passes, giving false assurance; production experiments run without the error-budget conversation, which turns a technical practice into a political one after the first bad day; and the opposite failure, an organisation that never graduates from staging and therefore keeps discovering its real failure modes during real outages.

## References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [Principles of Chaos Engineering](https://principlesofchaos.org/)
- Manual or specification: [Azure Well-Architected — reliability testing strategy](https://learn.microsoft.com/en-us/azure/well-architected/reliability/testing-strategy)
- Maintainer or personal blog: [Nora Jones — resilience engineering writing](https://medium.com/@NoraJones)
- Technical blog: [Netflix Technology Blog](https://netflixtechblog.com/)
- Hands-on guide: [Google SRE book — embracing risk and error budgets](https://sre.google/sre-book/embracing-risk/)
