# Publishing the site

`scripts/build_site.py` renders the Markdown corpus into a fully static site
in `build/site/`: root pages (`index.html`, `session.html`, `404.html`),
`assets/`, `config/`, and an `.html` page beside every `questions/` and
`docs/` Markdown source. No server-side code runs anywhere, so the output can
be published by anything that can serve files.

The publishing matrix:

| Target | How | Notes |
| --- | --- | --- |
| GitHub Pages | Push to `main`; the Pages deployment publishes the same layout. | Canonical public site: <https://shapovalovdev.github.io/devops-interview-questions/>. |
| Docker | `docker build -t devops-questions . && docker run -p 8080:8080 devops-questions` | Multi-stage image: `python:3.13-alpine` runs the build, `nginx:alpine` serves `build/site/` unprivileged on port 8080 with a healthcheck. Works on any Docker host, no Python needed there. |
| Any static web server | `python3 scripts/build_site.py`, then point any web server (nginx, Caddy, Apache, S3 + CDN, `python -m http.server`) at `build/site/`. | The output is plain files with relative links; serve the directory as the document root. |

## GitHub Pages (canonical)

The public database lives at
<https://shapovalovdev.github.io/devops-interview-questions/>. Publishing
follows the repository's Pages deployment: the URL layout the own-build
pipeline reproduces (`questions/<theme>/<slug>.html`, `docs/**/*.html`) is the
one Pages serves.

## Docker (any host)

Build and run the image:

```console
$ docker build -t devops-questions .
$ docker run -d -p 8080:8080 --name devops-questions devops-questions
$ curl -fsS http://127.0.0.1:8080/ | grep -o "<title>.*</title>"
<title>DevOps Question Field Manual</title>
```

Details:

- Multi-stage `Dockerfile`: the builder (`python:3.13-alpine`) runs
  `scripts/build_site.py`; the final stage (`nginx:alpine`) serves the build
  as the unprivileged `nginx` user on port 8080.
- The image ships a `HEALTHCHECK` (`wget` against `/`) so orchestrators see
  readiness.
- Cache headers: `assets/` is served with `Cache-Control: public,
  max-age=604800` (assets change rarely but are not fingerprinted, so a week
  rather than `immutable`), and every `.html` page with
  `Cache-Control: no-cache` so rebuilt content reaches visitors immediately.
- `.dockerignore` keeps the build context lean (no `.git`, `.claude`, `build/`,
  caches, `dist/`, `skills/`, `tests/`).

CI (`docker-build.yml`) builds the image on every pull request and push to
`main` and smoke-tests it: `docker run` plus `curl` assertions on `/` and a
Question page. There is no registry push — the workflow uses no secrets.

## Plain static hosting

Run the build once:

```console
$ python3 scripts/build_site.py
Rendered ... Markdown pages into build/site
```

Then serve `build/site/` with whatever you already operate — nginx, Caddy,
Apache, an S3 bucket behind a CDN, or even `python3 -m http.server -d build/site`.
All links inside the generated pages are relative, so the tree works at any
path prefix without rewriting.
