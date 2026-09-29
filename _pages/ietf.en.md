---
permalink: /ietf/
lang: en
title: "IETF and Internet standards"
author_profile: true
---

The group contributes to the **IETF** (Internet Engineering Task Force), the open body that develops the technical standards of the Internet, and promotes the participation of the Argentine and Latin American academic community in that process.

## RFC

{% include ietf-docs.html kind="rfcs" lang="en" %}

## Internet-Drafts

{% include ietf-docs.html kind="drafts" lang="en" %}

## IETF Day at JAIIO

Ignacio Alvarez-Hamelin is one of the chairs of **IETF Day**, the Internet Engineering Task Force Argentina workshop that FIUBA and SADIO have organized within the Argentine Computing Conference (JAIIO) since 2020, together with Gustavo Mercado (UTN FRM) and Marcela Orbiscay (IANIGLA–CONICET). The workshop brings Argentine and Latin American researchers into the development of Internet standards, and Alvarez-Hamelin co-edited its 2022 proceedings.

<p class="ietf-links">{%- for k in site.data.ietf.ietf_day.links -%}<a class="btn btn--info" href="{{ k.url }}" rel="noopener">{% if k.label.en %}{{ k.label.en }}{% else %}{{ k.label }}{% endif %}</a>{%- endfor -%}</p>

More: [Ignacio Alvarez-Hamelin's IETF Datatracker profile]({{ site.data.ietf.datatracker_profile }}) and the [group's publications on IETF standards](/publications/#topic=standards).
