# Cloud: related materials

Vendor scope, stated plainly: this Theme teaches cloud concepts through AWS.
Every Question's primary source is AWS documentation, and about six Questions
(CloudTrail, CloudWatch, AWS IAM evaluation, the AWS VPC, AWS multi-account
boundaries, and AWS incident response) are legitimately about one provider's
behaviour. The rest teach portable concepts — regions and fault domains,
RTO/RPO-driven recovery, tagging, quotas, autoscaling, health checks, landing
zones — and each of those answer guides names the Azure or Google Cloud
equivalent construct, with the other provider's documentation cited as an
additional primary source where it is the authority for that equivalent. Use
each Question's primary AWS documentation as the factual authority for AWS
behaviour, and treat the mapped equivalents as orientation, not a promise that
features or responsibility boundaries transfer unchanged to another provider.

## What to learn next

- Official documentation: [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- Manual or specification: [AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/)

## Legal free books

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) is freely
  published by Google and usefully complements cloud reliability, incident,
  capacity, and monitoring Questions.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) is a
  freely published practical companion. It is not AWS-specific; apply its
  methods only after checking the relevant provider documentation.

## Suggested study order

Boundaries first, then the resilience rungs, then governance: the order follows
how a workload lands in AWS and only afterwards how an organization governs many
of them.

1. [Choose an appropriate cloud service model](../../questions/cloud/cloud-service-models.html)
    — Service and shared-responsibility boundaries decide what the provider owes
    before anything is built.
2. [Explain the network boundaries of an AWS VPC](../../questions/cloud/vpc-network-foundations.html)
    — The VPC is the network boundary every later resource lands inside.
3. [Choose security groups and network ACLs deliberately](../../questions/cloud/security-groups-and-network-acls.html)
    — Security groups and network ACLs are the VPC's own traffic controls,
    learned beside the boundary they police.
4. [Provide controlled Internet egress from a private subnet](../../questions/cloud/private-subnet-egress.html)
    — Controlled egress from a private subnet completes the VPC story with the
    pattern most workloads need.
5. [Diagnose an unexpected AWS IAM authorization decision](../../questions/cloud/iam-policy-evaluation.html)
    — IAM policy evaluation explains the denials and grants every later
    permission puzzle reduces to.
6. [Apply least privilege to a cloud workload identity](../../questions/cloud/least-privilege-workload-identity.html)
    — Workload identity applies the evaluation model to machines rather than
    people.
7. [Rotate cloud workload secrets without an outage](../../questions/cloud/secrets-manager-rotation.html)
    — Rotating workload secrets without an outage operationalizes the identity
    tier's most dangerous credential.
8. [Choose Regions and Availability Zones for a workload](../../questions/cloud/regions-and-availability-zones.html)
    — Regions and zones are the fault domains the resilience tier is measured
    against.
9. [Design a cloud load-balancer health check](../../questions/cloud/load-balancer-health-checks.html)
    — Health checks decide how those fault domains hand traffic to healthy
    targets.
10. [Configure target-tracking autoscaling safely](../../questions/cloud/autoscaling-target-tracking.html)
    — Target-tracking autoscaling responds to demand inside the same fault
    domains.
11. [Prevent cloud service quotas from becoming an outage](../../questions/cloud/cloud-quota-capacity-planning.html)
    — Quota planning keeps the scaling tier's ceiling from becoming the outage.
12. [Design cloud disaster recovery from RTO and RPO](../../questions/cloud/disaster-recovery-rto-rpo.html)
    — RTO and RPO turn resilience from adjectives into numbers with owners.
13. [Set a cloud reliability strategy across product teams](../../questions/cloud/cloud-reliability-strategy.html)
    — The reliability strategy spends the whole resilience tier across product
    teams.
14. [Design a CloudWatch alarm that supports action](../../questions/cloud/cloudwatch-alarm-design.html)
    — Alarm design makes the resilience work observable and actionable.
15. [Prove a managed database backup can be restored](../../questions/cloud/managed-database-backup-restore.html)
    — A managed backup only counts once its restore has actually been proven.
16. [Choose object storage for durable application data](../../questions/cloud/object-storage-durability.html)
    — Durability design decides which data the recovery tier can lean on.
17. [Use CloudTrail as audit evidence during a change investigation](../../questions/cloud/cloudtrail-audit-evidence.html)
    — CloudTrail is the evidence an investigation reads after the tiers above
    have acted.
18. [Lead an AWS workload incident response](../../questions/cloud/cloud-incident-response.html)
    — Incident response spends the observability, recovery, and evidence tiers
    in one motion.
19. [Define AWS multi-account boundaries](../../questions/cloud/multi-account-boundaries.html)
    — Account boundaries are the governance tier's unit of isolation.
20. [Establish a governed cloud landing zone](../../questions/cloud/landing-zone-governance.html)
    — The landing zone makes those boundaries a governed default rather than an
    aspiration.
21. [Design a cloud resource tagging strategy](../../questions/cloud/resource-tagging-strategy.html)
    — Tagging is the metadata every cost and governance decision keys on.
22. [Establish cloud cost governance without blocking delivery](../../questions/cloud/cloud-finops-governance.html)
    — FinOps governance prices the platform without blocking the delivery it
    exists for.
23. [Govern data classification in cloud services](../../questions/cloud/data-classification-governance.html)
    — Data classification decides the handling rules the platform must enforce.
24. [Govern cloud identity at organization scale](../../questions/cloud/cloud-identity-governance.html)
    — Organization-wide identity governance closes the Theme at the scale the
    opening tiers never reached.
