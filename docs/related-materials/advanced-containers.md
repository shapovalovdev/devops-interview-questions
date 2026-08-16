# Advanced Containers: related materials

Treat the OCI specification, runtime documentation, and Linux kernel manuals
linked from each Question as factual authority. These additional resources help
connect cgroups, namespaces, capabilities, rootless operation, and runtime
security to hands-on practice.

## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)

## Legal free books

No commercial container book is linked. The upstream specification, kernel
manuals, and author-published material above are free to read and avoid
unauthorized reproductions.

## Suggested study order

Isolation primitives first and platform programmes last: the order builds from
the kernel mechanisms a container actually defends with to the incidents and
governance that spend them.

1. [Explain the Linux primitives behind container isolation](../../questions/advanced-containers/container-isolation-basics.html)
    — Namespaces and cgroups layered onto an ordinary process are the model
    every isolation decision in this Theme argues from.
2. [Explain mount namespaces and a container root filesystem](../../questions/advanced-containers/mount-namespace-basics.html)
    — The mount namespace holds the container's root filesystem, so it comes
    directly after the primitives that define what a container is.
3. [Explain PID namespaces and container process visibility](../../questions/advanced-containers/pid-namespace-basics.html)
    — PID namespaces explain why a container sees itself as process one and why
    host-side tools must name the namespace first.
4. [Design correct PID 1 signal handling in a container](../../questions/advanced-containers/pid-one-signal-handling.html)
    — Signal handling only becomes a design problem once the PID namespace has
    made the container's first process special.
5. [Explain a container network namespace](../../questions/advanced-containers/network-namespace-basics.html)
    — The network namespace completes the isolation picture with interfaces,
    addresses, and sockets of the container's own.
6. [Decide when containers should share a namespace](../../questions/advanced-containers/namespace-sharing-tradeoffs.html)
    — With all three namespaces understood, sharing any of them becomes an
    informed trade-off rather than a convenience.
7. [Explain cgroup resource accounting for containers](../../questions/advanced-containers/cgroup-resource-accounting.html)
    — Cgroups move from model to measurement: what the kernel charges the
    container for CPU, memory, and I/O.
8. [Diagnose cgroup CPU throttling in a container](../../questions/advanced-containers/cpu-quotas-and-throttling.html)
    — CPU quota throttling is the first accounting figure operators actually
    feel, and it misreads without the accounting model before it.
9. [Investigate a container cgroup memory limit and OOM kill](../../questions/advanced-containers/memory-limits-and-oom.html)
    — Memory limits fail differently from CPU quotas, and the OOM kill inside a
    cgroup is only legible with the accounting in hand.
10. [Use the cgroup PIDs controller to contain fork storms](../../questions/advanced-containers/pids-controller-protection.html)
    — The PIDs controller bounds the one resource a fork storm spends,
    completing the cgroup controls before migrating them.
11. [Lead a cgroup v2 migration for container hosts](../../questions/advanced-containers/cgroup-v2-migration.html)
    — Migrating hosts to cgroup v2 is safe only once the accounting, throttling,
    and controllers it reshuffles are understood.
12. [Explain overlay filesystem copy-up and container writes](../../questions/advanced-containers/overlay-filesystem-copy-up.html)
    — Copy-up explains where container writes actually land, the filesystem fact
    every runtime tier below builds on.
13. [Apply Linux capabilities with least privilege](../../questions/advanced-containers/capabilities-least-privilege.html)
    — Dropping capabilities is the first concrete narrowing of what a container
    may ask its host's kernel to do.
14. [Control device access for a container workload](../../questions/advanced-containers/device-access-control.html)
    — Device rules govern the kernel interface underneath the capabilities, the
    second thing least privilege must bound.
15. [Design a seccomp profile for a container workload](../../questions/advanced-containers/seccomp-profile-design.html)
    — Seccomp filters the syscall surface itself, the deepest of the three
    hardening mechanisms and last for that reason.
16. [Run a workload with a read-only root filesystem](../../questions/advanced-containers/readonly-root-filesystem.html)
    — A read-only root filesystem turns the copy-up and mount knowledge above
    into an enforced runtime policy.
17. [Explain user namespace UID and GID mapping](../../questions/advanced-containers/user-namespace-mapping.html)
    — UID mapping is the strongest answer to a container that needs root, and it
    presumes the capability and mount tiers before it.
18. [Evaluate rootless container runtime boundaries](../../questions/advanced-containers/rootless-runtime-boundaries.html)
    — Rootless operation composes every namespace and capability lesson into a
    whole runtime, and its limits read only then.
19. [Choose runtime isolation tiers for a multi-tenant platform](../../questions/advanced-containers/tenant-isolation-strategy.html)
    — Tiered isolation for multi-tenant platforms spends the whole primitive
    tier deciding what each tier of tenant may risk.
20. [Establish a container runtime hardening baseline](../../questions/advanced-containers/runtime-hardening-baseline.html)
    — A baseline turns per-mechanism hardening into a versioned standard the
    exceptions below are measured against.
21. [Review a privileged-container exception](../../questions/advanced-containers/privileged-container-exception.html)
    — Reviewing a privileged exception is the baseline applied to the one
    workload that refuses to meet it.
22. [Govern runtime-isolation exceptions across an organization](../../questions/advanced-containers/runtime-exception-governance.html)
    — Governing exceptions across an organization replaces folklore with owners,
    expiry dates, and records.
23. [Set a multi-year container runtime isolation roadmap](../../questions/advanced-containers/runtime-isolation-roadmap.html)
    — A multi-year roadmap prices the isolation tiers the platform will owe as
    its workloads and adversaries mature.
24. [Respond to a suspected container escape](../../questions/advanced-containers/container-escape-incident.html)
    — The escape response is the incident face of everything above: what was
    claimed, what held, and what to preserve.
25. [Design container-host incident readiness for isolation failures](../../questions/advanced-containers/container-host-incident-readiness.html)
    — Readiness design closes the Theme by making escape response a rehearsed
    platform capability instead of improvisation.
