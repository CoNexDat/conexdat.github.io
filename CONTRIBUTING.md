# Contributing to the CoNexDat website

Thanks for helping keep <https://conexdat.github.io> accurate. This page is the
public face of the group, so small, well-scoped changes are preferred.

## Ground rules

- `main` is protected: every change lands through a pull request, and the
  **Build site** check must pass before merging. Pushes to `main` deploy
  automatically, so a broken build never reaches production but a wrong link
  does — please preview locally first.
- The site is trilingual (ES / EN / FR). Every content change must keep the
  three languages in lock-step: either edit the `es:` / `en:` / `fr:` columns
  of the same YAML entry, or edit the `.md`, `.en.md` and `.fr.md` page
  together.
- English text uses **American English** (US spelling: `color`, `behavior`,
  `modeling`, `visualize`, `toward`), and so do code comments and names. Spanish
  and French stay in correct Spanish and French. Published paper titles are kept
  as published.
- The site publishes **no e-mail addresses**. The contact page points to the group
  director and to the [CoNexDat GitHub organization](https://github.com/CoNexDat).
- Do not link into the legacy `cnet.fi.uba.ar` server: unknown paths there quietly
  serve its old home page. See AGENTS.md for the few pages that still exist.
- Be kind: see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## What goes where

| I want to…                         | Edit                                   |
|------------------------------------|----------------------------------------|
| Add / update a member              | `_data/members.yml`                    |
| Add a news item                    | `_news/YYYY-MM-DD-slug.md` (+ `.en.md`, `.fr.md`) |
| Add a publication                  | `_bibliography/conexdat.bib` (+ `topics`) |
| Add / rename a publication topic   | `_data/publication_topics.yml`         |
| Add / update a funded project      | `_data/projects.yml`                   |
| Change a home-page project card    | `_data/highlights.yml`                 |
| Change a research area             | `_data/research_areas.yml`             |
| Add a thesis                       | `_data/theses.yml` (+ PDF under `files/theses/`) |
| Change navigation                  | `_data/navigation.yml`                 |
| Change a static page               | `_pages/<page>.md`, `.en.md`, `.fr.md` |

`_data/*.yml` files are the single source of truth; the `_includes/*.html`
partials render them. Do not hand-edit anything under `_site/`.

### Publications

Drop a BibTeX entry into `_bibliography/conexdat.bib` and tag it with one or
more topics, using the ids listed in `_data/publication_topics.yml`:

```bibtex
  topics = {internet-measurement, latam}
```

Topics appear as chips above the list and on every entry, and filter the list
when clicked (deep link: `/publications/#topic=latam`). Add a new topic to the
YAML file, in all three languages, only when no existing one fits.

Other optional fields that the entry template understands: `abstract`, `doi`,
`eprint` + `archiveprefix = {arXiv}`, `pdf` (file under `assets/pdf/` or a
URL), `code`, `slides`, `poster`, `website`, `bibtex_show = {true}`.

Author surnames listed under `cnet.highlighted_authors` in `_config.yml` are
emphasized automatically.

### Members

Each entry carries a `category` (`current`, `external`, `former-inhouse`,
`past-collaborator`, `alumni`) and, for alumni, a `tier`. Add an optional
`homepage` and drop a `images/people/<slug>.jpg` photo (the slug is the
kebab-cased name, or an explicit `slug:` key).

## Local preview

Requires Ruby 3.3 (Homebrew: `brew install ruby@3.3`) and Bundler.

```sh
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml
```

Then open <http://localhost:4000/>, `/en/` and `/fr/`. The dev config is
required: without it the pages link CSS and assets to the production URL and
local style changes silently do not show.

The warnings `Error reading file _layouts/single` are a known, harmless
jekyll-polyglot quirk.

## Pull-request checklist

- [ ] All three languages updated
- [ ] `bundle exec jekyll build` succeeds locally
- [ ] New external links open the page you expect (not a redirect to a home page)
- [ ] Screenshots attached for visual changes
