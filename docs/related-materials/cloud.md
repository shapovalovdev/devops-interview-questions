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

Start with service and shared-responsibility boundaries, then VPC and identity.
Move through resilience, observability, backup/restore, and incident response.
Finish with account governance, cost allocation, data classification, and
organization-wide control design.
