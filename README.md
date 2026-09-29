# CoNexDat website

Static site for the **Grupo de Redes Complejas y Comunicación de Datos** at
FIUBA — built with [Jekyll](https://jekyllrb.com) on top of the
[academicpages](https://github.com/academicpages/academicpages.github.io)
template, with [jekyll-polyglot](https://github.com/untra/polyglot) for
ES/EN/FR and [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar)
for BibTeX-driven publications.

Published at https://conexdat.github.io/. The legacy site at
`https://cnet.fi.uba.ar/` is being retired: unknown paths there land on its
old home page, so this site must not link into it except for pages that
still exist (NetSci-X 2023, SnailVis, the PIT/IXP reports, PaD) or through
Wayback Machine snapshots. Re-check with `grep -rn cnet.fi.uba.ar _data _pages _news`.

## Local development

Requires Ruby 3.3 (with Bundler). On macOS with Homebrew:

```sh
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml
```

The dev config is mandatory for previews: without it `head.html` links CSS and
assets to the production URL and local style changes silently do not show.

Open <http://localhost:4000/>, <http://localhost:4000/en/>,
<http://localhost:4000/fr/>.

## Layout

- `_config.yml` — site config + polyglot + scholar
- `_pages/<page>.md` / `<page>.en.md` / `<page>.fr.md` — one file per language
- `_data/members.yml` — group members (current / external / alumni), trilingual
- `_data/projects.yml` — research projects, trilingual
- `_data/news.yml`, `_data/highlights.yml` — home-page panels
- `_data/navigation.yml` — top nav with localized labels
- `_bibliography/conexdat.bib` — publications (rendered by jekyll-scholar),
  each tagged with `topics = {…}`
- `_data/publication_topics.yml` — trilingual publication topics (labels)
- `_data/software.yml`, `_data/ietf.yml` — the Software and IETF pages
- `_includes/people-list.html`, `projects-list.html` — shared layouts
- `_includes/publications-filter.html` + `assets/js/publications.js` — search,
  topic and person filters on `/publications/`
- `_includes/masthead.html`, `head.html` — overridden for i18n + favicon
- `images/` — logo, favicon, profile picture

## Deploy

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the site
under Ruby 3.3 and publishes `_site/` to the `gh-pages` branch via
[peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages).
GitHub Pages is configured to serve from `gh-pages`.

The `github-pages` gem is **not** used because GitHub's auto-build sandbox
does not whitelist `jekyll-polyglot` or `jekyll-scholar`.

## Contributing and governance

- `main` is protected by a repository ruleset: changes land through pull
  requests, the **Build site** check (`.github/workflows/build.yml`) must pass,
  and force-pushes / deletion are blocked. Repository admins can bypass in an
  emergency.
- Coding agents (and humans who want the details) read [AGENTS.md](AGENTS.md):
  American English, the three-language rule, no e-mail addresses, no links into
  the legacy server.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for what-goes-where, the local
  preview recipe and the PR checklist; [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
  and [SECURITY.md](SECURITY.md) for conduct and vulnerability reporting.
- Dependabot proposes weekly, grouped updates for the Ruby gems and the Actions
  (with a 7-day cooldown). Actions are pinned to commit SHAs.
- `security.yml` audits `Gemfile.lock` with bundler-audit and the workflows with
  zizmor, on changes and weekly. CodeQL, secret scanning and push protection are
  enabled in the repository settings.
- `link-check.yml` checks every link weekly and keeps a single "broken-link" issue
  open until they pass; the PR build checks internal links on every change.
- Every PR gets an independent review that follows `.github/REVIEW.md`.

### Language switcher gotcha

jekyll-polyglot rewrites every `href="/…"` in a non-default-language page into
the current language root, which breaks a hand-written ES | EN | FR switcher.
The masthead therefore writes the links as `ferh="/en/…"`; polyglot turns
`ferh` back into `href` without relativizing it. Do not "fix" the attribute
name, and do not put `//` line comments inside inline `<script>` blocks: the
production HTML compressor collapses them onto one line and comments out the
whole script (that is what silently disabled the previous JS-based switcher).

## Migrating new content

The `_data/` files are the single source of truth. To add a member, project,
or news item, edit the corresponding YAML — the translation columns
(`es: …`, `en: …`, `fr: …`) keep all three languages in lock-step. To add a
publication, drop a BibTeX entry into the appropriate `_bibliography/*.bib`.
