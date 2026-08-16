# Containers related materials

These resources support the Containers Theme. Use the Docker and OCI material
for product and format semantics; the personal material and the freely
available book are deliberately supplemental learning context, not evidence for
the answers in individual Questions.

## Vendor bias

This Theme teaches container concepts through Docker: nearly every primary
source is `docs.docker.com`, and the Questions phrase their examples in
Dockerfile and `docker` CLI syntax. That is a teaching choice, not a claim that
Docker is the canonical stack. The portable substrate underneath is the OCI
image, runtime, and distribution specifications, implemented equally by
containerd (the runtime beneath most Kubernetes distributions), podman (the
daemonless, rootless-first alternative), and other engines. Every
vendor-neutral Question's answer guide names the equivalent construct in at
least one other implementation, while genuinely Docker-specific behavior —
BuildKit cache semantics, rootless-mode details — keeps its Docker framing.

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)

## Suggested study order

Artifact before lifecycle, lifecycle before constraints and probes, hardening
before platform scope — each tier consumes the habits the previous one built.

1. [Distinguish a container image from a running container](../../questions/containers/container-image-and-runtime.html)
    — Image versus running container, read-only layers plus one writable layer,
    is the packaging fact everything else extends.
2. [Order a Dockerfile for safe cache reuse](../../questions/containers/build-cache-ordering.html)
    — A Dockerfile ordered for safe cache reuse makes builds predictable enough
    to keep honest.
3. [Build a small runtime image with multi-stage builds](../../questions/containers/multi-stage-runtime-image.html)
    — Multi-stage builds shrink the artifact the cache discipline just made
    predictable.
4. [Choose between CMD and ENTRYPOINT in a Docker image](../../questions/containers/cmd-and-entrypoint.html)
    — CMD versus ENTRYPOINT decides what the image actually runs, the contract
    inside the artifact.
5. [Distinguish image tags from digests](../../questions/containers/image-tag-and-digest.html)
    — Tags are names and digests are identity, so the artifact you run is the
    artifact you mean.
6. [Control Docker build context with .dockerignore](../../questions/containers/dockerfile-build-context.html)
    — Build-context control keeps the build's inputs as small as its promises.
7. [Explain container lifecycle states and restart policy](../../questions/containers/container-lifecycle-states.html)
    — Lifecycle follows artifact: states and restart policy define what the
    runtime does with the image.
8. [Investigate a container that exits immediately](../../questions/containers/inspect-container-failure.html)
    — The immediately exiting container is the first lifecycle evidence you
    learn to read.
9. [Make a container stop gracefully](../../questions/containers/pid-one-and-graceful-shutdown.html)
    — Graceful stops complete the lifecycle tier by making exit behaviour a
    contract.
10. [Triage a container service restart storm](../../questions/containers/container-incident-triage.html)
    — The restart storm is what bad lifecycle configuration produces, diagnosed
    with the tiers above.
11. [Apply CPU and memory constraints to a container](../../questions/containers/resource-constraints.html)
    — A limit is only sensible once the restart policy's verdict is understood,
    which is why constraints follow lifecycle.
12. [Design a useful container health check](../../questions/containers/container-healthcheck-design.html)
    — A probe is a decision about who declares health, made after the runtime
    can act on that verdict.
13. [Run a containerized service as a non-root user](../../questions/containers/non-root-container.html)
    — Hardening opens with the user: the service runs as non-root by default.
14. [Reduce Linux capabilities for a containerized service](../../questions/containers/container-capabilities-security.html)
    — Dropped capabilities bound what even a non-root container may ask the
    kernel for.
15. [Evaluate Docker rootless mode for a build worker](../../questions/containers/rootless-mode-boundaries.html)
    — Rootless mode removes the daemon's own privilege, and its limits read only
    with the tiers above.
16. [Define a container logging contract](../../questions/containers/container-logging-contract.html)
    — The logging contract keeps the hardened runtime observable.
17. [Choose a Docker volume or a bind mount](../../questions/containers/volume-versus-bind-mount.html)
    — Volumes versus bind mounts is the persistence decision the writable layer
    refused to be.
18. [Use a private dependency credential during an image build](../../questions/containers/build-secrets.html)
    — Private build credentials close the hardening tier with the secret that
    must never reach the image.
19. [Design a governed base-image program](../../questions/containers/platform-base-image-program.html)
    — The governed base-image program is the first full platform programme,
    consuming the artifact identity from the start.
20. [Maintain a base-image update policy](../../questions/containers/base-image-update-policy.html)
    — The update policy keeps the program's images current without surprising
    its consumers.
21. [Build an image supply-chain control plane](../../questions/containers/image-supply-chain-control-plane.html)
    — The supply-chain control plane makes provenance and promotion enforceable
    rather than aspirational.
22. [Release a multi-platform container image](../../questions/containers/multi-platform-image-release.html)
    — Multi-platform releases extend the identity discipline across
    architectures.
23. [Set a container-platform cost and capacity model](../../questions/containers/container-platform-cost-model.html)
    — The cost and capacity model prices the platform the program has become.
24. [Define tenant isolation boundaries for a container platform](../../questions/containers/tenant-isolation-boundaries.html)
    — Tenant boundaries decide who may share the platform the tiers above just
    built.
25. [Lead a container runtime migration](../../questions/containers/container-runtime-migration.html)
    — Runtime migration closes the Theme by changing the substrate underneath
    everything it taught.
