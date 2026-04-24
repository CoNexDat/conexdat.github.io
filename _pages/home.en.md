---
permalink: /
lang: en
title: "Complex Networks and Data Communication Group"
author_profile: true
feature_row:
  - title: '<i class="fas fa-project-diagram"></i> Complex Systems'
    excerpt: "We study complex networks via *k-core* decomposition and community detection. Graph theory and propagation models applied to biological, social and technological networks."
  - title: '<i class="fas fa-database"></i> Data Science'
    excerpt: "Large-scale analysis of Twitter traces, electoral data, and Call Detail Records (CDR). We infer human mobility, content demand, and online community dynamics."
  - title: '<i class="fas fa-globe"></i> Internet'
    excerpt: "Internet tomography and topology modelling (BGP, IXPs, AS-level). We design routing protocols whose tables grow sub-linearly with network size."
  - title: '<i class="fas fa-chart-line"></i> Network traffic'
    excerpt: "Statistical *self-similar* characterization of residential traffic. Continuous low-load probing for QoS assessment and IXP/CDN traffic detection."
  - title: '<i class="fas fa-broadcast-tower"></i> Ad-hoc networks'
    excerpt: "Routing protocols for infrastructure-less wireless networks. We developed *ANTop* (bio-inspired algorithm) and evaluated it on the QUENAS simulator."
---

<div class="affiliations">
  <div class="affiliations__label">Affiliations</div>
  <ul class="affiliations__list">
    <li><a href="http://electronica.fi.uba.ar">Departamento de Electrónica</a></li>
    <li><a href="http://www.fi.uba.ar">Facultad de Ingeniería</a></li>
    <li><a href="http://www.uba.ar">Universidad de Buenos Aires</a></li>
    <li><a href="https://www.conicet.gov.ar">CONICET</a></li>
  </ul>
</div>

## Research areas

{% include feature_row %}

## News

{% include news.html lang="en" %}

## Featured projects

<div class="feature__wrapper">
{% for h in site.data.highlights %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title">{{ h.title }}</h2>
        <div class="archive__item-excerpt"><p>{{ h.blurb.en }}</p></div>
        {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Visit site &raquo;</a></p>{% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>

---

*Research group within [INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
