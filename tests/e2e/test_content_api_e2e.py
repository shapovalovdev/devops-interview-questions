"""The Content API as a deployed service, over real HTTP.

Everything else in the suite imports the app and talks to it through
`TestClient`, which is fast and proves the application logic. It cannot prove
that the image builds, that the store ships inside it, that the service starts
as a non-root user, that uvicorn serves what FastAPI describes, or that a
container handed no Write credential refuses writes rather than accepting them.

Those are the failures that only appear once the thing is packaged, so this
suite builds the image, runs it, waits for its health check, and speaks to it
with `urllib` — no `TestClient`, no imports from `api/`. It reads the service
the way a client on another machine would.

Run it directly (`python tests/e2e/test_content_api_e2e.py`) or through CI. It
skips, loudly, when Docker is not available, because a skipped end-to-end suite
is honest and a fabricated one is not.
"""

from __future__ import annotations

import json
import secrets
import shutil
import subprocess
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMAGE = "devops-questions-api:e2e"
CONTAINER = "devops-questions-api-e2e"
PORT = 8123
BASE = f"http://127.0.0.1:{PORT}/api/v1"
WRITE_KEY = secrets.token_urlsafe(24)
STARTUP_TIMEOUT = 90


def docker_available() -> bool:
    if shutil.which("docker") is None:
        return False
    return subprocess.run(("docker", "info"), capture_output=True).returncode == 0


def run(*arguments: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(arguments, capture_output=True, text=True, check=check)


class Headers(dict):
    """Response headers, looked up without caring about case.

    HTTP header names are case-insensitive and uvicorn sends them lowercase, so
    a plain dict would make `headers["ETag"]` depend on how the server happened
    to spell it. Title-casing is not enough either: `"etag".title()` is `"Etag"`.
    """

    def __init__(self, message):
        super().__init__({name.lower(): value for name, value in message.items()})

    def __getitem__(self, name):
        return super().__getitem__(name.lower())

    def __contains__(self, name):
        return super().__contains__(str(name).lower())

    def get(self, name, default=None):
        return super().get(str(name).lower(), default)


def _headers(message) -> Headers:
    return Headers(message)


def request(
    method: str,
    path: str,
    body: dict | None = None,
    headers: dict[str, str] | None = None,
) -> tuple[int, dict, dict[str, str]]:
    """One real HTTP request. Returns `(status, parsed body, headers)`.

    A `4xx` or `5xx` is an answer here, not an exception: this suite is mostly
    about what the service refuses.
    """
    data = json.dumps(body).encode("utf-8") if body is not None else None
    outgoing = {"Content-Type": "application/json"} if data else {}
    outgoing.update(headers or {})
    attempt = urllib.request.Request(f"{BASE}{path}", data=data, headers=outgoing, method=method)
    try:
        with urllib.request.urlopen(attempt) as response:
            raw = response.read()
            return response.status, (json.loads(raw) if raw else {}), _headers(response.headers)
    except urllib.error.HTTPError as error:
        raw = error.read()
        return error.code, (json.loads(raw) if raw else {}), _headers(error.headers)


def question_body(slug: str) -> dict:
    return {
        "theme": "kubernetes",
        "slug": slug,
        "title": "A Question written over HTTP",
        "difficulty": "middle",
        "type": "theory",
        "tags": ["kubernetes"],
        "sources": [
            {
                "url": "https://kubernetes.io/docs/",
                "source_type": "official-docs",
                "verified_on": "2026-08-18",
            }
        ],
        "prompt": "What does this endpoint prove?",
        "answer_guide": ["That the packaged service accepts a write over real HTTP."],
        "body_markdown": (
            "\n# A Question written over HTTP\n\nWhat does this endpoint prove?\n\n"
            "## Answer guide\n\n- That the packaged service accepts a write over real HTTP.\n"
        ),
    }


@unittest.skipUnless(docker_available(), "Docker is not available; the end-to-end suite cannot run")
class ContentApiEndToEnd(unittest.TestCase):
    """One container, built and started once, exercised as a whole service."""

    @classmethod
    def setUpClass(cls):
        run("docker", "rm", "-f", CONTAINER, check=False)
        source_commit = run("git", "-C", str(ROOT), "rev-parse", "HEAD").stdout.strip()
        build_timestamp = run("git", "-C", str(ROOT), "show", "-s", "--format=%cI", "HEAD").stdout.strip()
        build = run(
            "docker", "build", "-f", str(ROOT / "Dockerfile.api"), "-t", IMAGE,
            "--build-arg", f"SOURCE_COMMIT={source_commit}",
            "--build-arg", f"BUILD_TIMESTAMP={build_timestamp}",
            str(ROOT), check=False
        )
        assert build.returncode == 0, f"the API image did not build:\n{build.stderr[-2000:]}"
        started = run(
            "docker", "run", "-d", "--name", CONTAINER,
            "-p", f"{PORT}:8000",
            "-e", f"CONTENT_API_WRITE_KEY={WRITE_KEY}",
            IMAGE,
            check=False,
        )
        assert started.returncode == 0, f"the container did not start:\n{started.stderr[-2000:]}"
        cls._await_health()

    @classmethod
    def tearDownClass(cls):
        # Always, even when a test failed: a wedged container in CI is worse
        # than a red test, and worse than no test at all on a developer's laptop.
        run("docker", "rm", "-f", CONTAINER, check=False)

    @classmethod
    def _await_health(cls):
        deadline = time.monotonic() + STARTUP_TIMEOUT
        while time.monotonic() < deadline:
            try:
                status, body, _ = request("GET", "/health")
                if status == 200 and body.get("status") == "ok":
                    return
            except (urllib.error.URLError, ConnectionError, OSError):
                pass
            time.sleep(1)
        logs = run("docker", "logs", CONTAINER, check=False)
        raise AssertionError(
            f"the service was not healthy within {STARTUP_TIMEOUT}s\n{logs.stdout[-2000:]}\n{logs.stderr[-2000:]}"
        )

    def write(self, method: str, path: str, body: dict | None = None, **headers: str):
        return request(method, path, body, {"X-API-Key": WRITE_KEY, **headers})

    # -- the service itself ------------------------------------------------

    def test_it_reports_healthy_and_names_its_contract(self):
        status, body, _ = request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "ok")
        self.assertEqual(body["contract_version"], "v1")

    def test_it_announces_its_immutable_snapshot_on_success_and_error(self):
        status, body, headers = request("GET", "/meta")
        self.assertEqual(status, 200)
        self.assertEqual(body["api_version"], "v1")
        self.assertEqual(body["license"]["spdx_id"], "CC-BY-4.0")
        self.assertEqual(body["attribution"], "https://github.com/shapovalovdev/devops-interview-questions")
        self.assertEqual(len(body["source_commit"]), 40)
        self.assertEqual(len(body["content_digest"]), 64)
        self.assertEqual(headers["X-Content-Snapshot"], body["content_digest"])

        missing_status, _, missing_headers = request("GET", "/questions/no-such-theme/no-such-question")
        self.assertEqual(missing_status, 404)
        self.assertEqual(missing_headers["X-Content-Snapshot"], body["content_digest"])

    def test_it_runs_as_a_non_root_user(self):
        identity = run("docker", "exec", CONTAINER, "id", "-u")
        self.assertNotEqual(identity.stdout.strip(), "0", "the service must not run as root")

    def test_it_serves_the_contract_it_was_built_from(self):
        with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/openapi.json") as response:
            schema = json.loads(response.read())
        self.assertEqual(schema["info"]["title"], "Content API")
        self.assertIn("/api/v1/questions", schema["paths"])

    def test_the_store_shipped_inside_the_image(self):
        """No volume, no seeding step: the corpus is in the image."""
        status, body, _ = request("GET", "/questions?limit=1")
        self.assertEqual(status, 200)
        self.assertGreater(body["total"], 1000, "the image should carry the whole corpus")

    # -- reading, the way a learner would ---------------------------------

    def test_a_learner_can_filter_a_theme_by_difficulty_and_tag(self):
        status, body, _ = request("GET", "/questions?theme=kubernetes&difficulty=senior&limit=5")
        self.assertEqual(status, 200)
        self.assertGreater(body["total"], 0)
        for item in body["items"]:
            self.assertEqual(item["theme"], "kubernetes")
            self.assertEqual(item["difficulty"], "senior")

    def test_a_lab_leads_to_the_question_it_prepares_you_for(self):
        status, labs, _ = request("GET", "/labs?limit=1")
        self.assertEqual(status, 200)
        self.assertTrue(labs["items"], "the image should carry Labs as well as Questions")
        reference = labs["items"][0]["question_ref"]

        status, question, headers = request("GET", f"/questions/{reference}")
        self.assertEqual(status, 200, f"a Lab pointed at {reference}, which the API could not serve")
        self.assertEqual(question["id"], reference)
        self.assertIn("Link", headers, "the Question should link back to the Labs that prepare it")

    def test_a_conditional_re_read_is_answered_304(self):
        status, _, headers = request("GET", "/questions?limit=1")
        identifier = request("GET", "/questions?limit=1")[1]["items"][0]["id"]
        status, _, headers = request("GET", f"/questions/{identifier}")
        self.assertEqual(status, 200)
        etag = headers["ETag"]

        status, _, _ = request("GET", f"/questions/{identifier}", headers={"If-None-Match": etag})
        self.assertEqual(status, 304)

    def test_search_spans_questions_and_labs(self):
        status, body, _ = request("GET", "/search?q=kubernetes&limit=5")
        self.assertEqual(status, 200)
        self.assertGreater(body["total"], 0)
        self.assertTrue({"kind", "score", "item"} <= set(body["items"][0]))

    def test_an_unknown_question_is_a_problem_document(self):
        status, body, headers = request("GET", "/questions/kubernetes/nothing-here")
        self.assertEqual(status, 404)
        self.assertTrue(headers["Content-Type"].startswith("application/problem+json"))
        self.assertEqual(body["status"], 404)
        self.assertNotIn("Traceback", json.dumps(body))

    # -- writing, with everything that guards it ---------------------------

    def test_a_write_journey_over_real_http(self):
        body = question_body("e2e-write-journey")
        path = f"/questions/{body['theme']}/{body['slug']}"

        status, created, _ = self.write("POST", "/questions", body)
        self.assertEqual(status, 201, created)

        status, fetched, headers = request("GET", path)
        self.assertEqual(status, 200)
        self.assertEqual(fetched["title"], body["title"])
        etag = headers["ETag"]

        status, patched, _ = self.write(
            "PATCH", path, {"difficulty": "senior"}, **{"If-Match": etag}
        )
        self.assertEqual(status, 200, patched)
        self.assertEqual(request("GET", path)[1]["difficulty"], "senior")

        current = request("GET", path)[2]["ETag"]
        status, _, _ = self.write("DELETE", path, None, **{"If-Match": current})
        self.assertEqual(status, 204)
        self.assertEqual(request("GET", path)[0], 404)

    def test_a_write_without_the_credential_is_refused(self):
        status, _, _ = request("POST", "/questions", question_body("e2e-no-credential"))
        self.assertEqual(status, 401)

    def test_a_write_with_the_wrong_credential_is_refused(self):
        status, _, _ = request(
            "POST", "/questions", question_body("e2e-wrong-credential"), {"X-API-Key": "not-the-key"}
        )
        self.assertEqual(status, 403)

    def test_a_mutation_without_a_validator_is_refused(self):
        identifier = request("GET", "/questions?limit=1")[1]["items"][0]["id"]
        status, _, _ = self.write("PATCH", f"/questions/{identifier}", {"difficulty": "senior"})
        self.assertEqual(status, 428)

    def test_a_mutation_with_a_stale_validator_is_refused(self):
        identifier = request("GET", "/questions?limit=1")[1]["items"][0]["id"]
        status, _, _ = self.write(
            "PATCH", f"/questions/{identifier}", {"difficulty": "senior"}, **{"If-Match": '"stale"'}
        )
        self.assertEqual(status, 412)

    def test_a_write_breaking_a_corpus_rule_is_refused(self):
        body = question_body("e2e-bad-theme")
        body["theme"] = "not-a-theme"
        status, problem, _ = self.write("POST", "/questions", body)
        self.assertEqual(status, 422)
        self.assertIn("theme", json.dumps(problem))

    def test_the_credential_never_appears_in_a_response(self):
        for status, body, headers in (
            request("POST", "/questions", question_body("e2e-leak-check")),
            request(
                "POST", "/questions", question_body("e2e-leak-check"), {"X-API-Key": "not-the-key"}
            ),
        ):
            rendered = json.dumps(body) + json.dumps(dict(headers))
            self.assertNotIn(WRITE_KEY, rendered)


class ReadOnlyContainer(unittest.TestCase):
    """A container handed no credential must refuse writes, not accept them."""

    CONTAINER = f"{CONTAINER}-readonly"
    PORT = PORT + 1

    @classmethod
    def setUpClass(cls):
        if not docker_available():
            raise unittest.SkipTest("Docker is not available; the end-to-end suite cannot run")
        run("docker", "rm", "-f", cls.CONTAINER, check=False)
        source_commit = run("git", "-C", str(ROOT), "rev-parse", "HEAD").stdout.strip()
        build_timestamp = run("git", "-C", str(ROOT), "show", "-s", "--format=%cI", "HEAD").stdout.strip()
        build = run(
            "docker", "build", "-f", str(ROOT / "Dockerfile.api"), "-t", IMAGE,
            "--build-arg", f"SOURCE_COMMIT={source_commit}",
            "--build-arg", f"BUILD_TIMESTAMP={build_timestamp}",
            str(ROOT), check=False
        )
        assert build.returncode == 0, f"the API image did not build:\n{build.stderr[-2000:]}"
        run("docker", "run", "-d", "--name", cls.CONTAINER, "-p", f"{cls.PORT}:8000", IMAGE)
        deadline = time.monotonic() + STARTUP_TIMEOUT
        while time.monotonic() < deadline:
            try:
                with urllib.request.urlopen(
                    f"http://127.0.0.1:{cls.PORT}/api/v1/health"
                ) as response:
                    if response.status == 200:
                        return
            except (urllib.error.URLError, OSError):
                time.sleep(1)
        raise AssertionError("the read-only container never became healthy")

    @classmethod
    def tearDownClass(cls):
        run("docker", "rm", "-f", cls.CONTAINER, check=False)

    def test_it_serves_reads(self):
        with urllib.request.urlopen(f"http://127.0.0.1:{self.PORT}/api/v1/questions?limit=1") as r:
            self.assertEqual(r.status, 200)

    def test_it_refuses_every_write_with_503(self):
        attempt = urllib.request.Request(
            f"http://127.0.0.1:{self.PORT}/api/v1/questions",
            data=json.dumps(question_body("e2e-read-only")).encode("utf-8"),
            headers={"Content-Type": "application/json", "X-API-Key": "anything"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(attempt) as response:
                self.fail(f"the read-only container accepted a write: {response.status}")
        except urllib.error.HTTPError as error:
            self.assertEqual(error.code, 503)
            self.assertIn("CONTENT_API_WRITE_KEY", error.read().decode("utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
