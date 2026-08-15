# CI/CD: related materials

Use upstream delivery documentation for product behavior; use the materials below to practise safe, repeatable delivery changes.

## What to learn next

- Official documentation: [GitHub Actions documentation](https://docs.github.com/en/actions)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Troy Hunt](https://www.troyhunt.com/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [GitHub Actions build and test tutorial](https://docs.github.com/en/actions/tutorials/build-and-test-code)

## Suggested study order

Read the pipeline before the deployment machinery: what triggers CI, what
quality gates actually prove, safe test parallelization, flaky-test handling,
and triage of a failed job from its logs — everything later is a promotion of
something a gate passed. Make artifact identity solid next, with immutable
release artifacts, traceable semantic versions, provenance verification, and
retention and promotion rules, because GitOps reconciliation only means
something once declared state names a digest. The GitOps sequence follows
deliberately: the four principles, then the pull-versus-push decision, then
responding to Argo CD drift without masking an incident, closing with
organization-wide delivery standards. Progressive delivery comes after
reconciliation — Argo Rollouts strategies and AnalysisTemplates, the canary
advance-or-stop call, blue-green cutover, rollback design — and then Argo
Workflows and Argo Events extend the automation past deployment. Finish at
platform scope: multi-team pipeline architecture, reusable workflow boundaries,
secrets protection, least-privilege tokens, the cost and capacity model,
deployment freezes during incidents, and recovering the delivery platform
itself during an outage.
