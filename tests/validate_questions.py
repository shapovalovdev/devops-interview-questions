import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
ALLOWED_DIFFICULTIES = {"junior", "middle", "senior", "staff"}
ALLOWED_TYPES = {"theory", "scenario", "troubleshooting"}
CONTAINER_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
OBSERVABILITY_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
SECURITY_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
SHELL_SCRIPTING_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
HARDWARE_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
STORAGE_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
QUEUE_MESSAGING_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
ADVANCED_CONTAINERS_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
CONFIGURATION_MANAGEMENT_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
DATABASES_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
CONTAINER_NETWORKING_DISTRIBUTION = {"junior": 5, "middle": 10, "senior": 5, "staff": 5}
ICA_MINIMUM_QUESTIONS = 15
CKAD_MINIMUM_QUESTIONS = 20
CKS_MINIMUM_QUESTIONS = 19
PCA_MINIMUM_QUESTIONS = 25


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---", f"{path}: front matter must begin with ---"
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        if not line or ": " not in line or line.startswith("  - ") or line.startswith("    "):
            continue
        key, value = line.split(": ", 1)
        fields[key] = value
    return fields


def known_tags() -> set[str]:
    text = (ROOT / "TAGS.md").read_text(encoding="utf-8")
    return set(re.findall(r"`([a-z0-9-]+)`", text))


def catalog_paths() -> list[str]:
    text = (ROOT / "assets/questions.js").read_text(encoding="utf-8")
    return re.findall(r'path: "([^"]+)"', text)


def main() -> None:
    question_files = sorted(QUESTIONS.glob("*/*.md"))
    assert question_files, "No active Questions found"
    tags = known_tags()
    catalog = catalog_paths()
    assert len(catalog) == len(set(catalog)), "Website catalog contains duplicate paths"

    expected_catalog = set()
    container_difficulties: dict[str, int] = {difficulty: 0 for difficulty in CONTAINER_DISTRIBUTION}
    observability_difficulties: dict[str, int] = {difficulty: 0 for difficulty in OBSERVABILITY_DISTRIBUTION}
    security_difficulties: dict[str, int] = {difficulty: 0 for difficulty in SECURITY_DISTRIBUTION}
    shell_scripting_difficulties: dict[str, int] = {difficulty: 0 for difficulty in SHELL_SCRIPTING_DISTRIBUTION}
    hardware_difficulties: dict[str, int] = {difficulty: 0 for difficulty in HARDWARE_DISTRIBUTION}
    storage_difficulties: dict[str, int] = {difficulty: 0 for difficulty in STORAGE_DISTRIBUTION}
    queue_messaging_difficulties: dict[str, int] = {difficulty: 0 for difficulty in QUEUE_MESSAGING_DISTRIBUTION}
    advanced_containers_difficulties: dict[str, int] = {difficulty: 0 for difficulty in ADVANCED_CONTAINERS_DISTRIBUTION}
    configuration_management_difficulties: dict[str, int] = {difficulty: 0 for difficulty in CONFIGURATION_MANAGEMENT_DISTRIBUTION}
    databases_difficulties: dict[str, int] = {difficulty: 0 for difficulty in DATABASES_DISTRIBUTION}
    container_networking_difficulties: dict[str, int] = {difficulty: 0 for difficulty in CONTAINER_NETWORKING_DISTRIBUTION}
    ica_questions = 0
    ckad_questions = 0
    cks_questions = 0
    pca_questions = 0
    for path in question_files:
        fields = front_matter(path)
        required = {"title", "theme", "difficulty", "type", "tags"}
        assert required <= fields.keys(), f"{path}: missing required front-matter fields"
        assert fields["theme"] == path.parent.name, f"{path}: theme must match canonical folder"
        assert fields["difficulty"] in ALLOWED_DIFFICULTIES, f"{path}: invalid difficulty"
        assert fields["type"] in ALLOWED_TYPES, f"{path}: invalid Question type"
        question_tags = re.findall(r"[a-z0-9-]+", fields["tags"])
        assert question_tags, f"{path}: requires at least one Tag"
        assert set(question_tags) <= tags, f"{path}: uses a Tag missing from TAGS.md"
        content = path.read_text(encoding="utf-8")
        assert "## Answer guide" in content, f"{path}: missing answer guide"
        answer = content.split("## Answer guide", 1)[1].split("## References", 1)[0]
        answer_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", answer)
        assert len(answer_words) >= 60, f"{path}: answer guide is too short for a full answer"
        assert len(re.findall(r"^- ", answer, re.MULTILINE)) >= 3, f"{path}: answer guide requires direct answer, constraints, and operational guidance"
        assert re.search(r"^sources:\n  - url: https://", content, re.MULTILINE), f"{path}: missing HTTPS primary source metadata"
        assert re.search(r"^    source_type: (standard|official-docs|official-api)$", content, re.MULTILINE), f"{path}: invalid source type"
        assert re.search(r"^    verified_on: \d{4}-\d{2}-\d{2}$", content, re.MULTILINE), f"{path}: missing source verification date"
        assert "## References" in content, f"{path}: missing References section"
        assert re.search(r"^- \[.*\]\(https://", content, re.MULTILINE), f"{path}: requires a primary reference"
        assert re.search(r"^- Further reading \(blog\): .*\(https://", content, re.MULTILINE), f"{path}: requires a labeled complementary blog post"
        if fields["theme"] == "containers":
            container_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "observability":
            observability_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "security":
            security_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "shell-scripting":
            shell_scripting_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "hardware":
            hardware_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "storage":
            storage_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "queue-messaging":
            queue_messaging_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "advanced-containers":
            advanced_containers_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "configuration-management":
            configuration_management_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "databases":
            databases_difficulties[fields["difficulty"]] += 1
        if fields["theme"] == "container-networking":
            container_networking_difficulties[fields["difficulty"]] += 1
        if "ckad" in question_tags:
            ckad_questions += 1
        if "cks" in question_tags:
            cks_questions += 1
        if "ica" in question_tags:
            ica_questions += 1
        if "pca" in question_tags:
            pca_questions += 1
        expected_catalog.add(path.relative_to(ROOT).with_suffix(".html").as_posix())

    assert set(catalog) == expected_catalog, "Website catalog must contain every active Question exactly once"
    assert container_difficulties == CONTAINER_DISTRIBUTION, f"containers must contain {CONTAINER_DISTRIBUTION}, got {container_difficulties}"
    assert observability_difficulties == OBSERVABILITY_DISTRIBUTION, f"observability must contain {OBSERVABILITY_DISTRIBUTION}, got {observability_difficulties}"
    assert security_difficulties == SECURITY_DISTRIBUTION, f"security must contain {SECURITY_DISTRIBUTION}, got {security_difficulties}"
    assert shell_scripting_difficulties == SHELL_SCRIPTING_DISTRIBUTION, f"shell-scripting must contain {SHELL_SCRIPTING_DISTRIBUTION}, got {shell_scripting_difficulties}"
    assert hardware_difficulties == HARDWARE_DISTRIBUTION, f"hardware must contain {HARDWARE_DISTRIBUTION}, got {hardware_difficulties}"
    assert storage_difficulties == STORAGE_DISTRIBUTION, f"storage must contain {STORAGE_DISTRIBUTION}, got {storage_difficulties}"
    assert queue_messaging_difficulties == QUEUE_MESSAGING_DISTRIBUTION, f"queue-messaging must contain {QUEUE_MESSAGING_DISTRIBUTION}, got {queue_messaging_difficulties}"
    assert advanced_containers_difficulties == ADVANCED_CONTAINERS_DISTRIBUTION, f"advanced-containers must contain {ADVANCED_CONTAINERS_DISTRIBUTION}, got {advanced_containers_difficulties}"
    assert configuration_management_difficulties == CONFIGURATION_MANAGEMENT_DISTRIBUTION, f"configuration-management must contain {CONFIGURATION_MANAGEMENT_DISTRIBUTION}, got {configuration_management_difficulties}"
    assert databases_difficulties == DATABASES_DISTRIBUTION, f"databases must contain {DATABASES_DISTRIBUTION}, got {databases_difficulties}"
    assert container_networking_difficulties == CONTAINER_NETWORKING_DISTRIBUTION, f"container-networking must contain {CONTAINER_NETWORKING_DISTRIBUTION}, got {container_networking_difficulties}"
    assert "ckad" in tags, "CKAD certification tag must be documented in TAGS.md"
    assert (ROOT / "docs/certifications/ckad.md").is_file(), "CKAD certification map is required"
    assert ckad_questions >= CKAD_MINIMUM_QUESTIONS, f"CKAD requires at least {CKAD_MINIMUM_QUESTIONS} mapped Questions, got {ckad_questions}"
    assert "cks" in tags, "CKS certification tag must be documented in TAGS.md"
    assert (ROOT / "docs/certifications/cks.md").is_file(), "CKS certification map is required"
    assert cks_questions >= CKS_MINIMUM_QUESTIONS, f"CKS requires at least {CKS_MINIMUM_QUESTIONS} mapped Questions, got {cks_questions}"
    assert "ica" in tags, "ICA certification tag must be documented in TAGS.md"
    assert (ROOT / "docs/certifications/ica.md").is_file(), "ICA certification map is required"
    assert ica_questions >= ICA_MINIMUM_QUESTIONS, f"ICA requires at least {ICA_MINIMUM_QUESTIONS} mapped Questions, got {ica_questions}"
    assert "pca" in tags, "PCA certification tag must be documented in TAGS.md"
    assert (ROOT / "docs/certifications/pca.md").is_file(), "PCA certification map is required"
    assert pca_questions >= PCA_MINIMUM_QUESTIONS, f"PCA requires at least {PCA_MINIMUM_QUESTIONS} mapped Questions, got {pca_questions}"
    print(f"Validated {len(question_files)} active Questions and {len(catalog)} website records.")


if __name__ == "__main__":
    main()
