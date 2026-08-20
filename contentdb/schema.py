"""The Content store schema.

One SQLite database, rebuilt from scratch by every Ingest run: questions,
labs, themes, tags, their relations, Question sources, learning paths, and an
FTS5 index over title/prompt/body.  Foreign keys stay on; indexes cover the
columns the Content API filters by (``theme``, ``difficulty``, ``type``, tag
joins, and a Lab's ``question_ref``).

FTS5 is the only feature that not every ``sqlite3`` build carries.  The DDL
for it lives in :data:`FTS_DDL` and is created last, separately, so Ingest can
skip it and still deliver a fully readable store when the runtime lacks FTS5.
"""

from __future__ import annotations

SCHEMA_DDL = """
CREATE TABLE themes (
    name              TEXT PRIMARY KEY,
    state             TEXT NOT NULL,
    question_count    INTEGER NOT NULL,
    lab_count         INTEGER NOT NULL,
    difficulty_counts TEXT NOT NULL
);

CREATE TABLE tags (
    name           TEXT PRIMARY KEY,
    question_count INTEGER NOT NULL,
    lab_count      INTEGER NOT NULL
);

CREATE TABLE questions (
    id            TEXT PRIMARY KEY,
    theme         TEXT NOT NULL REFERENCES themes(name),
    slug          TEXT NOT NULL,
    title         TEXT NOT NULL,
    difficulty    TEXT NOT NULL CHECK (difficulty IN ('junior', 'middle', 'senior', 'staff')),
    type          TEXT NOT NULL CHECK (type IN ('theory', 'scenario', 'troubleshooting')),
    prompt        TEXT NOT NULL,
    answer_guide  TEXT NOT NULL,
    body_markdown TEXT NOT NULL,
    source_path   TEXT NOT NULL UNIQUE,
    content_hash  TEXT NOT NULL,
    updated_at    TEXT NOT NULL
);
CREATE INDEX idx_questions_theme ON questions(theme);
CREATE INDEX idx_questions_difficulty ON questions(difficulty);
CREATE INDEX idx_questions_type ON questions(type);

CREATE TABLE question_tags (
    question_id TEXT NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    position    INTEGER NOT NULL,
    tag         TEXT NOT NULL REFERENCES tags(name),
    PRIMARY KEY (question_id, tag)
);
CREATE INDEX idx_question_tags_tag ON question_tags(tag);

CREATE TABLE question_sources (
    question_id TEXT NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    position    INTEGER NOT NULL,
    url         TEXT NOT NULL,
    source_type TEXT NOT NULL,
    verified_on TEXT NOT NULL,
    PRIMARY KEY (question_id, position)
);

CREATE TABLE labs (
    id            TEXT PRIMARY KEY,
    theme         TEXT NOT NULL REFERENCES themes(name),
    slug          TEXT NOT NULL,
    title         TEXT NOT NULL,
    difficulty    TEXT NOT NULL CHECK (difficulty IN ('junior', 'middle', 'senior', 'staff')),
    question_ref  TEXT NOT NULL REFERENCES questions(id),
    why           TEXT NOT NULL,
    checklist     TEXT NOT NULL,
    body_markdown TEXT NOT NULL,
    source_path   TEXT NOT NULL UNIQUE,
    content_hash  TEXT NOT NULL,
    updated_at    TEXT NOT NULL
);
CREATE INDEX idx_labs_theme ON labs(theme);
CREATE INDEX idx_labs_difficulty ON labs(difficulty);
CREATE INDEX idx_labs_question_ref ON labs(question_ref);

CREATE TABLE lab_tags (
    lab_id   TEXT NOT NULL REFERENCES labs(id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    tag      TEXT NOT NULL REFERENCES tags(name),
    PRIMARY KEY (lab_id, tag)
);
CREATE INDEX idx_lab_tags_tag ON lab_tags(tag);

CREATE TABLE learning_paths (
    slug            TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    description     TEXT NOT NULL,
    icon            TEXT,
    color           TEXT,
    target_audience TEXT,
    certifications  TEXT NOT NULL DEFAULT '[]',
    prerequisites   TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE learning_path_steps (
    path_slug   TEXT NOT NULL REFERENCES learning_paths(slug) ON DELETE CASCADE,
    position    INTEGER NOT NULL,
    step_id     TEXT NOT NULL,
    skill_id    TEXT,
    title       TEXT,
    difficulty  TEXT,
    theme       TEXT,
    question_id TEXT REFERENCES questions(id),
    lab_slug    TEXT,
    concepts    TEXT NOT NULL DEFAULT '[]',
    why         TEXT,
    PRIMARY KEY (path_slug, position)
);

CREATE TABLE learning_path_prerequisites (
    path_slug       TEXT NOT NULL REFERENCES learning_paths(slug) ON DELETE CASCADE,
    step_id         TEXT NOT NULL,
    depends_on_step TEXT NOT NULL,
    PRIMARY KEY (path_slug, step_id, depends_on_step)
);

-- The snapshot's own provenance, written once by Ingest and read by the
-- Content API's `GET /api/v1/meta` and snapshot response header: which commit
-- the corpus was ingested from (`source_commit`), the pinned corpus-wide
-- digest (`content_digest`, see `contentdb.corpus.content_digest`), and when
-- that commit was made (`build_timestamp` — the commit's time, not the
-- wall-clock time of the Ingest run, so two builds stay byte-identical).
CREATE TABLE store_meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""

FTS_DDL = """
CREATE VIRTUAL TABLE content_search USING fts5(
    kind UNINDEXED,
    ref_id UNINDEXED,
    title,
    prompt,
    body,
    tokenize = 'porter'
);
"""

FTS_TABLE = "content_search"
