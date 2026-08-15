#!/usr/bin/env python3
"""Vendor-honesty gates for the three single-vendor Themes (issue #111).

`configuration-management`, `containers`, and `service-mesh` each teach
category-level concepts through one product's documentation. Issue #111 made
that scope honest instead of hiding it:

* every Theme's related-materials page states its vendor bias plainly, so a
  reader knows what they are getting before they start;
* every vendor-neutral Question's answer guide maps its concept onto at
  least one other implementation, naming the equivalent construct rather
  than gesturing at "other tools";
* where a vendor-neutral authority genuinely exists (an OCI specification,
  the Gateway API, SPIFFE, NIST guidance, or a second implementation's
  documentation), it is also a declared primary source, verified before it
  was written in.

These checks keep those properties from regressing: remove a bias statement
or a portability mapping and the Theme stops being honest without anyone
noticing.
"""

from __future__ import annotations

from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from validate_questions import primary_source_urls  # noqa: E402

THEMES = ("configuration-management", "containers", "service-mesh")

# Answer-guide markers that name a concrete other implementation or the
# vendor-neutral authority for the concept. A Question counts as mapped when
# its answer guide contains at least one of its Theme's markers.
PORTABILITY_MARKERS = {
    "containers": (
        "OCI",
        "containerd",
        "podman",
        "Podman",
        "Buildah",
        "Kubernetes",
        "crun",
        "runc",
        "gVisor",
        "CRI",
    ),
    "configuration-management": (
        "Terraform",
        "terraform",
        "Puppet",
        "PuppetDB",
        "Puppetfile",
        "Salt",
        "Hiera",
        "Ohai",
        "Chef",
        "SOPS",
        "git-crypt",
        "NIST",
        "declarative-convergence",
    ),
    "service-mesh": (
        "Linkerd",
        "linkerd",
        "Gateway API",
        "Cilium",
        "SPIFFE",
        "Envoy Gateway",
        "eBPF",
        "Hubble",
    ),
}

# Hosts whose documentation is a vendor-neutral or second-implementation
# authority for these Themes rather than the Theme's dominant vendor.
NEUTRAL_SOURCE_HOSTS = {
    "github.com",  # opencontainers/* and containers/* specifications
    "docs.podman.io",
    "containerd.io",
    "kubernetes.io",
    "gvisor.dev",
    "spiffe.io",
    "linkerd.io",
    "gateway-api.sigs.k8s.io",
    "csrc.nist.gov",
    "developer.hashicorp.com",
}

# Dominant vendors per Theme: a primary source on one of these hosts is the
# honest baseline, not the portability addition this test counts.
DOMINANT_VENDOR_HOSTS = {
    "containers": {"docs.docker.com", "www.docker.com"},
    "configuration-management": {"docs.ansible.com", "www.ansible.com", "spacelift.io"},
    "service-mesh": {"istio.io", "buoyant.io", "www.tetrate.io", "docs.cilium.io"},
}

# Floors for Questions carrying a neutral-authority primary source. They are
# deliberately below the current counts so an individual honest removal does
# not fail, while dropping the portability work wholesale does.
MIN_NEUTRAL_SOURCED_QUESTIONS = {
    "containers": 20,
    "configuration-management": 3,
    "service-mesh": 8,
}


def answer_guide(text: str) -> str:
    guide = text.split("## Answer guide", 1)[1].split("## References", 1)[0]
    return guide


def test_related_materials_state_vendor_bias() -> None:
    for theme in THEMES:
        page = ROOT / "docs" / "related-materials" / f"{theme}.md"
        text = page.read_text(encoding="utf-8")
        assert "## Vendor bias" in text, f"{page}: must state the Theme's vendor bias plainly"
        assert text.count("## Vendor bias") == 1, f"{page}: exactly one vendor-bias statement"


def test_every_vendor_neutral_question_maps_to_another_implementation() -> None:
    unmapped: list[str] = []
    for theme in THEMES:
        markers = PORTABILITY_MARKERS[theme]
        for question in sorted((ROOT / "questions" / theme).glob("*.md")):
            if not any(marker in answer_guide(question.read_text(encoding="utf-8")) for marker in markers):
                unmapped.append(str(question.relative_to(ROOT)))
    assert not unmapped, (
        "These vendor-neutral Questions do not map their concept onto another "
        "implementation in the answer guide:\n" + "\n".join(unmapped)
    )


def test_neutral_authorities_are_declared_primary_sources() -> None:
    counts = {theme: 0 for theme in THEMES}
    undersourced: list[str] = []
    for theme in THEMES:
        dominant = DOMINANT_VENDOR_HOSTS[theme]
        for question in sorted((ROOT / "questions" / theme).glob("*.md")):
            text = question.read_text(encoding="utf-8")
            hosts = {url.split("/")[2] for url in primary_source_urls(text, question)}
            if hosts - dominant & NEUTRAL_SOURCE_HOSTS:
                counts[theme] += 1
        if counts[theme] < MIN_NEUTRAL_SOURCED_QUESTIONS[theme]:
            undersourced.append(f"{theme}: {counts[theme]}")
    assert not undersourced, (
        "Themes with too few Questions citing a vendor-neutral authority as a "
        "primary source (expected at least "
        + ", ".join(f"{theme}: {minimum}" for theme, minimum in MIN_NEUTRAL_SOURCED_QUESTIONS.items())
        + "):\n" + "\n".join(undersourced)
    )


def main() -> None:
    test_related_materials_state_vendor_bias()
    test_every_vendor_neutral_question_maps_to_another_implementation()
    test_neutral_authorities_are_declared_primary_sources()
    total = sum(len(list((ROOT / "questions" / theme).glob("*.md"))) for theme in THEMES)
    print(f"Validated vendor-honesty coverage across {total} Questions in three Themes.")


if __name__ == "__main__":
    main()
