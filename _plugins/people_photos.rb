# frozen_string_literal: true

# Exposes the slugs of the photos in images/people/ as site.data["people_photos"],
# so _includes/people-list.html can decide at build time whether a member has a
# photo. site.static_files cannot be used for this: jekyll-polyglot drops the
# files of `exclude_from_localization` folders (images/ is one) while it renders
# the EN and FR pages, so every lookup there would miss.
Jekyll::Hooks.register :site, :post_read do |site|
  dir = File.join(site.source, "images", "people")
  site.data["people_photos"] = Dir.glob(File.join(dir, "*.jpg")).map { |f| File.basename(f, ".jpg") }.sort
end
