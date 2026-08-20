"""Render gates for the Helm-owned Content API Kubernetes contract."""

from __future__ import annotations

import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / "deploy" / "content-api"
OVERLAY = ROOT / "kustomize" / "k3d"
SMOKE_SCRIPT = ROOT / "scripts" / "smoke_k3d_content_api.sh"


def render_helm() -> str:
    return subprocess.run(
        [
            "helm", "template", "content-api-test", str(CHART),
            "--set", "image.repository=registry.example/content-api",
            "--set", "image.digest=sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ],
        check=True,
        text=True,
        capture_output=True,
    ).stdout


def documents_by_kind(rendered: str) -> dict[str, list[str]]:
    """Split Helm/Kustomize output without adding a YAML dependency to stdlib CI."""
    documents: dict[str, list[str]] = {}
    for document in rendered.split("\n---\n"):
        match = re.search(r"^kind: (\w+)$", document, flags=re.MULTILINE)
        if match:
            documents.setdefault(match.group(1), []).append(document)
    return documents


class ContentApiKubernetesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if shutil.which("helm") is None or shutil.which("kustomize") is None:
            raise unittest.SkipTest("helm and kustomize are required for Kubernetes render tests")
        cls.chart_documents = documents_by_kind(render_helm())
        overlay = subprocess.run(
            ["kustomize", "build", "--enable-helm", "--load-restrictor", "LoadRestrictionsNone", str(OVERLAY)],
            check=True,
            text=True,
            capture_output=True,
        ).stdout
        cls.overlay_documents = documents_by_kind(overlay)

    def test_chart_owns_the_only_workload_and_service(self) -> None:
        expected = {"Deployment", "Service", "ServiceAccount"}
        self.assertEqual(set(self.chart_documents), expected)
        self.assertEqual(set(self.overlay_documents), expected)
        for kind in expected:
            self.assertEqual(len(self.chart_documents[kind]), 1, f"Chart produced duplicate {kind}")
            self.assertEqual(len(self.overlay_documents[kind]), 1, f"Overlay produced duplicate {kind}")
        service = self.chart_documents["Service"][0]
        self.assertIn("type: ClusterIP", service)
        self.assertIn("port: 8000", service)

    def test_deployment_is_restricted_and_runs_pure_read_only_from_baked_image(self) -> None:
        deployment = self.chart_documents["Deployment"][0]
        for expected in (
            "serviceAccountName: content-api-test",
            "automountServiceAccountToken: false",
            "runAsNonRoot: true",
            "runAsUser: 10001",
            "runAsGroup: 10001",
            "fsGroup: 10001",
            "type: RuntimeDefault",
            "allowPrivilegeEscalation: false",
            "readOnlyRootFilesystem: true",
            "drop:\n                - ALL",
            "startupProbe:",
            "readinessProbe:",
            "livenessProbe:",
            "path: /api/v1/health",
            "initialDelaySeconds: 1",
            "periodSeconds: 2",
            "failureThreshold: 30",
            "cpu: 100m",
            "memory: 128Mi",
            "cpu: 500m",
            "memory: 256Mi",
        ):
            self.assertIn(expected, deployment)
        
        # Pure read-only from baked image: no init containers, no writable mounts, no emptyDir volumes
        self.assertNotIn("initContainers:", deployment)
        self.assertNotIn("volumeMounts:", deployment)
        self.assertNotIn("emptyDir:", deployment)
        self.assertNotIn("command: [\"cp\", \"/srv/data/content.db\"", deployment)

    def test_k3d_overlay_has_single_source_image_identity_and_no_images_transformer(self) -> None:
        kustomization = (OVERLAY / "kustomization.yaml").read_text(encoding="utf-8")
        self.assertNotIn("images:", kustomization)
        values = (OVERLAY / "values.yaml").read_text(encoding="utf-8")
        self.assertIn("repository: devops-questions-content-api", values)
        self.assertIn("tag: local", values)
        self.assertIn("local: true", values)

    def test_chart_requires_a_valid_digest_outside_local_overlay(self) -> None:
        result = subprocess.run(
            ["helm", "template", "content-api-test", str(CHART), "--set", "image.repository=registry.example/content-api", "--set", "image.tag=immutable-looking-tag"],
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("image.digest is required", result.stderr)
        malformed = subprocess.run(
            ["helm", "template", "content-api-test", str(CHART), "--set", "image.repository=registry.example/content-api", "--set", "image.digest=sha256:not-a-digest"],
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(malformed.returncode, 0)
        self.assertIn("must be a sha256 digest", malformed.stderr)

    def test_chart_allows_a_tag_only_for_the_local_overlay(self) -> None:
        output = subprocess.run(
            ["helm", "template", "content-api-test", str(CHART), "--set", "image.repository=content-api", "--set", "image.tag=commit-tag", "--set", "image.local=true"],
            check=True,
            text=True,
            capture_output=True,
        ).stdout
        self.assertIn('image: "content-api:commit-tag"', output)

    def test_k3d_smoke_verifies_the_default_import_reaches_containerd(self) -> None:
        script = SMOKE_SCRIPT.read_text(encoding="utf-8")
        self.assertIn('k3d image import "$image:$source_commit" -c "$cluster"', script)
        self.assertNotIn("--mode direct", script)
        self.assertNotIn("perl -0pi", script)
        self.assertIn("--provenance=false", script)
        self.assertIn("image=docker.io/library/devops-questions-content-api", script)
        self.assertIn('ctr -n k8s.io images list -q', script)
        self.assertIn('grep -Eq "(^|/)${image}:${source_commit}$"', script)
        self.assertIn("--dump-header - --output /dev/null", script)
        self.assertNotIn("--head", script)
        self.assertIn("for attempt in $(seq 1 30); do", script)
        self.assertIn("meta.source_commit", script)
        self.assertIn("X-Content-Snapshot", script)
        self.assertIn("restarts", script)


if __name__ == "__main__":
    unittest.main()
