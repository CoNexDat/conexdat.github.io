---
permalink: /en/
lang: en
title: "Complex Networks and Data Communication Group"
author_profile: true
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) ·
[Facultad de Ingeniería](http://www.fi.uba.ar) ·
[Universidad de Buenos Aires](http://www.uba.ar)

Our research areas:

- Complex Systems
- Data Science
- Internet: routing protocols and topology modelling
- Network traffic: statistical analysis *(self-similar)*
- Ad-hoc networks: routing protocols

## News

{% for item in site.data.news %}
- {% if item.url and item.url != "" %}[**{{ item.title.en }}**]({{ item.url }}){% else %}**{{ item.title.en }}**{% endif %}
{% endfor %}

## Featured projects

<div class="grid__wrapper">
{% for h in site.data.highlights %}
  <div class="archive__item">
    <h3 class="archive__item-title">{{ h.title }}</h3>
    <p>{{ h.blurb.en }}</p>
    {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Visit site &raquo;</a></p>{% endif %}
  </div>
{% endfor %}
</div>

---

*Research group within [INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
