#!/usr/bin/env python3
"""Render the site's Markdown corpus to HTML with zero Jekyll involvement.

`scripts/build_site.py` is the one command any host needs: it rebuilds the
GitHub Pages URL layout (`questions/<theme>/<slug>.md` renders beside its
source at `questions/<theme>/<slug>.html`, same for `docs/**/*.md`) into a
build output directory, copies the hand-written root pages and static
directories verbatim, and depends on nothing but the Python standard
library.  The renderer intentionally covers only the Markdown subset the
corpus actually uses (see `docs/agents/domain.md`): ATX headings, paragraphs,
bullet and ordered lists with lazy continuation lines, fenced code blocks,
pipe tables, horizontal rules, and the inline constructs code span, link,
bold, and italic.  Internal Question links written as `.md` are rewritten to
the rendered `.html` so every relative link in the generated pages resolves
within the build.
"""

from __future__ import annotations

import argparse
import html
import posixpath
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
CONFIG = ROOT / "config"
LABS = ROOT / "labs"
DEFAULT_OUTPUT = ROOT / "build" / "site"

FRONT_MATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
BULLET_ITEM = re.compile(r"^- (.*)$")
ORDERED_ITEM = re.compile(r"^\d+\. (.*)$")
CONTINUATION = re.compile(r"^ +(\S.*)$")
FENCE = re.compile(r"^```(\S*)\s*$")
TABLE_ROW = re.compile(r"^\|(.*)\|\s*$")
TABLE_SEPARATOR = re.compile(r"^\|? *:?-{3,}:? *(\| *:?-{3,}:? *)*\|?\s*$")
HR = re.compile(r"^ {0,3}(?:-{3,}|\*{3,}|_{3,})\s*$")
ORDERED_START = re.compile(r"^\d+\. ")
CODE_SPAN = re.compile(r"(`+)(.+?)\1")
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BOLD = re.compile(r"\*\*(.+?)\*\*")
ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
TITLE_FIELD = re.compile(r"^title:\s*(.+)$", re.MULTILINE)

ROOT_PAGES = ("index.html", "404.html", "session.html")
STATIC_DIRS = (ASSETS, CONFIG)

TEMPLATE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="DevOps interview question database" />
    <title>{title}</title>
    <style>
      :root {{ color-scheme: light dark; }}
      body {{
        margin: 0 auto;
        padding: 2rem 1.25rem 4rem;
        max-width: 46rem;
        font: 1rem/1.65 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
        color: #1f2430;
        background: #fbfaf7;
      }}
      @media (prefers-color-scheme: dark) {{
        body {{ color: #d6dae3; background: #16181f; }}
        a {{ color: #8ab4f8; }}
        code, pre {{ background: #21242e; }}
        th, td {{ border-color: #3a3f4e; }}
        blockquote {{ border-color: #3a3f4e; color: #aeb4c0; }}
      }}
      a {{ color: #2050b0; }}
      header.site {{ margin-bottom: 2rem; font-size: 0.85rem; }}
      header.site a {{ text-decoration: none; }}
      h1 {{
        font-size: 1.9rem;
        line-height: 1.25;
        margin: 0 0 1rem;
        letter-spacing: -0.01em;
      }}
      h2 {{
        font-size: 1.3rem;
        margin: 2.25rem 0 0.75rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(128, 128, 128, 0.25);
      }}
      h3 {{ font-size: 1.1rem; margin: 1.75rem 0 0.5rem; }}
      code {{
        font: 0.875em ui-monospace, "DM Mono", "SFMono-Regular", Menlo, Consolas, monospace;
        background: rgba(128, 128, 128, 0.14);
        border-radius: 3px;
        padding: 0.1em 0.35em;
      }}
      pre {{
        overflow-x: auto;
        padding: 1rem 1.25rem;
        border-radius: 6px;
        background: rgba(128, 128, 128, 0.12);
      }}
      pre code {{ background: none; padding: 0; }}
      table {{ border-collapse: collapse; width: 100%; margin: 1.25rem 0; font-size: 0.95rem; }}
      th, td {{ border: 1px solid rgba(128, 128, 128, 0.35); padding: 0.45rem 0.6rem; text-align: left; vertical-align: top; }}
      th {{ background: rgba(128, 128, 128, 0.1); }}
      ul, ol {{ padding-left: 1.5rem; }}
      li {{ margin: 0.35rem 0; }}
      blockquote {{
        margin: 1.25rem 0;
        padding: 0.25rem 1rem;
        border-left: 3px solid rgba(128, 128, 128, 0.4);
        color: #4c5566;
      }}
      hr {{ border: none; border-top: 1px solid rgba(128, 128, 128, 0.35); margin: 2.5rem 0; }}
      footer {{ margin-top: 3rem; font-size: 0.8rem; color: #6b7280; }}
    </style>
  </head>
  <body>
    <header class="site"><a href="{home}">← DevOps Question Field Manual</a></header>
    <main>
{body}
    </main>
    <footer>Original / paraphrased content · CC BY 4.0</footer>
  </body>
</html>
"""


def strip_front_matter(text: str) -> str:
    return FRONT_MATTER.sub("", text, count=1)


def front_matter_title(text: str) -> str | None:
    if not FRONT_MATTER.search(text):
        return None
    match = TITLE_FIELD.search(text)
    return match.group(1).strip().strip("\"'") if match else None


def rewrite_internal_link(url: str, source: Path) -> str:
    """Point a corpus-relative `.md` link at the rendered `.html` page."""
    if "://" in url or url.startswith("#") or not url.endswith(".md"):
        return url
    relative_dir = source.parent.relative_to(ROOT).as_posix()
    target = ROOT / Path(posixpath.normpath(posixpath.join(relative_dir, url)))
    if target.suffix != ".md" or not target.is_file():
        return url
    if QUESTIONS not in target.parents and DOCS not in target.parents:
        return url
    return url[: -len(".md")] + ".html"


def render_inline(text: str, source: Path) -> str:
    """Render the corpus's inline subset: code spans, links, bold, italic."""
    code_spans: list[str] = []

    def stash(match: re.Match[str]) -> str:
        code_spans.append(html.escape(match.group(2)))
        return f"\x00{len(code_spans) - 1}\x00"

    text = CODE_SPAN.sub(stash, text)
    text = html.escape(text, quote=False)

    def link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        url = rewrite_internal_link(url, source)
        return f'<a href="{html.escape(url, quote=True)}">{label}</a>'

    text = LINK.sub(link, text)
    text = BOLD.sub(r"<strong>\1</strong>", text)
    text = ITALIC.sub(r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{code_spans[int(m.group(1))]}</code>", text)


def _split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_markdown(text: str, source: Path) -> str:
    lines = text.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    fence: str | None = None
    fence_buffer: list[str] = []
    table_buffer: list[str] = []
    list_items: list[tuple[str, str]] = []  # (marker, text)
    list_marker: str | None = None

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(f"<p>{render_inline(' '.join(paragraph), source)}</p>")
            paragraph.clear()

    def flush_table() -> None:
        if not table_buffer:
            return
        header = _split_table_row(table_buffer[0])
        body = [_split_table_row(row) for row in table_buffer[2:]]
        cells = lambda row: "".join(f"<td>{render_inline(cell, source)}</td>" for cell in row)  # noqa: E731
        head = "".join(f"<th>{render_inline(cell, source)}</th>" for cell in header)
        rows = "".join(f"<tr>{cells(row)}</tr>" for row in body)
        blocks.append(f"<table>\n<thead><tr>{head}</tr></thead>\n<tbody>\n{rows}\n</tbody>\n</table>")
        table_buffer.clear()

    def flush_list() -> None:
        nonlocal list_marker
        if list_marker:
            tag = "ol" if list_marker == "1" else "ul"
            items = "".join(f"<li>{render_inline(text_, source)}</li>" for _, text_ in list_items)
            blocks.append(f"<{tag}>\n{items}\n</{tag}>")
            list_items.clear()
            list_marker = None

    def flush_all() -> None:
        flush_paragraph()
        flush_table()
        flush_list()

    for line in lines:
        if fence is not None:
            if FENCE.match(line):
                classes = f' class="language-{fence}"' if fence else ""
                blocks.append(f"<pre><code{classes}>\n{html.escape(chr(10).join(fence_buffer))}\n</code></pre>")
                fence, fence_buffer = None, []
            else:
                fence_buffer.append(line)
            continue
        fence_match = FENCE.match(line)
        if fence_match:
            flush_all()
            fence = fence_match.group(1)
            continue
        if not line.strip():
            flush_paragraph()
            table_blank = bool(table_buffer)
            flush_table()
            if table_blank:
                continue
            # A blank line inside a list block (followed by more list content)
            # keeps the list open; the paragraph buffer is empty here.
            continue
        if TABLE_ROW.match(line) or TABLE_SEPARATOR.match(line):
            flush_paragraph()
            flush_list()
            table_buffer.append(line)
            continue
        if table_buffer:
            flush_table()
        heading = HEADING.match(line)
        if heading:
            flush_all()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{render_inline(heading.group(2), source)}</h{level}>")
            continue
        if HR.match(line):
            flush_all()
            blocks.append("<hr />")
            continue
        bullet = BULLET_ITEM.match(line)
        ordered = ORDERED_ITEM.match(line) if not bullet else None
        continuation = CONTINUATION.match(line) if not bullet and not ordered else None
        if bullet or ordered:
            flush_paragraph()
            marker = "-" if bullet else "1"
            if list_marker not in (None, marker):
                flush_list()
            list_marker = marker
            list_items.append((marker, (bullet or ordered).group(1)))  # type: ignore[union-attr]
            continue
        if continuation and list_marker:
            marker, text_ = list_items[-1]
            list_items[-1] = (marker, f"{text_} {continuation.group(1)}")
            continue
        flush_list()
        if CONTINUATION.match(line) and not paragraph:
            stripped = CONTINUATION.match(line).group(1)  # type: ignore[union-attr]
            blocks.append(f"<pre><code>{html.escape(stripped)}</code></pre>")
            continue
        paragraph.append(line.strip())
    if fence is not None:
        raise AssertionError(f"{source}: unclosed code fence")
    flush_all()
    return "\n".join(blocks)


def page_title(markdown: str, source: Path) -> str:
    titled = front_matter_title(markdown)
    if titled:
        return titled
    for line in strip_front_matter(markdown).splitlines():
        heading = HEADING.match(line)
        if heading:
            return html.escape(heading.group(2).strip("`*"))
    return source.stem


def home_prefix(output_rel: str) -> str:
    depth = len(Path(output_rel).parent.parts)
    return "../" * depth + "index.html"


def render_page(source: Path, markdown: str, output_rel: str) -> str:
    body = render_markdown(strip_front_matter(markdown), source)
    return TEMPLATE.format(
        title=page_title(markdown, source),
        home=home_prefix(output_rel),
        body=body,
    )


def copy_static(output: Path) -> list[str]:
    written: list[str] = []
    for name in ROOT_PAGES:
        source = ROOT / name
        if source.is_file():
            shutil.copyfile(source, output / name)
            written.append(name)
    for directory in STATIC_DIRS:
        target = output / directory.name
        if directory.is_dir():
            shutil.copytree(directory, target, dirs_exist_ok=True)
            written.append(f"{directory.name}/")
    return written


def build(output: Path) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    copy_static(output)

    pages = 0
    for corpus in (QUESTIONS, DOCS):
        for source in sorted(corpus.rglob("*")):
            relative = source.relative_to(ROOT)
            target = output / relative
            if source.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if source.suffix == ".md":
                target = target.with_suffix(".html")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    render_page(source, source.read_text(encoding="utf-8"), relative.as_posix()),
                    encoding="utf-8",
                )
                pages += 1
            else:
                # Static files inside the corpus (for example the research
                # JSON manifests) publish verbatim, as GitHub Pages does.
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
    return {"pages": pages, "output": output}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"build output directory (default: {DEFAULT_OUTPUT.relative_to(ROOT)})",
    )
    args = parser.parse_args(argv)
    result = build(args.output)
    print(f"Rendered {result['pages']} Markdown pages into {result['output']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
