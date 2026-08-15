# Ordered learning paths

A learning path is an ordered route through Questions that already exist. It is **data, not prose**, and the ordering belongs to the path rather than to the Question, so the same Question can hold position 4 in one path and position 27 in another without a single Question file changing. Nothing about a path appears in Question front matter.

Paths are declared in [`config/learning-paths.json`](../config/learning-paths.json), the way certification tracks are declared in `config/content-manifest.json`.

## Schema

```json
{
  "version": 1,
  "paths": [
    {
      "slug": "sre-track",
      "title": "Site reliability engineering",
      "audience": "Who this path is written for",
      "prerequisites": [],
      "steps": [
        { "question": "questions/sre/explain-error-budget.md", "why": "why this Question belongs at this position" }
      ]
    }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `version` | Manifest schema version. Currently `1`. |
| `slug` | Lowercase, hyphen-separated. It is the URL state: `index.html#path=<slug>`. |
| `title` | Human title shown at the head of the path view. |
| `audience` | One sentence naming the reader who should follow this path. |
| `prerequisites` | List of other path slugs to complete first. Empty for an entry-level path. |
| `steps` | The ordered route. Position in this array *is* the step number. |
| `steps[].question` | Repository-relative path to an existing Markdown Question. |
| `steps[].why` | Why this Question earns *this* position. |

## Adding a path

1. Append a path object to `paths`. Do not touch any Question file.
2. Run `python3 scripts/generate_question_catalog.py` to republish `assets/questions.js`; the site reads paths from the generated `window.learningPaths`, where each step is resolved to its title, theme, difficulty, and `href`. Never hand-edit that file.
3. Run `python3 tests/test_learning_paths.py`.

The site picks a new path up automatically: it gains a button in the landing view's **Learning paths** bank and an ordered view at `#path=<slug>`. No change to `index.html`, `assets/site.js`, or `assets/site.css` is needed. The masthead shortcut beside the drill deck is a deliberate exception — it points at one flagship path, currently `sre-track`, and only changes if the flagship does.

## Writing a `why`

A `why` explains the **position**, not the topic. The reader can see the title; what they cannot see is why they are being sent here now.

- Weak: "Covers alerting."
- Earned: "You need burn-rate maths before the multi-window alert question is meaningful."

Order by pedagogy rather than by the difficulty label. A staff Question on error-budget policy belongs after the middle Question that explains what an error budget is, because policy is meaningless without the arithmetic underneath it. Read the Questions you are sequencing; do not order by title.

## Declared paths

- [`sre-track`](../index.html#path=sre-track) — foundations to staff for engineers moving into an SRE or on-call role.
