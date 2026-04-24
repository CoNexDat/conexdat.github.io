---
permalink: /
lang: fr
title: "Groupe de Réseaux Complexes et Communication de Données"
author_profile: true
feature_row:
  - title: "Systèmes complexes"
    excerpt: "Modèles et propriétés des réseaux complexes et systèmes multi-agents."
  - title: "Science des données"
    excerpt: "Analyse à grande échelle de traces web, sociales et de mobilité."
  - title: "Internet"
    excerpt: "Protocoles de routage et modélisation de la topologie d'Internet."
  - title: "Trafic réseau"
    excerpt: "Analyse statistique *(auto-similaire)* du trafic des réseaux de données."
  - title: "Réseaux ad-hoc"
    excerpt: "Protocoles de routage pour réseaux sans-fil sans infrastructure."
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) · [Facultad de Ingeniería](http://www.fi.uba.ar) · [Universidad de Buenos Aires](http://www.uba.ar)

## Axes de recherche

{% include feature_row %}

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
