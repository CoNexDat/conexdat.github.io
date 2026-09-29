# AGENTS.md — CoNexDat website

Instructions for AI coding agents (Claude Code, Copilot, Codex, Cursor, ...) working in
this repository. `CLAUDE.md` includes this file. Humans: see `CONTRIBUTING.md`.

## What this project is

The public website of CoNexDat, the Complex Networks and Data Communication Group at
the School of Engineering of the University of Buenos Aires (FIUBA), directed by
J. Ignacio Alvarez-Hamelin. It is a static Jekyll 4 site built on the academicpages
template, trilingual (Spanish default, English, French) through jekyll-polyglot, with
publications rendered from BibTeX by jekyll-scholar. GitHub Actions builds it and
publishes `_site/` to the `gh-pages` branch, served at <https://conexdat.github.io>.
It replaces the legacy site at `cnet.fi.uba.ar`, which is being retired.

## Layout

```
_config.yml                 site, polyglot and scholar settings; cnet.highlighted_authors
_config.dev.yml             local overrides (url: http://localhost:4000); required for previews
_pages/<page>.md            Spanish page; <page>.en.md and <page>.fr.md are the translations
_data/
  members.yml               people, by category (current, external, former-inhouse, ...)
  projects.yml              funded projects
  research_areas.yml        research areas: home cards + /research/<slug>/ pages
  highlights.yml            home-page project cards
  publication_topics.yml    publication topics (labels), trilingual
  theses.yml, navigation.yml, ui-text.yml
_news/                      one file per news item and language (inline, no pages)
_bibliography/conexdat.bib  THE publication list (other .bib files are unused sources)
_layouts/bib_entry.html     how one publication renders (buttons, highlighting, topic chips)
_includes/                  masthead (language switcher), people/projects/theses lists,
                            publications-filter.html, research-area.html
assets/js/publications.js   search / topic / person filter on /publications/
_sass/_conexdat.scss        all site-specific styles (colors, cards, chips, dark mode)
.github/workflows/          build.yml (PR check "Build site"), deploy.yml (push to main)
```

## Commands

```bash
export PATH="/usr/local/opt/ruby@3.3/bin:$PATH"   # macOS/Homebrew; Ruby 3.3 only
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml   # preview
JEKYLL_ENV=production bundle exec jekyll build                              # what CI runs
```

Ruby 3.3 is required: the system Ruby is too old for Bundler 4, and Ruby 4 cannot
compile the `sassc` native gem. A full build takes about 30 seconds. The repeated
"Error reading file _layouts/single" warnings are a harmless polyglot quirk. To preview
a finished build without Jekyll, serve `_site/` on **port 4000**; the dev config
hard-codes that origin for CSS and assets.

## Conventions

- **American English everywhere** (mandatory) for English text: the `.en.md` pages, the
  `en:` values in `_data/`, English news, this file, README, CONTRIBUTING, commit
  messages, PR descriptions, and every code comment, identifier, CSS class and
  JavaScript name (`color`, `gray`, `center`, `behavior`, `modeling`, `analyze`,
  `visualize`, `normalize`, `organization`, `toward`, `inquiry`). Spanish and French
  content stays in correct Spanish and French. Exceptions: proper names and published
  paper titles in the bibliography are kept exactly as published.
- **Three languages in lock-step.** Every content change updates Spanish, English and
  French together: the three `.md` files of a page, or the `es:` / `en:` / `fr:` keys of
  the same YAML entry. Never ship a page or entry in one language only.
- **No e-mail addresses anywhere on the site** (group decision, September 2026). The
  contact page points to the director and to <https://github.com/CoNexDat>. Do not add
  `mailto:` links, and keep `author.email` in `_config.yml` empty.
- **Do not link into `cnet.fi.uba.ar`.** Unknown paths there silently serve the legacy
  home page, so a link can look alive and still be wrong. Pages that still exist there
  and may be linked: `netscix23/`, `SnailVis/`, `PIT/…`, `PaD/`. Otherwise use the
  project's new home (TiX: <https://github.com/TiX-measurements>, LaNet-vi:
  <https://github.com/CoNexDat/LaNet-vi>, TMA2018: <https://netcores.fi.uba.ar/>) or a
  Wayback Machine snapshot. Check with `grep -rn cnet.fi.uba.ar _data _pages _news`.
- **Verify every new external link** with `curl -sIL` and read where it lands: a 200 on
  a home page, a sign-in wall or a parked domain is a broken link.
- **Publications**: add entries to `_bibliography/conexdat.bib` with a
  `topics = {id1, id2}` field using ids from `_data/publication_topics.yml` (add a new
  topic there, in three languages, only when no existing one fits). Two 1990s
  instrumentation papers (`onditas96`, `Thermog95`) are deliberately untagged: no topic
  fits them, and they only disappear while a topic filter is active. Prefer a bare DOI
  (`10.xxxx/…`), `eprint` + `archiveprefix = {arXiv}` for preprints, and check the key is
  not already present: the group's own exports contain duplicates.
- Internal links are written without language prefix (`/projects/`); polyglot adds
  `/en/` or `/fr/`. Do not hard-code `https://conexdat.github.io/...` in content.
- Commit messages and PR descriptions in American English, imperative subject line.

## Things that are easy to get wrong

- **Language switcher.** Polyglot rewrites every `href="/…"` on EN and FR pages into the
  current language, which breaks hand-written ES | EN | FR links. The masthead writes them
  as `ferh="/en/…"`, which polyglot turns back into `href` untouched. Do not rename the
  attribute. The `Build site` workflow greps the output for the expected hrefs.
- **No `//` comments inside inline `<script>` blocks.** Production builds compress HTML
  onto one line, so a `//` comment swallows the rest of the script. That silently broke
  the previous language switcher. Use `/* … */` or move the code to `assets/js/`.
- `assets/js/main.min.js` is a prebuilt file; `assets/js/_main.js` and `plugins/` are
  excluded from the build, so editing them changes nothing.
- `jekyll-sass-converter` is pinned to 2.x on purpose: the academicpages partials do not
  compile under dart-sass (3.x). Dependabot is told to ignore that major version.
- Jekyll-scholar exposes custom BibTeX fields (`topics`, `pdf`, `code`, ...) to
  `_layouts/bib_entry.html`; the same template renders the short paper lists on research
  area pages, so keep it free of page-specific assumptions.

## Pull request workflow (required)

`main` is protected by the "Protect main" ruleset: no direct pushes, no force-push or
deletion, pull request required, and the `Build site` check must pass. Repository
admins can bypass; do not use the bypass unless a maintainer explicitly asks for it in
an emergency, and say so in the PR description.

1. Branch from `main` (`feat/…`, `fix/…`, `content/…`, `docs/…`, `chore/…`), commit,
   push, open the PR with `gh pr create`, and fill the PR template checklist honestly.
2. Build locally before pushing. For visual changes, check ES, EN and FR in the browser,
   in light and dark mode, and at phone width.
3. Wait for `Build site`. If it is red, read the log (`gh run view <id> --log-failed`),
   fix, push, and wait again. Never weaken the check to get green.
4. Get a review before merging (see CLAUDE.md for how Claude Code sessions do this).
5. Merge with `gh pr merge <n> --squash --delete-branch`. Merging deploys to production
   within a few minutes; confirm the live page afterwards.
