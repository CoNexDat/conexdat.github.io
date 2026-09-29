---
permalink: /ietf/
lang: fr
title: "IETF et normes d'Internet"
author_profile: true
---

Le groupe contribue à l'**IETF** (Internet Engineering Task Force), l'organisme ouvert qui élabore les normes techniques d'Internet, et promeut la participation de la communauté académique argentine et latino-américaine à ce processus.

## RFC

{% include ietf-docs.html kind="rfcs" lang="fr" %}

## Internet-Drafts

{% include ietf-docs.html kind="drafts" lang="fr" %}

## IETF Day aux JAIIO

L'**IETF Day** est l'atelier du groupe de travail argentin de l'Internet Engineering Task Force au sein des Journées argentines d'informatique (JAIIO), organisé par la FIUBA, la SADIO et ce groupe de travail, avec des éditions depuis 2020. Il rapproche les chercheurs argentins et latino-américains de l'élaboration des normes d'Internet. Ignacio Alvarez-Hamelin est l'un des coprésidents de l'édition 2026, avec Gustavo Mercado (UTN FRM) et Marcela Orbiscay (IANIGLA–CONICET), et a coédité les actes de l'édition 2022.

<p class="ietf-links">{%- for k in site.data.ietf.ietf_day.links -%}<a class="btn btn--info" href="{{ k.url }}" rel="noopener">{% if k.label.fr %}{{ k.label.fr }}{% else %}{{ k.label }}{% endif %}</a>{%- endfor -%}</p>

Plus : le [profil d'Ignacio Alvarez-Hamelin sur le Datatracker de l'IETF]({{ site.data.ietf.datatracker_profile }}) et les [publications du groupe sur les normes IETF](/publications/#topic=standards).
