---
permalink: /
lang: en
title: "Complex Networks and Data Communication Group"
author_profile: true
feature_row:
  - title: "Complex Systems"
    excerpt: "Models and properties of complex networks and multi-agent systems."
  - title: "Data Science"
    excerpt: "Large-scale analysis of web, social, and mobility traces."
  - title: "Internet"
    excerpt: "Routing protocols and topology modelling of the Internet."
  - title: "Network traffic"
    excerpt: "Statistical *(self-similar)* analysis of data-network traffic."
  - title: "Ad-hoc networks"
    excerpt: "Routing protocols for infrastructure-less wireless networks."
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) · [Facultad de Ingeniería](http://www.fi.uba.ar) · [Universidad de Buenos Aires](http://www.uba.ar)

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
