---
permalink: /
lang: fr
title: "Groupe de Réseaux Complexes et Communication de Données"
author_profile: true
feature_row:
  - title: '<i class="fas fa-project-diagram"></i> Systèmes complexes'
    excerpt: "Étude des réseaux complexes par décomposition en *k-cœurs* et détection de communautés. Théorie des graphes et modèles de propagation appliqués aux réseaux biologiques, sociaux et technologiques."
  - title: '<i class="fas fa-database"></i> Science des données'
    excerpt: "Analyse à grande échelle de traces Twitter, de données électorales et de registres mobiles (CDR). Inférence de la mobilité humaine, de la demande de contenu et de la dynamique des communautés en ligne."
  - title: '<i class="fas fa-globe"></i> Internet'
    excerpt: "Tomographie d'Internet et modélisation de sa topologie (BGP, IXP, niveau AS). Conception de protocoles de routage dont les tables croissent sous-linéairement avec la taille du réseau."
  - title: '<i class="fas fa-chart-line"></i> Trafic réseau'
    excerpt: "Caractérisation statistique *auto-similaire* du trafic résidentiel. Sondages continus à faible charge pour l'évaluation de la QoS et la détection du trafic IXP/CDN."
  - title: '<i class="fas fa-broadcast-tower"></i> Réseaux ad-hoc'
    excerpt: "Protocoles de routage pour réseaux sans-fil sans infrastructure. Nous avons développé *ANTop* (algorithme bio-inspiré) et l'avons évalué sur le simulateur QUENAS."
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
