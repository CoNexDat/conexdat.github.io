---
permalink: /
lang: es
title: "Grupo de Redes Complejas y Comunicación de Datos"
author_profile: true
feature_row:
  - title: '<i class="fas fa-project-diagram"></i> Sistemas Complejos'
    excerpt: "Estudiamos redes complejas con métodos como descomposición en *k-núcleos* y detección de comunidades. Aplicamos teoría de grafos y modelos de propagación a redes biológicas, sociales y tecnológicas."
  - title: '<i class="fas fa-database"></i> Ciencia de Datos'
    excerpt: "Análisis a gran escala de trazas de Twitter, datos electorales y registros móviles (CDR). Inferimos movilidad humana, demanda de contenidos y dinámica de comunidades online."
  - title: '<i class="fas fa-globe"></i> Internet'
    excerpt: "Tomografía de Internet y modelado de su topología (BGP, IXPs, AS-level). Diseñamos protocolos de ruteo cuyas tablas crecen sub-linealmente con el tamaño de la red."
  - title: '<i class="fas fa-chart-line"></i> Tráfico de red'
    excerpt: "Caracterización estadística *autosimilar* del tráfico residencial. Mediciones continuas de baja carga para evaluar QoS y detectar tráfico de IXPs y CDNs."
  - title: '<i class="fas fa-broadcast-tower"></i> Redes ad-hoc'
    excerpt: "Protocolos de ruteo para redes inalámbricas sin infraestructura. Desarrollamos *ANTop* (algoritmo bio-inspirado) y lo evaluamos sobre el simulador QUENAS."
---

<div class="affiliations">
  <div class="affiliations__label">Pertenencia institucional</div>
  <ul class="affiliations__list">
    <li><a href="http://electronica.fi.uba.ar">Departamento de Electrónica</a></li>
    <li><a href="http://www.fi.uba.ar">Facultad de Ingeniería</a></li>
    <li><a href="http://www.uba.ar">Universidad de Buenos Aires</a></li>
    <li><a href="https://www.conicet.gov.ar">CONICET</a></li>
  </ul>
</div>

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
