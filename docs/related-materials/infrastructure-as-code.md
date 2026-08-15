# Infrastructure as Code: related materials

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)

## Suggested study order

Ask why Terraform keeps state before writing configuration: the answer, the
address-to-resource mapping, turns remote backends, lock contention, and the
state-ownership model into engineering rather than ritual. Learn the language
tier next — root modules and resource addresses, safe input variables, local
values versus data sources, for_each versus count, and when depends_on is a
smell — then module craft: stable interfaces, shared modules treated as
products, outputs that do not leak secrets, pinned providers. The surgery set
follows: importing existing resources, refactoring addresses safely, lifecycle
rules that do not mask risk, and migrating state to a remote backend. The
plan-review question is the hinge of the Theme — the change contract, read
after the language that produces plans and before anything that automates them
— and it leads into the testing strategy, policy-as-code gates, environment
isolation, and the zero-downtime migration. Close with drift: detection first,
then organization-scale drift governance, the risk-based change model, platform
guardrails, and state ownership — the tier that makes infrastructure-as-code an
organizational capability rather than a tool.
