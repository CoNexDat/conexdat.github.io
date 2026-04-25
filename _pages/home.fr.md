---
permalink: /
lang: fr
title: "Groupe de Réseaux Complexes et Communication de Données"
author_profile: true
---

<div class="affiliations">
  <div class="affiliations__label">Affiliations institutionnelles</div>
  <ul class="affiliations__list">
    <li><a href="http://electronica.fi.uba.ar">Departamento de Electrónica</a></li>
    <li><a href="http://www.fi.uba.ar">Facultad de Ingeniería</a></li>
    <li><a href="http://www.uba.ar">Universidad de Buenos Aires</a></li>
    <li><a href="https://www.conicet.gov.ar">CONICET</a></li>
  </ul>
</div>

## Axes de recherche

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

## Actualités

{% include news.html lang="fr" %}

## Projets phares

<div class="feature__wrapper">
{% for h in site.data.highlights %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title">{{ h.title }}</h2>
        <div class="archive__item-excerpt"><p>{{ h.blurb.fr }}</p></div>
        {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Visiter le site &raquo;</a></p>{% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>

---

*Groupe de recherche affilié à l'[INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
