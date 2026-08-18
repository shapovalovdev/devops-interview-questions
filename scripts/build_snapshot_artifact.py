#!/usr/bin/env python3
"""Build and verify immutable, digest-addressed Content API snapshots.

The released archive is intentionally self-contained: it carries the SQLite
store, the same metadata shape as ``GET /api/v1/meta``, and checksums for both
files.  The archive checksum is adjacent to the archive rather than inside it,
because an archive cannot truthfully contain a checksum of its final bytes.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import sqlite3
import sys
import tarfile
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from contentdb import ingest


API_VERSION = "v1"
LICENSE = {
    "name": "CC BY 4.0",
    "spdx_id": "CC-BY-4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/",
}
ATTRIBUTION = "https://github.com/shapovalovdev/devops-interview-questions"
CONTENTS = ("content.db", "snapshot.json", "SHA256SUMS")


@dataclass(frozen=True)
class Artifact:
    """Paths and identity of one completed snapshot artifact."""

    archive: Path
    checksum: Path
    content_digest: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def timestamp_seconds(timestamp: str) -> int:
    """Convert the store's UTC build timestamp to the tar/gzip timestamp."""
    parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError(f"build timestamp must include a timezone: {timestamp!r}")
    return int(parsed.astimezone(timezone.utc).timestamp())


def store_meta(database: Path) -> dict[str, str]:
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        meta = dict(connection.execute("SELECT key, value FROM store_meta"))
    finally:
        connection.close()
    required = ("source_commit", "content_digest", "build_timestamp")
    missing = [key for key in required if not meta.get(key)]
    if missing:
        raise ValueError(f"content.db has no snapshot metadata for {', '.join(missing)}")
    return meta


def snapshot_from_store(database: Path) -> dict[str, object]:
    """The exact object the API's ``GET /api/v1/meta`` returns."""
    meta = store_meta(database)
    return {
        "source_commit": meta["source_commit"],
        "content_digest": meta["content_digest"],
        "api_version": API_VERSION,
        "build_timestamp": meta["build_timestamp"],
        "license": LICENSE,
        "attribution": ATTRIBUTION,
    }


def checksum_lines(files: dict[str, bytes]) -> bytes:
    return "".join(f"{sha256_bytes(files[name])}  {name}\n" for name in sorted(files)).encode("ascii")


def write_archive(archive: Path, files: dict[str, bytes], mtime: int) -> None:
    """Write a byte-reproducible gzip-compressed tar archive."""
    with archive.open("wb") as raw:
        # An empty filename avoids a host-path field in the gzip header.
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=mtime) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.GNU_FORMAT) as bundle:
                for name in sorted(files):
                    entry = tarfile.TarInfo(name)
                    entry.size = len(files[name])
                    entry.mode = 0o644
                    entry.uid = entry.gid = 0
                    entry.uname = entry.gname = ""
                    entry.mtime = mtime
                    bundle.addfile(entry, io.BytesIO(files[name]))


def build_artifact(
    root: Path,
    output_dir: Path,
    *,
    source_commit: str | None = None,
    build_timestamp: str | None = None,
) -> Artifact:
    """Ingest ``root`` and package its immutable snapshot into ``output_dir``."""
    root = Path(root)
    output_dir = Path(output_dir)
    commit = source_commit or ingest.source_commit_at(root)
    timestamp = build_timestamp or ingest.build_timestamp_for(root, commit)
    mtime = timestamp_seconds(timestamp)
    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="content-snapshot-") as temporary:
        database = Path(temporary) / "content.db"
        ingest.build(root, database, source_commit=commit, build_timestamp=timestamp)
        snapshot = snapshot_from_store(database)
        snapshot_bytes = (json.dumps(snapshot, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        files = {"content.db": database.read_bytes(), "snapshot.json": snapshot_bytes}
        files["SHA256SUMS"] = checksum_lines(files)
        digest = str(snapshot["content_digest"])
        archive = output_dir / f"content-snapshot-{digest}.tar.gz"
        write_archive(archive, files, mtime)

    checksum = archive.with_name(archive.name + ".sha256")
    checksum.write_text(f"{sha256_file(archive)}  {archive.name}\n", encoding="ascii")
    return Artifact(archive=archive, checksum=checksum, content_digest=digest)


def parse_checksums(data: bytes) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for line in data.decode("ascii").splitlines():
        digest, separator, name = line.partition("  ")
        if not separator or len(digest) != 64 or not name or name in checksums:
            raise ValueError("SHA256SUMS is malformed")
        checksums[name] = digest
    return checksums


def digest_from_store(database: Path) -> str:
    """Recompute the documented digest recipe from an extracted store alone."""
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        pairs = connection.execute(
            "SELECT id, content_hash FROM questions UNION ALL SELECT id, content_hash FROM labs "
            "ORDER BY id, content_hash"
        ).fetchall()
    finally:
        connection.close()
    material = "".join(f"{identifier} {content_hash}\n" for identifier, content_hash in pairs)
    return sha256_bytes(material.encode("utf-8"))


def verify_artifact(archive: Path, checksum: Path | None = None) -> dict[str, object]:
    """Verify an archive without a corpus checkout or a running API."""
    archive = Path(archive)
    if checksum is not None:
        expected, separator, name = Path(checksum).read_text(encoding="ascii").strip().partition("  ")
        if separator != "  " or name != archive.name or expected != sha256_file(archive):
            raise ValueError(f"archive checksum does not match {archive.name}")
    with tarfile.open(archive, "r:gz") as bundle:
        members = bundle.getmembers()
        names = [member.name for member in members]
        if names != sorted(CONTENTS) or any(not member.isfile() for member in members):
            raise ValueError("archive must contain only content.db, snapshot.json, and SHA256SUMS")
        files = {name: bundle.extractfile(name).read() for name in names}
    checksums = parse_checksums(files["SHA256SUMS"])
    expected_files = {"content.db", "snapshot.json"}
    if set(checksums) != expected_files or any(checksums[name] != sha256_bytes(files[name]) for name in checksums):
        raise ValueError("contained file checksum does not match SHA256SUMS")
    snapshot = json.loads(files["snapshot.json"])
    if set(snapshot) != {"source_commit", "content_digest", "api_version", "build_timestamp", "license", "attribution"}:
        raise ValueError("snapshot.json does not have the API metadata shape")
    with tempfile.TemporaryDirectory(prefix="content-snapshot-verify-") as temporary:
        database = Path(temporary) / "content.db"
        database.write_bytes(files["content.db"])
        expected_snapshot = snapshot_from_store(database)
        if snapshot != expected_snapshot:
            raise ValueError("snapshot.json does not match content.db metadata")
        if snapshot["content_digest"] != digest_from_store(database):
            raise ValueError("content.db does not match its content digest")
    return snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build or verify a Content API snapshot release artifact.")
    parser.add_argument("--root", type=Path, default=ROOT, help="corpus repository root")
    parser.add_argument("--output-dir", type=Path, default=Path("build/snapshots"), help="artifact destination")
    parser.add_argument("--source-commit", help="explicit source Git SHA")
    parser.add_argument("--build-timestamp", help="explicit deterministic commit timestamp")
    parser.add_argument("--verify", type=Path, metavar="ARCHIVE", help="verify an existing archive instead of building")
    parser.add_argument("--checksum", type=Path, help="adjacent archive checksum to verify")
    arguments = parser.parse_args(argv)
    try:
        if arguments.verify:
            snapshot = verify_artifact(arguments.verify, arguments.checksum)
            print(f"Verified {arguments.verify}: {snapshot['content_digest']}")
        else:
            artifact = build_artifact(
                arguments.root,
                arguments.output_dir,
                source_commit=arguments.source_commit,
                build_timestamp=arguments.build_timestamp,
            )
            print(f"Built {artifact.archive}")
            print(f"Wrote {artifact.checksum}")
    except (OSError, ValueError, sqlite3.Error, tarfile.TarError) as error:
        print(f"Snapshot artifact failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
