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

Learn what a play is before learning how to run one safely: inventory and host
groups, then plays, tasks, and modules, then templates, handlers, variables,
facts, and tags — the vocabulary every remaining question leans on. Idempotence
comes next, with check and diff mode immediately after, since validating a
change is only interesting once a no-op re-run means something. Then the
fleet-safety tier in widening order: concurrency limits, rolling updates,
delegation, and failure handling that does not conceal drift, each widening the
blast radius the previous control bounded. Build up to craft — reusable roles,
pinned collections, a content test strategy, least-privilege escalation,
protected secrets — and close with strategy: the risk-based change model,
ownership across a fleet, guardrails, control-plane resilience, and
standardization without blocking teams. Drift remediation is last of all,
because classify-before-converging only lands on someone who has seen what
unrecorded changes cost.
