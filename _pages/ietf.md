---
permalink: /ietf/
lang: es
title: "IETF y estándares de Internet"
author_profile: true
---

El grupo contribuye al **IETF** (Internet Engineering Task Force), el organismo abierto que desarrolla los estándares técnicos de Internet, y promueve la participación de la comunidad académica argentina y latinoamericana en ese proceso.

## RFC

{% include ietf-docs.html kind="rfcs" lang="es" %}

## Internet-Drafts

{% include ietf-docs.html kind="drafts" lang="es" %}

## IETF Day en las JAIIO

Ignacio Alvarez-Hamelin es uno de los *chairs* del **IETF Day**, el Taller del Grupo de Trabajo de Ingeniería de Internet / Argentina que FIUBA y SADIO organizan dentro de las Jornadas Argentinas de Informática (JAIIO) desde 2020, junto con Gustavo Mercado (UTN FRM) y Marcela Orbiscay (IANIGLA–CONICET). El taller acerca a investigadores argentinos y latinoamericanos al desarrollo de los estándares de Internet, y Alvarez-Hamelin coeditó sus actas de 2022.

<p class="ietf-links">{%- for k in site.data.ietf.ietf_day.links -%}<a class="btn btn--info" href="{{ k.url }}" rel="noopener">{% if k.label.es %}{{ k.label.es }}{% else %}{{ k.label }}{% endif %}</a>{%- endfor -%}</p>

Más: el [perfil de Ignacio Alvarez-Hamelin en el Datatracker del IETF]({{ site.data.ietf.datatracker_profile }}) y las [publicaciones del grupo sobre estándares IETF](/publications/#topic=standards).
