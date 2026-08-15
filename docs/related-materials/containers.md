# Containers related materials

These resources support the Containers Theme. Use the Docker and OCI material
for product and format semantics; the personal material and the freely
available book are deliberately supplemental learning context, not evidence for
the answers in individual Questions.

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)

## Suggested study order

Begin with what an image is versus what a running container is — read-only
layers plus one writable layer — then write Dockerfiles ordered for safe cache
reuse and shrunk with multi-stage builds. Take CMD versus ENTRYPOINT, tags
versus digests, and build-context control next, so the artifact you run is the
artifact you mean. Lifecycle follows artifact: states and restart policy, the
container that exits immediately, graceful stops, and the restart storm that
bad lifecycle configuration produces. Resource constraints and health-check
design come after lifecycle deliberately — a limit or probe is only sensible
once you know what the restart policy does with its verdict. Then harden the
runtime: non-root users, dropped capabilities, rootless mode, the logging
contract, volumes versus bind mounts, and private build credentials. Close at
platform scope with the governed base-image program and update policy, the
supply-chain control plane, multi-platform releases, cost and capacity, tenant
isolation boundaries, and the runtime migration — each consuming the artifact
and lifecycle habits from the first half.
