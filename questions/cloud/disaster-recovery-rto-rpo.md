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
  - url: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
    source_type: standard
    verified_on: 2026-08-16
  - url: https://cloud.google.com/architecture/dr-scenarios-planning-guide
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design cloud disaster recovery from RTO and RPO

How do recovery time and recovery point objectives determine a cloud disaster-recovery design?

## Answer guide

- RTO is the maximum acceptable time to restore service; RPO is the maximum acceptable data loss measured in time. Obtain both per workload from business owners before choosing a pattern.
- Compare backup-and-restore, pilot light, warm standby, and active-active approaches against those objectives, including data replication, dependency recovery, DNS or traffic cutover, cost, and operational staffing.
- Write a tested recovery plan with decision authority, region/account access, artifact availability, data consistency checks, and explicit failback. Measure actual exercise results against objectives.
- A multi-region copy alone is not DR. Unrehearsed credentials, quotas, infrastructure dependencies, stale data, or an untested application cutover can exceed the promised RTO.
- RTO and RPO selection is provider-neutral work: NIST SP 800-34 derives contingency requirements from them without naming a vendor, and Google's DR planning guide walks the same backup-and-restore through hot-standby ladder with provider-neutral names, so justify the chosen pattern by objectives rather than by AWS branding.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS disaster recovery of workloads](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [Further reading: AWS Well-Architected reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
- [Google Cloud — DR scenarios planning guide](https://cloud.google.com/architecture/dr-scenarios-planning-guide)

## What to learn next

- Official documentation: [AWS disaster recovery guidance](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- Manual or specification: [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Database Blog — RDS disaster recovery](https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/)
- Hands-on guide: [AWS disaster recovery workshops](https://catalog.workshops.aws/disaster-recovery/en-US)
