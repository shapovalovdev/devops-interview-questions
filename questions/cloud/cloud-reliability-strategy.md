---
title: Set a cloud reliability strategy across product teams
theme: cloud
difficulty: staff
type: scenario
tags: [aws, cloud, reliability, availability, observability, governance]
sources:
  - url: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set a cloud reliability strategy across product teams

How would you set reliability expectations for a portfolio of cloud services with different business criticality?

## Answer guide

- Classify services by business impact and set measurable service-level objectives, recovery objectives, and dependency assumptions with their owners. The same availability target is neither affordable nor appropriate for every workload.
- Provide reusable patterns for multi-AZ deployment, backups, capacity, observability, safe change delivery, and incident response. Test important failure modes through exercises rather than reviewing diagrams alone.
- Track error-budget consumption, recovery-exercise results, repeated dependency failures, and resilience debt; fund improvements based on demonstrated risk and customer impact.
- Do not promise an aggregate platform SLA while critical dependencies have unknown limits or single points of failure. Reliability is an end-to-end property, including people and recovery procedures.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Further reading: AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html)

## What to learn next

- Official documentation: [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- Manual or specification: [AWS Well-Architected Tool guide](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/)
