---
permalink: /research/
lang: en
title: "Research areas"
author_profile: true
---

We work in five broad areas, all bridged by **complex-network theory**,
**data science**, and the **empirical measurement** of large-scale
communication systems.

<div class="feature__wrapper">
{% for a in site.data.research_areas %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title"><i class="{{ a.icon }}"></i> {{ a.title[page.lang] }}</h2>
        <div class="archive__item-excerpt">{{ a.excerpt[page.lang] | markdownify }}</div>
        <p><a class="btn btn--info" href="/research/{{ a.slug }}/">Learn more &raquo;</a></p>
      </div>
    </div>
  </div>
{% endfor %}
</div>
