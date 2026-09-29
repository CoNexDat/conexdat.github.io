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

**IETF Day** is the Internet Engineering Task Force Argentina workshop at the Argentine Computing Conference (JAIIO), organized by FIUBA, SADIO and that working group, with editions since 2020. It brings Argentine and Latin American researchers into the development of Internet standards. Ignacio Alvarez-Hamelin is one of the chairs of the 2026 edition, together with Gustavo Mercado (UTN FRM) and Marcela Orbiscay (IANIGLA–CONICET), and co-edited the proceedings of the 2022 edition.

<p class="ietf-links">{%- for k in site.data.ietf.ietf_day.links -%}<a class="btn btn--info" href="{{ k.url }}" rel="noopener">{% if k.label.en %}{{ k.label.en }}{% else %}{{ k.label }}{% endif %}</a>{%- endfor -%}</p>

More: [Ignacio Alvarez-Hamelin's IETF Datatracker profile]({{ site.data.ietf.datatracker_profile }}) and the [group's publications on IETF standards](/publications/#topic=standards).
