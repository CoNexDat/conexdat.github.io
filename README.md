# CoNexDat website

Static site for the **Grupo de Redes Complejas y Comunicación de Datos** at
FIUBA — built with [Jekyll](https://jekyllrb.com) on top of the
[academicpages](https://github.com/academicpages/academicpages.github.io)
template, with [jekyll-polyglot](https://github.com/untra/polyglot) for
ES/EN/FR and [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar)
for BibTeX-driven publications.

Published at https://conexdat.github.io/. The legacy URL
`https://cnet.fi.uba.ar/` 302-redirects here; the FIUBA Apache box stays
online only for serving bulkier datasets.

## Local development

Requires Ruby 3.2+ (with Bundler).

```sh
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml
```

Open <http://localhost:4000/>, <http://localhost:4000/en/>,
<http://localhost:4000/fr/>.

## Layout

- `_config.yml` — site config + polyglot + scholar
- `_pages/<page>.md` / `<page>.en.md` / `<page>.fr.md` — one file per language
- `_data/members.yml` — group members (current / external / alumni), trilingual
- `_data/projects.yml` — research projects, trilingual
- `_data/news.yml`, `_data/highlights.yml` — home-page panels
- `_data/navigation.yml` — top nav with localized labels
- `_bibliography/*.bib` — publications (rendered by jekyll-scholar)
- `_includes/people-list.html`, `projects-list.html` — shared layouts
- `_includes/masthead.html`, `head.html` — overridden for i18n + favicon
- `images/` — logo, favicon, profile picture

## Deploy

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the site
under Ruby 3.2 and publishes `_site/` to the `gh-pages` branch via
[peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages).
GitHub Pages is configured to serve from `gh-pages`.

The `github-pages` gem is **not** used because GitHub's auto-build sandbox
does not whitelist `jekyll-polyglot` or `jekyll-scholar`.

## Migrating new content

The `_data/` files are the single source of truth. To add a member, project,
or news item, edit the corresponding YAML — the translation columns
(`es: …`, `en: …`, `fr: …`) keep all three languages in lock-step. To add a
publication, drop a BibTeX entry into the appropriate `_bibliography/*.bib`.
