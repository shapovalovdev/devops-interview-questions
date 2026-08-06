---
title: Explain why multi-stage builds reduce runtime risk
theme: advanced-containers
difficulty: junior
type: theory
tags: [containers, docker, dockerfile, multi-stage-builds, security]
sources:
  - url: https://docs.docker.com/build/building/multi-stage/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain why multi-stage builds reduce runtime risk

How do multi-stage Dockerfiles separate build dependencies from the deployed image?

## Answer guide

- Each `FROM` begins a stage. A later stage can selectively `COPY --from` a named earlier stage, so compilers and source trees do not have to be present in the final image.
- Keep the runtime stage explicit: copy only required artifacts, run under a non-root user where practical, and set the intended entrypoint.
- This reduces image size and attack surface but does not prove the binary is secure. Build dependencies and generated artifacts still need provenance, scanning, and testing.
- Validate the final stage, not merely the build stage. Missing shared libraries, CA certificates, timezone data, or file ownership are common production failures.

## References

- [Docker Docs: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- Further reading (blog): [Docker: Intro guide to Dockerfile best practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
