---
permalink: /
lang: fr
title: "Groupe de Réseaux Complexes et Communication de Données"
author_profile: true
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) ·
[Facultad de Ingeniería](http://www.fi.uba.ar) ·
[Universidad de Buenos Aires](http://www.uba.ar)

Nos axes de recherche :

- Systèmes complexes
- Science des données
- Internet : protocoles de routage et modélisation de la topologie
- Trafic réseau : analyse statistique *(auto-similaire)*
- Réseaux ad-hoc : protocoles de routage

## Actualités

{% for item in site.data.news %}
- {% if item.url and item.url != "" %}[**{{ item.title.fr }}**]({{ item.url }}){% else %}**{{ item.title.fr }}**{% endif %}
{% endfor %}

## Projets phares

<div class="grid__wrapper">
{% for h in site.data.highlights %}
  <div class="archive__item">
    <h3 class="archive__item-title">{{ h.title }}</h3>
    <p>{{ h.blurb.fr }}</p>
    {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Visiter le site &raquo;</a></p>{% endif %}
  </div>
{% endfor %}
</div>

---

*Groupe de recherche affilié à l'[INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
