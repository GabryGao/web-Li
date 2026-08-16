---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

## Publications

<p class="section-intro">Selected research listed on the academic homepage. (*: Equal Contribution, ^: Corresponding Author)</p>

<input type="text" class="pub-search" id="pubSearch" placeholder="Filter by title, author, venue, or year...">

<div class="selected-pubs" id="pubList">
{% for pub in site.data.publications %}
<article class="pub-card" data-pub-searchable>
  <h4 class="pub-title">
    {% if pub.url %}<a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a>{% else %}{{ pub.title }}{% endif %}
  </h4>
  <p class="pub-meta"><span class="pub-venue">{{ pub.venue }}</span>{% if pub.year %} · {{ pub.year }}{% endif %}</p>
  <p class="pub-authors">{{ pub.authors }}</p>
  <div class="pub-actions">
    {% if pub.url %}<a href="{{ pub.url }}" target="_blank" rel="noopener" class="btn-pill btn-doi">Paper</a>{% endif %}
    {% if pub.website %}<a href="{{ pub.website }}" target="_blank" rel="noopener" class="btn-pill btn-website">Website</a>{% endif %}
    {% if pub.code %}<a href="{{ pub.code }}" target="_blank" rel="noopener" class="btn-pill btn-git">Code</a>{% endif %}
    {% if pub.dataset %}<a href="{{ pub.dataset }}" target="_blank" rel="noopener" class="btn-pill btn-website">Dataset</a>{% endif %}
    {% if pub.weights %}<a href="{{ pub.weights }}" target="_blank" rel="noopener" class="btn-pill btn-website">Weights</a>{% endif %}
  </div>
</article>
{% endfor %}
</div>
