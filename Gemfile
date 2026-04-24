source 'https://rubygems.org'

# Jekyll itself + the build-time plugins academicpages relies on.
# We deliberately do NOT use the `github-pages` gem because GitHub Pages'
# auto-build sandbox does not whitelist jekyll-polyglot or jekyll-scholar;
# the site is built and deployed via GitHub Actions instead.
gem 'jekyll', '~> 4.3'

group :jekyll_plugins do
  gem 'jekyll-feed'
  gem 'jekyll-sitemap'
  gem 'jekyll-redirect-from'
  gem 'jekyll-polyglot'
  gem 'jekyll-scholar'
end

gem 'webrick', '~> 1.8'
gem 'csv'
gem 'base64'
