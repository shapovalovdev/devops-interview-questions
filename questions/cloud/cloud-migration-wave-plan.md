---
title: Plan a safe cloud migration wave
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, deployment, reliability, governance]
sources:
  - url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/introduction.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan a safe cloud migration wave

How do you migrate a group of applications to cloud infrastructure without treating cutover as a single big-bang event?

## Answer guide

- Inventory dependencies, data flows, owners, performance constraints, compliance needs, and acceptance metrics. Group applications into waves whose dependencies and rollback paths are understood.
- Select a migration strategy per workload rather than assuming rehosting fits all. Establish the landing zone, identity, network, observability, backups, and operating model before moving production traffic.
- Pilot with a low-risk wave, rehearse data synchronization and cutover, set explicit go/no-go criteria, and retain a time-bounded rollback or fail-forward plan.
- Avoid measuring progress only by servers moved. A migration that leaves unowned operations, weak recovery, or incompatible data latency has moved risk rather than delivered a reliable service.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Prescriptive Guidance: application portfolio assessment strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/introduction.html)
- [Further reading: AWS migration readiness guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/introduction.html)

## What to learn next

- Official documentation: [AWS application portfolio assessment strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/introduction.html)
- Manual or specification: [AWS migration readiness guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/introduction.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS migration workshops](https://catalog.workshops.aws/migration/en-US)
