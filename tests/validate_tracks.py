#!/usr/bin/env python3
"""Validate declarative learning path track manifests and their prerequisite DAGs."""

from __future__ import annotations

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKS_DIR = ROOT / "tracks"
QUESTIONS_DIR = ROOT / "questions"
LABS_DIR = ROOT / "labs"

VALID_DIFFICULTIES = {"junior", "middle", "senior", "staff"}


def load_tracks() -> list[dict]:
    """Load all track manifest JSON and YAML files."""
    assert TRACKS_DIR.is_dir(), f"Track manifests directory not found at {TRACKS_DIR}"
    track_files = sorted(TRACKS_DIR.glob("*.json"))
    if not track_files:
        try:
            import yaml
            track_files = sorted(list(TRACKS_DIR.glob("*.yml")) + list(TRACKS_DIR.glob("*.yaml")))
        except ImportError:
            track_files = []

    assert track_files, f"No track manifests found in {TRACKS_DIR}"
    tracks = []
    for path in track_files:
        with open(path, "r", encoding="utf-8") as f:
            if path.suffix == ".json":
                data = json.load(f)
            else:
                import yaml
                data = yaml.safe_load(f)
            assert isinstance(data, dict), f"{path}: manifest root must be a mapping"
            tracks.append(data)
    return tracks


def validate_dag(track_id: str, steps: list[dict]) -> None:
    """Verify that prerequisites form a valid Directed Acyclic Graph (DAG) with no cycles."""
    step_ids = {s["id"] for s in steps}
    adj: dict[str, list[str]] = {s["id"]: [] for s in steps}

    for step in steps:
        step_id = step["id"]
        for prereq in step.get("prerequisites", []):
            assert prereq in step_ids, (
                f"Track '{track_id}', step '{step_id}' references unknown prerequisite '{prereq}'"
            )
            assert prereq != step_id, f"Track '{track_id}', step '{step_id}' cannot depend on itself"
            adj[prereq].append(step_id)

    # Cycle detection via DFS (0 = unvisited, 1 = visiting, 2 = visited)
    visited: dict[str, int] = {s["id"]: 0 for s in steps}

    def dfs(node: str, path: list[str]) -> None:
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 1:
                cycle = " -> ".join(path + [neighbor])
                raise AssertionError(f"Cycle detected in track '{track_id}': {cycle}")
            if visited[neighbor] == 0:
                dfs(neighbor, path + [neighbor])
        visited[node] = 2

    for step in steps:
        if visited[step["id"]] == 0:
            dfs(step["id"], [step["id"]])


def validate_track(track: dict) -> None:
    """Validate a single track manifest against content and schema rules."""
    for required in ("id", "name", "description", "icon", "color", "steps"):
        assert required in track, f"Track missing required field '{required}': {track}"

    track_id = track["id"]
    steps = track["steps"]
    assert isinstance(steps, list) and len(steps) > 0, f"Track '{track_id}' must have at least one step"

    seen_step_ids = set()
    seen_skills = set()

    for step in steps:
        for req_step in ("id", "skill_id", "title", "description", "difficulty", "theme", "concepts"):
            assert req_step in step, f"Track '{track_id}' step missing required field '{req_step}': {step}"

        step_id = step["id"]
        assert step_id not in seen_step_ids, f"Track '{track_id}' duplicate step id '{step_id}'"
        seen_step_ids.add(step_id)

        skill_id = step["skill_id"]
        assert skill_id not in seen_skills, f"Track '{track_id}' duplicate skill_id '{skill_id}'"
        seen_skills.add(skill_id)

        diff = step["difficulty"]
        assert diff in VALID_DIFFICULTIES, f"Track '{track_id}' invalid difficulty '{diff}' in step '{step_id}'"

        # Validate Question Reference
        if "question_id" in step and step["question_id"]:
            q_rel = step["question_id"]
            q_path = QUESTIONS_DIR / f"{q_rel}.md"
            assert q_path.is_file(), (
                f"Track '{track_id}' step '{step_id}' references non-existent question '{q_rel}' ({q_path})"
            )

        # Validate Lab Reference
        if "lab_slug" in step and step["lab_slug"]:
            lab_rel = step["lab_slug"]
            lab_path = LABS_DIR / f"{lab_rel}.md"
            assert lab_path.is_file(), (
                f"Track '{track_id}' step '{step_id}' references non-existent lab '{lab_rel}' ({lab_path})"
            )

    # Validate DAG Structure
    validate_dag(track_id, steps)


def main() -> None:
    tracks = load_tracks()
    for track in tracks:
        validate_track(track)
    print(f"Validated {len(tracks)} track manifests across {sum(len(t['steps']) for t in tracks)} competency steps successfully (0 cycles).")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as err:
        print(f"Validation failed: {err}", file=sys.stderr)
        sys.exit(1)
