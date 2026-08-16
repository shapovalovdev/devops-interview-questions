# Configuration Management: related materials

Use upstream Ansible documentation for behavior and practise changes in disposable inventories before applying them to production.

## Vendor bias

Ansible is the single engine this Theme teaches through: every mechanics
Question (plays, handlers, roles, inventory) uses Ansible vocabulary with
`docs.ansible.com` as its authority, and even the strategy Questions cite
Ansible documentation. The portable core is the declarative-convergence
model — declare desired state, converge idempotently, predict changes before
applying, detect drift — which Terraform, Puppet, and Salt implement with
their own constructs. Each Question's answer guide names the equivalent
construct or the model-level invariant in at least one other implementation,
rather than presenting Ansible as the category.

## What to learn next

- Official documentation: [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- Manual or specification: [Ansible community guide](https://docs.ansible.com/ansible/latest/community/)
- Maintainer or personal blog: [Jeff Geerling](https://www.jeffgeerling.com/blog)
- Technical blog: [Ansible blog](https://www.ansible.com/blog)
- Hands-on guide: [Ansible playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)

## Suggested study order

Vocabulary before idempotence, idempotence before fleet safety, fleet safety
before strategy, and drift remediation last because classify-before-converging
only lands on someone who has seen what unrecorded changes cost.

1. [Explain an Ansible inventory and host groups](../../questions/configuration-management/ansible-inventory-basics.html)
    — Inventory and host groups are the vocabulary every remaining Question in
    the Theme leans on.
2. [Explain plays, tasks, and modules in Ansible](../../questions/configuration-management/ansible-playbook-basics.html)
    — Plays, tasks, and modules run against the inventory the Theme has just
    defined.
3. [Deliver a configuration file with an Ansible template](../../questions/configuration-management/ansible-templates.html)
    — Templates deliver the first configuration content the plays must manage
    reproducibly.
4. [Use Ansible handlers for service reloads](../../questions/configuration-management/ansible-handlers.html)
    — Handlers sequence reloads so template changes take effect exactly once.
5. [Use Ansible variables without creating precedence surprises](../../questions/configuration-management/ansible-variables-basics.html)
    — Variables parameterize the plays without creating precedence surprises.
6. [Gather and use Ansible facts deliberately](../../questions/configuration-management/ansible-facts.html)
    — Facts let the playbook reason about the host it is about to change.
7. [Target Ansible tasks with tags safely](../../questions/configuration-management/ansible-tags.html)
    — Tags target subsets of the vocabulary once the whole play has grown.
8. [Explain idempotence in an Ansible playbook](../../questions/configuration-management/ansible-idempotence.html)
    — Idempotence makes re-runs meaningful, and it is the property everything
    after depends on.
9. [Validate an Ansible change with check and diff mode](../../questions/configuration-management/ansible-check-diff.html)
    — Check and diff mode validate a change, which is only interesting once a
    no-op re-run means something.
10. [Set safe Ansible concurrency for a fleet change](../../questions/configuration-management/ansible-concurrency-limits.html)
    — The fleet-safety tier widens in order, and concurrency limits bound the
    blast radius first.
11. [Perform an Ansible rolling configuration update](../../questions/configuration-management/ansible-rolling-update.html)
    — Rolling updates batch that blast radius across the inventory in waves.
12. [Coordinate a configuration change with Ansible delegation](../../questions/configuration-management/ansible-delegation.html)
    — Delegation widens where change happens by moving tasks to another host.
13. [Handle Ansible task failures without concealing drift](../../questions/configuration-management/ansible-error-handling.html)
    — Failure handling must not conceal drift, the widest blast radius of the
    four controls.
14. [Design a reusable Ansible role](../../questions/configuration-management/ansible-role-design.html)
    — Reusable roles open the craft tier with composition done deliberately.
15. [Pin and update Ansible collections safely](../../questions/configuration-management/ansible-collection-pinning.html)
    — Pinned collections keep those roles reproducible across fleets and across
    time.
16. [Build an Ansible content test strategy](../../questions/configuration-management/ansible-test-strategy.html)
    — A content test strategy treats the roles as the products they now are.
17. [Apply least privilege to Ansible privilege escalation](../../questions/configuration-management/ansible-privilege-escalation.html)
    — Least-privilege escalation bounds what the automation itself is allowed to
    do.
18. [Protect secrets used by Ansible automation](../../questions/configuration-management/ansible-vault-secrets.html)
    — Protected secrets close the craft tier with its most sensitive payload.
19. [Create a risk-based configuration change model](../../questions/configuration-management/cm-change-risk-model.html)
    — The risk-based change model opens strategy by pricing fleet changes.
20. [Define configuration ownership across a platform fleet](../../questions/configuration-management/cm-fleet-ownership.html)
    — Ownership decides who may change what across the fleet.
21. [Establish configuration-management platform guardrails](../../questions/configuration-management/cm-platform-guardrails.html)
    — Guardrails enforce the ownership model without blocking the teams it
    governs.
22. [Design resilience for a configuration-management control plane](../../questions/configuration-management/cm-resilience-strategy.html)
    — Control-plane resilience keeps the automation itself from becoming the
    outage.
23. [Standardize configuration management without blocking teams](../../questions/configuration-management/cm-standardization-strategy.html)
    — Standardizing without blocking teams is the strategy capstone the
    guardrails made possible.
24. [Design safe configuration drift remediation](../../questions/configuration-management/configuration-drift-remediation.html)
    — Drift remediation is last of all because classify-before-converging only
    lands on someone who has seen unrecorded changes cost an outage.
