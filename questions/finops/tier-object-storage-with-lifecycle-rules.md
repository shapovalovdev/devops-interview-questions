---
title: Tier object storage with lifecycle rules
theme: finops
difficulty: middle
type: scenario
tags: [finops, storage, cost-optimization, cloud]
sources:
  - url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/storage/docs/lifecycle
    source_type: official-docs
    verified_on: 2026-08-11
---

# Tier object storage with lifecycle rules

An object store holds hundreds of terabytes and is growing. How do you design storage tiering so it actually reduces the bill?

## Answer guide

- Start from an access profile per prefix or bucket, not per byte: how old objects are when they stop being read, how many objects there are, their average size, and whether anything retrieves them in bulk. Tiering saves money on storage rate and costs money on transitions and retrieval, so the profile decides whether the trade is positive.
- The mechanism is a lifecycle configuration evaluated asynchronously against object age or object tags: transition to an infrequent-access or archive class after N days, expire after M days, and clean up noncurrent versions, incomplete multipart uploads, and delete markers. S3 lifecycle rules and Google Cloud Storage lifecycle rules both work this way, and both charge per transition request.
- The decisive constraints are the ones people forget: colder classes carry a minimum storage duration and, on some classes, a minimum billable object size, so transitioning many small or short-lived objects can cost more than leaving them alone. Archive classes add retrieval fees and restore latency measured in minutes to hours, which changes what the data can be used for.
- Consider intelligent tiering when the access pattern is genuinely unknown: it moves objects between tiers automatically for a monitoring charge per object, which is a good trade for large objects and a bad one for billions of tiny ones.
- Failure modes: expiring data that a compliance or legal-hold requirement still needed; archiving a dataset a nightly job actually reads, converting a storage saving into a large retrieval bill; forgetting noncurrent versions in a versioned bucket so the visible size is a fraction of the billed size; and leaving abandoned multipart uploads accumulating invisibly for years.

## References

- [Manage the S3 object lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Google Cloud Storage object lifecycle management](https://cloud.google.com/storage/docs/lifecycle)
- Further reading (blog): [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

## What to learn next

- Official documentation: [Manage the S3 object lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- Manual or specification: [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS blog](https://www.lastweekinaws.com/blog/)
- Technical blog: [Vantage engineering blog](https://www.vantage.sh/blog)
- Hands-on guide: [Google Cloud Storage object lifecycle management](https://cloud.google.com/storage/docs/lifecycle)
