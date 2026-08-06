---
title: Why does Terraform use state?
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
---

# Why does Terraform use state?

What information does Terraform state hold, and what practices protect it in a team environment?

## Answer guide

- State maps declared resource addresses to real infrastructure and attributes needed to calculate changes.
- Use a shared remote backend with access control, encryption, versioning, and locking where supported.
- Treat state as sensitive because it can contain secret values.
- Review plans and use controlled recovery processes instead of ad-hoc state edits.
