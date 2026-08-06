---
title: Rotate cloud workload secrets without an outage
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, security, iam, reliability]
sources:
  - url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Rotate cloud workload secrets without an outage

How would you rotate a database credential used by production workloads in AWS?

## Answer guide

- Store the secret in Secrets Manager, grant runtime roles read access only to the required secret, and use a supported rotation strategy or Lambda rotation function appropriate for the database.
- Design clients to refresh credentials safely and tolerate a brief overlap: validate the new secret before promoting it, preserve the previous version until consumers have moved, and monitor authentication errors.
- Limit rotation-function permissions, log rotation events without logging secret values, and test failure handling in a non-production environment. Decide who owns emergency rotation and recovery.
- Rotation can break production when applications cache credentials indefinitely, connection pools cannot reconnect, or a custom function changes the secret before verifying the target system accepted it.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Secrets Manager: rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
- [Further reading: Secrets Manager rotation Lambda functions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_lambda-functions.html)
