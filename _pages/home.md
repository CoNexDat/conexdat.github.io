---
permalink: /
lang: es
title: "Grupo de Redes Complejas y Comunicación de Datos"
author_profile: true
---

[Departamento de Electrónica](http://electronica.fi.uba.ar) ·
[Facultad de Ingeniería](http://www.fi.uba.ar) ·
[Universidad de Buenos Aires](http://www.uba.ar)

Investigamos en:

- Sistemas Complejos
- Ciencia de Datos
- Internet: protocolos de ruteo, y modelado de su topología
- Tráfico en redes de datos: análisis de sus características estadísticas *(autosimilar)*
- Redes ad-hoc: protocolos de ruteo

## Noticias

{% for item in site.data.news %}
- {% if item.url and item.url != "" %}[**{{ item.title.es }}**]({{ item.url }}){% else %}**{{ item.title.es }}**{% endif %}
{% endfor %}

## Proyectos destacados

<div class="grid__wrapper">
{% for h in site.data.highlights %}
  <div class="archive__item">
    <h3 class="archive__item-title">{{ h.title }}</h3>
    <p>{{ h.blurb.es }}</p>
    {% if h.url and h.url != "" %}<p><a class="btn btn--info" href="{{ h.url }}">Ir al sitio &raquo;</a></p>{% endif %}
  </div>
{% endfor %}
</div>

---

*Grupo de investigación perteneciente al [INTECIN — Instituto de Tecnologías y Ciencias de la Ingeniería "Ing. Hilario Fernández Long"](http://intecin.fi.uba.ar).*
