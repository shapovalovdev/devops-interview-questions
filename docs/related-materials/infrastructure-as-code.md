# Infrastructure as Code: related materials

Vendor scope, stated plainly: this Theme teaches infrastructure as code
through Terraform. Every Question's primary source is HashiCorp's Terraform
documentation, and the Questions are written in Terraform terms. The concepts —
state, plan review, module craft, drift, guardrails — are tool-portable, and
each answer guide names the equivalent construct elsewhere: OpenTofu, the
Linux Foundation fork that keeps the same language, state, and plan mechanics,
plus CloudFormation change sets, resource import, and retention policies,
Pulumi previews, aliases, and stacks, and Azure Bicep modules where they carry
the same lesson. OpenTofu, CloudFormation, Pulumi, Bicep, and Open Policy
Agent documentation are cited as additional primary sources where they are the
authority for the mapped construct. Since the OpenTofu fork, single-vendor
Terraform framing deserves this scrutiny: treat Terraform behaviour as
Terraform's, and check the fork's or another tool's documentation before
assuming an identical mechanism.

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)

## Suggested study order

State before language, language before module craft, surgery before the
plan-review hinge, and drift governance last — the tier that makes IaC an
organizational capability.

1. [Why does Terraform use state?](../../questions/infrastructure-as-code/terraform-state-purpose.html)
    — Why Terraform keeps state turns backends, locking, and ownership into
    engineering rather than ritual.
2. [Handle Terraform state lock contention](../../questions/infrastructure-as-code/state-lock-contention.html)
    — Lock contention is the state model's operational failure mode, met before
    configuration begins.
3. [Explain a Terraform root module and resource address](../../questions/infrastructure-as-code/terraform-configuration-basics.html)
    — Root modules and resource addresses are the language tier the state maps
    onto.
4. [Define safe Terraform input variables](../../questions/infrastructure-as-code/input-variables-and-validation.html)
    — Safe input variables keep the language tier's interfaces honest at the
    boundary.
5. [Distinguish Terraform local values from data sources](../../questions/infrastructure-as-code/local-values-and-data-sources.html)
    — Local values versus data sources decides where each value should actually
    live.
6. [Choose for_each or count for repeated Terraform resources](../../questions/infrastructure-as-code/for-each-versus-count.html)
    — for_each versus count is the repetition decision every module below
    inherits.
7. [Model Terraform dependencies without overusing depends_on](../../questions/infrastructure-as-code/explicit-dependencies.html)
    — depends_on is a smell precisely when the language tier is properly
    understood.
8. [Design a stable Terraform module interface](../../questions/infrastructure-as-code/module-interface-design.html)
    — Module craft opens with stable interfaces, the product's front door.
9. [Treat shared Terraform modules as internal products](../../questions/infrastructure-as-code/iac-module-product-strategy.html)
    — Shared modules are products, with users, versions, and support
    obligations.
10. [Design Terraform outputs without exposing secrets](../../questions/infrastructure-as-code/output-contracts-and-sensitive-data.html)
    — Outputs must not leak the secrets the modules handled safely internally.
11. [Pin Terraform provider dependencies safely](../../questions/infrastructure-as-code/provider-version-pinning.html)
    — Pinned providers keep the whole craft reproducible across time.
12. [Import an existing resource into Terraform](../../questions/infrastructure-as-code/import-existing-infrastructure.html)
    — The surgery set opens by bringing existing resources under management.
13. [Refactor Terraform resource addresses safely](../../questions/infrastructure-as-code/safe-resource-refactoring.html)
    — Refactoring resource addresses safely is the surgery the import made
    necessary.
14. [Use Terraform lifecycle rules without masking risk](../../questions/infrastructure-as-code/resource-lifecycle-controls.html)
    — Lifecycle rules must not mask the very risk the surgery tier exists to
    expose.
15. [Migrate Terraform state to a remote backend](../../questions/infrastructure-as-code/remote-backend-migration.html)
    — Migrating state to a remote backend completes the surgery with the state
    tier's opening promise.
16. [Review a Terraform plan before production apply](../../questions/infrastructure-as-code/terraform-plan-review.html)
    — The plan review is the hinge: the change contract, read after the language
    that produces plans and before anything that automates them.
17. [Build a Terraform testing strategy](../../questions/infrastructure-as-code/terraform-test-strategy.html)
    — Testing follows the hinge because tests generate and check exactly those
    plans.
18. [Design policy-as-code gates for Terraform delivery](../../questions/infrastructure-as-code/policy-as-code-gates.html)
    — Policy-as-code gates automate the review the hinge taught humans to
    perform.
19. [Isolate Terraform environments and blast radius](../../questions/infrastructure-as-code/multi-environment-isolation.html)
    — Environment isolation bounds the blast radius the automation above can
    reach.
20. [Plan a zero-downtime infrastructure migration with Terraform](../../questions/infrastructure-as-code/zero-downtime-iac-migration.html)
    — The zero-downtime migration spends review, tests, and gates on one real
    change.
21. [Detect and handle infrastructure drift](../../questions/infrastructure-as-code/infrastructure-drift.html)
    — Drift detection opens the close: declared state meets operational reality.
22. [Govern infrastructure drift at organization scale](../../questions/infrastructure-as-code/iac-drift-governance.html)
    — Organization-scale drift governance routes differences to owners rather
    than auto-applying them.
23. [Create a risk-based IaC change-management model](../../questions/infrastructure-as-code/iac-change-risk-management.html)
    — The risk-based change model prices what the drift tier keeps finding.
24. [Establish infrastructure-as-code platform guardrails](../../questions/infrastructure-as-code/iac-platform-guardrails.html)
    — Platform guardrails enforce the model without blocking every team that
    touches it.
25. [Define an infrastructure-as-code state ownership model](../../questions/infrastructure-as-code/iac-state-ownership-model.html)
    — State ownership is last because it is the tier that makes IaC an
    organizational capability rather than a tool.
