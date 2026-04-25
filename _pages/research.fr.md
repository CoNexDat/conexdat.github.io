---
permalink: /research/
lang: fr
title: "Axes de recherche"
author_profile: true
---

Nous travaillons sur cinq grands axes, tous reliés par la **théorie des
réseaux complexes**, la **science des données** et la **mesure
empirique** des systèmes de communication à grande échelle.

<div class="feature__wrapper">
{% for a in site.data.research_areas %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title"><i class="{{ a.icon }}"></i> {{ a.title[page.lang] }}</h2>
        <div class="archive__item-excerpt">{{ a.excerpt[page.lang] | markdownify }}</div>
        <p><a class="btn btn--info" href="/research/{{ a.slug }}/">En savoir plus &raquo;</a></p>
      </div>
    </div>
  </div>
{% endfor %}
</div>
