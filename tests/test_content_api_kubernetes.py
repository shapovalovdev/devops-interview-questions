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
    """Split Helm/Kustomize output without hiding duplicate resource Kinds."""
    documents: dict[str, list[str]] = {}
    for document in rendered.split("\n---\n"):
        match = re.search(r"^kind: (\w+)$", document, flags=re.MULTILINE)
        if match:
            documents.setdefault(match.group(1), []).append(document)
    return documents


def mapping_block(document: str, key: str) -> str:
    """Return one indented YAML mapping as stripped lines, independent of key order."""
    lines = document.splitlines()
    matches = [index for index, line in enumerate(lines) if line.strip() == f"{key}:"]
    if len(matches) != 1:
        raise AssertionError(f"expected one {key} mapping, found {len(matches)}")
    start = matches[0]
    indentation = len(lines[start]) - len(lines[start].lstrip())
    block = [lines[start].strip()]
    for line in lines[start + 1:]:
        if line.strip() and len(line) - len(line.lstrip()) <= indentation:
            break
        block.append(line.strip())
    return "\n".join(block)


class RenderParsingTest(unittest.TestCase):
    def test_document_splitter_preserves_duplicate_kinds(self) -> None:
        rendered = "kind: Service\nmetadata:\n  name: one\n---\nkind: Service\nmetadata:\n  name: two\n"

        documents = documents_by_kind(rendered)

        self.assertEqual(len(documents["Service"]), 2)
        self.assertIn("name: one", documents["Service"][0])
        self.assertIn("name: two", documents["Service"][1])


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
        expected = {"Deployment": 1, "Service": 1, "ServiceAccount": 1}
        self.assertEqual({kind: len(items) for kind, items in self.chart_documents.items()}, expected)
        self.assertEqual({kind: len(items) for kind, items in self.overlay_documents.items()}, expected)
        for source, documents in (("Helm", self.chart_documents), ("Kustomize", self.overlay_documents)):
            with self.subTest(source=source):
                service = documents["Service"][0]
                self.assertIn("type: ClusterIP", service)
                self.assertIn("port: 8000", service)

    def test_deployment_is_restricted_and_uses_the_image_baked_store_read_only(self) -> None:
        for source, documents, service_account in (
            ("Helm", self.chart_documents, "content-api-test"),
            ("Kustomize", self.overlay_documents, "content-api-k3d"),
        ):
            with self.subTest(source=source):
                deployment = documents["Deployment"][0]
                for expected in (
                    f"serviceAccountName: {service_account}",
                    "automountServiceAccountToken: false",
                    "runAsNonRoot: true",
                    "runAsUser: 10001",
                    "runAsGroup: 10001",
                    "type: RuntimeDefault",
                    "allowPrivilegeEscalation: false",
                    "readOnlyRootFilesystem: true",
                    "cpu: 100m",
                    "memory: 128Mi",
                    "cpu: 500m",
                    "memory: 256Mi",
                ):
                    self.assertIn(expected, deployment)
                self.assertRegex(deployment, r"capabilities:\n\s+drop:\n\s+- ALL")
                for forbidden in (
                    "initContainers:",
                    "seed-content-store",
                    "fsGroup:",
                    "volumeMounts:",
                    "mountPath: /srv/data",
                    "volumes:",
                    "emptyDir:",
                    "CONTENT_API_WRITE_KEY",
                ):
                    self.assertNotIn(forbidden, deployment)

    def test_probes_cover_cold_start_readiness_and_runtime_health(self) -> None:
        for source, documents in (("Helm", self.chart_documents), ("Kustomize", self.overlay_documents)):
            with self.subTest(source=source):
                deployment = documents["Deployment"][0]
                expected_probes = {
                    "startupProbe": ("periodSeconds: 5", "timeoutSeconds: 2", "failureThreshold: 24"),
                    "readinessProbe": ("periodSeconds: 5", "timeoutSeconds: 2", "failureThreshold: 3"),
                    "livenessProbe": ("periodSeconds: 10", "timeoutSeconds: 2", "failureThreshold: 3"),
                }
                for probe, settings in expected_probes.items():
                    block = mapping_block(deployment, probe)
                    self.assertIn("httpGet:", block)
                    self.assertIn("path: /api/v1/health", block)
                    self.assertIn("port: http", block)
                    for setting in settings:
                        self.assertIn(setting, block)
                self.assertEqual(deployment.count("path: /api/v1/health"), 3)

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
        subprocess.run(["bash", "-n", str(SMOKE_SCRIPT)], check=True)
        self.assertIn('k3d image import "$image:$source_commit" -c "$cluster"', script)
        self.assertNotIn("--mode direct", script)
        self.assertIn("--provenance=false", script)
        self.assertIn("image=docker.io/library/devops-questions-content-api", script)
        self.assertIn('ctr -n k8s.io images list -q', script)
        self.assertIn('grep -Eq "(^|/)${image}:${source_commit}$"', script)
        self.assertIn("git status --porcelain=v1 --untracked-files=all", script)
        self.assertIn('[[ "$source_commit" == "$head_commit" ]]', script)
        self.assertIn('namespace="content-api-216-${source_commit:0:8}-$(date +%s)-$$"', script)
        self.assertIn('if [[ "$namespace_created" == true ]]', script)
        self.assertIn("namespace_uid", script)
        self.assertIn('&& "$current_uid" == "$namespace_uid" ]]', script)
        self.assertIn("meta.get(\"source_commit\") != expected_commit", script)
        self.assertIn('headers.get("x-content-snapshot") != content_digest', script)
        self.assertIn("assert_no_restarts", script)
        self.assertIn("restartCount", script)
        self.assertNotIn("namespace=content-api-206", script)
        self.assertNotIn("--head", script)


if __name__ == "__main__":
    unittest.main()
