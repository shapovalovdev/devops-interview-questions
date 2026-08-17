"""A tiny, complete corpus the Content store tests can predict answers about.

The live corpus is the right fixture for "did Ingest read everything?" and for
determinism, but it is useless for "does `theme=linux&difficulty=staff` return
exactly one row?" — the answer changes every time somebody writes a Question.
So the query and failure tests run against the corpus built here: eight
Questions, three Labs, two active Themes and one planned one, chosen so that
every filter the Content API exposes has at least one row that matches and one
that does not.

This module is deliberately not named `test_*.py`: `tests/run_all_tests.py`
discovers checks by that prefix, and a fixture builder is not a check.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


THEMES = ("kubernetes", "linux", "queue-messaging")

TAGS_MD = """# Tag vocabulary

## Technologies and concepts

`kubernetes`, `linux`, `security`, `storage`, `networking`, `troubleshooting`, `unused-tag`

## Certifications

`cks`
"""


@dataclass(frozen=True)
class QuestionSpec:
    theme: str
    slug: str
    title: str
    difficulty: str
    type: str
    tags: tuple[str, ...]
    prompt: str
    #: An extra body paragraph, used to give the search-ranking test a Question
    #: that mentions a term only in its body and never in its title or prompt.
    body_note: str = ""


@dataclass(frozen=True)
class LabSpec:
    theme: str
    slug: str
    title: str
    difficulty: str
    question_ref: str
    tags: tuple[str, ...]


QUESTIONS = (
    QuestionSpec(
        "kubernetes",
        "admission-policy",
        "Design an admission policy",
        "senior",
        "scenario",
        ("kubernetes", "security", "cks"),
        "How would you roll out an admission policy without breaking every existing workload?",
    ),
    QuestionSpec(
        "kubernetes",
        "pod-scheduling",
        "Explain pod scheduling",
        "junior",
        "theory",
        ("kubernetes",),
        "What decides which node a pod lands on?",
    ),
    QuestionSpec(
        "kubernetes",
        "crashloop-debug",
        "Debug a CrashLoopBackOff",
        "middle",
        "troubleshooting",
        ("kubernetes", "troubleshooting"),
        "A deployment is stuck in CrashLoopBackOff. How do you find out why?",
    ),
    QuestionSpec(
        "kubernetes",
        "etcd-backup",
        "Plan an etcd backup strategy",
        "staff",
        "scenario",
        ("kubernetes", "storage"),
        "How do you make etcd restorable without pretending a snapshot is a plan?",
    ),
    QuestionSpec(
        "linux",
        "disk-full",
        "Recover a full filesystem",
        "middle",
        "troubleshooting",
        ("linux", "storage", "troubleshooting"),
        "A production host reports a full filesystem but du disagrees with df. What now?",
    ),
    QuestionSpec(
        "linux",
        "systemd-unit",
        "Read a failing systemd unit",
        "junior",
        "theory",
        ("linux",),
        "Where does a failing unit tell you what it tried to do?",
    ),
    QuestionSpec(
        "linux",
        "kernel-tuning",
        "Justify a kernel tuning change",
        "senior",
        "theory",
        ("linux", "networking"),
        "Which evidence would convince you to change a sysctl on a busy host?",
        body_note="A cluster admission policy can also block the change, which is worth knowing about.",
    ),
    QuestionSpec(
        "linux",
        "capacity-planning",
        "Own capacity planning for a fleet",
        "staff",
        "scenario",
        ("linux",),
        "How do you turn growth guesses into a defensible capacity plan?",
    ),
)

LABS = (
    LabSpec(
        "kubernetes",
        "admission-lab",
        "Build an admission policy in a throwaway cluster",
        "middle",
        "kubernetes/admission-policy.md",
        ("kubernetes", "security"),
    ),
    LabSpec(
        "linux",
        "disk-lab",
        "Fill a disk on purpose and recover it",
        "junior",
        "linux/disk-full.md",
        ("linux", "storage"),
    ),
    LabSpec(
        "linux",
        "systemd-lab",
        "Break and repair a systemd unit",
        "senior",
        "linux/systemd-unit.md",
        ("linux", "troubleshooting"),
    ),
)


def question_markdown(spec: QuestionSpec) -> str:
    return (
        "---\n"
        f"title: {spec.title}\n"
        f"theme: {spec.theme}\n"
        f"difficulty: {spec.difficulty}\n"
        f"type: {spec.type}\n"
        f"tags: [{', '.join(spec.tags)}]\n"
        "sources:\n"
        f"  - url: https://example.invalid/{spec.theme}/{spec.slug}\n"
        "    source_type: official-docs\n"
        "    verified_on: 2026-08-06\n"
        "---\n"
        "\n"
        f"# {spec.title}\n"
        "\n"
        f"{spec.prompt}\n"
        "\n"
        "## Answer guide\n"
        "\n"
        "- Name the mechanism and the evidence that proves it is the mechanism.\n"
        "- State the constraint that makes the obvious answer wrong here.\n"
        "- Say what you would do first in production and how you would roll it back.\n"
        "\n"
        + (f"{spec.body_note}\n\n" if spec.body_note else "")
        + "## References\n"
        "\n"
        f"- [Reference]( https://example.invalid/{spec.theme} )\n"
    )


def lab_markdown(spec: LabSpec) -> str:
    return (
        "---\n"
        f'title: "{spec.title}"\n'
        f'theme: "{spec.theme}"\n'
        f'difficulty: "{spec.difficulty}"\n'
        f'question_ref: "{spec.question_ref}"\n'
        f"tags: [{', '.join(spec.tags)}]\n"
        f'why: "This lab drills the {spec.theme} skill the linked Question asks about, on real '
        'infrastructure rather than from memory, so the answer comes from having done it."\n'
        "checklist:\n"
        '  - "Stand the environment up from nothing."\n'
        '  - "Reproduce the failure the Question describes."\n'
        '  - "Repair it and write down which signal proved the repair worked."\n'
        "---\n"
        "\n"
        f"# {spec.title}\n"
        "\n"
        "## Exercise 1\n"
        "\n"
        "Do the thing, then explain what you saw.\n"
    )


LEARNING_PATHS = {
    "version": 1,
    "paths": [
        {
            "slug": "kubernetes-track",
            "title": "Kubernetes from scheduling to policy",
            "audience": "Engineers who can run kubectl but have never had to defend a cluster policy decision",
            "prerequisites": ["linux basics"],
            "steps": [
                {
                    "question": "questions/kubernetes/pod-scheduling.md",
                    "why": "Everything else assumes you know where a pod ends up and why.",
                },
                {
                    "question": "questions/kubernetes/admission-policy.md",
                    "why": "Policy is only enforceable once scheduling is understood.",
                },
            ],
        }
    ],
}


def write_corpus(root: Path) -> Path:
    """Write the whole fixture corpus under `root` and return it."""
    (root / "config").mkdir(parents=True, exist_ok=True)
    (root / "TAGS.md").write_text(TAGS_MD, encoding="utf-8")
    (root / "config" / "content-manifest.json").write_text(
        json.dumps(
            {
                "schema_version": 2,
                "themes": [
                    {"name": "kubernetes", "state": "complete"},
                    {"name": "linux", "state": "complete"},
                    {"name": "queue-messaging", "state": "planned"},
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (root / "config" / "learning-paths.json").write_text(
        json.dumps(LEARNING_PATHS, indent=2) + "\n", encoding="utf-8"
    )
    for spec in QUESTIONS:
        path = root / "questions" / spec.theme / f"{spec.slug}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(question_markdown(spec), encoding="utf-8")
    for spec in LABS:
        path = root / "labs" / spec.theme / f"{spec.slug}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(lab_markdown(spec), encoding="utf-8")
    return root
