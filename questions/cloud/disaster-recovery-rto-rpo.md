---
title: Design cloud disaster recovery from RTO and RPO
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, reliability, availability, incident-response]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design cloud disaster recovery from RTO and RPO

How do recovery time and recovery point objectives determine a cloud disaster-recovery design?

## Answer guide

- RTO is the maximum acceptable time to restore service; RPO is the maximum acceptable data loss measured in time. Obtain both per workload from business owners before choosing a pattern.
- Compare backup-and-restore, pilot light, warm standby, and active-active approaches against those objectives, including data replication, dependency recovery, DNS or traffic cutover, cost, and operational staffing.
- Write a tested recovery plan with decision authority, region/account access, artifact availability, data consistency checks, and explicit failback. Measure actual exercise results against objectives.
- A multi-region copy alone is not DR. Unrehearsed credentials, quotas, infrastructure dependencies, stale data, or an untested application cutover can exceed the promised RTO.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS disaster recovery of workloads](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [Further reading: AWS Well-Architected reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
