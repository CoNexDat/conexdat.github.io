---
permalink: /
lang: es
title: "Grupo de Redes Complejas y Comunicación de Datos"
author_profile: true
feature_row:
  - title: "Sistemas Complejos"
    excerpt: "Modelos y propiedades de redes complejas y sistemas multi-agente."
  - title: "Ciencia de Datos"
    excerpt: "Análisis a gran escala de trazas web, sociales y de movilidad."
  - title: "Internet"
    excerpt: "Protocolos de ruteo y modelado de la topología de Internet."
  - title: "Tráfico de red"
    excerpt: "Análisis estadístico *(autosimilar)* de tráfico en redes de datos."
  - title: "Redes ad-hoc"
    excerpt: "Protocolos de ruteo para redes inalámbricas sin infraestructura."
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) · [Facultad de Ingeniería](http://www.fi.uba.ar) · [Universidad de Buenos Aires](http://www.uba.ar)

## Áreas de investigación

{% include feature_row %}

## Noticias

{% include news.html lang="es" %}

## Proyectos destacados

<div class="feature__wrapper">
{% for h in site.data.highlights %}
  <div class="feature__item">
    <div class="archive__item">
      <div class="archive__item-body">
        <h2 class="archive__item-title">{{ h.title }}</h2>
        <div class="archive__item-excerpt"><p>{{ h.blurb.es }}</p></div>
        {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Ir al sitio &raquo;</a></p>{% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>

---

*Grupo de investigación perteneciente al [INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
