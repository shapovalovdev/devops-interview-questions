# Cloud learning-material and source audit

Audited: 2026-08-06

Scope: all 25 active files in `questions/cloud/`. The Cloud Theme deliberately
uses AWS because every prompt, answer, tag, and source names AWS behavior. The
answers must not be read as provider-neutral cloud guarantees.

## Primary-source review

Every Cloud Question has one structured `official-docs` source from AWS and a
descriptive direct link to it in `## References`. The sources were reviewed
against the answer's subject as follows:

| Subject group | Questions | Primary documentation reviewed |
| --- | --- | --- |
| Compute, scaling, and observability | target tracking, quotas, CloudWatch alarms, load-balancer health checks | EC2 Auto Scaling and CloudWatch documentation |
| Identity and governance | identity governance, IAM evaluation, workload identity, landing zones, multi-account boundaries, tagging, data classification | IAM, Organizations, Control Tower, and Well-Architected documentation |
| Reliability and recovery | incident response, reliability strategy, DR, regions/AZs, RDS backup/restore, S3 durability | AWS Reliability Pillar, DR whitepaper, service guides |
| Network controls | VPC foundations, private egress, security groups and NACLs | Amazon VPC and PrivateLink documentation |
| Strategy and operations | service models, migration, FinOps, CloudTrail, Secrets Manager | AWS overview, prescriptive guidance, cost, CloudTrail, and Secrets Manager guides |

The direct reference immediately following the existing complementary AWS blog
in each Question is the primary source record. AWS blog material is learning
context only; it is not the factual authority for the answer guide.

## Curated learning links

All 25 Questions now have exactly five HTTPS learning links: a directly
relevant official guide; a second official manual, specification, or service
guide; Corey Quinn's named independent cloud-operations publication; an AWS
technical blog appropriate to the subject; and a public hands-on resource.

`Corey Quinn — Last Week in AWS` is deliberately labelled as a personal
technical blog. It is context and critical operational commentary, not evidence
for AWS product semantics. The Theme page records two legal free books from
Google (the SRE Book and SRE Workbook); commercial cloud books are not copied
or linked as unauthorized downloads.

## Live-link method

Run the repository validator with the certifi CA bundle in environments whose
Python trust store lacks the issuer used by public documentation hosts:

```sh
SSL_CERT_FILE="$(python3 -m certifi)" python3 tests/validate_learning_resources.py --check-live --report
```

The link-audit manifest is the authoritative scope for this completed Cloud
slice. Any live failure is repaired with a public equivalent rather than added
to an exception list.
