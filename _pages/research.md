---
permalink: /research/
lang: es
title: "Áreas de investigación"
author_profile: true
---

Trabajamos en cinco grandes áreas, todas atravesadas por la teoría de
**redes complejas**, la **ciencia de datos** y la **medición empírica**
de sistemas de comunicación a gran escala.

<div class="feature__wrapper">
{% for a in site.data.research_areas %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title"><i class="{{ a.icon }}"></i> {{ a.title[page.lang] }}</h2>
        <div class="archive__item-excerpt">{{ a.excerpt[page.lang] | markdownify }}</div>
        <p><a class="btn btn--info" href="/research/{{ a.slug }}/">Saber más &raquo;</a></p>
      </div>
    </div>
  </div>
{% endfor %}
</div>
