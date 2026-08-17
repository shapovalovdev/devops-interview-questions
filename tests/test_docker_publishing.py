"""Structural gates for the Docker publishing path (issue #163).

The image must keep mirroring the own-build pipeline: the builder stage runs
`scripts/build_site.py`, the final stage serves the output unprivileged on
8080, and CI builds the image on every pull request so the Dockerfile cannot
rot silently.  These checks pin the files that docker itself does not
validate (compose of stages, ignored context entries, workflow wiring) and
run as part of `tests/run_all_tests.py`.
"""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCKERFILE = ROOT / "Dockerfile"
DOCKERIGNORE = ROOT / ".dockerignore"
NGINX_CONF = ROOT / "docker" / "nginx.conf"
WORKFLOW = ROOT / ".github" / "workflows" / "docker-build.yml"
PUBLISHING_DOC = ROOT / "docs" / "publishing.md"
README = ROOT / "README.md"


class DockerPublishingTest(unittest.TestCase):
    def test_dockerfile_is_multistage_and_runs_the_own_build(self) -> None:
        text = DOCKERFILE.read_text(encoding="utf-8")
        self.assertIn("python:3.13-alpine", text)
        self.assertIn("scripts/build_site.py", text)
        self.assertIn("nginx:alpine", text)
        self.assertIn("COPY --from=builder /site/build/site", text)
        self.assertIn("EXPOSE 8080", text)
        self.assertIn("USER nginx", text)
        self.assertIn("HEALTHCHECK", text)

    def test_dockerignore_keeps_the_context_lean(self) -> None:
        entries = {
            line.strip()
            for line in DOCKERIGNORE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
        for excluded in (".git", ".claude", "build", "dist", "skills", "__pycache__"):
            self.assertIn(excluded, entries)

    def test_nginx_config_serves_html_uncached_and_assets_cached(self) -> None:
        text = NGINX_CONF.read_text(encoding="utf-8")
        self.assertIn("listen 8080", text)
        self.assertIn("location /assets/", text)
        self.assertIn("max-age=604800", text)
        # Every HTML route must revalidate on each visit.
        html_block = text.split("~* \\.html$")[1]
        self.assertIn("no-cache", html_block)

    def test_ci_builds_and_smoke_tests_the_image(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("docker build", text)
        self.assertIn("docker run -d", text)
        self.assertIn("pull_request", text)
        self.assertIn("branches: [main]", text)
        self.assertIn("argo-cd-application-sync.html", text)

    def test_publishing_docs_cover_all_three_targets(self) -> None:
        text = PUBLISHING_DOC.read_text(encoding="utf-8")
        for phrase in (
            "GitHub Pages",
            "docker build -t devops-questions .",
            "docker run -p 8080:8080",
            "scripts/build_site.py",
        ):
            self.assertIn(phrase, text)
        readme = README.read_text(encoding="utf-8")
        self.assertIn("## Self-hosting", readme)
        self.assertIn("docs/publishing.md", readme)


if __name__ == "__main__":
    unittest.main()
