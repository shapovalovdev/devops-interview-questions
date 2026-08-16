# CI/CD: related materials

Use upstream delivery documentation for product behavior; use the materials below to practise safe, repeatable delivery changes.

## What to learn next

- Official documentation: [GitHub Actions documentation](https://docs.github.com/en/actions)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Troy Hunt](https://www.troyhunt.com/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [GitHub Actions build and test tutorial](https://docs.github.com/en/actions/tutorials/build-and-test-code)

## Suggested study order

Read the pipeline before the deployment machinery, artifact identity before
GitOps, reconciliation before progressive delivery — every later stage promotes
something an earlier gate passed.

1. [Choose CI pipeline triggers](../../questions/ci-cd/trigger-a-pipeline.html)
    — What triggers CI decides what every later gate and promotion reacts to.
2. [Design CI/CD quality gates for a service](../../questions/ci-cd/pipeline-quality-gates.html)
    — Gates prove things about a change, and everything later in the Theme is a
    promotion of something a gate passed.
3. [Parallelize a CI test suite safely](../../questions/ci-cd/parallelize-test-suite.html)
    — Safe test parallelization keeps the gate fast without making it blind.
4. [Handle flaky tests without masking regressions](../../questions/ci-cd/retry-flaky-tests.html)
    — Flaky-test handling preserves the gate's signal instead of masking
    regressions to keep it green.
5. [Triage a failed CI job from its logs](../../questions/ci-cd/read-ci-logs.html)
    — Triaging a failed job from its logs is the human skill the pipeline tier
    ends on.
6. [Why should CI publish immutable release artifacts?](../../questions/ci-cd/immutable-release-artifacts.html)
    — Artifact identity comes next because GitOps reconciliation only means
    something once declared state names a digest.
7. [Produce a traceable semantic-version release](../../questions/ci-cd/semantic-version-release.html)
    — Traceable semantic versions make the digest human-readable without ever
    replacing it.
8. [Verify supply-chain provenance before deployment](../../questions/ci-cd/supply-chain-provenance.html)
    — Provenance verification binds the artifact to a trusted builder, source
    revision, and declared inputs.
9. [Set artifact retention and promotion rules](../../questions/ci-cd/artifact-retention-and-promotion.html)
    — Retention and promotion rules decide how long that identity stays
    trustworthy across environments.
10. [Explain the four GitOps principles](../../questions/ci-cd/gitops-principles.html)
    — The four principles name the operating model the delivery machinery is
    about to adopt.
11. [Choose a pull-based reconciler or a push-based deployment pipeline](../../questions/ci-cd/gitops-pull-versus-push-delivery.html)
    — Pull versus push is a design decision rather than a preference, and it
    needs the principles first.
12. [Respond to Argo CD drift without masking an incident](../../questions/ci-cd/argo-cd-reconciliation-drift.html)
    — Responding to drift without masking an incident keeps reconciliation
    honest.
13. [Establish organization-wide delivery standards](../../questions/ci-cd/platform-delivery-standards.html)
    — Organization-wide delivery standards close the GitOps sequence by making
    it a paved path.
14. [Choose a progressive Argo Rollouts strategy](../../questions/ci-cd/argo-rollouts-progressive-delivery.html)
    — Progressive delivery comes after reconciliation because a rollout refines
    what the reconciler already guarantees.
15. [Define an Argo Rollouts AnalysisTemplate safely](../../questions/ci-cd/argo-rollouts-analysis.html)
    — AnalysisTemplates decide what evidence advances or stops the rollout
    strategies above.
16. [Decide whether to advance or stop a canary deployment](../../questions/ci-cd/canary-deployment-decision.html)
    — The advance-or-stop call is the judgement the AnalysisTemplate automates.
17. [Plan a blue-green production cutover](../../questions/ci-cd/blue-green-cutover.html)
    — Blue-green trades the gradual canary for a controlled instant switch.
18. [Design a deployment rollback](../../questions/ci-cd/roll-back-a-deployment.html)
    — Rollback design completes the delivery tier with the path every step above
    may one day need.
19. [Explain when to use Argo Workflows](../../questions/ci-cd/argo-workflows-fundamentals.html)
    — Argo Workflows extends the automation past deployment, and only after
    deployment itself is safe.
20. [Model failure and parallelism in an Argo Workflow DAG](../../questions/ci-cd/argo-workflows-dag-failure.html)
    — Modelling failure and parallelism in a DAG keeps the workflow honest under
    real load.
21. [Pass artifacts safely between Argo Workflow steps](../../questions/ci-cd/argo-workflow-artifacts.html)
    — Passing artifacts between steps carries the identity discipline up into
    orchestration.
22. [Reuse Argo Workflow templates without losing control](../../questions/ci-cd/argo-workflow-template-reuse.html)
    — Template reuse keeps the workflow fleet maintainable rather than
    copy-pasted.
23. [Explain the Argo Events event path](../../questions/ci-cd/argo-events-architecture.html)
    — The Argo Events event path explains what triggers the automation the
    workflows run.
24. [Design an Argo Events Sensor for a production trigger](../../questions/ci-cd/argo-events-sensor-dependencies.html)
    — Sensor dependencies make event triggers reliable enough to own in
    production.
25. [Design a multi-team pipeline architecture](../../questions/ci-cd/multi-team-pipeline-architecture.html)
    — Multi-team pipeline architecture opens the platform tier the whole tool
    tier serves.
26. [Choose reusable workflow boundaries](../../questions/ci-cd/reusable-workflow-boundaries.html)
    — Reusable workflow boundaries keep the shared pipelines composable across
    many teams.
27. [Protect deployment secrets in CI/CD](../../questions/ci-cd/protect-deployment-secrets.html)
    — Secrets protection is the first platform duty the shared machinery owes
    its tenants.
28. [Apply least privilege to a workflow token](../../questions/ci-cd/least-privilege-workflow-token.html)
    — Least-privilege tokens bound what the delivery automation itself may do.
29. [Build a CI/CD cost and capacity model](../../questions/ci-cd/ci-cd-cost-capacity-model.html)
    — The cost and capacity model prices the platform the teams now share.
30. [Decide whether to freeze deployments during an incident](../../questions/ci-cd/incident-change-freeze.html)
    — Freeze decisions during incidents connect delivery governance back to
    incident governance.
31. [Recover the delivery platform during an outage](../../questions/ci-cd/disaster-recover-delivery-platform.html)
    — Recovering the delivery platform itself during an outage is the failure
    the whole Theme rehearses for.
