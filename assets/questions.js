window.questions = [
  {"title": "Apply Linux capabilities with least privilege", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "linux", "capabilities", "security", "least-privilege"], "path": "questions/advanced-containers/capabilities-least-privilege.html"},
  {"title": "Explain cgroup resource accounting for containers", "theme": "advanced-containers", "difficulty": "middle", "type": "theory", "tags": ["containers", "linux", "cgroups", "resource-limits", "performance"], "path": "questions/advanced-containers/cgroup-resource-accounting.html"},
  {"title": "Lead a cgroup v2 migration for container hosts", "theme": "advanced-containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "linux", "cgroups", "performance", "governance", "reliability"], "path": "questions/advanced-containers/cgroup-v2-migration.html"},
  {"title": "Respond to a suspected container escape", "theme": "advanced-containers", "difficulty": "senior", "type": "troubleshooting", "tags": ["containers", "security", "incident-response", "process-isolation", "troubleshooting"], "path": "questions/advanced-containers/container-escape-incident.html"},
  {"title": "Design container-host incident readiness for isolation failures", "theme": "advanced-containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "security", "incident-response", "observability", "governance", "reliability"], "path": "questions/advanced-containers/container-host-incident-readiness.html"},
  {"title": "Explain the Linux primitives behind container isolation", "theme": "advanced-containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "linux", "namespaces", "cgroups", "process-isolation"], "path": "questions/advanced-containers/container-isolation-basics.html"},
  {"title": "Diagnose cgroup CPU throttling in a container", "theme": "advanced-containers", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "linux", "cgroups", "cpu", "performance", "troubleshooting"], "path": "questions/advanced-containers/cpu-quotas-and-throttling.html"},
  {"title": "Control device access for a container workload", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "linux", "security", "least-privilege", "filesystem"], "path": "questions/advanced-containers/device-access-control.html"},
  {"title": "Investigate a container cgroup memory limit and OOM kill", "theme": "advanced-containers", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "linux", "cgroups", "memory", "resource-limits", "troubleshooting"], "path": "questions/advanced-containers/memory-limits-and-oom.html"},
  {"title": "Explain mount namespaces and a container root filesystem", "theme": "advanced-containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "linux", "namespaces", "mount-namespace", "filesystem"], "path": "questions/advanced-containers/mount-namespace-basics.html"},
  {"title": "Decide when containers should share a namespace", "theme": "advanced-containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "linux", "namespaces", "networking", "process-isolation"], "path": "questions/advanced-containers/namespace-sharing-tradeoffs.html"},
  {"title": "Explain a container network namespace", "theme": "advanced-containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "linux", "namespaces", "networking", "process-isolation"], "path": "questions/advanced-containers/network-namespace-basics.html"},
  {"title": "Explain overlay filesystem copy-up and container writes", "theme": "advanced-containers", "difficulty": "senior", "type": "theory", "tags": ["containers", "filesystem", "images", "performance", "storage"], "path": "questions/advanced-containers/overlay-filesystem-copy-up.html"},
  {"title": "Explain PID namespaces and container process visibility", "theme": "advanced-containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "linux", "namespaces", "pid-1", "process-isolation"], "path": "questions/advanced-containers/pid-namespace-basics.html"},
  {"title": "Design correct PID 1 signal handling in a container", "theme": "advanced-containers", "difficulty": "junior", "type": "scenario", "tags": ["containers", "linux", "pid-1", "signals", "reliability"], "path": "questions/advanced-containers/pid-one-signal-handling.html"},
  {"title": "Use the cgroup PIDs controller to contain fork storms", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "linux", "cgroups", "pid-1", "reliability", "security"], "path": "questions/advanced-containers/pids-controller-protection.html"},
  {"title": "Review a privileged-container exception", "theme": "advanced-containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "security", "capabilities", "process-isolation", "governance"], "path": "questions/advanced-containers/privileged-container-exception.html"},
  {"title": "Run a workload with a read-only root filesystem", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "filesystem", "security", "least-privilege", "reliability"], "path": "questions/advanced-containers/readonly-root-filesystem.html"},
  {"title": "Evaluate rootless container runtime boundaries", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "linux", "rootless", "user-namespace", "security"], "path": "questions/advanced-containers/rootless-runtime-boundaries.html"},
  {"title": "Govern runtime-isolation exceptions across an organization", "theme": "advanced-containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "security", "governance", "capabilities", "rootless", "platform-engineering"], "path": "questions/advanced-containers/runtime-exception-governance.html"},
  {"title": "Establish a container runtime hardening baseline", "theme": "advanced-containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "security", "seccomp", "capabilities", "rootless", "governance"], "path": "questions/advanced-containers/runtime-hardening-baseline.html"},
  {"title": "Set a multi-year container runtime isolation roadmap", "theme": "advanced-containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "security", "governance", "cgroups", "rootless", "platform-engineering"], "path": "questions/advanced-containers/runtime-isolation-roadmap.html"},
  {"title": "Design a seccomp profile for a container workload", "theme": "advanced-containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "linux", "seccomp", "security", "least-privilege"], "path": "questions/advanced-containers/seccomp-profile-design.html"},
  {"title": "Choose runtime isolation tiers for a multi-tenant platform", "theme": "advanced-containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "security", "process-isolation", "governance", "platform-engineering"], "path": "questions/advanced-containers/tenant-isolation-strategy.html"},
  {"title": "Explain user namespace UID and GID mapping", "theme": "advanced-containers", "difficulty": "middle", "type": "theory", "tags": ["containers", "linux", "namespaces", "user-namespace", "security"], "path": "questions/advanced-containers/user-namespace-mapping.html"},
  {"title": "Explain the role of an API gateway", "theme": "backend-architecture", "difficulty": "junior", "type": "theory", "tags": ["http", "networking", "security"], "path": "questions/backend-architecture/api-gateway-basics.html"},
  {"title": "Govern API versioning and deprecation", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["http", "change-management", "dependencies", "cba"], "path": "questions/backend-architecture/api-versioning-policy.html"},
  {"title": "Manage an architecture decision portfolio", "theme": "backend-architecture", "difficulty": "staff", "type": "theory", "tags": ["governance", "leadership", "change-management"], "path": "questions/backend-architecture/architecture-decision-portfolio.html"},
  {"title": "Separate authentication from authorization", "theme": "backend-architecture", "difficulty": "middle", "type": "theory", "tags": ["security", "iam", "jwt", "cba"], "path": "questions/backend-architecture/authentication-authorization-boundary.html"},
  {"title": "Design a durable background job contract", "theme": "backend-architecture", "difficulty": "middle", "type": "scenario", "tags": ["message-queues", "reliability", "event-driven"], "path": "questions/backend-architecture/background-job-contract.html"},
  {"title": "Diagnose why a service never appears in the Backstage catalog", "theme": "backend-architecture", "difficulty": "senior", "type": "troubleshooting", "tags": ["architecture", "platform-engineering", "troubleshooting", "automation", "governance", "cba"], "path": "questions/backend-architecture/backstage-catalog-ingestion-triage.html"},
  {"title": "Decide whether a Backstage capability belongs in a frontend or backend plugin", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["architecture", "platform-engineering", "security", "least-privilege", "automation", "cba"], "path": "questions/backend-architecture/backstage-plugin-boundaries.html"},
  {"title": "Move a Backstage instance from local defaults to production configuration", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["architecture", "platform-engineering", "configuration-management", "security", "iam", "cba"], "path": "questions/backend-architecture/backstage-production-configuration.html"},
  {"title": "Keep Backstage UI customizations upgradable", "theme": "backend-architecture", "difficulty": "staff", "type": "scenario", "tags": ["architecture", "platform-engineering", "change-management", "quality", "governance", "cba"], "path": "questions/backend-architecture/backstage-ui-customization-upgrades.html"},
  {"title": "Design cache invalidation for mutable data", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["performance", "databases", "reliability"], "path": "questions/backend-architecture/cache-invalidation-strategy.html"},
  {"title": "Operate a circuit breaker", "theme": "backend-architecture", "difficulty": "middle", "type": "troubleshooting", "tags": ["reliability", "availability", "monitoring"], "path": "questions/backend-architecture/circuit-breaker-operations.html"},
  {"title": "Design cursor pagination", "theme": "backend-architecture", "difficulty": "middle", "type": "theory", "tags": ["databases", "performance", "http"], "path": "questions/backend-architecture/cursor-pagination.html"},
  {"title": "Establish data governance architecture", "theme": "backend-architecture", "difficulty": "staff", "type": "scenario", "tags": ["security", "governance", "databases", "cba"], "path": "questions/backend-architecture/data-governance-architecture.html"},
  {"title": "Roll out a backward-compatible database migration", "theme": "backend-architecture", "difficulty": "middle", "type": "scenario", "tags": ["databases", "deployment", "change-management"], "path": "questions/backend-architecture/database-migration-safety.html"},
  {"title": "Design a developer-portal catalog contract teams can trust", "theme": "backend-architecture", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "governance", "reliability", "automation", "cnpa", "cba"], "path": "questions/backend-architecture/developer-portal-catalog-contract.html"},
  {"title": "Govern evolutionary backend architecture", "theme": "backend-architecture", "difficulty": "staff", "type": "theory", "tags": ["governance", "change-management", "reliability", "cba"], "path": "questions/backend-architecture/evolutionary-architecture-governance.html"},
  {"title": "Apply HTTP caching safely", "theme": "backend-architecture", "difficulty": "junior", "type": "theory", "tags": ["http", "performance", "availability"], "path": "questions/backend-architecture/http-caching-basics.html"},
  {"title": "Implement idempotency keys for mutations", "theme": "backend-architecture", "difficulty": "middle", "type": "scenario", "tags": ["http", "databases", "reliability"], "path": "questions/backend-architecture/idempotency-keys.html"},
  {"title": "Decompose a monolith without a rewrite", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["dependencies", "deployment", "reliability"], "path": "questions/backend-architecture/monolith-decomposition.html"},
  {"title": "Design multi-tenant isolation", "theme": "backend-architecture", "difficulty": "senior", "type": "scenario", "tags": ["security", "databases", "iam"], "path": "questions/backend-architecture/multi-tenancy-isolation.html"},
  {"title": "Set platform and product-service boundaries", "theme": "backend-architecture", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "governance", "dependencies", "cnpa"], "path": "questions/backend-architecture/platform-boundary-strategy.html"},
  {"title": "Design an API rate-limiting policy", "theme": "backend-architecture", "difficulty": "middle", "type": "scenario", "tags": ["http", "availability", "security"], "path": "questions/backend-architecture/rate-limiting-policy.html"},
  {"title": "Prioritize backend resilience investments", "theme": "backend-architecture", "difficulty": "staff", "type": "scenario", "tags": ["reliability", "availability", "capacity-planning"], "path": "questions/backend-architecture/resilience-investment-model.html"},
  {"title": "Design resource-oriented HTTP endpoints", "theme": "backend-architecture", "difficulty": "junior", "type": "theory", "tags": ["http", "networking", "dependencies"], "path": "questions/backend-architecture/rest-resource-semantics.html"},
  {"title": "Make backend retries safe", "theme": "backend-architecture", "difficulty": "middle", "type": "troubleshooting", "tags": ["reliability", "availability", "http"], "path": "questions/backend-architecture/retry-backoff-and-jitter.html"},
  {"title": "Coordinate a saga with compensations", "theme": "backend-architecture", "difficulty": "senior", "type": "theory", "tags": ["event-driven", "reliability", "databases"], "path": "questions/backend-architecture/saga-compensation.html"},
  {"title": "Design a stateless backend service", "theme": "backend-architecture", "difficulty": "junior", "type": "theory", "tags": ["availability", "cloud", "load", "cba"], "path": "questions/backend-architecture/stateless-service-design.html"},
  {"title": "Choose synchronous versus asynchronous API processing", "theme": "backend-architecture", "difficulty": "junior", "type": "scenario", "tags": ["http", "event-driven", "message-queues"], "path": "questions/backend-architecture/synchronous-versus-asynchronous-api.html"},
  {"title": "Choose a transaction boundary", "theme": "backend-architecture", "difficulty": "middle", "type": "theory", "tags": ["databases", "reliability", "dependencies"], "path": "questions/backend-architecture/transaction-boundaries.html"},
  {"title": "Use a transactional outbox for event publication", "theme": "backend-architecture", "difficulty": "middle", "type": "theory", "tags": ["databases", "event-driven", "reliability"], "path": "questions/backend-architecture/transactional-outbox.html"},
  {"title": "Explain cache-aside basics", "theme": "caching", "difficulty": "junior", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-aside-basics.html"},
  {"title": "Build a cache capacity and cost model", "theme": "caching", "difficulty": "staff", "type": "scenario", "tags": ["caching", "capacity-planning", "cost-optimization", "performance", "memory"], "path": "questions/caching/cache-capacity-cost-model.html"},
  {"title": "Evaluate cache consistency trade-offs", "theme": "caching", "difficulty": "senior", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-consistency-tradeoffs.html"},
  {"title": "Choose a cache eviction policy", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-eviction-policy.html"},
  {"title": "Interpret a cache hit ratio honestly", "theme": "caching", "difficulty": "junior", "type": "theory", "tags": ["caching", "performance", "monitoring", "metrics"], "path": "questions/caching/cache-hit-ratio-basics.html"},
  {"title": "Design cache invalidation policy", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-invalidation-policy.html"},
  {"title": "Design cache keys safely", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-key-design.html"},
  {"title": "Observe cache health", "theme": "caching", "difficulty": "middle", "type": "troubleshooting", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-observability.html"},
  {"title": "Contain the blast radius of a cache outage", "theme": "caching", "difficulty": "senior", "type": "troubleshooting", "tags": ["caching", "reliability", "availability", "incident-response", "troubleshooting"], "path": "questions/caching/cache-outage-blast-radius.html"},
  {"title": "Compare cache placement layers", "theme": "caching", "difficulty": "junior", "type": "theory", "tags": ["caching", "cdn", "http", "architecture"], "path": "questions/caching/cache-placement-layers.html"},
  {"title": "Defend a shared cache against poisoning", "theme": "caching", "difficulty": "senior", "type": "scenario", "tags": ["caching", "security", "http", "cdn", "availability"], "path": "questions/caching/cache-poisoning-defense.html"},
  {"title": "Set SLOs that survive a degraded cache", "theme": "caching", "difficulty": "staff", "type": "scenario", "tags": ["caching", "sre", "reliability", "observability", "monitoring"], "path": "questions/caching/cache-slo-degradation-policy.html"},
  {"title": "Prevent a cache stampede", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-stampede-control.html"},
  {"title": "Design a cache warming strategy", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "performance", "reliability", "databases"], "path": "questions/caching/cache-warming-strategy.html"},
  {"title": "Decide whether a cache is the right answer", "theme": "caching", "difficulty": "staff", "type": "theory", "tags": ["caching", "architecture", "performance", "governance", "capacity-planning"], "path": "questions/caching/caching-strategy-decision.html"},
  {"title": "Scope a CDN cache key correctly", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "cdn", "http", "security"], "path": "questions/caching/cdn-cache-key-scoping.html"},
  {"title": "Investigate a cache that stopped hitting", "theme": "caching", "difficulty": "junior", "type": "troubleshooting", "tags": ["caching", "troubleshooting", "latency", "monitoring"], "path": "questions/caching/cold-cache-troubleshooting.html"},
  {"title": "Mitigate a hot key in a sharded cache", "theme": "caching", "difficulty": "middle", "type": "troubleshooting", "tags": ["caching", "redis", "performance", "troubleshooting", "latency"], "path": "questions/caching/hot-key-mitigation.html"},
  {"title": "Operate Memcached memory and slab allocation", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "memcached", "memory", "capacity", "performance"], "path": "questions/caching/memcached-slab-tuning.html"},
  {"title": "Design cache coherence across regions", "theme": "caching", "difficulty": "staff", "type": "scenario", "tags": ["caching", "distributed-systems", "architecture", "reliability", "latency"], "path": "questions/caching/multi-region-cache-coherence.html"},
  {"title": "Cache negative results safely", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "reliability", "availability", "databases"], "path": "questions/caching/negative-caching.html"},
  {"title": "Explain a read-through cache", "theme": "caching", "difficulty": "junior", "type": "theory", "tags": ["caching", "databases", "architecture", "reliability"], "path": "questions/caching/read-through-cache-basics.html"},
  {"title": "Operate Redis replication and failover for a cache tier", "theme": "caching", "difficulty": "senior", "type": "scenario", "tags": ["caching", "redis", "reliability", "availability", "incident-response"], "path": "questions/caching/redis-failover-operations.html"},
  {"title": "Tune Redis maxmemory and eviction behaviour", "theme": "caching", "difficulty": "middle", "type": "scenario", "tags": ["caching", "redis", "memory", "capacity", "reliability"], "path": "questions/caching/redis-maxmemory-tuning.html"},
  {"title": "Govern a shared cache platform", "theme": "caching", "difficulty": "staff", "type": "scenario", "tags": ["caching", "platform-engineering", "governance", "reliability", "cost-optimization"], "path": "questions/caching/shared-cache-platform-governance.html"},
  {"title": "Set a staleness budget with stale-while-revalidate", "theme": "caching", "difficulty": "senior", "type": "scenario", "tags": ["caching", "http", "reliability", "availability", "latency"], "path": "questions/caching/stale-while-revalidate-budget.html"},
  {"title": "Choose a TTL for a cached value", "theme": "caching", "difficulty": "junior", "type": "scenario", "tags": ["caching", "performance", "reliability", "latency"], "path": "questions/caching/ttl-selection-basics.html"},
  {"title": "Choose between write-through and write-behind caching", "theme": "caching", "difficulty": "senior", "type": "theory", "tags": ["caching", "databases", "architecture", "reliability", "distributed-systems"], "path": "questions/caching/write-through-versus-write-behind.html"},
  {"title": "Build a safe Kubernetes cluster upgrade runbook", "theme": "certification-last-minute-review", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "cka", "reliability", "rolling-update", "troubleshooting"], "path": "questions/certification-last-minute-review/cluster-upgrade-runbook.html"},
  {"title": "Choose ConfigMaps and Secrets without overstating protection", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "theory", "tags": ["kubernetes", "security", "cka", "ckad", "kcsa"], "path": "questions/certification-last-minute-review/configmap-secret-boundaries.html"},
  {"title": "Triage an unavailable Kubernetes control plane", "theme": "certification-last-minute-review", "difficulty": "senior", "type": "troubleshooting", "tags": ["kubernetes", "cka", "troubleshooting", "incident-response", "reliability"], "path": "questions/certification-last-minute-review/control-plane-triage.html"},
  {"title": "Verify a Deployment rollout and recover safely", "theme": "certification-last-minute-review", "difficulty": "junior", "type": "scenario", "tags": ["kubernetes", "deployment", "cka", "ckad", "kcna", "rolling-update"], "path": "questions/certification-last-minute-review/deployment-rollout-check.html"},
  {"title": "Debug Kubernetes DNS before changing application code", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "dns", "networking", "cka", "ckad", "troubleshooting"], "path": "questions/certification-last-minute-review/dns-debugging.html"},
  {"title": "Plan and validate an etcd backup and restore", "theme": "certification-last-minute-review", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "storage", "cka", "reliability", "incident-response"], "path": "questions/certification-last-minute-review/etcd-backup-restore.html"},
  {"title": "Diagnose HTTP routing through Ingress or Gateway APIs", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "networking", "http", "tls", "cka", "ckad", "troubleshooting"], "path": "questions/certification-last-minute-review/ingress-gateway-routing.html"},
  {"title": "Operate Jobs and CronJobs without uncontrolled retries", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "automation", "reliability", "cka", "ckad"], "path": "questions/certification-last-minute-review/job-cronjob-cleanup.html"},
  {"title": "Switch kubectl contexts safely under time pressure", "theme": "certification-last-minute-review", "difficulty": "junior", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "kcna", "troubleshooting"], "path": "questions/certification-last-minute-review/kubectl-context-safety.html"},
  {"title": "Distinguish namespaced and cluster-scoped Kubernetes resources", "theme": "certification-last-minute-review", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "cka", "ckad", "kcna"], "path": "questions/certification-last-minute-review/namespace-scope.html"},
  {"title": "Reason about NetworkPolicy enforcement and default deny", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "theory", "tags": ["kubernetes", "networking", "security", "cka", "cks", "kcsa"], "path": "questions/certification-last-minute-review/networkpolicy-semantics.html"},
  {"title": "Use PodDisruptionBudgets without blocking maintenance", "theme": "certification-last-minute-review", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "availability", "cka", "reliability", "rolling-update"], "path": "questions/certification-last-minute-review/pod-disruption-budget.html"},
  {"title": "Read Pod phase, container state, and restart evidence", "theme": "certification-last-minute-review", "difficulty": "junior", "type": "troubleshooting", "tags": ["kubernetes", "containers", "cka", "ckad", "kcna", "troubleshooting"], "path": "questions/certification-last-minute-review/pod-lifecycle-signals.html"},
  {"title": "Select startup, readiness, and liveness probes", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "healthchecks", "reliability", "cka", "ckad"], "path": "questions/certification-last-minute-review/probe-selection.html"},
  {"title": "Debug a PersistentVolumeClaim that stays Pending", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "storage", "volumes", "cka", "ckad", "troubleshooting"], "path": "questions/certification-last-minute-review/pvc-binding.html"},
  {"title": "Diagnose an RBAC denial without broadening access", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "security", "iam", "least-privilege", "cka", "ckad", "cks", "kcsa"], "path": "questions/certification-last-minute-review/rbac-least-privilege.html"},
  {"title": "Explain requests, limits, QoS, and a Pending Pod", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "cpu", "memory", "resource-limits", "cka", "ckad", "troubleshooting"], "path": "questions/certification-last-minute-review/resource-requests-limits.html"},
  {"title": "Combine node selectors, affinity, taints, and tolerations", "theme": "certification-last-minute-review", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "availability", "troubleshooting"], "path": "questions/certification-last-minute-review/scheduling-constraints.html"},
  {"title": "Review a Pod security context for least privilege", "theme": "certification-last-minute-review", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "containers", "least-privilege", "cks", "kcsa"], "path": "questions/certification-last-minute-review/security-context-review.html"},
  {"title": "Debug a Service with no reachable backends", "theme": "certification-last-minute-review", "difficulty": "junior", "type": "troubleshooting", "tags": ["kubernetes", "networking", "dns", "cka", "ckad", "kcna", "troubleshooting"], "path": "questions/certification-last-minute-review/service-endpoints-debug.html"},
  {"title": "Keep certification preparation ethical and operationally useful", "theme": "certification-last-minute-review", "difficulty": "staff", "type": "theory", "tags": ["kubernetes", "cka", "ckad", "cks", "kcna", "governance"], "path": "questions/certification-last-minute-review/staff-certification-boundaries.html"},
  {"title": "Prioritize certification review under a two-hour deadline", "theme": "certification-last-minute-review", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "cks", "kcna", "reliability"], "path": "questions/certification-last-minute-review/staff-certification-prioritization.html"},
  {"title": "Evaluate a Kubernetes disaster-recovery exercise", "theme": "certification-last-minute-review", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "reliability", "storage", "incident-response", "cka"], "path": "questions/certification-last-minute-review/staff-disaster-recovery-exercise.html"},
  {"title": "Lead a Kubernetes incident while preserving recovery options", "theme": "certification-last-minute-review", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "incident-response", "troubleshooting", "reliability", "cka"], "path": "questions/certification-last-minute-review/staff-incident-command.html"},
  {"title": "Design platform guardrails that retain team autonomy", "theme": "certification-last-minute-review", "difficulty": "staff", "type": "theory", "tags": ["kubernetes", "platform-engineering", "security", "governance", "reliability", "cks"], "path": "questions/certification-last-minute-review/staff-platform-guardrails.html"},
  {"title": "Abort a running chaos experiment", "theme": "chaos-engineering", "difficulty": "junior", "type": "troubleshooting", "tags": ["chaos-engineering", "incident-response", "blast-radius", "operations"], "path": "questions/chaos-engineering/abort-a-running-experiment.html"},
  {"title": "Choose a first chaos experiment safely", "theme": "chaos-engineering", "difficulty": "junior", "type": "scenario", "tags": ["chaos-engineering", "fault-injection", "blast-radius", "reliability"], "path": "questions/chaos-engineering/choose-a-first-chaos-experiment.html"},
  {"title": "Decide whether to experiment in production or staging", "theme": "chaos-engineering", "difficulty": "senior", "type": "scenario", "tags": ["chaos-engineering", "experimentation", "governance", "reliability"], "path": "questions/chaos-engineering/choose-production-or-staging.html"},
  {"title": "Control the blast radius of an experiment", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "blast-radius", "fault-injection", "availability"], "path": "questions/chaos-engineering/control-the-blast-radius.html"},
  {"title": "Decide when not to run a chaos experiment", "theme": "chaos-engineering", "difficulty": "staff", "type": "scenario", "tags": ["chaos-engineering", "governance", "change-management", "reliability"], "path": "questions/chaos-engineering/decide-when-not-to-run-an-experiment.html"},
  {"title": "Define chaos engineering and what it is for", "theme": "chaos-engineering", "difficulty": "junior", "type": "theory", "tags": ["chaos-engineering", "resilience", "reliability", "sre"], "path": "questions/chaos-engineering/define-chaos-engineering.html"},
  {"title": "Design a hypothesis-driven chaos experiment", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "experimentation", "resilience", "testing-strategy"], "path": "questions/chaos-engineering/design-a-hypothesis-driven-experiment.html"},
  {"title": "Diagnose an experiment that caused a real outage", "theme": "chaos-engineering", "difficulty": "senior", "type": "troubleshooting", "tags": ["chaos-engineering", "incident-response", "blast-radius", "troubleshooting"], "path": "questions/chaos-engineering/diagnose-an-experiment-that-caused-an-outage.html"},
  {"title": "Exhaust CPU and memory deliberately", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "fault-injection", "cpu", "memory"], "path": "questions/chaos-engineering/exhaust-cpu-and-memory.html"},
  {"title": "Exhaust disk space and file descriptors", "theme": "chaos-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["chaos-engineering", "fault-injection", "disk", "file-descriptors"], "path": "questions/chaos-engineering/exhaust-disk-and-file-descriptors.html"},
  {"title": "Facilitate a game day", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "game-day", "incident-response", "operations"], "path": "questions/chaos-engineering/facilitate-a-game-day.html"},
  {"title": "Govern consent and ethics for production experiments", "theme": "chaos-engineering", "difficulty": "staff", "type": "scenario", "tags": ["chaos-engineering", "governance", "security", "experimentation"], "path": "questions/chaos-engineering/govern-consent-for-production-experiments.html"},
  {"title": "Inject latency into a single dependency", "theme": "chaos-engineering", "difficulty": "junior", "type": "scenario", "tags": ["chaos-engineering", "fault-injection", "latency", "networking"], "path": "questions/chaos-engineering/inject-latency-into-a-dependency.html"},
  {"title": "Inject packet loss and network partitions", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "fault-injection", "packet-loss", "networking"], "path": "questions/chaos-engineering/inject-packet-loss-and-partitions.html"},
  {"title": "Justify the cost of a chaos engineering programme", "theme": "chaos-engineering", "difficulty": "staff", "type": "scenario", "tags": ["chaos-engineering", "cost-optimization", "governance", "leadership"], "path": "questions/chaos-engineering/justify-the-cost-of-a-chaos-programme.html"},
  {"title": "Measure whether resilience actually improved", "theme": "chaos-engineering", "difficulty": "staff", "type": "scenario", "tags": ["chaos-engineering", "resilience", "metrics", "reliability"], "path": "questions/chaos-engineering/measure-resilience-improvement.html"},
  {"title": "Run a chaos engineering programme across many teams", "theme": "chaos-engineering", "difficulty": "staff", "type": "scenario", "tags": ["chaos-engineering", "platform-engineering", "governance", "leadership"], "path": "questions/chaos-engineering/run-a-chaos-engineering-programme.html"},
  {"title": "Run data-layer chaos without risking the data", "theme": "chaos-engineering", "difficulty": "senior", "type": "scenario", "tags": ["chaos-engineering", "databases", "storage", "recovery"], "path": "questions/chaos-engineering/run-data-layer-chaos-safely.html"},
  {"title": "Run pod-level chaos in Kubernetes", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "kubernetes", "fault-injection", "availability"], "path": "questions/chaos-engineering/run-pod-level-chaos-in-kubernetes.html"},
  {"title": "Select experiments from incident history", "theme": "chaos-engineering", "difficulty": "senior", "type": "scenario", "tags": ["chaos-engineering", "incident-management", "experimentation", "reliability"], "path": "questions/chaos-engineering/select-experiments-from-incident-history.html"},
  {"title": "Simulate a downstream dependency failure", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "fault-injection", "dependencies", "resilience"], "path": "questions/chaos-engineering/simulate-a-downstream-dependency-failure.html"},
  {"title": "Simulate an availability-zone or region failure", "theme": "chaos-engineering", "difficulty": "senior", "type": "scenario", "tags": ["chaos-engineering", "cloud", "availability", "capacity-planning"], "path": "questions/chaos-engineering/simulate-a-zone-or-region-failure.html"},
  {"title": "State a steady-state hypothesis", "theme": "chaos-engineering", "difficulty": "junior", "type": "theory", "tags": ["chaos-engineering", "experimentation", "metrics", "monitoring"], "path": "questions/chaos-engineering/state-a-steady-state-hypothesis.html"},
  {"title": "Terminate a node and verify real recovery", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "kubernetes", "recovery", "capacity"], "path": "questions/chaos-engineering/terminate-a-node-and-verify-recovery.html"},
  {"title": "Verify observability before injecting a fault", "theme": "chaos-engineering", "difficulty": "middle", "type": "scenario", "tags": ["chaos-engineering", "observability", "monitoring", "metrics"], "path": "questions/chaos-engineering/verify-observability-before-injecting.html"},
  {"title": "Configure production environment protection", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "deployment", "security", "governance"], "path": "questions/ci-cd/approval-environment-protection.html"},
  {"title": "Set Argo CD Application project boundaries", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-cd", "capa", "security", "least-privilege", "cgoa"], "path": "questions/ci-cd/argo-cd-application-project-boundaries.html"},
  {"title": "Explain Argo CD Application synchronization", "theme": "ci-cd", "difficulty": "junior", "type": "theory", "tags": ["ci-cd", "kubernetes", "argo", "argo-cd", "capa", "git", "deployment", "cnpa", "cgoa"], "path": "questions/ci-cd/argo-cd-application-sync.html"},
  {"title": "Choose Helm or Kustomize rendering in Argo CD", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-cd", "capa", "configuration-management", "cgoa"], "path": "questions/ci-cd/argo-cd-helm-kustomize-rendering.html"},
  {"title": "Respond to Argo CD drift without masking an incident", "theme": "ci-cd", "difficulty": "senior", "type": "troubleshooting", "tags": ["ci-cd", "kubernetes", "argo", "argo-cd", "capa", "troubleshooting", "reliability", "cnpe", "cnpa", "cgoa"], "path": "questions/ci-cd/argo-cd-reconciliation-drift.html"},
  {"title": "Explain the Argo Events event path", "theme": "ci-cd", "difficulty": "junior", "type": "theory", "tags": ["ci-cd", "kubernetes", "argo", "argo-events", "capa", "event-driven", "automation", "cgoa"], "path": "questions/ci-cd/argo-events-architecture.html"},
  {"title": "Design an Argo Events Sensor for a production trigger", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-events", "capa", "event-driven", "security", "cgoa"], "path": "questions/ci-cd/argo-events-sensor-dependencies.html"},
  {"title": "Define an Argo Rollouts AnalysisTemplate safely", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-rollouts", "capa", "observability", "reliability", "cgoa"], "path": "questions/ci-cd/argo-rollouts-analysis.html"},
  {"title": "Choose a progressive Argo Rollouts strategy", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-rollouts", "capa", "deployment", "reliability", "cnpe", "cgoa"], "path": "questions/ci-cd/argo-rollouts-progressive-delivery.html"},
  {"title": "Pass artifacts safely between Argo Workflow steps", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-workflows", "capa", "storage"], "path": "questions/ci-cd/argo-workflow-artifacts.html"},
  {"title": "Reuse Argo Workflow templates without losing control", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-workflows", "capa", "automation"], "path": "questions/ci-cd/argo-workflow-template-reuse.html"},
  {"title": "Model failure and parallelism in an Argo Workflow DAG", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo", "argo-workflows", "capa", "reliability"], "path": "questions/ci-cd/argo-workflows-dag-failure.html"},
  {"title": "Explain when to use Argo Workflows", "theme": "ci-cd", "difficulty": "junior", "type": "theory", "tags": ["ci-cd", "kubernetes", "argo", "argo-workflows", "capa", "automation"], "path": "questions/ci-cd/argo-workflows-fundamentals.html"},
  {"title": "Set artifact retention and promotion rules", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "delivery", "supply-chain", "reliability"], "path": "questions/ci-cd/artifact-retention-and-promotion.html"},
  {"title": "Produce a reproducible Backstage backend image from its Yarn workspace", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "containers", "docker", "build-cache", "delivery", "platform-engineering", "cba"], "path": "questions/ci-cd/backstage-app-build-and-image.html"},
  {"title": "Plan a blue-green production cutover", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "deployment", "reliability", "availability", "cgoa"], "path": "questions/ci-cd/blue-green-cutover.html"},
  {"title": "Cache CI dependencies without using stale outputs", "theme": "ci-cd", "difficulty": "junior", "type": "scenario", "tags": ["ci-cd", "automation", "reliability", "security", "cba"], "path": "questions/ci-cd/cache-dependencies-safely.html"},
  {"title": "Decide whether to advance or stop a canary deployment", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "deployment", "monitoring", "reliability", "cgoa"], "path": "questions/ci-cd/canary-deployment-decision.html"},
  {"title": "Build a CI/CD cost and capacity model", "theme": "ci-cd", "difficulty": "staff", "type": "scenario", "tags": ["ci-cd", "cost-optimization", "capacity-planning", "monitoring", "governance"], "path": "questions/ci-cd/ci-cd-cost-capacity-model.html"},
  {"title": "Distinguish continuous integration, delivery, and deployment", "theme": "ci-cd", "difficulty": "junior", "type": "theory", "tags": ["ci-cd", "automation", "delivery", "deployment", "kcna", "cgoa"], "path": "questions/ci-cd/ci-versus-cd.html"},
  {"title": "Prevent conflicting production deployments", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "deployment", "reliability", "automation"], "path": "questions/ci-cd/deployment-concurrency-control.html"},
  {"title": "Recover the delivery platform during an outage", "theme": "ci-cd", "difficulty": "staff", "type": "scenario", "tags": ["ci-cd", "incident-response", "reliability", "security", "platform-engineering"], "path": "questions/ci-cd/disaster-recover-delivery-platform.html"},
  {"title": "Explain how Flux reconciles a cluster from a source", "theme": "ci-cd", "difficulty": "middle", "type": "theory", "tags": ["ci-cd", "kubernetes", "git", "flux", "gitops", "deployment", "automation", "cgoa"], "path": "questions/ci-cd/flux-reconciliation-engine.html"},
  {"title": "Close the feedback loop for a GitOps deployment", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "argo-cd", "gitops", "monitoring", "deployment", "observability", "cgoa"], "path": "questions/ci-cd/gitops-feedback-loop.html"},
  {"title": "Explain the four GitOps principles", "theme": "ci-cd", "difficulty": "junior", "type": "theory", "tags": ["ci-cd", "git", "kubernetes", "deployment", "delivery", "automation", "cgoa"], "path": "questions/ci-cd/gitops-principles.html"},
  {"title": "Choose a pull-based reconciler or a push-based deployment pipeline", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "kubernetes", "git", "argo-cd", "deployment", "architecture", "least-privilege", "cgoa"], "path": "questions/ci-cd/gitops-pull-versus-push-delivery.html"},
  {"title": "Why should CI publish immutable release artifacts?", "theme": "ci-cd", "difficulty": "middle", "type": "theory", "tags": ["ci-cd", "delivery", "supply-chain", "security", "cgoa"], "path": "questions/ci-cd/immutable-release-artifacts.html"},
  {"title": "Decide whether to freeze deployments during an incident", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "incident-response", "deployment", "reliability"], "path": "questions/ci-cd/incident-change-freeze.html"},
  {"title": "Apply least privilege to a workflow token", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "github-actions", "security", "least-privilege"], "path": "questions/ci-cd/least-privilege-workflow-token.html"},
  {"title": "Design a multi-team pipeline architecture", "theme": "ci-cd", "difficulty": "staff", "type": "scenario", "tags": ["ci-cd", "platform-engineering", "automation", "governance", "security", "cnpe", "cnpa"], "path": "questions/ci-cd/multi-team-pipeline-architecture.html"},
  {"title": "Parallelize a CI test suite safely", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "automation", "reliability", "monitoring"], "path": "questions/ci-cd/parallelize-test-suite.html"},
  {"title": "Design CI/CD quality gates for a service", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "delivery", "deployment", "automation", "security", "cgoa"], "path": "questions/ci-cd/pipeline-quality-gates.html"},
  {"title": "Establish organization-wide delivery standards", "theme": "ci-cd", "difficulty": "staff", "type": "scenario", "tags": ["ci-cd", "platform-engineering", "governance", "security", "reliability"], "path": "questions/ci-cd/platform-delivery-standards.html"},
  {"title": "Protect deployment secrets in CI/CD", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "security", "least-privilege", "deployment"], "path": "questions/ci-cd/protect-deployment-secrets.html"},
  {"title": "Triage a failed CI job from its logs", "theme": "ci-cd", "difficulty": "junior", "type": "troubleshooting", "tags": ["ci-cd", "debugging", "troubleshooting", "automation"], "path": "questions/ci-cd/read-ci-logs.html"},
  {"title": "Govern release risk across a product portfolio", "theme": "ci-cd", "difficulty": "staff", "type": "scenario", "tags": ["ci-cd", "governance", "deployment", "reliability", "monitoring"], "path": "questions/ci-cd/release-risk-governance.html"},
  {"title": "Handle flaky tests without masking regressions", "theme": "ci-cd", "difficulty": "middle", "type": "troubleshooting", "tags": ["ci-cd", "debugging", "reliability", "troubleshooting"], "path": "questions/ci-cd/retry-flaky-tests.html"},
  {"title": "Choose reusable workflow boundaries", "theme": "ci-cd", "difficulty": "middle", "type": "theory", "tags": ["ci-cd", "github-actions", "automation", "governance"], "path": "questions/ci-cd/reusable-workflow-boundaries.html"},
  {"title": "Design a deployment rollback", "theme": "ci-cd", "difficulty": "middle", "type": "scenario", "tags": ["ci-cd", "deployment", "reliability", "incident-response", "cgoa"], "path": "questions/ci-cd/roll-back-a-deployment.html"},
  {"title": "Produce a traceable semantic-version release", "theme": "ci-cd", "difficulty": "junior", "type": "scenario", "tags": ["ci-cd", "git", "delivery", "automation"], "path": "questions/ci-cd/semantic-version-release.html"},
  {"title": "Verify supply-chain provenance before deployment", "theme": "ci-cd", "difficulty": "senior", "type": "scenario", "tags": ["ci-cd", "supply-chain", "security", "deployment", "cnpa", "cgoa"], "path": "questions/ci-cd/supply-chain-provenance.html"},
  {"title": "Choose CI pipeline triggers", "theme": "ci-cd", "difficulty": "junior", "type": "scenario", "tags": ["ci-cd", "automation", "git", "delivery"], "path": "questions/ci-cd/trigger-a-pipeline.html"},
  {"title": "Configure target-tracking autoscaling safely", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "capacity-planning", "monitoring", "reliability"], "path": "questions/cloud/autoscaling-target-tracking.html"},
  {"title": "Establish cloud cost governance without blocking delivery", "theme": "cloud", "difficulty": "staff", "type": "scenario", "tags": ["aws", "cloud", "cost-optimization", "governance", "monitoring"], "path": "questions/cloud/cloud-finops-governance.html"},
  {"title": "Govern cloud identity at organization scale", "theme": "cloud", "difficulty": "staff", "type": "scenario", "tags": ["aws", "cloud", "iam", "security", "governance", "least-privilege"], "path": "questions/cloud/cloud-identity-governance.html"},
  {"title": "Lead an AWS workload incident response", "theme": "cloud", "difficulty": "senior", "type": "scenario", "tags": ["aws", "cloud", "incident-response", "observability", "reliability"], "path": "questions/cloud/cloud-incident-response.html"},
  {"title": "Plan a safe cloud migration wave", "theme": "cloud", "difficulty": "senior", "type": "scenario", "tags": ["aws", "cloud", "deployment", "reliability", "governance"], "path": "questions/cloud/cloud-migration-wave-plan.html"},
  {"title": "Prevent cloud service quotas from becoming an outage", "theme": "cloud", "difficulty": "senior", "type": "scenario", "tags": ["aws", "cloud", "capacity-planning", "reliability", "monitoring"], "path": "questions/cloud/cloud-quota-capacity-planning.html"},
  {"title": "Set a cloud reliability strategy across product teams", "theme": "cloud", "difficulty": "staff", "type": "scenario", "tags": ["aws", "cloud", "reliability", "availability", "observability", "governance"], "path": "questions/cloud/cloud-reliability-strategy.html"},
  {"title": "Choose an appropriate cloud service model", "theme": "cloud", "difficulty": "junior", "type": "theory", "tags": ["cloud", "security", "reliability"], "path": "questions/cloud/cloud-service-models.html"},
  {"title": "Use CloudTrail as audit evidence during a change investigation", "theme": "cloud", "difficulty": "middle", "type": "troubleshooting", "tags": ["aws", "cloud", "security", "observability", "troubleshooting"], "path": "questions/cloud/cloudtrail-audit-evidence.html"},
  {"title": "Design a CloudWatch alarm that supports action", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "monitoring", "reliability", "incident-response"], "path": "questions/cloud/cloudwatch-alarm-design.html"},
  {"title": "Govern data classification in cloud services", "theme": "cloud", "difficulty": "staff", "type": "scenario", "tags": ["aws", "cloud", "security", "governance", "storage"], "path": "questions/cloud/data-classification-governance.html"},
  {"title": "Design cloud disaster recovery from RTO and RPO", "theme": "cloud", "difficulty": "senior", "type": "scenario", "tags": ["aws", "cloud", "reliability", "availability", "incident-response"], "path": "questions/cloud/disaster-recovery-rto-rpo.html"},
  {"title": "Diagnose an unexpected AWS IAM authorization decision", "theme": "cloud", "difficulty": "middle", "type": "troubleshooting", "tags": ["aws", "iam", "cloud", "security", "least-privilege"], "path": "questions/cloud/iam-policy-evaluation.html"},
  {"title": "Establish a governed cloud landing zone", "theme": "cloud", "difficulty": "staff", "type": "scenario", "tags": ["aws", "cloud", "governance", "security", "platform-engineering", "cnpa", "must-know"], "path": "questions/cloud/landing-zone-governance.html"},
  {"title": "Apply least privilege to a cloud workload identity", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "iam", "cloud", "security", "least-privilege"], "path": "questions/cloud/least-privilege-workload-identity.html"},
  {"title": "Design a cloud load-balancer health check", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "availability", "reliability", "monitoring"], "path": "questions/cloud/load-balancer-health-checks.html"},
  {"title": "Prove a managed database backup can be restored", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "databases", "storage", "reliability"], "path": "questions/cloud/managed-database-backup-restore.html"},
  {"title": "Define AWS multi-account boundaries", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "security", "governance", "least-privilege"], "path": "questions/cloud/multi-account-boundaries.html"},
  {"title": "Choose object storage for durable application data", "theme": "cloud", "difficulty": "junior", "type": "scenario", "tags": ["aws", "cloud", "storage", "reliability"], "path": "questions/cloud/object-storage-durability.html"},
  {"title": "Provide controlled Internet egress from a private subnet", "theme": "cloud", "difficulty": "middle", "type": "scenario", "tags": ["aws", "cloud", "networking", "security", "reliability"], "path": "questions/cloud/private-subnet-egress.html"},
  {"title": "Choose Regions and Availability Zones for a workload", "theme": "cloud", "difficulty": "junior", "type": "theory", "tags": ["aws", "cloud", "availability", "reliability"], "path": "questions/cloud/regions-and-availability-zones.html"},
  {"title": "Design a cloud resource tagging strategy", "theme": "cloud", "difficulty": "junior", "type": "scenario", "tags": ["aws", "cloud", "cost-optimization", "governance"], "path": "questions/cloud/resource-tagging-strategy.html"},
  {"title": "Rotate cloud workload secrets without an outage", "theme": "cloud", "difficulty": "senior", "type": "scenario", "tags": ["aws", "cloud", "security", "iam", "reliability"], "path": "questions/cloud/secrets-manager-rotation.html"},
  {"title": "Choose security groups and network ACLs deliberately", "theme": "cloud", "difficulty": "middle", "type": "theory", "tags": ["aws", "cloud", "networking", "security"], "path": "questions/cloud/security-groups-and-network-acls.html"},
  {"title": "Explain the network boundaries of an AWS VPC", "theme": "cloud", "difficulty": "junior", "type": "theory", "tags": ["aws", "cloud", "networking", "security"], "path": "questions/cloud/vpc-network-foundations.html"},
  {"title": "Validate an Ansible change with check and diff mode", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-check-diff.html"},
  {"title": "Pin and update Ansible collections safely", "theme": "configuration-management", "difficulty": "senior", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "supply-chain", "security"], "path": "questions/configuration-management/ansible-collection-pinning.html"},
  {"title": "Set safe Ansible concurrency for a fleet change", "theme": "configuration-management", "difficulty": "senior", "type": "troubleshooting", "tags": ["ansible", "automation", "configuration-management", "reliability", "troubleshooting"], "path": "questions/configuration-management/ansible-concurrency-limits.html"},
  {"title": "Coordinate a configuration change with Ansible delegation", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "deployment", "reliability"], "path": "questions/configuration-management/ansible-delegation.html"},
  {"title": "Operate Ansible dynamic inventory safely", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "cloud", "reliability"], "path": "questions/configuration-management/ansible-dynamic-inventory.html"},
  {"title": "Handle Ansible task failures without concealing drift", "theme": "configuration-management", "difficulty": "middle", "type": "troubleshooting", "tags": ["ansible", "automation", "configuration-management", "troubleshooting", "reliability"], "path": "questions/configuration-management/ansible-error-handling.html"},
  {"title": "Gather and use Ansible facts deliberately", "theme": "configuration-management", "difficulty": "middle", "type": "theory", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-facts.html"},
  {"title": "Use Ansible handlers for service reloads", "theme": "configuration-management", "difficulty": "junior", "type": "theory", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-handlers.html"},
  {"title": "Explain idempotence in an Ansible playbook", "theme": "configuration-management", "difficulty": "middle", "type": "theory", "tags": ["ansible", "automation", "configuration-management", "reliability", "cgoa"], "path": "questions/configuration-management/ansible-idempotence.html"},
  {"title": "Explain an Ansible inventory and host groups", "theme": "configuration-management", "difficulty": "junior", "type": "theory", "tags": ["ansible", "automation", "configuration-management"], "path": "questions/configuration-management/ansible-inventory-basics.html"},
  {"title": "Explain plays, tasks, and modules in Ansible", "theme": "configuration-management", "difficulty": "junior", "type": "theory", "tags": ["ansible", "automation", "configuration-management"], "path": "questions/configuration-management/ansible-playbook-basics.html"},
  {"title": "Apply least privilege to Ansible privilege escalation", "theme": "configuration-management", "difficulty": "senior", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "security", "least-privilege"], "path": "questions/configuration-management/ansible-privilege-escalation.html"},
  {"title": "Design a reusable Ansible role", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-role-design.html"},
  {"title": "Perform an Ansible rolling configuration update", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "deployment", "reliability"], "path": "questions/configuration-management/ansible-rolling-update.html"},
  {"title": "Target Ansible tasks with tags safely", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "deployment"], "path": "questions/configuration-management/ansible-tags.html"},
  {"title": "Deliver a configuration file with an Ansible template", "theme": "configuration-management", "difficulty": "junior", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-templates.html"},
  {"title": "Build an Ansible content test strategy", "theme": "configuration-management", "difficulty": "senior", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability", "deployment"], "path": "questions/configuration-management/ansible-test-strategy.html"},
  {"title": "Use Ansible variables without creating precedence surprises", "theme": "configuration-management", "difficulty": "junior", "type": "theory", "tags": ["ansible", "automation", "configuration-management", "reliability"], "path": "questions/configuration-management/ansible-variables-basics.html"},
  {"title": "Protect secrets used by Ansible automation", "theme": "configuration-management", "difficulty": "middle", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "security"], "path": "questions/configuration-management/ansible-vault-secrets.html"},
  {"title": "Create a risk-based configuration change model", "theme": "configuration-management", "difficulty": "staff", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "governance", "deployment", "reliability"], "path": "questions/configuration-management/cm-change-risk-model.html"},
  {"title": "Define configuration ownership across a platform fleet", "theme": "configuration-management", "difficulty": "staff", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "governance", "platform-engineering", "reliability"], "path": "questions/configuration-management/cm-fleet-ownership.html"},
  {"title": "Establish configuration-management platform guardrails", "theme": "configuration-management", "difficulty": "staff", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "platform-engineering", "governance", "security", "cnpa"], "path": "questions/configuration-management/cm-platform-guardrails.html"},
  {"title": "Design resilience for a configuration-management control plane", "theme": "configuration-management", "difficulty": "staff", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability", "availability", "incident-response"], "path": "questions/configuration-management/cm-resilience-strategy.html"},
  {"title": "Standardize configuration management without blocking teams", "theme": "configuration-management", "difficulty": "staff", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "platform-engineering", "governance", "reliability"], "path": "questions/configuration-management/cm-standardization-strategy.html"},
  {"title": "Design safe configuration drift remediation", "theme": "configuration-management", "difficulty": "senior", "type": "scenario", "tags": ["ansible", "automation", "configuration-management", "reliability", "security", "cgoa"], "path": "questions/configuration-management/configuration-drift-remediation.html"},
  {"title": "Trace bridge-network traffic", "theme": "container-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "docker", "networking", "tcp", "troubleshooting"], "path": "questions/container-networking/bridge-traffic-path.html"},
  {"title": "Advertise Kubernetes routes with Cilium BGP Control Plane", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "reliability", "troubleshooting", "cca"], "path": "questions/container-networking/cilium-bgp-external-routing.html"},
  {"title": "Prepare clusters for Cilium Cluster Mesh", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "security", "reliability", "cca"], "path": "questions/container-networking/cilium-clustermesh-prerequisites.html"},
  {"title": "Explain Cilium's eBPF datapath trade-offs", "theme": "container-networking", "difficulty": "middle", "type": "theory", "tags": ["containers", "kubernetes", "networking", "performance", "security", "cca"], "path": "questions/container-networking/cilium-ebpf-datapath-tradeoffs.html"},
  {"title": "Design controlled egress with Cilium Egress Gateway", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "security", "reliability", "cca", "ckne"], "path": "questions/container-networking/cilium-egress-gateway-design.html"},
  {"title": "Evaluate Cilium kube-proxy replacement", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "performance", "reliability", "cca", "ckne"], "path": "questions/container-networking/cilium-kube-proxy-replacement.html"},
  {"title": "Apply Cilium identity-aware L7 network policy", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "security", "least-privilege", "cca"], "path": "questions/container-networking/cilium-l7-network-policy.html"},
  {"title": "Define a Compose network contract", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "deployment", "reliability"], "path": "questions/container-networking/compose-network-contract.html"},
  {"title": "Debug container DNS resolution", "theme": "container-networking", "difficulty": "junior", "type": "troubleshooting", "tags": ["containers", "docker", "networking", "dns", "troubleshooting"], "path": "questions/container-networking/container-dns-resolution.html"},
  {"title": "Debug failed container egress", "theme": "container-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "docker", "networking", "dns", "troubleshooting"], "path": "questions/container-networking/container-egress-debugging.html"},
  {"title": "Explain a container network namespace", "theme": "container-networking", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "networking", "linux"], "path": "questions/container-networking/container-network-namespace.html"},
  {"title": "Design container network security architecture", "theme": "container-networking", "difficulty": "staff", "type": "scenario", "tags": ["containers", "kubernetes", "docker", "networking", "security", "governance", "least-privilege"], "path": "questions/container-networking/container-network-security-architecture.html"},
  {"title": "Distinguish EXPOSE from port publishing", "theme": "container-networking", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "networking", "tcp", "security"], "path": "questions/container-networking/expose-versus-publish.html"},
  {"title": "Evaluate host networking", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "security", "performance"], "path": "questions/container-networking/host-networking-tradeoffs.html"},
  {"title": "Define ingress and gateway boundaries", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "http", "security", "reliability", "cca", "ckne"], "path": "questions/container-networking/ingress-gateway-boundary.html"},
  {"title": "Enable IPv6 container networking safely", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "dns", "reliability"], "path": "questions/container-networking/ipv6-container-networking.html"},
  {"title": "Trace Kubernetes Service traffic", "theme": "container-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["containers", "kubernetes", "networking", "dns", "troubleshooting", "cca", "ckne"], "path": "questions/container-networking/kubernetes-service-traffic-path.html"},
  {"title": "Diagnose an MTU mismatch across container paths", "theme": "container-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["containers", "docker", "networking", "tcp", "troubleshooting", "performance"], "path": "questions/container-networking/mtu-mismatch-troubleshooting.html"},
  {"title": "Define a multi-cluster connectivity strategy", "theme": "container-networking", "difficulty": "staff", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "reliability", "governance", "platform-engineering", "cca", "ckne"], "path": "questions/container-networking/multi-cluster-connectivity-strategy.html"},
  {"title": "Segment a multi-tier application with Docker networks", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "security", "least-privilege"], "path": "questions/container-networking/multi-network-segmentation.html"},
  {"title": "Configure and troubleshoot a multi-interface Pod with Multus", "theme": "container-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["containers", "kubernetes", "networking", "cni", "multus", "ipam", "routing", "troubleshooting", "ckne"], "path": "questions/container-networking/multus-multi-interface-pod-troubleshooting.html"},
  {"title": "Design network aliases for service lifecycle", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "dns", "deployment"], "path": "questions/container-networking/network-alias-lifecycle.html"},
  {"title": "Govern high-risk container network changes", "theme": "container-networking", "difficulty": "staff", "type": "scenario", "tags": ["containers", "kubernetes", "docker", "networking", "deployment", "governance", "reliability"], "path": "questions/container-networking/network-change-governance.html"},
  {"title": "Explain Docker network drivers", "theme": "container-networking", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "networking", "reliability"], "path": "questions/container-networking/network-driver-basics.html"},
  {"title": "Establish container network observability standards", "theme": "container-networking", "difficulty": "staff", "type": "scenario", "tags": ["containers", "kubernetes", "docker", "networking", "observability", "monitoring", "governance", "cca", "ckne"], "path": "questions/container-networking/network-observability-standard.html"},
  {"title": "Validate Kubernetes NetworkPolicy enforcement", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "security", "least-privilege", "kcsa", "cca", "ckne"], "path": "questions/container-networking/network-policy-enforcement-limits.html"},
  {"title": "Plan overlay-network prerequisites", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "deployment", "reliability"], "path": "questions/container-networking/overlay-network-prerequisites.html"},
  {"title": "Govern workload egress on a container platform", "theme": "container-networking", "difficulty": "staff", "type": "scenario", "tags": ["containers", "kubernetes", "networking", "security", "governance", "reliability"], "path": "questions/container-networking/platform-egress-governance.html"},
  {"title": "Restrict published-port exposure", "theme": "container-networking", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "networking", "security", "least-privilege"], "path": "questions/container-networking/port-binding-exposure.html"},
  {"title": "Trace traffic to a published container port", "theme": "container-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "docker", "networking", "tcp", "troubleshooting"], "path": "questions/container-networking/published-port-traffic-path.html"},
  {"title": "Choose Swarm ingress or host publishing", "theme": "container-networking", "difficulty": "senior", "type": "scenario", "tags": ["containers", "docker", "networking", "deployment", "availability"], "path": "questions/container-networking/swarm-ingress-routing.html"},
  {"title": "Use a user-defined bridge for service discovery", "theme": "container-networking", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "networking", "dns"], "path": "questions/container-networking/user-defined-bridge-dns.html"},
  {"title": "Maintain a base-image update policy", "theme": "containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "docker", "images", "image-digests", "security", "supply-chain", "cks"], "path": "questions/containers/base-image-update-policy.html"},
  {"title": "Order a Dockerfile for safe cache reuse", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "dockerfile", "build-cache", "automation", "cba"], "path": "questions/containers/build-cache-ordering.html"},
  {"title": "Use a private dependency credential during an image build", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "build-secrets", "security", "supply-chain"], "path": "questions/containers/build-secrets.html"},
  {"title": "Choose between CMD and ENTRYPOINT in a Docker image", "theme": "containers", "difficulty": "middle", "type": "theory", "tags": ["containers", "docker", "images"], "path": "questions/containers/cmd-and-entrypoint.html"},
  {"title": "Reduce Linux capabilities for a containerized service", "theme": "containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "docker", "security", "least-privilege", "cks", "kcsa", "ckad"], "path": "questions/containers/container-capabilities-security.html"},
  {"title": "Design a useful container health check", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "healthchecks", "reliability"], "path": "questions/containers/container-healthcheck-design.html"},
  {"title": "Distinguish a container image from a running container", "theme": "containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "images", "ckad", "kcna", "lfcs", "must-know"], "path": "questions/containers/container-image-and-runtime.html"},
  {"title": "Triage a container service restart storm", "theme": "containers", "difficulty": "senior", "type": "troubleshooting", "tags": ["containers", "docker", "debugging", "monitoring", "incident-response", "reliability"], "path": "questions/containers/container-incident-triage.html"},
  {"title": "Explain container lifecycle states and restart policy", "theme": "containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "reliability", "kcna"], "path": "questions/containers/container-lifecycle-states.html"},
  {"title": "Define a container logging contract", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "logging", "observability", "reliability", "ckad"], "path": "questions/containers/container-logging-contract.html"},
  {"title": "Set a container-platform cost and capacity model", "theme": "containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "docker", "cgroups", "resource-limits", "cost-optimization", "reliability", "platform-engineering", "cnpe", "cnpa"], "path": "questions/containers/container-platform-cost-model.html"},
  {"title": "Lead a container runtime migration", "theme": "containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "docker", "container-runtime", "reliability", "platform-engineering", "governance", "kcsa"], "path": "questions/containers/container-runtime-migration.html"},
  {"title": "Control Docker build context with .dockerignore", "theme": "containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "dockerfile", "security", "cba"], "path": "questions/containers/dockerfile-build-context.html"},
  {"title": "Build an image supply-chain control plane", "theme": "containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "docker", "images", "registries", "security", "supply-chain", "governance"], "path": "questions/containers/image-supply-chain-control-plane.html"},
  {"title": "Distinguish image tags from digests", "theme": "containers", "difficulty": "junior", "type": "theory", "tags": ["containers", "docker", "images", "image-tags", "image-digests"], "path": "questions/containers/image-tag-and-digest.html"},
  {"title": "Investigate a container that exits immediately", "theme": "containers", "difficulty": "junior", "type": "troubleshooting", "tags": ["containers", "docker", "debugging", "troubleshooting"], "path": "questions/containers/inspect-container-failure.html"},
  {"title": "Release a multi-platform container image", "theme": "containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "docker", "images", "multi-platform", "registries", "automation"], "path": "questions/containers/multi-platform-image-release.html"},
  {"title": "Build a small runtime image with multi-stage builds", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "dockerfile", "multi-stage-builds", "images", "security", "cba"], "path": "questions/containers/multi-stage-runtime-image.html"},
  {"title": "Run a containerized service as a non-root user", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "security", "least-privilege", "cks", "kcsa"], "path": "questions/containers/non-root-container.html"},
  {"title": "Make a container stop gracefully", "theme": "containers", "difficulty": "middle", "type": "troubleshooting", "tags": ["containers", "docker", "signals", "reliability", "troubleshooting"], "path": "questions/containers/pid-one-and-graceful-shutdown.html"},
  {"title": "Design a governed base-image program", "theme": "containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "docker", "images", "security", "supply-chain", "governance", "platform-engineering"], "path": "questions/containers/platform-base-image-program.html"},
  {"title": "Apply CPU and memory constraints to a container", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "cgroups", "resource-limits", "reliability"], "path": "questions/containers/resource-constraints.html"},
  {"title": "Evaluate Docker rootless mode for a build worker", "theme": "containers", "difficulty": "senior", "type": "scenario", "tags": ["containers", "docker", "rootless", "security", "least-privilege"], "path": "questions/containers/rootless-mode-boundaries.html"},
  {"title": "Define tenant isolation boundaries for a container platform", "theme": "containers", "difficulty": "staff", "type": "scenario", "tags": ["containers", "docker", "security", "least-privilege", "platform-engineering", "governance", "cnpa"], "path": "questions/containers/tenant-isolation-boundaries.html"},
  {"title": "Choose a Docker volume or a bind mount", "theme": "containers", "difficulty": "middle", "type": "scenario", "tags": ["containers", "docker", "storage", "volumes"], "path": "questions/containers/volume-versus-bind-mount.html"},
  {"title": "Operate PostgreSQL autovacuum safely", "theme": "databases", "difficulty": "middle", "type": "scenario", "tags": ["databases", "postgresql", "monitoring", "reliability", "performance"], "path": "questions/databases/autovacuum-operations.html"},
  {"title": "Explain database backup and restore validation", "theme": "databases", "difficulty": "junior", "type": "scenario", "tags": ["databases", "postgresql", "storage", "reliability"], "path": "questions/databases/backup-restore-basics.html"},
  {"title": "Explain PostgreSQL connection authentication", "theme": "databases", "difficulty": "junior", "type": "theory", "tags": ["databases", "postgresql", "security", "least-privilege"], "path": "questions/databases/connection-authentication-basics.html"},
  {"title": "Size a PostgreSQL connection pool", "theme": "databases", "difficulty": "middle", "type": "scenario", "tags": ["databases", "postgresql", "capacity-planning", "performance", "reliability"], "path": "questions/databases/connection-pool-capacity.html"},
  {"title": "Respond to suspected PostgreSQL data corruption", "theme": "databases", "difficulty": "senior", "type": "troubleshooting", "tags": ["databases", "postgresql", "incident-response", "reliability", "storage"], "path": "questions/databases/data-corruption-response.html"},
  {"title": "Govern data lifecycle and retention in PostgreSQL", "theme": "databases", "difficulty": "staff", "type": "scenario", "tags": ["databases", "postgresql", "security", "governance", "reliability"], "path": "questions/databases/data-lifecycle-governance.html"},
  {"title": "Govern capacity for a multi-team database platform", "theme": "databases", "difficulty": "staff", "type": "scenario", "tags": ["databases", "postgresql", "capacity-planning", "governance", "reliability"], "path": "questions/databases/database-capacity-governance.html"},
  {"title": "Establish database change governance without blocking delivery", "theme": "databases", "difficulty": "staff", "type": "scenario", "tags": ["databases", "postgresql", "governance", "deployment", "reliability"], "path": "questions/databases/database-change-governance.html"},
  {"title": "Lead a database disaster-recovery program", "theme": "databases", "difficulty": "staff", "type": "scenario", "tags": ["databases", "postgresql", "incident-response", "reliability", "governance"], "path": "questions/databases/database-disaster-recovery-program.html"},
  {"title": "Define SLOs for a shared database service", "theme": "databases", "difficulty": "staff", "type": "scenario", "tags": ["databases", "postgresql", "reliability", "monitoring", "governance"], "path": "questions/databases/database-service-slo.html"},
  {"title": "Design PostgreSQL high availability and failover", "theme": "databases", "difficulty": "senior", "type": "scenario", "tags": ["databases", "postgresql", "availability", "reliability", "incident-response"], "path": "questions/databases/high-availability-failover.html"},
  {"title": "Explain database index trade-offs", "theme": "databases", "difficulty": "middle", "type": "theory", "tags": ["databases", "postgresql", "reliability", "troubleshooting"], "path": "questions/databases/index-tradeoffs.html"},
  {"title": "Select a PostgreSQL transaction isolation level", "theme": "databases", "difficulty": "middle", "type": "scenario", "tags": ["databases", "postgresql", "reliability", "troubleshooting"], "path": "questions/databases/isolation-level-selection.html"},
  {"title": "Triage PostgreSQL lock contention", "theme": "databases", "difficulty": "middle", "type": "troubleshooting", "tags": ["databases", "postgresql", "monitoring", "troubleshooting", "reliability"], "path": "questions/databases/lock-contention-triage.html"},
  {"title": "Diagnose long transactions in an MVCC database", "theme": "databases", "difficulty": "middle", "type": "troubleshooting", "tags": ["databases", "postgresql", "monitoring", "troubleshooting", "reliability"], "path": "questions/databases/mvcc-and-long-transactions.html"},
  {"title": "Choose a PostgreSQL partitioning strategy", "theme": "databases", "difficulty": "senior", "type": "scenario", "tags": ["databases", "postgresql", "performance", "capacity-planning", "reliability"], "path": "questions/databases/partitioning-strategy.html"},
  {"title": "Design PostgreSQL point-in-time recovery", "theme": "databases", "difficulty": "senior", "type": "scenario", "tags": ["databases", "postgresql", "storage", "reliability", "incident-response"], "path": "questions/databases/point-in-time-recovery-design.html"},
  {"title": "Explain relational tables, keys, and constraints", "theme": "databases", "difficulty": "junior", "type": "theory", "tags": ["databases", "postgresql", "reliability"], "path": "questions/databases/relational-data-model-basics.html"},
  {"title": "Respond to PostgreSQL replication lag", "theme": "databases", "difficulty": "middle", "type": "troubleshooting", "tags": ["databases", "postgresql", "monitoring", "troubleshooting", "availability"], "path": "questions/databases/replication-lag-response.html"},
  {"title": "Design least-privilege PostgreSQL roles", "theme": "databases", "difficulty": "middle", "type": "scenario", "tags": ["databases", "postgresql", "security", "least-privilege", "governance"], "path": "questions/databases/role-privilege-design.html"},
  {"title": "Deploy a PostgreSQL schema migration safely", "theme": "databases", "difficulty": "middle", "type": "scenario", "tags": ["databases", "postgresql", "deployment", "reliability", "troubleshooting"], "path": "questions/databases/schema-migration-safety.html"},
  {"title": "Triage a sudden slow PostgreSQL query", "theme": "databases", "difficulty": "middle", "type": "troubleshooting", "tags": ["databases", "postgresql", "performance", "monitoring", "troubleshooting"], "path": "questions/databases/slow-query-triage.html"},
  {"title": "Read a basic PostgreSQL query plan", "theme": "databases", "difficulty": "junior", "type": "theory", "tags": ["databases", "postgresql", "performance", "troubleshooting"], "path": "questions/databases/sql-query-plan-basics.html"},
  {"title": "Explain database transaction boundaries", "theme": "databases", "difficulty": "junior", "type": "theory", "tags": ["databases", "postgresql", "reliability"], "path": "questions/databases/transaction-basics.html"},
  {"title": "Plan a near-zero-downtime PostgreSQL major upgrade", "theme": "databases", "difficulty": "senior", "type": "scenario", "tags": ["databases", "postgresql", "deployment", "reliability", "governance"], "path": "questions/databases/zero-downtime-major-upgrade.html"},
  {"title": "Plan anti-entropy repair", "theme": "distributed-systems", "difficulty": "senior", "type": "scenario", "tags": ["databases", "recovery", "reliability"], "path": "questions/distributed-systems/anti-entropy-repair.html"},
  {"title": "Consume an at-least-once event stream safely", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["event-driven", "kafka", "reliability"], "path": "questions/distributed-systems/at-least-once-delivery.html"},
  {"title": "Govern a high-risk distributed state change", "theme": "distributed-systems", "difficulty": "staff", "type": "scenario", "tags": ["change-management", "reliability", "recovery"], "path": "questions/distributed-systems/change-safety.html"},
  {"title": "Use a circuit breaker without masking failure", "theme": "distributed-systems", "difficulty": "middle", "type": "troubleshooting", "tags": ["reliability", "availability", "troubleshooting"], "path": "questions/distributed-systems/circuit-breakers.html"},
  {"title": "Handle clock skew in a distributed service", "theme": "distributed-systems", "difficulty": "junior", "type": "troubleshooting", "tags": ["time", "reliability", "troubleshooting"], "path": "questions/distributed-systems/clock-skew.html"},
  {"title": "Explain consistency and availability during a network partition", "theme": "distributed-systems", "difficulty": "junior", "type": "theory", "tags": ["availability", "reliability", "networking", "must-know"], "path": "questions/distributed-systems/consistency-and-availability.html"},
  {"title": "Rebalance a consistent-hash partitioned service", "theme": "distributed-systems", "difficulty": "senior", "type": "scenario", "tags": ["databases", "capacity-planning", "reliability"], "path": "questions/distributed-systems/consistent-hashing.html"},
  {"title": "Establish data-integrity controls across services", "theme": "distributed-systems", "difficulty": "staff", "type": "theory", "tags": ["databases", "security", "reliability"], "path": "questions/distributed-systems/data-integrity.html"},
  {"title": "Operate a dead-letter queue", "theme": "distributed-systems", "difficulty": "senior", "type": "troubleshooting", "tags": ["message-queues", "event-driven", "recovery"], "path": "questions/distributed-systems/dead-letter-queues.html"},
  {"title": "Use fencing tokens to prevent stale writers", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "security", "databases"], "path": "questions/distributed-systems/fencing-tokens.html"},
  {"title": "Make a retried write idempotent", "theme": "distributed-systems", "difficulty": "junior", "type": "scenario", "tags": ["reliability", "event-driven", "databases"], "path": "questions/distributed-systems/idempotent-operations.html"},
  {"title": "Lead a cross-service consistency incident", "theme": "distributed-systems", "difficulty": "staff", "type": "troubleshooting", "tags": ["incident-management", "recovery", "reliability"], "path": "questions/distributed-systems/incident-command.html"},
  {"title": "Explain safe leader election", "theme": "distributed-systems", "difficulty": "middle", "type": "theory", "tags": ["availability", "reliability", "leadership"], "path": "questions/distributed-systems/leader-election.html"},
  {"title": "Choose a linearizable read", "theme": "distributed-systems", "difficulty": "senior", "type": "theory", "tags": ["databases", "reliability", "availability"], "path": "questions/distributed-systems/linearizable-read.html"},
  {"title": "Shed load to preserve a critical service", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["availability", "capacity-planning", "reliability"], "path": "questions/distributed-systems/load-shedding.html"},
  {"title": "Design multi-region failover", "theme": "distributed-systems", "difficulty": "staff", "type": "scenario", "tags": ["availability", "recovery", "capacity-planning"], "path": "questions/distributed-systems/multi-region-failover.html"},
  {"title": "Apply the transactional outbox pattern", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["event-driven", "databases", "reliability"], "path": "questions/distributed-systems/outbox-pattern.html"},
  {"title": "Design a quorum for replicated writes", "theme": "distributed-systems", "difficulty": "junior", "type": "scenario", "tags": ["availability", "reliability", "databases"], "path": "questions/distributed-systems/quorum-basics.html"},
  {"title": "Provide read-your-writes consistency", "theme": "distributed-systems", "difficulty": "senior", "type": "scenario", "tags": ["databases", "reliability", "latency"], "path": "questions/distributed-systems/read-your-writes.html"},
  {"title": "Diagnose replication lag", "theme": "distributed-systems", "difficulty": "middle", "type": "troubleshooting", "tags": ["databases", "latency", "troubleshooting"], "path": "questions/distributed-systems/replication-lag.html"},
  {"title": "Coordinate a multi-service saga", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["event-driven", "reliability", "recovery", "must-know"], "path": "questions/distributed-systems/saga-compensation.html"},
  {"title": "Evolve an event schema safely", "theme": "distributed-systems", "difficulty": "middle", "type": "scenario", "tags": ["event-driven", "kafka", "delivery"], "path": "questions/distributed-systems/schema-evolution.html"},
  {"title": "Design service discovery and client load balancing", "theme": "distributed-systems", "difficulty": "middle", "type": "theory", "tags": ["dns", "networking", "availability"], "path": "questions/distributed-systems/service-discovery.html"},
  {"title": "Protect tenant fairness in a shared distributed platform", "theme": "distributed-systems", "difficulty": "staff", "type": "scenario", "tags": ["capacity-planning", "reliability", "platform-engineering"], "path": "questions/distributed-systems/tenant-fairness.html"},
  {"title": "Choose timeouts, retries, and backoff", "theme": "distributed-systems", "difficulty": "junior", "type": "troubleshooting", "tags": ["reliability", "latency", "troubleshooting"], "path": "questions/distributed-systems/timeouts-retries-backoff.html"},
  {"title": "Allocate shared and untaggable cost", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "cost-allocation", "chargeback", "governance"], "path": "questions/finops/allocate-shared-and-untaggable-cost.html"},
  {"title": "Attribute Kubernetes cluster cost to teams", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "kubernetes", "cost-allocation", "platform-engineering"], "path": "questions/finops/attribute-kubernetes-cluster-cost-to-teams.html"},
  {"title": "Build a commitment discount portfolio", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "commitment-discounts", "forecasting", "cost-optimization"], "path": "questions/finops/build-a-commitment-discount-portfolio.html"},
  {"title": "Compare on-demand, committed, and spot pricing", "theme": "finops", "difficulty": "junior", "type": "theory", "tags": ["finops", "commitment-discounts", "spot-instances", "cost-optimization"], "path": "questions/finops/compare-on-demand-committed-and-spot-pricing.html"},
  {"title": "Decide when not to optimise cost", "theme": "finops", "difficulty": "staff", "type": "scenario", "tags": ["finops", "leadership", "cost-optimization", "architecture"], "path": "questions/finops/decide-when-not-to-optimise-cost.html"},
  {"title": "Design account structure for cost visibility", "theme": "finops", "difficulty": "senior", "type": "scenario", "tags": ["finops", "cost-allocation", "cloud", "architecture"], "path": "questions/finops/design-account-structure-for-cost-visibility.html"},
  {"title": "Explain cloud unit economics", "theme": "finops", "difficulty": "junior", "type": "theory", "tags": ["finops", "unit-economics", "cloud", "cost-optimization"], "path": "questions/finops/explain-cloud-unit-economics.html"},
  {"title": "Explain showback and chargeback", "theme": "finops", "difficulty": "junior", "type": "theory", "tags": ["finops", "chargeback", "cost-allocation", "governance"], "path": "questions/finops/explain-showback-and-chargeback.html"},
  {"title": "Forecast next quarter cloud spend", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "forecasting", "budgeting", "capacity-planning"], "path": "questions/finops/forecast-next-quarter-cloud-spend.html"},
  {"title": "Investigate a cost anomaly alert", "theme": "finops", "difficulty": "middle", "type": "troubleshooting", "tags": ["finops", "anomaly-detection", "monitoring", "incident-response"], "path": "questions/finops/investigate-a-cost-anomaly-alert.html"},
  {"title": "Manage commitment risk on a changing fleet", "theme": "finops", "difficulty": "senior", "type": "scenario", "tags": ["finops", "commitment-discounts", "forecasting", "governance"], "path": "questions/finops/manage-commitment-risk-on-a-changing-fleet.html"},
  {"title": "Model cost per transaction for a service", "theme": "finops", "difficulty": "senior", "type": "scenario", "tags": ["finops", "unit-economics", "architecture", "cost-optimization"], "path": "questions/finops/model-cost-per-transaction-for-a-service.html"},
  {"title": "Normalise multi-cloud billing data with FOCUS", "theme": "finops", "difficulty": "middle", "type": "theory", "tags": ["finops", "cost-allocation", "cloud", "architecture"], "path": "questions/finops/normalise-multi-cloud-billing-data-with-focus.html"},
  {"title": "Prioritise a cost reduction programme", "theme": "finops", "difficulty": "staff", "type": "scenario", "tags": ["finops", "leadership", "governance", "capacity-planning"], "path": "questions/finops/prioritise-a-cost-reduction-programme.html"},
  {"title": "Read a cloud bill and find its drivers", "theme": "finops", "difficulty": "junior", "type": "theory", "tags": ["finops", "cloud", "cost-optimization", "aws"], "path": "questions/finops/read-a-cloud-bill-and-find-its-drivers.html"},
  {"title": "Reclaim idle Kubernetes capacity", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "kubernetes", "rightsizing", "resource-limits"], "path": "questions/finops/reclaim-idle-kubernetes-capacity.html"},
  {"title": "Rightsize overprovisioned compute", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "rightsizing", "cost-optimization", "capacity-planning"], "path": "questions/finops/rightsize-overprovisioned-compute.html"},
  {"title": "Run production work on spot capacity", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "spot-instances", "reliability", "kubernetes"], "path": "questions/finops/run-production-work-on-spot-capacity.html"},
  {"title": "Set a cloud budget and alert", "theme": "finops", "difficulty": "junior", "type": "scenario", "tags": ["finops", "budgeting", "monitoring", "cloud"], "path": "questions/finops/set-a-cloud-budget-and-alert.html"},
  {"title": "Set incentives for cost accountability", "theme": "finops", "difficulty": "staff", "type": "scenario", "tags": ["finops", "leadership", "governance", "chargeback"], "path": "questions/finops/set-incentives-for-cost-accountability.html"},
  {"title": "Stand up a FinOps practice", "theme": "finops", "difficulty": "staff", "type": "scenario", "tags": ["finops", "governance", "leadership", "platform-engineering"], "path": "questions/finops/stand-up-a-finops-practice.html"},
  {"title": "Tag resources for cost allocation", "theme": "finops", "difficulty": "junior", "type": "theory", "tags": ["finops", "tagging", "cost-allocation", "cloud"], "path": "questions/finops/tag-resources-for-cost-allocation.html"},
  {"title": "Tier object storage with lifecycle rules", "theme": "finops", "difficulty": "middle", "type": "scenario", "tags": ["finops", "storage", "cost-optimization", "cloud"], "path": "questions/finops/tier-object-storage-with-lifecycle-rules.html"},
  {"title": "Trace an unexplained data transfer bill", "theme": "finops", "difficulty": "middle", "type": "troubleshooting", "tags": ["finops", "data-transfer", "networking", "cost-optimization"], "path": "questions/finops/trace-an-unexplained-data-transfer-bill.html"},
  {"title": "Trade cost against reliability", "theme": "finops", "difficulty": "senior", "type": "scenario", "tags": ["finops", "reliability", "sre", "cost-optimization"], "path": "questions/finops/trade-cost-against-reliability.html"},
  {"title": "Tune autoscaling for cost and latency", "theme": "finops", "difficulty": "senior", "type": "scenario", "tags": ["finops", "kubernetes", "latency", "capacity-planning"], "path": "questions/finops/tune-autoscaling-for-cost-and-latency.html"},
  {"title": "Weigh engineering time against infrastructure cost", "theme": "finops", "difficulty": "staff", "type": "theory", "tags": ["finops", "leadership", "platform-engineering", "cost-optimization"], "path": "questions/finops/weigh-engineering-time-against-infrastructure-cost.html"},
  {"title": "Maintain a trustworthy server hardware inventory", "theme": "hardware", "difficulty": "junior", "type": "scenario", "tags": ["hardware", "automation", "monitoring", "reliability"], "path": "questions/hardware/asset-inventory-basics.html"},
  {"title": "Triage a degrading production disk", "theme": "hardware", "difficulty": "middle", "type": "troubleshooting", "tags": ["hardware", "storage", "troubleshooting", "reliability"], "path": "questions/hardware/disk-failure-triage.html"},
  {"title": "Respond to corrected and uncorrected memory errors", "theme": "hardware", "difficulty": "middle", "type": "troubleshooting", "tags": ["hardware", "memory", "troubleshooting", "reliability"], "path": "questions/hardware/ecc-memory-errors.html"},
  {"title": "Plan a production server firmware upgrade", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "firmware", "deployment", "reliability", "security"], "path": "questions/hardware/firmware-upgrade-runbook.html"},
  {"title": "Govern firmware risk across a server fleet", "theme": "hardware", "difficulty": "staff", "type": "scenario", "tags": ["hardware", "firmware", "security", "governance", "automation", "reliability"], "path": "questions/hardware/fleet-firmware-governance.html"},
  {"title": "Build a hardware capacity baseline", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "capacity-planning", "monitoring", "reliability"], "path": "questions/hardware/hardware-capacity-baseline.html"},
  {"title": "Establish a server hardware lifecycle strategy", "theme": "hardware", "difficulty": "staff", "type": "scenario", "tags": ["hardware", "governance", "capacity-planning", "reliability", "security"], "path": "questions/hardware/hardware-lifecycle-strategy.html"},
  {"title": "Design a representative hardware performance benchmark", "theme": "hardware", "difficulty": "senior", "type": "scenario", "tags": ["hardware", "cpu", "storage", "networking", "capacity-planning", "reliability"], "path": "questions/hardware/hardware-performance-benchmark.html"},
  {"title": "Plan a hardware refresh without service interruption", "theme": "hardware", "difficulty": "senior", "type": "scenario", "tags": ["hardware", "deployment", "capacity-planning", "reliability", "availability"], "path": "questions/hardware/hardware-refresh-migration.html"},
  {"title": "Design actionable server hardware sensor monitoring", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "sensors", "monitoring", "troubleshooting", "reliability"], "path": "questions/hardware/hardware-sensor-monitoring.html"},
  {"title": "Isolate a server network-interface fault", "theme": "hardware", "difficulty": "middle", "type": "troubleshooting", "tags": ["hardware", "networking", "troubleshooting", "monitoring", "reliability"], "path": "questions/hardware/network-interface-fault-isolation.html"},
  {"title": "Place a latency-sensitive workload on a NUMA server", "theme": "hardware", "difficulty": "senior", "type": "scenario", "tags": ["hardware", "cpu", "memory", "virtualization", "performance", "reliability"], "path": "questions/hardware/numa-aware-workload-placement.html"},
  {"title": "Recover access to an unreachable server without physical presence", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "troubleshooting", "availability"], "path": "questions/hardware/out-of-band-server-recovery.html"},
  {"title": "Define a standard hardware platform without blocking product teams", "theme": "hardware", "difficulty": "staff", "type": "scenario", "tags": ["hardware", "platform-engineering", "governance", "reliability", "security"], "path": "questions/hardware/platform-standardization.html"},
  {"title": "Govern rack power and cooling capacity", "theme": "hardware", "difficulty": "staff", "type": "scenario", "tags": ["hardware", "power", "sensors", "capacity-planning", "reliability", "governance"], "path": "questions/hardware/rack-power-cooling-governance.html"},
  {"title": "Operate safely during a RAID rebuild", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "raid", "storage", "reliability", "troubleshooting"], "path": "questions/hardware/raid-rebuild-safety.html"},
  {"title": "Explain RAID redundancy and its limits", "theme": "hardware", "difficulty": "junior", "type": "theory", "tags": ["hardware", "raid", "storage", "reliability"], "path": "questions/hardware/raid-redundancy-basics.html"},
  {"title": "Validate redundant server power paths", "theme": "hardware", "difficulty": "middle", "type": "scenario", "tags": ["hardware", "power", "availability", "reliability"], "path": "questions/hardware/redundant-power-validation.html"},
  {"title": "Use secure boot and platform attestation appropriately", "theme": "hardware", "difficulty": "senior", "type": "scenario", "tags": ["hardware", "firmware", "security", "least-privilege", "reliability"], "path": "questions/hardware/secure-boot-attestation.html"},
  {"title": "Explain the roles of core server components", "theme": "hardware", "difficulty": "junior", "type": "theory", "tags": ["hardware", "server-hardware", "cpu", "memory", "storage"], "path": "questions/hardware/server-component-basics.html"},
  {"title": "Interpret disk health signals without overtrusting SMART", "theme": "hardware", "difficulty": "junior", "type": "theory", "tags": ["hardware", "storage", "monitoring", "reliability"], "path": "questions/hardware/smart-health-basics.html"},
  {"title": "Design spares and failure-domain strategy for physical infrastructure", "theme": "hardware", "difficulty": "staff", "type": "scenario", "tags": ["hardware", "capacity-planning", "availability", "reliability", "incident-response"], "path": "questions/hardware/spares-and-failure-domain-strategy.html"},
  {"title": "Respond to a suspected storage-controller failure", "theme": "hardware", "difficulty": "senior", "type": "troubleshooting", "tags": ["hardware", "raid", "storage", "troubleshooting", "incident-response", "reliability"], "path": "questions/hardware/storage-controller-failure-response.html"},
  {"title": "Diagnose thermal throttling on a server", "theme": "hardware", "difficulty": "middle", "type": "troubleshooting", "tags": ["hardware", "sensors", "cpu", "troubleshooting", "monitoring"], "path": "questions/hardware/thermal-throttling-diagnosis.html"},
  {"title": "Plan graceful shutdown for loss of utility power", "theme": "hardware", "difficulty": "junior", "type": "scenario", "tags": ["hardware", "power", "availability", "reliability"], "path": "questions/hardware/ups-graceful-shutdown.html"},
  {"title": "Model Terraform dependencies without overusing depends_on", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/explicit-dependencies.html"},
  {"title": "Choose for_each or count for repeated Terraform resources", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/for-each-versus-count.html"},
  {"title": "Create a risk-based IaC change-management model", "theme": "infrastructure-as-code", "difficulty": "staff", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "governance", "deployment", "reliability", "security"], "path": "questions/infrastructure-as-code/iac-change-risk-management.html"},
  {"title": "Govern infrastructure drift at organization scale", "theme": "infrastructure-as-code", "difficulty": "staff", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "governance", "monitoring", "reliability", "security", "cgoa"], "path": "questions/infrastructure-as-code/iac-drift-governance.html"},
  {"title": "Treat shared Terraform modules as internal products", "theme": "infrastructure-as-code", "difficulty": "staff", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "platform-engineering", "governance", "reliability", "automation"], "path": "questions/infrastructure-as-code/iac-module-product-strategy.html"},
  {"title": "Establish infrastructure-as-code platform guardrails", "theme": "infrastructure-as-code", "difficulty": "staff", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "platform-engineering", "governance", "security", "reliability"], "path": "questions/infrastructure-as-code/iac-platform-guardrails.html"},
  {"title": "Define an infrastructure-as-code state ownership model", "theme": "infrastructure-as-code", "difficulty": "staff", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "governance", "platform-engineering", "reliability"], "path": "questions/infrastructure-as-code/iac-state-ownership-model.html"},
  {"title": "Import an existing resource into Terraform", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/import-existing-infrastructure.html"},
  {"title": "Detect and handle infrastructure drift", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "reliability", "troubleshooting", "cgoa"], "path": "questions/infrastructure-as-code/infrastructure-drift.html"},
  {"title": "Define safe Terraform input variables", "theme": "infrastructure-as-code", "difficulty": "junior", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/input-variables-and-validation.html"},
  {"title": "Distinguish Terraform local values from data sources", "theme": "infrastructure-as-code", "difficulty": "junior", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation"], "path": "questions/infrastructure-as-code/local-values-and-data-sources.html"},
  {"title": "Design a stable Terraform module interface", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/module-interface-design.html"},
  {"title": "Isolate Terraform environments and blast radius", "theme": "infrastructure-as-code", "difficulty": "senior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "security", "reliability", "governance"], "path": "questions/infrastructure-as-code/multi-environment-isolation.html"},
  {"title": "Design Terraform outputs without exposing secrets", "theme": "infrastructure-as-code", "difficulty": "junior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "security", "automation"], "path": "questions/infrastructure-as-code/output-contracts-and-sensitive-data.html"},
  {"title": "Design policy-as-code gates for Terraform delivery", "theme": "infrastructure-as-code", "difficulty": "senior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "security", "automation", "governance", "cgoa"], "path": "questions/infrastructure-as-code/policy-as-code-gates.html"},
  {"title": "Pin Terraform provider dependencies safely", "theme": "infrastructure-as-code", "difficulty": "junior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability", "security"], "path": "questions/infrastructure-as-code/provider-version-pinning.html"},
  {"title": "Migrate Terraform state to a remote backend", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability", "security"], "path": "questions/infrastructure-as-code/remote-backend-migration.html"},
  {"title": "Use Terraform lifecycle rules without masking risk", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "deployment", "reliability"], "path": "questions/infrastructure-as-code/resource-lifecycle-controls.html"},
  {"title": "Refactor Terraform resource addresses safely", "theme": "infrastructure-as-code", "difficulty": "senior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "deployment", "reliability"], "path": "questions/infrastructure-as-code/safe-resource-refactoring.html"},
  {"title": "Handle Terraform state lock contention", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "troubleshooting", "tags": ["terraform", "infrastructure-as-code", "troubleshooting", "reliability"], "path": "questions/infrastructure-as-code/state-lock-contention.html"},
  {"title": "Explain a Terraform root module and resource address", "theme": "infrastructure-as-code", "difficulty": "junior", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation"], "path": "questions/infrastructure-as-code/terraform-configuration-basics.html"},
  {"title": "Review a Terraform plan before production apply", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "deployment", "reliability"], "path": "questions/infrastructure-as-code/terraform-plan-review.html"},
  {"title": "Why does Terraform use state?", "theme": "infrastructure-as-code", "difficulty": "middle", "type": "theory", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability", "cgoa"], "path": "questions/infrastructure-as-code/terraform-state-purpose.html"},
  {"title": "Build a Terraform testing strategy", "theme": "infrastructure-as-code", "difficulty": "senior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "automation", "reliability"], "path": "questions/infrastructure-as-code/terraform-test-strategy.html"},
  {"title": "Plan a zero-downtime infrastructure migration with Terraform", "theme": "infrastructure-as-code", "difficulty": "senior", "type": "scenario", "tags": ["terraform", "infrastructure-as-code", "deployment", "availability", "reliability"], "path": "questions/infrastructure-as-code/zero-downtime-iac-migration.html"},
  {"title": "Establish Kubernetes admission policy guardrails", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "governance", "automation", "cks", "kcsa", "cka", "ckad", "cnpe", "cnpa"], "path": "questions/kubernetes/admission-policy-and-guardrails.html"},
  {"title": "Migrate an application away from a deprecated Kubernetes API", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "deployment", "reliability", "automation", "ckad"], "path": "questions/kubernetes/api-deprecation-migration.html"},
  {"title": "Debug a failing Kubernetes application with built-in CLI tools", "theme": "kubernetes", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "troubleshooting", "observability", "logging", "deployment", "ckad"], "path": "questions/kubernetes/application-debugging-with-cli.html"},
  {"title": "Design a Kubernetes audit policy for security detection", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "logging", "observability", "incident-response", "cks", "cnpe"], "path": "questions/kubernetes/audit-policy-runtime-detection.html"},
  {"title": "Explain the roles of Cilium agents, operator, and Envoy", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "networking", "security", "observability", "cca"], "path": "questions/kubernetes/cilium-component-roles.html"},
  {"title": "Validate a new Cilium installation before production traffic", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "networking", "deployment", "troubleshooting", "reliability", "cca", "ckne"], "path": "questions/kubernetes/cilium-install-connectivity-validation.html"},
  {"title": "Choose a Cilium IPAM mode for a Kubernetes cluster", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "networking", "cloud", "reliability", "cca", "ckne"], "path": "questions/kubernetes/cilium-ipam-mode-selection.html"},
  {"title": "Choose a Cilium policy-enforcement mode", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "networking", "security", "reliability", "cca"], "path": "questions/kubernetes/cilium-policy-enforcement-modes.html"},
  {"title": "Remediate a Kubernetes CIS benchmark finding", "theme": "kubernetes", "difficulty": "senior", "type": "troubleshooting", "tags": ["kubernetes", "security", "cks", "troubleshooting", "governance"], "path": "questions/kubernetes/cis-benchmark-remediation.html"},
  {"title": "Explain cloud-native principles and open-source collaboration", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "containers", "automation", "reliability", "kcna"], "path": "questions/kubernetes/cloud-native-principles-and-community.html"},
  {"title": "Plan a production Kubernetes cluster upgrade", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "deployment", "reliability", "governance", "security", "cks", "cka"], "path": "questions/kubernetes/cluster-upgrade-strategy.html"},
  {"title": "Deliver application configuration with ConfigMaps", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "configuration-management", "deployment", "reliability", "cka", "ckad", "kcna", "cba"], "path": "questions/kubernetes/configmap-delivery.html"},
  {"title": "Triage a Kubernetes control-plane availability incident", "theme": "kubernetes", "difficulty": "senior", "type": "troubleshooting", "tags": ["kubernetes", "incident-response", "observability", "reliability", "kcsa", "cka", "kcna"], "path": "questions/kubernetes/control-plane-incident-triage.html"},
  {"title": "Debug CoreDNS and Kubernetes Service resolution", "theme": "kubernetes", "difficulty": "senior", "type": "troubleshooting", "tags": ["kubernetes", "cka", "ckad", "networking", "dns", "troubleshooting", "ckne"], "path": "questions/kubernetes/coredns-service-debugging.html"},
  {"title": "Operate a custom resource and its controller safely", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "automation", "reliability", "security", "cnpe", "cnpa", "cgoa"], "path": "questions/kubernetes/crd-operator-lifecycle.html"},
  {"title": "Explain a Kubernetes Deployment rollout and rollback", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "deployment", "rolling-update", "reliability", "cka", "ckad", "kcna", "cba"], "path": "questions/kubernetes/deployment-rollout-and-rollback.html"},
  {"title": "Lead Kubernetes disaster recovery and restore exercises", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "incident-response", "reliability", "storage", "governance", "cka"], "path": "questions/kubernetes/disaster-recovery-and-restore-exercise.html"},
  {"title": "Govern a migration from Ingress to Gateway API", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "networking", "deployment", "governance", "reliability", "kcsa", "cka", "ckad", "ckne"], "path": "questions/kubernetes/gateway-migration-governance.html"},
  {"title": "Design a highly available kubeadm control plane", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "cka", "availability", "reliability", "networking"], "path": "questions/kubernetes/ha-control-plane-design.html"},
  {"title": "Install a cluster component with Helm or Kustomize safely", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "deployment", "configuration-management", "security", "cgoa"], "path": "questions/kubernetes/helm-kustomize-component-installation.html"},
  {"title": "Configure HorizontalPodAutoscaler behavior", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "monitoring", "capacity-planning", "reliability", "cka", "ckad"], "path": "questions/kubernetes/hpa-behavior-and-metrics.html"},
  {"title": "Configure TLS for Kubernetes Ingress safely", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "tls", "networking", "cks"], "path": "questions/kubernetes/ingress-tls-security.html"},
  {"title": "Build and maintain a kubeadm-managed cluster", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "cka", "automation", "security", "reliability"], "path": "questions/kubernetes/kubeadm-cluster-lifecycle.html"},
  {"title": "Test Kyverno policy changes with the CLI in CI", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca", "ci-cd", "automation"], "path": "questions/kubernetes/kyverno-cli-policy-ci.html"},
  {"title": "Roll out Kyverno enforcement using policy reports", "theme": "kubernetes", "difficulty": "middle", "type": "troubleshooting", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca", "monitoring", "troubleshooting"], "path": "questions/kubernetes/kyverno-enforcement-and-policy-reports.html"},
  {"title": "Install or upgrade Kyverno without blocking the cluster", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca", "rolling-update"], "path": "questions/kubernetes/kyverno-installation-upgrade-safety.html"},
  {"title": "Design a maintainable Kyverno policy set", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca", "supply-chain"], "path": "questions/kubernetes/kyverno-policy-authoring-design.html"},
  {"title": "Explain Kyverno policy-engine fundamentals", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca"], "path": "questions/kubernetes/kyverno-policy-engine-basics.html"},
  {"title": "Govern the Kyverno policy lifecycle and exceptions", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "security", "policy-as-code", "kyverno", "kca", "governance", "change-management"], "path": "questions/kubernetes/kyverno-policy-lifecycle-governance.html"},
  {"title": "Distinguish labels, selectors, and annotations", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "deployment", "automation", "cka", "ckad", "kcna", "cba"], "path": "questions/kubernetes/labels-selectors-and-annotations.html"},
  {"title": "Choose an init container or sidecar for an application Pod", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "containers", "deployment", "reliability", "ckad"], "path": "questions/kubernetes/multi-container-pod-patterns.html"},
  {"title": "Define multi-tenant Kubernetes platform boundaries", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "security", "governance", "platform-engineering", "reliability", "cka", "cnpe"], "path": "questions/kubernetes/multi-tenant-platform-boundaries.html"},
  {"title": "Use Kubernetes namespaces and resource scope correctly", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "security", "governance", "cka", "kcna"], "path": "questions/kubernetes/namespaces-and-resource-scope.html"},
  {"title": "Restrict Pod traffic with NetworkPolicy", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "networking", "security", "least-privilege", "cks", "kcsa", "cka", "ckad", "kcna", "cca", "ckne"], "path": "questions/kubernetes/network-policy-enforcement.html"},
  {"title": "Triage a Kubernetes node that becomes NotReady", "theme": "kubernetes", "difficulty": "senior", "type": "troubleshooting", "tags": ["kubernetes", "cka", "linux", "monitoring", "troubleshooting", "reliability"], "path": "questions/kubernetes/node-not-ready-triage.html"},
  {"title": "Design PersistentVolumeClaim lifecycle for a stateful workload", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "storage", "reliability", "deployment", "kcsa", "cka", "ckad", "kcna"], "path": "questions/kubernetes/persistent-volume-claim-lifecycle.html"},
  {"title": "Set Kubernetes platform SLO and capacity governance", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "observability", "capacity-planning", "reliability", "governance", "kcsa", "cka"], "path": "questions/kubernetes/platform-slo-and-capacity-governance.html"},
  {"title": "Use PodDisruptionBudgets for voluntary disruptions", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "availability", "reliability", "deployment", "cka"], "path": "questions/kubernetes/pod-disruption-budget-design.html"},
  {"title": "Explain Pod lifecycle and container restarts", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "troubleshooting", "reliability", "cka", "ckad", "kcna"], "path": "questions/kubernetes/pod-lifecycle-and-restarts.html"},
  {"title": "Read the essential parts of a Pod specification", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "containers", "deployment", "cka", "ckad", "kcna", "must-know"], "path": "questions/kubernetes/pod-spec-basics.html"},
  {"title": "Select Kubernetes readiness, liveness, and startup probes", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "reliability", "troubleshooting", "cka", "ckad", "kcna"], "path": "questions/kubernetes/probe-selection.html"},
  {"title": "Design a production Kubernetes policy exception process", "theme": "kubernetes", "difficulty": "staff", "type": "scenario", "tags": ["kubernetes", "security", "governance", "delivery", "reliability", "kcsa", "cka"], "path": "questions/kubernetes/production-policy-exception-process.html"},
  {"title": "Design least-privilege Kubernetes RBAC", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "least-privilege", "governance", "cks", "kcsa", "cka", "ckad", "kcna", "cnpe", "cnpa"], "path": "questions/kubernetes/rbac-least-privilege.html"},
  {"title": "Set Pod resource requests and limits", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "resource-limits", "capacity-planning", "reliability", "kcsa", "cka", "ckad", "kcna"], "path": "questions/kubernetes/resource-requests-limits-and-qos.html"},
  {"title": "Use RuntimeClass for higher-risk workload isolation", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "containers", "platform-engineering", "cks"], "path": "questions/kubernetes/runtimeclass-sandbox-isolation.html"},
  {"title": "Place Kubernetes workloads with affinity and taints", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "capacity-planning", "reliability", "security", "cka", "kcna"], "path": "questions/kubernetes/scheduling-affinity-and-taints.html"},
  {"title": "Apply seccomp and AppArmor to a Kubernetes workload", "theme": "kubernetes", "difficulty": "senior", "type": "scenario", "tags": ["kubernetes", "security", "linux", "containers", "least-privilege", "cks"], "path": "questions/kubernetes/seccomp-apparmor-workload.html"},
  {"title": "Secure Kubernetes Secret access and rotation", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "least-privilege", "automation", "cks", "kcsa", "cka", "ckad", "kcna", "cba"], "path": "questions/kubernetes/secrets-access-and-rotation.html"},
  {"title": "Give a Kubernetes workload the least-privilege ServiceAccount", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "security", "least-privilege", "deployment", "ckad"], "path": "questions/kubernetes/service-account-workload-identity.html"},
  {"title": "Explain Kubernetes Service discovery", "theme": "kubernetes", "difficulty": "junior", "type": "theory", "tags": ["kubernetes", "networking", "dns", "reliability", "cka", "ckad", "kcna", "cca"], "path": "questions/kubernetes/service-discovery-basics.html"},
  {"title": "Expose an application with the right Service type", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "cka", "ckad", "networking", "availability", "troubleshooting", "ckne"], "path": "questions/kubernetes/service-types-and-endpoints.html"},
  {"title": "Choose StatefulSet or Deployment", "theme": "kubernetes", "difficulty": "middle", "type": "scenario", "tags": ["kubernetes", "deployment", "storage", "reliability", "cka", "ckad"], "path": "questions/kubernetes/statefulset-versus-deployment.html"},
  {"title": "Diagnose a cgroup resource limit problem", "theme": "linux", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "cgroups", "reliability", "troubleshooting", "must-know"], "path": "questions/linux/cgroups-resource-isolation.html"},
  {"title": "Configure filesystem automounts without hiding a dependency failure", "theme": "linux", "difficulty": "middle", "type": "scenario", "tags": ["linux", "storage", "filesystem", "operations", "lfcs"], "path": "questions/linux/configure-filesystem-automounts.html"},
  {"title": "Configure LVM storage for a growing service", "theme": "linux", "difficulty": "middle", "type": "scenario", "tags": ["linux", "storage", "filesystem", "operations", "lfcs"], "path": "questions/linux/configure-lvm-storage.html"},
  {"title": "Choose between cron and systemd timers", "theme": "linux", "difficulty": "middle", "type": "scenario", "tags": ["linux", "automation", "reliability", "lfcs"], "path": "questions/linux/cron-versus-systemd-timers.html"},
  {"title": "Recover disk space held by deleted open files", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "filesystem", "troubleshooting", "lfcs"], "path": "questions/linux/deleted-open-files.html"},
  {"title": "Diagnose too many open files in a Linux service", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting", "lfcs"], "path": "questions/linux/file-descriptor-exhaustion.html"},
  {"title": "Respond to a filesystem mounted read-only after errors", "theme": "linux", "difficulty": "middle", "type": "scenario", "tags": ["linux", "filesystem", "storage", "troubleshooting", "lfcs"], "path": "questions/linux/filesystem-check-failure.html"},
  {"title": "Establish Linux fleet capacity governance", "theme": "linux", "difficulty": "staff", "type": "scenario", "tags": ["linux", "monitoring", "reliability", "automation"], "path": "questions/linux/fleet-capacity-governance.html"},
  {"title": "Define a Linux fleet lifecycle standard", "theme": "linux", "difficulty": "staff", "type": "scenario", "tags": ["linux", "security", "reliability", "automation"], "path": "questions/linux/fleet-os-lifecycle.html"},
  {"title": "Integrate LDAP users through SSSD safely", "theme": "linux", "difficulty": "senior", "type": "scenario", "tags": ["linux", "security", "permissions", "operations", "lfcs"], "path": "questions/linux/integrate-ldap-users-with-sssd.html"},
  {"title": "Plan a production Linux kernel upgrade and rollback", "theme": "linux", "difficulty": "senior", "type": "scenario", "tags": ["linux", "deployment", "reliability", "troubleshooting", "lfcs"], "path": "questions/linux/kernel-upgrade-rollback.html"},
  {"title": "Explain the Linux boot sequence", "theme": "linux", "difficulty": "middle", "type": "theory", "tags": ["linux", "troubleshooting", "must-know"], "path": "questions/linux/linux-boot-sequence.html"},
  {"title": "Apply Linux capabilities instead of full root privilege", "theme": "linux", "difficulty": "senior", "type": "scenario", "tags": ["linux", "security", "least-privilege", "lfcs"], "path": "questions/linux/linux-capabilities-least-privilege.html"},
  {"title": "Design a Linux incident evidence and forensics policy", "theme": "linux", "difficulty": "staff", "type": "scenario", "tags": ["linux", "security", "incident-response", "reliability"], "path": "questions/linux/linux-incident-forensics-policy.html"},
  {"title": "Define SLOs for a Linux host platform", "theme": "linux", "difficulty": "staff", "type": "theory", "tags": ["linux", "observability", "reliability", "monitoring"], "path": "questions/linux/linux-platform-slo.html"},
  {"title": "Govern a Linux security baseline without blocking delivery", "theme": "linux", "difficulty": "staff", "type": "scenario", "tags": ["linux", "security", "least-privilege", "automation"], "path": "questions/linux/linux-security-baseline.html"},
  {"title": "Interpret a high Linux load average", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "monitoring", "troubleshooting", "lfcs"], "path": "questions/linux/load-average-interpretation.html"},
  {"title": "Maintain package repositories without breaking fleet updates", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "operations", "troubleshooting", "security", "lfcs"], "path": "questions/linux/maintain-package-repositories.html"},
  {"title": "Manage a libvirt virtual machine change safely", "theme": "linux", "difficulty": "senior", "type": "scenario", "tags": ["linux", "virtualization", "operations", "change-management", "lfcs"], "path": "questions/linux/manage-libvirt-virtual-machines.html"},
  {"title": "Explain mounts and filesystem types on Linux", "theme": "linux", "difficulty": "junior", "type": "theory", "tags": ["linux", "filesystem", "storage"], "path": "questions/linux/mounts-and-filesystem-types.html"},
  {"title": "Investigate a Linux out-of-memory kill", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting"], "path": "questions/linux/oom-killer-investigation.html"},
  {"title": "Explain Linux permissions and umask", "theme": "linux", "difficulty": "junior", "type": "theory", "tags": ["linux", "security", "least-privilege", "lfcs"], "path": "questions/linux/permissions-and-umask.html"},
  {"title": "Debug process visibility across PID namespaces", "theme": "linux", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "containers", "debugging", "troubleshooting"], "path": "questions/linux/pid-namespaces-debugging.html"},
  {"title": "Investigate a failure that occurred only during the previous boot", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting"], "path": "questions/linux/previous-boot-log-analysis.html"},
  {"title": "Use process priorities without hiding a capacity problem", "theme": "linux", "difficulty": "junior", "type": "scenario", "tags": ["linux", "reliability", "troubleshooting"], "path": "questions/linux/process-priorities.html"},
  {"title": "Explain Linux process states during an incident", "theme": "linux", "difficulty": "junior", "type": "theory", "tags": ["linux", "debugging", "troubleshooting", "lfcs"], "path": "questions/linux/process-states.html"},
  {"title": "Debug an application that works in a shell but fails as a service", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting", "lfcs"], "path": "questions/linux/service-environment-debugging.html"},
  {"title": "Design a graceful Linux service shutdown", "theme": "linux", "difficulty": "junior", "type": "scenario", "tags": ["linux", "reliability", "deployment"], "path": "questions/linux/signals-and-graceful-shutdown.html"},
  {"title": "Use strace safely to investigate a hung Linux process", "theme": "linux", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting"], "path": "questions/linux/strace-production-safely.html"},
  {"title": "Diagnose a systemd service that repeatedly fails", "theme": "linux", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "debugging", "troubleshooting", "lfcs"], "path": "questions/linux/systemd-service-failure.html"},
  {"title": "Validate Linux bond failover behavior", "theme": "linux-networking", "difficulty": "middle", "type": "scenario", "tags": ["linux", "networking", "availability", "troubleshooting", "lfcs"], "path": "questions/linux-networking/bond-failover-validation.html"},
  {"title": "Triage Linux connection-tracking exhaustion", "theme": "linux-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "troubleshooting", "monitoring"], "path": "questions/linux-networking/conntrack-exhaustion-triage.html"},
  {"title": "Design a default-deny host firewall with nftables", "theme": "linux-networking", "difficulty": "senior", "type": "scenario", "tags": ["linux", "networking", "security", "least-privilege", "tcp"], "path": "questions/linux-networking/default-deny-host-firewall-design.html"},
  {"title": "Explain a Linux default route", "theme": "linux-networking", "difficulty": "junior", "type": "theory", "tags": ["linux", "networking"], "path": "questions/linux-networking/default-route-basics.html"},
  {"title": "Explain Linux DNS resolver configuration", "theme": "linux-networking", "difficulty": "junior", "type": "theory", "tags": ["linux", "networking", "dns", "troubleshooting", "lfcs"], "path": "questions/linux-networking/dns-resolver-configuration.html"},
  {"title": "Set a Linux dual-stack host strategy", "theme": "linux-networking", "difficulty": "staff", "type": "scenario", "tags": ["linux", "networking", "dns", "reliability", "governance"], "path": "questions/linux-networking/dual-stack-host-strategy.html"},
  {"title": "Triage a Linux host firewall path", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "security", "troubleshooting", "lfcs"], "path": "questions/linux-networking/firewall-path-triage.html"},
  {"title": "Govern Linux host network changes", "theme": "linux-networking", "difficulty": "staff", "type": "scenario", "tags": ["linux", "networking", "governance", "reliability", "deployment"], "path": "questions/linux-networking/host-network-change-governance.html"},
  {"title": "Inspect Linux interface state and addresses", "theme": "linux-networking", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting", "lfcs"], "path": "questions/linux-networking/interface-state-and-addresses.html"},
  {"title": "Explain iptables-nft compatibility on modern distros", "theme": "linux-networking", "difficulty": "middle", "type": "theory", "tags": ["linux", "networking", "security", "migration"], "path": "questions/linux-networking/iptables-nft-compatibility.html"},
  {"title": "Build a Linux network capacity strategy", "theme": "linux-networking", "difficulty": "staff", "type": "scenario", "tags": ["linux", "networking", "capacity-planning", "monitoring", "reliability"], "path": "questions/linux-networking/linux-network-capacity-strategy.html"},
  {"title": "Lead a Linux networking incident response", "theme": "linux-networking", "difficulty": "staff", "type": "scenario", "tags": ["linux", "networking", "incident-response", "reliability", "troubleshooting"], "path": "questions/linux-networking/linux-network-incident-command.html"},
  {"title": "Design Linux host network observability", "theme": "linux-networking", "difficulty": "senior", "type": "scenario", "tags": ["linux", "networking", "monitoring", "reliability", "ckne"], "path": "questions/linux-networking/linux-network-observability.html"},
  {"title": "Diagnose an MTU mismatch on Linux", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "troubleshooting"], "path": "questions/linux-networking/mtu-mismatch-triage.html"},
  {"title": "Triage a failed Linux neighbour entry", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting"], "path": "questions/linux-networking/neighbour-table-triage.html"},
  {"title": "Debug connectivity across a Linux network namespace", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "containers", "troubleshooting", "ckne"], "path": "questions/linux-networking/network-namespace-connectivity.html"},
  {"title": "Read an nftables ruleset", "theme": "linux-networking", "difficulty": "junior", "type": "theory", "tags": ["linux", "networking", "security"], "path": "questions/linux-networking/nftables-ruleset-reading.html"},
  {"title": "Explain why nftables replaces iptables", "theme": "linux-networking", "difficulty": "junior", "type": "theory", "tags": ["linux", "networking", "security"], "path": "questions/linux-networking/nftables-vs-iptables-motivation.html"},
  {"title": "Capture Linux packets without losing diagnostic value", "theme": "linux-networking", "difficulty": "middle", "type": "scenario", "tags": ["linux", "networking", "troubleshooting", "security", "ckne"], "path": "questions/linux-networking/packet-capture-scope.html"},
  {"title": "Interpret a Linux ping result safely", "theme": "linux-networking", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting"], "path": "questions/linux-networking/ping-interpretation.html"},
  {"title": "Diagnose Linux policy routing rules", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting"], "path": "questions/linux-networking/policy-routing-with-rules.html"},
  {"title": "Distinguish connection refused from a firewall drop", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "security", "troubleshooting", "tcp"], "path": "questions/linux-networking/refused-vs-dropped-diagnosis.html"},
  {"title": "Diagnose reverse-path filtering drops", "theme": "linux-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "networking", "security", "troubleshooting"], "path": "questions/linux-networking/reverse-path-filtering.html"},
  {"title": "Debug a Linux route with ip route get", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting", "lfcs"], "path": "questions/linux-networking/route-get-debugging.html"},
  {"title": "Identify the process listening on a Linux port", "theme": "linux-networking", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "troubleshooting"], "path": "questions/linux-networking/socket-listener-inspection.html"},
  {"title": "Diagnose a Linux TCP accept-backlog overflow", "theme": "linux-networking", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "troubleshooting", "performance"], "path": "questions/linux-networking/tcp-backlog-overflow.html"},
  {"title": "Triage TCP connection states on Linux", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "troubleshooting"], "path": "questions/linux-networking/tcp-connection-state-triage.html"},
  {"title": "Select a Linux traffic-control investigation path", "theme": "linux-networking", "difficulty": "senior", "type": "scenario", "tags": ["linux", "networking", "performance", "troubleshooting"], "path": "questions/linux-networking/traffic-control-qdisc.html"},
  {"title": "Triage a Linux VLAN interface", "theme": "linux-networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "troubleshooting"], "path": "questions/linux-networking/vlan-interface-triage.html"},
  {"title": "Set zero-trust Linux host network boundaries", "theme": "linux-networking", "difficulty": "staff", "type": "scenario", "tags": ["linux", "networking", "security", "least-privilege", "governance"], "path": "questions/linux-networking/zero-trust-host-network-boundaries.html"},
  {"title": "Triage cgroup memory-limit failures", "theme": "linux-performance", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "performance", "memory", "cgroups", "troubleshooting"], "path": "questions/linux-performance/cgroup-memory-limit-triage.html"},
  {"title": "Investigate excess context switching", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "debugging", "monitoring"], "path": "questions/linux-performance/context-switch-analysis.html"},
  {"title": "Investigate a growing CPU run queue", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "monitoring", "troubleshooting"], "path": "questions/linux-performance/cpu-run-queue-triage.html"},
  {"title": "Diagnose cgroup CPU throttling", "theme": "linux-performance", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "cgroups", "troubleshooting"], "path": "questions/linux-performance/cpu-throttling-diagnosis.html"},
  {"title": "Read CPU utilization before tuning", "theme": "linux-performance", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "monitoring", "troubleshooting"], "path": "questions/linux-performance/cpu-utilization-basics.html"},
  {"title": "Diagnose a full filesystem with free-looking space", "theme": "linux-performance", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "performance", "filesystem", "storage", "troubleshooting"], "path": "questions/linux-performance/disk-space-versus-inodes.html"},
  {"title": "Diagnose file-descriptor exhaustion", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "filesystem", "troubleshooting", "reliability"], "path": "questions/linux-performance/file-descriptor-exhaustion.html"},
  {"title": "Interpret iowait without blaming storage immediately", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "storage", "monitoring", "troubleshooting"], "path": "questions/linux-performance/iowait-interpretation.html"},
  {"title": "Evaluate kernel samepage merging safely", "theme": "linux-performance", "difficulty": "senior", "type": "scenario", "tags": ["linux", "performance", "memory", "virtualization", "security"], "path": "questions/linux-performance/kernel-samepage-merging.html"},
  {"title": "Interpret Linux load average correctly", "theme": "linux-performance", "difficulty": "junior", "type": "theory", "tags": ["linux", "performance", "cpu", "monitoring", "troubleshooting"], "path": "questions/linux-performance/load-average-meaning.html"},
  {"title": "Distinguish free memory from available memory", "theme": "linux-performance", "difficulty": "junior", "type": "theory", "tags": ["linux", "performance", "memory", "monitoring"], "path": "questions/linux-performance/memory-available-basics.html"},
  {"title": "Triage TCP retransmissions on a Linux service", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "networking", "tcp", "troubleshooting"], "path": "questions/linux-performance/network-retransmission-triage.html"},
  {"title": "Design a noisy-neighbor performance policy", "theme": "linux-performance", "difficulty": "staff", "type": "scenario", "tags": ["linux", "performance", "cgroups", "capacity-planning", "governance"], "path": "questions/linux-performance/noisy-neighbor-policy.html"},
  {"title": "Recognize NUMA locality as a performance constraint", "theme": "linux-performance", "difficulty": "senior", "type": "scenario", "tags": ["linux", "performance", "cpu", "memory", "capacity-planning"], "path": "questions/linux-performance/numa-locality.html"},
  {"title": "Govern performance-observability overhead", "theme": "linux-performance", "difficulty": "staff", "type": "scenario", "tags": ["linux", "performance", "observability", "governance", "security"], "path": "questions/linux-performance/observability-overhead-governance.html"},
  {"title": "Analyze a Linux OOM kill", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "memory", "troubleshooting", "incident-response"], "path": "questions/linux-performance/oom-killer-analysis.html"},
  {"title": "Investigate page-cache reclaim and memory pressure", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "memory", "filesystem", "troubleshooting"], "path": "questions/linux-performance/page-cache-reclaim.html"},
  {"title": "Profile CPU with perf safely in production", "theme": "linux-performance", "difficulty": "senior", "type": "scenario", "tags": ["linux", "performance", "cpu", "debugging", "observability"], "path": "questions/linux-performance/perf-sampling-safety.html"},
  {"title": "Establish a Linux performance baseline program", "theme": "linux-performance", "difficulty": "staff", "type": "scenario", "tags": ["linux", "performance", "monitoring", "capacity-planning", "governance"], "path": "questions/linux-performance/performance-baseline-program.html"},
  {"title": "Build a capacity model for a Linux service", "theme": "linux-performance", "difficulty": "staff", "type": "scenario", "tags": ["linux", "performance", "capacity-planning", "reliability", "governance"], "path": "questions/linux-performance/performance-capacity-model.html"},
  {"title": "Lead a Linux performance incident", "theme": "linux-performance", "difficulty": "staff", "type": "scenario", "tags": ["linux", "performance", "incident-response", "monitoring", "reliability"], "path": "questions/linux-performance/performance-incident-command.html"},
  {"title": "Use pressure stall information to find contention", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "memory", "monitoring"], "path": "questions/linux-performance/pressure-stall-information.html"},
  {"title": "Diagnose network softirq saturation", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "networking", "cpu", "troubleshooting"], "path": "questions/linux-performance/softirq-saturation.html"},
  {"title": "Respond to sustained swap activity", "theme": "linux-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "memory", "troubleshooting", "reliability", "lfcs"], "path": "questions/linux-performance/swap-activity-response.html"},
  {"title": "Use vmstat for a first performance pass", "theme": "linux-performance", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "performance", "cpu", "memory", "monitoring"], "path": "questions/linux-performance/vmstat-first-pass.html"},
  {"title": "Analyze a host with a high load average but low CPU utilization", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "load", "cpu", "troubleshooting"], "path": "questions/linux-troubleshooting/analyze-load-average.html"},
  {"title": "Architect Linux fleet observability for rapid fault isolation", "theme": "linux-troubleshooting", "difficulty": "staff", "type": "troubleshooting", "tags": ["linux", "observability", "metrics", "logging", "troubleshooting"], "path": "questions/linux-troubleshooting/architect-linux-observability.html"},
  {"title": "Coordinate a cross-team major incident rooted in Linux host failures", "theme": "linux-troubleshooting", "difficulty": "staff", "type": "troubleshooting", "tags": ["linux", "incident-management", "troubleshooting", "leadership"], "path": "questions/linux-troubleshooting/coordinate-linux-major-incident.html"},
  {"title": "Debug a failed network or local mount at boot", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "filesystem", "systemd", "mount", "troubleshooting", "lfcs"], "path": "questions/linux-troubleshooting/debug-failed-mount.html"},
  {"title": "Lead evidence-preserving triage after a Linux kernel panic", "theme": "linux-troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "kernel", "panic", "incident-response"], "path": "questions/linux-troubleshooting/debug-kernel-panic.html"},
  {"title": "Debug a Linux `Permission denied` failure for a service", "theme": "linux-troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "permissions", "selinux", "troubleshooting", "lfcs"], "path": "questions/linux-troubleshooting/debug-permission-denied.html"},
  {"title": "Design an evidence-driven Linux troubleshooting runbook program", "theme": "linux-troubleshooting", "difficulty": "staff", "type": "troubleshooting", "tags": ["linux", "runbooks", "incident-response", "operations"], "path": "questions/linux-troubleshooting/design-linux-troubleshooting-runbooks.html"},
  {"title": "Diagnose a Linux filesystem reported as full", "theme": "linux-troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "filesystem", "disk", "troubleshooting"], "path": "questions/linux-troubleshooting/diagnose-full-filesystem.html"},
  {"title": "Diagnose an application stalled on an NFS mount", "theme": "linux-troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "nfs", "storage", "troubleshooting"], "path": "questions/linux-troubleshooting/diagnose-nfs-stall.html"},
  {"title": "Diagnose an OOM-killed service in a cgroup-aware host", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "cgroups", "oom", "memory", "troubleshooting"], "path": "questions/linux-troubleshooting/diagnose-oom-kill.html"},
  {"title": "Diagnose a systemd service that starts before its dependency is usable", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "systemd", "dependencies", "troubleshooting"], "path": "questions/linux-troubleshooting/diagnose-systemd-dependency.html"},
  {"title": "Govern fleet-wide Linux kernel update and rollback decisions", "theme": "linux-troubleshooting", "difficulty": "staff", "type": "troubleshooting", "tags": ["linux", "kernel", "change-management", "reliability"], "path": "questions/linux-troubleshooting/govern-fleet-kernel-updates.html"},
  {"title": "Inspect a Linux service that is failing after a restart", "theme": "linux-troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["systemd", "journald", "logs", "troubleshooting"], "path": "questions/linux-troubleshooting/inspect-service-logs.html"},
  {"title": "Investigate a service that reports too many open files", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "file-descriptors", "limits", "troubleshooting"], "path": "questions/linux-troubleshooting/investigate-file-descriptors.html"},
  {"title": "Investigate a Linux hung-task warning or D-state process", "theme": "linux-troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "kernel", "processes", "troubleshooting"], "path": "questions/linux-troubleshooting/investigate-hung-task.html"},
  {"title": "Investigate Linux memory pressure without immediately adding RAM", "theme": "linux-troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "memory", "oom", "troubleshooting"], "path": "questions/linux-troubleshooting/investigate-memory-pressure.html"},
  {"title": "Investigate accumulating zombie processes on Linux", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "processes", "pid1", "troubleshooting"], "path": "questions/linux-troubleshooting/investigate-zombie-processes.html"},
  {"title": "Lead capacity and saturation risk management for a Linux platform", "theme": "linux-troubleshooting", "difficulty": "staff", "type": "troubleshooting", "tags": ["linux", "capacity", "performance", "reliability"], "path": "questions/linux-troubleshooting/lead-linux-capacity-risk.html"},
  {"title": "Perform first-pass storage I/O latency triage on Linux", "theme": "linux-troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "storage", "io", "latency", "troubleshooting"], "path": "questions/linux-troubleshooting/perform-storage-io-triage.html"},
  {"title": "Recover from an interrupted Linux package transaction safely", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "packages", "recovery", "troubleshooting"], "path": "questions/linux-troubleshooting/recover-package-manager.html"},
  {"title": "Recover safely from a Linux boot failure after a configuration change", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "boot", "systemd", "recovery"], "path": "questions/linux-troubleshooting/repair-boot-failure.html"},
  {"title": "Resolve clock skew that is breaking Linux service authentication", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "time", "ntp", "tls", "troubleshooting"], "path": "questions/linux-troubleshooting/resolve-clock-skew.html"},
  {"title": "Trace suspected connection-tracking exhaustion on a Linux node", "theme": "linux-troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "networking", "conntrack", "troubleshooting"], "path": "questions/linux-troubleshooting/trace-conntrack-exhaustion.html"},
  {"title": "Trace an intermittent DNS resolution failure on Linux", "theme": "linux-troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "dns", "resolver", "troubleshooting"], "path": "questions/linux-troubleshooting/trace-dns-failure.html"},
  {"title": "Triage packet loss from a Linux host to a critical dependency", "theme": "linux-troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "packet-loss", "troubleshooting", "lfcs"], "path": "questions/linux-troubleshooting/triage-network-packet-loss.html"},
  {"title": "Distinguish audit logs from application logs", "theme": "logging", "difficulty": "middle", "type": "theory", "tags": ["logging", "security", "governance", "incident-response"], "path": "questions/logging/audit-vs-application-logs.html"},
  {"title": "Design collector buffering and backpressure", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "observability", "reliability", "capacity-planning", "otca"], "path": "questions/logging/collector-buffering.html"},
  {"title": "Enrich Kubernetes logs without destroying provenance", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "kubernetes", "observability", "debugging", "otca"], "path": "questions/logging/kubernetes-log-enrichment.html"},
  {"title": "Attribute and reduce logging cost safely", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "cost-optimization", "capacity-planning", "governance"], "path": "questions/logging/log-cost-attribution.html"},
  {"title": "Choose fields for a log data model", "theme": "logging", "difficulty": "junior", "type": "theory", "tags": ["logging", "observability", "debugging", "otca"], "path": "questions/logging/log-data-model.html"},
  {"title": "Preserve log integrity for an investigation", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "security", "incident-response", "governance"], "path": "questions/logging/log-forensics-integrity.html"},
  {"title": "Define a production log-level policy", "theme": "logging", "difficulty": "junior", "type": "theory", "tags": ["logging", "observability", "debugging", "operations"], "path": "questions/logging/log-level-policy.html"},
  {"title": "Define an SLO for a log delivery pipeline", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "reliability", "monitoring", "observability", "otca"], "path": "questions/logging/log-pipeline-slo.html"},
  {"title": "Diagnose a slow expensive log query", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "performance", "capacity-planning", "troubleshooting"], "path": "questions/logging/log-query-performance.html"},
  {"title": "Define a log retention policy", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "security", "governance", "cost-optimization"], "path": "questions/logging/log-retention-policy.html"},
  {"title": "Use logs effectively during a cross-service incident", "theme": "logging", "difficulty": "staff", "type": "scenario", "tags": ["logging", "incident-management", "leadership", "troubleshooting"], "path": "questions/logging/logging-incident-command.html"},
  {"title": "Migrate a company from fragmented logging to a common platform", "theme": "logging", "difficulty": "staff", "type": "scenario", "tags": ["logging", "platform-engineering", "change-management", "leadership"], "path": "questions/logging/logging-migration.html"},
  {"title": "Define ownership boundaries for a logging service", "theme": "logging", "difficulty": "staff", "type": "scenario", "tags": ["logging", "platform-engineering", "reliability", "leadership"], "path": "questions/logging/logging-service-ownership.html"},
  {"title": "Select and filter log streams with LogQL", "theme": "logging", "difficulty": "junior", "type": "theory", "tags": ["logging", "loki", "grafana", "debugging"], "path": "questions/logging/logql-stream-filtering-basics.html"},
  {"title": "Explain Loki architecture and label design", "theme": "logging", "difficulty": "middle", "type": "theory", "tags": ["logging", "loki", "grafana", "observability"], "path": "questions/logging/loki-architecture-and-label-design.html"},
  {"title": "Design Loki retention and multi-tenancy", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "loki", "grafana", "multi-tenancy"], "path": "questions/logging/loki-retention-and-multi-tenancy.html"},
  {"title": "Compare Loki and ELK for log platform cost", "theme": "logging", "difficulty": "middle", "type": "theory", "tags": ["logging", "loki", "grafana", "cost-optimization"], "path": "questions/logging/loki-vs-elk-tradeoffs.html"},
  {"title": "Parse multiline exception logs safely", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "debugging", "troubleshooting", "observability"], "path": "questions/logging/multiline-log-parsing.html"},
  {"title": "Set a platform strategy for organization-wide logging", "theme": "logging", "difficulty": "staff", "type": "scenario", "tags": ["logging", "platform-engineering", "governance", "leadership"], "path": "questions/logging/organization-logging-platform.html"},
  {"title": "Govern logging with privacy by design", "theme": "logging", "difficulty": "staff", "type": "scenario", "tags": ["logging", "security", "governance", "leadership"], "path": "questions/logging/privacy-by-design.html"},
  {"title": "Handle log rotation without duplicate or missing events", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "linux", "reliability", "troubleshooting"], "path": "questions/logging/rotation-and-tailers.html"},
  {"title": "Evolve a log schema without breaking consumers", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "observability", "change-management", "reliability", "otca"], "path": "questions/logging/schema-evolution.html"},
  {"title": "Prevent secrets from entering logs", "theme": "logging", "difficulty": "junior", "type": "scenario", "tags": ["logging", "security", "incident-response", "troubleshooting"], "path": "questions/logging/secret-redaction.html"},
  {"title": "Explain why containers log to standard streams", "theme": "logging", "difficulty": "junior", "type": "theory", "tags": ["logging", "containers", "kubernetes", "observability"], "path": "questions/logging/stdout-in-containers.html"},
  {"title": "Design structured logs for request correlation", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "observability", "debugging", "incident-response", "otca"], "path": "questions/logging/structured-log-correlation.html"},
  {"title": "Convert journald and Flask logs to structured JSON", "theme": "logging", "difficulty": "junior", "type": "scenario", "tags": ["logging", "observability", "debugging", "journald"], "path": "questions/logging/structured-logging-json-format.html"},
  {"title": "Explain syslog facilities and severity", "theme": "logging", "difficulty": "junior", "type": "theory", "tags": ["logging", "linux", "operations", "troubleshooting"], "path": "questions/logging/syslog-basics.html"},
  {"title": "Isolate tenants in a shared logging platform", "theme": "logging", "difficulty": "senior", "type": "scenario", "tags": ["logging", "security", "reliability", "platform-engineering"], "path": "questions/logging/tenant-isolation.html"},
  {"title": "Make log timestamps useful in incident analysis", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "time", "debugging", "incident-response"], "path": "questions/logging/timestamp-correctness.html"},
  {"title": "Correlate trace context with logs", "theme": "logging", "difficulty": "middle", "type": "scenario", "tags": ["logging", "observability", "debugging", "distributed-systems", "otca"], "path": "questions/logging/trace-log-correlation.html"},
  {"title": "Explain VictoriaMetrics next to Prometheus", "theme": "logging", "difficulty": "middle", "type": "theory", "tags": ["logging", "monitoring", "prometheus", "cost-optimization", "observability"], "path": "questions/logging/victoriametrics-vs-prometheus.html"},
  {"title": "Prevent multi-writer block-storage corruption", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "reliability", "filesystem"], "path": "questions/network-storage/block-storage-single-writer.html"},
  {"title": "Protect Ceph recovery capacity", "theme": "network-storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "reliability", "performance", "capacity-planning", "monitoring"], "path": "questions/network-storage/ceph-recovery-capacity.html"},
  {"title": "Choose Ceph replication or erasure coding", "theme": "network-storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "networking", "reliability", "performance", "capacity-planning"], "path": "questions/network-storage/ceph-replication-vs-erasure-coding.html"},
  {"title": "Design cross-region storage resilience", "theme": "network-storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "networking", "reliability", "security", "capacity-planning"], "path": "questions/network-storage/cross-region-storage-resilience.html"},
  {"title": "Explain iSCSI initiators and targets", "theme": "network-storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "networking", "security", "filesystem"], "path": "questions/network-storage/iscsi-initiator-target.html"},
  {"title": "Validate iSCSI multipathing", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "reliability", "performance"], "path": "questions/network-storage/iscsi-multipathing.html"},
  {"title": "Choose NAS, SAN, or object storage for a workload", "theme": "network-storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "networking", "performance"], "path": "questions/network-storage/nas-san-object-storage.html"},
  {"title": "Explain NFS cache coherency", "theme": "network-storage", "difficulty": "middle", "type": "theory", "tags": ["storage", "networking", "performance", "filesystem"], "path": "questions/network-storage/nfs-caching-coherency.html"},
  {"title": "Choose NFS failure behavior", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "reliability", "performance"], "path": "questions/network-storage/nfs-hard-soft-mounts.html"},
  {"title": "Diagnose NFS ownership and identity mapping", "theme": "network-storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["storage", "networking", "security", "filesystem"], "path": "questions/network-storage/nfs-identity-mapping.html"},
  {"title": "Plan NFS lock recovery", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "reliability", "filesystem"], "path": "questions/network-storage/nfs-lock-recovery.html"},
  {"title": "Mount an NFS export safely", "theme": "network-storage", "difficulty": "junior", "type": "scenario", "tags": ["storage", "networking", "filesystem", "security"], "path": "questions/network-storage/nfs-mount-basics.html"},
  {"title": "Select an NFS protocol version", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "security", "performance"], "path": "questions/network-storage/nfs-version-selection.html"},
  {"title": "Design an NVMe over Fabrics deployment", "theme": "network-storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "networking", "performance", "reliability", "security"], "path": "questions/network-storage/nvmeof-fabrics-design.html"},
  {"title": "Design object lifecycle and retention rules", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "security", "reliability", "cost-optimization"], "path": "questions/network-storage/object-lifecycle-retention.html"},
  {"title": "Design for object-storage consistency and retries", "theme": "network-storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "networking", "reliability", "performance"], "path": "questions/network-storage/object-storage-consistency.html"},
  {"title": "Build ransomware-resilient storage backups", "theme": "network-storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "security", "reliability", "monitoring", "governance"], "path": "questions/network-storage/ransomware-resilient-backups.html"},
  {"title": "Explain an SMB file share", "theme": "network-storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "networking", "filesystem", "security"], "path": "questions/network-storage/smb-share-basics.html"},
  {"title": "Apply SMB signing and encryption", "theme": "network-storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "security", "performance"], "path": "questions/network-storage/smb-signing-encryption.html"},
  {"title": "Distinguish snapshots from backups", "theme": "network-storage", "difficulty": "middle", "type": "theory", "tags": ["storage", "reliability", "security", "performance"], "path": "questions/network-storage/snapshots-versus-backups.html"},
  {"title": "Govern storage cost and capacity across teams", "theme": "network-storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "capacity-planning", "cost-optimization", "governance", "monitoring"], "path": "questions/network-storage/storage-cost-and-capacity-governance.html"},
  {"title": "Run a storage disaster-recovery exercise", "theme": "network-storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "reliability", "security", "monitoring", "governance"], "path": "questions/network-storage/storage-disaster-recovery-exercise.html"},
  {"title": "Investigate network-storage latency", "theme": "network-storage", "difficulty": "senior", "type": "troubleshooting", "tags": ["storage", "networking", "performance", "monitoring", "troubleshooting"], "path": "questions/network-storage/storage-performance-investigation.html"},
  {"title": "Define storage platform service tiers", "theme": "network-storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "reliability", "performance", "capacity-planning", "governance"], "path": "questions/network-storage/storage-platform-service-tiers.html"},
  {"title": "Establish storage tenancy boundaries", "theme": "network-storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "security", "iam", "governance", "networking"], "path": "questions/network-storage/storage-security-tenancy.html"},
  {"title": "Debug an authoritative DNS delegation", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["dns", "networking", "troubleshooting"], "path": "questions/networking/authoritative-dns-delegation.html"},
  {"title": "Respond to a BGP route leak risk", "theme": "networking", "difficulty": "senior", "type": "scenario", "tags": ["networking", "security", "incident-response", "reliability"], "path": "questions/networking/bgp-route-leak-response.html"},
  {"title": "Calculate an IPv4 CIDR range", "theme": "networking", "difficulty": "junior", "type": "theory", "tags": ["networking", "troubleshooting"], "path": "questions/networking/cidr-address-calculation.html"},
  {"title": "Lead a DNS incident response", "theme": "networking", "difficulty": "senior", "type": "scenario", "tags": ["dns", "networking", "incident-response", "reliability"], "path": "questions/networking/dns-incident-response.html"},
  {"title": "Select DNS record types and TTLs", "theme": "networking", "difficulty": "middle", "type": "scenario", "tags": ["dns", "networking", "reliability"], "path": "questions/networking/dns-record-types-and-ttl.html"},
  {"title": "Trace a DNS lookup from an application to an answer", "theme": "networking", "difficulty": "middle", "type": "theory", "tags": ["dns", "networking", "troubleshooting"], "path": "questions/networking/dns-resolution-path.html"},
  {"title": "Plan a dual-stack migration", "theme": "networking", "difficulty": "senior", "type": "scenario", "tags": ["networking", "dns", "deployment", "reliability"], "path": "questions/networking/dual-stack-migration-plan.html"},
  {"title": "Govern production network egress", "theme": "networking", "difficulty": "staff", "type": "scenario", "tags": ["networking", "security", "observability", "least-privilege"], "path": "questions/networking/egress-governance.html"},
  {"title": "Operate a dual-stack service", "theme": "networking", "difficulty": "middle", "type": "scenario", "tags": ["networking", "dns", "troubleshooting"], "path": "questions/networking/ipv6-dual-stack-basics.html"},
  {"title": "Design load-balancer health checks", "theme": "networking", "difficulty": "senior", "type": "scenario", "tags": ["networking", "http", "reliability", "availability"], "path": "questions/networking/load-balancer-health-check-design.html"},
  {"title": "Design multi-region connectivity boundaries", "theme": "networking", "difficulty": "staff", "type": "scenario", "tags": ["networking", "cloud", "reliability", "security"], "path": "questions/networking/multi-region-connectivity-architecture.html"},
  {"title": "Troubleshoot NAT connection failures", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["networking", "tcp", "troubleshooting"], "path": "questions/networking/nat-connection-troubleshooting.html"},
  {"title": "Create a network capacity model", "theme": "networking", "difficulty": "staff", "type": "scenario", "tags": ["networking", "monitoring", "reliability", "capacity-planning"], "path": "questions/networking/network-capacity-model.html"},
  {"title": "Build safe network change delivery", "theme": "networking", "difficulty": "staff", "type": "scenario", "tags": ["networking", "deployment", "automation", "reliability"], "path": "questions/networking/network-change-management.html"},
  {"title": "Set a network reliability strategy", "theme": "networking", "difficulty": "staff", "type": "scenario", "tags": ["networking", "reliability", "availability", "monitoring"], "path": "questions/networking/network-reliability-strategy.html"},
  {"title": "Design network segmentation for a service", "theme": "networking", "difficulty": "senior", "type": "scenario", "tags": ["networking", "security", "least-privilege", "reliability"], "path": "questions/networking/network-segmentation-design.html"},
  {"title": "Map a request to network layers", "theme": "networking", "difficulty": "junior", "type": "theory", "tags": ["networking", "tcp", "troubleshooting"], "path": "questions/networking/osi-and-tcp-ip-layers.html"},
  {"title": "Diagnose a path MTU discovery black hole", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["networking", "tcp", "troubleshooting"], "path": "questions/networking/path-mtu-discovery.html"},
  {"title": "Explain ports and sockets", "theme": "networking", "difficulty": "junior", "type": "theory", "tags": ["networking", "tcp", "troubleshooting"], "path": "questions/networking/ports-and-sockets.html"},
  {"title": "Use private IPv4 address space safely", "theme": "networking", "difficulty": "junior", "type": "scenario", "tags": ["networking", "security", "troubleshooting"], "path": "questions/networking/private-address-space.html"},
  {"title": "Diagnose route selection and asymmetric paths", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["networking", "troubleshooting", "reliability"], "path": "questions/networking/route-selection-and-asymmetry.html"},
  {"title": "Interpret TCP retransmissions and timeouts", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["tcp", "networking", "monitoring", "troubleshooting"], "path": "questions/networking/tcp-retransmission-and-timeouts.html"},
  {"title": "Diagnose a failed TCP three-way handshake", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["tcp", "networking", "troubleshooting"], "path": "questions/networking/tcp-three-way-handshake.html"},
  {"title": "Choose between TCP and UDP", "theme": "networking", "difficulty": "junior", "type": "theory", "tags": ["tcp", "networking", "reliability"], "path": "questions/networking/tcp-versus-udp.html"},
  {"title": "Debug a TLS handshake failure", "theme": "networking", "difficulty": "middle", "type": "troubleshooting", "tags": ["tls", "http", "networking", "troubleshooting"], "path": "questions/networking/tls-handshake-failure.html"},
  {"title": "Manage a large host fleet with Zabbix templates", "theme": "observability", "difficulty": "junior", "type": "scenario", "tags": ["observability", "monitoring", "zabbix", "automation", "configuration-management"], "path": "questions/observability/apply-zabbix-templates-at-scale.html"},
  {"title": "Build an actionable production alert", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "incident-response", "reliability", "prometheus", "pca"], "path": "questions/observability/build-an-actionable-alert.html"},
  {"title": "Choose useful application log levels", "theme": "observability", "difficulty": "junior", "type": "scenario", "tags": ["observability", "logging", "troubleshooting", "security", "pca"], "path": "questions/observability/choose-log-levels.html"},
  {"title": "Investigate a failed request with Cilium Hubble", "theme": "observability", "difficulty": "middle", "type": "troubleshooting", "tags": ["observability", "kubernetes", "networking", "troubleshooting", "debugging", "cca"], "path": "questions/observability/cilium-hubble-flow-observation.html"},
  {"title": "Combine black-box and white-box monitoring", "theme": "observability", "difficulty": "middle", "type": "theory", "tags": ["observability", "monitoring", "reliability", "troubleshooting", "prometheus", "pca"], "path": "questions/observability/compare-blackbox-whitebox.html"},
  {"title": "Choose between Zabbix and Prometheus", "theme": "observability", "difficulty": "middle", "type": "theory", "tags": ["observability", "monitoring", "zabbix", "prometheus", "architecture"], "path": "questions/observability/compare-zabbix-and-prometheus.html"},
  {"title": "Control metric-label cardinality", "theme": "observability", "difficulty": "middle", "type": "troubleshooting", "tags": ["observability", "monitoring", "prometheus", "troubleshooting", "pca", "otca"], "path": "questions/observability/control-metric-cardinality.html"},
  {"title": "Debug gaps in production telemetry", "theme": "observability", "difficulty": "senior", "type": "troubleshooting", "tags": ["observability", "monitoring", "debugging", "troubleshooting", "prometheus", "pca", "otca"], "path": "questions/observability/debug-telemetry-gaps.html"},
  {"title": "Decide when to deploy a Zabbix proxy", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "zabbix", "distributed-systems", "networking", "resilience"], "path": "questions/observability/decide-zabbix-proxy-placement.html"},
  {"title": "Define an SLI and SLO for an API", "theme": "observability", "difficulty": "junior", "type": "theory", "tags": ["observability", "monitoring", "reliability", "kcna", "prometheus", "pca"], "path": "questions/observability/define-an-sli-and-slo.html"},
  {"title": "Choose a counter, gauge, histogram, or summary", "theme": "observability", "difficulty": "junior", "type": "theory", "tags": ["observability", "monitoring", "prometheus", "reliability", "pca"], "path": "questions/observability/describe-metric-types.html"},
  {"title": "Design a useful service dashboard", "theme": "observability", "difficulty": "junior", "type": "scenario", "tags": ["observability", "monitoring", "reliability", "troubleshooting", "prometheus", "pca"], "path": "questions/observability/design-a-dashboard.html"},
  {"title": "Design an incident evidence strategy", "theme": "observability", "difficulty": "staff", "type": "scenario", "tags": ["observability", "incident-response", "governance", "security", "prometheus", "pca"], "path": "questions/observability/design-incident-evidence.html"},
  {"title": "Design multi-tenant observability boundaries", "theme": "observability", "difficulty": "staff", "type": "scenario", "tags": ["observability", "security", "governance", "platform-engineering", "prometheus", "pca"], "path": "questions/observability/design-multitenant-observability.html"},
  {"title": "Design trace sampling without losing incidents", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "troubleshooting", "cost-optimization", "pca", "otca"], "path": "questions/observability/design-telemetry-sampling.html"},
  {"title": "Diagnose Zabbix trigger false positives", "theme": "observability", "difficulty": "senior", "type": "troubleshooting", "tags": ["observability", "monitoring", "zabbix", "incident-response", "slo"], "path": "questions/observability/diagnose-zabbix-trigger-false-positives.html"},
  {"title": "Establish an observability platform product", "theme": "observability", "difficulty": "staff", "type": "scenario", "tags": ["observability", "platform-engineering", "governance", "reliability", "prometheus", "pca", "cnpe", "cnpa", "otca"], "path": "questions/observability/establish-observability-platform.html"},
  {"title": "Explain a metrics time series and its labels", "theme": "observability", "difficulty": "junior", "type": "theory", "tags": ["observability", "monitoring", "prometheus", "pca"], "path": "questions/observability/explain-time-series-labels.html"},
  {"title": "Explain Zabbix items, triggers, and actions", "theme": "observability", "difficulty": "junior", "type": "theory", "tags": ["observability", "monitoring", "zabbix", "healthchecks"], "path": "questions/observability/explain-zabbix-items-triggers-actions.html"},
  {"title": "Govern an organization-wide SLO program", "theme": "observability", "difficulty": "staff", "type": "scenario", "tags": ["observability", "monitoring", "governance", "reliability", "prometheus", "pca"], "path": "questions/observability/govern-an-slo-program.html"},
  {"title": "Govern telemetry cost across teams", "theme": "observability", "difficulty": "staff", "type": "scenario", "tags": ["observability", "governance", "cost-optimization", "platform-engineering", "prometheus", "pca", "cnpe", "cnpa"], "path": "questions/observability/govern-telemetry-cost.html"},
  {"title": "Instrument a distributed trace for an API request", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "debugging", "troubleshooting", "pca", "otca"], "path": "questions/observability/instrument-a-trace.html"},
  {"title": "Reduce alert fatigue without hiding risk", "theme": "observability", "difficulty": "senior", "type": "scenario", "tags": ["observability", "monitoring", "incident-response", "reliability", "prometheus", "pca"], "path": "questions/observability/investigate-alert-fatigue.html"},
  {"title": "Measure and improve tail latency", "theme": "observability", "difficulty": "senior", "type": "troubleshooting", "tags": ["observability", "monitoring", "reliability", "troubleshooting", "prometheus", "pca"], "path": "questions/observability/measure-tail-latency.html"},
  {"title": "Operate a reliable telemetry collection pipeline", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "logging", "reliability", "prometheus", "pca", "otca"], "path": "questions/observability/operate-a-telemetry-pipeline.html"},
  {"title": "Diagnose missing trace context across services", "theme": "observability", "difficulty": "middle", "type": "troubleshooting", "tags": ["observability", "debugging", "troubleshooting", "security", "pca", "otca"], "path": "questions/observability/propagate-trace-context.html"},
  {"title": "Set telemetry retention and query-cost controls", "theme": "observability", "difficulty": "senior", "type": "scenario", "tags": ["observability", "monitoring", "logging", "cost-optimization", "prometheus", "pca"], "path": "questions/observability/set-observability-retention.html"},
  {"title": "Explain an SLO error-budget burn-rate alert", "theme": "observability", "difficulty": "senior", "type": "theory", "tags": ["observability", "monitoring", "reliability", "incident-response", "prometheus", "pca"], "path": "questions/observability/slo-burn-rate.html"},
  {"title": "Compare metrics, logs, and traces during an incident", "theme": "observability", "difficulty": "middle", "type": "theory", "tags": ["observability", "monitoring", "debugging", "incident-response", "kcna", "prometheus", "pca", "otca", "must-know"], "path": "questions/observability/three-observability-signals.html"},
  {"title": "Use recording rules for expensive PromQL", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "prometheus", "reliability", "pca"], "path": "questions/observability/use-recording-rules.html"},
  {"title": "Monitor discovered entities with Zabbix low-level discovery", "theme": "observability", "difficulty": "middle", "type": "scenario", "tags": ["observability", "monitoring", "zabbix", "automation"], "path": "questions/observability/use-zabbix-low-level-discovery.html"},
  {"title": "Validate telemetry data quality after a release", "theme": "observability", "difficulty": "middle", "type": "troubleshooting", "tags": ["observability", "monitoring", "deployment", "troubleshooting", "prometheus", "pca", "otca"], "path": "questions/observability/validate-telemetry-data-quality.html"},
  {"title": "Why can high-cardinality metrics become a performance incident?", "theme": "performance-engineering", "difficulty": "middle", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/avoid-metric-cardinality.html"},
  {"title": "What must stay controlled when you compare two performance runs?", "theme": "performance-engineering", "difficulty": "junior", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/benchmark-control-variables.html"},
  {"title": "How do you run performance experiments without endangering production?", "theme": "performance-engineering", "difficulty": "senior", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/benchmark-production-safety.html"},
  {"title": "How do you evaluate whether a cache improves a service?", "theme": "performance-engineering", "difficulty": "middle", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/cache-performance-evaluation.html"},
  {"title": "How would you establish a capacity baseline for a service?", "theme": "performance-engineering", "difficulty": "middle", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/capacity-baseline-design.html"},
  {"title": "How should capacity economics influence performance governance?", "theme": "performance-engineering", "difficulty": "staff", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/capacity-economics-governance.html"},
  {"title": "How should an engineer choose latency histogram buckets?", "theme": "performance-engineering", "difficulty": "middle", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/choose-histogram-buckets.html"},
  {"title": "How do you size a client connection pool safely?", "theme": "performance-engineering", "difficulty": "middle", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/connection-pool-sizing.html"},
  {"title": "What cross-team contracts prevent performance regressions in a platform?", "theme": "performance-engineering", "difficulty": "staff", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/cross-team-performance-contracts.html"},
  {"title": "How do you investigate a database query performance regression?", "theme": "performance-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/database-query-regression.html"},
  {"title": "What makes a performance objective actionable?", "theme": "performance-engineering", "difficulty": "junior", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/define-performance-objectives.html"},
  {"title": "What evidence distinguishes a bottleneck from a busy component?", "theme": "performance-engineering", "difficulty": "junior", "type": "troubleshooting", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/identify-bottleneck-signals.html"},
  {"title": "When and how should a service shed load?", "theme": "performance-engineering", "difficulty": "senior", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/load-shedding-design.html"},
  {"title": "Why use latency percentiles instead of an average?", "theme": "performance-engineering", "difficulty": "junior", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/measure-latency-percentiles.html"},
  {"title": "How do you diagnose and mitigate noisy-neighbor performance?", "theme": "performance-engineering", "difficulty": "senior", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/multi-tenant-noisy-neighbor.html"},
  {"title": "How do performance budgets change API and dependency design?", "theme": "performance-engineering", "difficulty": "senior", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/performance-budget-api.html"},
  {"title": "How would a staff engineer prioritize a portfolio of performance work?", "theme": "performance-engineering", "difficulty": "staff", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/performance-investment-portfolio.html"},
  {"title": "How do you design a performance observability strategy across many services?", "theme": "performance-engineering", "difficulty": "staff", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/performance-observability-strategy.html"},
  {"title": "What should a performance regression check in CI actually prove?", "theme": "performance-engineering", "difficulty": "middle", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/performance-regression-ci.html"},
  {"title": "How do you investigate a CPU hotspot without optimizing the wrong code?", "theme": "performance-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/profile-cpu-hotspots.html"},
  {"title": "How should a staff engineer evaluate resilience versus performance trade-offs?", "theme": "performance-engineering", "difficulty": "staff", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/resilience-performance-tradeoffs.html"},
  {"title": "How do you select a load model for a production-facing service?", "theme": "performance-engineering", "difficulty": "middle", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/select-load-test-model.html"},
  {"title": "How do you triage a p99 latency regression?", "theme": "performance-engineering", "difficulty": "senior", "type": "troubleshooting", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/tail-latency-triage.html"},
  {"title": "How are throughput, concurrency, and latency related during a load test?", "theme": "performance-engineering", "difficulty": "junior", "type": "theory", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/throughput-and-concurrency.html"},
  {"title": "How do you find the critical path of a slow distributed request?", "theme": "performance-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/performance-engineering/trace-critical-path.html"},
  {"title": "Choose a guardrail over a gate", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "guardrails", "policy-as-code", "governance"], "path": "questions/platform-engineering/choose-a-guardrail-over-a-gate.html"},
  {"title": "Choose between mandated and voluntary adoption", "theme": "platform-engineering", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "adoption", "governance", "leadership"], "path": "questions/platform-engineering/choose-between-mandated-and-voluntary-adoption.html"},
  {"title": "Consolidate two competing internal platforms", "theme": "platform-engineering", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "migration", "governance", "internal-developer-platform"], "path": "questions/platform-engineering/consolidate-two-competing-internal-platforms.html"},
  {"title": "Contain a noisy neighbour on a shared platform", "theme": "platform-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["platform-engineering", "multi-tenancy", "resource-limits", "kubernetes"], "path": "questions/platform-engineering/contain-a-noisy-neighbour-on-a-shared-platform.html"},
  {"title": "Decide build versus buy for a capability", "theme": "platform-engineering", "difficulty": "senior", "type": "scenario", "tags": ["platform-engineering", "build-vs-buy", "cost-optimization", "architecture"], "path": "questions/platform-engineering/decide-build-versus-buy-for-a-capability.html"},
  {"title": "Define an internal developer platform", "theme": "platform-engineering", "difficulty": "junior", "type": "theory", "tags": ["platform-engineering", "internal-developer-platform", "architecture", "self-service"], "path": "questions/platform-engineering/define-an-internal-developer-platform.html"},
  {"title": "Design an escape hatch from the paved road", "theme": "platform-engineering", "difficulty": "senior", "type": "scenario", "tags": ["platform-engineering", "golden-path", "crossplane", "self-service"], "path": "questions/platform-engineering/design-an-escape-hatch-from-the-paved-road.html"},
  {"title": "Explain a paved road and a golden path", "theme": "platform-engineering", "difficulty": "junior", "type": "theory", "tags": ["platform-engineering", "golden-path", "guardrails", "delivery"], "path": "questions/platform-engineering/explain-a-paved-road-and-a-golden-path.html"},
  {"title": "Justify continued platform investment", "theme": "platform-engineering", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "cost-optimization", "leadership", "product-management"], "path": "questions/platform-engineering/justify-continued-platform-investment.html"},
  {"title": "Make platform documentation discoverable", "theme": "platform-engineering", "difficulty": "junior", "type": "theory", "tags": ["platform-engineering", "documentation", "backstage", "developer-experience"], "path": "questions/platform-engineering/make-platform-documentation-discoverable.html"},
  {"title": "Measure developer experience", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "developer-experience", "product-management", "quality"], "path": "questions/platform-engineering/measure-developer-experience.html"},
  {"title": "Measure platform adoption", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "adoption", "product-management", "internal-developer-platform"], "path": "questions/platform-engineering/measure-platform-adoption.html"},
  {"title": "Offer self-service with safe defaults", "theme": "platform-engineering", "difficulty": "junior", "type": "theory", "tags": ["platform-engineering", "self-service", "guardrails", "kubernetes"], "path": "questions/platform-engineering/offer-self-service-with-safe-defaults.html"},
  {"title": "Onboard a team onto the platform", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "onboarding", "adoption", "developer-experience"], "path": "questions/platform-engineering/onboard-a-team-onto-the-platform.html"},
  {"title": "Plan a migration onto the paved road", "theme": "platform-engineering", "difficulty": "senior", "type": "scenario", "tags": ["platform-engineering", "migration", "golden-path", "adoption"], "path": "questions/platform-engineering/plan-a-migration-onto-the-paved-road.html"},
  {"title": "Publish platform SLOs and a support model", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "slo", "reliability", "internal-developer-platform"], "path": "questions/platform-engineering/publish-platform-slos-and-a-support-model.html"},
  {"title": "Recognise when a platform team is the wrong answer", "theme": "platform-engineering", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "leadership", "team-topologies", "architecture"], "path": "questions/platform-engineering/recognise-when-a-platform-team-is-the-wrong-answer.html"},
  {"title": "Reduce cognitive load with team topologies", "theme": "platform-engineering", "difficulty": "senior", "type": "scenario", "tags": ["platform-engineering", "cognitive-load", "team-topologies", "leadership"], "path": "questions/platform-engineering/reduce-cognitive-load-with-team-topologies.html"},
  {"title": "Retire a platform capability", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "deprecation", "migration", "adoption"], "path": "questions/platform-engineering/retire-a-platform-capability.html"},
  {"title": "Roll out a change across every tenant", "theme": "platform-engineering", "difficulty": "senior", "type": "scenario", "tags": ["platform-engineering", "blast-radius", "change-management", "multi-tenancy"], "path": "questions/platform-engineering/roll-out-a-change-across-every-tenant.html"},
  {"title": "Run a platform-wide incident", "theme": "platform-engineering", "difficulty": "middle", "type": "troubleshooting", "tags": ["platform-engineering", "incident-response", "blast-radius", "multi-tenancy"], "path": "questions/platform-engineering/run-a-platform-wide-incident.html"},
  {"title": "Scope what the platform owns", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "internal-developer-platform", "architecture", "governance"], "path": "questions/platform-engineering/scope-what-the-platform-owns.html"},
  {"title": "Size and staff a platform team", "theme": "platform-engineering", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "leadership", "capacity-planning", "cost-optimization"], "path": "questions/platform-engineering/size-and-staff-a-platform-team.html"},
  {"title": "Treat the platform as a product", "theme": "platform-engineering", "difficulty": "junior", "type": "theory", "tags": ["platform-engineering", "product-management", "adoption", "developer-experience"], "path": "questions/platform-engineering/treat-the-platform-as-a-product.html"},
  {"title": "Version a platform interface", "theme": "platform-engineering", "difficulty": "middle", "type": "scenario", "tags": ["platform-engineering", "api-versioning", "internal-developer-platform", "change-management"], "path": "questions/platform-engineering/version-a-platform-interface.html"},
  {"title": "Secure environment handling at exec boundaries", "theme": "processes", "difficulty": "middle", "type": "scenario", "tags": ["linux", "processes", "security", "least-privilege"], "path": "questions/processes/environment-and-exec-security.html"},
  {"title": "Control file descriptor inheritance across exec", "theme": "processes", "difficulty": "middle", "type": "theory", "tags": ["linux", "processes", "file-descriptors", "security"], "path": "questions/processes/file-descriptor-inheritance.html"},
  {"title": "Explain the fork exec wait lifecycle", "theme": "processes", "difficulty": "middle", "type": "theory", "tags": ["linux", "processes", "debugging", "systemd"], "path": "questions/processes/fork-exec-wait-lifecycle.html"},
  {"title": "Design a graceful shutdown contract", "theme": "processes", "difficulty": "senior", "type": "scenario", "tags": ["linux", "processes", "signals", "reliability", "deployment"], "path": "questions/processes/graceful-shutdown-contract.html"},
  {"title": "Triage a hung process without destroying evidence", "theme": "processes", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "processes", "debugging", "incident-response", "logs"], "path": "questions/processes/hung-process-triage.html"},
  {"title": "Correlate process failures with the journal", "theme": "processes", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "processes", "journald", "logs", "debugging"], "path": "questions/processes/journald-process-diagnostics.html"},
  {"title": "Use nice values without promising performance", "theme": "processes", "difficulty": "middle", "type": "theory", "tags": ["linux", "processes", "cpu", "performance", "limits"], "path": "questions/processes/nice-and-scheduling.html"},
  {"title": "Recover safely after an OOM-killed process", "theme": "processes", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "processes", "memory", "oom", "reliability", "recovery"], "path": "questions/processes/oom-kill-process-recovery.html"},
  {"title": "Explain PIDs and parent processes", "theme": "processes", "difficulty": "junior", "type": "theory", "tags": ["linux", "processes", "pid1", "debugging"], "path": "questions/processes/pid-and-parent-process.html"},
  {"title": "Govern fleet process capacity and limits", "theme": "processes", "difficulty": "staff", "type": "scenario", "tags": ["linux", "processes", "capacity-planning", "limits", "performance", "governance"], "path": "questions/processes/process-capacity-governance.html"},
  {"title": "Avoid PID-reuse errors in automation", "theme": "processes", "difficulty": "senior", "type": "scenario", "tags": ["linux", "processes", "automation", "security", "debugging"], "path": "questions/processes/process-identity-and-pid-reuse.html"},
  {"title": "Govern process isolation and privilege policy", "theme": "processes", "difficulty": "staff", "type": "scenario", "tags": ["linux", "processes", "security", "least-privilege", "namespaces", "capabilities"], "path": "questions/processes/process-isolation-policy.html"},
  {"title": "Establish a platform-wide process lifecycle contract", "theme": "processes", "difficulty": "staff", "type": "scenario", "tags": ["linux", "processes", "platform-engineering", "reliability", "governance"], "path": "questions/processes/process-lifecycle-platform.html"},
  {"title": "Investigate a process memory-growth incident", "theme": "processes", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "processes", "memory", "oom", "performance", "incident-response"], "path": "questions/processes/process-memory-incident.html"},
  {"title": "Define process observability without exposing secrets", "theme": "processes", "difficulty": "staff", "type": "scenario", "tags": ["linux", "processes", "observability", "monitoring", "security"], "path": "questions/processes/process-observability-standard.html"},
  {"title": "Design guardrails for automated process remediation", "theme": "processes", "difficulty": "staff", "type": "scenario", "tags": ["linux", "processes", "automation", "incident-response", "reliability"], "path": "questions/processes/process-remediation-guardrails.html"},
  {"title": "Interpret process state and load average", "theme": "processes", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "processes", "load", "performance", "debugging"], "path": "questions/processes/process-state-and-load.html"},
  {"title": "Design supervision for a multi-process application", "theme": "processes", "difficulty": "senior", "type": "scenario", "tags": ["linux", "processes", "systemd", "pid1", "reliability", "must-know"], "path": "questions/processes/process-tree-supervision.html"},
  {"title": "Distinguish a program from a process", "theme": "processes", "difficulty": "junior", "type": "theory", "tags": ["linux", "processes", "pid1", "debugging"], "path": "questions/processes/program-vs-process.html"},
  {"title": "Read a process status safely", "theme": "processes", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "processes", "debugging", "monitoring"], "path": "questions/processes/read-process-status.html"},
  {"title": "Diagnose a per-process resource limit", "theme": "processes", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "processes", "limits", "file-descriptors", "capacity-planning", "lfcs"], "path": "questions/processes/resource-limits.html"},
  {"title": "Choose a signal for a running process", "theme": "processes", "difficulty": "junior", "type": "theory", "tags": ["linux", "processes", "signals", "troubleshooting"], "path": "questions/processes/signal-basics.html"},
  {"title": "Reason about signal masks in a multithreaded service", "theme": "processes", "difficulty": "middle", "type": "theory", "tags": ["linux", "processes", "signals", "debugging"], "path": "questions/processes/signal-masks-and-threads.html"},
  {"title": "Model a service lifecycle with systemd", "theme": "processes", "difficulty": "middle", "type": "scenario", "tags": ["linux", "processes", "systemd", "reliability", "operations"], "path": "questions/processes/systemd-service-lifecycle.html"},
  {"title": "Explain and handle a zombie process", "theme": "processes", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "processes", "debugging", "pid1"], "path": "questions/processes/zombie-process-basics.html"},
  {"title": "Choose a libvirt CPU mode for a fleet", "theme": "qemu-kvm", "difficulty": "middle", "type": "scenario", "tags": ["libvirt", "cpu", "live-migration", "kvm"], "path": "questions/qemu-kvm/choose-a-libvirt-cpu-mode.html"},
  {"title": "Choose the storage architecture for a VM fleet", "theme": "qemu-kvm", "difficulty": "staff", "type": "scenario", "tags": ["libvirt", "storage", "snapshots", "architecture", "performance"], "path": "questions/qemu-kvm/choose-fleet-vm-storage.html"},
  {"title": "Choose internal or external disk snapshots", "theme": "qemu-kvm", "difficulty": "middle", "type": "scenario", "tags": ["snapshots", "qemu", "libvirt", "storage"], "path": "questions/qemu-kvm/choose-internal-or-external-snapshots.html"},
  {"title": "Choose raw or qcow2 for a disk image", "theme": "qemu-kvm", "difficulty": "junior", "type": "theory", "tags": ["qemu", "storage", "disk", "virtualization"], "path": "questions/qemu-kvm/choose-raw-or-qcow2.html"},
  {"title": "Convert and rebase disk images with qemu-img", "theme": "qemu-kvm", "difficulty": "middle", "type": "scenario", "tags": ["qemu", "storage", "migration", "automation"], "path": "questions/qemu-kvm/convert-and-rebase-with-qemu-img.html"},
  {"title": "Decide when nested virtualization is worth it", "theme": "qemu-kvm", "difficulty": "middle", "type": "scenario", "tags": ["kvm", "virtualization", "performance", "linux"], "path": "questions/qemu-kvm/decide-on-nested-virtualization.html"},
  {"title": "Design backups for running VMs", "theme": "qemu-kvm", "difficulty": "senior", "type": "scenario", "tags": ["snapshots", "storage", "libvirt", "qemu", "reliability"], "path": "questions/qemu-kvm/design-running-vm-backups.html"},
  {"title": "Diagnose a guest silently running under TCG", "theme": "qemu-kvm", "difficulty": "middle", "type": "troubleshooting", "tags": ["kvm", "qemu", "troubleshooting", "performance"], "path": "questions/qemu-kvm/diagnose-fallback-to-tcg.html"},
  {"title": "Find where virtualization steals your performance", "theme": "qemu-kvm", "difficulty": "senior", "type": "troubleshooting", "tags": ["kvm", "performance", "troubleshooting", "observability"], "path": "questions/qemu-kvm/find-virtualization-overhead.html"},
  {"title": "Govern QEMU upgrades across a fleet", "theme": "qemu-kvm", "difficulty": "staff", "type": "scenario", "tags": ["qemu", "change-management", "security", "governance", "automation"], "path": "questions/qemu-kvm/govern-qemu-upgrades.html"},
  {"title": "Harden a multi-tenant KVM host", "theme": "qemu-kvm", "difficulty": "staff", "type": "scenario", "tags": ["kvm", "security", "multi-tenancy", "selinux", "least-privilege"], "path": "questions/qemu-kvm/harden-a-multi-tenant-kvm-host.html"},
  {"title": "Design live migration for a fleet with mixed CPU generations", "theme": "qemu-kvm", "difficulty": "staff", "type": "scenario", "tags": ["live-migration", "capacity-planning", "kvm", "change-management"], "path": "questions/qemu-kvm/migrate-a-fleet-with-mixed-cpus.html"},
  {"title": "Model storage as libvirt pools and volumes", "theme": "qemu-kvm", "difficulty": "middle", "type": "theory", "tags": ["libvirt", "storage", "volumes", "linux"], "path": "questions/qemu-kvm/model-storage-as-pools-and-volumes.html"},
  {"title": "Operate memory ballooning under host pressure", "theme": "qemu-kvm", "difficulty": "middle", "type": "theory", "tags": ["kvm", "memory", "virtio", "monitoring"], "path": "questions/qemu-kvm/operate-memory-ballooning.html"},
  {"title": "Pick bridged or macvtap guest networking", "theme": "qemu-kvm", "difficulty": "middle", "type": "theory", "tags": ["libvirt", "networking", "kvm", "linux"], "path": "questions/qemu-kvm/pick-bridged-or-macvtap.html"},
  {"title": "Pin a latency-sensitive VM to NUMA and hugepages", "theme": "qemu-kvm", "difficulty": "senior", "type": "scenario", "tags": ["numa", "cpu", "memory", "kvm", "performance"], "path": "questions/qemu-kvm/pin-a-vm-to-numa-and-hugepages.html"},
  {"title": "Read a libvirt domain's states", "theme": "qemu-kvm", "difficulty": "junior", "type": "theory", "tags": ["libvirt", "kvm", "linux", "operations"], "path": "questions/qemu-kvm/read-libvirt-domain-states.html"},
  {"title": "Respect machine types when editing guests", "theme": "qemu-kvm", "difficulty": "middle", "type": "theory", "tags": ["qemu", "virtualization", "boot", "linux"], "path": "questions/qemu-kvm/respect-machine-types.html"},
  {"title": "Run a live migration you can trust", "theme": "qemu-kvm", "difficulty": "senior", "type": "scenario", "tags": ["live-migration", "kvm", "libvirt", "networking"], "path": "questions/qemu-kvm/run-a-live-migration-you-trust.html"},
  {"title": "Secure libvirt and QEMU access on a shared host", "theme": "qemu-kvm", "difficulty": "senior", "type": "scenario", "tags": ["libvirt", "security", "permissions", "selinux", "least-privilege"], "path": "questions/qemu-kvm/secure-libvirt-and-qemu-access.html"},
  {"title": "Set an honest overcommit policy for a VM fleet", "theme": "qemu-kvm", "difficulty": "staff", "type": "scenario", "tags": ["kvm", "memory", "cpu", "capacity-planning", "slo"], "path": "questions/qemu-kvm/set-an-honest-overcommit-policy.html"},
  {"title": "Split QEMU's job from KVM's job", "theme": "qemu-kvm", "difficulty": "junior", "type": "theory", "tags": ["qemu", "kvm", "libvirt", "virtualization"], "path": "questions/qemu-kvm/split-qemu-from-kvm.html"},
  {"title": "Use the QEMU monitor without desyncing libvirt", "theme": "qemu-kvm", "difficulty": "middle", "type": "theory", "tags": ["qemu", "libvirt", "debugging", "kernel"], "path": "questions/qemu-kvm/use-the-qemu-monitor-without-desync.html"},
  {"title": "What /dev/kvm exposes to QEMU", "theme": "qemu-kvm", "difficulty": "junior", "type": "theory", "tags": ["kvm", "qemu", "linux", "kernel"], "path": "questions/qemu-kvm/what-dev-kvm-exposes.html"},
  {"title": "Why virtio beats emulated devices", "theme": "qemu-kvm", "difficulty": "junior", "type": "theory", "tags": ["virtio", "qemu", "performance", "linux"], "path": "questions/qemu-kvm/why-virtio-beats-emulated-devices.html"},
  {"title": "Acknowledge RabbitMQ work safely", "theme": "queue-messaging", "difficulty": "junior", "type": "scenario", "tags": ["rabbitmq", "message-queues", "reliability", "troubleshooting"], "path": "questions/queue-messaging/acknowledge-rabbitmq-work-safely.html"},
  {"title": "Choose a messaging platform for an organization", "theme": "queue-messaging", "difficulty": "staff", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "platform-engineering", "governance", "must-know"], "path": "questions/queue-messaging/choose-a-messaging-platform.html"},
  {"title": "Choose a work queue or an event log", "theme": "queue-messaging", "difficulty": "junior", "type": "theory", "tags": ["message-queues", "kafka", "rabbitmq", "event-driven", "reliability"], "path": "questions/queue-messaging/choose-a-queue-or-log.html"},
  {"title": "Choose Kafka retention or log compaction", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["kafka", "message-queues", "storage", "reliability"], "path": "questions/queue-messaging/choose-kafka-retention-or-compaction.html"},
  {"title": "Choose a RabbitMQ queue type", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["rabbitmq", "message-queues", "reliability", "performance"], "path": "questions/queue-messaging/choose-rabbitmq-queue-type.html"},
  {"title": "Commit Kafka offsets after processing effects", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["kafka", "message-queues", "reliability", "databases"], "path": "questions/queue-messaging/commit-kafka-offsets-after-effects.html"},
  {"title": "Configure Kafka producer durability", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["kafka", "message-queues", "reliability", "performance"], "path": "questions/queue-messaging/configure-kafka-producer-durability.html"},
  {"title": "Define messaging platform SLOs", "theme": "queue-messaging", "difficulty": "staff", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "observability", "reliability", "governance"], "path": "questions/queue-messaging/define-messaging-slos.html"},
  {"title": "Design Kafka disaster recovery", "theme": "queue-messaging", "difficulty": "senior", "type": "scenario", "tags": ["kafka", "message-queues", "incident-response", "reliability", "availability"], "path": "questions/queue-messaging/design-kafka-disaster-recovery.html"},
  {"title": "Design a Kafka exactly-once processing flow", "theme": "queue-messaging", "difficulty": "senior", "type": "scenario", "tags": ["kafka", "message-queues", "event-driven", "reliability"], "path": "questions/queue-messaging/design-kafka-exactly-once-flow.html"},
  {"title": "Design multi-tenant messaging security", "theme": "queue-messaging", "difficulty": "staff", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "security", "least-privilege", "governance"], "path": "questions/queue-messaging/design-multi-tenant-messaging-security.html"},
  {"title": "Design RabbitMQ dead-letter handling", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["rabbitmq", "message-queues", "troubleshooting", "reliability"], "path": "questions/queue-messaging/design-rabbitmq-dead-lettering.html"},
  {"title": "Explain at-most-once, at-least-once, and exactly-once claims", "theme": "queue-messaging", "difficulty": "junior", "type": "theory", "tags": ["kafka", "rabbitmq", "message-queues", "reliability"], "path": "questions/queue-messaging/explain-delivery-semantics.html"},
  {"title": "Explain Kafka topics and partitions", "theme": "queue-messaging", "difficulty": "junior", "type": "theory", "tags": ["kafka", "message-queues", "event-driven", "performance"], "path": "questions/queue-messaging/explain-kafka-topics-and-partitions.html"},
  {"title": "Explain RabbitMQ exchanges, bindings, and queues", "theme": "queue-messaging", "difficulty": "junior", "type": "theory", "tags": ["rabbitmq", "message-queues", "event-driven", "reliability"], "path": "questions/queue-messaging/explain-rabbitmq-routing.html"},
  {"title": "Govern event contracts across teams", "theme": "queue-messaging", "difficulty": "staff", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "event-driven", "governance", "reliability"], "path": "questions/queue-messaging/govern-event-contracts.html"},
  {"title": "Govern messaging capacity and cost", "theme": "queue-messaging", "difficulty": "staff", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "capacity-planning", "cost-optimization", "governance"], "path": "questions/queue-messaging/govern-messaging-capacity-and-cost.html"},
  {"title": "Handle Kafka consumer rebalances safely", "theme": "queue-messaging", "difficulty": "middle", "type": "troubleshooting", "tags": ["kafka", "message-queues", "troubleshooting", "reliability"], "path": "questions/queue-messaging/handle-kafka-consumer-rebalances.html"},
  {"title": "Handle RabbitMQ poison messages", "theme": "queue-messaging", "difficulty": "middle", "type": "troubleshooting", "tags": ["rabbitmq", "message-queues", "troubleshooting", "reliability"], "path": "questions/queue-messaging/handle-rabbitmq-poison-messages.html"},
  {"title": "Manage event schema evolution", "theme": "queue-messaging", "difficulty": "senior", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "event-driven", "governance"], "path": "questions/queue-messaging/manage-event-schema-evolution.html"},
  {"title": "Plan Kafka partition capacity", "theme": "queue-messaging", "difficulty": "senior", "type": "scenario", "tags": ["kafka", "message-queues", "capacity-planning", "performance", "reliability"], "path": "questions/queue-messaging/plan-kafka-partition-capacity.html"},
  {"title": "Preserve required ordering in asynchronous processing", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["kafka", "rabbitmq", "message-queues", "event-driven", "reliability"], "path": "questions/queue-messaging/preserve-order-in-async-processing.html"},
  {"title": "Respond to a RabbitMQ cluster incident", "theme": "queue-messaging", "difficulty": "senior", "type": "troubleshooting", "tags": ["rabbitmq", "message-queues", "incident-response", "troubleshooting", "reliability"], "path": "questions/queue-messaging/respond-to-rabbitmq-cluster-incident.html"},
  {"title": "Triage Kafka consumer lag", "theme": "queue-messaging", "difficulty": "middle", "type": "troubleshooting", "tags": ["kafka", "message-queues", "monitoring", "troubleshooting"], "path": "questions/queue-messaging/triage-kafka-consumer-lag.html"},
  {"title": "Tune RabbitMQ consumer prefetch", "theme": "queue-messaging", "difficulty": "middle", "type": "scenario", "tags": ["rabbitmq", "message-queues", "performance", "reliability"], "path": "questions/queue-messaging/tune-rabbitmq-prefetch.html"},
  {"title": "Verify container image provenance before deployment", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["containers", "images", "security", "supply-chain", "cks", "kcsa", "cnpe", "must-know"], "path": "questions/security/container-image-provenance.html"},
  {"title": "Harden a container runtime workload", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "containers", "least-privilege", "linux", "cks", "kcsa"], "path": "questions/security/container-runtime-hardening.html"},
  {"title": "Manage vulnerable application dependencies", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "supply-chain", "automation", "ci-cd", "cks", "cba"], "path": "questions/security/dependency-vulnerability-management.html"},
  {"title": "Deliver secrets to a GitOps-reconciled cluster", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["security", "kubernetes", "ci-cd", "git", "least-privilege", "governance", "gitops", "cgoa"], "path": "questions/security/gitops-secret-delivery.html"},
  {"title": "Enforce Kubernetes Pod Security Standards", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "kubernetes", "containers", "least-privilege", "cks", "kcsa", "ckad"], "path": "questions/security/kubernetes-pod-security.html"},
  {"title": "Apply least privilege to a workload identity", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "iam", "least-privilege", "cloud"], "path": "questions/security/least-privilege-iam.html"},
  {"title": "Choose multi-factor authentication for privileged access", "theme": "security", "difficulty": "junior", "type": "theory", "tags": ["security", "iam", "least-privilege"], "path": "questions/security/multi-factor-authentication.html"},
  {"title": "Build organization-wide incident readiness", "theme": "security", "difficulty": "staff", "type": "scenario", "tags": ["security", "incident-response", "governance", "observability"], "path": "questions/security/organization-incident-readiness.html"},
  {"title": "Store application passwords safely", "theme": "security", "difficulty": "junior", "type": "theory", "tags": ["security", "least-privilege"], "path": "questions/security/password-storage.html"},
  {"title": "Explain risk-based patch management", "theme": "security", "difficulty": "junior", "type": "theory", "tags": ["security", "linux", "reliability", "automation"], "path": "questions/security/patch-management-basics.html"},
  {"title": "Design production network segmentation", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["security", "networking", "least-privilege", "reliability", "kcsa"], "path": "questions/security/production-segmentation.html"},
  {"title": "Design recoverable backups for ransomware", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["security", "storage", "incident-response", "reliability"], "path": "questions/security/ransomware-recovery-design.html"},
  {"title": "Respond to a leaked production secret", "theme": "security", "difficulty": "middle", "type": "troubleshooting", "tags": ["security", "incident-response", "logging", "least-privilege", "kcsa"], "path": "questions/security/secret-leak-response.html"},
  {"title": "Describe a secure secret-management lifecycle", "theme": "security", "difficulty": "middle", "type": "theory", "tags": ["security", "kubernetes", "least-privilege", "automation"], "path": "questions/security/secret-management-lifecycle.html"},
  {"title": "Secure shared CI runners", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "ci-cd", "least-privilege", "supply-chain"], "path": "questions/security/secure-ci-runners.html"},
  {"title": "Deliver secure platform defaults at scale", "theme": "security", "difficulty": "staff", "type": "scenario", "tags": ["security", "platform-engineering", "automation", "governance", "kcsa", "cnpa"], "path": "questions/security/secure-platform-defaults.html"},
  {"title": "Govern security-control exceptions", "theme": "security", "difficulty": "staff", "type": "scenario", "tags": ["security", "governance", "delivery", "reliability", "kcsa"], "path": "questions/security/security-exception-governance.html"},
  {"title": "Set web security headers deliberately", "theme": "security", "difficulty": "middle", "type": "scenario", "tags": ["security", "http", "web-server"], "path": "questions/security/security-headers.html"},
  {"title": "Triage a suspected security incident", "theme": "security", "difficulty": "middle", "type": "troubleshooting", "tags": ["security", "incident-response", "logging", "reliability", "cks", "kcsa"], "path": "questions/security/security-incident-triage.html"},
  {"title": "Design useful security event logging", "theme": "security", "difficulty": "junior", "type": "theory", "tags": ["security", "logging", "observability", "cks"], "path": "questions/security/security-logging-basics.html"},
  {"title": "Define security metrics that drive engineering decisions", "theme": "security", "difficulty": "staff", "type": "scenario", "tags": ["security", "governance", "monitoring", "platform-engineering"], "path": "questions/security/security-metrics-program.html"},
  {"title": "Establish a security platform risk model", "theme": "security", "difficulty": "staff", "type": "scenario", "tags": ["security", "governance", "platform-engineering", "reliability", "kcsa"], "path": "questions/security/security-platform-risk-model.html"},
  {"title": "Design software supply-chain controls", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["security", "supply-chain", "ci-cd", "governance", "cks", "kcsa"], "path": "questions/security/software-supply-chain-controls.html"},
  {"title": "Explain TLS certificate validation", "theme": "security", "difficulty": "junior", "type": "theory", "tags": ["security", "tls", "networking"], "path": "questions/security/tls-certificate-basics.html"},
  {"title": "Triage a production vulnerability report", "theme": "security", "difficulty": "middle", "type": "troubleshooting", "tags": ["security", "incident-response", "containers", "reliability"], "path": "questions/security/vulnerability-triage.html"},
  {"title": "Design zero-trust service access", "theme": "security", "difficulty": "senior", "type": "scenario", "tags": ["security", "iam", "networking", "least-privilege"], "path": "questions/security/zero-trust-service-access.html"},
  {"title": "Decide whether a function should attach to a private network", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "networking", "security", "reliability", "cost-optimization"], "path": "questions/serverless/attach-function-to-private-network.html"},
  {"title": "Choose a serverless trigger safely", "theme": "serverless", "difficulty": "junior", "type": "theory", "tags": ["cloud", "event-driven", "reliability", "architecture"], "path": "questions/serverless/choose-serverless-trigger.html"},
  {"title": "Decide between managed functions and long-running compute", "theme": "serverless", "difficulty": "staff", "type": "scenario", "tags": ["cloud", "architecture", "cost-optimization", "governance", "capacity-planning"], "path": "questions/serverless/choose-serverless-versus-long-running-compute.html"},
  {"title": "Control serverless cost without hiding demand", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "cost-optimization", "performance", "governance"], "path": "questions/serverless/control-serverless-cost.html"},
  {"title": "Deploy a serverless function safely", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "deployment", "reliability", "observability"], "path": "questions/serverless/deploy-serverless-safely.html"},
  {"title": "Design serverless function timeouts and deadlines", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "reliability", "performance", "observability"], "path": "questions/serverless/design-function-timeouts.html"},
  {"title": "Design idempotent serverless functions", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "event-driven", "reliability", "architecture"], "path": "questions/serverless/design-idempotent-functions.html"},
  {"title": "Design idempotent serverless event processing", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "event-driven", "reliability", "architecture"], "path": "questions/serverless/design-idempotent-serverless-events.html"},
  {"title": "Design multi-region resilience for a serverless application", "theme": "serverless", "difficulty": "staff", "type": "scenario", "tags": ["cloud", "availability", "reliability", "architecture", "incident-response"], "path": "questions/serverless/design-multi-region-serverless-resilience.html"},
  {"title": "Explain serverless payload, memory, and duration limits", "theme": "serverless", "difficulty": "junior", "type": "theory", "tags": ["cloud", "limits", "reliability", "performance"], "path": "questions/serverless/explain-function-payload-limits.html"},
  {"title": "Explain synchronous and asynchronous serverless invocation", "theme": "serverless", "difficulty": "junior", "type": "theory", "tags": ["cloud", "event-driven", "reliability", "message-queues"], "path": "questions/serverless/explain-invocation-delivery-semantics.html"},
  {"title": "Explain how serverless billing differs from always-on compute", "theme": "serverless", "difficulty": "junior", "type": "theory", "tags": ["cloud", "cost-optimization", "capacity", "architecture"], "path": "questions/serverless/explain-serverless-billing-model.html"},
  {"title": "Explain the serverless function execution model", "theme": "serverless", "difficulty": "junior", "type": "theory", "tags": ["cloud", "architecture", "event-driven", "performance"], "path": "questions/serverless/explain-serverless-execution-model.html"},
  {"title": "Govern a serverless platform across teams", "theme": "serverless", "difficulty": "staff", "type": "scenario", "tags": ["cloud", "governance", "platform-engineering", "security"], "path": "questions/serverless/govern-serverless-platform.html"},
  {"title": "Design for serverless function cold starts", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "performance", "observability", "architecture"], "path": "questions/serverless/handle-function-cold-starts.html"},
  {"title": "Handle serverless failures and poison events", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "event-driven", "reliability", "incident-response"], "path": "questions/serverless/handle-serverless-failures.html"},
  {"title": "Manage serverless function concurrency safely", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "performance", "reliability", "observability"], "path": "questions/serverless/manage-function-concurrency.html"},
  {"title": "Manage serverless configuration safely", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "configuration-management", "security", "deployment"], "path": "questions/serverless/manage-serverless-configuration.html"},
  {"title": "Manage database connections from serverless functions", "theme": "serverless", "difficulty": "middle", "type": "troubleshooting", "tags": ["cloud", "databases", "reliability", "performance", "postgresql"], "path": "questions/serverless/manage-serverless-database-connections.html"},
  {"title": "Observe a serverless workload in production", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "observability", "monitoring", "reliability"], "path": "questions/serverless/observe-serverless-production.html"},
  {"title": "Orchestrate a serverless workflow safely", "theme": "serverless", "difficulty": "senior", "type": "scenario", "tags": ["cloud", "event-driven", "architecture", "reliability"], "path": "questions/serverless/orchestrate-serverless-workflows.html"},
  {"title": "Plan for serverless runtime deprecations across an estate", "theme": "serverless", "difficulty": "staff", "type": "scenario", "tags": ["cloud", "governance", "change-management", "security", "dependencies"], "path": "questions/serverless/plan-function-runtime-deprecations.html"},
  {"title": "Reduce a serverless deployment package and its dependency weight", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "performance", "dependencies", "deployment", "supply-chain"], "path": "questions/serverless/reduce-function-package-size.html"},
  {"title": "Secure serverless function identity", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "iam", "security", "least-privilege"], "path": "questions/serverless/secure-function-identity.html"},
  {"title": "Standardize event contracts across a serverless estate", "theme": "serverless", "difficulty": "staff", "type": "scenario", "tags": ["cloud", "event-driven", "governance", "architecture", "change-management"], "path": "questions/serverless/standardize-serverless-event-contracts.html"},
  {"title": "Test serverless integrations without production surprises", "theme": "serverless", "difficulty": "middle", "type": "scenario", "tags": ["cloud", "testing-strategy", "reliability", "event-driven"], "path": "questions/serverless/test-serverless-integrations.html"},
  {"title": "Trace a request across ephemeral serverless components", "theme": "serverless", "difficulty": "middle", "type": "troubleshooting", "tags": ["cloud", "observability", "latency", "debugging", "event-driven"], "path": "questions/serverless/trace-ephemeral-function-requests.html"},
  {"title": "Route ingress traffic with Cilium Gateway API", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "kubernetes", "networking", "traffic-management", "security", "cca", "ckne"], "path": "questions/service-mesh/cilium-gateway-api-routing.html"},
  {"title": "Plan Cilium transparent workload encryption", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "kubernetes", "networking", "security", "mtls", "cca", "ckne"], "path": "questions/service-mesh/cilium-transparent-encryption.html"},
  {"title": "Route LLM inference traffic with Gateway API controls", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "kubernetes", "networking", "gateway-api", "traffic-management", "llm", "inference", "routing", "observability", "ckne"], "path": "questions/service-mesh/gateway-api-llm-inference-routing.html"},
  {"title": "Upgrade Istio with a bounded canary", "theme": "service-mesh", "difficulty": "staff", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "deployment", "reliability"], "path": "questions/service-mesh/istio-canary-upgrade.html"},
  {"title": "Triage an Istio configuration that is not taking effect", "theme": "service-mesh", "difficulty": "middle", "type": "troubleshooting", "tags": ["service-mesh", "istio", "kubernetes", "ica", "troubleshooting", "traffic-management"], "path": "questions/service-mesh/istio-configuration-triage.html"},
  {"title": "Distinguish Istio control-plane and data-plane failures", "theme": "service-mesh", "difficulty": "staff", "type": "troubleshooting", "tags": ["service-mesh", "istio", "kubernetes", "ica", "troubleshooting", "observability", "reliability"], "path": "questions/service-mesh/istio-control-plane-data-plane-triage.html"},
  {"title": "Apply traffic policies with a DestinationRule", "theme": "service-mesh", "difficulty": "middle", "type": "theory", "tags": ["service-mesh", "istio", "kubernetes", "ica", "traffic-management", "reliability"], "path": "questions/service-mesh/istio-destination-rule-policies.html"},
  {"title": "Secure edge traffic at an Istio gateway", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "tls", "security", "networking"], "path": "questions/service-mesh/istio-edge-tls.html"},
  {"title": "Connect a mesh workload to an external service", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "networking", "security"], "path": "questions/service-mesh/istio-external-service-entry.html"},
  {"title": "Use Istio fault injection safely", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "traffic-management", "troubleshooting", "reliability"], "path": "questions/service-mesh/istio-fault-injection.html"},
  {"title": "Configure Istio ingress and egress boundaries", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "networking", "security"], "path": "questions/service-mesh/istio-ingress-egress-gateways.html"},
  {"title": "Customize an Istio installation safely", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "configuration-management", "security"], "path": "questions/service-mesh/istio-install-customization.html"},
  {"title": "Select an Istio data-plane mode", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "security", "observability"], "path": "questions/service-mesh/istio-installation-mode-selection.html"},
  {"title": "Combine JWT authentication and authorization in Istio", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "jwt", "security", "least-privilege", "ckne"], "path": "questions/service-mesh/istio-jwt-authorization.html"},
  {"title": "Enforce Istio mutual TLS incrementally", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "mtls", "security", "reliability"], "path": "questions/service-mesh/istio-mutual-tls.html"},
  {"title": "Shift traffic progressively with Istio", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "traffic-management", "deployment", "reliability"], "path": "questions/service-mesh/istio-progressive-traffic-shift.html"},
  {"title": "Design an Istio resilience policy", "theme": "service-mesh", "difficulty": "senior", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "traffic-management", "reliability"], "path": "questions/service-mesh/istio-resilience-policy.html"},
  {"title": "Route mesh traffic with a VirtualService", "theme": "service-mesh", "difficulty": "middle", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "ica", "traffic-management", "reliability"], "path": "questions/service-mesh/istio-virtualservice-routing.html"},
  {"title": "Make a service-mesh adoption decision with measurable outcomes", "theme": "service-mesh", "difficulty": "staff", "type": "scenario", "tags": ["service-mesh", "platform-engineering", "kubernetes", "governance", "cost-optimization", "reliability"], "path": "questions/service-mesh/service-mesh-adoption-decision.html"},
  {"title": "Distinguish a mesh control plane from its data plane", "theme": "service-mesh", "difficulty": "junior", "type": "theory", "tags": ["service-mesh", "istio", "kubernetes", "networking", "observability", "troubleshooting"], "path": "questions/service-mesh/service-mesh-control-data-plane.html"},
  {"title": "Explain workload identity in a service mesh", "theme": "service-mesh", "difficulty": "junior", "type": "theory", "tags": ["service-mesh", "istio", "kubernetes", "security", "mtls", "least-privilege"], "path": "questions/service-mesh/service-mesh-identity.html"},
  {"title": "Design service-mesh boundaries across multiple clusters", "theme": "service-mesh", "difficulty": "staff", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "networking", "security", "reliability", "cloud"], "path": "questions/service-mesh/service-mesh-multicluster-boundaries.html"},
  {"title": "Use mesh telemetry without mistaking it for complete observability", "theme": "service-mesh", "difficulty": "junior", "type": "scenario", "tags": ["service-mesh", "istio", "observability", "monitoring", "logging", "reliability", "ckne"], "path": "questions/service-mesh/service-mesh-observability.html"},
  {"title": "Establish safe service-mesh platform guardrails", "theme": "service-mesh", "difficulty": "staff", "type": "scenario", "tags": ["service-mesh", "istio", "kubernetes", "platform-engineering", "security", "governance", "reliability", "cnpe", "cnpa"], "path": "questions/service-mesh/service-mesh-platform-guardrails.html"},
  {"title": "Explain what a service mesh does and does not replace", "theme": "service-mesh", "difficulty": "junior", "type": "theory", "tags": ["service-mesh", "istio", "kubernetes", "networking", "security", "observability"], "path": "questions/service-mesh/service-mesh-purpose.html"},
  {"title": "Verify sidecar enrollment before troubleshooting mesh policy", "theme": "service-mesh", "difficulty": "junior", "type": "troubleshooting", "tags": ["service-mesh", "istio", "kubernetes", "containers", "troubleshooting", "observability"], "path": "questions/service-mesh/service-mesh-sidecar-injection.html"},
  {"title": "Prevent command injection in an automation script", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "security", "least-privilege"], "path": "questions/shell-scripting/avoid-command-injection.html"},
  {"title": "Apply Bash strict mode with context", "theme": "shell-scripting", "difficulty": "middle", "type": "theory", "tags": ["bash", "shell", "scripting", "troubleshooting", "reliability"], "path": "questions/shell-scripting/choose-strict-mode.html"},
  {"title": "Control concurrent jobs in a Bash worker", "theme": "shell-scripting", "difficulty": "senior", "type": "scenario", "tags": ["bash", "shell", "scripting", "automation", "reliability"], "path": "questions/shell-scripting/control-concurrent-jobs.html"},
  {"title": "Debug a failing production script safely", "theme": "shell-scripting", "difficulty": "senior", "type": "troubleshooting", "tags": ["bash", "shell", "scripting", "debugging", "incident-response", "reliability"], "path": "questions/shell-scripting/debug-production-script-safely.html"},
  {"title": "Find shell-script defects before deployment", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "debugging", "ci-cd"], "path": "questions/shell-scripting/debug-with-shellcheck.html"},
  {"title": "Decide when to replace a shell script", "theme": "shell-scripting", "difficulty": "staff", "type": "scenario", "tags": ["bash", "shell", "scripting", "platform-engineering", "reliability", "governance"], "path": "questions/shell-scripting/decide-when-to-replace-shell.html"},
  {"title": "Define a safe shell-automation standard", "theme": "shell-scripting", "difficulty": "staff", "type": "scenario", "tags": ["bash", "shell", "scripting", "governance", "platform-engineering", "security"], "path": "questions/shell-scripting/define-shell-automation-standard.html"},
  {"title": "Design a fleet-remediation runbook", "theme": "shell-scripting", "difficulty": "staff", "type": "scenario", "tags": ["bash", "shell", "scripting", "incident-response", "reliability", "governance"], "path": "questions/shell-scripting/design-fleet-remediation-runbook.html"},
  {"title": "Execute a shell script with an explicit interpreter", "theme": "shell-scripting", "difficulty": "junior", "type": "theory", "tags": ["bash", "shell", "scripting", "automation"], "path": "questions/shell-scripting/execute-a-script-portably.html"},
  {"title": "Govern the shell-script supply chain", "theme": "shell-scripting", "difficulty": "staff", "type": "scenario", "tags": ["bash", "shell", "scripting", "security", "supply-chain", "governance"], "path": "questions/shell-scripting/govern-shell-script-supply-chain.html"},
  {"title": "Handle shell-script arguments without losing boundaries", "theme": "shell-scripting", "difficulty": "junior", "type": "theory", "tags": ["bash", "shell", "scripting", "automation"], "path": "questions/shell-scripting/handle-script-arguments.html"},
  {"title": "Handle termination signals and cleanup", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "signals", "reliability"], "path": "questions/shell-scripting/handle-signals-and-cleanup.html"},
  {"title": "Make a remediation script idempotent", "theme": "shell-scripting", "difficulty": "senior", "type": "scenario", "tags": ["bash", "shell", "scripting", "automation", "reliability"], "path": "questions/shell-scripting/implement-idempotent-remediation.html"},
  {"title": "Prevent overlapping scheduled script runs", "theme": "shell-scripting", "difficulty": "senior", "type": "scenario", "tags": ["bash", "shell", "scripting", "automation", "reliability"], "path": "questions/shell-scripting/lock-singleton-job.html"},
  {"title": "Make shell-script logs useful without leaking secrets", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "logging", "security", "troubleshooting"], "path": "questions/shell-scripting/log-without-secrets.html"},
  {"title": "Create and clean temporary files safely", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "security", "filesystem"], "path": "questions/shell-scripting/manage-temporary-files.html"},
  {"title": "Measure shell-automation reliability", "theme": "shell-scripting", "difficulty": "staff", "type": "scenario", "tags": ["bash", "shell", "scripting", "observability", "reliability", "governance"], "path": "questions/shell-scripting/measure-automation-reliability.html"},
  {"title": "Parse command-line options with getopts", "theme": "shell-scripting", "difficulty": "middle", "type": "scenario", "tags": ["bash", "shell", "scripting", "automation"], "path": "questions/shell-scripting/parse-options-with-getopts.html"},
  {"title": "Preserve the failed command in a pipeline", "theme": "shell-scripting", "difficulty": "middle", "type": "troubleshooting", "tags": ["bash", "shell", "scripting", "debugging", "reliability"], "path": "questions/shell-scripting/preserve-pipeline-failures.html"},
  {"title": "Read arbitrary input lines safely in Bash", "theme": "shell-scripting", "difficulty": "junior", "type": "scenario", "tags": ["bash", "shell", "scripting", "filesystem", "automation"], "path": "questions/shell-scripting/read-lines-safely.html"},
  {"title": "Explain shell quoting and variable expansion", "theme": "shell-scripting", "difficulty": "junior", "type": "theory", "tags": ["bash", "shell", "scripting", "troubleshooting"], "path": "questions/shell-scripting/shell-quoting-and-expansion.html"},
  {"title": "Test a shell script before production", "theme": "shell-scripting", "difficulty": "senior", "type": "scenario", "tags": ["bash", "shell", "scripting", "ci-cd", "troubleshooting"], "path": "questions/shell-scripting/test-shell-scripts.html"},
  {"title": "Use Bash arrays for command arguments", "theme": "shell-scripting", "difficulty": "middle", "type": "theory", "tags": ["bash", "shell", "scripting", "automation"], "path": "questions/shell-scripting/use-arrays-for-arguments.html"},
  {"title": "Use command substitution without hiding failures", "theme": "shell-scripting", "difficulty": "middle", "type": "troubleshooting", "tags": ["bash", "shell", "scripting", "debugging", "reliability"], "path": "questions/shell-scripting/use-command-substitution-deliberately.html"},
  {"title": "Use exit statuses as an automation contract", "theme": "shell-scripting", "difficulty": "junior", "type": "theory", "tags": ["bash", "shell", "scripting", "ci-cd", "troubleshooting"], "path": "questions/shell-scripting/use-exit-statuses.html"},
  {"title": "Assign incident-management roles", "theme": "sre", "difficulty": "middle", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/assign-incident-roles.html"},
  {"title": "Build a reliability investment roadmap", "theme": "sre", "difficulty": "staff", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/build-reliability-roadmap.html"},
  {"title": "Classify an alert as a page, ticket, or log", "theme": "sre", "difficulty": "junior", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/classify-alert-urgency.html"},
  {"title": "Coordinate a major incident across teams", "theme": "sre", "difficulty": "senior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/coordinate-major-incident.html"},
  {"title": "Define service reliability and the role of an SRE", "theme": "sre", "difficulty": "junior", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/define-service-reliability.html"},
  {"title": "Define an SRE engagement model", "theme": "sre", "difficulty": "staff", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/define-sre-engagement-model.html"},
  {"title": "Choose a user-journey SLI", "theme": "sre", "difficulty": "junior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/define-user-journey-sli.html"},
  {"title": "Design a multi-window burn-rate alert", "theme": "sre", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/design-multiwindow-burn-alert.html"},
  {"title": "Design an organizational incident-management program", "theme": "sre", "difficulty": "staff", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/design-organizational-incident-program.html"},
  {"title": "Design a reliable product launch", "theme": "sre", "difficulty": "senior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/design-reliable-launch.html"},
  {"title": "Establish an effective on-call handoff", "theme": "sre", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/establish-oncall-handoff.html"},
  {"title": "Establish service ownership and reliability accountability", "theme": "sre", "difficulty": "staff", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting", "cnpa", "cba"], "path": "questions/sre/establish-service-ownership.html"},
  {"title": "Explain an error budget", "theme": "sre", "difficulty": "junior", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/explain-error-budget.html"},
  {"title": "Govern an error-budget policy", "theme": "sre", "difficulty": "staff", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/govern-error-budget-policy.html"},
  {"title": "Manage critical state for reliability", "theme": "sre", "difficulty": "senior", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/manage-critical-state.html"},
  {"title": "Measure and reduce toil", "theme": "sre", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/measure-and-reduce-toil.html"},
  {"title": "Measure platform impact with DORA metrics without gaming teams", "theme": "sre", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "reliability", "monitoring", "ci-cd", "governance", "cnpa"], "path": "questions/sre/measure-platform-impact-with-dora.html"},
  {"title": "Monitor a distributed service", "theme": "sre", "difficulty": "middle", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/monitor-distributed-service.html"},
  {"title": "Plan service capacity", "theme": "sre", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/plan-service-capacity.html"},
  {"title": "Prevent cascading failures", "theme": "sre", "difficulty": "senior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/prevent-cascading-failures.html"},
  {"title": "Protect a service from overload", "theme": "sre", "difficulty": "middle", "type": "troubleshooting", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/protect-service-from-overload.html"},
  {"title": "Run a production-readiness review", "theme": "sre", "difficulty": "middle", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting", "cba"], "path": "questions/sre/run-production-readiness-review.html"},
  {"title": "Test a disaster-recovery plan", "theme": "sre", "difficulty": "senior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/test-disaster-recovery.html"},
  {"title": "Triage a production incident", "theme": "sre", "difficulty": "middle", "type": "troubleshooting", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting", "cnpe", "cnpa", "must-know"], "path": "questions/sre/triage-production-incident.html"},
  {"title": "Write an actionable runbook", "theme": "sre", "difficulty": "junior", "type": "scenario", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/write-actionable-runbook.html"},
  {"title": "Write a blameless postmortem", "theme": "sre", "difficulty": "middle", "type": "theory", "tags": ["reliability", "monitoring", "incident-response", "troubleshooting"], "path": "questions/sre/write-blameless-postmortem.html"},
  {"title": "Choose between block, file, and object storage", "theme": "storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "filesystem", "reliability"], "path": "questions/storage/block-file-object-storage.html"},
  {"title": "Build a self-service storage platform with guardrails", "theme": "storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "platform-engineering", "governance", "security", "reliability", "cnpe", "cnpa"], "path": "questions/storage/build-self-service-storage-platform.html"},
  {"title": "Choose block-volume performance for a workload", "theme": "storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "capacity-planning", "reliability", "cost-optimization"], "path": "questions/storage/choose-volume-performance.html"},
  {"title": "Use storage quotas without surprising tenants", "theme": "storage", "difficulty": "junior", "type": "scenario", "tags": ["storage", "linux", "capacity-planning", "reliability"], "path": "questions/storage/control-storage-quotas.html"},
  {"title": "Design database point-in-time recovery", "theme": "storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "databases", "reliability", "incident-response"], "path": "questions/storage/database-point-in-time-recovery.html"},
  {"title": "Create an application-consistent volume snapshot", "theme": "storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "databases", "reliability", "automation"], "path": "questions/storage/design-consistent-snapshot.html"},
  {"title": "Design cross-region storage recovery", "theme": "storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "cloud", "reliability", "incident-response", "availability"], "path": "questions/storage/design-cross-region-recovery.html"},
  {"title": "Design immutable recovery copies against ransomware", "theme": "storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "security", "reliability", "incident-response"], "path": "questions/storage/design-immutable-recovery.html"},
  {"title": "Recover storage held by deleted open files", "theme": "storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "storage", "filesystem", "troubleshooting"], "path": "questions/storage/diagnose-deleted-open-files.html"},
  {"title": "Respond to suspected filesystem corruption", "theme": "storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["storage", "filesystem", "linux", "incident-response", "troubleshooting", "lfcs"], "path": "questions/storage/diagnose-filesystem-corruption.html"},
  {"title": "Distinguish backups from storage snapshots", "theme": "storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "reliability", "incident-response"], "path": "questions/storage/distinguish-backups-and-snapshots.html"},
  {"title": "Explain RAID redundancy and its limits", "theme": "storage", "difficulty": "junior", "type": "theory", "tags": ["storage", "hardware", "reliability", "availability"], "path": "questions/storage/explain-raid-redundancy.html"},
  {"title": "Govern data retention and deletion across storage systems", "theme": "storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "governance", "security", "reliability", "cost-optimization"], "path": "questions/storage/govern-data-retention.html"},
  {"title": "Plan for performance when restoring a volume from a snapshot", "theme": "storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["storage", "deployment", "troubleshooting", "reliability"], "path": "questions/storage/handle-snapshot-restore-latency.html"},
  {"title": "Diagnose a full filesystem when free space remains", "theme": "storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "storage", "filesystem", "troubleshooting"], "path": "questions/storage/inode-exhaustion.html"},
  {"title": "Investigate a storage latency incident", "theme": "storage", "difficulty": "middle", "type": "troubleshooting", "tags": ["storage", "monitoring", "troubleshooting", "reliability", "lfcs"], "path": "questions/storage/investigate-storage-latency.html"},
  {"title": "Lead an organization-wide storage disaster-recovery strategy", "theme": "storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "incident-response", "governance", "reliability", "availability"], "path": "questions/storage/lead-storage-disaster-recovery.html"},
  {"title": "Design an object-storage lifecycle policy", "theme": "storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "cost-optimization", "reliability", "automation"], "path": "questions/storage/manage-object-lifecycle.html"},
  {"title": "Manage storage cost and capacity as a portfolio", "theme": "storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "cost-optimization", "capacity-planning", "governance", "reliability"], "path": "questions/storage/manage-storage-cost-and-capacity.html"},
  {"title": "Migrate stateful storage with controlled downtime", "theme": "storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "deployment", "reliability", "databases"], "path": "questions/storage/migrate-stateful-storage.html"},
  {"title": "Mount persistent storage safely on Linux", "theme": "storage", "difficulty": "junior", "type": "scenario", "tags": ["linux", "storage", "filesystem", "reliability", "lfcs"], "path": "questions/storage/mount-persistent-storage.html"},
  {"title": "Operate NFS shared storage safely", "theme": "storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "networking", "linux", "reliability", "lfcs"], "path": "questions/storage/operate-nfs-shared-storage.html"},
  {"title": "Plan a degraded RAID rebuild without compounding risk", "theme": "storage", "difficulty": "senior", "type": "scenario", "tags": ["storage", "hardware", "reliability", "incident-response"], "path": "questions/storage/plan-raid-rebuild-risk.html"},
  {"title": "Run a meaningful backup restore exercise", "theme": "storage", "difficulty": "middle", "type": "scenario", "tags": ["storage", "reliability", "incident-response", "automation"], "path": "questions/storage/restore-backup-exercise.html"},
  {"title": "Set storage SLOs for a platform", "theme": "storage", "difficulty": "staff", "type": "scenario", "tags": ["storage", "reliability", "observability", "governance", "capacity-planning"], "path": "questions/storage/set-storage-slos.html"},
  {"title": "Why establish a baseline before performance tuning?", "theme": "systems-performance", "difficulty": "junior", "type": "scenario", "tags": ["performance", "monitoring", "debugging", "capacity-planning"], "path": "questions/systems-performance/baseline-before-tuning.html"},
  {"title": "How do you review whether a benchmark result is valid for a production decision?", "theme": "systems-performance", "difficulty": "senior", "type": "scenario", "tags": ["performance", "capacity-planning", "cloud", "reliability"], "path": "questions/systems-performance/benchmark-validity-review.html"},
  {"title": "How would you govern a capacity model for a multi-tenant platform?", "theme": "systems-performance", "difficulty": "staff", "type": "scenario", "tags": ["capacity-planning", "performance", "cloud", "governance"], "path": "questions/systems-performance/capacity-model-governance.html"},
  {"title": "When are high context-switch rates a performance concern?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "cpu", "performance", "debugging"], "path": "questions/systems-performance/context-switch-investigation.html"},
  {"title": "What is a safe first pass for investigating unexpected CPU consumption?", "theme": "systems-performance", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "cpu", "performance", "debugging"], "path": "questions/systems-performance/cpu-profiling-first-pass.html"},
  {"title": "How do you investigate high CPU steal time on a virtual machine?", "theme": "systems-performance", "difficulty": "senior", "type": "troubleshooting", "tags": ["cloud", "cpu", "virtualization", "performance"], "path": "questions/systems-performance/cpu-steal-time-cloud.html"},
  {"title": "What is the difference between CPU utilization and CPU saturation?", "theme": "systems-performance", "difficulty": "junior", "type": "theory", "tags": ["linux", "cpu", "performance", "monitoring"], "path": "questions/systems-performance/cpu-utilization-and-saturation.html"},
  {"title": "How do you break down elevated disk I/O latency?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "storage", "performance", "debugging"], "path": "questions/systems-performance/disk-latency-breakdown.html"},
  {"title": "What safeguards are needed when using eBPF for production observability?", "theme": "systems-performance", "difficulty": "middle", "type": "scenario", "tags": ["linux", "observability", "performance", "security"], "path": "questions/systems-performance/ebpf-observability-safety.html"},
  {"title": "How do you prioritize a platform-wide performance and efficiency roadmap?", "theme": "systems-performance", "difficulty": "staff", "type": "scenario", "tags": ["performance", "cost-optimization", "capacity-planning", "platform-engineering"], "path": "questions/systems-performance/efficiency-roadmap-prioritization.html"},
  {"title": "How does the Linux page cache affect filesystem performance measurements?", "theme": "systems-performance", "difficulty": "middle", "type": "theory", "tags": ["linux", "filesystem", "memory", "performance"], "path": "questions/systems-performance/filesystem-cache-behavior.html"},
  {"title": "How do you select ftrace events for a latency investigation?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "performance", "debugging", "observability"], "path": "questions/systems-performance/ftrace-event-selection.html"},
  {"title": "How are latency, throughput, and concurrency related during load?", "theme": "systems-performance", "difficulty": "junior", "type": "theory", "tags": ["performance", "capacity-planning", "monitoring", "reliability"], "path": "questions/systems-performance/latency-throughput-concurrency.html"},
  {"title": "How do you prove lock contention is causing an application latency regression?", "theme": "systems-performance", "difficulty": "senior", "type": "troubleshooting", "tags": ["linux", "performance", "debugging", "monitoring"], "path": "questions/systems-performance/lock-contention-analysis.html"},
  {"title": "Which signals distinguish memory use from memory pressure on Linux?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "memory", "performance", "monitoring"], "path": "questions/systems-performance/memory-pressure-signals.html"},
  {"title": "How do TCP retransmissions inform a latency investigation?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "networking", "tcp", "performance"], "path": "questions/systems-performance/network-retransmission-triage.html"},
  {"title": "How can NUMA locality cause a performance regression on a large host?", "theme": "systems-performance", "difficulty": "senior", "type": "scenario", "tags": ["linux", "memory", "cpu", "performance"], "path": "questions/systems-performance/numa-locality-performance.html"},
  {"title": "How do you investigate an OOM-killer incident without treating the kill as the root cause?", "theme": "systems-performance", "difficulty": "middle", "type": "troubleshooting", "tags": ["linux", "memory", "incident-response", "performance"], "path": "questions/systems-performance/oom-killer-incident.html"},
  {"title": "How do you use sampling profilers without distorting production performance?", "theme": "systems-performance", "difficulty": "middle", "type": "scenario", "tags": ["linux", "performance", "debugging", "monitoring"], "path": "questions/systems-performance/perf-sampling-and-overhead.html"},
  {"title": "How do you use performance budgets in architecture governance?", "theme": "systems-performance", "difficulty": "staff", "type": "theory", "tags": ["performance", "capacity-planning", "governance", "reliability"], "path": "questions/systems-performance/performance-budget-architecture.html"},
  {"title": "How should a staff engineer lead a cross-layer performance incident?", "theme": "systems-performance", "difficulty": "staff", "type": "scenario", "tags": ["performance", "incident-response", "reliability", "debugging"], "path": "questions/systems-performance/performance-incident-command.html"},
  {"title": "How would you design a systems-performance observability program across teams?", "theme": "systems-performance", "difficulty": "staff", "type": "scenario", "tags": ["performance", "observability", "governance", "reliability"], "path": "questions/systems-performance/performance-observability-program.html"},
  {"title": "What does Linux pressure stall information add to resource monitoring?", "theme": "systems-performance", "difficulty": "middle", "type": "theory", "tags": ["linux", "cpu", "memory", "performance"], "path": "questions/systems-performance/pressure-stall-information.html"},
  {"title": "How do you investigate a tail-latency incident when average latency is normal?", "theme": "systems-performance", "difficulty": "senior", "type": "troubleshooting", "tags": ["performance", "monitoring", "incident-response", "reliability"], "path": "questions/systems-performance/tail-latency-incident.html"},
  {"title": "How do you apply the USE method to a production resource?", "theme": "systems-performance", "difficulty": "junior", "type": "troubleshooting", "tags": ["linux", "performance", "monitoring", "debugging"], "path": "questions/systems-performance/use-method-basics.html"},
  {"title": "Design accessibility testing strategy", "theme": "testing-strategy", "difficulty": "junior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/accessibility-test-strategy.html"},
  {"title": "Adopt consumer-driven contracts", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/consumer-driven-contracts.html"},
  {"title": "Use contract tests between services", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/contract-testing-boundaries.html"},
  {"title": "Control end-to-end test scope", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/end-to-end-test-scope.html"},
  {"title": "Design ephemeral test environments", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/ephemeral-test-environments.html"},
  {"title": "Define a flaky-test quarantine policy", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/flaky-test-quarantine-policy.html"},
  {"title": "Choose integration test boundaries", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/integration-test-boundaries.html"},
  {"title": "Define integration test data contracts", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/integration-test-data-contract.html"},
  {"title": "Evaluate mutation testing trade-offs", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/mutation-testing-tradeoffs.html"},
  {"title": "Place performance tests in CI", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/performance-tests-in-ci.html"},
  {"title": "Set production experiment guardrails", "theme": "testing-strategy", "difficulty": "staff", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/production-experiment-guardrails.html"},
  {"title": "Prioritize quality investment portfolio", "theme": "testing-strategy", "difficulty": "staff", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/quality-investment-portfolio.html"},
  {"title": "Design release gates as risk controls", "theme": "testing-strategy", "difficulty": "staff", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/release-gate-design.html"},
  {"title": "Set security testing boundaries", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/security-test-boundaries.html"},
  {"title": "Use shadow traffic safely", "theme": "testing-strategy", "difficulty": "staff", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/shadow-traffic-testing.html"},
  {"title": "Set shared test environment policy", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/shared-test-environment-policy.html"},
  {"title": "Name test cases for diagnosis", "theme": "testing-strategy", "difficulty": "junior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-case-naming.html"},
  {"title": "Treat coverage as a testing signal", "theme": "testing-strategy", "difficulty": "junior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-coverage-signal.html"},
  {"title": "Design isolated test data", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-data-isolation.html"},
  {"title": "Manage test data safely", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-data-management.html"},
  {"title": "Model test execution cost", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-execution-cost-model.html"},
  {"title": "Make test failures observable", "theme": "testing-strategy", "difficulty": "senior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-observability.html"},
  {"title": "Define test-pyramid boundaries", "theme": "testing-strategy", "difficulty": "junior", "type": "theory", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-pyramid-boundaries.html"},
  {"title": "Set test-suite execution policy", "theme": "testing-strategy", "difficulty": "middle", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-suite-execution-policy.html"},
  {"title": "Assign test suite ownership", "theme": "testing-strategy", "difficulty": "staff", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/test-suite-ownership.html"},
  {"title": "Design a focused unit test", "theme": "testing-strategy", "difficulty": "junior", "type": "scenario", "tags": ["testing-strategy", "quality", "reliability", "delivery"], "path": "questions/testing-strategy/unit-test-design.html"},
  {"title": "Build a learning loop from production troubleshooting", "theme": "troubleshooting", "difficulty": "staff", "type": "scenario", "tags": ["troubleshooting", "leadership", "automation", "reliability", "runbooks"], "path": "questions/troubleshooting/build-learning-loop.html"},
  {"title": "Build an incident timeline from reliable evidence", "theme": "troubleshooting", "difficulty": "junior", "type": "scenario", "tags": ["troubleshooting", "logs", "monitoring", "incident-response"], "path": "questions/troubleshooting/collect-timeline.html"},
  {"title": "Debug an authentication failure without weakening access control", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "security", "iam", "logs", "least-privilege"], "path": "questions/troubleshooting/debug-auth-failure.html"},
  {"title": "Triage an error-budget burn alert", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "reliability", "monitoring", "incident-response"], "path": "questions/troubleshooting/debug-error-budget.html"},
  {"title": "Debug latency without averaging away the incident", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "latency", "performance", "monitoring", "metrics"], "path": "questions/troubleshooting/debug-latency.html"},
  {"title": "Debug an observability gap during an active incident", "theme": "troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["troubleshooting", "observability", "monitoring", "logs", "metrics"], "path": "questions/troubleshooting/debug-observability-gap.html"},
  {"title": "Triage a growing asynchronous work backlog", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "message-queues", "capacity-planning", "monitoring", "reliability"], "path": "questions/troubleshooting/debug-queue-backlog.html"},
  {"title": "Diagnose a TLS handshake failure safely", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "tls", "security", "networking", "certificates"], "path": "questions/troubleshooting/debug-tls.html"},
  {"title": "Define an organization-wide troubleshooting strategy", "theme": "troubleshooting", "difficulty": "staff", "type": "scenario", "tags": ["troubleshooting", "leadership", "runbooks", "reliability", "incident-management"], "path": "questions/troubleshooting/define-troubleshooting-strategy.html"},
  {"title": "Design reliable multi-team incident handoffs", "theme": "troubleshooting", "difficulty": "staff", "type": "scenario", "tags": ["troubleshooting", "leadership", "incident-management", "runbooks", "reliability"], "path": "questions/troubleshooting/design-multi-team-handoff.html"},
  {"title": "Design a production troubleshooting experiment", "theme": "troubleshooting", "difficulty": "senior", "type": "scenario", "tags": ["troubleshooting", "runbooks", "debugging", "change-management", "reliability"], "path": "questions/troubleshooting/design-runbook-experiment.html"},
  {"title": "Diagnose DNS failure from client to authoritative data", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "dns", "networking", "resolver", "monitoring"], "path": "questions/troubleshooting/diagnose-dns.html"},
  {"title": "Establish impact before changing a failing service", "theme": "troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["troubleshooting", "incident-response", "monitoring", "reliability"], "path": "questions/troubleshooting/establish-impact.html"},
  {"title": "Govern risky mitigations during a business-critical outage", "theme": "troubleshooting", "difficulty": "staff", "type": "scenario", "tags": ["troubleshooting", "leadership", "change-management", "incident-response", "reliability"], "path": "questions/troubleshooting/govern-risky-mitigation.html"},
  {"title": "Contain a bad deployment while protecting evidence", "theme": "troubleshooting", "difficulty": "senior", "type": "troubleshooting", "tags": ["troubleshooting", "deployment", "recovery", "incident-response", "reliability", "cgoa"], "path": "questions/troubleshooting/handle-bad-deployment.html"},
  {"title": "Investigate a production data mismatch safely", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "databases", "recovery", "reliability", "incident-response"], "path": "questions/troubleshooting/investigate-data-mismatch.html"},
  {"title": "Isolate a suspected change without guessing", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "deployment", "debugging", "change-management"], "path": "questions/troubleshooting/isolate-change.html"},
  {"title": "Lead a severe incident without uncontrolled changes", "theme": "troubleshooting", "difficulty": "senior", "type": "scenario", "tags": ["troubleshooting", "incident-response", "leadership", "reliability", "change-management"], "path": "questions/troubleshooting/lead-sev-incident.html"},
  {"title": "Reduce recurring incidents across a platform portfolio", "theme": "troubleshooting", "difficulty": "staff", "type": "scenario", "tags": ["troubleshooting", "leadership", "reliability", "capacity-planning", "automation"], "path": "questions/troubleshooting/portfolio-recurrence.html"},
  {"title": "Read alert context before escalating", "theme": "troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["troubleshooting", "monitoring", "logs", "incident-response"], "path": "questions/troubleshooting/read-alert-context.html"},
  {"title": "Stop a cascading failure while preserving useful traffic", "theme": "troubleshooting", "difficulty": "middle", "type": "scenario", "tags": ["troubleshooting", "reliability", "dependencies", "capacity-planning", "incident-response"], "path": "questions/troubleshooting/reduce-cascading-failure.html"},
  {"title": "Decide whether a restart is a safe diagnostic action", "theme": "troubleshooting", "difficulty": "junior", "type": "scenario", "tags": ["troubleshooting", "recovery", "deployment", "reliability"], "path": "questions/troubleshooting/safe-restart.html"},
  {"title": "Trace a dependency failure across service boundaries", "theme": "troubleshooting", "difficulty": "middle", "type": "troubleshooting", "tags": ["troubleshooting", "dependencies", "logs", "monitoring", "reliability"], "path": "questions/troubleshooting/trace-dependency-failure.html"},
  {"title": "Triage a regional outage with a safe traffic strategy", "theme": "troubleshooting", "difficulty": "senior", "type": "scenario", "tags": ["troubleshooting", "availability", "networking", "incident-response", "capacity-planning"], "path": "questions/troubleshooting/triage-regional-outage.html"},
  {"title": "Verify recovery rather than trusting a green deployment", "theme": "troubleshooting", "difficulty": "junior", "type": "troubleshooting", "tags": ["troubleshooting", "monitoring", "reliability", "deployment"], "path": "questions/troubleshooting/verify-recovery.html"},
  {"title": "Use git bisect to find a regression", "theme": "version-control", "difficulty": "middle", "type": "troubleshooting", "tags": ["git", "version-control", "troubleshooting", "debugging"], "path": "questions/version-control/bisect-regression.html"},
  {"title": "Explain local branches and remote-tracking branches", "theme": "version-control", "difficulty": "junior", "type": "theory", "tags": ["git", "version-control", "delivery"], "path": "questions/version-control/branches-and-remote-tracking.html"},
  {"title": "Design branching governance across product teams", "theme": "version-control", "difficulty": "staff", "type": "scenario", "tags": ["git", "version-control", "governance", "delivery", "change-management"], "path": "questions/version-control/branching-governance.html"},
  {"title": "Establish a change-provenance strategy for production", "theme": "version-control", "difficulty": "staff", "type": "scenario", "tags": ["git", "version-control", "supply-chain", "security", "governance", "delivery"], "path": "questions/version-control/change-provenance-strategy.html"},
  {"title": "Cherry-pick a targeted fix safely", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "delivery", "troubleshooting"], "path": "questions/version-control/cherry-pick-safely.html"},
  {"title": "Describe a reviewable Git commit", "theme": "version-control", "difficulty": "junior", "type": "scenario", "tags": ["git", "version-control", "change-management", "delivery"], "path": "questions/version-control/commit-quality.html"},
  {"title": "Fetch and inspect before integrating remote work", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "delivery", "troubleshooting"], "path": "questions/version-control/fetch-before-integrate.html"},
  {"title": "Explain Git's object model", "theme": "version-control", "difficulty": "junior", "type": "theory", "tags": ["git", "version-control", "cgoa"], "path": "questions/version-control/git-object-model.html"},
  {"title": "Structure a Git state store for GitOps environments", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["version-control", "git", "ci-cd", "kubernetes", "deployment", "governance", "gitops", "cgoa"], "path": "questions/version-control/gitops-state-store-layout.html"},
  {"title": "Choose the right boundary for Git hooks", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "ci-cd", "security"], "path": "questions/version-control/hooks-boundaries.html"},
  {"title": "Manage ignored files without hiding needed changes", "theme": "version-control", "difficulty": "junior", "type": "troubleshooting", "tags": ["git", "version-control", "security", "troubleshooting"], "path": "questions/version-control/ignore-rules.html"},
  {"title": "Keep a large Git repository operable", "theme": "version-control", "difficulty": "senior", "type": "scenario", "tags": ["git", "version-control", "performance", "operations"], "path": "questions/version-control/large-repository-maintenance.html"},
  {"title": "Choose merge or rebase when integrating a branch", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "change-management", "delivery"], "path": "questions/version-control/merge-versus-rebase.html"},
  {"title": "Make a monorepo versus multirepo decision", "theme": "version-control", "difficulty": "staff", "type": "scenario", "tags": ["git", "version-control", "platform-engineering", "operations", "governance", "cba"], "path": "questions/version-control/monorepo-decision.html"},
  {"title": "Use multiple Git worktrees safely", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "operations", "troubleshooting"], "path": "questions/version-control/multiple-worktrees.html"},
  {"title": "Recover a locally lost commit with reflog", "theme": "version-control", "difficulty": "middle", "type": "troubleshooting", "tags": ["git", "version-control", "troubleshooting", "recovery"], "path": "questions/version-control/recover-with-reflog.html"},
  {"title": "Create an auditable release tag", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "delivery", "supply-chain", "cgoa"], "path": "questions/version-control/release-tags.html"},
  {"title": "Govern repository access and automation credentials", "theme": "version-control", "difficulty": "staff", "type": "scenario", "tags": ["git", "version-control", "security", "governance", "supply-chain"], "path": "questions/version-control/repository-access-governance.html"},
  {"title": "Respond to suspected Git repository corruption", "theme": "version-control", "difficulty": "senior", "type": "troubleshooting", "tags": ["git", "version-control", "troubleshooting", "recovery", "reliability"], "path": "questions/version-control/repository-corruption-response.html"},
  {"title": "Resolve a Git merge conflict safely", "theme": "version-control", "difficulty": "middle", "type": "troubleshooting", "tags": ["git", "version-control", "troubleshooting", "change-management"], "path": "questions/version-control/resolve-conflicts.html"},
  {"title": "Choose between Git revert and reset for a bad change", "theme": "version-control", "difficulty": "middle", "type": "scenario", "tags": ["git", "version-control", "delivery", "troubleshooting"], "path": "questions/version-control/revert-versus-reset.html"},
  {"title": "Repair a shared branch with a force push safely", "theme": "version-control", "difficulty": "senior", "type": "scenario", "tags": ["git", "version-control", "delivery", "change-management", "troubleshooting"], "path": "questions/version-control/safe-force-push.html"},
  {"title": "Migrate source control platforms without losing traceability", "theme": "version-control", "difficulty": "staff", "type": "scenario", "tags": ["git", "version-control", "change-management", "governance", "reliability"], "path": "questions/version-control/source-migration.html"},
  {"title": "Explain the purpose of Git's staging area", "theme": "version-control", "difficulty": "junior", "type": "theory", "tags": ["git", "version-control", "delivery"], "path": "questions/version-control/staging-area-purpose.html"},
  {"title": "Evaluate Git submodules for a production dependency", "theme": "version-control", "difficulty": "senior", "type": "scenario", "tags": ["git", "version-control", "dependencies", "supply-chain"], "path": "questions/version-control/submodule-risk.html"},
  {"title": "Verify signed commits and release tags", "theme": "version-control", "difficulty": "senior", "type": "scenario", "tags": ["git", "version-control", "security", "delivery", "supply-chain"], "path": "questions/version-control/verify-signed-release.html"},
  {"title": "Design useful web-server access logs", "theme": "web-servers", "difficulty": "junior", "type": "scenario", "tags": ["logging", "observability", "http", "web-server"], "path": "questions/web-servers/access-log-design.html"},
  {"title": "Prevent a reverse-proxy cache from serving the wrong response", "theme": "web-servers", "difficulty": "middle", "type": "troubleshooting", "tags": ["http", "nginx", "performance", "security"], "path": "questions/web-servers/cache-proxy-correctness.html"},
  {"title": "Design a response-compression policy", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["http", "nginx", "performance", "security"], "path": "questions/web-servers/compression-policy.html"},
  {"title": "Model web-server connection capacity", "theme": "web-servers", "difficulty": "senior", "type": "scenario", "tags": ["performance", "capacity-planning", "file-descriptors", "nginx"], "path": "questions/web-servers/connection-capacity-model.html"},
  {"title": "Govern edge cost and capacity across products", "theme": "web-servers", "difficulty": "staff", "type": "scenario", "tags": ["capacity-planning", "cost-optimization", "governance", "web-server"], "path": "questions/web-servers/edge-cost-and-capacity-governance.html"},
  {"title": "Lead an edge-web-server incident triage", "theme": "web-servers", "difficulty": "senior", "type": "troubleshooting", "tags": ["incident-response", "troubleshooting", "nginx", "observability"], "path": "questions/web-servers/edge-incident-triage.html"},
  {"title": "Establish an edge observability strategy", "theme": "web-servers", "difficulty": "staff", "type": "scenario", "tags": ["observability", "metrics", "logging", "governance"], "path": "questions/web-servers/edge-observability-strategy.html"},
  {"title": "Define an edge-platform contract for application teams", "theme": "web-servers", "difficulty": "staff", "type": "scenario", "tags": ["platform-engineering", "governance", "web-server", "security"], "path": "questions/web-servers/edge-platform-contract.html"},
  {"title": "Preserve client identity behind proxies", "theme": "web-servers", "difficulty": "middle", "type": "troubleshooting", "tags": ["http", "nginx", "security", "logging"], "path": "questions/web-servers/forwarded-client-ip.html"},
  {"title": "Govern global traffic failover for web endpoints", "theme": "web-servers", "difficulty": "staff", "type": "scenario", "tags": ["availability", "dns", "traffic-management", "incident-management"], "path": "questions/web-servers/global-traffic-failover.html"},
  {"title": "Reload and drain a web server without dropping traffic", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["nginx", "deployment", "availability", "web-server"], "path": "questions/web-servers/graceful-reload-and-drain.html"},
  {"title": "Explain a web server request lifecycle", "theme": "web-servers", "difficulty": "junior", "type": "theory", "tags": ["http", "web-server", "nginx"], "path": "questions/web-servers/http-request-lifecycle.html"},
  {"title": "Roll out HTTP/2 or HTTP/3 safely", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["http", "tls", "performance", "web-server"], "path": "questions/web-servers/http2-and-http3-rollout.html"},
  {"title": "Design multi-tenant isolation at the web edge", "theme": "web-servers", "difficulty": "staff", "type": "scenario", "tags": ["security", "governance", "web-server", "availability"], "path": "questions/web-servers/multi-tenant-edge-isolation.html"},
  {"title": "Set reverse-proxy timeouts from a request budget", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["nginx", "http", "latency", "reliability"], "path": "questions/web-servers/proxy-timeout-budget.html"},
  {"title": "Apply web-server rate limits without harming clients", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["nginx", "security", "availability", "traffic-management"], "path": "questions/web-servers/rate-limiting-policy.html"},
  {"title": "Debug a 502 response from a reverse proxy", "theme": "web-servers", "difficulty": "middle", "type": "troubleshooting", "tags": ["http", "nginx", "web-server", "troubleshooting"], "path": "questions/web-servers/reverse-proxy-502-debugging.html"},
  {"title": "Serve static content with correct cache control", "theme": "web-servers", "difficulty": "junior", "type": "scenario", "tags": ["http", "web-server", "performance"], "path": "questions/web-servers/static-content-cache-control.html"},
  {"title": "Deploy a TLS certificate on a web server", "theme": "web-servers", "difficulty": "junior", "type": "scenario", "tags": ["tls", "certificates", "http", "web-server", "lfcs"], "path": "questions/web-servers/tls-certificate-deployment.html"},
  {"title": "Establish a TLS security baseline at the edge", "theme": "web-servers", "difficulty": "senior", "type": "scenario", "tags": ["tls", "certificates", "security", "web-server"], "path": "questions/web-servers/tls-security-baseline.html"},
  {"title": "Choose an upstream load-balancing policy", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["nginx", "web-server", "traffic-management", "availability"], "path": "questions/web-servers/upstream-load-balancing.html"},
  {"title": "Make upstream retries safe at a proxy", "theme": "web-servers", "difficulty": "senior", "type": "scenario", "tags": ["http", "nginx", "reliability", "availability"], "path": "questions/web-servers/upstream-retry-safety.html"},
  {"title": "Configure virtual-host routing safely", "theme": "web-servers", "difficulty": "junior", "type": "theory", "tags": ["http", "dns", "nginx", "web-server"], "path": "questions/web-servers/virtual-host-routing.html"},
  {"title": "Define WAF and application-security boundaries", "theme": "web-servers", "difficulty": "senior", "type": "scenario", "tags": ["security", "web-server", "http", "governance"], "path": "questions/web-servers/waf-and-application-boundaries.html"},
  {"title": "Proxy WebSocket connections correctly", "theme": "web-servers", "difficulty": "middle", "type": "scenario", "tags": ["http", "nginx", "tcp", "web-server"], "path": "questions/web-servers/websocket-proxying.html"},
];

window.certifications = [
  {"tag": "capa", "map": "docs/certifications/capa.md", "minimumQuestions": 12},
  {"tag": "cba", "map": "docs/certifications/cba.md", "minimumQuestions": 23},
  {"tag": "cca", "map": "docs/certifications/cca.md", "minimumQuestions": 20},
  {"tag": "cgoa", "map": "docs/certifications/cgoa.md", "minimumQuestions": 32},
  {"tag": "cka", "map": "docs/certifications/cka.md", "minimumQuestions": 25},
  {"tag": "ckad", "map": "docs/certifications/ckad.md", "minimumQuestions": 20},
  {"tag": "ckne", "map": "docs/certifications/ckne.md", "minimumQuestions": 22},
  {"tag": "cks", "map": "docs/certifications/cks.md", "minimumQuestions": 19},
  {"tag": "cnpa", "map": "docs/certifications/cnpa.md", "minimumQuestions": 21},
  {"tag": "cnpe", "map": "docs/certifications/cnpe.md", "minimumQuestions": 15},
  {"tag": "ica", "map": "docs/certifications/ica.md", "minimumQuestions": 15},
  {"tag": "kca", "map": "docs/certifications/kca.md", "minimumQuestions": 6},
  {"tag": "kcna", "map": "docs/certifications/kcna.md", "minimumQuestions": 15},
  {"tag": "kcsa", "map": "docs/certifications/kcsa.md", "minimumQuestions": 20},
  {"tag": "lfcs", "map": "docs/certifications/lfcs.md", "minimumQuestions": 25},
  {"tag": "otca", "map": "docs/certifications/otca.md", "minimumQuestions": 16},
  {"tag": "pca", "map": "docs/certifications/pca.md", "minimumQuestions": 25},
];

window.learningPaths = [
  {
    "slug": "sre-track",
    "title": "Site reliability engineering",
    "audience": "Engineers moving into an SRE or on-call role who can already run a service but have never been asked to defend its reliability with numbers",
    "prerequisites": [],
    "steps": [
      {
        "title": "Define service reliability and the role of an SRE",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/define-service-reliability.html",
        "why": "Everything later in the track is a technique for defending a promise, so start by naming the promise: reliability is a measured user outcome and SRE is shared ownership of it, not a ticket queue."
      },
      {
        "title": "Define an SLI and SLO for an API",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/define-an-sli-and-slo.html",
        "why": "The promise is only defensible once it is arithmetic. Learn the SLI/SLO vocabulary — eligible events, good events, window, owner — before any step that assumes a target exists."
      },
      {
        "title": "Choose a user-journey SLI",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/define-user-journey-sli.html",
        "why": "Knowing the SLI definition is not the same as choosing a good one. This step applies the previous definition to a real checkout journey and shows why a convenient host metric fails as an indicator."
      },
      {
        "title": "Explain an error budget",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/explain-error-budget.html",
        "why": "An error budget is nothing but the leftover of the SLO you just learned to define, so it can only be taught after the target and its window are concrete. Every budget, burn-rate, and policy step below depends on this one."
      },
      {
        "title": "Explain Linux process states during an incident",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/process-states.html",
        "why": "The track now drops from the promise to the machine that keeps it. Process state is the smallest unit of host evidence, and the runnable-versus-uninterruptible distinction here is exactly what makes the next step readable."
      },
      {
        "title": "Interpret a high Linux load average",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/load-average-interpretation.html",
        "why": "Linux load counts uninterruptible sleep as well as runnable work, so this question is misread by anyone who has not just learned process states. Placed here it teaches saturation-versus-utilisation rather than a folk rule about CPU count."
      },
      {
        "title": "Triage a hung process without destroying evidence",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/hung-process-triage.html",
        "why": "Process state showed you what a stuck task looks like; this is the first step that makes you act on one. It introduces the capture-before-you-restart discipline — evidence in increasing order of intrusion — that the incident stage later turns into a team practice."
      },
      {
        "title": "Diagnose a systemd service that repeatedly fails",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/systemd-service-failure.html",
        "why": "The first host-level thing an on-call engineer actually touches is a unit that will not stay up. It also introduces the restart-amplification trap that the graceful-shutdown contract in the next step resolves."
      },
      {
        "title": "Design a graceful Linux service shutdown",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/signals-and-graceful-shutdown.html",
        "why": "Comes directly after the restart-policy discussion because it supplies the missing half: SIGTERM as a bounded drain contract and SIGKILL as a deadline, plus removing the instance from the load balancer before exit."
      },
      {
        "title": "Investigate a Linux out-of-memory kill",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/oom-killer-investigation.html",
        "why": "The first named saturation failure, and it needs the earlier steps: kernel OOM selection is only interpretable once you can read process and cgroup pressure rather than an application exit code."
      },
      {
        "title": "Diagnose too many open files in a Linux service",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/file-descriptor-exhaustion.html",
        "why": "A second exhaustion class with a different shape — a slow leak against a soft limit rather than a sudden kill — which is what teaches the general habit of alerting on a resource relative to its limit."
      },
      {
        "title": "Trace a DNS lookup from an application to an answer",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/dns-resolution-path.html",
        "why": "The track now leaves the host. Most \"the service is down\" reports start at name resolution, and walking stub resolver to cache to authoritative teaches the layer discipline — say which component answered and from which cache — that the remaining network steps reuse."
      },
      {
        "title": "Diagnose a failed TCP three-way handshake",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/tcp-three-way-handshake.html",
        "why": "Once names resolve, the next failure boundary is the connection. SYN followed by RST versus SYN with no reply is the cheapest way to separate \"nothing is listening\" from \"something is dropping\", and it is the evidence the health-check step below depends on."
      },
      {
        "title": "Design load-balancer health checks",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/load-balancer-health-check-design.html",
        "why": "The first design question in the track, and it needs the two steps before it: a health check is only a real decision once you know what a completed handshake proves, what it says nothing about downstream, and how eviction thresholds interact with the drain contract from the shutdown step."
      },
      {
        "title": "Compare metrics, logs, and traces during an incident",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/three-observability-signals.html",
        "why": "The host and network stages read one machine at a time; here the track switches to reading a population. It establishes the alert-then-metrics-then-trace-then-logs order that every following telemetry step assumes."
      },
      {
        "title": "Choose a counter, gauge, histogram, or summary",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/describe-metric-types.html",
        "why": "Placed before anything that reads a distribution, because counter versus gauge versus histogram is the choice that decides whether tail latency is measurable at all. Its bucket advice is a prerequisite for the quantile step two positions later."
      },
      {
        "title": "Instrument a distributed trace for an API request",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/instrument-a-trace.html",
        "why": "Metrics establish that a population is unhealthy; a trace establishes where in the dependency chain it happened. Coming after the signal comparison, context propagation reads as filling a named gap rather than as tooling for its own sake."
      },
      {
        "title": "Measure and improve tail latency",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/measure-tail-latency.html",
        "why": "The first senior measurement question, and it only works once histograms and traces are both in place. It asks you to choose buckets around an SLO boundary, which ties this stage back to the objectives defined in the opening steps."
      },
      {
        "title": "Classify an alert as a page, ticket, or log",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/classify-alert-urgency.html",
        "why": "Before writing an alert, decide whether it should wake anyone. Page, ticket, or log is the cheapest filter in the track, and taking it first stops the next steps from producing technically correct alerts that no responder can act on."
      },
      {
        "title": "Build an actionable production alert",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/build-an-actionable-alert.html",
        "why": "Applies that classification to one concrete alert — owner, runbook, symptom, and an expression tested against missing data. It closes by pointing at multi-window SLO logic, which is exactly what the next two steps construct."
      },
      {
        "title": "Explain an SLO error-budget burn-rate alert",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/slo-burn-rate.html",
        "why": "The arithmetic step. Burn rate is the bad-event rate divided by the budget rate defined back in the error-budget step, so it belongs after both that definition and a working alerting habit — and strictly before any multi-window alert design."
      },
      {
        "title": "Design a multi-window burn-rate alert",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/design-multiwindow-burn-alert.html",
        "why": "Deliberately after the senior burn-rate theory even though it is labelled middle: the short-and-long-window construction is a design decision rather than a copied recipe only once you can compute the burn rate it thresholds."
      },
      {
        "title": "Read alert context before escalating",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/read-alert-context.html",
        "why": "The incident stage starts where a page starts. Having just built alerts, the first responder skill is reading one back critically — what it measures, over what window, and whether it is a detector failure rather than an outage."
      },
      {
        "title": "Establish impact before changing a failing service",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/establish-impact.html",
        "why": "Comes before any mitigation step because it fixes the order of operations for the whole stage: record a baseline and form one falsifiable hypothesis before changing anything, since changing several variables at once destroys the evidence."
      },
      {
        "title": "Triage an error-budget burn alert",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-error-budget.html",
        "why": "The direct sequel to the multi-window burn alert you designed — this is what to do when it fires. It tells you to validate the numerator, denominator, window, and exclusions first, which is only a meaningful instruction to someone who defined those fields earlier in this track."
      },
      {
        "title": "Triage a production incident",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/triage-production-incident.html",
        "why": "Scales the single-responder method up to a declared incident with a lead, a severity, and an update cadence. This is where the track stops teaching a debugging technique and starts teaching a role."
      },
      {
        "title": "Verify recovery rather than trusting a green deployment",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/verify-recovery.html",
        "why": "Near the end of the incident stage despite its junior label, because \"is it actually over?\" is only answerable once you hold an impact statement and an SLI to check it against. It is the antidote to the briefly green dashboard the previous steps can produce."
      },
      {
        "title": "Write a blameless postmortem",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/write-blameless-postmortem.html",
        "why": "Closes the loop the page opened, and it depends on the evidence habits built from the hung-process step onward: a postmortem can only be written from the timestamps, alert payloads, and change records that triage bothered to preserve."
      },
      {
        "title": "Choose timeouts, retries, and backoff",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/timeouts-retries-backoff.html",
        "why": "The track turns from responding to failure to designing against it. Deadlines, bounded attempts, and jittered backoff come first because retry amplification is the mechanism underneath most of the cascades in the steps that follow."
      },
      {
        "title": "Make a retried write idempotent",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/idempotent-operations.html",
        "why": "Immediately after retries, because the previous step is only safe advice when a repeated write is safe. A timeout means the caller lacks an answer, not that the server did nothing, and that distinction is the entire reason idempotency keys exist."
      },
      {
        "title": "Use a circuit breaker without masking failure",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/circuit-breakers.html",
        "why": "A retry budget protects the caller; a breaker protects the dependency. It belongs after both, because its failure modes — synchronised half-open probes, a silently open circuit hiding a long outage — are the retry problems you have just learned to recognise, one layer out."
      },
      {
        "title": "Prevent cascading failures",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/prevent-cascading-failures.html",
        "why": "The synthesis of this stage: timeouts, bulkheads, backpressure, and degradation set as one compatible system instead of four independent settings. It is unreadable before the three primitives above it, and it is the reason the next stage exists."
      },
      {
        "title": "Define chaos engineering and what it is for",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/define-chaos-engineering.html",
        "why": "You now hold containment mechanisms you believe in but have never falsified. Chaos engineering enters here and not earlier because its own stated precondition — observability good enough to detect harm within seconds — is exactly what the telemetry stage built."
      },
      {
        "title": "State a steady-state hypothesis",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/state-a-steady-state-hypothesis.html",
        "why": "An experiment needs a falsifiable statement before it needs a tool, and the hypothesis reuses the user-visible SLI thinking from the opening steps rather than a CPU graph. Without this there is nothing for the later steps to abort against."
      },
      {
        "title": "Verify observability before injecting a fault",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/verify-observability-before-injecting.html",
        "why": "The audit between hypothesis and injection: histogram resolution, labels that match the scope, and telemetry that does not travel the path you are about to break. It turns the earlier metric-type and tail-latency choices into a go or no-go decision."
      },
      {
        "title": "Control the blast radius of an experiment",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/control-the-blast-radius.html",
        "why": "Last in this stage because it is the safety contract that lets the rest of it run in production: bound the fault on every axis, widen only in planned steps, and give each step its own abort condition."
      },
      {
        "title": "Run a production-readiness review",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/run-production-readiness-review.html",
        "why": "The staff stage opens by making the whole track repeatable for a service you did not build. A readiness review is a walk through every earlier stage — ownership, SLOs, capacity, failure modes, rollback — which is precisely why it cannot come first."
      },
      {
        "title": "Measure and reduce toil",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/measure-and-reduce-toil.html",
        "why": "Moves the subject from one service to the engineer's time. It follows the incident and readiness work because you can only price toil after feeling which repeated manual tasks those stages generate."
      },
      {
        "title": "Govern an error-budget policy",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/govern-error-budget-policy.html",
        "why": "The clearest pedagogy-over-difficulty placement in the track: this staff question is meaningless without the junior error-budget step near the start and the burn-rate maths in the middle. Only with both does \"what happens when the budget is exhausted\" become an organisational decision rather than a definition."
      },
      {
        "title": "Build a reliability investment roadmap",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/build-reliability-roadmap.html",
        "why": "The final step because it is the only one that consumes the output of every other: SLO gaps, incident history, measured toil, and experiment results become a funded plan with owners. The track ends where it began, on the promise, now with a way to invest in it."
      }
    ]
  },
  {
    "slug": "devops-platform",
    "title": "DevOps platform",
    "audience": "Engineers building and running delivery platforms — the people who will operate Kubernetes and hand it to other teams",
    "prerequisites": [],
    "steps": [
      {
        "title": "Define an internal developer platform",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/define-an-internal-developer-platform.html",
        "why": "Everything later in this path is one layer of the product named here: a curated, supported set of capabilities offered to delivery teams as self-service. Opening on the definition keeps the Linux, container, and cluster chapters reading as what the platform is made of, rather than a tour of unrelated tools."
      },
      {
        "title": "Diagnose a cgroup resource limit problem",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/cgroups-resource-isolation.html",
        "why": "The first promise a platform makes is bounded resources per tenant, and cgroups are the kernel mechanism that keeps it — container limits, cluster quotas, and fleet capacity envelopes are all cgroup controls in different clothes. The throttling-versus-utilisation gap taught here is the reading every later resource step assumes."
      },
      {
        "title": "Govern a Linux security baseline without blocking delivery",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/linux-security-baseline.html",
        "why": "Before tenants arrive, the substrate they will share needs a hardening story. This step also introduces the pattern the whole path reuses at every layer — a versioned baseline, a threat rationale per control, exceptions with an owner and an expiry — on the most familiar ground available: Linux hosts."
      },
      {
        "title": "Define a Linux fleet lifecycle standard",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/fleet-os-lifecycle.html",
        "why": "The baseline defined what every host must conform to; this step sets the fleet in motion. Image provenance, patch SLAs, staged promotion with rollback images, and published decision rights turn the static baseline into a lifecycle, using the same canary-and-batch motion the delivery chapter later applies to software."
      },
      {
        "title": "Distinguish a container image from a running container",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/container-image-and-runtime.html",
        "why": "The path now drops from the fleet to the artifact every tenant submits. The image-versus-running-container distinction — read-only layers, one thin writable layer, and why that layer is not persistence — is the packaging contract the platform standardises, and the base-image program at the end of this chapter governs exactly it."
      },
      {
        "title": "Apply CPU and memory constraints to a container",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/resource-constraints.html",
        "why": "The cgroup theory from the opening chapter becomes per-container vocabulary: what a memory limit does on breach, what a CPU weight does and does not promise, and why defaults are not isolation. Placed before Kubernetes so requests, limits, and QoS later arrive as a scheduling translation of a mechanism already understood."
      },
      {
        "title": "Design a useful container health check",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/container-healthcheck-design.html",
        "why": "The second contract between tenant and platform: who decides a workload is healthy. Cheap deterministic checks, thresholds matched to startup, and the warning that a dependency-coupled probe turns an outage into mass restarts are precisely the failure the orchestrator probes and rollout steps below inherit, so the contract is set at the container layer first."
      },
      {
        "title": "Design a governed base-image program",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/platform-base-image-program.html",
        "why": "The container chapter's synthesis and the first full platform programme on the path: versioned base images with digest references, support windows, automated rebuilds that reach consumers as pull requests, and exceptions with expiry. It consumes the image identity from the start of the chapter and re-instantiates the fleet baseline pattern for artifacts."
      },
      {
        "title": "What /dev/kvm exposes to QEMU",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/what-dev-kvm-exposes.html",
        "why": "The isolation chapter this path enters next opens by contrasting containers with virtual machines, and that contrast only teaches once the virtual machine is concrete: an ordinary QEMU process that opens /dev/kvm, with the kernel executing guest instructions natively and handing control back only at exits it refuses to handle itself. Placed here, VMs and containers both resolve into processes on a shared host — the exact frame the isolation model argues from."
      },
      {
        "title": "Why virtio beats emulated devices",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/why-virtio-beats-emulated-devices.html",
        "why": "The previous step left one bill unpaid: guest code runs natively only until it touches a device, and every emulated-device access is a trap into slow translation. Virtio is the escape — a guest that knows it is virtualised and cooperates through paravirtual devices — and it sharpens the isolation contrast directly ahead: a container needs no virtio driver because it already runs against the host kernel's real interfaces, which is the shortest honest answer to how the two models differ."
      },
      {
        "title": "Explain the Linux primitives behind container isolation",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/container-isolation-basics.html",
        "why": "The platform must now say what a container actually defends. Namespaces, cgroups, and credentials layered onto an ordinary process — not a virtual machine — is the model every isolation decision in this chapter argues from, and its layered-not-absolute caveat is the honesty a multi-tenant platform owes its tenants."
      },
      {
        "title": "Apply Linux capabilities with least privilege",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/capabilities-least-privilege.html",
        "why": "The first concrete tenant demand — one privileged operation — and the mechanism for granting it without handing over the host. Start from the default set, drop, then add the single capability proved necessary; that review vocabulary is what the admission guardrails later automate at the API boundary."
      },
      {
        "title": "Explain user namespace UID and GID mapping",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/user-namespace-mapping.html",
        "why": "Extends capabilities with the strongest answer to the next tenant demand, a container that needs root: UID 0 inside mapping to an unprivileged host ID outside. Reading ownership, mounts, and capabilities against the mapping from both sides is exactly the check a platform runs before root-claiming images are allowed onto shared nodes."
      },
      {
        "title": "Choose runtime isolation tiers for a multi-tenant platform",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/tenant-isolation-strategy.html",
        "why": "The payoff of the isolation chapter: classify tenants by trust and escape impact, offer a constrained default tier with stronger tiers as priced exceptions, and admit a shared kernel cannot satisfy every adversarial model. This is the tier menu the cluster tenancy decision later in the path draws from."
      },
      {
        "title": "Read the essential parts of a Pod specification",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/pod-spec-basics.html",
        "why": "The Kubernetes chapter opens on the object tenants actually submit. Labels as the selector contract, containers with resources, probes, and security context, and why a bare Pod is nobody's production — the vocabulary that the requests, rollout, RBAC, and admission steps all read and write."
      },
      {
        "title": "Set Pod resource requests and limits",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/resource-requests-limits-and-qos.html",
        "why": "Resource limits return with cluster semantics: requests drive scheduling decisions, limits bound runtime, and the request/limit shape sets QoS class and eviction priority. The step only adds new knowledge because container-level limits are already in hand; what it contributes is the scheduler and the eviction order."
      },
      {
        "title": "Explain a Kubernetes Deployment rollout and rollback",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/deployment-rollout-and-rollback.html",
        "why": "Tenants do not ship Pods, they ship rollouts. maxSurge and maxUnavailable as capacity decisions, readiness gating traffic, and inspecting ReplicaSets and probe failures before rollback are the machinery progressive delivery later refines and cluster upgrades later depend on for drain capacity."
      },
      {
        "title": "Design least-privilege Kubernetes RBAC",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/rbac-least-privilege.html",
        "why": "Before the platform can enforce anything it must say who may act. Namespace-scoped bindings, the breadth hiding in list, watch, and secret reads, and workload identities kept separate from humans form the authorization layer that admission policy in the next step presumes and extends."
      },
      {
        "title": "Establish Kubernetes admission policy guardrails",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/admission-policy-and-guardrails.html",
        "why": "Where the platform's contract becomes executable: validate, mutate, or reject manifests at the API boundary so unsafe workloads never exist, staged warn-then-enforce, with CI pre-checks giving developers fast feedback. It is the Kubernetes instantiation of the versioned-baseline-plus-exceptions pattern established back on Linux hosts."
      },
      {
        "title": "Plan a production Kubernetes cluster upgrade",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/cluster-upgrade-strategy.html",
        "why": "Operating the cluster rather than only defending it: version-skew rules and API removals read before scheduling, node drains in small eviction batches that respect disruption budgets, distribution-specific rollback rehearsed in advance. The core-Kubernetes chapter closes on the recurring duty that otherwise becomes the platform's least-planned outage."
      },
      {
        "title": "Run a live migration you can trust",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/run-a-live-migration-you-trust.html",
        "why": "The upgrade step just evacuated nodes in small drain batches a disruption budget could absorb; this is the identical duty one layer down, where firmware maintenance must move a host's guests — often the cluster's own node VMs — without stopping them. Pre-copy convergence, dirty-page tracking, and a bounded downtime window are the VM fleet's drain-and-PDB machinery, so the step lands directly after the pattern it repeats."
      },
      {
        "title": "Choose a libvirt CPU mode for a fleet",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/choose-a-libvirt-cpu-mode.html",
        "why": "Migration as taught in the previous step silently assumes the target host can serve the exact CPU the guest booted with. This step turns that assumption into a fleet template decision — host-passthrough, host-model, or a named baseline — because on hardware that refreshes unevenly the wrong mode surfaces only as the 3 a.m. migration failure, which is why it belongs immediately after the step that created the tension."
      },
      {
        "title": "Pin a latency-sensitive VM to NUMA and hugepages",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/pin-a-vm-to-numa-and-hugepages.html",
        "why": "From fleet compatibility to one latency-sensitive guest: cross-socket memory hops and 4 kB page churn, not hypervisor overhead, are where VM jitter is usually born, and NUMA pinning with hugepages is the host-level answer. It follows the CPU-mode step because both buy performance by constraining placement, and every pin this step adds is a migration the two steps above must be re-checked against."
      },
      {
        "title": "Set an honest overcommit policy for a VM fleet",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/set-an-honest-overcommit-policy.html",
        "why": "The tuning steps above asked what one VM may demand; this staff step asks what the fleet may honestly promise. Overcommit ratios become per-tier contracts exactly as container requests and limits became QoS classes in the cluster chapter, and the willingness to say which tiers are never packed is the capacity honesty the platform-SLO step near the path's end publishes outward, closing the VM fleet chapter as a contract rather than a ratio."
      },
      {
        "title": "Explain a container network namespace",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/container-network-namespace.html",
        "why": "The network chapter restarts at the primitive the isolation chapter used: a namespace holding interfaces, addresses, routes, and sockets. Inspecting from the correct namespace — a listener on the host is not a listener in the container — is the habit the traffic-tracing and policy steps below demand."
      },
      {
        "title": "Trace Kubernetes Service traffic",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/kubernetes-service-traffic-path.html",
        "why": "The platform operator's canonical traffic question, asked before anything is broken: selector, to ready endpoints, to implementation-specific dataplane. A Service name that resolves while having zero usable backends is the tenant-visible failure this step teaches you to explain, and it rehearses the readiness contract from the rollout step on network ground."
      },
      {
        "title": "Validate Kubernetes NetworkPolicy enforcement",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/network-policy-enforcement-limits.html",
        "why": "The isolation promise of the runtime chapter meets the network: default-deny only exists if the installed plugin enforces it, so capability is verified before policy is trusted. Staged allow-listing of DNS and required flows is how a platform introduces tenant segmentation without causing the outage it was meant to prevent."
      },
      {
        "title": "Define ingress and gateway boundaries",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/ingress-gateway-boundary.html",
        "why": "The front door every tenant shares. Deciding who owns listeners, certificates, TLS policy, and route delegation under Gateway API is an ownership migration, not a YAML rename, and it completes the in-cluster network story with the boundary teams outside the platform actually touch."
      },
      {
        "title": "Define multi-tenant Kubernetes platform boundaries",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/multi-tenant-platform-boundaries.html",
        "why": "The synthesis the cluster and network chapters were building toward: tenant trust, blast radius, and the honest trade-off between shared control planes and dedicated ones. It consumes the RBAC, admission, quota, and network-policy decisions of the previous ten steps to answer the founding question — can these teams share this cluster?"
      },
      {
        "title": "Design CI/CD quality gates for a service",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/pipeline-quality-gates.html",
        "why": "The delivery chapter opens inside the pipeline a tenant's commit triggers: deterministic checks before merge, scans treated as risk evidence rather than guarantees, and the warning that slow, flaky, unowned gates degrade into bypasses. Everything later in the chapter — artifacts, provenance, reconciliation — sits on the far side of these gates."
      },
      {
        "title": "Why should CI publish immutable release artifacts?",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/immutable-release-artifacts.html",
        "why": "Build once, promote the digest: the identity discipline the base-image program applied to foundations, applied to every release. It precedes GitOps deliberately, because a reconciler that restores the declared state is only trustworthy when the state names immutable content instead of a mutable tag."
      },
      {
        "title": "Design software supply-chain controls",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/software-supply-chain-controls.html",
        "why": "Extends artifact identity into proof: signed provenance binding the digest to a trusted builder, source revision, and declared inputs, verified before promotion. It sits here rather than in a security chapter because the control point is the delivery pipeline the previous two steps built, and its break-glass path is a platform interface."
      },
      {
        "title": "Explain the four GitOps principles",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/gitops-principles.html",
        "why": "Names the operating model the platform hands to tenants: declarative desired state, versioned and immutable, pulled by agents, continuously reconciled. Learning the four principles as properties — and what each partial adoption still costs — is what turns the next step's push-versus-pull choice into an engineering decision."
      },
      {
        "title": "Choose a pull-based reconciler or a push-based deployment pipeline",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/gitops-pull-versus-push-delivery.html",
        "why": "The design decision itself: pull agents remove thirty sets of cluster credentials from CI, and where the reconciler runs decides whether one hub outage halts every cluster at once. It needs the principles first — otherwise a reconciler is just another deploy tool — and it makes drift the daily consequence."
      },
      {
        "title": "Respond to Argo CD drift without masking an incident",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/argo-cd-reconciliation-drift.html",
        "why": "Reconciliation's sharp edge, and the platform's version of a 3am change: an operator's emergency edit now registers as drift. Classify the change before reverting it, make the durable fix in Git, and never normalise blind resync — the discipline the infrastructure and host drift steps later in the path reuse."
      },
      {
        "title": "Establish organization-wide delivery standards",
        "theme": "ci-cd",
        "difficulty": "staff",
        "href": "questions/ci-cd/platform-delivery-standards.html",
        "why": "The delivery chapter's synthesis: publish the paved path as versioned workflows with provenance requirements, measured lead time, change-failure rate, and gate reliability, and exceptions that expire. This is where CI/CD stops being per-team tooling and becomes the capability the founding definition promised."
      },
      {
        "title": "Why does Terraform use state?",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/terraform-state-purpose.html",
        "why": "The infrastructure chapter opens on the component that makes declarative infrastructure possible: state as the address-to-resource mapping, remote backends with locking, and the sensitivity of saved plans. Plan review and drift governance both presume state is owned, protected, and never directly edited."
      },
      {
        "title": "Review a Terraform plan before production apply",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/terraform-plan-review.html",
        "why": "The infrastructure change contract: the plan is built from the same reviewed configuration, variables, and provider versions production will use, every create, replace, and destroy inspected, and the reviewed plan applied promptly or re-planned. It is the twin of the delivery chapter's merge gates — evidence reviewed before an irreversible action."
      },
      {
        "title": "Govern infrastructure drift at organization scale",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-drift-governance.html",
        "why": "Transplants the Argo CD drift lesson to infrastructure at organisation scale: scheduled read-only plan checks routed to owning teams, time-bounded emergency changes with an auditable record, and no auto-apply of every detected difference. This is what keeps GitOps honesty from ending at the cluster boundary."
      },
      {
        "title": "Design safe configuration drift remediation",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/configuration-drift-remediation.html",
        "why": "The drift thread's last layer, host configuration, carries the invariant every reconciler above silently assumed: classify before converging, because overwriting an unrecorded emergency repair repeats the outage it fixed. With this step, declared state has been taught across workloads, infrastructure, and hosts."
      },
      {
        "title": "Explain a paved road and a golden path",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/explain-a-paved-road-and-a-golden-path.html",
        "why": "The product chapter reopens with the vocabulary for everything the technical chapters built: the paved road as the supported, opinionated route the platform keeps working, deliberately distinct from rules that bind everyone. The road-versus-rule distinction reframes the admission guardrails from the cluster chapter as kindness rather than control."
      },
      {
        "title": "Offer self-service with safe defaults",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/offer-self-service-with-safe-defaults.html",
        "why": "The mechanism that makes a road real: intent to a working, compliant result with no human in the platform queue, defaults the platform would defend in review, and escape hatches that cost something. Every default it lists — limits, probes, log pipelines, network policy — is a contract earlier chapters already taught."
      },
      {
        "title": "Deliver secure platform defaults at scale",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/secure-platform-defaults.html",
        "why": "Security lands exactly where security decisions are made: the secure path must also be the easy path or shadow platforms appear. Templates that provision identity, secrets, TLS, and provenance by default, with risky choices made explicit and reviewable — the paved road instantiated for security rather than bolted on afterwards."
      },
      {
        "title": "Publish platform SLOs and a support model",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/publish-platform-slos-and-a-support-model.html",
        "why": "The handover contract: per-capability objectives measured where developers experience them, control-plane and data-plane promises stated separately, and a support model with tiers, hours, and escalation. A team that operates Kubernetes but publishes no promises gives its tenants nothing they can depend on."
      },
      {
        "title": "Measure platform adoption",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/measure-platform-adoption.html",
        "why": "Before defending the investment, learn what a number can and cannot say: workloads on the road and activity flowing through it rather than teams-once-onboarded, denominators stated, and mandated adoption worth nothing as evidence. This is the honest instrument the closing step must quote, or be dismissed as advocacy."
      },
      {
        "title": "Justify continued platform investment",
        "theme": "platform-engineering",
        "difficulty": "staff",
        "href": "questions/platform-engineering/justify-continued-platform-investment.html",
        "why": "The final step because it consumes every other: cost avoided by standardisation, capability previously impossible, risk reduced — each with its own evidence, cohorts instead of a counterfactual, and the platform's own price included. The path ends where it began, on the platform as a product, now with the case that keeps it funded."
      }
    ]
  },
  {
    "slug": "backend",
    "title": "Backend engineering",
    "audience": "Backend engineers preparing for systems-design and operational interview rounds",
    "prerequisites": [],
    "steps": [
      {
        "title": "Design a stateless backend service",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/stateless-service-design.html",
        "why": "The whole path is about what happens to state once it leaves the request process, so it opens by naming that premise: durable state lives in a database, an object store, or a managed cache, and any healthy instance can serve any request. Every later pattern — transaction, cache, queue, saga — is coordination between those external stores."
      },
      {
        "title": "Choose synchronous versus asynchronous API processing",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/synchronous-versus-asynchronous-api.html",
        "why": "With the premise set, the first real design decision is the fork every backend faces: answer synchronously inside the caller's latency expectation, or accept the work and expose a status resource. The queueing, outbox, and saga stages all live on the asynchronous branch, so the reader must choose the branch before the machinery for it can make sense."
      },
      {
        "title": "Explain database transaction boundaries",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/transaction-basics.html",
        "why": "The asynchronous branch still ends in a database, so fix the unit of atomicity before anything complicates it: related changes commit or roll back together and the boundary matches one business operation. Its closing note — side effects outside the database need their own design — is a deliberate forward pointer to both the idempotency stage and the outbox."
      },
      {
        "title": "Choose a transaction boundary",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/transaction-boundaries.html",
        "why": "Restates that definition at the level of one backend request: validate first, keep the atomic core short, commit, and only then trigger slow external effects. Its central claim — a transaction cannot atomically include an email, an HTTP call, or a broker publish — is the exact gap the outbox stage later fills, which is why the gap must be met here and not at the end of the path."
      },
      {
        "title": "Select a PostgreSQL transaction isolation level",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/isolation-level-selection.html",
        "why": "A boundary is only meaningful once concurrent writers are in the picture. This step forces the reader to derive isolation from an invariant — do not oversell inventory — rather than from a preferred label, and it plants a habit the whole spine reuses: a rejected transaction is retried as a whole unit, and the unit must stay short enough that retrying it is affordable."
      },
      {
        "title": "Choose timeouts, retries, and backoff",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/timeouts-retries-backoff.html",
        "why": "The path now leaves the single database and calls a remote dependency, and the first thing failure costs is time. Deadlines come from a measured end-to-end budget and retries target only demonstrably transient failures — and the caveat that a retry must be safe to repeat is left deliberately hanging, because the next two steps exist to satisfy it."
      },
      {
        "title": "Make a retried write idempotent",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/idempotent-operations.html",
        "why": "Answers the hanging caveat: a timeout means the caller lacks an answer, not that the server did nothing, so a repeated write needs a stable client-generated key persisted atomically with the effect and returned as the prior outcome on retry. This is the first spine concept in full, and the queueing stage will reintroduce it later as duplicate delivery."
      },
      {
        "title": "Implement idempotency keys for mutations",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/idempotency-keys.html",
        "why": "Turns the concept into a production contract for a payment-like mutation: key scope bound to the authenticated caller, retention and expiry, a deterministic conflict response when the same key arrives with changed parameters, and the record coupled transactionally to the business write. It sits directly after the concept it operationalises and directly before the proxy layer whose retries depend on such keys existing."
      },
      {
        "title": "Set reverse-proxy timeouts from a request budget",
        "theme": "web-servers",
        "difficulty": "middle",
        "href": "questions/web-servers/proxy-timeout-budget.html",
        "why": "Individual retries are now safe; this step makes the edge's arithmetic add up. Connect, send, and read timeouts are allocations from the caller's end-to-end objective rather than independent knobs, and a deadline that is never propagated is one the upstream cannot honour — the discipline that keeps a slow upstream from becoming an amplified outage."
      },
      {
        "title": "Make upstream retries safe at a proxy",
        "theme": "web-servers",
        "difficulty": "senior",
        "href": "questions/web-servers/upstream-retry-safety.html",
        "why": "The proxy itself now wants to retry, and the question is when it may. The answer — only operations known to be safe to repeat or protected by an idempotency-key replay contract — is undecidable without the two steps above it, and placed there it reads as applying that vocabulary to the one layer that retries without the application ever knowing."
      },
      {
        "title": "Use a circuit breaker without masking failure",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/circuit-breakers.html",
        "why": "Retries and proxy budgets discipline one request; the breaker disciplines the population. It comes after both because its failure modes are their failure modes scaled up — synchronised half-open probes, an open circuit quietly hiding a long outage — and because a declared degraded response only means something once the caller's own retry behaviour is already bounded."
      },
      {
        "title": "Shed load to preserve a critical service",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/load-shedding.html",
        "why": "Closes the failure stage by turning the lens around: the breaker protects an unhealthy dependency, but shedding protects this service when demand exceeds safe capacity. Ranking requests by business importance and rejecting low-value work early needs the admission signals — queue depth, concurrency, dependency latency — that every previous step in the stage instrumented."
      },
      {
        "title": "Explain cache-aside basics",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/cache-aside-basics.html",
        "why": "The path now adds its first deliberately replicated state. Cache-aside is the pattern most backends actually run, and its answer guide carries the two facts the rest of the stage leans on: delete on write rather than update, and a concurrent read and write can repopulate a stale value that nothing in the pattern itself prevents — which is why the TTL step must come next."
      },
      {
        "title": "Choose a TTL for a cached value",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/ttl-selection-basics.html",
        "why": "The repopulation race cannot be fixed inside the pattern, so the mitigation is a bound: the TTL is the explicit contract for how wrong a value may be and for how long. Placed before keys, invalidation, and stampedes, it teaches that every later cache mechanism tightens or backs up this contract rather than replacing it."
      },
      {
        "title": "Design cache keys safely",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-key-design.html",
        "why": "Before any invalidation cleverness, the cache must not become a data leak. Keys carry the tenant boundary, the representation version, and every input that materially changes the response, because a shared key that crosses a privacy boundary is the one cache bug no consistency model repairs. It sits between mechanics and policy because policy built on unsafe keys is wasted work."
      },
      {
        "title": "Design cache invalidation policy",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-invalidation-policy.html",
        "why": "The hard problem of the stage, and it needs what came before: invalidation that is remembered rather than derived fails the moment a fourth reader adds a fourth key, so the policy is declared dependency sets, deletion from the write path that owns the data, and versioned keys as the alternative that makes invalidation atomic. The TTL bound from earlier remains the backstop when an invalidation is lost."
      },
      {
        "title": "Prevent a cache stampede",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-stampede-control.html",
        "why": "Only now does the stampede question make sense, because a stampede is what the invalidation and TTL model produces when a popular entry expires for every requester at once. Request coalescing, stale-while-revalidate, and expiry jitter treat it as the capacity event it is — a reader who met synchronized expiry through the previous steps diagnoses the burst instead of complaining that the database got slow."
      },
      {
        "title": "Evaluate cache consistency trade-offs",
        "theme": "caching",
        "difficulty": "senior",
        "href": "questions/caching/cache-consistency-tradeoffs.html",
        "why": "Closes the cache stage by naming what the whole stage really was: a second copy of state with its own update path. Bounded staleness and read-your-writes are separable promises with different costs, and the stale profile name in this question is a read-your-writes violation, not a staleness one — the exact distinction the replication-lag and read-your-writes steps later need, which is why the consistency stage starts from this bridge."
      },
      {
        "title": "Choose a work queue or an event log",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/choose-a-queue-or-log.html",
        "why": "The asynchronous branch chosen near the start now gets its transport decision: competing-consumer work queue or append-only event log. The distinction decides everything downstream — whether messages are deleted on consumption or replayable, which ordering is possible, and why an outbox relay can safely retry publication — so it must precede the mechanics built on top of it."
      },
      {
        "title": "Explain at-most-once, at-least-once, and exactly-once claims",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/explain-delivery-semantics.html",
        "why": "Delivery semantics are end-to-end properties of producer, broker, and consumer, and an exactly-once claim is incomplete for any external side effect. It follows the platform choice and precedes the Kafka mechanics because it re-derives the idempotency argument from earlier at system scale: the broker's guarantee stops at the consumer, and the effect is the reader's problem again."
      },
      {
        "title": "Explain Kafka topics and partitions",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/explain-kafka-topics-and-partitions.html",
        "why": "The concrete unit of the log platform: a partition is both the unit of parallelism and the entire scope of ordering, and ordering does not exist across partitions. Stated on its own it becomes a premise the next two steps immediately exercise; buried inside them it would be trivia."
      },
      {
        "title": "Preserve required ordering in asynchronous processing",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/preserve-order-in-async-processing.html",
        "why": "Applies the partition premise to a real requirement: events for one order process in sequence while different orders proceed in parallel. Keying by aggregate, serialising per partition, and versioning events is the first place ordering and idempotency explicitly meet — the idempotent transitions that make replay safe are doing quiet load-bearing work from the earlier idempotency steps."
      },
      {
        "title": "Commit Kafka offsets after processing effects",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/commit-kafka-offsets-after-effects.html",
        "why": "The smallest possible dual-write: one consumer, one external database, two commits that cannot be atomic. Committing the offset before the effect loses work permanently; committing after permits replay that repeats it — and the escape hatch this question names, an idempotency key or an outbox, is the next stage in full. Meeting the miniature first makes the general pattern feel inevitable rather than clever."
      },
      {
        "title": "Consume an at-least-once event stream safely",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/at-least-once-delivery.html",
        "why": "Generalises the offset problem to any at-least-once transport: assume duplicates after a crash or rebalance, deduplicate on a durable key, commit the position only after the effect is recorded, and choose that atomic boundary deliberately. It is the last step before the outbox because its own resolution is the outbox — the pattern has been earned before it is named."
      },
      {
        "title": "Apply the transactional outbox pattern",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/outbox-pattern.html",
        "why": "The spine's centrepiece, and it resolves the tension the path built on purpose: the business change and its event must become atomic, so both are written in one database transaction and a separate relay publishes later. It lands after transaction boundaries, idempotency, and the offset miniature because each is a premise of the design and of its honest limit — consumers still see duplicates."
      },
      {
        "title": "Use a transactional outbox for event publication",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/transactional-outbox.html",
        "why": "The operational sequel, because an outbox that is only designed is an unbounded table and an unmonitored relay. Relay ownership, age and backlog metrics, replay and poison-event handling, and the refusal to claim exactly-once delivery are what turn the previous step's diagram into a service someone can run — the operational-round half of the same question."
      },
      {
        "title": "Coordinate a multi-service saga",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/saga-compensation.html",
        "why": "One service's dual-write is now solved; the multi-service workflow is not, and this is where a global transaction is deliberately given up. Local transactions plus compensating actions — a business reversal, never a database rollback — with orchestration versus choreography chosen for visibility. It follows the outbox because the saga's steps communicate through exactly the events the outbox guarantees."
      },
      {
        "title": "Coordinate a saga with compensations",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/saga-compensation.html",
        "why": "Deepens the saga into an operable contract: correlation identity and durable state so a failover resumes rather than infers progress, compensations written as idempotent commands, and an explicit operator path for the indeterminate outcome — because a shipped item cannot be un-shipped. The honest close of this summit is admitting which effects cannot be undone, out loud, in the design."
      },
      {
        "title": "Explain consistency and availability during a network partition",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/consistency-and-availability.html",
        "why": "With eventual consistency now running through the reader's own hands, the trade-off question finally has a referent. A partition forces an explicit safety decision, availability is a per-operation and per-replica statement rather than a global adjective, and an unsafe fail-open leader is the concrete split-brain disaster. Before the outbox this was theory; after it, it is a description of the reader's system."
      },
      {
        "title": "Design a quorum for replicated writes",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/quorum-basics.html",
        "why": "The mechanism underneath the partition decision: every successful read quorum must intersect every successful write quorum, and the intersection is what carries the committed position. It follows the trade-off step because rejecting writes without quorum is only a defensible policy once the reader can compute why the intersection keeps two successful operations from disagreeing."
      },
      {
        "title": "Use fencing tokens to prevent stale writers",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/fencing-tokens.html",
        "why": "Quorums govern membership, but a stale writer that resumes after a failover still believes it owns the work. A monotonically increasing token, checked at the point of side effect, is the write-side complement to the idempotency that opened the spine: duplicates are made harmless, and late writers are made visible and rejectable."
      },
      {
        "title": "Diagnose replication lag",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/replication-lag.html",
        "why": "Consistency trade-offs have a practical face, and it is lag: measured as backlog and replay position rather than wall-clock age, staged through transport, durable write, and replay, and diagnosed against what the primary was doing. This is the operational diagnosis that makes the next step's user-facing promise implementable rather than aspirational."
      },
      {
        "title": "Provide read-your-writes consistency",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/read-your-writes.html",
        "why": "The promise extracted from lag: return a replication position with the write and refuse that session a read from a replica behind it. It is the same separable promise the cache-consistency step established on the cache side — bounded staleness for everyone, read-your-writes for the writer — now implemented across replicas, which is why that bridge step stood where it did."
      },
      {
        "title": "Choose a linearizable read",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/linearizable-read.html",
        "why": "The top of the read-guarantee ladder: a lock check, a quota, or a leadership decision before a destructive action must reflect the latest committed state, and that costs quorum or leader contact and its latency. It closes the consistency stage because choosing this expensive read is only rational after the reader can say exactly which reads do not need it."
      },
      {
        "title": "Explain the serverless function execution model",
        "theme": "serverless",
        "difficulty": "junior",
        "href": "questions/serverless/explain-serverless-execution-model.html",
        "why": "The path now replays its spine on the compute model that removes the safety net: instances appear and vanish between requests and nothing survives in the process. That is the stateless premise from the opening step with no in-flight guarantees and no implicit deduplication left, which is why the execution model is restated here rather than explained at the start."
      },
      {
        "title": "Explain synchronous and asynchronous serverless invocation",
        "theme": "serverless",
        "difficulty": "junior",
        "href": "questions/serverless/explain-invocation-delivery-semantics.html",
        "why": "On this platform the retry decision partly belongs to the infrastructure: asynchronous invocations are retried by the platform, so duplicates arrive by design rather than by accident. It re-derives the delivery-semantics argument from the queueing stage in a setting where the retry budget is invisible — the reason the next step is mandatory rather than optional."
      },
      {
        "title": "Design idempotent serverless event processing",
        "theme": "serverless",
        "difficulty": "senior",
        "href": "questions/serverless/design-idempotent-serverless-events.html",
        "why": "The spine's first concept returns as the senior version of itself: the event identifier and the business operation are separate keys, an idempotency record is created with an atomic conditional write before any irreversible effect, and a duplicate returns the prior result. Everything between the early idempotency steps and here is what makes this design routine instead of heroic."
      },
      {
        "title": "Adopt consumer-driven contracts",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/consumer-driven-contracts.html",
        "why": "The path has built boundaries — APIs, events, the outbox, the saga — and this is how they are verified without a shared staging environment. Consumer-driven contracts record what each client actually reads and replay every pact against the provider, replacing the integration free-for-all that event-driven systems otherwise produce. It can only arrive after the boundaries exist, because before then it has nothing to test."
      },
      {
        "title": "Diagnose missing trace context across services",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/propagate-trace-context.html",
        "why": "The last skill is diagnosing the machinery itself, and the first casualty of an event-driven design is trace context: a span dies at the broker unless identifiers travel through the payloads, and the outbox relay, the saga steps, and the serverless consumer each start a fresh trace otherwise. The design-time contracts came first; this is their runtime complement."
      },
      {
        "title": "Establish data-integrity controls across services",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/data-integrity.html",
        "why": "The capstone, because it is the one question that consumes the whole spine at once: end-to-end integrity across services is idempotency keys, transaction boundaries, the outbox, saga compensation, fencing, and reconciliation — chosen per data class, owned, and auditable. The path ends where a staff interview begins: not one pattern, but a justified portfolio of them."
      }
    ]
  }
];

window.studyOrders = [
  {
    "theme": "advanced-containers",
    "note": "Isolation primitives first and platform programmes last: the order builds from the kernel mechanisms a container actually defends with to the incidents and governance that spend them.",
    "steps": [
      {
        "title": "Explain the Linux primitives behind container isolation",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/container-isolation-basics.html",
        "why": "Namespaces and cgroups layered onto an ordinary process are the model every isolation decision in this Theme argues from."
      },
      {
        "title": "Explain mount namespaces and a container root filesystem",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/mount-namespace-basics.html",
        "why": "The mount namespace holds the container's root filesystem, so it comes directly after the primitives that define what a container is."
      },
      {
        "title": "Explain PID namespaces and container process visibility",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/pid-namespace-basics.html",
        "why": "PID namespaces explain why a container sees itself as process one and why host-side tools must name the namespace first."
      },
      {
        "title": "Design correct PID 1 signal handling in a container",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/pid-one-signal-handling.html",
        "why": "Signal handling only becomes a design problem once the PID namespace has made the container's first process special."
      },
      {
        "title": "Explain a container network namespace",
        "theme": "advanced-containers",
        "difficulty": "junior",
        "href": "questions/advanced-containers/network-namespace-basics.html",
        "why": "The network namespace completes the isolation picture with interfaces, addresses, and sockets of the container's own."
      },
      {
        "title": "Decide when containers should share a namespace",
        "theme": "advanced-containers",
        "difficulty": "senior",
        "href": "questions/advanced-containers/namespace-sharing-tradeoffs.html",
        "why": "With all three namespaces understood, sharing any of them becomes an informed trade-off rather than a convenience."
      },
      {
        "title": "Explain cgroup resource accounting for containers",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/cgroup-resource-accounting.html",
        "why": "Cgroups move from model to measurement: what the kernel charges the container for CPU, memory, and I/O."
      },
      {
        "title": "Diagnose cgroup CPU throttling in a container",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/cpu-quotas-and-throttling.html",
        "why": "CPU quota throttling is the first accounting figure operators actually feel, and it misreads without the accounting model before it."
      },
      {
        "title": "Investigate a container cgroup memory limit and OOM kill",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/memory-limits-and-oom.html",
        "why": "Memory limits fail differently from CPU quotas, and the OOM kill inside a cgroup is only legible with the accounting in hand."
      },
      {
        "title": "Use the cgroup PIDs controller to contain fork storms",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/pids-controller-protection.html",
        "why": "The PIDs controller bounds the one resource a fork storm spends, completing the cgroup controls before migrating them."
      },
      {
        "title": "Lead a cgroup v2 migration for container hosts",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/cgroup-v2-migration.html",
        "why": "Migrating hosts to cgroup v2 is safe only once the accounting, throttling, and controllers it reshuffles are understood."
      },
      {
        "title": "Explain overlay filesystem copy-up and container writes",
        "theme": "advanced-containers",
        "difficulty": "senior",
        "href": "questions/advanced-containers/overlay-filesystem-copy-up.html",
        "why": "Copy-up explains where container writes actually land, the filesystem fact every runtime tier below builds on."
      },
      {
        "title": "Apply Linux capabilities with least privilege",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/capabilities-least-privilege.html",
        "why": "Dropping capabilities is the first concrete narrowing of what a container may ask its host's kernel to do."
      },
      {
        "title": "Control device access for a container workload",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/device-access-control.html",
        "why": "Device rules govern the kernel interface underneath the capabilities, the second thing least privilege must bound."
      },
      {
        "title": "Design a seccomp profile for a container workload",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/seccomp-profile-design.html",
        "why": "Seccomp filters the syscall surface itself, the deepest of the three hardening mechanisms and last for that reason."
      },
      {
        "title": "Run a workload with a read-only root filesystem",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/readonly-root-filesystem.html",
        "why": "A read-only root filesystem turns the copy-up and mount knowledge above into an enforced runtime policy."
      },
      {
        "title": "Explain user namespace UID and GID mapping",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/user-namespace-mapping.html",
        "why": "UID mapping is the strongest answer to a container that needs root, and it presumes the capability and mount tiers before it."
      },
      {
        "title": "Evaluate rootless container runtime boundaries",
        "theme": "advanced-containers",
        "difficulty": "middle",
        "href": "questions/advanced-containers/rootless-runtime-boundaries.html",
        "why": "Rootless operation composes every namespace and capability lesson into a whole runtime, and its limits read only then."
      },
      {
        "title": "Choose runtime isolation tiers for a multi-tenant platform",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/tenant-isolation-strategy.html",
        "why": "Tiered isolation for multi-tenant platforms spends the whole primitive tier deciding what each tier of tenant may risk."
      },
      {
        "title": "Establish a container runtime hardening baseline",
        "theme": "advanced-containers",
        "difficulty": "senior",
        "href": "questions/advanced-containers/runtime-hardening-baseline.html",
        "why": "A baseline turns per-mechanism hardening into a versioned standard the exceptions below are measured against."
      },
      {
        "title": "Review a privileged-container exception",
        "theme": "advanced-containers",
        "difficulty": "senior",
        "href": "questions/advanced-containers/privileged-container-exception.html",
        "why": "Reviewing a privileged exception is the baseline applied to the one workload that refuses to meet it."
      },
      {
        "title": "Govern runtime-isolation exceptions across an organization",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/runtime-exception-governance.html",
        "why": "Governing exceptions across an organization replaces folklore with owners, expiry dates, and records."
      },
      {
        "title": "Set a multi-year container runtime isolation roadmap",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/runtime-isolation-roadmap.html",
        "why": "A multi-year roadmap prices the isolation tiers the platform will owe as its workloads and adversaries mature."
      },
      {
        "title": "Respond to a suspected container escape",
        "theme": "advanced-containers",
        "difficulty": "senior",
        "href": "questions/advanced-containers/container-escape-incident.html",
        "why": "The escape response is the incident face of everything above: what was claimed, what held, and what to preserve."
      },
      {
        "title": "Design container-host incident readiness for isolation failures",
        "theme": "advanced-containers",
        "difficulty": "staff",
        "href": "questions/advanced-containers/container-host-incident-readiness.html",
        "why": "Readiness design closes the Theme by making escape response a rehearsed platform capability instead of improvisation."
      }
    ]
  },
  {
    "theme": "backend-architecture",
    "note": "The reading spine walks the backend path first — stateless service, the API fork, the transaction sequence — before widening to the boundary questions and the portfolio tier that presupposes a running system.",
    "steps": [
      {
        "title": "Design a stateless backend service",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/stateless-service-design.html",
        "why": "The spine opens by naming what stays out of the request process, because every later pattern coordinates state that already left."
      },
      {
        "title": "Choose synchronous versus asynchronous API processing",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/synchronous-versus-asynchronous-api.html",
        "why": "The synchronous-asynchronous fork is the first real design decision, and the queueing and outbox stages live on its asynchronous branch."
      },
      {
        "title": "Design resource-oriented HTTP endpoints",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/rest-resource-semantics.html",
        "why": "Resource-oriented endpoints settle the API surface before its failure modes arrive."
      },
      {
        "title": "Separate authentication from authorization",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/authentication-authorization-boundary.html",
        "why": "Separating authentication from authorization completes the surface and prevents the conflation the boundary questions would inherit."
      },
      {
        "title": "Choose a transaction boundary",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/transaction-boundaries.html",
        "why": "The transaction sequence starts here because the unit it defines is what retries and idempotency keys repeat."
      },
      {
        "title": "Make backend retries safe",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/retry-backoff-and-jitter.html",
        "why": "A retry is only affordable once the unit it repeats is short, which is exactly why boundaries come first."
      },
      {
        "title": "Implement idempotency keys for mutations",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/idempotency-keys.html",
        "why": "Keys turn safe retries into a production contract for mutations, directly after the retry discipline they serve."
      },
      {
        "title": "Use a transactional outbox for event publication",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/transactional-outbox.html",
        "why": "The outbox only makes sense once you have felt the dual-write it fixes, so it follows boundaries, retries, and keys."
      },
      {
        "title": "Coordinate a saga with compensations",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/saga-compensation.html",
        "why": "Compensation extends atomicity across services and presumes the outbox's guaranteed events as its transport."
      },
      {
        "title": "Operate a circuit breaker",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/circuit-breaker-operations.html",
        "why": "Operating the breaker after the retries it judges keeps the operator honest about what it masks."
      },
      {
        "title": "Explain the role of an API gateway",
        "theme": "backend-architecture",
        "difficulty": "junior",
        "href": "questions/backend-architecture/api-gateway-basics.html",
        "why": "The gateway is the first boundary question, consuming the API surface settled at the start of the spine."
      },
      {
        "title": "Govern API versioning and deprecation",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/api-versioning-policy.html",
        "why": "Versioning and deprecation govern how the surface may change without breaking the contracts above."
      },
      {
        "title": "Design an API rate-limiting policy",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/rate-limiting-policy.html",
        "why": "Rate limiting protects the settled surface under load, a policy question once gateway and versioning exist."
      },
      {
        "title": "Design cursor pagination",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/cursor-pagination.html",
        "why": "Cursor pagination fixes the one read pattern offset paging quietly breaks at scale."
      },
      {
        "title": "Design multi-tenant isolation",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/multi-tenancy-isolation.html",
        "why": "Tenant isolation widens the boundary questions from per-request correctness to per-customer state."
      },
      {
        "title": "Design a durable background job contract",
        "theme": "backend-architecture",
        "difficulty": "middle",
        "href": "questions/backend-architecture/background-job-contract.html",
        "why": "The durable background job gives the asynchronous fork from step two its own operable contract."
      },
      {
        "title": "Design a developer-portal catalog contract teams can trust",
        "theme": "backend-architecture",
        "difficulty": "staff",
        "href": "questions/backend-architecture/developer-portal-catalog-contract.html",
        "why": "The catalog makes service boundaries discoverable, which only matters once those boundaries exist to publish."
      },
      {
        "title": "Decompose a monolith without a rewrite",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/monolith-decomposition.html",
        "why": "Decomposition opens the portfolio tier by re-cutting a running system along the seams the spine taught."
      },
      {
        "title": "Set platform and product-service boundaries",
        "theme": "backend-architecture",
        "difficulty": "staff",
        "href": "questions/backend-architecture/platform-boundary-strategy.html",
        "why": "Platform and product-service boundaries decide which side of each seam owns what, after decomposition shows what bad seams cost."
      },
      {
        "title": "Design cache invalidation for mutable data",
        "theme": "backend-architecture",
        "difficulty": "senior",
        "href": "questions/backend-architecture/cache-invalidation-strategy.html",
        "why": "Invalidation for mutable data is the hardest boundary to hold and presumes the seam that owns the data."
      },
      {
        "title": "Manage an architecture decision portfolio",
        "theme": "backend-architecture",
        "difficulty": "staff",
        "href": "questions/backend-architecture/architecture-decision-portfolio.html",
        "why": "A decision portfolio governs the record of choices the tiers above kept making implicitly."
      },
      {
        "title": "Govern evolutionary backend architecture",
        "theme": "backend-architecture",
        "difficulty": "staff",
        "href": "questions/backend-architecture/evolutionary-architecture-governance.html",
        "why": "Evolutionary governance makes change itself a managed process rather than a series of surprises."
      },
      {
        "title": "Prioritize backend resilience investments",
        "theme": "backend-architecture",
        "difficulty": "staff",
        "href": "questions/backend-architecture/resilience-investment-model.html",
        "why": "Prioritizing resilience investments is last because it prices everything the Theme has built."
      }
    ]
  },
  {
    "theme": "caching",
    "note": "Placement, TTL, and hit ratio come before invalidation and stampedes because every later mechanism tightens or backs up the contract a bound on wrongness sets.",
    "steps": [
      {
        "title": "Compare cache placement layers",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/cache-placement-layers.html",
        "why": "Where the copy lives is the first of the three decisions every caching question ultimately reduces to."
      },
      {
        "title": "Explain cache-aside basics",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/cache-aside-basics.html",
        "why": "Cache-aside is the pattern most services actually run, so it anchors the mechanics tier before any variation."
      },
      {
        "title": "Explain a read-through cache",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/read-through-cache-basics.html",
        "why": "Read-through is the managed counterpoint, and the difference between them only teaches when placed side by side."
      },
      {
        "title": "Choose a TTL for a cached value",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/ttl-selection-basics.html",
        "why": "The TTL is the explicit contract for how wrong a value may be and for how long, set before keys or invalidation tighten it."
      },
      {
        "title": "Interpret a cache hit ratio honestly",
        "theme": "caching",
        "difficulty": "junior",
        "href": "questions/caching/cache-hit-ratio-basics.html",
        "why": "Reading a hit ratio honestly calibrates the mechanics before the policy questions arrive."
      },
      {
        "title": "Design cache keys safely",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-key-design.html",
        "why": "Keys carry the tenant and representation boundaries, so they precede invalidation — policy built on unsafe keys is wasted work."
      },
      {
        "title": "Design cache invalidation policy",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-invalidation-policy.html",
        "why": "Invalidation is the hard problem, and it needs safe keys and the TTL backstop already in place."
      },
      {
        "title": "Choose a cache eviction policy",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-eviction-policy.html",
        "why": "Eviction governs what the cache keeps when memory runs out, the mechanical sibling of invalidation."
      },
      {
        "title": "Prevent a cache stampede",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/cache-stampede-control.html",
        "why": "A stampede is what the invalidation and TTL model produces at expiry, so it follows them directly."
      },
      {
        "title": "Cache negative results safely",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/negative-caching.html",
        "why": "Caching failures and misses extends the same wrongness contract to values that are absent."
      },
      {
        "title": "Tune Redis maxmemory and eviction behaviour",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/redis-maxmemory-tuning.html",
        "why": "Redis under memory pressure is where the operational tier starts, because eviction becomes an incident when maxmemory is wrong."
      },
      {
        "title": "Operate Redis replication and failover for a cache tier",
        "theme": "caching",
        "difficulty": "senior",
        "href": "questions/caching/redis-failover-operations.html",
        "why": "Failover is the cache tier's outage rehearsal, and it presumes the tuning that shaped its steady state."
      },
      {
        "title": "Operate Memcached memory and slab allocation",
        "theme": "caching",
        "difficulty": "middle",
        "href": "questions/caching/memcached-slab-tuning.html",
        "why": "Memcached's slab allocator is the counter-example that keeps Redis habits from hardening into folklore."
      },
      {
        "title": "Design cache coherence across regions",
        "theme": "caching",
        "difficulty": "staff",
        "href": "questions/caching/multi-region-cache-coherence.html",
        "why": "Multi-region coherence widens every earlier contract across distance and replication."
      },
      {
        "title": "Build a cache capacity and cost model",
        "theme": "caching",
        "difficulty": "staff",
        "href": "questions/caching/cache-capacity-cost-model.html",
        "why": "The capacity and cost model prices the tier the coherence question just made global."
      },
      {
        "title": "Set SLOs that survive a degraded cache",
        "theme": "caching",
        "difficulty": "staff",
        "href": "questions/caching/cache-slo-degradation-policy.html",
        "why": "SLOs that survive a degraded cache promise the degradation the tiers above rehearsed."
      },
      {
        "title": "Govern a shared cache platform",
        "theme": "caching",
        "difficulty": "staff",
        "href": "questions/caching/shared-cache-platform-governance.html",
        "why": "Governing a shared cache platform is the close, because a cache other teams depend on is a product."
      }
    ]
  },
  {
    "theme": "certification-last-minute-review",
    "note": "Read this Theme as a rehearsal, in roughly the order the exam weights the platform, from the Pod outward through the surrounding services to the runbooks and the two meta-questions that run the last week.",
    "steps": [
      {
        "title": "Read Pod phase, container state, and restart evidence",
        "theme": "certification-last-minute-review",
        "difficulty": "junior",
        "href": "questions/certification-last-minute-review/pod-lifecycle-signals.html",
        "why": "The exam weights the Pod first, and phase, container state, and restart evidence are how every scenario item opens."
      },
      {
        "title": "Select startup, readiness, and liveness probes",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/probe-selection.html",
        "why": "Probes decide restart evidence before any surrounding service can be blamed for it."
      },
      {
        "title": "Explain requests, limits, QoS, and a Pending Pod",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/resource-requests-limits.html",
        "why": "Requests, limits, and QoS explain the Pending Pod that scenario items love to hide."
      },
      {
        "title": "Review a Pod security context for least privilege",
        "theme": "certification-last-minute-review",
        "difficulty": "senior",
        "href": "questions/certification-last-minute-review/security-context-review.html",
        "why": "The security context review completes the Pod-level opening the exam always starts from."
      },
      {
        "title": "Choose ConfigMaps and Secrets without overstating protection",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/configmap-secret-boundaries.html",
        "why": "ConfigMaps versus Secrets is the first layer around the Pod, and scenario items fail here far more often than at exotic ones."
      },
      {
        "title": "Debug a Service with no reachable backends",
        "theme": "certification-last-minute-review",
        "difficulty": "junior",
        "href": "questions/certification-last-minute-review/service-endpoints-debug.html",
        "why": "The Service with no reachable backends is the canonical scenario failure at the service layer."
      },
      {
        "title": "Debug Kubernetes DNS before changing application code",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/dns-debugging.html",
        "why": "DNS debugging recurs inside Kubernetes with harder symptoms than the host version ever shows."
      },
      {
        "title": "Reason about NetworkPolicy enforcement and default deny",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/networkpolicy-semantics.html",
        "why": "Default deny and enforcement semantics decide whether the isolation the exam describes actually exists."
      },
      {
        "title": "Diagnose an RBAC denial without broadening access",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/rbac-least-privilege.html",
        "why": "The RBAC denial without broadening access is the last surrounding layer and the easiest one to flunk."
      },
      {
        "title": "Combine node selectors, affinity, taints, and tolerations",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/scheduling-constraints.html",
        "why": "Scheduling comes before storage and control-plane items because a Pending PVC presumes placement reasoning already works."
      },
      {
        "title": "Use PodDisruptionBudgets without blocking maintenance",
        "theme": "certification-last-minute-review",
        "difficulty": "senior",
        "href": "questions/certification-last-minute-review/pod-disruption-budget.html",
        "why": "Disruption budgets complete the scheduling story for the voluntary disruptions the exam asks about."
      },
      {
        "title": "Debug a PersistentVolumeClaim that stays Pending",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/pvc-binding.html",
        "why": "The Pending PVC is the storage item the scheduling tier just made legible."
      },
      {
        "title": "Triage an unavailable Kubernetes control plane",
        "theme": "certification-last-minute-review",
        "difficulty": "senior",
        "href": "questions/certification-last-minute-review/control-plane-triage.html",
        "why": "An unavailable control plane presumes you can already reason about where the workloads run."
      },
      {
        "title": "Operate Jobs and CronJobs without uncontrolled retries",
        "theme": "certification-last-minute-review",
        "difficulty": "middle",
        "href": "questions/certification-last-minute-review/job-cronjob-cleanup.html",
        "why": "Jobs and CronJobs without uncontrolled retries open the runbook set that converts knowledge into sequence."
      },
      {
        "title": "Plan and validate an etcd backup and restore",
        "theme": "certification-last-minute-review",
        "difficulty": "senior",
        "href": "questions/certification-last-minute-review/etcd-backup-restore.html",
        "why": "The etcd backup and restore is the runbook the exam trusts you can validate, not just describe."
      },
      {
        "title": "Build a safe Kubernetes cluster upgrade runbook",
        "theme": "certification-last-minute-review",
        "difficulty": "senior",
        "href": "questions/certification-last-minute-review/cluster-upgrade-runbook.html",
        "why": "The upgrade runbook spends the version-skew and drain discipline the runbook set just assembled."
      },
      {
        "title": "Evaluate a Kubernetes disaster-recovery exercise",
        "theme": "certification-last-minute-review",
        "difficulty": "staff",
        "href": "questions/certification-last-minute-review/staff-disaster-recovery-exercise.html",
        "why": "The disaster-recovery exercise converts the runbooks into a rehearsed motion with evidence."
      },
      {
        "title": "Lead a Kubernetes incident while preserving recovery options",
        "theme": "certification-last-minute-review",
        "difficulty": "staff",
        "href": "questions/certification-last-minute-review/staff-incident-command.html",
        "why": "Leading an incident while preserving recovery options is the runbook set's human tier."
      },
      {
        "title": "Prioritize certification review under a two-hour deadline",
        "theme": "certification-last-minute-review",
        "difficulty": "staff",
        "href": "questions/certification-last-minute-review/staff-certification-prioritization.html",
        "why": "The two-hour deadline question is how the last week before the exam should actually run."
      },
      {
        "title": "Keep certification preparation ethical and operationally useful",
        "theme": "certification-last-minute-review",
        "difficulty": "staff",
        "href": "questions/certification-last-minute-review/staff-certification-boundaries.html",
        "why": "Keeping preparation ethical closes the Theme because rehearsal that cheats the exam cheats the job."
      }
    ]
  },
  {
    "theme": "chaos-engineering",
    "note": "Definition and hypothesis before faults, faults before programmes: the order starts with what chaos engineering claims, ends with what it costs to run across many teams.",
    "steps": [
      {
        "title": "Define chaos engineering and what it is for",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/define-chaos-engineering.html",
        "why": "The definition, including why an experiment is not a test, anchors every experiment the Theme later runs."
      },
      {
        "title": "State a steady-state hypothesis",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/state-a-steady-state-hypothesis.html",
        "why": "An experiment needs a falsifiable steady-state claim before it needs a fault or a tool."
      },
      {
        "title": "Design a hypothesis-driven chaos experiment",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/design-a-hypothesis-driven-experiment.html",
        "why": "Designing the full experiment turns the hypothesis into a procedure with a written result."
      },
      {
        "title": "Control the blast radius of an experiment",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/control-the-blast-radius.html",
        "why": "Bounding the fault comes before injecting any, because every later fault assumes the bound holds."
      },
      {
        "title": "Abort a running chaos experiment",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/abort-a-running-experiment.html",
        "why": "Abort criteria are the other half of blast-radius control: what makes you stop."
      },
      {
        "title": "Simulate a downstream dependency failure",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/simulate-a-downstream-dependency-failure.html",
        "why": "A single dependency fault is the smallest experiment the bounds above can safely hold."
      },
      {
        "title": "Inject latency into a single dependency",
        "theme": "chaos-engineering",
        "difficulty": "junior",
        "href": "questions/chaos-engineering/inject-latency-into-a-dependency.html",
        "why": "Latency exposes the timeout and retry behaviour that hard failure hides completely."
      },
      {
        "title": "Inject packet loss and network partitions",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/inject-packet-loss-and-partitions.html",
        "why": "Packet loss and partitions add the partial failure shapes between latency and outright outage."
      },
      {
        "title": "Exhaust CPU and memory deliberately",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/exhaust-cpu-and-memory.html",
        "why": "Resource exhaustion moves the fault vocabulary from the network onto the host's own capacity."
      },
      {
        "title": "Exhaust disk space and file descriptors",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/exhaust-disk-and-file-descriptors.html",
        "why": "Disk and descriptor exhaustion complete the resource tier with slower and subtler saturation."
      },
      {
        "title": "Run pod-level chaos in Kubernetes",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/run-pod-level-chaos-in-kubernetes.html",
        "why": "Pod-level chaos applies the fault vocabulary to the platform most teams actually run."
      },
      {
        "title": "Terminate a node and verify real recovery",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/terminate-a-node-and-verify-recovery.html",
        "why": "Node termination verifies real recovery rather than a briefly green dashboard."
      },
      {
        "title": "Simulate an availability-zone or region failure",
        "theme": "chaos-engineering",
        "difficulty": "senior",
        "href": "questions/chaos-engineering/simulate-a-zone-or-region-failure.html",
        "why": "Zone failure is the widest blast radius the earlier bounds make survivable."
      },
      {
        "title": "Decide whether to experiment in production or staging",
        "theme": "chaos-engineering",
        "difficulty": "senior",
        "href": "questions/chaos-engineering/choose-production-or-staging.html",
        "why": "Production versus staging is a trade-off question that only exists once the faults themselves are known."
      },
      {
        "title": "Run data-layer chaos without risking the data",
        "theme": "chaos-engineering",
        "difficulty": "senior",
        "href": "questions/chaos-engineering/run-data-layer-chaos-safely.html",
        "why": "Data-layer risk deserves its own care tier after the compute and network tiers are rehearsed."
      },
      {
        "title": "Facilitate a game day",
        "theme": "chaos-engineering",
        "difficulty": "middle",
        "href": "questions/chaos-engineering/facilitate-a-game-day.html",
        "why": "Game days make experimentation a team practice rather than a solo technique."
      },
      {
        "title": "Select experiments from incident history",
        "theme": "chaos-engineering",
        "difficulty": "senior",
        "href": "questions/chaos-engineering/select-experiments-from-incident-history.html",
        "why": "Incident history chooses the next experiments better than curiosity ever does."
      },
      {
        "title": "Govern consent and ethics for production experiments",
        "theme": "chaos-engineering",
        "difficulty": "staff",
        "href": "questions/chaos-engineering/govern-consent-for-production-experiments.html",
        "why": "Consent and ethics govern who may run what in production, and with whose permission."
      },
      {
        "title": "Justify the cost of a chaos engineering programme",
        "theme": "chaos-engineering",
        "difficulty": "staff",
        "href": "questions/chaos-engineering/justify-the-cost-of-a-chaos-programme.html",
        "why": "Cost justification prices the programme the practice has by now become."
      },
      {
        "title": "Run a chaos engineering programme across many teams",
        "theme": "chaos-engineering",
        "difficulty": "staff",
        "href": "questions/chaos-engineering/run-a-chaos-engineering-programme.html",
        "why": "Running the programme across many teams is the governance capstone the whole order built toward."
      }
    ]
  },
  {
    "theme": "ci-cd",
    "note": "Read the pipeline before the deployment machinery, artifact identity before GitOps, reconciliation before progressive delivery — every later stage promotes something an earlier gate passed.",
    "steps": [
      {
        "title": "Choose CI pipeline triggers",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/trigger-a-pipeline.html",
        "why": "What triggers CI decides what every later gate and promotion reacts to."
      },
      {
        "title": "Design CI/CD quality gates for a service",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/pipeline-quality-gates.html",
        "why": "Gates prove things about a change, and everything later in the Theme is a promotion of something a gate passed."
      },
      {
        "title": "Parallelize a CI test suite safely",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/parallelize-test-suite.html",
        "why": "Safe test parallelization keeps the gate fast without making it blind."
      },
      {
        "title": "Handle flaky tests without masking regressions",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/retry-flaky-tests.html",
        "why": "Flaky-test handling preserves the gate's signal instead of masking regressions to keep it green."
      },
      {
        "title": "Triage a failed CI job from its logs",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/read-ci-logs.html",
        "why": "Triaging a failed job from its logs is the human skill the pipeline tier ends on."
      },
      {
        "title": "Why should CI publish immutable release artifacts?",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/immutable-release-artifacts.html",
        "why": "Artifact identity comes next because GitOps reconciliation only means something once declared state names a digest."
      },
      {
        "title": "Produce a traceable semantic-version release",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/semantic-version-release.html",
        "why": "Traceable semantic versions make the digest human-readable without ever replacing it."
      },
      {
        "title": "Verify supply-chain provenance before deployment",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/supply-chain-provenance.html",
        "why": "Provenance verification binds the artifact to a trusted builder, source revision, and declared inputs."
      },
      {
        "title": "Set artifact retention and promotion rules",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/artifact-retention-and-promotion.html",
        "why": "Retention and promotion rules decide how long that identity stays trustworthy across environments."
      },
      {
        "title": "Explain the four GitOps principles",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/gitops-principles.html",
        "why": "The four principles name the operating model the delivery machinery is about to adopt."
      },
      {
        "title": "Choose a pull-based reconciler or a push-based deployment pipeline",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/gitops-pull-versus-push-delivery.html",
        "why": "Pull versus push is a design decision rather than a preference, and it needs the principles first."
      },
      {
        "title": "Respond to Argo CD drift without masking an incident",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/argo-cd-reconciliation-drift.html",
        "why": "Responding to drift without masking an incident keeps reconciliation honest."
      },
      {
        "title": "Establish organization-wide delivery standards",
        "theme": "ci-cd",
        "difficulty": "staff",
        "href": "questions/ci-cd/platform-delivery-standards.html",
        "why": "Organization-wide delivery standards close the GitOps sequence by making it a paved path."
      },
      {
        "title": "Choose a progressive Argo Rollouts strategy",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/argo-rollouts-progressive-delivery.html",
        "why": "Progressive delivery comes after reconciliation because a rollout refines what the reconciler already guarantees."
      },
      {
        "title": "Define an Argo Rollouts AnalysisTemplate safely",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/argo-rollouts-analysis.html",
        "why": "AnalysisTemplates decide what evidence advances or stops the rollout strategies above."
      },
      {
        "title": "Decide whether to advance or stop a canary deployment",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/canary-deployment-decision.html",
        "why": "The advance-or-stop call is the judgement the AnalysisTemplate automates."
      },
      {
        "title": "Plan a blue-green production cutover",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/blue-green-cutover.html",
        "why": "Blue-green trades the gradual canary for a controlled instant switch."
      },
      {
        "title": "Design a deployment rollback",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/roll-back-a-deployment.html",
        "why": "Rollback design completes the delivery tier with the path every step above may one day need."
      },
      {
        "title": "Explain when to use Argo Workflows",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/argo-workflows-fundamentals.html",
        "why": "Argo Workflows extends the automation past deployment, and only after deployment itself is safe."
      },
      {
        "title": "Model failure and parallelism in an Argo Workflow DAG",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/argo-workflows-dag-failure.html",
        "why": "Modelling failure and parallelism in a DAG keeps the workflow honest under real load."
      },
      {
        "title": "Pass artifacts safely between Argo Workflow steps",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/argo-workflow-artifacts.html",
        "why": "Passing artifacts between steps carries the identity discipline up into orchestration."
      },
      {
        "title": "Reuse Argo Workflow templates without losing control",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/argo-workflow-template-reuse.html",
        "why": "Template reuse keeps the workflow fleet maintainable rather than copy-pasted."
      },
      {
        "title": "Explain the Argo Events event path",
        "theme": "ci-cd",
        "difficulty": "junior",
        "href": "questions/ci-cd/argo-events-architecture.html",
        "why": "The Argo Events event path explains what triggers the automation the workflows run."
      },
      {
        "title": "Design an Argo Events Sensor for a production trigger",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/argo-events-sensor-dependencies.html",
        "why": "Sensor dependencies make event triggers reliable enough to own in production."
      },
      {
        "title": "Design a multi-team pipeline architecture",
        "theme": "ci-cd",
        "difficulty": "staff",
        "href": "questions/ci-cd/multi-team-pipeline-architecture.html",
        "why": "Multi-team pipeline architecture opens the platform tier the whole tool tier serves."
      },
      {
        "title": "Choose reusable workflow boundaries",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/reusable-workflow-boundaries.html",
        "why": "Reusable workflow boundaries keep the shared pipelines composable across many teams."
      },
      {
        "title": "Protect deployment secrets in CI/CD",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/protect-deployment-secrets.html",
        "why": "Secrets protection is the first platform duty the shared machinery owes its tenants."
      },
      {
        "title": "Apply least privilege to a workflow token",
        "theme": "ci-cd",
        "difficulty": "middle",
        "href": "questions/ci-cd/least-privilege-workflow-token.html",
        "why": "Least-privilege tokens bound what the delivery automation itself may do."
      },
      {
        "title": "Build a CI/CD cost and capacity model",
        "theme": "ci-cd",
        "difficulty": "staff",
        "href": "questions/ci-cd/ci-cd-cost-capacity-model.html",
        "why": "The cost and capacity model prices the platform the teams now share."
      },
      {
        "title": "Decide whether to freeze deployments during an incident",
        "theme": "ci-cd",
        "difficulty": "senior",
        "href": "questions/ci-cd/incident-change-freeze.html",
        "why": "Freeze decisions during incidents connect delivery governance back to incident governance."
      },
      {
        "title": "Recover the delivery platform during an outage",
        "theme": "ci-cd",
        "difficulty": "staff",
        "href": "questions/ci-cd/disaster-recover-delivery-platform.html",
        "why": "Recovering the delivery platform itself during an outage is the failure the whole Theme rehearses for."
      }
    ]
  },
  {
    "theme": "cloud",
    "note": "Boundaries first, then the resilience rungs, then governance: the order follows how a workload lands in AWS and only afterwards how an organization governs many of them.",
    "steps": [
      {
        "title": "Choose an appropriate cloud service model",
        "theme": "cloud",
        "difficulty": "junior",
        "href": "questions/cloud/cloud-service-models.html",
        "why": "Service and shared-responsibility boundaries decide what the provider owes before anything is built."
      },
      {
        "title": "Explain the network boundaries of an AWS VPC",
        "theme": "cloud",
        "difficulty": "junior",
        "href": "questions/cloud/vpc-network-foundations.html",
        "why": "The VPC is the network boundary every later resource lands inside."
      },
      {
        "title": "Choose security groups and network ACLs deliberately",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/security-groups-and-network-acls.html",
        "why": "Security groups and network ACLs are the VPC's own traffic controls, learned beside the boundary they police."
      },
      {
        "title": "Provide controlled Internet egress from a private subnet",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/private-subnet-egress.html",
        "why": "Controlled egress from a private subnet completes the VPC story with the pattern most workloads need."
      },
      {
        "title": "Diagnose an unexpected AWS IAM authorization decision",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/iam-policy-evaluation.html",
        "why": "IAM policy evaluation explains the denials and grants every later permission puzzle reduces to."
      },
      {
        "title": "Apply least privilege to a cloud workload identity",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/least-privilege-workload-identity.html",
        "why": "Workload identity applies the evaluation model to machines rather than people."
      },
      {
        "title": "Rotate cloud workload secrets without an outage",
        "theme": "cloud",
        "difficulty": "senior",
        "href": "questions/cloud/secrets-manager-rotation.html",
        "why": "Rotating workload secrets without an outage operationalizes the identity tier's most dangerous credential."
      },
      {
        "title": "Choose Regions and Availability Zones for a workload",
        "theme": "cloud",
        "difficulty": "junior",
        "href": "questions/cloud/regions-and-availability-zones.html",
        "why": "Regions and zones are the fault domains the resilience tier is measured against."
      },
      {
        "title": "Design a cloud load-balancer health check",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/load-balancer-health-checks.html",
        "why": "Health checks decide how those fault domains hand traffic to healthy targets."
      },
      {
        "title": "Configure target-tracking autoscaling safely",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/autoscaling-target-tracking.html",
        "why": "Target-tracking autoscaling responds to demand inside the same fault domains."
      },
      {
        "title": "Prevent cloud service quotas from becoming an outage",
        "theme": "cloud",
        "difficulty": "senior",
        "href": "questions/cloud/cloud-quota-capacity-planning.html",
        "why": "Quota planning keeps the scaling tier's ceiling from becoming the outage."
      },
      {
        "title": "Design cloud disaster recovery from RTO and RPO",
        "theme": "cloud",
        "difficulty": "senior",
        "href": "questions/cloud/disaster-recovery-rto-rpo.html",
        "why": "RTO and RPO turn resilience from adjectives into numbers with owners."
      },
      {
        "title": "Set a cloud reliability strategy across product teams",
        "theme": "cloud",
        "difficulty": "staff",
        "href": "questions/cloud/cloud-reliability-strategy.html",
        "why": "The reliability strategy spends the whole resilience tier across product teams."
      },
      {
        "title": "Design a CloudWatch alarm that supports action",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/cloudwatch-alarm-design.html",
        "why": "Alarm design makes the resilience work observable and actionable."
      },
      {
        "title": "Prove a managed database backup can be restored",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/managed-database-backup-restore.html",
        "why": "A managed backup only counts once its restore has actually been proven."
      },
      {
        "title": "Choose object storage for durable application data",
        "theme": "cloud",
        "difficulty": "junior",
        "href": "questions/cloud/object-storage-durability.html",
        "why": "Durability design decides which data the recovery tier can lean on."
      },
      {
        "title": "Use CloudTrail as audit evidence during a change investigation",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/cloudtrail-audit-evidence.html",
        "why": "CloudTrail is the evidence an investigation reads after the tiers above have acted."
      },
      {
        "title": "Lead an AWS workload incident response",
        "theme": "cloud",
        "difficulty": "senior",
        "href": "questions/cloud/cloud-incident-response.html",
        "why": "Incident response spends the observability, recovery, and evidence tiers in one motion."
      },
      {
        "title": "Define AWS multi-account boundaries",
        "theme": "cloud",
        "difficulty": "middle",
        "href": "questions/cloud/multi-account-boundaries.html",
        "why": "Account boundaries are the governance tier's unit of isolation."
      },
      {
        "title": "Establish a governed cloud landing zone",
        "theme": "cloud",
        "difficulty": "staff",
        "href": "questions/cloud/landing-zone-governance.html",
        "why": "The landing zone makes those boundaries a governed default rather than an aspiration."
      },
      {
        "title": "Design a cloud resource tagging strategy",
        "theme": "cloud",
        "difficulty": "junior",
        "href": "questions/cloud/resource-tagging-strategy.html",
        "why": "Tagging is the metadata every cost and governance decision keys on."
      },
      {
        "title": "Establish cloud cost governance without blocking delivery",
        "theme": "cloud",
        "difficulty": "staff",
        "href": "questions/cloud/cloud-finops-governance.html",
        "why": "FinOps governance prices the platform without blocking the delivery it exists for."
      },
      {
        "title": "Govern data classification in cloud services",
        "theme": "cloud",
        "difficulty": "staff",
        "href": "questions/cloud/data-classification-governance.html",
        "why": "Data classification decides the handling rules the platform must enforce."
      },
      {
        "title": "Govern cloud identity at organization scale",
        "theme": "cloud",
        "difficulty": "staff",
        "href": "questions/cloud/cloud-identity-governance.html",
        "why": "Organization-wide identity governance closes the Theme at the scale the opening tiers never reached."
      }
    ]
  },
  {
    "theme": "configuration-management",
    "note": "Vocabulary before idempotence, idempotence before fleet safety, fleet safety before strategy, and drift remediation last because classify-before-converging only lands on someone who has seen what unrecorded changes cost.",
    "steps": [
      {
        "title": "Explain an Ansible inventory and host groups",
        "theme": "configuration-management",
        "difficulty": "junior",
        "href": "questions/configuration-management/ansible-inventory-basics.html",
        "why": "Inventory and host groups are the vocabulary every remaining Question in the Theme leans on."
      },
      {
        "title": "Explain plays, tasks, and modules in Ansible",
        "theme": "configuration-management",
        "difficulty": "junior",
        "href": "questions/configuration-management/ansible-playbook-basics.html",
        "why": "Plays, tasks, and modules run against the inventory the Theme has just defined."
      },
      {
        "title": "Deliver a configuration file with an Ansible template",
        "theme": "configuration-management",
        "difficulty": "junior",
        "href": "questions/configuration-management/ansible-templates.html",
        "why": "Templates deliver the first configuration content the plays must manage reproducibly."
      },
      {
        "title": "Use Ansible handlers for service reloads",
        "theme": "configuration-management",
        "difficulty": "junior",
        "href": "questions/configuration-management/ansible-handlers.html",
        "why": "Handlers sequence reloads so template changes take effect exactly once."
      },
      {
        "title": "Use Ansible variables without creating precedence surprises",
        "theme": "configuration-management",
        "difficulty": "junior",
        "href": "questions/configuration-management/ansible-variables-basics.html",
        "why": "Variables parameterize the plays without creating precedence surprises."
      },
      {
        "title": "Gather and use Ansible facts deliberately",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-facts.html",
        "why": "Facts let the playbook reason about the host it is about to change."
      },
      {
        "title": "Target Ansible tasks with tags safely",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-tags.html",
        "why": "Tags target subsets of the vocabulary once the whole play has grown."
      },
      {
        "title": "Explain idempotence in an Ansible playbook",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-idempotence.html",
        "why": "Idempotence makes re-runs meaningful, and it is the property everything after depends on."
      },
      {
        "title": "Validate an Ansible change with check and diff mode",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-check-diff.html",
        "why": "Check and diff mode validate a change, which is only interesting once a no-op re-run means something."
      },
      {
        "title": "Set safe Ansible concurrency for a fleet change",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/ansible-concurrency-limits.html",
        "why": "The fleet-safety tier widens in order, and concurrency limits bound the blast radius first."
      },
      {
        "title": "Perform an Ansible rolling configuration update",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-rolling-update.html",
        "why": "Rolling updates batch that blast radius across the inventory in waves."
      },
      {
        "title": "Coordinate a configuration change with Ansible delegation",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-delegation.html",
        "why": "Delegation widens where change happens by moving tasks to another host."
      },
      {
        "title": "Handle Ansible task failures without concealing drift",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-error-handling.html",
        "why": "Failure handling must not conceal drift, the widest blast radius of the four controls."
      },
      {
        "title": "Design a reusable Ansible role",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-role-design.html",
        "why": "Reusable roles open the craft tier with composition done deliberately."
      },
      {
        "title": "Pin and update Ansible collections safely",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/ansible-collection-pinning.html",
        "why": "Pinned collections keep those roles reproducible across fleets and across time."
      },
      {
        "title": "Build an Ansible content test strategy",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/ansible-test-strategy.html",
        "why": "A content test strategy treats the roles as the products they now are."
      },
      {
        "title": "Apply least privilege to Ansible privilege escalation",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/ansible-privilege-escalation.html",
        "why": "Least-privilege escalation bounds what the automation itself is allowed to do."
      },
      {
        "title": "Protect secrets used by Ansible automation",
        "theme": "configuration-management",
        "difficulty": "middle",
        "href": "questions/configuration-management/ansible-vault-secrets.html",
        "why": "Protected secrets close the craft tier with its most sensitive payload."
      },
      {
        "title": "Create a risk-based configuration change model",
        "theme": "configuration-management",
        "difficulty": "staff",
        "href": "questions/configuration-management/cm-change-risk-model.html",
        "why": "The risk-based change model opens strategy by pricing fleet changes."
      },
      {
        "title": "Define configuration ownership across a platform fleet",
        "theme": "configuration-management",
        "difficulty": "staff",
        "href": "questions/configuration-management/cm-fleet-ownership.html",
        "why": "Ownership decides who may change what across the fleet."
      },
      {
        "title": "Establish configuration-management platform guardrails",
        "theme": "configuration-management",
        "difficulty": "staff",
        "href": "questions/configuration-management/cm-platform-guardrails.html",
        "why": "Guardrails enforce the ownership model without blocking the teams it governs."
      },
      {
        "title": "Design resilience for a configuration-management control plane",
        "theme": "configuration-management",
        "difficulty": "staff",
        "href": "questions/configuration-management/cm-resilience-strategy.html",
        "why": "Control-plane resilience keeps the automation itself from becoming the outage."
      },
      {
        "title": "Standardize configuration management without blocking teams",
        "theme": "configuration-management",
        "difficulty": "staff",
        "href": "questions/configuration-management/cm-standardization-strategy.html",
        "why": "Standardizing without blocking teams is the strategy capstone the guardrails made possible."
      },
      {
        "title": "Design safe configuration drift remediation",
        "theme": "configuration-management",
        "difficulty": "senior",
        "href": "questions/configuration-management/configuration-drift-remediation.html",
        "why": "Drift remediation is last of all because classify-before-converging only lands on someone who has seen unrecorded changes cost an outage."
      }
    ]
  },
  {
    "theme": "container-networking",
    "note": "Start inside one container's namespace and finish at platform governance, because choosing a dataplane presumes knowing what it replaces.",
    "steps": [
      {
        "title": "Explain a container network namespace",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/container-network-namespace.html",
        "why": "The namespace is the vantage point you must inspect from before any driver or cluster layer makes sense."
      },
      {
        "title": "Explain Docker network drivers",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/network-driver-basics.html",
        "why": "Bridge, overlay, and host drivers are the first thing the namespace connects to."
      },
      {
        "title": "Use a user-defined bridge for service discovery",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/user-defined-bridge-dns.html",
        "why": "The user-defined bridge brings DNS-based service discovery to plain Docker networking."
      },
      {
        "title": "Design network aliases for service lifecycle",
        "theme": "container-networking",
        "difficulty": "middle",
        "href": "questions/container-networking/network-alias-lifecycle.html",
        "why": "Aliases make that discovery survive service lifecycle events rather than depend on coincidences."
      },
      {
        "title": "Distinguish EXPOSE from port publishing",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/expose-versus-publish.html",
        "why": "EXPOSE documents while publishing forwards, and confusing the two breaks the model early."
      },
      {
        "title": "Debug container DNS resolution",
        "theme": "container-networking",
        "difficulty": "junior",
        "href": "questions/container-networking/container-dns-resolution.html",
        "why": "Container DNS failures recur later in Kubernetes with harder symptoms, so they are debugged here first."
      },
      {
        "title": "Debug failed container egress",
        "theme": "container-networking",
        "difficulty": "middle",
        "href": "questions/container-networking/container-egress-debugging.html",
        "why": "Failed egress is the other pre-cluster failure the Theme insists you meet early."
      },
      {
        "title": "Trace Kubernetes Service traffic",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/kubernetes-service-traffic-path.html",
        "why": "A name that resolves with zero usable backends is the canonical tenant complaint, so Service traffic is traced early."
      },
      {
        "title": "Diagnose an MTU mismatch across container paths",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/mtu-mismatch-troubleshooting.html",
        "why": "MTU symptoms only become legible after the Service traces the Theme has just taught."
      },
      {
        "title": "Validate Kubernetes NetworkPolicy enforcement",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/network-policy-enforcement-limits.html",
        "why": "Default deny only exists if the installed plugin enforces it, so capability is verified before policy is trusted."
      },
      {
        "title": "Segment a multi-tier application with Docker networks",
        "theme": "container-networking",
        "difficulty": "middle",
        "href": "questions/container-networking/multi-network-segmentation.html",
        "why": "Multi-tier segmentation applies the verified policy to a real application topology."
      },
      {
        "title": "Define ingress and gateway boundaries",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/ingress-gateway-boundary.html",
        "why": "The gateway is about who owns the front door, a question that only opens after what-may-talk is settled."
      },
      {
        "title": "Explain Cilium's eBPF datapath trade-offs",
        "theme": "container-networking",
        "difficulty": "middle",
        "href": "questions/container-networking/cilium-ebpf-datapath-tradeoffs.html",
        "why": "The Cilium family opens with its dataplane, the replacement everything else in the family presumes."
      },
      {
        "title": "Evaluate Cilium kube-proxy replacement",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/cilium-kube-proxy-replacement.html",
        "why": "Replacing kube-proxy is the concrete trade the dataplane question frames."
      },
      {
        "title": "Apply Cilium identity-aware L7 network policy",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/cilium-l7-network-policy.html",
        "why": "Identity-aware L7 policy is what the eBPF dataplane uniquely buys."
      },
      {
        "title": "Design controlled egress with Cilium Egress Gateway",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/cilium-egress-gateway-design.html",
        "why": "Egress Gateway extends the identity model to outbound traffic."
      },
      {
        "title": "Advertise Kubernetes routes with Cilium BGP Control Plane",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/cilium-bgp-external-routing.html",
        "why": "BGP advertisement connects the cluster to the network that surrounds it."
      },
      {
        "title": "Prepare clusters for Cilium Cluster Mesh",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/cilium-clustermesh-prerequisites.html",
        "why": "Cluster Mesh presumes the dataplane and routing decisions made above it."
      },
      {
        "title": "Configure and troubleshoot a multi-interface Pod with Multus",
        "theme": "container-networking",
        "difficulty": "senior",
        "href": "questions/container-networking/multus-multi-interface-pod-troubleshooting.html",
        "why": "Multus adds per-Pod interfaces, the multi-network edge case after the Cilium core."
      },
      {
        "title": "Establish container network observability standards",
        "theme": "container-networking",
        "difficulty": "staff",
        "href": "questions/container-networking/network-observability-standard.html",
        "why": "Observability standards open the platform tier every tool family above must serve."
      },
      {
        "title": "Enable IPv6 container networking safely",
        "theme": "container-networking",
        "difficulty": "middle",
        "href": "questions/container-networking/ipv6-container-networking.html",
        "why": "IPv6 enablement is a platform programme the standards tier makes safe to attempt."
      },
      {
        "title": "Define a multi-cluster connectivity strategy",
        "theme": "container-networking",
        "difficulty": "staff",
        "href": "questions/container-networking/multi-cluster-connectivity-strategy.html",
        "why": "The multi-cluster strategy spends the single-cluster story across boundaries."
      },
      {
        "title": "Govern workload egress on a container platform",
        "theme": "container-networking",
        "difficulty": "staff",
        "href": "questions/container-networking/platform-egress-governance.html",
        "why": "Egress governance turns connectivity into policy with named owners."
      },
      {
        "title": "Govern high-risk container network changes",
        "theme": "container-networking",
        "difficulty": "staff",
        "href": "questions/container-networking/network-change-governance.html",
        "why": "High-risk change control keeps the platform's own network mutations survivable."
      },
      {
        "title": "Design container network security architecture",
        "theme": "container-networking",
        "difficulty": "staff",
        "href": "questions/container-networking/container-network-security-architecture.html",
        "why": "The security architecture closes the Theme by composing policy, identity, and boundaries into one design."
      }
    ]
  },
  {
    "theme": "containers",
    "note": "Artifact before lifecycle, lifecycle before constraints and probes, hardening before platform scope — each tier consumes the habits the previous one built.",
    "steps": [
      {
        "title": "Distinguish a container image from a running container",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/container-image-and-runtime.html",
        "why": "Image versus running container, read-only layers plus one writable layer, is the packaging fact everything else extends."
      },
      {
        "title": "Order a Dockerfile for safe cache reuse",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/build-cache-ordering.html",
        "why": "A Dockerfile ordered for safe cache reuse makes builds predictable enough to keep honest."
      },
      {
        "title": "Build a small runtime image with multi-stage builds",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/multi-stage-runtime-image.html",
        "why": "Multi-stage builds shrink the artifact the cache discipline just made predictable."
      },
      {
        "title": "Choose between CMD and ENTRYPOINT in a Docker image",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/cmd-and-entrypoint.html",
        "why": "CMD versus ENTRYPOINT decides what the image actually runs, the contract inside the artifact."
      },
      {
        "title": "Distinguish image tags from digests",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/image-tag-and-digest.html",
        "why": "Tags are names and digests are identity, so the artifact you run is the artifact you mean."
      },
      {
        "title": "Control Docker build context with .dockerignore",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/dockerfile-build-context.html",
        "why": "Build-context control keeps the build's inputs as small as its promises."
      },
      {
        "title": "Explain container lifecycle states and restart policy",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/container-lifecycle-states.html",
        "why": "Lifecycle follows artifact: states and restart policy define what the runtime does with the image."
      },
      {
        "title": "Investigate a container that exits immediately",
        "theme": "containers",
        "difficulty": "junior",
        "href": "questions/containers/inspect-container-failure.html",
        "why": "The immediately exiting container is the first lifecycle evidence you learn to read."
      },
      {
        "title": "Make a container stop gracefully",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/pid-one-and-graceful-shutdown.html",
        "why": "Graceful stops complete the lifecycle tier by making exit behaviour a contract."
      },
      {
        "title": "Triage a container service restart storm",
        "theme": "containers",
        "difficulty": "senior",
        "href": "questions/containers/container-incident-triage.html",
        "why": "The restart storm is what bad lifecycle configuration produces, diagnosed with the tiers above."
      },
      {
        "title": "Apply CPU and memory constraints to a container",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/resource-constraints.html",
        "why": "A limit is only sensible once the restart policy's verdict is understood, which is why constraints follow lifecycle."
      },
      {
        "title": "Design a useful container health check",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/container-healthcheck-design.html",
        "why": "A probe is a decision about who declares health, made after the runtime can act on that verdict."
      },
      {
        "title": "Run a containerized service as a non-root user",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/non-root-container.html",
        "why": "Hardening opens with the user: the service runs as non-root by default."
      },
      {
        "title": "Reduce Linux capabilities for a containerized service",
        "theme": "containers",
        "difficulty": "senior",
        "href": "questions/containers/container-capabilities-security.html",
        "why": "Dropped capabilities bound what even a non-root container may ask the kernel for."
      },
      {
        "title": "Evaluate Docker rootless mode for a build worker",
        "theme": "containers",
        "difficulty": "senior",
        "href": "questions/containers/rootless-mode-boundaries.html",
        "why": "Rootless mode removes the daemon's own privilege, and its limits read only with the tiers above."
      },
      {
        "title": "Define a container logging contract",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/container-logging-contract.html",
        "why": "The logging contract keeps the hardened runtime observable."
      },
      {
        "title": "Choose a Docker volume or a bind mount",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/volume-versus-bind-mount.html",
        "why": "Volumes versus bind mounts is the persistence decision the writable layer refused to be."
      },
      {
        "title": "Use a private dependency credential during an image build",
        "theme": "containers",
        "difficulty": "middle",
        "href": "questions/containers/build-secrets.html",
        "why": "Private build credentials close the hardening tier with the secret that must never reach the image."
      },
      {
        "title": "Design a governed base-image program",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/platform-base-image-program.html",
        "why": "The governed base-image program is the first full platform programme, consuming the artifact identity from the start."
      },
      {
        "title": "Maintain a base-image update policy",
        "theme": "containers",
        "difficulty": "senior",
        "href": "questions/containers/base-image-update-policy.html",
        "why": "The update policy keeps the program's images current without surprising its consumers."
      },
      {
        "title": "Build an image supply-chain control plane",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/image-supply-chain-control-plane.html",
        "why": "The supply-chain control plane makes provenance and promotion enforceable rather than aspirational."
      },
      {
        "title": "Release a multi-platform container image",
        "theme": "containers",
        "difficulty": "senior",
        "href": "questions/containers/multi-platform-image-release.html",
        "why": "Multi-platform releases extend the identity discipline across architectures."
      },
      {
        "title": "Set a container-platform cost and capacity model",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/container-platform-cost-model.html",
        "why": "The cost and capacity model prices the platform the program has become."
      },
      {
        "title": "Define tenant isolation boundaries for a container platform",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/tenant-isolation-boundaries.html",
        "why": "Tenant boundaries decide who may share the platform the tiers above just built."
      },
      {
        "title": "Lead a container runtime migration",
        "theme": "containers",
        "difficulty": "staff",
        "href": "questions/containers/container-runtime-migration.html",
        "why": "Runtime migration closes the Theme by changing the substrate underneath everything it taught."
      }
    ]
  },
  {
    "theme": "databases",
    "note": "Constraints and transactions before query plans, query plans before recovery — the order runs from the relational basics to keeping a production PostgreSQL alive.",
    "steps": [
      {
        "title": "Explain relational tables, keys, and constraints",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/relational-data-model-basics.html",
        "why": "Tables, keys, and constraints are the contract every later query, lock, and recovery presumes."
      },
      {
        "title": "Explain database transaction boundaries",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/transaction-basics.html",
        "why": "Transactions define the unit of atomicity before concurrency arrives to complicate it."
      },
      {
        "title": "Design least-privilege PostgreSQL roles",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/role-privilege-design.html",
        "why": "Least-privilege roles decide who may hold the power the transaction gives."
      },
      {
        "title": "Explain PostgreSQL connection authentication",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/connection-authentication-basics.html",
        "why": "Connection authentication is the door the roles and transactions sit behind."
      },
      {
        "title": "Read a basic PostgreSQL query plan",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/sql-query-plan-basics.html",
        "why": "Reading a query plan turns slow performance into evidence instead of folklore."
      },
      {
        "title": "Explain database index trade-offs",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/index-tradeoffs.html",
        "why": "Indexes are the plan's main lever, with write costs that must be priced rather than ignored."
      },
      {
        "title": "Triage PostgreSQL lock contention",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/lock-contention-triage.html",
        "why": "Lock contention is the concurrency face of the plans and indexes above."
      },
      {
        "title": "Diagnose long transactions in an MVCC database",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/mvcc-and-long-transactions.html",
        "why": "MVCC explains why long transactions poison even correctly indexed tables."
      },
      {
        "title": "Explain database backup and restore validation",
        "theme": "databases",
        "difficulty": "junior",
        "href": "questions/databases/backup-restore-basics.html",
        "why": "Backups open the durability tier, and only a validated restore makes them real."
      },
      {
        "title": "Design PostgreSQL point-in-time recovery",
        "theme": "databases",
        "difficulty": "senior",
        "href": "questions/databases/point-in-time-recovery-design.html",
        "why": "Point-in-time recovery bounds how much a restore can lose, the arithmetic the backup proved."
      },
      {
        "title": "Respond to PostgreSQL replication lag",
        "theme": "databases",
        "difficulty": "middle",
        "href": "questions/databases/replication-lag-response.html",
        "why": "Replication adds the read copies the failover tier will depend on."
      },
      {
        "title": "Design PostgreSQL high availability and failover",
        "theme": "databases",
        "difficulty": "senior",
        "href": "questions/databases/high-availability-failover.html",
        "why": "Failover spends the replication design on the day the primary dies."
      },
      {
        "title": "Govern capacity for a multi-team database platform",
        "theme": "databases",
        "difficulty": "staff",
        "href": "questions/databases/database-capacity-governance.html",
        "why": "Capacity governance prices a database platform shared by many teams."
      },
      {
        "title": "Plan a near-zero-downtime PostgreSQL major upgrade",
        "theme": "databases",
        "difficulty": "senior",
        "href": "questions/databases/zero-downtime-major-upgrade.html",
        "why": "The near-zero-downtime major upgrade is the durability tier's capstone, consuming replication, failover, and capacity at once."
      }
    ]
  },
  {
    "theme": "distributed-systems",
    "note": "This is the failure-and-consistency spine the backend and SRE paths share, and its order is earned rather than chosen.",
    "steps": [
      {
        "title": "Choose timeouts, retries, and backoff",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/timeouts-retries-backoff.html",
        "why": "Everything later either retries or survives a retried caller, so deadlines and backoff come first."
      },
      {
        "title": "Make a retried write idempotent",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/idempotent-operations.html",
        "why": "A retry is only safe advice when the repeated write is safe, so idempotency follows immediately."
      },
      {
        "title": "Use a circuit breaker without masking failure",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/circuit-breakers.html",
        "why": "The breaker protects the dependency the retries above would happily hammer."
      },
      {
        "title": "Shed load to preserve a critical service",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/load-shedding.html",
        "why": "Shedding closes the failure stage by protecting the service instead of the dependency."
      },
      {
        "title": "Design service discovery and client load balancing",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/service-discovery.html",
        "why": "Discovery with client load balancing earns its place once retries exist to hide transient failures."
      },
      {
        "title": "Consume an at-least-once event stream safely",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/at-least-once-delivery.html",
        "why": "Delivery opens the transport tier by assuming the duplicates the failure stage created."
      },
      {
        "title": "Operate a dead-letter queue",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/dead-letter-queues.html",
        "why": "Dead-lettering contains the poison messages the delivery tier now admits."
      },
      {
        "title": "Evolve an event schema safely",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/schema-evolution.html",
        "why": "Schema evolution keeps events flowing across versions of every producer and consumer."
      },
      {
        "title": "Apply the transactional outbox pattern",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/outbox-pattern.html",
        "why": "The outbox resolves the dual-write the transaction and delivery tiers exposed on purpose."
      },
      {
        "title": "Coordinate a multi-service saga",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/saga-compensation.html",
        "why": "Compensation extends the outbox's guarantees across multi-service workflows."
      },
      {
        "title": "Explain consistency and availability during a network partition",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/consistency-and-availability.html",
        "why": "The replication ladder opens with the partition decision every rung below hangs from."
      },
      {
        "title": "Explain safe leader election",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/leader-election.html",
        "why": "Leadership is the first mechanism the partition decision actually needs."
      },
      {
        "title": "Handle clock skew in a distributed service",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/clock-skew.html",
        "why": "Clock skew belongs at leader election because both are trust-in-coordination problems."
      },
      {
        "title": "Design a quorum for replicated writes",
        "theme": "distributed-systems",
        "difficulty": "junior",
        "href": "questions/distributed-systems/quorum-basics.html",
        "why": "Quorums carry the committed position through the membership the election produced."
      },
      {
        "title": "Use fencing tokens to prevent stale writers",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/fencing-tokens.html",
        "why": "Fencing makes the stale writer visible and rejectable at the point of side effect."
      },
      {
        "title": "Plan anti-entropy repair",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/anti-entropy-repair.html",
        "why": "Anti-entropy repair is the replication tier's own healing mechanism, defined against replication itself."
      },
      {
        "title": "Diagnose replication lag",
        "theme": "distributed-systems",
        "difficulty": "middle",
        "href": "questions/distributed-systems/replication-lag.html",
        "why": "Lag is the operational face of the replication the ladder just built."
      },
      {
        "title": "Provide read-your-writes consistency",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/read-your-writes.html",
        "why": "Read-your-writes is the user-facing promise extracted from measured lag."
      },
      {
        "title": "Choose a linearizable read",
        "theme": "distributed-systems",
        "difficulty": "senior",
        "href": "questions/distributed-systems/linearizable-read.html",
        "why": "The linearizable read tops the guarantee ladder and prices it honestly in latency."
      },
      {
        "title": "Design multi-region failover",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/multi-region-failover.html",
        "why": "The operational tier opens by spending the whole ladder across regions."
      },
      {
        "title": "Lead a cross-service consistency incident",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/incident-command.html",
        "why": "The cross-service consistency incident is the ladder breaking in public."
      },
      {
        "title": "Govern a high-risk distributed state change",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/change-safety.html",
        "why": "High-risk state changes govern the mutations the ladder made possible."
      },
      {
        "title": "Protect tenant fairness in a shared distributed platform",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/tenant-fairness.html",
        "why": "Tenant fairness protects the shared platforms the ladder now underpins."
      },
      {
        "title": "Establish data-integrity controls across services",
        "theme": "distributed-systems",
        "difficulty": "staff",
        "href": "questions/distributed-systems/data-integrity.html",
        "why": "End-to-end data-integrity controls are the staff capstone consuming every mechanism above at once."
      }
    ]
  },
  {
    "theme": "finops",
    "note": "The billing data model before allocation, allocation before optimisation, optimisation before the trade-offs a senior engineer is actually asked to make.",
    "steps": [
      {
        "title": "Read a cloud bill and find its drivers",
        "theme": "finops",
        "difficulty": "junior",
        "href": "questions/finops/read-a-cloud-bill-and-find-its-drivers.html",
        "why": "Line items, usage quantity versus rate, amortised versus unblended — the data model everything else reads."
      },
      {
        "title": "Normalise multi-cloud billing data with FOCUS",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/normalise-multi-cloud-billing-data-with-focus.html",
        "why": "FOCUS normalisation makes multi-cloud bills comparable before any analysis begins."
      },
      {
        "title": "Explain showback and chargeback",
        "theme": "finops",
        "difficulty": "junior",
        "href": "questions/finops/explain-showback-and-chargeback.html",
        "why": "Showback and chargeback are the vocabulary of allocation the billing model feeds."
      },
      {
        "title": "Allocate shared and untaggable cost",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/allocate-shared-and-untaggable-cost.html",
        "why": "Shared and untaggable cost is where honest allocation actually gets hard."
      },
      {
        "title": "Tag resources for cost allocation",
        "theme": "finops",
        "difficulty": "junior",
        "href": "questions/finops/tag-resources-for-cost-allocation.html",
        "why": "Tagging is the mechanism the whole allocation vocabulary depends on."
      },
      {
        "title": "Design account structure for cost visibility",
        "theme": "finops",
        "difficulty": "senior",
        "href": "questions/finops/design-account-structure-for-cost-visibility.html",
        "why": "Account structure decides whether the tags can even do their job."
      },
      {
        "title": "Rightsize overprovisioned compute",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/rightsize-overprovisioned-compute.html",
        "why": "Rightsizing is the first optimisation, and it presumes allocation that is already visible."
      },
      {
        "title": "Compare on-demand, committed, and spot pricing",
        "theme": "finops",
        "difficulty": "junior",
        "href": "questions/finops/compare-on-demand-committed-and-spot-pricing.html",
        "why": "On-demand, committed, and spot are the trade every commitment decision makes."
      },
      {
        "title": "Build a commitment discount portfolio",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/build-a-commitment-discount-portfolio.html",
        "why": "A portfolio prices commitment risk instead of chasing the maximum discount."
      },
      {
        "title": "Manage commitment risk on a changing fleet",
        "theme": "finops",
        "difficulty": "senior",
        "href": "questions/finops/manage-commitment-risk-on-a-changing-fleet.html",
        "why": "A changing fleet makes yesterday's commitments a liability to be managed."
      },
      {
        "title": "Run production work on spot capacity",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/run-production-work-on-spot-capacity.html",
        "why": "Spot strategy spends the pricing knowledge on work that genuinely tolerates eviction."
      },
      {
        "title": "Tier object storage with lifecycle rules",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/tier-object-storage-with-lifecycle-rules.html",
        "why": "Storage tiering is the same commitment logic applied to bytes."
      },
      {
        "title": "Trace an unexplained data transfer bill",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/trace-an-unexplained-data-transfer-bill.html",
        "why": "Egress archaeology closes the optimisation tier with its most surprising bill."
      },
      {
        "title": "Attribute Kubernetes cluster cost to teams",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/attribute-kubernetes-cluster-cost-to-teams.html",
        "why": "Kubernetes attribution extends allocation to where the bill is densest."
      },
      {
        "title": "Reclaim idle Kubernetes capacity",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/reclaim-idle-kubernetes-capacity.html",
        "why": "Idle capacity is the Kubernetes bill's silent majority."
      },
      {
        "title": "Tune autoscaling for cost and latency",
        "theme": "finops",
        "difficulty": "senior",
        "href": "questions/finops/tune-autoscaling-for-cost-and-latency.html",
        "why": "Autoscaling economics trade latency against spend with every step size."
      },
      {
        "title": "Set a cloud budget and alert",
        "theme": "finops",
        "difficulty": "junior",
        "href": "questions/finops/set-a-cloud-budget-and-alert.html",
        "why": "Budgets convert spend into a decision someone actually gets woken by."
      },
      {
        "title": "Investigate a cost anomaly alert",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/investigate-a-cost-anomaly-alert.html",
        "why": "Anomaly investigation is the budget alert's diagnostic sequel."
      },
      {
        "title": "Forecast next quarter cloud spend",
        "theme": "finops",
        "difficulty": "middle",
        "href": "questions/finops/forecast-next-quarter-cloud-spend.html",
        "why": "Forecasting makes the spend a plan rather than a quarterly surprise."
      },
      {
        "title": "Trade cost against reliability",
        "theme": "finops",
        "difficulty": "senior",
        "href": "questions/finops/trade-cost-against-reliability.html",
        "why": "The senior trade-offs open exactly where reliability and latency meet the bill."
      },
      {
        "title": "Weigh engineering time against infrastructure cost",
        "theme": "finops",
        "difficulty": "staff",
        "href": "questions/finops/weigh-engineering-time-against-infrastructure-cost.html",
        "why": "Engineering time is the other currency every optimisation above spent silently."
      },
      {
        "title": "Set incentives for cost accountability",
        "theme": "finops",
        "difficulty": "staff",
        "href": "questions/finops/set-incentives-for-cost-accountability.html",
        "why": "Incentives keep the practice honest when its metrics are gameable."
      },
      {
        "title": "Stand up a FinOps practice",
        "theme": "finops",
        "difficulty": "staff",
        "href": "questions/finops/stand-up-a-finops-practice.html",
        "why": "Standing up the practice is the organizational capstone the tiers above justify."
      }
    ]
  },
  {
    "theme": "hardware",
    "note": "Components before the diagnostics they produce, failures before the practice tier that instruments them, and lifecycle economics only once a fleet is trustworthy.",
    "steps": [
      {
        "title": "Explain the roles of core server components",
        "theme": "hardware",
        "difficulty": "junior",
        "href": "questions/hardware/server-component-basics.html",
        "why": "What CPU, memory, NIC, controller, and PSU each contribute: every later diagnostic is one of those components talking."
      },
      {
        "title": "Interpret disk health signals without overtrusting SMART",
        "theme": "hardware",
        "difficulty": "junior",
        "href": "questions/hardware/smart-health-basics.html",
        "why": "SMART is the disks speaking for themselves, interpreted without overtrusting a single score."
      },
      {
        "title": "Triage a degrading production disk",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/disk-failure-triage.html",
        "why": "A degrading production disk is the first triage the health signals above must support."
      },
      {
        "title": "Respond to a suspected storage-controller failure",
        "theme": "hardware",
        "difficulty": "senior",
        "href": "questions/hardware/storage-controller-failure-response.html",
        "why": "The suspected controller failure is the disk trio's confounder, so it comes last among them."
      },
      {
        "title": "Respond to corrected and uncorrected memory errors",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/ecc-memory-errors.html",
        "why": "Corrected and uncorrected memory errors complete the set of components that actually fail."
      },
      {
        "title": "Explain RAID redundancy and its limits",
        "theme": "hardware",
        "difficulty": "junior",
        "href": "questions/hardware/raid-redundancy-basics.html",
        "why": "RAID follows the disks directly because it exists to survive their failure."
      },
      {
        "title": "Operate safely during a RAID rebuild",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/raid-rebuild-safety.html",
        "why": "The rebuild question follows RAID because a rebuild is when a degraded array is most dangerous."
      },
      {
        "title": "Govern rack power and cooling capacity",
        "theme": "hardware",
        "difficulty": "staff",
        "href": "questions/hardware/rack-power-cooling-governance.html",
        "why": "Power and cooling are taken as one unit with the compute they serve because they fail together."
      },
      {
        "title": "Diagnose thermal throttling on a server",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/thermal-throttling-diagnosis.html",
        "why": "Thermal throttling is the power-and-cooling unit's performance symptom."
      },
      {
        "title": "Isolate a server network-interface fault",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/network-interface-fault-isolation.html",
        "why": "NIC fault isolation moves from chassis failures out to the network edge."
      },
      {
        "title": "Place a latency-sensitive workload on a NUMA server",
        "theme": "hardware",
        "difficulty": "senior",
        "href": "questions/hardware/numa-aware-workload-placement.html",
        "why": "NUMA placement is the topology question the component question quietly opened."
      },
      {
        "title": "Design a representative hardware performance benchmark",
        "theme": "hardware",
        "difficulty": "senior",
        "href": "questions/hardware/hardware-performance-benchmark.html",
        "why": "The practice tier opens with benchmarks that represent the workloads, after the failures they instrument."
      },
      {
        "title": "Build a hardware capacity baseline",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/hardware-capacity-baseline.html",
        "why": "The capacity baseline is what a benchmark becomes when it is kept honestly."
      },
      {
        "title": "Plan a production server firmware upgrade",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/firmware-upgrade-runbook.html",
        "why": "Firmware upgrades are the practice tier's riskiest routine."
      },
      {
        "title": "Govern firmware risk across a server fleet",
        "theme": "hardware",
        "difficulty": "staff",
        "href": "questions/hardware/fleet-firmware-governance.html",
        "why": "Fleet firmware governance prices that upgrade risk across every host at once."
      },
      {
        "title": "Use secure boot and platform attestation appropriately",
        "theme": "hardware",
        "difficulty": "senior",
        "href": "questions/hardware/secure-boot-attestation.html",
        "why": "Secure boot and attestation turn the boot chain into a measured supply chain."
      },
      {
        "title": "Validate redundant server power paths",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/redundant-power-validation.html",
        "why": "Redundant power paths are proven rather than assumed, which is why validation follows the design."
      },
      {
        "title": "Maintain a trustworthy server hardware inventory",
        "theme": "hardware",
        "difficulty": "junior",
        "href": "questions/hardware/asset-inventory-basics.html",
        "why": "Lifecycle economics open with an inventory worth trusting."
      },
      {
        "title": "Plan a hardware refresh without service interruption",
        "theme": "hardware",
        "difficulty": "senior",
        "href": "questions/hardware/hardware-refresh-migration.html",
        "why": "Refresh planning spends the inventory and the failure models together."
      },
      {
        "title": "Design spares and failure-domain strategy for physical infrastructure",
        "theme": "hardware",
        "difficulty": "staff",
        "href": "questions/hardware/spares-and-failure-domain-strategy.html",
        "why": "Spares and failure domains decide what any single failure is allowed to cost."
      },
      {
        "title": "Define a standard hardware platform without blocking product teams",
        "theme": "hardware",
        "difficulty": "staff",
        "href": "questions/hardware/platform-standardization.html",
        "why": "The standard hardware platform is the lifecycle answer to heterogeneous fleets."
      },
      {
        "title": "Recover access to an unreachable server without physical presence",
        "theme": "hardware",
        "difficulty": "middle",
        "href": "questions/hardware/out-of-band-server-recovery.html",
        "why": "Recovering an unreachable server without physical presence is the operational extreme the inventory enables."
      },
      {
        "title": "Plan graceful shutdown for loss of utility power",
        "theme": "hardware",
        "difficulty": "junior",
        "href": "questions/hardware/ups-graceful-shutdown.html",
        "why": "Graceful shutdown on lost utility power is the other operational extreme, and the Theme's close."
      }
    ]
  },
  {
    "theme": "infrastructure-as-code",
    "note": "State before language, language before module craft, surgery before the plan-review hinge, and drift governance last — the tier that makes IaC an organizational capability.",
    "steps": [
      {
        "title": "Why does Terraform use state?",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/terraform-state-purpose.html",
        "why": "Why Terraform keeps state turns backends, locking, and ownership into engineering rather than ritual."
      },
      {
        "title": "Handle Terraform state lock contention",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/state-lock-contention.html",
        "why": "Lock contention is the state model's operational failure mode, met before configuration begins."
      },
      {
        "title": "Explain a Terraform root module and resource address",
        "theme": "infrastructure-as-code",
        "difficulty": "junior",
        "href": "questions/infrastructure-as-code/terraform-configuration-basics.html",
        "why": "Root modules and resource addresses are the language tier the state maps onto."
      },
      {
        "title": "Define safe Terraform input variables",
        "theme": "infrastructure-as-code",
        "difficulty": "junior",
        "href": "questions/infrastructure-as-code/input-variables-and-validation.html",
        "why": "Safe input variables keep the language tier's interfaces honest at the boundary."
      },
      {
        "title": "Distinguish Terraform local values from data sources",
        "theme": "infrastructure-as-code",
        "difficulty": "junior",
        "href": "questions/infrastructure-as-code/local-values-and-data-sources.html",
        "why": "Local values versus data sources decides where each value should actually live."
      },
      {
        "title": "Choose for_each or count for repeated Terraform resources",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/for-each-versus-count.html",
        "why": "for_each versus count is the repetition decision every module below inherits."
      },
      {
        "title": "Model Terraform dependencies without overusing depends_on",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/explicit-dependencies.html",
        "why": "depends_on is a smell precisely when the language tier is properly understood."
      },
      {
        "title": "Design a stable Terraform module interface",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/module-interface-design.html",
        "why": "Module craft opens with stable interfaces, the product's front door."
      },
      {
        "title": "Treat shared Terraform modules as internal products",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-module-product-strategy.html",
        "why": "Shared modules are products, with users, versions, and support obligations."
      },
      {
        "title": "Design Terraform outputs without exposing secrets",
        "theme": "infrastructure-as-code",
        "difficulty": "junior",
        "href": "questions/infrastructure-as-code/output-contracts-and-sensitive-data.html",
        "why": "Outputs must not leak the secrets the modules handled safely internally."
      },
      {
        "title": "Pin Terraform provider dependencies safely",
        "theme": "infrastructure-as-code",
        "difficulty": "junior",
        "href": "questions/infrastructure-as-code/provider-version-pinning.html",
        "why": "Pinned providers keep the whole craft reproducible across time."
      },
      {
        "title": "Import an existing resource into Terraform",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/import-existing-infrastructure.html",
        "why": "The surgery set opens by bringing existing resources under management."
      },
      {
        "title": "Refactor Terraform resource addresses safely",
        "theme": "infrastructure-as-code",
        "difficulty": "senior",
        "href": "questions/infrastructure-as-code/safe-resource-refactoring.html",
        "why": "Refactoring resource addresses safely is the surgery the import made necessary."
      },
      {
        "title": "Use Terraform lifecycle rules without masking risk",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/resource-lifecycle-controls.html",
        "why": "Lifecycle rules must not mask the very risk the surgery tier exists to expose."
      },
      {
        "title": "Migrate Terraform state to a remote backend",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/remote-backend-migration.html",
        "why": "Migrating state to a remote backend completes the surgery with the state tier's opening promise."
      },
      {
        "title": "Review a Terraform plan before production apply",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/terraform-plan-review.html",
        "why": "The plan review is the hinge: the change contract, read after the language that produces plans and before anything that automates them."
      },
      {
        "title": "Build a Terraform testing strategy",
        "theme": "infrastructure-as-code",
        "difficulty": "senior",
        "href": "questions/infrastructure-as-code/terraform-test-strategy.html",
        "why": "Testing follows the hinge because tests generate and check exactly those plans."
      },
      {
        "title": "Design policy-as-code gates for Terraform delivery",
        "theme": "infrastructure-as-code",
        "difficulty": "senior",
        "href": "questions/infrastructure-as-code/policy-as-code-gates.html",
        "why": "Policy-as-code gates automate the review the hinge taught humans to perform."
      },
      {
        "title": "Isolate Terraform environments and blast radius",
        "theme": "infrastructure-as-code",
        "difficulty": "senior",
        "href": "questions/infrastructure-as-code/multi-environment-isolation.html",
        "why": "Environment isolation bounds the blast radius the automation above can reach."
      },
      {
        "title": "Plan a zero-downtime infrastructure migration with Terraform",
        "theme": "infrastructure-as-code",
        "difficulty": "senior",
        "href": "questions/infrastructure-as-code/zero-downtime-iac-migration.html",
        "why": "The zero-downtime migration spends review, tests, and gates on one real change."
      },
      {
        "title": "Detect and handle infrastructure drift",
        "theme": "infrastructure-as-code",
        "difficulty": "middle",
        "href": "questions/infrastructure-as-code/infrastructure-drift.html",
        "why": "Drift detection opens the close: declared state meets operational reality."
      },
      {
        "title": "Govern infrastructure drift at organization scale",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-drift-governance.html",
        "why": "Organization-scale drift governance routes differences to owners rather than auto-applying them."
      },
      {
        "title": "Create a risk-based IaC change-management model",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-change-risk-management.html",
        "why": "The risk-based change model prices what the drift tier keeps finding."
      },
      {
        "title": "Establish infrastructure-as-code platform guardrails",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-platform-guardrails.html",
        "why": "Platform guardrails enforce the model without blocking every team that touches it."
      },
      {
        "title": "Define an infrastructure-as-code state ownership model",
        "theme": "infrastructure-as-code",
        "difficulty": "staff",
        "href": "questions/infrastructure-as-code/iac-state-ownership-model.html",
        "why": "State ownership is last because it is the tier that makes IaC an organizational capability rather than a tool."
      }
    ]
  },
  {
    "theme": "kubernetes",
    "note": "This Theme climbs the same route the platform path climbs: from the object a tenant submits to the cluster an operator runs.",
    "steps": [
      {
        "title": "Explain cloud-native principles and open-source collaboration",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/cloud-native-principles-and-community.html",
        "why": "Cloud-native principles come first: what the platform promises and how its community governs change."
      },
      {
        "title": "Distinguish labels, selectors, and annotations",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/labels-selectors-and-annotations.html",
        "why": "Labels and selectors are the query contract every object below carries."
      },
      {
        "title": "Read the essential parts of a Pod specification",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/pod-spec-basics.html",
        "why": "The Pod specification is the object a tenant actually submits, so it opens the workload tier."
      },
      {
        "title": "Select Kubernetes readiness, liveness, and startup probes",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/probe-selection.html",
        "why": "Probes decide readiness and liveness inside the specification the Theme has just read."
      },
      {
        "title": "Explain Pod lifecycle and container restarts",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/pod-lifecycle-and-restarts.html",
        "why": "Lifecycle and restarts define what the cluster does with the probe's verdict."
      },
      {
        "title": "Set Pod resource requests and limits",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/resource-requests-limits-and-qos.html",
        "why": "Requests, limits, and QoS come before any rollout question because capacity decisions drive maxSurge and maxUnavailable."
      },
      {
        "title": "Explain a Kubernetes Deployment rollout and rollback",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/deployment-rollout-and-rollback.html",
        "why": "Rollout and rollback are the capacity decisions the requests tier just priced."
      },
      {
        "title": "Choose StatefulSet or Deployment",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/statefulset-versus-deployment.html",
        "why": "StatefulSet versus Deployment is the workload choice the rollout machinery serves."
      },
      {
        "title": "Deliver application configuration with ConfigMaps",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/configmap-delivery.html",
        "why": "ConfigMap delivery decouples configuration from the images the rollouts promote."
      },
      {
        "title": "Choose an init container or sidecar for an application Pod",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/multi-container-pod-patterns.html",
        "why": "Init containers versus sidecars compose the Pod the specification defined."
      },
      {
        "title": "Place Kubernetes workloads with affinity and taints",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/scheduling-affinity-and-taints.html",
        "why": "Affinity and taints place the workloads the objects above create."
      },
      {
        "title": "Explain Kubernetes Service discovery",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/service-discovery-basics.html",
        "why": "Service discovery makes the placed workload reachable by name."
      },
      {
        "title": "Expose an application with the right Service type",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/service-types-and-endpoints.html",
        "why": "The right Service type and its endpoints complete the reachability story."
      },
      {
        "title": "Debug a failing Kubernetes application with built-in CLI tools",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/application-debugging-with-cli.html",
        "why": "The debugging set lands mid-Theme on purpose, once every object it reads has been introduced."
      },
      {
        "title": "Debug CoreDNS and Kubernetes Service resolution",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/coredns-service-debugging.html",
        "why": "CoreDNS failures are the discovery tier breaking, read with the CLI tier above."
      },
      {
        "title": "Triage a Kubernetes node that becomes NotReady",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/node-not-ready-triage.html",
        "why": "The NotReady node moves debugging from objects to the machines that run them."
      },
      {
        "title": "Triage a Kubernetes control-plane availability incident",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/control-plane-incident-triage.html",
        "why": "The control-plane incident is the hardest debugging case the tier builds toward."
      },
      {
        "title": "Design least-privilege Kubernetes RBAC",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/rbac-least-privilege.html",
        "why": "Security opens with who may act, before the platform can enforce anything."
      },
      {
        "title": "Give a Kubernetes workload the least-privilege ServiceAccount",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/service-account-workload-identity.html",
        "why": "Workload identities are kept separate from humans, the RBAC tier applied to software."
      },
      {
        "title": "Establish Kubernetes admission policy guardrails",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/admission-policy-and-guardrails.html",
        "why": "Admission policy makes the platform's contract executable at the API boundary."
      },
      {
        "title": "Explain Kyverno policy-engine fundamentals",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/kyverno-policy-engine-basics.html",
        "why": "The Kyverno family opens with the policy engine's model."
      },
      {
        "title": "Design a maintainable Kyverno policy set",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/kyverno-policy-authoring-design.html",
        "why": "Authoring a maintainable policy set is the engine's first real use."
      },
      {
        "title": "Test Kyverno policy changes with the CLI in CI",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/kyverno-cli-policy-ci.html",
        "why": "Testing policy in CI gives the set the delivery discipline the Theme teaches elsewhere."
      },
      {
        "title": "Install or upgrade Kyverno without blocking the cluster",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/kyverno-installation-upgrade-safety.html",
        "why": "Installing or upgrading Kyverno must never block the cluster it guards."
      },
      {
        "title": "Roll out Kyverno enforcement using policy reports",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/kyverno-enforcement-and-policy-reports.html",
        "why": "Rolling out enforcement through policy reports is warn-then-enforce made data."
      },
      {
        "title": "Design a production Kubernetes policy exception process",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/production-policy-exception-process.html",
        "why": "The exception process keeps the guardrails honest when a workload cannot meet them."
      },
      {
        "title": "Govern the Kyverno policy lifecycle and exceptions",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/kyverno-policy-lifecycle-governance.html",
        "why": "Lifecycle governance keeps the policy set alive long after the rollout succeeds."
      },
      {
        "title": "Design a Kubernetes audit policy for security detection",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/audit-policy-runtime-detection.html",
        "why": "Audit policy turns runtime behaviour into detectable evidence."
      },
      {
        "title": "Apply seccomp and AppArmor to a Kubernetes workload",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/seccomp-apparmor-workload.html",
        "why": "Seccomp and AppArmor harden the workload itself rather than its surroundings."
      },
      {
        "title": "Use RuntimeClass for higher-risk workload isolation",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/runtimeclass-sandbox-isolation.html",
        "why": "RuntimeClass buys higher-risk workloads a stronger sandbox on demand."
      },
      {
        "title": "Remediate a Kubernetes CIS benchmark finding",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/cis-benchmark-remediation.html",
        "why": "The CIS benchmark closes the security movement with its outer measurement."
      },
      {
        "title": "Design PersistentVolumeClaim lifecycle for a stateful workload",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/persistent-volume-claim-lifecycle.html",
        "why": "Storage opens with the claim lifecycle every stateful workload rides."
      },
      {
        "title": "Configure HorizontalPodAutoscaler behavior",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/hpa-behavior-and-metrics.html",
        "why": "The autoscaler scales the workloads the placement tier pinned down."
      },
      {
        "title": "Use PodDisruptionBudgets for voluntary disruptions",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/pod-disruption-budget-design.html",
        "why": "Disruption budgets bound the voluntary disruptions autoscaling and upgrades cause."
      },
      {
        "title": "Configure TLS for Kubernetes Ingress safely",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/ingress-tls-security.html",
        "why": "Ingress TLS secures the traffic the Service tier exposed."
      },
      {
        "title": "Govern a migration from Ingress to Gateway API",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/gateway-migration-governance.html",
        "why": "The Gateway API migration is an ownership change, governed rather than renamed."
      },
      {
        "title": "Design a highly available kubeadm control plane",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/ha-control-plane-design.html",
        "why": "The operator tier opens by making the control plane itself highly available."
      },
      {
        "title": "Build and maintain a kubeadm-managed cluster",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/kubeadm-cluster-lifecycle.html",
        "why": "The kubeadm lifecycle keeps the HA design reproducible from day one."
      },
      {
        "title": "Plan a production Kubernetes cluster upgrade",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/cluster-upgrade-strategy.html",
        "why": "The production upgrade spends the version-skew rules and drain capacity the tiers above built."
      },
      {
        "title": "Migrate an application away from a deprecated Kubernetes API",
        "theme": "kubernetes",
        "difficulty": "senior",
        "href": "questions/kubernetes/api-deprecation-migration.html",
        "why": "Deprecated API migrations are the upgrade's application-facing half."
      },
      {
        "title": "Explain the roles of Cilium agents, operator, and Envoy",
        "theme": "kubernetes",
        "difficulty": "junior",
        "href": "questions/kubernetes/cilium-component-roles.html",
        "why": "The Cilium questions open with what each component actually does."
      },
      {
        "title": "Validate a new Cilium installation before production traffic",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/cilium-install-connectivity-validation.html",
        "why": "A new Cilium installation is validated before it carries production traffic."
      },
      {
        "title": "Choose a Cilium IPAM mode for a Kubernetes cluster",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/cilium-ipam-mode-selection.html",
        "why": "IPAM mode decides where pod addresses come from."
      },
      {
        "title": "Choose a Cilium policy-enforcement mode",
        "theme": "kubernetes",
        "difficulty": "middle",
        "href": "questions/kubernetes/cilium-policy-enforcement-modes.html",
        "why": "Enforcement mode selection sets what policy can honestly promise."
      },
      {
        "title": "Lead Kubernetes disaster recovery and restore exercises",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/disaster-recovery-and-restore-exercise.html",
        "why": "Disaster-recovery exercises rehearse the control-plane tiers' worst day."
      },
      {
        "title": "Set Kubernetes platform SLO and capacity governance",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/platform-slo-and-capacity-governance.html",
        "why": "Platform SLOs and capacity governance publish what the operator tier promises."
      },
      {
        "title": "Define multi-tenant Kubernetes platform boundaries",
        "theme": "kubernetes",
        "difficulty": "staff",
        "href": "questions/kubernetes/multi-tenant-platform-boundaries.html",
        "why": "The multi-tenant boundaries decision is last and hardest because every earlier chapter feeds it."
      }
    ]
  },
  {
    "theme": "linux",
    "note": "Boot, process states, and load average open the Theme because half its incidents are misread without that trio, and the close is fleet scope.",
    "steps": [
      {
        "title": "Explain the Linux boot sequence",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/linux-boot-sequence.html",
        "why": "The boot sequence opens the Theme because half its incidents are misread without it."
      },
      {
        "title": "Explain Linux process states during an incident",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/process-states.html",
        "why": "Process states are the smallest unit of host evidence the Theme ever reads."
      },
      {
        "title": "Interpret a high Linux load average",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/load-average-interpretation.html",
        "why": "Load average counts uninterruptible sleep, so it is only honest after process states."
      },
      {
        "title": "Diagnose a systemd service that repeatedly fails",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/systemd-service-failure.html",
        "why": "The repeatedly failing unit is the first host object an operator actually touches."
      },
      {
        "title": "Design a graceful Linux service shutdown",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/signals-and-graceful-shutdown.html",
        "why": "The graceful-shutdown contract resolves the restart-amplification trap the failing unit exposed."
      },
      {
        "title": "Use strace safely to investigate a hung Linux process",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/strace-production-safely.html",
        "why": "strace covers the cases systemd hides, used safely on a production host."
      },
      {
        "title": "Debug process visibility across PID namespaces",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/pid-namespaces-debugging.html",
        "why": "PID-namespace visibility completes the debugging pair for container-era hosts."
      },
      {
        "title": "Explain mounts and filesystem types on Linux",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/mounts-and-filesystem-types.html",
        "why": "Storage opens with what is mounted where, and as what filesystem."
      },
      {
        "title": "Configure LVM storage for a growing service",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/configure-lvm-storage.html",
        "why": "LVM grows the storage story beyond a single device."
      },
      {
        "title": "Explain Linux permissions and umask",
        "theme": "linux",
        "difficulty": "junior",
        "href": "questions/linux/permissions-and-umask.html",
        "why": "Permissions and umask decide who may read what the mounts exposed."
      },
      {
        "title": "Respond to a filesystem mounted read-only after errors",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/filesystem-check-failure.html",
        "why": "The filesystem mounted read-only after errors is the storage tier's own failure mode."
      },
      {
        "title": "Recover disk space held by deleted open files",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/deleted-open-files.html",
        "why": "Space held by deleted open files is the storage tier's most famous surprise."
      },
      {
        "title": "Investigate a Linux out-of-memory kill",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/oom-killer-investigation.html",
        "why": "Memory opens with the kernel's own kill decision, interpretable with process state in hand."
      },
      {
        "title": "Diagnose a cgroup resource limit problem",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/cgroups-resource-isolation.html",
        "why": "The cgroup limit problem is memory pressure with a named owner."
      },
      {
        "title": "Diagnose too many open files in a Linux service",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/file-descriptor-exhaustion.html",
        "why": "File-descriptor exhaustion comes last so its usage-versus-limit alerting lesson follows two different exhaustion shapes."
      },
      {
        "title": "Maintain package repositories without breaking fleet updates",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/maintain-package-repositories.html",
        "why": "The change tier opens with where the fleet's software actually comes from."
      },
      {
        "title": "Plan a production Linux kernel upgrade and rollback",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/kernel-upgrade-rollback.html",
        "why": "The kernel upgrade with rollback is the change tier's highest-stakes routine."
      },
      {
        "title": "Choose between cron and systemd timers",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/cron-versus-systemd-timers.html",
        "why": "Cron versus systemd timers is the scheduling decision the change tier makes daily."
      },
      {
        "title": "Integrate LDAP users through SSSD safely",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/integrate-ldap-users-with-sssd.html",
        "why": "SSSD brings external identity onto the host the Theme has been changing."
      },
      {
        "title": "Manage a libvirt virtual machine change safely",
        "theme": "linux",
        "difficulty": "senior",
        "href": "questions/linux/manage-libvirt-virtual-machines.html",
        "why": "A libvirt change is the host learning it runs someone else's workload."
      },
      {
        "title": "Investigate a failure that occurred only during the previous boot",
        "theme": "linux",
        "difficulty": "middle",
        "href": "questions/linux/previous-boot-log-analysis.html",
        "why": "The failure that happened only during the previous boot is change diagnosis with cold evidence."
      },
      {
        "title": "Define SLOs for a Linux host platform",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/linux-platform-slo.html",
        "why": "Fleet scope opens by promising what the host platform will deliver."
      },
      {
        "title": "Govern a Linux security baseline without blocking delivery",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/linux-security-baseline.html",
        "why": "The security baseline governs every host the SLO just made a promise about."
      },
      {
        "title": "Design a Linux incident evidence and forensics policy",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/linux-incident-forensics-policy.html",
        "why": "The forensics policy decides what evidence the fleet preserves when promises break."
      },
      {
        "title": "Establish Linux fleet capacity governance",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/fleet-capacity-governance.html",
        "why": "Capacity governance prices the fleet the baseline standardized."
      },
      {
        "title": "Define a Linux fleet lifecycle standard",
        "theme": "linux",
        "difficulty": "staff",
        "href": "questions/linux/fleet-os-lifecycle.html",
        "why": "The fleet lifecycle standard closes the Theme at the same altitude the platform path reaches."
      }
    ]
  },
  {
    "theme": "linux-networking",
    "note": "Interfaces, addresses, and routes before MTU and packet capture, and the namespace and policy tier only once single-host diagnosis is reliable.",
    "steps": [
      {
        "title": "Inspect Linux interface state and addresses",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/interface-state-and-addresses.html",
        "why": "Interfaces and addresses are the first facts every later diagnosis reads."
      },
      {
        "title": "Explain a Linux default route",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/default-route-basics.html",
        "why": "The default route decides where everything unmentioned actually goes."
      },
      {
        "title": "Debug a Linux route with ip route get",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/route-get-debugging.html",
        "why": "ip route get shows the kernel's routing decision for one packet, the route tier's tool."
      },
      {
        "title": "Explain Linux DNS resolver configuration",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/dns-resolver-configuration.html",
        "why": "Resolver configuration decides which names the host can even ask about."
      },
      {
        "title": "Identify the process listening on a Linux port",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/socket-listener-inspection.html",
        "why": "Socket state answers who is listening, the question before any connectivity debugging."
      },
      {
        "title": "Triage TCP connection states on Linux",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/tcp-connection-state-triage.html",
        "why": "Connection states show the handshake's aftermath from the host's side."
      },
      {
        "title": "Diagnose an MTU mismatch on Linux",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/mtu-mismatch-triage.html",
        "why": "MTU mismatches fail only for large packets, so they follow the state tier that can prove it."
      },
      {
        "title": "Triage a failed Linux neighbour entry",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/neighbour-table-triage.html",
        "why": "Neighbour discovery is layer-two reachability, the tier underneath routing."
      },
      {
        "title": "Triage a Linux host firewall path",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/firewall-path-triage.html",
        "why": "Firewall paths are where correct routes still silently drop packets."
      },
      {
        "title": "Capture Linux packets without losing diagnostic value",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/packet-capture-scope.html",
        "why": "Capturing with the right scope keeps evidence without drowning the reader."
      },
      {
        "title": "Diagnose a Linux TCP accept-backlog overflow",
        "theme": "linux-networking",
        "difficulty": "senior",
        "href": "questions/linux-networking/tcp-backlog-overflow.html",
        "why": "The accept-backlog overflow is the socket tier's saturation failure."
      },
      {
        "title": "Debug connectivity across a Linux network namespace",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/network-namespace-connectivity.html",
        "why": "Namespaces reopen every earlier tool from a different vantage point."
      },
      {
        "title": "Diagnose Linux policy routing rules",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/policy-routing-with-rules.html",
        "why": "Policy routing answers why the seemingly wrong interface answered."
      },
      {
        "title": "Select a Linux traffic-control investigation path",
        "theme": "linux-networking",
        "difficulty": "senior",
        "href": "questions/linux-networking/traffic-control-qdisc.html",
        "why": "The qdisc investigation shows shaping and queueing the routes never mentioned."
      },
      {
        "title": "Build a Linux network capacity strategy",
        "theme": "linux-networking",
        "difficulty": "staff",
        "href": "questions/linux-networking/linux-network-capacity-strategy.html",
        "why": "The capacity strategy prices the host network the diagnostics kept honest."
      },
      {
        "title": "Lead a Linux networking incident response",
        "theme": "linux-networking",
        "difficulty": "staff",
        "href": "questions/linux-networking/linux-network-incident-command.html",
        "why": "Incident command spends the whole diagnostic stack under real pressure."
      },
      {
        "title": "Explain why nftables replaces iptables",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/nftables-vs-iptables-motivation.html",
        "why": "The nftables motivation explains why new hosts default to a framework that replaces the iptables habits most runbooks still carry."
      },
      {
        "title": "Read an nftables ruleset",
        "theme": "linux-networking",
        "difficulty": "junior",
        "href": "questions/linux-networking/nftables-ruleset-reading.html",
        "why": "Reading a ruleset turns firewall output from noise into the ordered policy it actually is."
      },
      {
        "title": "Distinguish connection refused from a firewall drop",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/refused-vs-dropped-diagnosis.html",
        "why": "The refused-versus-dropped split tells the responder whether the firewall or the listener failed first."
      },
      {
        "title": "Design a default-deny host firewall with nftables",
        "theme": "linux-networking",
        "difficulty": "senior",
        "href": "questions/linux-networking/default-deny-host-firewall-design.html",
        "why": "The default-deny design turns the diagnostic tier into an engineered policy built to fail closed."
      },
      {
        "title": "Explain iptables-nft compatibility on modern distros",
        "theme": "linux-networking",
        "difficulty": "middle",
        "href": "questions/linux-networking/iptables-nft-compatibility.html",
        "why": "The iptables-nft compatibility layer explains why legacy scripts still shape traffic on modern nftables hosts."
      },
      {
        "title": "Set zero-trust Linux host network boundaries",
        "theme": "linux-networking",
        "difficulty": "staff",
        "href": "questions/linux-networking/zero-trust-host-network-boundaries.html",
        "why": "Zero-trust boundaries close the Theme by removing the trusted-host assumption everything above leaned on."
      }
    ]
  },
  {
    "theme": "linux-performance",
    "note": "Work this Theme as a resource tour, one subsystem at a time, before any governance question.",
    "steps": [
      {
        "title": "Use vmstat for a first performance pass",
        "theme": "linux-performance",
        "difficulty": "junior",
        "href": "questions/linux-performance/vmstat-first-pass.html",
        "why": "vmstat is the cheap first pass whose whole job is pointing at the next tool."
      },
      {
        "title": "Read CPU utilization before tuning",
        "theme": "linux-performance",
        "difficulty": "junior",
        "href": "questions/linux-performance/cpu-utilization-basics.html",
        "why": "Reading CPU utilization correctly prevents tuning a number that was never the problem."
      },
      {
        "title": "Investigate a growing CPU run queue",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/cpu-run-queue-triage.html",
        "why": "The growing run queue is the saturation the utilization average hid."
      },
      {
        "title": "Interpret Linux load average correctly",
        "theme": "linux-performance",
        "difficulty": "junior",
        "href": "questions/linux-performance/load-average-meaning.html",
        "why": "Load average interpreted honestly follows the queue, since it counts runnable and uninterruptible work alike."
      },
      {
        "title": "Investigate excess context switching",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/context-switch-analysis.html",
        "why": "Excess context switching continues the CPU story at the scheduler."
      },
      {
        "title": "Profile CPU with perf safely in production",
        "theme": "linux-performance",
        "difficulty": "senior",
        "href": "questions/linux-performance/perf-sampling-safety.html",
        "why": "perf profiling goes deeper than the counters, used safely in production."
      },
      {
        "title": "Diagnose cgroup CPU throttling",
        "theme": "linux-performance",
        "difficulty": "senior",
        "href": "questions/linux-performance/cpu-throttling-diagnosis.html",
        "why": "Cgroup CPU throttling is the container-era ceiling the scheduler tier explains."
      },
      {
        "title": "Distinguish free memory from available memory",
        "theme": "linux-performance",
        "difficulty": "junior",
        "href": "questions/linux-performance/memory-available-basics.html",
        "why": "Memory opens with free versus available, the distinction every capacity claim leans on."
      },
      {
        "title": "Analyze a Linux OOM kill",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/oom-killer-analysis.html",
        "why": "The OOM analysis needs the pressure picture the available-memory tier built."
      },
      {
        "title": "Investigate page-cache reclaim and memory pressure",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/page-cache-reclaim.html",
        "why": "Page-cache reclaim explains memory pressure with no process to blame."
      },
      {
        "title": "Use pressure stall information to find contention",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/pressure-stall-information.html",
        "why": "PSI quantifies the contention the tiers above could only infer."
      },
      {
        "title": "Respond to sustained swap activity",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/swap-activity-response.html",
        "why": "Sustained swap is the memory tier's slow failure, responded to rather than feared."
      },
      {
        "title": "Interpret iowait without blaming storage immediately",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/iowait-interpretation.html",
        "why": "The I/O group opens with iowait read without immediately blaming storage."
      },
      {
        "title": "Diagnose a full filesystem with free-looking space",
        "theme": "linux-performance",
        "difficulty": "junior",
        "href": "questions/linux-performance/disk-space-versus-inodes.html",
        "why": "The full filesystem with free-looking space is the I/O tier's famous trap."
      },
      {
        "title": "Diagnose file-descriptor exhaustion",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/file-descriptor-exhaustion.html",
        "why": "Descriptor exhaustion completes the exhaustion shapes with a slow leak against a limit."
      },
      {
        "title": "Triage TCP retransmissions on a Linux service",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/network-retransmission-triage.html",
        "why": "TCP retransmissions bring the resource tour to the network interface."
      },
      {
        "title": "Diagnose network softirq saturation",
        "theme": "linux-performance",
        "difficulty": "middle",
        "href": "questions/linux-performance/softirq-saturation.html",
        "why": "Softirq saturation is the network stack's own saturation signature."
      },
      {
        "title": "Recognize NUMA locality as a performance constraint",
        "theme": "linux-performance",
        "difficulty": "senior",
        "href": "questions/linux-performance/numa-locality.html",
        "why": "NUMA locality becomes a constraint worth naming once single-host diagnosis is reliable."
      },
      {
        "title": "Evaluate kernel samepage merging safely",
        "theme": "linux-performance",
        "difficulty": "senior",
        "href": "questions/linux-performance/kernel-samepage-merging.html",
        "why": "KSM prices memory deduplication honestly against its own CPU cost."
      },
      {
        "title": "Design a noisy-neighbor performance policy",
        "theme": "linux-performance",
        "difficulty": "staff",
        "href": "questions/linux-performance/noisy-neighbor-policy.html",
        "why": "The noisy-neighbour policy makes co-tenancy a governed trade rather than a gamble."
      },
      {
        "title": "Govern performance-observability overhead",
        "theme": "linux-performance",
        "difficulty": "staff",
        "href": "questions/linux-performance/observability-overhead-governance.html",
        "why": "Observability overhead is governed rather than assumed to be free."
      },
      {
        "title": "Establish a Linux performance baseline program",
        "theme": "linux-performance",
        "difficulty": "staff",
        "href": "questions/linux-performance/performance-baseline-program.html",
        "why": "The programme tier opens by making baselines an organizational habit."
      },
      {
        "title": "Build a capacity model for a Linux service",
        "theme": "linux-performance",
        "difficulty": "staff",
        "href": "questions/linux-performance/performance-capacity-model.html",
        "why": "The capacity model turns those baselines into provisioning plans."
      },
      {
        "title": "Lead a Linux performance incident",
        "theme": "linux-performance",
        "difficulty": "staff",
        "href": "questions/linux-performance/performance-incident-command.html",
        "why": "Leading the performance incident closes the Theme with the tools as a method."
      }
    ]
  },
  {
    "theme": "linux-troubleshooting",
    "note": "Booting failures first, because every later diagnosis presumes a booted machine; diagnostics before the fleet programmes that organize them.",
    "steps": [
      {
        "title": "Recover safely from a Linux boot failure after a configuration change",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/repair-boot-failure.html",
        "why": "The boot that fails after a change comes first because everything later presumes a booted machine."
      },
      {
        "title": "Debug a failed network or local mount at boot",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/debug-failed-mount.html",
        "why": "The mount that blocks startup is the boot's most common hostage."
      },
      {
        "title": "Recover from an interrupted Linux package transaction safely",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/recover-package-manager.html",
        "why": "The interrupted package transaction leaves the host between states, recovered before services arrive."
      },
      {
        "title": "Debug a Linux `Permission denied` failure for a service",
        "theme": "linux-troubleshooting",
        "difficulty": "junior",
        "href": "questions/linux-troubleshooting/debug-permission-denied.html",
        "why": "The service tier opens with the filesystem saying no to a service."
      },
      {
        "title": "Inspect a Linux service that is failing after a restart",
        "theme": "linux-troubleshooting",
        "difficulty": "junior",
        "href": "questions/linux-troubleshooting/inspect-service-logs.html",
        "why": "The service failing after a restart is read from its logs before anything is touched."
      },
      {
        "title": "Diagnose a systemd service that starts before its dependency is usable",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/diagnose-systemd-dependency.html",
        "why": "The unit that starts before its dependency is an ordering problem, and it reads only with unit literacy."
      },
      {
        "title": "Diagnose a Linux filesystem reported as full",
        "theme": "linux-troubleshooting",
        "difficulty": "junior",
        "href": "questions/linux-troubleshooting/diagnose-full-filesystem.html",
        "why": "Resource exhaustion opens with the full filesystem and its several different causes."
      },
      {
        "title": "Investigate a service that reports too many open files",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/investigate-file-descriptors.html",
        "why": "Too many open files is exhaustion with a per-process culprit to find."
      },
      {
        "title": "Diagnose an OOM-killed service in a cgroup-aware host",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/diagnose-oom-kill.html",
        "why": "The OOM kill on a cgroup-aware host needs the cgroup boundaries named."
      },
      {
        "title": "Investigate Linux memory pressure without immediately adding RAM",
        "theme": "linux-troubleshooting",
        "difficulty": "junior",
        "href": "questions/linux-troubleshooting/investigate-memory-pressure.html",
        "why": "Memory pressure investigated without immediately adding RAM is the disciplined sequel to the kill."
      },
      {
        "title": "Investigate accumulating zombie processes on Linux",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/investigate-zombie-processes.html",
        "why": "Zombies accumulate when a parent forgets, harmless right up until they are not."
      },
      {
        "title": "Investigate a Linux hung-task warning or D-state process",
        "theme": "linux-troubleshooting",
        "difficulty": "senior",
        "href": "questions/linux-troubleshooting/investigate-hung-task.html",
        "why": "The D-state hung task is where process-state knowledge pays for itself."
      },
      {
        "title": "Analyze a host with a high load average but low CPU utilization",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/analyze-load-average.html",
        "why": "High load with low CPU bridges pure CPU thinking into storage I/O latency."
      },
      {
        "title": "Perform first-pass storage I/O latency triage on Linux",
        "theme": "linux-troubleshooting",
        "difficulty": "senior",
        "href": "questions/linux-troubleshooting/perform-storage-io-triage.html",
        "why": "First-pass storage I/O triage follows the bridge that pointed here."
      },
      {
        "title": "Trace an intermittent DNS resolution failure on Linux",
        "theme": "linux-troubleshooting",
        "difficulty": "junior",
        "href": "questions/linux-troubleshooting/trace-dns-failure.html",
        "why": "The network set opens with intermittent DNS, the flakiest dependency of all."
      },
      {
        "title": "Trace suspected connection-tracking exhaustion on a Linux node",
        "theme": "linux-troubleshooting",
        "difficulty": "senior",
        "href": "questions/linux-troubleshooting/trace-conntrack-exhaustion.html",
        "why": "Connection-tracking exhaustion fails new connections while the old ones keep living."
      },
      {
        "title": "Triage packet loss from a Linux host to a critical dependency",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/triage-network-packet-loss.html",
        "why": "Packet loss to a critical dependency is measured rather than assumed."
      },
      {
        "title": "Diagnose an application stalled on an NFS mount",
        "theme": "linux-troubleshooting",
        "difficulty": "senior",
        "href": "questions/linux-troubleshooting/diagnose-nfs-stall.html",
        "why": "The NFS-stalled application shows local symptoms with remote causes."
      },
      {
        "title": "Resolve clock skew that is breaking Linux service authentication",
        "theme": "linux-troubleshooting",
        "difficulty": "middle",
        "href": "questions/linux-troubleshooting/resolve-clock-skew.html",
        "why": "Clock skew breaking authentication is time, the quietest dependency on the host."
      },
      {
        "title": "Lead evidence-preserving triage after a Linux kernel panic",
        "theme": "linux-troubleshooting",
        "difficulty": "senior",
        "href": "questions/linux-troubleshooting/debug-kernel-panic.html",
        "why": "The kernel panic is kept last among diagnostics because it is pure evidence-preservation discipline."
      },
      {
        "title": "Design an evidence-driven Linux troubleshooting runbook program",
        "theme": "linux-troubleshooting",
        "difficulty": "staff",
        "href": "questions/linux-troubleshooting/design-linux-troubleshooting-runbooks.html",
        "why": "The fleet tier opens by making the diagnostics above a runbook programme."
      },
      {
        "title": "Architect Linux fleet observability for rapid fault isolation",
        "theme": "linux-troubleshooting",
        "difficulty": "staff",
        "href": "questions/linux-troubleshooting/architect-linux-observability.html",
        "why": "Fleet observability finds the faults before the runbooks ever fire."
      },
      {
        "title": "Lead capacity and saturation risk management for a Linux platform",
        "theme": "linux-troubleshooting",
        "difficulty": "staff",
        "href": "questions/linux-troubleshooting/lead-linux-capacity-risk.html",
        "why": "Capacity and saturation risk management governs the fleet's future failures."
      },
      {
        "title": "Coordinate a cross-team major incident rooted in Linux host failures",
        "theme": "linux-troubleshooting",
        "difficulty": "staff",
        "href": "questions/linux-troubleshooting/coordinate-linux-major-incident.html",
        "why": "The cross-team major incident closes the Theme at the scale the runbooks organize."
      }
    ]
  },
  {
    "theme": "logging",
    "note": "Streams before data model, data model before pipeline, pipeline before duties and strategy — the pipeline questions are about moving and protecting the model.",
    "steps": [
      {
        "title": "Explain why containers log to standard streams",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/stdout-in-containers.html",
        "why": "The Theme begins where container logs begin: standard streams as the platform contract."
      },
      {
        "title": "Explain syslog facilities and severity",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/syslog-basics.html",
        "why": "Facilities and severity are the vocabulary those streams inherit from syslog."
      },
      {
        "title": "Design structured logs for request correlation",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/structured-log-correlation.html",
        "why": "Structured logs with request correlation turn raw streams into evidence."
      },
      {
        "title": "Convert journald and Flask logs to structured JSON",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/structured-logging-json-format.html",
        "why": "Converting journald and Flask output to structured JSON makes the correlation fields above machine-readable instead of grep-dependent."
      },
      {
        "title": "Choose fields for a log data model",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/log-data-model.html",
        "why": "The data model decides what the pipeline will even be able to answer."
      },
      {
        "title": "Define a production log-level policy",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/log-level-policy.html",
        "why": "The level policy keeps volume honest before the model grows unwieldy."
      },
      {
        "title": "Parse multiline exception logs safely",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/multiline-log-parsing.html",
        "why": "Multiline exceptions parse safely or the model's best evidence corrupts itself."
      },
      {
        "title": "Handle log rotation without duplicate or missing events",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/rotation-and-tailers.html",
        "why": "Rotation without duplicate or missing events keeps the stream continuous."
      },
      {
        "title": "Make log timestamps useful in incident analysis",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/timestamp-correctness.html",
        "why": "Timestamps that survive incident analysis are the model's spine."
      },
      {
        "title": "Design collector buffering and backpressure",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/collector-buffering.html",
        "why": "The platform tier opens with buffering and backpressure, the pipeline's shock absorbers."
      },
      {
        "title": "Define an SLO for a log delivery pipeline",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/log-pipeline-slo.html",
        "why": "The delivery SLO promises exactly what the buffering tier made possible."
      },
      {
        "title": "Evolve a log schema without breaking consumers",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/schema-evolution.html",
        "why": "Evolving the schema without breaking consumers keeps those promises across versions."
      },
      {
        "title": "Diagnose a slow expensive log query",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/log-query-performance.html",
        "why": "The slow expensive query is the bill that poor field design writes."
      },
      {
        "title": "Select and filter log streams with LogQL",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/logql-stream-filtering-basics.html",
        "why": "LogQL stream selectors and line filters are the query vocabulary the performance tier above is judged against."
      },
      {
        "title": "Explain Loki architecture and label design",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/loki-architecture-and-label-design.html",
        "why": "The Loki pipeline and its label model explain why stream selection, not index tuning, drives most query cost."
      },
      {
        "title": "Prevent secrets from entering logs",
        "theme": "logging",
        "difficulty": "junior",
        "href": "questions/logging/secret-redaction.html",
        "why": "The duties open with keeping secrets out of logs, which outranks any feature."
      },
      {
        "title": "Govern logging with privacy by design",
        "theme": "logging",
        "difficulty": "staff",
        "href": "questions/logging/privacy-by-design.html",
        "why": "Privacy by design governs the whole pipeline rather than filtering at the end."
      },
      {
        "title": "Define a log retention policy",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/log-retention-policy.html",
        "why": "Retention decides what the platform keeps and what it owes regulators."
      },
      {
        "title": "Attribute and reduce logging cost safely",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/log-cost-attribution.html",
        "why": "Cost attribution prices the volume the levels and retention allowed."
      },
      {
        "title": "Isolate tenants in a shared logging platform",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/tenant-isolation.html",
        "why": "Tenant isolation keeps one customer's evidence away from another's eyes."
      },
      {
        "title": "Preserve log integrity for an investigation",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/log-forensics-integrity.html",
        "why": "Integrity for investigations is the duty tier's own close."
      },
      {
        "title": "Correlate trace context with logs",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/trace-log-correlation.html",
        "why": "Use opens with trace context correlated back into logs."
      },
      {
        "title": "Use logs effectively during a cross-service incident",
        "theme": "logging",
        "difficulty": "staff",
        "href": "questions/logging/logging-incident-command.html",
        "why": "Reading logs across services mid-incident is the use case everything above served."
      },
      {
        "title": "Migrate a company from fragmented logging to a common platform",
        "theme": "logging",
        "difficulty": "staff",
        "href": "questions/logging/logging-migration.html",
        "why": "The strategy tier opens with migrating off fragmented logging."
      },
      {
        "title": "Define ownership boundaries for a logging service",
        "theme": "logging",
        "difficulty": "staff",
        "href": "questions/logging/logging-service-ownership.html",
        "why": "Ownership boundaries decide who actually runs the platform the migration built."
      },
      {
        "title": "Set a platform strategy for organization-wide logging",
        "theme": "logging",
        "difficulty": "staff",
        "href": "questions/logging/organization-logging-platform.html",
        "why": "The organization-wide platform decision closes the Theme at fleet scale."
      },
      {
        "title": "Compare Loki and ELK for log platform cost",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/loki-vs-elk-tradeoffs.html",
        "why": "The Loki-versus-ELK cost comparison prices the two dominant log platform models before committing to one."
      },
      {
        "title": "Explain VictoriaMetrics next to Prometheus",
        "theme": "logging",
        "difficulty": "middle",
        "href": "questions/logging/victoriametrics-vs-prometheus.html",
        "why": "The VictoriaMetrics comparison extends the build-versus-adopt decision to the metrics backend beside the log platform."
      },
      {
        "title": "Design Loki retention and multi-tenancy",
        "theme": "logging",
        "difficulty": "senior",
        "href": "questions/logging/loki-retention-and-multi-tenancy.html",
        "why": "Retention and multi-tenancy design turns the platform choice into enforceable per-team data boundaries and lifetimes."
      }
    ]
  },
  {
    "theme": "network-storage",
    "note": "Decide the access shape before the protocol, because the NAS, SAN, or object question routes you to everything that follows.",
    "steps": [
      {
        "title": "Choose NAS, SAN, or object storage for a workload",
        "theme": "network-storage",
        "difficulty": "junior",
        "href": "questions/network-storage/nas-san-object-storage.html",
        "why": "The NAS, SAN, or object question comes first because it routes everything that follows."
      },
      {
        "title": "Mount an NFS export safely",
        "theme": "network-storage",
        "difficulty": "junior",
        "href": "questions/network-storage/nfs-mount-basics.html",
        "why": "NFS opens the file chapter by mounting an export safely."
      },
      {
        "title": "Select an NFS protocol version",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/nfs-version-selection.html",
        "why": "The protocol version changes failure behaviour, so it is chosen before that behaviour is tuned."
      },
      {
        "title": "Choose NFS failure behavior",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/nfs-hard-soft-mounts.html",
        "why": "Hard versus soft mounts decide what the client does when the server vanishes."
      },
      {
        "title": "Explain NFS cache coherency",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/nfs-caching-coherency.html",
        "why": "Cache coherency explains why NFS reads can surprise the writer."
      },
      {
        "title": "Diagnose NFS ownership and identity mapping",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/nfs-identity-mapping.html",
        "why": "Identity mapping decides whose permissions the export actually enforces."
      },
      {
        "title": "Plan NFS lock recovery",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/nfs-lock-recovery.html",
        "why": "Lock recovery is incomprehensible until coherency has already worried you, so it comes last."
      },
      {
        "title": "Explain an SMB file share",
        "theme": "network-storage",
        "difficulty": "junior",
        "href": "questions/network-storage/smb-share-basics.html",
        "why": "SMB mirrors the NFS chapter, opening with the share itself."
      },
      {
        "title": "Apply SMB signing and encryption",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/smb-signing-encryption.html",
        "why": "Signing and encryption are SMB's security tier above the share."
      },
      {
        "title": "Explain iSCSI initiators and targets",
        "theme": "network-storage",
        "difficulty": "junior",
        "href": "questions/network-storage/iscsi-initiator-target.html",
        "why": "The block chapter opens with the iSCSI initiator and target model."
      },
      {
        "title": "Validate iSCSI multipathing",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/iscsi-multipathing.html",
        "why": "Multipathing validation proves the redundancy the block path claims."
      },
      {
        "title": "Design an NVMe over Fabrics deployment",
        "theme": "network-storage",
        "difficulty": "senior",
        "href": "questions/network-storage/nvmeof-fabrics-design.html",
        "why": "NVMe over Fabrics is the block chapter's modern transport."
      },
      {
        "title": "Prevent multi-writer block-storage corruption",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/block-storage-single-writer.html",
        "why": "The multi-writer corruption question stands guard over the whole block story."
      },
      {
        "title": "Design for object-storage consistency and retries",
        "theme": "network-storage",
        "difficulty": "junior",
        "href": "questions/network-storage/object-storage-consistency.html",
        "why": "Object storage opens with consistency and retry design."
      },
      {
        "title": "Design object lifecycle and retention rules",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/object-lifecycle-retention.html",
        "why": "Lifecycle and retention rules govern what object storage keeps and for how long."
      },
      {
        "title": "Choose Ceph replication or erasure coding",
        "theme": "network-storage",
        "difficulty": "senior",
        "href": "questions/network-storage/ceph-replication-vs-erasure-coding.html",
        "why": "Ceph opens with its core durability trade, replication versus erasure coding."
      },
      {
        "title": "Protect Ceph recovery capacity",
        "theme": "network-storage",
        "difficulty": "senior",
        "href": "questions/network-storage/ceph-recovery-capacity.html",
        "why": "Recovery capacity is what keeps a degraded Ceph cluster alive."
      },
      {
        "title": "Distinguish snapshots from backups",
        "theme": "network-storage",
        "difficulty": "middle",
        "href": "questions/network-storage/snapshots-versus-backups.html",
        "why": "Platform resilience opens by distinguishing snapshots from backups."
      },
      {
        "title": "Design cross-region storage resilience",
        "theme": "network-storage",
        "difficulty": "staff",
        "href": "questions/network-storage/cross-region-storage-resilience.html",
        "why": "Cross-region design spends the snapshot-versus-backup distinction at distance."
      },
      {
        "title": "Build ransomware-resilient storage backups",
        "theme": "network-storage",
        "difficulty": "senior",
        "href": "questions/network-storage/ransomware-resilient-backups.html",
        "why": "Ransomware-resilient backups assume the adversary reaches the primary copy."
      },
      {
        "title": "Run a storage disaster-recovery exercise",
        "theme": "network-storage",
        "difficulty": "staff",
        "href": "questions/network-storage/storage-disaster-recovery-exercise.html",
        "why": "The disaster-recovery exercise proves the resilience tier rather than describing it."
      },
      {
        "title": "Investigate network-storage latency",
        "theme": "network-storage",
        "difficulty": "senior",
        "href": "questions/network-storage/storage-performance-investigation.html",
        "why": "Latency triage is the operations tier's daily question."
      },
      {
        "title": "Define storage platform service tiers",
        "theme": "network-storage",
        "difficulty": "staff",
        "href": "questions/network-storage/storage-platform-service-tiers.html",
        "why": "Service tiers promise latency and capacity per class of workload."
      },
      {
        "title": "Establish storage tenancy boundaries",
        "theme": "network-storage",
        "difficulty": "staff",
        "href": "questions/network-storage/storage-security-tenancy.html",
        "why": "Tenancy boundaries keep tenants apart on shared storage."
      },
      {
        "title": "Govern storage cost and capacity across teams",
        "theme": "network-storage",
        "difficulty": "staff",
        "href": "questions/network-storage/storage-cost-and-capacity-governance.html",
        "why": "Cost and capacity governance closes the Theme at platform scale."
      }
    ]
  },
  {
    "theme": "networking",
    "note": "Build the stack bottom-up and resolve names before connections, because most service-down reports in this Theme start at resolution.",
    "steps": [
      {
        "title": "Map a request to network layers",
        "theme": "networking",
        "difficulty": "junior",
        "href": "questions/networking/osi-and-tcp-ip-layers.html",
        "why": "Mapping a request to network layers is the map every later diagnosis navigates."
      },
      {
        "title": "Calculate an IPv4 CIDR range",
        "theme": "networking",
        "difficulty": "junior",
        "href": "questions/networking/cidr-address-calculation.html",
        "why": "CIDR arithmetic is the addressing vocabulary the map requires."
      },
      {
        "title": "Use private IPv4 address space safely",
        "theme": "networking",
        "difficulty": "junior",
        "href": "questions/networking/private-address-space.html",
        "why": "Private address space used correctly keeps routing honest."
      },
      {
        "title": "Explain ports and sockets",
        "theme": "networking",
        "difficulty": "junior",
        "href": "questions/networking/ports-and-sockets.html",
        "why": "Ports versus sockets separates names from actual endpoints."
      },
      {
        "title": "Choose between TCP and UDP",
        "theme": "networking",
        "difficulty": "junior",
        "href": "questions/networking/tcp-versus-udp.html",
        "why": "TCP or UDP is the transport choice everything above enables."
      },
      {
        "title": "Select DNS record types and TTLs",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/dns-record-types-and-ttl.html",
        "why": "Names before connections: record types and TTLs are DNS's own contract."
      },
      {
        "title": "Trace a DNS lookup from an application to an answer",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/dns-resolution-path.html",
        "why": "The lookup traced from application to authoritative answer is the path most service-down reports start on."
      },
      {
        "title": "Debug an authoritative DNS delegation",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/authoritative-dns-delegation.html",
        "why": "The delegation failure is name resolution breaking at its root."
      },
      {
        "title": "Diagnose a failed TCP three-way handshake",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/tcp-three-way-handshake.html",
        "why": "The failed handshake separates a host with nothing listening from one silently dropping packets."
      },
      {
        "title": "Interpret TCP retransmissions and timeouts",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/tcp-retransmission-and-timeouts.html",
        "why": "Retransmissions and timeouts quantify how much distress the transport is actually in."
      },
      {
        "title": "Diagnose a path MTU discovery black hole",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/path-mtu-discovery.html",
        "why": "The MTU black hole fails only the big packets, found after transport works."
      },
      {
        "title": "Debug a TLS handshake failure",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/tls-handshake-failure.html",
        "why": "TLS fails on top of a working transport, so it is diagnosed last in the group."
      },
      {
        "title": "Diagnose route selection and asymmetric paths",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/route-selection-and-asymmetry.html",
        "why": "Routing diagnosis opens with selection and the asymmetric paths it hides."
      },
      {
        "title": "Troubleshoot NAT connection failures",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/nat-connection-troubleshooting.html",
        "why": "NAT connection failures are routing's stateful cousin, diagnosed after plain selection is understood."
      },
      {
        "title": "Design load-balancer health checks",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/load-balancer-health-check-design.html",
        "why": "Health-check design is undecidable until you know what a completed handshake actually proves."
      },
      {
        "title": "Operate a dual-stack service",
        "theme": "networking",
        "difficulty": "middle",
        "href": "questions/networking/ipv6-dual-stack-basics.html",
        "why": "The policy tier opens with operating a dual-stack service."
      },
      {
        "title": "Plan a dual-stack migration",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/dual-stack-migration-plan.html",
        "why": "The migration plan is the dual-stack strategy set in motion."
      },
      {
        "title": "Design network segmentation for a service",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/network-segmentation-design.html",
        "why": "Segmentation decides what may talk to what, as policy."
      },
      {
        "title": "Govern production network egress",
        "theme": "networking",
        "difficulty": "staff",
        "href": "questions/networking/egress-governance.html",
        "why": "Egress governance turns outbound traffic into policy with owners."
      },
      {
        "title": "Create a network capacity model",
        "theme": "networking",
        "difficulty": "staff",
        "href": "questions/networking/network-capacity-model.html",
        "why": "The remainder opens with the capacity model, answered for a network rather than a host."
      },
      {
        "title": "Build safe network change delivery",
        "theme": "networking",
        "difficulty": "staff",
        "href": "questions/networking/network-change-management.html",
        "why": "Safe change delivery keeps the network itself from being the outage."
      },
      {
        "title": "Design multi-region connectivity boundaries",
        "theme": "networking",
        "difficulty": "staff",
        "href": "questions/networking/multi-region-connectivity-architecture.html",
        "why": "Multi-region boundaries spend the capacity and change tiers at scale."
      },
      {
        "title": "Respond to a BGP route leak risk",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/bgp-route-leak-response.html",
        "why": "The BGP route leak is the internet's failure mode arriving at your door."
      },
      {
        "title": "Lead a DNS incident response",
        "theme": "networking",
        "difficulty": "senior",
        "href": "questions/networking/dns-incident-response.html",
        "why": "DNS incident response is the resolution tier's worst day, rehearsed."
      },
      {
        "title": "Set a network reliability strategy",
        "theme": "networking",
        "difficulty": "staff",
        "href": "questions/networking/network-reliability-strategy.html",
        "why": "The reliability strategy closes the Theme as a funded promise."
      }
    ]
  },
  {
    "theme": "observability",
    "note": "Define an SLI and an SLO before touching a tool: until a target exists, nothing here knows whether it is succeeding.",
    "steps": [
      {
        "title": "Define an SLI and SLO for an API",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/define-an-sli-and-slo.html",
        "why": "Until a target exists, nothing in the Theme knows whether it is succeeding."
      },
      {
        "title": "Compare metrics, logs, and traces during an incident",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/three-observability-signals.html",
        "why": "The signal map compares metrics, logs, and traces during an incident."
      },
      {
        "title": "Choose a counter, gauge, histogram, or summary",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/describe-metric-types.html",
        "why": "Counter versus histogram decides whether tail behaviour is measurable at all."
      },
      {
        "title": "Explain a metrics time series and its labels",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/explain-time-series-labels.html",
        "why": "Time-series anatomy shows what the metric types actually produce."
      },
      {
        "title": "Instrument a distributed trace for an API request",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/instrument-a-trace.html",
        "why": "Instrumentation begins with one request traced end to end."
      },
      {
        "title": "Design trace sampling without losing incidents",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/design-telemetry-sampling.html",
        "why": "Sampling design keeps tracing affordable without losing the incidents."
      },
      {
        "title": "Diagnose missing trace context across services",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/propagate-trace-context.html",
        "why": "Missing trace context is the diagnosis the sampling tier must survive, and the bridge that correlates context back into logs."
      },
      {
        "title": "Measure and improve tail latency",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/measure-tail-latency.html",
        "why": "Measurement deepens before alerting does: tails need histograms and traces in place first."
      },
      {
        "title": "Design a useful service dashboard",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/design-a-dashboard.html",
        "why": "Useful dashboards make the measurements readable under pressure."
      },
      {
        "title": "Combine black-box and white-box monitoring",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/compare-blackbox-whitebox.html",
        "why": "Black-box against white-box chooses the vantage point per question."
      },
      {
        "title": "Explain Zabbix items, triggers, and actions",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/explain-zabbix-items-triggers-actions.html",
        "why": "The Zabbix items-triggers-actions pipeline shows the same alerting concepts above carried by a concrete agent-based tool."
      },
      {
        "title": "Manage a large host fleet with Zabbix templates",
        "theme": "observability",
        "difficulty": "junior",
        "href": "questions/observability/apply-zabbix-templates-at-scale.html",
        "why": "Template management scales the per-host pipeline into a fleet-wide standard instead of hand-built checks."
      },
      {
        "title": "Use recording rules for expensive PromQL",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/use-recording-rules.html",
        "why": "Recording rules make expensive PromQL affordable at query time."
      },
      {
        "title": "Choose between Zabbix and Prometheus",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/compare-zabbix-and-prometheus.html",
        "why": "The Zabbix-versus-Prometheus comparison prices the pull-based metrics model against agent-based monitoring before standardizing on one."
      },
      {
        "title": "Control metric-label cardinality",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/control-metric-cardinality.html",
        "why": "Cardinality kept under control is the budget the rules and dashboards spend."
      },
      {
        "title": "Build an actionable production alert",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/build-an-actionable-alert.html",
        "why": "The alerting arc opens with an alert an owner can actually act on."
      },
      {
        "title": "Reduce alert fatigue without hiding risk",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/investigate-alert-fatigue.html",
        "why": "Reducing alert fatigue without hiding risk keeps the alerts trusted."
      },
      {
        "title": "Diagnose Zabbix trigger false positives",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/diagnose-zabbix-trigger-false-positives.html",
        "why": "Trigger false-positive diagnosis applies the alert-fatigue tier to one tool's expressions, dependencies, and maintenance windows."
      },
      {
        "title": "Explain an SLO error-budget burn-rate alert",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/slo-burn-rate.html",
        "why": "The burn-rate alert closes the loop back to the opening SLO."
      },
      {
        "title": "Operate a reliable telemetry collection pipeline",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/operate-a-telemetry-pipeline.html",
        "why": "The platform tier opens with pipeline reliability, the substrate everything rode."
      },
      {
        "title": "Decide when to deploy a Zabbix proxy",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/decide-zabbix-proxy-placement.html",
        "why": "Proxy placement is the distributed-monitoring tier of telemetry transport applied to monitoring of remote and isolated networks."
      },
      {
        "title": "Monitor discovered entities with Zabbix low-level discovery",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/use-zabbix-low-level-discovery.html",
        "why": "Low-level discovery keeps per-entity monitoring in sync with reality without hand-maintained check lists."
      },
      {
        "title": "Debug gaps in production telemetry",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/debug-telemetry-gaps.html",
        "why": "Telemetry gaps are found before they are needed, not discovered mid-incident."
      },
      {
        "title": "Validate telemetry data quality after a release",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/validate-telemetry-data-quality.html",
        "why": "Data-quality validation catches the release that silently broke the pipeline."
      },
      {
        "title": "Set telemetry retention and query-cost controls",
        "theme": "observability",
        "difficulty": "senior",
        "href": "questions/observability/set-observability-retention.html",
        "why": "Retention and query-cost controls price the history the platform keeps."
      },
      {
        "title": "Govern telemetry cost across teams",
        "theme": "observability",
        "difficulty": "staff",
        "href": "questions/observability/govern-telemetry-cost.html",
        "why": "Cost governance spends the retention decisions across every team."
      },
      {
        "title": "Design multi-tenant observability boundaries",
        "theme": "observability",
        "difficulty": "staff",
        "href": "questions/observability/design-multitenant-observability.html",
        "why": "Tenant boundaries keep one team's data out of another's console."
      },
      {
        "title": "Design an incident evidence strategy",
        "theme": "observability",
        "difficulty": "staff",
        "href": "questions/observability/design-incident-evidence.html",
        "why": "The evidence strategy makes incidents investigable after the fact."
      },
      {
        "title": "Investigate a failed request with Cilium Hubble",
        "theme": "observability",
        "difficulty": "middle",
        "href": "questions/observability/cilium-hubble-flow-observation.html",
        "why": "Hubble covers the network blind spot the signal map left open."
      },
      {
        "title": "Establish an observability platform product",
        "theme": "observability",
        "difficulty": "staff",
        "href": "questions/observability/establish-observability-platform.html",
        "why": "The observability platform as a product is the tier's synthesis."
      },
      {
        "title": "Govern an organization-wide SLO program",
        "theme": "observability",
        "difficulty": "staff",
        "href": "questions/observability/govern-an-slo-program.html",
        "why": "The organization-wide SLO program is the Theme's close."
      }
    ]
  },
  {
    "theme": "performance-engineering",
    "note": "Measurement literacy before optimization, diagnosis before capacity and economics, and contracts and portfolios to close.",
    "steps": [
      {
        "title": "Why use latency percentiles instead of an average?",
        "theme": "performance-engineering",
        "difficulty": "junior",
        "href": "questions/performance-engineering/measure-latency-percentiles.html",
        "why": "Latency percentiles instead of averages is the literacy the whole Theme stands on."
      },
      {
        "title": "How should an engineer choose latency histogram buckets?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/choose-histogram-buckets.html",
        "why": "Histogram buckets chosen around objectives make the percentiles measurable."
      },
      {
        "title": "What makes a performance objective actionable?",
        "theme": "performance-engineering",
        "difficulty": "junior",
        "href": "questions/performance-engineering/define-performance-objectives.html",
        "why": "An objective somebody can act on turns measurement into actual work."
      },
      {
        "title": "How do you select a load model for a production-facing service?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/select-load-test-model.html",
        "why": "The load model decides what the numbers will even mean before they are gathered."
      },
      {
        "title": "How are throughput, concurrency, and latency related during a load test?",
        "theme": "performance-engineering",
        "difficulty": "junior",
        "href": "questions/performance-engineering/throughput-and-concurrency.html",
        "why": "How throughput, concurrency, and latency relate explains most reports that the service is slow."
      },
      {
        "title": "How do you find the critical path of a slow distributed request?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/trace-critical-path.html",
        "why": "The critical path of a slow distributed request localizes the blame honestly."
      },
      {
        "title": "What evidence distinguishes a bottleneck from a busy component?",
        "theme": "performance-engineering",
        "difficulty": "junior",
        "href": "questions/performance-engineering/identify-bottleneck-signals.html",
        "why": "Bottleneck versus busy is the evidence question the diagnostic tier opens with."
      },
      {
        "title": "How do you investigate a CPU hotspot without optimizing the wrong code?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/profile-cpu-hotspots.html",
        "why": "CPU hotspots follow, investigated without optimizing the wrong code."
      },
      {
        "title": "How do you investigate a database query performance regression?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/database-query-regression.html",
        "why": "Query regressions are the database tier of the same diagnosis."
      },
      {
        "title": "How do you size a client connection pool safely?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/connection-pool-sizing.html",
        "why": "Pool sizing is the concurrency question the load model framed earlier."
      },
      {
        "title": "How do you evaluate whether a cache improves a service?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/cache-performance-evaluation.html",
        "why": "Whether the cache actually helps is asked before crediting it with the improvement."
      },
      {
        "title": "How would you establish a capacity baseline for a service?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/capacity-baseline-design.html",
        "why": "The capacity tier opens with a baseline that survives scrutiny."
      },
      {
        "title": "How should capacity economics influence performance governance?",
        "theme": "performance-engineering",
        "difficulty": "staff",
        "href": "questions/performance-engineering/capacity-economics-governance.html",
        "why": "Capacity economics influence what the baseline can honestly recommend."
      },
      {
        "title": "How do you diagnose and mitigate noisy-neighbor performance?",
        "theme": "performance-engineering",
        "difficulty": "senior",
        "href": "questions/performance-engineering/multi-tenant-noisy-neighbor.html",
        "why": "Noisy neighbours are the multi-tenant version of the capacity problem."
      },
      {
        "title": "When and how should a service shed load?",
        "theme": "performance-engineering",
        "difficulty": "senior",
        "href": "questions/performance-engineering/load-shedding-design.html",
        "why": "Load shedding is a performance tool here, not only an emergency brake."
      },
      {
        "title": "What must stay controlled when you compare two performance runs?",
        "theme": "performance-engineering",
        "difficulty": "junior",
        "href": "questions/performance-engineering/benchmark-control-variables.html",
        "why": "Experiment integrity opens with comparisons whose variables stayed controlled."
      },
      {
        "title": "How do you run performance experiments without endangering production?",
        "theme": "performance-engineering",
        "difficulty": "senior",
        "href": "questions/performance-engineering/benchmark-production-safety.html",
        "why": "Production experiments run safely or they do not run at all."
      },
      {
        "title": "What should a performance regression check in CI actually prove?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/performance-regression-ci.html",
        "why": "A CI regression check must prove only what it can honestly prove."
      },
      {
        "title": "How do performance budgets change API and dependency design?",
        "theme": "performance-engineering",
        "difficulty": "senior",
        "href": "questions/performance-engineering/performance-budget-api.html",
        "why": "Contracts open with performance budgets shaping API and dependency design."
      },
      {
        "title": "What cross-team contracts prevent performance regressions in a platform?",
        "theme": "performance-engineering",
        "difficulty": "staff",
        "href": "questions/performance-engineering/cross-team-performance-contracts.html",
        "why": "Cross-team contracts keep regressions from crossing team borders unnoticed."
      },
      {
        "title": "How do you design a performance observability strategy across many services?",
        "theme": "performance-engineering",
        "difficulty": "staff",
        "href": "questions/performance-engineering/performance-observability-strategy.html",
        "why": "Observability across services watches those contracts actually hold."
      },
      {
        "title": "How should a staff engineer evaluate resilience versus performance trade-offs?",
        "theme": "performance-engineering",
        "difficulty": "staff",
        "href": "questions/performance-engineering/resilience-performance-tradeoffs.html",
        "why": "Resilience versus performance is the staff trade the contracts just priced."
      },
      {
        "title": "How would a staff engineer prioritize a portfolio of performance work?",
        "theme": "performance-engineering",
        "difficulty": "staff",
        "href": "questions/performance-engineering/performance-investment-portfolio.html",
        "why": "The staff-level portfolio prioritizes all the work the contracts surfaced."
      },
      {
        "title": "How do you triage a p99 latency regression?",
        "theme": "performance-engineering",
        "difficulty": "senior",
        "href": "questions/performance-engineering/tail-latency-triage.html",
        "why": "The p99 triage stays last as a dress rehearsal for the whole diagnostic tier above."
      },
      {
        "title": "Why can high-cardinality metrics become a performance incident?",
        "theme": "performance-engineering",
        "difficulty": "middle",
        "href": "questions/performance-engineering/avoid-metric-cardinality.html",
        "why": "The high-cardinality incident is the other dress rehearsal, turning measurement itself into the outage."
      }
    ]
  },
  {
    "theme": "platform-engineering",
    "note": "Definition, road, and product before self-service mechanics, and the judgement calls only after the operating model exists.",
    "steps": [
      {
        "title": "Define an internal developer platform",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/define-an-internal-developer-platform.html",
        "why": "What an internal developer platform is names the product everything else serves."
      },
      {
        "title": "Explain a paved road and a golden path",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/explain-a-paved-road-and-a-golden-path.html",
        "why": "The paved road and golden path give the platform its central metaphor."
      },
      {
        "title": "Treat the platform as a product",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/treat-the-platform-as-a-product.html",
        "why": "Platform-as-a-product is the operating model that separates it from a ticket queue."
      },
      {
        "title": "Offer self-service with safe defaults",
        "theme": "platform-engineering",
        "difficulty": "junior",
        "href": "questions/platform-engineering/offer-self-service-with-safe-defaults.html",
        "why": "Self-service with safe defaults is the mechanism that makes the road real."
      },
      {
        "title": "Choose a guardrail over a gate",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/choose-a-guardrail-over-a-gate.html",
        "why": "Guardrails versus gates decides how the defaults treat every deviation."
      },
      {
        "title": "Version a platform interface",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/version-a-platform-interface.html",
        "why": "Interface versioning and deprecation keep the road's promises honest over time."
      },
      {
        "title": "Publish platform SLOs and a support model",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/publish-platform-slos-and-a-support-model.html",
        "why": "SLOs and a support model publish what tenants may actually depend on."
      },
      {
        "title": "Onboard a team onto the platform",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/onboard-a-team-onto-the-platform.html",
        "why": "Onboarding is the first lifecycle moment those promises must survive."
      },
      {
        "title": "Plan a migration onto the paved road",
        "theme": "platform-engineering",
        "difficulty": "senior",
        "href": "questions/platform-engineering/plan-a-migration-onto-the-paved-road.html",
        "why": "Migration moves existing teams onto the road without coercion."
      },
      {
        "title": "Measure platform adoption",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/measure-platform-adoption.html",
        "why": "Adoption measurement says what a number can and cannot prove."
      },
      {
        "title": "Measure developer experience",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/measure-developer-experience.html",
        "why": "The judgement calls open with developer experience measured honestly."
      },
      {
        "title": "Reduce cognitive load with team topologies",
        "theme": "platform-engineering",
        "difficulty": "senior",
        "href": "questions/platform-engineering/reduce-cognitive-load-with-team-topologies.html",
        "why": "Cognitive load and interaction modes decide what the platform should absorb."
      },
      {
        "title": "Decide build versus buy for a capability",
        "theme": "platform-engineering",
        "difficulty": "senior",
        "href": "questions/platform-engineering/decide-build-versus-buy-for-a-capability.html",
        "why": "Build versus buy prices each capability the platform might own."
      },
      {
        "title": "Contain a noisy neighbour on a shared platform",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/contain-a-noisy-neighbour-on-a-shared-platform.html",
        "why": "Noisy neighbours are the multi-tenancy judgement the sharing model creates."
      },
      {
        "title": "Run a platform-wide incident",
        "theme": "platform-engineering",
        "difficulty": "middle",
        "href": "questions/platform-engineering/run-a-platform-wide-incident.html",
        "why": "Platform incident response and blast radius are the judgement under pressure."
      },
      {
        "title": "Size and staff a platform team",
        "theme": "platform-engineering",
        "difficulty": "staff",
        "href": "questions/platform-engineering/size-and-staff-a-platform-team.html",
        "why": "Cost and staffing size the team all the decisions above implied."
      },
      {
        "title": "Recognise when a platform team is the wrong answer",
        "theme": "platform-engineering",
        "difficulty": "staff",
        "href": "questions/platform-engineering/recognise-when-a-platform-team-is-the-wrong-answer.html",
        "why": "Knowing when a platform team is the wrong answer is the staff-level close."
      }
    ]
  },
  {
    "theme": "processes",
    "note": "The vocabulary of procfs, PIDs, states, and signals before lifecycles, and real service lifecycles before fleet governance.",
    "steps": [
      {
        "title": "Read a process status safely",
        "theme": "processes",
        "difficulty": "junior",
        "href": "questions/processes/read-process-status.html",
        "why": "/proc and process status are the primary sources the Theme reads first."
      },
      {
        "title": "Explain PIDs and parent processes",
        "theme": "processes",
        "difficulty": "junior",
        "href": "questions/processes/pid-and-parent-process.html",
        "why": "PIDs and parentage explain the family tree every status line belongs to."
      },
      {
        "title": "Interpret process state and load average",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/process-state-and-load.html",
        "why": "Process states and load average connect kernel state to the number everyone quotes."
      },
      {
        "title": "Choose a signal for a running process",
        "theme": "processes",
        "difficulty": "junior",
        "href": "questions/processes/signal-basics.html",
        "why": "Choosing a signal is the first act performed on a process you understand."
      },
      {
        "title": "Explain the fork exec wait lifecycle",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/fork-exec-wait-lifecycle.html",
        "why": "fork, exec, and wait explain how processes come to exist and to exit."
      },
      {
        "title": "Control file descriptor inheritance across exec",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/file-descriptor-inheritance.html",
        "why": "Descriptor inheritance decides what an exec'd child actually holds open."
      },
      {
        "title": "Model a service lifecycle with systemd",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/systemd-service-lifecycle.html",
        "why": "Unit, cgroup, and kill semantics turn kernel primitives into real service lifecycles."
      },
      {
        "title": "Diagnose a per-process resource limit",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/resource-limits.html",
        "why": "Per-process limits are the controls the lifecycle tier finally makes sensible."
      },
      {
        "title": "Define process observability without exposing secrets",
        "theme": "processes",
        "difficulty": "staff",
        "href": "questions/processes/process-observability-standard.html",
        "why": "The observability standard decides what the fleet knows about its processes."
      },
      {
        "title": "Triage a hung process without destroying evidence",
        "theme": "processes",
        "difficulty": "middle",
        "href": "questions/processes/hung-process-triage.html",
        "why": "Hung-process triage is evidence preservation under pressure, the use case the tier above serves."
      },
      {
        "title": "Design guardrails for automated process remediation",
        "theme": "processes",
        "difficulty": "staff",
        "href": "questions/processes/process-remediation-guardrails.html",
        "why": "Organization-wide guardrails close the Theme by governing automated process remediation."
      }
    ]
  },
  {
    "theme": "qemu-kvm",
    "note": "The three-boxes picture opens the Theme because every later answer assumes you know which layer owns what.",
    "steps": [
      {
        "title": "Split QEMU's job from KVM's job",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/split-qemu-from-kvm.html",
        "why": "The three-boxes picture opens the Theme: kernel, QEMU, and libvirt each own a layer."
      },
      {
        "title": "What /dev/kvm exposes to QEMU",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/what-dev-kvm-exposes.html",
        "why": "What /dev/kvm exposes makes the kernel's half of that split concrete."
      },
      {
        "title": "Why virtio beats emulated devices",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/why-virtio-beats-emulated-devices.html",
        "why": "Virtio's shared-ring mechanism is half the performance vocabulary the Theme speaks."
      },
      {
        "title": "Read a libvirt domain's states",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/read-libvirt-domain-states.html",
        "why": "Domain states are the operating grammar you read before acting on any guest."
      },
      {
        "title": "Choose raw or qcow2 for a disk image",
        "theme": "qemu-kvm",
        "difficulty": "junior",
        "href": "questions/qemu-kvm/choose-raw-or-qcow2.html",
        "why": "Raw or qcow2 is the first decision a new domain actually forces."
      },
      {
        "title": "Diagnose a guest silently running under TCG",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/diagnose-fallback-to-tcg.html",
        "why": "The silent TCG fallback is the foundations inverted, rehearsed as a 3 a.m. page."
      },
      {
        "title": "Pick bridged or macvtap guest networking",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/pick-bridged-or-macvtap.html",
        "why": "Bridged versus macvtap carries the other surprise every operator meets exactly once."
      },
      {
        "title": "Use the QEMU monitor without desyncing libvirt",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/use-the-qemu-monitor-without-desync.html",
        "why": "The monitor ownership rule keeps every later procedure truthful with libvirt."
      },
      {
        "title": "Convert and rebase disk images with qemu-img",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/convert-and-rebase-with-qemu-img.html",
        "why": "The storage line runs image-first: convert and rebase with qemu-img."
      },
      {
        "title": "Model storage as libvirt pools and volumes",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/model-storage-as-pools-and-volumes.html",
        "why": "Pools and volumes manage what qemu-img just produced."
      },
      {
        "title": "Choose internal or external disk snapshots",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/choose-internal-or-external-snapshots.html",
        "why": "Snapshots are the point-in-time decision on top of managed storage."
      },
      {
        "title": "Operate memory ballooning under host pressure",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/operate-memory-ballooning.html",
        "why": "Ballooning is the memory lever pulled when host memory runs short."
      },
      {
        "title": "Decide when nested virtualization is worth it",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/decide-on-nested-virtualization.html",
        "why": "Nested virtualization returns to the TCG diagnosis's outer-hypervisor cause, priced this time."
      },
      {
        "title": "Run a live migration you can trust",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/run-a-live-migration-you-trust.html",
        "why": "The senior band opens with migration, which consumes CPU modes, shared storage, and downtime budgets in one motion."
      },
      {
        "title": "Choose a libvirt CPU mode for a fleet",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/choose-a-libvirt-cpu-mode.html",
        "why": "Migration silently assumes the target serves the exact CPU the guest booted with, so the fleet CPU-mode decision lands directly after it."
      },
      {
        "title": "Respect machine types when editing guests",
        "theme": "qemu-kvm",
        "difficulty": "middle",
        "href": "questions/qemu-kvm/respect-machine-types.html",
        "why": "Machine types obey the same rule as CPU modes: never silently change what the guest booted last time."
      },
      {
        "title": "Find where virtualization steals your performance",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/find-virtualization-overhead.html",
        "why": "The overhead investigation supplies the evidence discipline that settles the hypervisor-tax argument."
      },
      {
        "title": "Pin a latency-sensitive VM to NUMA and hugepages",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/pin-a-vm-to-numa-and-hugepages.html",
        "why": "NUMA pinning and hugepages buy latency by constraining placement."
      },
      {
        "title": "Design backups for running VMs",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/design-running-vm-backups.html",
        "why": "Backups for running VMs join the snapshot machinery with consistency."
      },
      {
        "title": "Secure libvirt and QEMU access on a shared host",
        "theme": "qemu-kvm",
        "difficulty": "senior",
        "href": "questions/qemu-kvm/secure-libvirt-and-qemu-access.html",
        "why": "The shared-host permissions model is the one the TCG diagnosis only hinted at."
      },
      {
        "title": "Design live migration for a fleet with mixed CPU generations",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/migrate-a-fleet-with-mixed-cpus.html",
        "why": "The staff band opens with fleet migration across mixed CPU generations."
      },
      {
        "title": "Set an honest overcommit policy for a VM fleet",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/set-an-honest-overcommit-policy.html",
        "why": "The overcommit policy makes fleet capacity a contract rather than a ratio."
      },
      {
        "title": "Choose the storage architecture for a VM fleet",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/choose-fleet-vm-storage.html",
        "why": "The fleet storage architecture is the storage line at fleet scale."
      },
      {
        "title": "Harden a multi-tenant KVM host",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/harden-a-multi-tenant-kvm-host.html",
        "why": "Hardening a shared host is isolation with adversaries, not just tenants."
      },
      {
        "title": "Govern QEMU upgrades across a fleet",
        "theme": "qemu-kvm",
        "difficulty": "staff",
        "href": "questions/qemu-kvm/govern-qemu-upgrades.html",
        "why": "A governed upgrade is machine types, migration, and hardening used as one maintenance motion: the whole course as a single change."
      }
    ]
  },
  {
    "theme": "queue-messaging",
    "note": "Semantics, routing, and delivery guarantees before platform mechanics, and the platform questions — security, recovery, SLOs — last.",
    "steps": [
      {
        "title": "Choose a work queue or an event log",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/choose-a-queue-or-log.html",
        "why": "Queue versus log semantics decide deletion, replay, and ordering before any platform is chosen."
      },
      {
        "title": "Explain RabbitMQ exchanges, bindings, and queues",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/explain-rabbitmq-routing.html",
        "why": "Routing through exchanges and bindings is the vocabulary of the queue side."
      },
      {
        "title": "Acknowledge RabbitMQ work safely",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/acknowledge-rabbitmq-work-safely.html",
        "why": "Acknowledgements make at-least-once work safe on the queue side."
      },
      {
        "title": "Explain at-most-once, at-least-once, and exactly-once claims",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/explain-delivery-semantics.html",
        "why": "Delivery semantics are end-to-end claims, and exactly-once stops at the consumer."
      },
      {
        "title": "Explain Kafka topics and partitions",
        "theme": "queue-messaging",
        "difficulty": "junior",
        "href": "questions/queue-messaging/explain-kafka-topics-and-partitions.html",
        "why": "Topics and partitions are the log platform's unit of both parallelism and ordering."
      },
      {
        "title": "Preserve required ordering in asynchronous processing",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/preserve-order-in-async-processing.html",
        "why": "Ordering per key is what partitions make possible, made deliberate here."
      },
      {
        "title": "Commit Kafka offsets after processing effects",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/commit-kafka-offsets-after-effects.html",
        "why": "Committing offsets after effects is the smallest dual-write, met before any general pattern."
      },
      {
        "title": "Handle Kafka consumer rebalances safely",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/handle-kafka-consumer-rebalances.html",
        "why": "Rebalances are the log platform's failure choreography for consumers."
      },
      {
        "title": "Choose Kafka retention or log compaction",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/choose-kafka-retention-or-compaction.html",
        "why": "Retention versus compaction is what the log keeps, and for whom."
      },
      {
        "title": "Manage event schema evolution",
        "theme": "queue-messaging",
        "difficulty": "senior",
        "href": "questions/queue-messaging/manage-event-schema-evolution.html",
        "why": "Schema evolution keeps producers and consumers compatible across time."
      },
      {
        "title": "Plan Kafka partition capacity",
        "theme": "queue-messaging",
        "difficulty": "senior",
        "href": "questions/queue-messaging/plan-kafka-partition-capacity.html",
        "why": "Partition capacity prices the parallelism everything above assumed."
      },
      {
        "title": "Design multi-tenant messaging security",
        "theme": "queue-messaging",
        "difficulty": "staff",
        "href": "questions/queue-messaging/design-multi-tenant-messaging-security.html",
        "why": "The platform tier opens with tenants kept apart on shared brokers."
      },
      {
        "title": "Design Kafka disaster recovery",
        "theme": "queue-messaging",
        "difficulty": "senior",
        "href": "questions/queue-messaging/design-kafka-disaster-recovery.html",
        "why": "Disaster recovery for the log platform replays what retention kept."
      },
      {
        "title": "Triage Kafka consumer lag",
        "theme": "queue-messaging",
        "difficulty": "middle",
        "href": "questions/queue-messaging/triage-kafka-consumer-lag.html",
        "why": "Consumer lag is the platform's daily symptom, triaged before the worst day."
      },
      {
        "title": "Respond to a RabbitMQ cluster incident",
        "theme": "queue-messaging",
        "difficulty": "senior",
        "href": "questions/queue-messaging/respond-to-rabbitmq-cluster-incident.html",
        "why": "The RabbitMQ cluster incident is the queue side's own worst day."
      },
      {
        "title": "Define messaging platform SLOs",
        "theme": "queue-messaging",
        "difficulty": "staff",
        "href": "questions/queue-messaging/define-messaging-slos.html",
        "why": "Reliability SLOs close the Theme by promising what the platform delivers."
      }
    ]
  },
  {
    "theme": "security",
    "note": "Identity, access control, secrets, and TLS before delivery and container controls, then detection and incident handling, then the risk governance and recovery design that spend them.",
    "steps": [
      {
        "title": "Apply least privilege to a workload identity",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/least-privilege-iam.html",
        "why": "Identity opens the Theme because every later control binds itself to one."
      },
      {
        "title": "Choose multi-factor authentication for privileged access",
        "theme": "security",
        "difficulty": "junior",
        "href": "questions/security/multi-factor-authentication.html",
        "why": "MFA for privileged access is the identity tier's strongest gate."
      },
      {
        "title": "Design zero-trust service access",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/zero-trust-service-access.html",
        "why": "Zero-trust access removes network location as an implicit grant."
      },
      {
        "title": "Describe a secure secret-management lifecycle",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/secret-management-lifecycle.html",
        "why": "The secret lifecycle governs the credentials the identity tier issues."
      },
      {
        "title": "Store application passwords safely",
        "theme": "security",
        "difficulty": "junior",
        "href": "questions/security/password-storage.html",
        "why": "Storing passwords safely is that lifecycle's most abused corner."
      },
      {
        "title": "Explain TLS certificate validation",
        "theme": "security",
        "difficulty": "junior",
        "href": "questions/security/tls-certificate-basics.html",
        "why": "TLS validation is the transport trust the tiers above ride on."
      },
      {
        "title": "Set web security headers deliberately",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/security-headers.html",
        "why": "Security headers complete the browser-facing controls of the transport tier."
      },
      {
        "title": "Secure shared CI runners",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/secure-ci-runners.html",
        "why": "Secure delivery opens with the runners, where pipeline code meets secrets."
      },
      {
        "title": "Deliver secrets to a GitOps-reconciled cluster",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/gitops-secret-delivery.html",
        "why": "Secret delivery to a reconciled cluster keeps GitOps honest about sensitive state."
      },
      {
        "title": "Verify container image provenance before deployment",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/container-image-provenance.html",
        "why": "Image provenance verifies what the delivery tier actually ships."
      },
      {
        "title": "Harden a container runtime workload",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/container-runtime-hardening.html",
        "why": "Runtime hardening bounds what the shipped workloads may do."
      },
      {
        "title": "Enforce Kubernetes Pod Security Standards",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/kubernetes-pod-security.html",
        "why": "Pod Security Standards enforce that hardening at the platform boundary."
      },
      {
        "title": "Design software supply-chain controls",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/software-supply-chain-controls.html",
        "why": "Supply-chain controls compose signing, provenance, and verification into one system."
      },
      {
        "title": "Design useful security event logging",
        "theme": "security",
        "difficulty": "junior",
        "href": "questions/security/security-logging-basics.html",
        "why": "Detection opens with deciding which events are worth logging."
      },
      {
        "title": "Triage a suspected security incident",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/security-incident-triage.html",
        "why": "Incident triage decides what the detected events actually mean."
      },
      {
        "title": "Respond to a leaked production secret",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/secret-leak-response.html",
        "why": "A leaked secret gets a response runbook, not just a rotation."
      },
      {
        "title": "Triage a production vulnerability report",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/vulnerability-triage.html",
        "why": "Vulnerability reports are triaged by exploitation reality, not CVSS folklore."
      },
      {
        "title": "Manage vulnerable application dependencies",
        "theme": "security",
        "difficulty": "middle",
        "href": "questions/security/dependency-vulnerability-management.html",
        "why": "Dependency management is vulnerability triage at fleet scale."
      },
      {
        "title": "Explain risk-based patch management",
        "theme": "security",
        "difficulty": "junior",
        "href": "questions/security/patch-management-basics.html",
        "why": "Risk-based patching closes detection and response with a defensible cadence."
      },
      {
        "title": "Design production network segmentation",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/production-segmentation.html",
        "why": "Resilience opens with segmentation that contains the blast radius."
      },
      {
        "title": "Design recoverable backups for ransomware",
        "theme": "security",
        "difficulty": "senior",
        "href": "questions/security/ransomware-recovery-design.html",
        "why": "Ransomware recovery assumes the adversary held the backups too."
      },
      {
        "title": "Govern security-control exceptions",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/security-exception-governance.html",
        "why": "Risk governance opens with exceptions that are owned, priced, and expiring."
      },
      {
        "title": "Define security metrics that drive engineering decisions",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/security-metrics-program.html",
        "why": "Metrics exist to drive engineering decisions rather than dashboard theatre."
      },
      {
        "title": "Establish a security platform risk model",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/security-platform-risk-model.html",
        "why": "The platform risk model names what the organization explicitly accepts."
      },
      {
        "title": "Deliver secure platform defaults at scale",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/secure-platform-defaults.html",
        "why": "Secure defaults at scale make the safe path the easy path for every team."
      },
      {
        "title": "Build organization-wide incident readiness",
        "theme": "security",
        "difficulty": "staff",
        "href": "questions/security/organization-incident-readiness.html",
        "why": "Organization-wide readiness is the Theme's close: every control rehearsed together."
      }
    ]
  },
  {
    "theme": "serverless",
    "note": "Execution model and invocation semantics before idempotency and concurrency, because the platform's delivery rules decide what correctness costs.",
    "steps": [
      {
        "title": "Explain the serverless function execution model",
        "theme": "serverless",
        "difficulty": "junior",
        "href": "questions/serverless/explain-serverless-execution-model.html",
        "why": "The execution model comes first because everything disappears between requests."
      },
      {
        "title": "Explain serverless payload, memory, and duration limits",
        "theme": "serverless",
        "difficulty": "junior",
        "href": "questions/serverless/explain-function-payload-limits.html",
        "why": "Quotas are the platform's opinions, learned before they bite in production."
      },
      {
        "title": "Explain synchronous and asynchronous serverless invocation",
        "theme": "serverless",
        "difficulty": "junior",
        "href": "questions/serverless/explain-invocation-delivery-semantics.html",
        "why": "Synchronous, asynchronous, and poll-based invocation decide who owns the retry."
      },
      {
        "title": "Design idempotent serverless functions",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/design-idempotent-functions.html",
        "why": "Idempotency is practised against the delivery semantics established above."
      },
      {
        "title": "Design idempotent serverless event processing",
        "theme": "serverless",
        "difficulty": "senior",
        "href": "questions/serverless/design-idempotent-serverless-events.html",
        "why": "Event-processing idempotency separates the event key from the business key."
      },
      {
        "title": "Design serverless function timeouts and deadlines",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/design-function-timeouts.html",
        "why": "Timeouts and deadlines bound exactly what the platform will retry."
      },
      {
        "title": "Handle serverless failures and poison events",
        "theme": "serverless",
        "difficulty": "senior",
        "href": "questions/serverless/handle-serverless-failures.html",
        "why": "Failure and poison-event handling is where those retries finally surface."
      },
      {
        "title": "Manage serverless function concurrency safely",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/manage-function-concurrency.html",
        "why": "Concurrency controls protect the backing services from the whole fleet."
      },
      {
        "title": "Manage database connections from serverless functions",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/manage-serverless-database-connections.html",
        "why": "Connection management is the stateful dependency serverless starves."
      },
      {
        "title": "Reduce a serverless deployment package and its dependency weight",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/reduce-function-package-size.html",
        "why": "Packaging closes the practised tier with cold-start economics."
      },
      {
        "title": "Trace a request across ephemeral serverless components",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/trace-ephemeral-function-requests.html",
        "why": "Tracing ephemeral compute is the observability you cannot log into."
      },
      {
        "title": "Control serverless cost without hiding demand",
        "theme": "serverless",
        "difficulty": "senior",
        "href": "questions/serverless/control-serverless-cost.html",
        "why": "Cost attribution watches the demand the concurrency tier just throttled."
      },
      {
        "title": "Secure serverless function identity",
        "theme": "serverless",
        "difficulty": "middle",
        "href": "questions/serverless/secure-function-identity.html",
        "why": "Least-privilege execution roles bound what each function may touch."
      },
      {
        "title": "Decide between managed functions and long-running compute",
        "theme": "serverless",
        "difficulty": "staff",
        "href": "questions/serverless/choose-serverless-versus-long-running-compute.html",
        "why": "When managed functions beat long-running services is the platform-level close."
      }
    ]
  },
  {
    "theme": "service-mesh",
    "note": "The control-plane, data-plane, and identity model first, practice in a disposable cluster second, ownership decisions last.",
    "steps": [
      {
        "title": "Distinguish a mesh control plane from its data plane",
        "theme": "service-mesh",
        "difficulty": "junior",
        "href": "questions/service-mesh/service-mesh-control-data-plane.html",
        "why": "The control-plane and data-plane split explains what a mesh actually adds."
      },
      {
        "title": "Explain workload identity in a service mesh",
        "theme": "service-mesh",
        "difficulty": "junior",
        "href": "questions/service-mesh/service-mesh-identity.html",
        "why": "Workload identity is the foundation everything else the mesh promises stands on."
      },
      {
        "title": "Verify sidecar enrollment before troubleshooting mesh policy",
        "theme": "service-mesh",
        "difficulty": "junior",
        "href": "questions/service-mesh/service-mesh-sidecar-injection.html",
        "why": "Enrollment is verified before policy, or nothing downstream can even be debugged."
      },
      {
        "title": "Enforce Istio mutual TLS incrementally",
        "theme": "service-mesh",
        "difficulty": "senior",
        "href": "questions/service-mesh/istio-mutual-tls.html",
        "why": "Mutual TLS is enforced incrementally once enrollment is trustworthy."
      },
      {
        "title": "Route mesh traffic with a VirtualService",
        "theme": "service-mesh",
        "difficulty": "middle",
        "href": "questions/service-mesh/istio-virtualservice-routing.html",
        "why": "Traffic management opens with the routing rules a mesh can express."
      },
      {
        "title": "Apply traffic policies with a DestinationRule",
        "theme": "service-mesh",
        "difficulty": "middle",
        "href": "questions/service-mesh/istio-destination-rule-policies.html",
        "why": "DestinationRules carry the traffic and resilience policies routing depends on."
      },
      {
        "title": "Shift traffic progressively with Istio",
        "theme": "service-mesh",
        "difficulty": "senior",
        "href": "questions/service-mesh/istio-progressive-traffic-shift.html",
        "why": "Progressive traffic shifts are traffic management with a safety contract."
      },
      {
        "title": "Configure Istio ingress and egress boundaries",
        "theme": "service-mesh",
        "difficulty": "middle",
        "href": "questions/service-mesh/istio-ingress-egress-gateways.html",
        "why": "Gateways govern where mesh traffic meets the outside world."
      },
      {
        "title": "Use mesh telemetry without mistaking it for complete observability",
        "theme": "service-mesh",
        "difficulty": "junior",
        "href": "questions/service-mesh/service-mesh-observability.html",
        "why": "Mesh telemetry is used without mistaking it for complete observability."
      },
      {
        "title": "Upgrade Istio with a bounded canary",
        "theme": "service-mesh",
        "difficulty": "staff",
        "href": "questions/service-mesh/istio-canary-upgrade.html",
        "why": "Upgrades come late because they risk everything above them at once."
      },
      {
        "title": "Design service-mesh boundaries across multiple clusters",
        "theme": "service-mesh",
        "difficulty": "staff",
        "href": "questions/service-mesh/service-mesh-multicluster-boundaries.html",
        "why": "Multicluster boundaries extend the identity and policy model across clusters."
      },
      {
        "title": "Make a service-mesh adoption decision with measurable outcomes",
        "theme": "service-mesh",
        "difficulty": "staff",
        "href": "questions/service-mesh/service-mesh-adoption-decision.html",
        "why": "The adoption decision is made with measurable outcomes, after the mechanics are known."
      },
      {
        "title": "Establish safe service-mesh platform guardrails",
        "theme": "service-mesh",
        "difficulty": "staff",
        "href": "questions/service-mesh/service-mesh-platform-guardrails.html",
        "why": "Platform guardrails close the Theme: whether the mesh improves reliability or merely complicates it."
      }
    ]
  },
  {
    "theme": "shell-scripting",
    "note": "The contract before the tricks: interpreter, exit statuses, and quoting carry every later technique from snippet to fleet service.",
    "steps": [
      {
        "title": "Execute a shell script with an explicit interpreter",
        "theme": "shell-scripting",
        "difficulty": "junior",
        "href": "questions/shell-scripting/execute-a-script-portably.html",
        "why": "Running with an explicit interpreter is the contract underneath every later technique."
      },
      {
        "title": "Use exit statuses as an automation contract",
        "theme": "shell-scripting",
        "difficulty": "junior",
        "href": "questions/shell-scripting/use-exit-statuses.html",
        "why": "Exit statuses are the automation contract everything downstream reads."
      },
      {
        "title": "Explain shell quoting and variable expansion",
        "theme": "shell-scripting",
        "difficulty": "junior",
        "href": "questions/shell-scripting/shell-quoting-and-expansion.html",
        "why": "Quoting and variable expansion under control is the third thing every later technique defends."
      },
      {
        "title": "Prevent command injection in an automation script",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/avoid-command-injection.html",
        "why": "Command injection is what uncontrolled quoting costs, met immediately after quoting."
      },
      {
        "title": "Handle shell-script arguments without losing boundaries",
        "theme": "shell-scripting",
        "difficulty": "junior",
        "href": "questions/shell-scripting/handle-script-arguments.html",
        "why": "Argument boundaries extend the contract to the inputs a script accepts."
      },
      {
        "title": "Parse command-line options with getopts",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/parse-options-with-getopts.html",
        "why": "getopts parses options without losing the boundaries established above."
      },
      {
        "title": "Use Bash arrays for command arguments",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/use-arrays-for-arguments.html",
        "why": "Arrays carry command arguments as words rather than one fragile string."
      },
      {
        "title": "Read arbitrary input lines safely in Bash",
        "theme": "shell-scripting",
        "difficulty": "junior",
        "href": "questions/shell-scripting/read-lines-safely.html",
        "why": "Reading arbitrary input lines safely is the boundary tier's last skill."
      },
      {
        "title": "Preserve the failed command in a pipeline",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/preserve-pipeline-failures.html",
        "why": "Pipelines that preserve the failed command extend the exit-status contract."
      },
      {
        "title": "Use command substitution without hiding failures",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/use-command-substitution-deliberately.html",
        "why": "Command substitution used deliberately does not hide the failures inside it."
      },
      {
        "title": "Apply Bash strict mode with context",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/choose-strict-mode.html",
        "why": "Strict mode is the first step from snippet toward service."
      },
      {
        "title": "Create and clean temporary files safely",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/manage-temporary-files.html",
        "why": "Temporary-file hygiene keeps the service from littering its host."
      },
      {
        "title": "Handle termination signals and cleanup",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/handle-signals-and-cleanup.html",
        "why": "Termination signals and cleanup make the exit paths deliberate."
      },
      {
        "title": "Prevent overlapping scheduled script runs",
        "theme": "shell-scripting",
        "difficulty": "senior",
        "href": "questions/shell-scripting/lock-singleton-job.html",
        "why": "Preventing overlapping scheduled runs completes the snippet-to-service tier."
      },
      {
        "title": "Make a remediation script idempotent",
        "theme": "shell-scripting",
        "difficulty": "senior",
        "href": "questions/shell-scripting/implement-idempotent-remediation.html",
        "why": "The fleet tier opens with remediation that is safe to re-run."
      },
      {
        "title": "Control concurrent jobs in a Bash worker",
        "theme": "shell-scripting",
        "difficulty": "senior",
        "href": "questions/shell-scripting/control-concurrent-jobs.html",
        "why": "Controlled concurrency keeps the worker from stampeding the fleet it serves."
      },
      {
        "title": "Make shell-script logs useful without leaking secrets",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/log-without-secrets.html",
        "why": "Fleet logs stay useful without leaking the secrets they pass near."
      },
      {
        "title": "Debug a failing production script safely",
        "theme": "shell-scripting",
        "difficulty": "senior",
        "href": "questions/shell-scripting/debug-production-script-safely.html",
        "why": "Debugging in production preserves evidence rather than destroying it."
      },
      {
        "title": "Test a shell script before production",
        "theme": "shell-scripting",
        "difficulty": "senior",
        "href": "questions/shell-scripting/test-shell-scripts.html",
        "why": "Testing before production is the fleet tier's own gate."
      },
      {
        "title": "Find shell-script defects before deployment",
        "theme": "shell-scripting",
        "difficulty": "middle",
        "href": "questions/shell-scripting/debug-with-shellcheck.html",
        "why": "Static defect-finding wraps the fleet tier from the outside."
      },
      {
        "title": "Govern the shell-script supply chain",
        "theme": "shell-scripting",
        "difficulty": "staff",
        "href": "questions/shell-scripting/govern-shell-script-supply-chain.html",
        "why": "Supply-chain governance wraps the same tier from the other side."
      },
      {
        "title": "Decide when to replace a shell script",
        "theme": "shell-scripting",
        "difficulty": "staff",
        "href": "questions/shell-scripting/decide-when-to-replace-shell.html",
        "why": "The judgement tier opens with knowing when shell is the wrong tool."
      },
      {
        "title": "Measure shell-automation reliability",
        "theme": "shell-scripting",
        "difficulty": "staff",
        "href": "questions/shell-scripting/measure-automation-reliability.html",
        "why": "Reliability measurement makes the fleet's scripts an accountable service."
      },
      {
        "title": "Design a fleet-remediation runbook",
        "theme": "shell-scripting",
        "difficulty": "staff",
        "href": "questions/shell-scripting/design-fleet-remediation-runbook.html",
        "why": "The runbook owes its reader judgement, not just a command list."
      },
      {
        "title": "Define a safe shell-automation standard",
        "theme": "shell-scripting",
        "difficulty": "staff",
        "href": "questions/shell-scripting/define-shell-automation-standard.html",
        "why": "The organization-wide standard closes the Theme by deciding what to actually mandate."
      }
    ]
  },
  {
    "theme": "sre",
    "note": "Take the promise first — reliability, user-journey SLI, error budget — because alerting, incidents, and governance are all arithmetic on it.",
    "steps": [
      {
        "title": "Define service reliability and the role of an SRE",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/define-service-reliability.html",
        "why": "The promise comes first: reliability as a measured user outcome, SRE as shared ownership of it."
      },
      {
        "title": "Choose a user-journey SLI",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/define-user-journey-sli.html",
        "why": "The user-journey SLI makes the promise arithmetic, which is why it precedes any budget."
      },
      {
        "title": "Explain an error budget",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/explain-error-budget.html",
        "why": "The budget is arithmetic on the SLI, and the SLI is a claim about users."
      },
      {
        "title": "Classify an alert as a page, ticket, or log",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/classify-alert-urgency.html",
        "why": "Alerting follows definitions: page, ticket, or log is the cheapest filter in the Theme."
      },
      {
        "title": "Design a multi-window burn-rate alert",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/design-multiwindow-burn-alert.html",
        "why": "The multi-window burn alert spends the budget's maths the definitions built."
      },
      {
        "title": "Establish an effective on-call handoff",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/establish-oncall-handoff.html",
        "why": "The incident arc reads like a shift, and it opens with a real handoff."
      },
      {
        "title": "Assign incident-management roles",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/assign-incident-roles.html",
        "why": "Roles keep the incident organized before the pressure actually arrives."
      },
      {
        "title": "Triage a production incident",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/triage-production-incident.html",
        "why": "Triage is the single-responder method running inside a declared incident."
      },
      {
        "title": "Coordinate a major incident across teams",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/coordinate-major-incident.html",
        "why": "The cross-team major incident scales the same method across organizations."
      },
      {
        "title": "Write an actionable runbook",
        "theme": "sre",
        "difficulty": "junior",
        "href": "questions/sre/write-actionable-runbook.html",
        "why": "The actionable runbook makes the recurring work of the arc repeatable."
      },
      {
        "title": "Write a blameless postmortem",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/write-blameless-postmortem.html",
        "why": "The blameless postmortem closes the arc on the evidence every step preserved."
      },
      {
        "title": "Prevent cascading failures",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/prevent-cascading-failures.html",
        "why": "Reliability engineering proper opens with cascades contained as one compatible system."
      },
      {
        "title": "Protect a service from overload",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/protect-service-from-overload.html",
        "why": "Overload protection is admission control at the service's own limits."
      },
      {
        "title": "Manage critical state for reliability",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/manage-critical-state.html",
        "why": "Critical state is named and protected, never discovered mid-failure."
      },
      {
        "title": "Test a disaster-recovery plan",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/test-disaster-recovery.html",
        "why": "The disaster-recovery plan is tested, or it is only a document."
      },
      {
        "title": "Plan service capacity",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/plan-service-capacity.html",
        "why": "Capacity planning turns forecast demand into provisioned headroom with a defensible margin."
      },
      {
        "title": "Run a production-readiness review",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/run-production-readiness-review.html",
        "why": "The readiness review walks every earlier step for a service you did not build."
      },
      {
        "title": "Measure and reduce toil",
        "theme": "sre",
        "difficulty": "middle",
        "href": "questions/sre/measure-and-reduce-toil.html",
        "why": "Toil is priced after the incident work, because you can only price what you have felt."
      },
      {
        "title": "Measure platform impact with DORA metrics without gaming teams",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/measure-platform-impact-with-dora.html",
        "why": "DORA metrics are trusted only once you have watched teams try to game them."
      },
      {
        "title": "Govern an error-budget policy",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/govern-error-budget-policy.html",
        "why": "The budget policy is the organizational decision the arithmetic was always heading toward."
      },
      {
        "title": "Define an SRE engagement model",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/define-sre-engagement-model.html",
        "why": "The engagement model decides how SRE meets its partner teams."
      },
      {
        "title": "Establish service ownership and reliability accountability",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/establish-service-ownership.html",
        "why": "Ownership and accountability name who answers for reliability in the end."
      },
      {
        "title": "Design an organizational incident-management program",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/design-organizational-incident-program.html",
        "why": "The incident program scales the whole arc beyond one team's shift."
      },
      {
        "title": "Design a reliable product launch",
        "theme": "sre",
        "difficulty": "senior",
        "href": "questions/sre/design-reliable-launch.html",
        "why": "The reliable launch applies every prior habit to a brand-new service."
      },
      {
        "title": "Build a reliability investment roadmap",
        "theme": "sre",
        "difficulty": "staff",
        "href": "questions/sre/build-reliability-roadmap.html",
        "why": "The roadmap closes the Theme by turning everything above into funded work."
      }
    ]
  },
  {
    "theme": "storage",
    "note": "The shape question comes first because block, file, or object decides every later answer, and the close is platform scope.",
    "steps": [
      {
        "title": "Choose between block, file, and object storage",
        "theme": "storage",
        "difficulty": "junior",
        "href": "questions/storage/block-file-object-storage.html",
        "why": "Block, file, or object comes first because it decides every later answer."
      },
      {
        "title": "Mount persistent storage safely on Linux",
        "theme": "storage",
        "difficulty": "junior",
        "href": "questions/storage/mount-persistent-storage.html",
        "why": "Mounting persistent storage safely is the hands-on first step."
      },
      {
        "title": "Operate NFS shared storage safely",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/operate-nfs-shared-storage.html",
        "why": "NFS as the first real workload teaches shared storage's surprises early."
      },
      {
        "title": "Choose block-volume performance for a workload",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/choose-volume-performance.html",
        "why": "The performance and protection pairing opens with choosing block-volume performance for the workload."
      },
      {
        "title": "Create an application-consistent volume snapshot",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/design-consistent-snapshot.html",
        "why": "Application-consistent snapshots capture state that is actually restorable."
      },
      {
        "title": "Plan for performance when restoring a volume from a snapshot",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/handle-snapshot-restore-latency.html",
        "why": "Restore-from-snapshot planning prices the latency the snapshot hid."
      },
      {
        "title": "Distinguish backups from storage snapshots",
        "theme": "storage",
        "difficulty": "junior",
        "href": "questions/storage/distinguish-backups-and-snapshots.html",
        "why": "The distinction is stated before the exercise that proves it."
      },
      {
        "title": "Run a meaningful backup restore exercise",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/restore-backup-exercise.html",
        "why": "The restore exercise is what a backup claim is finally worth."
      },
      {
        "title": "Diagnose a full filesystem when free space remains",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/inode-exhaustion.html",
        "why": "The incident set opens with the full filesystem that still shows free space."
      },
      {
        "title": "Recover storage held by deleted open files",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/diagnose-deleted-open-files.html",
        "why": "Space held by deleted open files is the storage incident everyone meets once."
      },
      {
        "title": "Respond to suspected filesystem corruption",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/diagnose-filesystem-corruption.html",
        "why": "Suspected corruption is responded to, not blindly repaired."
      },
      {
        "title": "Explain RAID redundancy and its limits",
        "theme": "storage",
        "difficulty": "junior",
        "href": "questions/storage/explain-raid-redundancy.html",
        "why": "RAID limits sit between the incidents and the rebuild that actually kills arrays."
      },
      {
        "title": "Plan a degraded RAID rebuild without compounding risk",
        "theme": "storage",
        "difficulty": "senior",
        "href": "questions/storage/plan-raid-rebuild-risk.html",
        "why": "The degraded rebuild is planned because a rebuild is when an array dies."
      },
      {
        "title": "Investigate a storage latency incident",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/investigate-storage-latency.html",
        "why": "The storage latency incident closes the incident set."
      },
      {
        "title": "Design database point-in-time recovery",
        "theme": "storage",
        "difficulty": "senior",
        "href": "questions/storage/database-point-in-time-recovery.html",
        "why": "The resilience tier opens with database point-in-time recovery as its strictest form."
      },
      {
        "title": "Design cross-region storage recovery",
        "theme": "storage",
        "difficulty": "senior",
        "href": "questions/storage/design-cross-region-recovery.html",
        "why": "Cross-region recovery spends the resilience tier at distance."
      },
      {
        "title": "Design immutable recovery copies against ransomware",
        "theme": "storage",
        "difficulty": "senior",
        "href": "questions/storage/design-immutable-recovery.html",
        "why": "Immutable copies assume the ransomware reached everything else first."
      },
      {
        "title": "Design an object-storage lifecycle policy",
        "theme": "storage",
        "difficulty": "middle",
        "href": "questions/storage/manage-object-lifecycle.html",
        "why": "The object lifecycle policy automates what retention demands of objects."
      },
      {
        "title": "Govern data retention and deletion across storage systems",
        "theme": "storage",
        "difficulty": "staff",
        "href": "questions/storage/govern-data-retention.html",
        "why": "Retention governance closes the resilience tier with deletion as a duty."
      },
      {
        "title": "Set storage SLOs for a platform",
        "theme": "storage",
        "difficulty": "staff",
        "href": "questions/storage/set-storage-slos.html",
        "why": "Platform scope opens with SLOs the storage platform will defend."
      },
      {
        "title": "Use storage quotas without surprising tenants",
        "theme": "storage",
        "difficulty": "junior",
        "href": "questions/storage/control-storage-quotas.html",
        "why": "Quotas allocate the platform's storage without surprising the tenants who hit them."
      },
      {
        "title": "Migrate stateful storage with controlled downtime",
        "theme": "storage",
        "difficulty": "senior",
        "href": "questions/storage/migrate-stateful-storage.html",
        "why": "Stateful migration moves live data with controlled downtime."
      },
      {
        "title": "Manage storage cost and capacity as a portfolio",
        "theme": "storage",
        "difficulty": "staff",
        "href": "questions/storage/manage-storage-cost-and-capacity.html",
        "why": "Cost and capacity as a portfolio prices the whole estate together."
      },
      {
        "title": "Lead an organization-wide storage disaster-recovery strategy",
        "theme": "storage",
        "difficulty": "staff",
        "href": "questions/storage/lead-storage-disaster-recovery.html",
        "why": "The organization-wide disaster-recovery strategy is storage's staff-level close."
      },
      {
        "title": "Build a self-service storage platform with guardrails",
        "theme": "storage",
        "difficulty": "staff",
        "href": "questions/storage/build-self-service-storage-platform.html",
        "why": "The self-service platform wraps the whole subject in guardrails."
      }
    ]
  },
  {
    "theme": "systems-performance",
    "note": "Method before metrics, resources before tools, tools before benchmark validity — the staff tier spends the whole method.",
    "steps": [
      {
        "title": "Why establish a baseline before performance tuning?",
        "theme": "systems-performance",
        "difficulty": "junior",
        "href": "questions/systems-performance/baseline-before-tuning.html",
        "why": "A baseline is why tuning can be judged at all, so method comes before metrics."
      },
      {
        "title": "How do you apply the USE method to a production resource?",
        "theme": "systems-performance",
        "difficulty": "junior",
        "href": "questions/systems-performance/use-method-basics.html",
        "why": "The USE method turns checking everything into a directed question."
      },
      {
        "title": "What is the difference between CPU utilization and CPU saturation?",
        "theme": "systems-performance",
        "difficulty": "junior",
        "href": "questions/systems-performance/cpu-utilization-and-saturation.html",
        "why": "Utilization versus saturation decides which question to ask next of a resource."
      },
      {
        "title": "What is a safe first pass for investigating unexpected CPU consumption?",
        "theme": "systems-performance",
        "difficulty": "junior",
        "href": "questions/systems-performance/cpu-profiling-first-pass.html",
        "why": "CPU leads the resources with a safe first pass on unexpected consumption."
      },
      {
        "title": "When are high context-switch rates a performance concern?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/context-switch-investigation.html",
        "why": "Context-switch rates matter only against a threshold worth the name."
      },
      {
        "title": "How do you investigate high CPU steal time on a virtual machine?",
        "theme": "systems-performance",
        "difficulty": "senior",
        "href": "questions/systems-performance/cpu-steal-time-cloud.html",
        "why": "Steal time is somebody else's saturation billed to your virtual machine."
      },
      {
        "title": "How do you prove lock contention is causing an application latency regression?",
        "theme": "systems-performance",
        "difficulty": "senior",
        "href": "questions/systems-performance/lock-contention-analysis.html",
        "why": "Proving lock contention closes the CPU chapter where the application meets the scheduler."
      },
      {
        "title": "Which signals distinguish memory use from memory pressure on Linux?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/memory-pressure-signals.html",
        "why": "Memory opens with use versus pressure, the distinction everything leans on."
      },
      {
        "title": "How does the Linux page cache affect filesystem performance measurements?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/filesystem-cache-behavior.html",
        "why": "The page cache explains the filesystem measurements that confused everyone."
      },
      {
        "title": "What does Linux pressure stall information add to resource monitoring?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/pressure-stall-information.html",
        "why": "PSI quantifies the stall the pressure signals could only infer."
      },
      {
        "title": "How do you investigate an OOM-killer incident without treating the kill as the root cause?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/oom-killer-incident.html",
        "why": "The OOM investigation refuses to treat the kill itself as the root cause."
      },
      {
        "title": "How do you break down elevated disk I/O latency?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/disk-latency-breakdown.html",
        "why": "Storage follows the memory chapter with a structured disk-latency breakdown."
      },
      {
        "title": "How do TCP retransmissions inform a latency investigation?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/network-retransmission-triage.html",
        "why": "TCP retransmissions inform the latency investigation from the network side."
      },
      {
        "title": "How can NUMA locality cause a performance regression on a large host?",
        "theme": "systems-performance",
        "difficulty": "senior",
        "href": "questions/systems-performance/numa-locality-performance.html",
        "why": "NUMA locality is the topology regression large hosts quietly hide."
      },
      {
        "title": "How do you investigate a tail-latency incident when average latency is normal?",
        "theme": "systems-performance",
        "difficulty": "senior",
        "href": "questions/systems-performance/tail-latency-incident.html",
        "why": "The tail-latency incident with a normal average ties the resource chapters into one case."
      },
      {
        "title": "How do you select ftrace events for a latency investigation?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/ftrace-event-selection.html",
        "why": "Tools arrive late on purpose, because they assume you know what you are looking for."
      },
      {
        "title": "How do you use sampling profilers without distorting production performance?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/perf-sampling-and-overhead.html",
        "why": "Sampling profilers are used without distorting the production being measured."
      },
      {
        "title": "What safeguards are needed when using eBPF for production observability?",
        "theme": "systems-performance",
        "difficulty": "middle",
        "href": "questions/systems-performance/ebpf-observability-safety.html",
        "why": "eBPF carries safeguards because it is powerful in exactly the wrong places."
      },
      {
        "title": "How do you review whether a benchmark result is valid for a production decision?",
        "theme": "systems-performance",
        "difficulty": "senior",
        "href": "questions/systems-performance/benchmark-validity-review.html",
        "why": "Benchmark validity decides whether measurements ever become decisions."
      },
      {
        "title": "How would you govern a capacity model for a multi-tenant platform?",
        "theme": "systems-performance",
        "difficulty": "staff",
        "href": "questions/systems-performance/capacity-model-governance.html",
        "why": "The capacity model is governed, not worshipped, once it drives decisions."
      },
      {
        "title": "How do you use performance budgets in architecture governance?",
        "theme": "systems-performance",
        "difficulty": "staff",
        "href": "questions/systems-performance/performance-budget-architecture.html",
        "why": "The closing three open with performance budgets in architecture governance."
      },
      {
        "title": "How should a staff engineer lead a cross-layer performance incident?",
        "theme": "systems-performance",
        "difficulty": "staff",
        "href": "questions/systems-performance/performance-incident-command.html",
        "why": "Leading a cross-layer incident spends the whole method under pressure."
      },
      {
        "title": "How would you design a systems-performance observability program across teams?",
        "theme": "systems-performance",
        "difficulty": "staff",
        "href": "questions/systems-performance/performance-observability-program.html",
        "why": "The observability program is the staff-level synthesis of everything above."
      }
    ]
  },
  {
    "theme": "testing-strategy",
    "note": "Grow outward from the unit test: each ring only earns its cost once the ring inside it is honest.",
    "steps": [
      {
        "title": "Design a focused unit test",
        "theme": "testing-strategy",
        "difficulty": "junior",
        "href": "questions/testing-strategy/unit-test-design.html",
        "why": "Grow outward from the unit test: one focused test is the atom of the suite."
      },
      {
        "title": "Name test cases for diagnosis",
        "theme": "testing-strategy",
        "difficulty": "junior",
        "href": "questions/testing-strategy/test-case-naming.html",
        "why": "A test named for diagnosis fails helpfully instead of mysteriously."
      },
      {
        "title": "Define test-pyramid boundaries",
        "theme": "testing-strategy",
        "difficulty": "junior",
        "href": "questions/testing-strategy/test-pyramid-boundaries.html",
        "why": "Pyramid boundaries say where the unit layer stops and cost begins."
      },
      {
        "title": "Treat coverage as a testing signal",
        "theme": "testing-strategy",
        "difficulty": "junior",
        "href": "questions/testing-strategy/test-coverage-signal.html",
        "why": "Coverage as a signal calibrates the layer before it grows any further."
      },
      {
        "title": "Evaluate mutation testing trade-offs",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/mutation-testing-tradeoffs.html",
        "why": "Mutation testing prices what the coverage number actually proves."
      },
      {
        "title": "Design isolated test data",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/test-data-isolation.html",
        "why": "Isolated test data keeps the unit layer honest under repetition."
      },
      {
        "title": "Manage test data safely",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/test-data-management.html",
        "why": "Safe data management governs everything the tests consume."
      },
      {
        "title": "Choose integration test boundaries",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/integration-test-boundaries.html",
        "why": "Integration is the next ring, with boundaries chosen first."
      },
      {
        "title": "Define integration test data contracts",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/integration-test-data-contract.html",
        "why": "Data contracts make those integration boundaries actually testable."
      },
      {
        "title": "Use contract tests between services",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/contract-testing-boundaries.html",
        "why": "Contract tests verify a boundary from both of its sides."
      },
      {
        "title": "Adopt consumer-driven contracts",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/consumer-driven-contracts.html",
        "why": "Consumer-driven contracts only have something to verify once the boundaries exist."
      },
      {
        "title": "Control end-to-end test scope",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/end-to-end-test-scope.html",
        "why": "Scope control keeps the expensive ring from exploding."
      },
      {
        "title": "Design ephemeral test environments",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/ephemeral-test-environments.html",
        "why": "Ephemeral environments give every run its own disposable world."
      },
      {
        "title": "Set shared test environment policy",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/shared-test-environment-policy.html",
        "why": "The shared-environment policy governs the world that cannot be ephemeral."
      },
      {
        "title": "Define a flaky-test quarantine policy",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/flaky-test-quarantine-policy.html",
        "why": "The flaky quarantine keeps the suite's confidence measurable."
      },
      {
        "title": "Design release gates as risk controls",
        "theme": "testing-strategy",
        "difficulty": "staff",
        "href": "questions/testing-strategy/release-gate-design.html",
        "why": "Release opens with gates treated as risk controls rather than rituals."
      },
      {
        "title": "Place performance tests in CI",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/performance-tests-in-ci.html",
        "why": "Performance tests in CI prove only what they can honestly prove."
      },
      {
        "title": "Use shadow traffic safely",
        "theme": "testing-strategy",
        "difficulty": "staff",
        "href": "questions/testing-strategy/shadow-traffic-testing.html",
        "why": "Shadow traffic rehearses production without betting the production on it."
      },
      {
        "title": "Set production experiment guardrails",
        "theme": "testing-strategy",
        "difficulty": "staff",
        "href": "questions/testing-strategy/production-experiment-guardrails.html",
        "why": "Production experiments run inside guardrails or they do not run."
      },
      {
        "title": "Set security testing boundaries",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/security-test-boundaries.html",
        "why": "Security testing boundaries keep the tests from becoming the attack."
      },
      {
        "title": "Design accessibility testing strategy",
        "theme": "testing-strategy",
        "difficulty": "junior",
        "href": "questions/testing-strategy/accessibility-test-strategy.html",
        "why": "Accessibility strategy is a different risk with the same shape of decision."
      },
      {
        "title": "Make test failures observable",
        "theme": "testing-strategy",
        "difficulty": "senior",
        "href": "questions/testing-strategy/test-observability.html",
        "why": "Suites stay alive for years only when failures are observable."
      },
      {
        "title": "Model test execution cost",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/test-execution-cost-model.html",
        "why": "Execution cost is modelled rather than discovered at release time."
      },
      {
        "title": "Set test-suite execution policy",
        "theme": "testing-strategy",
        "difficulty": "middle",
        "href": "questions/testing-strategy/test-suite-execution-policy.html",
        "why": "Execution policy decides what runs when, and who waits for it."
      },
      {
        "title": "Assign test suite ownership",
        "theme": "testing-strategy",
        "difficulty": "staff",
        "href": "questions/testing-strategy/test-suite-ownership.html",
        "why": "Ownership assigns who answers when the policy fires red."
      },
      {
        "title": "Prioritize quality investment portfolio",
        "theme": "testing-strategy",
        "difficulty": "staff",
        "href": "questions/testing-strategy/quality-investment-portfolio.html",
        "why": "The quality-investment portfolio closes the Theme by pricing all of it."
      }
    ]
  },
  {
    "theme": "troubleshooting",
    "note": "Begin the way a page begins — alert context, then impact — because those two habits preserve every option the rest of the Theme depends on.",
    "steps": [
      {
        "title": "Read alert context before escalating",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/read-alert-context.html",
        "why": "Begin the way a page begins: what the alert measures, over what window."
      },
      {
        "title": "Establish impact before changing a failing service",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/establish-impact.html",
        "why": "Impact is established before changing anything, or every option is lost."
      },
      {
        "title": "Isolate a suspected change without guessing",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/isolate-change.html",
        "why": "Isolating a suspected change without guessing is the first diagnostic act."
      },
      {
        "title": "Decide whether a restart is a safe diagnostic action",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/safe-restart.html",
        "why": "Whether a restart is a safe diagnostic action is decided, never assumed."
      },
      {
        "title": "Contain a bad deployment while protecting evidence",
        "theme": "troubleshooting",
        "difficulty": "senior",
        "href": "questions/troubleshooting/handle-bad-deployment.html",
        "why": "Containing a bad deployment while protecting evidence keeps both options open."
      },
      {
        "title": "Trace a dependency failure across service boundaries",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/trace-dependency-failure.html",
        "why": "The dependency failure is traced across the boundaries it hides behind."
      },
      {
        "title": "Diagnose DNS failure from client to authoritative data",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/diagnose-dns.html",
        "why": "The specialist diagnoses open with DNS from client to authoritative data."
      },
      {
        "title": "Diagnose a TLS handshake failure safely",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-tls.html",
        "why": "The TLS handshake is diagnosed safely rather than disabled in frustration."
      },
      {
        "title": "Debug an authentication failure without weakening access control",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-auth-failure.html",
        "why": "Authentication is debugged without weakening the access control around it."
      },
      {
        "title": "Debug latency without averaging away the incident",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-latency.html",
        "why": "Latency is debugged without averaging away the incident."
      },
      {
        "title": "Investigate a production data mismatch safely",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/investigate-data-mismatch.html",
        "why": "The data mismatch is investigated safely across its stores."
      },
      {
        "title": "Triage a growing asynchronous work backlog",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-queue-backlog.html",
        "why": "The growing backlog is the asynchronous tier's fever chart."
      },
      {
        "title": "Debug an observability gap during an active incident",
        "theme": "troubleshooting",
        "difficulty": "senior",
        "href": "questions/troubleshooting/debug-observability-gap.html",
        "why": "The observability gap mid-incident is a failure in its own right."
      },
      {
        "title": "Stop a cascading failure while preserving useful traffic",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/reduce-cascading-failure.html",
        "why": "Stopping the cascade while preserving useful traffic is the specialists' synthesis."
      },
      {
        "title": "Triage an error-budget burn alert",
        "theme": "troubleshooting",
        "difficulty": "middle",
        "href": "questions/troubleshooting/debug-error-budget.html",
        "why": "The burn alert is triaged by validating its own arithmetic first."
      },
      {
        "title": "Verify recovery rather than trusting a green deployment",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/verify-recovery.html",
        "why": "Recovery is verified rather than trusted from a green dashboard."
      },
      {
        "title": "Design reliable multi-team incident handoffs",
        "theme": "troubleshooting",
        "difficulty": "staff",
        "href": "questions/troubleshooting/design-multi-team-handoff.html",
        "why": "The final tier opens with handoffs that survive shift changes."
      },
      {
        "title": "Lead a severe incident without uncontrolled changes",
        "theme": "troubleshooting",
        "difficulty": "senior",
        "href": "questions/troubleshooting/lead-sev-incident.html",
        "why": "Leading a severe incident means controlling the changes, not just the communications."
      },
      {
        "title": "Govern risky mitigations during a business-critical outage",
        "theme": "troubleshooting",
        "difficulty": "staff",
        "href": "questions/troubleshooting/govern-risky-mitigation.html",
        "why": "Risky mitigations are governed during the business-critical outage itself."
      },
      {
        "title": "Triage a regional outage with a safe traffic strategy",
        "theme": "troubleshooting",
        "difficulty": "senior",
        "href": "questions/troubleshooting/triage-regional-outage.html",
        "why": "The regional outage pairs diagnosis with a safe traffic strategy."
      },
      {
        "title": "Build an incident timeline from reliable evidence",
        "theme": "troubleshooting",
        "difficulty": "junior",
        "href": "questions/troubleshooting/collect-timeline.html",
        "why": "Timelines are built from reliable evidence or not at all."
      },
      {
        "title": "Design a production troubleshooting experiment",
        "theme": "troubleshooting",
        "difficulty": "senior",
        "href": "questions/troubleshooting/design-runbook-experiment.html",
        "why": "Designed troubleshooting experiments turn hypotheses into repeatable practice."
      },
      {
        "title": "Build a learning loop from production troubleshooting",
        "theme": "troubleshooting",
        "difficulty": "staff",
        "href": "questions/troubleshooting/build-learning-loop.html",
        "why": "The learning loop makes each incident improve the system itself."
      },
      {
        "title": "Reduce recurring incidents across a platform portfolio",
        "theme": "troubleshooting",
        "difficulty": "staff",
        "href": "questions/troubleshooting/portfolio-recurrence.html",
        "why": "Recurring incidents are reduced across the portfolio, not one service at a time."
      },
      {
        "title": "Define an organization-wide troubleshooting strategy",
        "theme": "troubleshooting",
        "difficulty": "staff",
        "href": "questions/troubleshooting/define-troubleshooting-strategy.html",
        "why": "The organization-wide strategy is the same method at fleet scale."
      }
    ]
  },
  {
    "theme": "version-control",
    "note": "Recovery reading starts with how commits, references, and the working tree relate, because every undo decision hangs on that model.",
    "steps": [
      {
        "title": "Explain Git's object model",
        "theme": "version-control",
        "difficulty": "junior",
        "href": "questions/version-control/git-object-model.html",
        "why": "How commits, references, and the working tree relate is the model every recovery decision hangs on."
      },
      {
        "title": "Choose between Git revert and reset for a bad change",
        "theme": "version-control",
        "difficulty": "middle",
        "href": "questions/version-control/revert-versus-reset.html",
        "why": "Reset and revert are practised on a disposable repository before they touch shared history."
      },
      {
        "title": "Repair a shared branch with a force push safely",
        "theme": "version-control",
        "difficulty": "senior",
        "href": "questions/version-control/safe-force-push.html",
        "why": "Repairing a shared branch prices the additive revert against the explicitly coordinated history rewrite."
      }
    ]
  },
  {
    "theme": "web-servers",
    "note": "Serve and log first, then proxy and deliberately break it, then run the edge like a platform.",
    "steps": [
      {
        "title": "Configure virtual-host routing safely",
        "theme": "web-servers",
        "difficulty": "junior",
        "href": "questions/web-servers/virtual-host-routing.html",
        "why": "Virtual hosts are the first routing decision a web server ever makes."
      },
      {
        "title": "Serve static content with correct cache control",
        "theme": "web-servers",
        "difficulty": "junior",
        "href": "questions/web-servers/static-content-cache-control.html",
        "why": "Static content with correct cache control is the first thing served at scale."
      },
      {
        "title": "Deploy a TLS certificate on a web server",
        "theme": "web-servers",
        "difficulty": "junior",
        "href": "questions/web-servers/tls-certificate-deployment.html",
        "why": "TLS deployment secures what the routing just exposed."
      },
      {
        "title": "Design useful web-server access logs",
        "theme": "web-servers",
        "difficulty": "junior",
        "href": "questions/web-servers/access-log-design.html",
        "why": "Request logging is designed before an incident needs it."
      },
      {
        "title": "Debug a 502 response from a reverse proxy",
        "theme": "web-servers",
        "difficulty": "middle",
        "href": "questions/web-servers/reverse-proxy-502-debugging.html",
        "why": "Proxying begins by deliberately breaking DNS and upstream connectivity and reading the resulting 502."
      },
      {
        "title": "Establish a TLS security baseline at the edge",
        "theme": "web-servers",
        "difficulty": "senior",
        "href": "questions/web-servers/tls-security-baseline.html",
        "why": "The edge TLS baseline hardens what the deployment step merely made work."
      },
      {
        "title": "Prevent a reverse-proxy cache from serving the wrong response",
        "theme": "web-servers",
        "difficulty": "middle",
        "href": "questions/web-servers/cache-proxy-correctness.html",
        "why": "Breaking cache keys teaches exactly what a proxy must never serve wrong."
      },
      {
        "title": "Set reverse-proxy timeouts from a request budget",
        "theme": "web-servers",
        "difficulty": "middle",
        "href": "questions/web-servers/proxy-timeout-budget.html",
        "why": "Timeouts are allocated from a request budget rather than set as independent knobs."
      },
      {
        "title": "Model web-server connection capacity",
        "theme": "web-servers",
        "difficulty": "senior",
        "href": "questions/web-servers/connection-capacity-model.html",
        "why": "Capacity drills model what the proxy tier can actually hold."
      },
      {
        "title": "Reload and drain a web server without dropping traffic",
        "theme": "web-servers",
        "difficulty": "middle",
        "href": "questions/web-servers/graceful-reload-and-drain.html",
        "why": "Deployment draining reloads the server without dropping live traffic."
      },
      {
        "title": "Define WAF and application-security boundaries",
        "theme": "web-servers",
        "difficulty": "senior",
        "href": "questions/web-servers/waf-and-application-boundaries.html",
        "why": "Security boundaries assign what the edge owes versus what the application owes."
      },
      {
        "title": "Design multi-tenant isolation at the web edge",
        "theme": "web-servers",
        "difficulty": "staff",
        "href": "questions/web-servers/multi-tenant-edge-isolation.html",
        "why": "Multi-tenant platform decisions close the Theme at edge scale."
      }
    ]
  }
];

window.labs = [
  {
    "title": "Redis как кэш Flask-приложения: от ручного кэша к TTL и eviction",
    "theme": "caching",
    "difficulty": "middle",
    "tags": [
      "caching",
      "redis",
      "docker",
      "prometheus",
      "monitoring",
      "memory",
      "healthchecks"
    ],
    "why": "A cache layer is named in four of the eight analyzed vacancies (Interlizing, efin, T1 pattern names Redis explicitly), yet candidates usually stop at installing it. This lab teaches hit-ratio thinking: cache-aside in the Flask app, TTL and invalidation choices, maxmemory eviction experiments with allkeys-lru versus volatile-star policies, and cache failure modes like stampede — the interview questions behind the install command.",
    "questionTitle": "Tune Redis maxmemory and eviction behaviour",
    "questionHref": "questions/caching/redis-maxmemory-tuning.html",
    "slug": "caching/redis-practical"
  },
  {
    "title": "ArgoCD: деплой Helm-чарта из Git вместо ручного helm upgrade",
    "theme": "ci-cd",
    "difficulty": "middle",
    "tags": [
      "ci-cd",
      "kubernetes",
      "argo-cd",
      "gitops",
      "deployment",
      "git",
      "delivery"
    ],
    "why": "ArgoCD is a hard requirement in efin A-tier vacancies and GitOps is a frequent senior interview topic. This lab teaches pull-based deployment and drift thinking rather than mere tool installation, closing the gap between running helm upgrade by hand and declarative delivery where Git is the single source of truth.",
    "questionTitle": "Choose a pull-based reconciler or a push-based deployment pipeline",
    "questionHref": "questions/ci-cd/gitops-pull-versus-push-delivery.html",
    "slug": "ci-cd/argocd-gitops-deploy"
  },
  {
    "title": "Explain idempotence in an Ansible playbook",
    "theme": "configuration-management",
    "difficulty": "middle",
    "tags": [
      "ansible",
      "automation",
      "configuration-management",
      "reliability"
    ],
    "why": "An idempotent automation run behaves predictably. If a task executes twice, it must not mutate the target or trigger duplicate changes. This ensures that scheduled runs and retries can occur safely without risk of configuration drift or service interruption.",
    "questionTitle": "Explain idempotence in an Ansible playbook",
    "questionHref": "questions/configuration-management/ansible-idempotence.html",
    "slug": "configuration-management/ansible-idempotence"
  },
  {
    "title": "Configure database readiness wait-for logic in Ansible",
    "theme": "configuration-management",
    "difficulty": "middle",
    "tags": [
      "ansible",
      "automation",
      "configuration-management",
      "reliability"
    ],
    "why": "Distributed services start up at different speeds. If the application server starts up before the database is ready, it will fail to connect and crash. Automating readiness checks via Ansible ensures playbooks execute smoothly without dependency race conditions.",
    "questionTitle": "Design a reusable Ansible role",
    "questionHref": "questions/configuration-management/ansible-role-design.html",
    "slug": "configuration-management/ansible-wait-logic"
  },
  {
    "title": "PostgreSQL: streaming-репликация, failover вручную и PITR",
    "theme": "databases",
    "difficulty": "middle",
    "tags": [
      "databases",
      "postgresql",
      "availability",
      "storage",
      "reliability",
      "ansible"
    ],
    "why": "Backups, replication and migrations are a direct Interlizing job requirement, and T1 asks for Patroni diagnostics: doing failover and recovery by hand builds the exact mental model Patroni automates, without installing it yet.",
    "questionTitle": "Design PostgreSQL high availability and failover",
    "questionHref": "questions/databases/high-availability-failover.html",
    "slug": "databases/postgresql-replication-pitr"
  },
  {
    "title": "Kubernetes break-fix: kubeadm-кластер и диагностика CNI/ingress",
    "theme": "kubernetes",
    "difficulty": "middle",
    "tags": [
      "kubernetes",
      "cni",
      "networking",
      "certificates",
      "troubleshooting",
      "fault-injection"
    ],
    "why": "Kubernetes appears in all eight target vacancies, and interviewers distinguish 'used k3s' from 'can repair a cluster'. This break-fix lab drills diagnosis through kubectl describe, logs, and events, plus control-plane understanding (etcd, apiserver, certificates), rather than deployment alone.",
    "questionTitle": "Triage a Kubernetes node that becomes NotReady",
    "questionHref": "questions/kubernetes/node-not-ready-triage.html",
    "slug": "kubernetes/kubeadm-cni-ingress-break-fix"
  },
  {
    "title": "Diagnose a systemd service that repeatedly fails",
    "theme": "linux",
    "difficulty": "middle",
    "tags": [
      "linux",
      "debugging",
      "troubleshooting",
      "lfcs"
    ],
    "why": "Linux system processes are managed through systemd unit configurations. If a service crashes or rate-limits, you must be able to navigate dependencies, file sockets, environment contexts, and boot journals to isolate unit flaws from runtime exceptions.",
    "questionTitle": "Diagnose a systemd service that repeatedly fails",
    "questionHref": "questions/linux/systemd-service-failure.html",
    "slug": "linux/systemd-service-failure"
  },
  {
    "title": "Мониторинг и логи на существующем стенде: Prometheus + Alertmanager + Loki + Grafana",
    "theme": "observability",
    "difficulty": "middle",
    "tags": [
      "observability",
      "monitoring",
      "logging",
      "prometheus",
      "ansible"
    ],
    "why": "Monitoring appears in eight of the eight analyzed vacancies and logging in six of eight; Loki covers the practical logging side more cheaply and simply than ELK, and correlating metrics with logs in a single dashboard is exactly what Ostrovok, T1, and efin interviews ask for. A candidate with production Zabbix+Grafana experience and pet-level Prometheus closes the main gap here: transferring scattered Zabbix experience onto the Prometheus stack and learning to tie an alert to its cause through logs.",
    "questionTitle": "Build an actionable production alert",
    "questionHref": "questions/observability/build-an-actionable-alert.html",
    "slug": "observability/prometheus-loki-telemetry"
  },
  {
    "title": "Live-Migrate a libvirt Domain and Measure the Real Downtime",
    "theme": "qemu-kvm",
    "difficulty": "senior",
    "tags": [
      "kvm",
      "libvirt",
      "live-migration",
      "migration",
      "networking",
      "performance",
      "troubleshooting"
    ],
    "why": "Pre-copy live migration looks like one command until a maintenance window depends on it. This lab builds the two-host preconditions yourself — shared storage, a writable domain, a budgeted migration — then forces the failure modes (uncontrolled bandwidth, a runaway dirty rate) and measures actual cutover downtime with ping, so you learn why convergence settings exist and what a trusted migration window really contains.",
    "questionTitle": "Run a live migration you can trust",
    "questionHref": "questions/qemu-kvm/run-a-live-migration-you-trust.html",
    "slug": "qemu-kvm/live-migrate-with-measured-downtime"
  },
  {
    "title": "RabbitMQ на практике: асинхронная обработка вокруг существующего приложения",
    "theme": "queue-messaging",
    "difficulty": "middle",
    "tags": [
      "rabbitmq",
      "message-queues",
      "event-driven",
      "observability",
      "reliability"
    ],
    "why": "Message brokers appear in four of the eight current vacancies, while the queue-messaging bank holds about thirty questions with no practical footing. RabbitMQ is the cheapest entry into the topic: one evening with a compose stand teaches the basic vocabulary (exchange, binding, ack, DLQ) and removes the fear of those interview questions. Interlizing vacancies require RabbitMQ clusters and efin asks Kafka concepts, and both interview branches start with understanding how a broker differs from a log.",
    "questionTitle": "Design RabbitMQ dead-letter handling",
    "questionHref": "questions/queue-messaging/design-rabbitmq-dead-lettering.html",
    "slug": "queue-messaging/rabbitmq-practical"
  },
  {
    "title": "SRE Chaos Sandbox: Chaos on a Leash",
    "theme": "sre",
    "difficulty": "senior",
    "tags": [
      "sre",
      "troubleshooting",
      "incident-response",
      "monitoring",
      "chaos-engineering"
    ],
    "why": "Real SRE operations involve responding to live alarms and diagnosing unknown state changes under pressure. Setting up a time-leashed chaos sandbox teaches how to manage on-call alerts, query journals, isolate latency, and build self-healing service definitions.",
    "questionTitle": "Exhaust disk space and file descriptors",
    "questionHref": "questions/chaos-engineering/exhaust-disk-and-file-descriptors.html",
    "slug": "sre/chaos-on-a-leash"
  }
];
