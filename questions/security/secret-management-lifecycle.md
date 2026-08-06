---
title: Describe a secure secret-management lifecycle
theme: security
difficulty: middle
type: theory
tags: [security, kubernetes, least-privilege, automation]
---

# Describe a secure secret-management lifecycle

How should an organization create, distribute, rotate, and revoke application secrets?

## Answer guide

- Generate secrets securely and store them in a dedicated audited secrets system.
- Deliver secrets at runtime through authenticated identity, not source control or baked images.
- Grant workloads only the secret scope they need and avoid exposing values in logs.
- Rotate regularly or on compromise, and enable applications to reload or roll out changed credentials safely.
