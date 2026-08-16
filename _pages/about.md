---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About

<div class="about-layout">
<div class="section-card">
<div class="pi-card">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ site.photo }}" class="pi-photo" alt="{{ site.name }}" loading="lazy">
<div>
<h3 class="pi-name">{{ site.name }}</h3>
<p style="font-style: italic; color: var(--text-secondary);">{{ site.title }}, The Hong Kong Polytechnic University</p>
<p style="color: var(--text-muted);">{{ site.lab_tagline }}</p>
<div class="pi-links">
{% if site.email %}<a href="mailto:{{ site.email }}" class="icon-link" title="Email"><i class="fa-solid fa-envelope"></i></a>{% endif %}
{% if site.links.email_alt and site.links.email_alt != "" %}<a href="mailto:{{ site.links.email_alt }}" class="icon-link" title="Alternate email"><i class="fa-regular fa-envelope"></i></a>{% endif %}
{% if site.links.google_scholar and site.links.google_scholar != "" %}<a href="{{ site.links.google_scholar }}" class="icon-link" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>{% endif %}
{% if site.links.researchgate and site.links.researchgate != "" %}<a href="{{ site.links.researchgate }}" class="icon-link" title="ResearchGate"><i class="ai ai-researchgate"></i></a>{% endif %}
</div>
</div>
</div>
</div>
</div>

<div class="section-card">
<p>I am an Assistant Professor in the Department of Data Science and Artificial Intelligence (DSAI) at The Hong Kong Polytechnic University (PolyU).</p>
<p>Previously, I was a Research Fellow in the College of Computing and Data Science at NTU, working with Prof. XiaoFeng Wang and Prof. Wei Dong. I completed my Ph.D. with honors at Zhejiang University, co-supervised by Prof. Wenyuan Xu, Prof. Xiaoyu Ji, and Prof. Chen Yan. I obtained my B.Eng. with honors from Zhejiang University.</p>
<p>My research focuses on <strong>AI security and privacy</strong>, especially the security, privacy, and safety of <strong>multimodal LLMs &amp; agentic AI systems</strong>. I study how to secure interactions between agentic AI systems and the real world. My goal is to help AI agents become robust and responsible partners. Robust agents should be resilient to external attacks, and responsible agents should behave in a helpful, harmless, and honest manner. My work has appeared in security and AI/ML venues: IEEE S&amp;P, ACM CCS, USENIX Security, NDSS, NeurIPS, ICML, ICLR, KDD, CVPR, ACL, etc.</p>
</div>

## Education

<div class="section-card">
<ul>
{% for education in site.data.pi[0].education %}
<li>{{ education | replace: "-","&#8211;" }}</li>
{% endfor %}
</ul>
</div>

## Professional Services

<div class="section-card">
<p>I actively contribute to the academic community through program organization and peer review for leading conferences and journals in security, AI, and systems.</p>
<h4>Program Organization</h4>
<ul>
<li>KDD 2025: Tutorial Organizer</li>
</ul>
<h4>Conference</h4>
<ul>
<li>Area Chair: ICLR’27, NeurIPS, ICLR’26</li>
<li>PC Member: USENIX Security’27, AsiaCCS’27, CCS’26, SaTML’26, AAAI’26</li>
<li>Reviewer: ICML’26, CVPR’26</li>
<li>External Reviewer: IEEE S&amp;P’19, ‘20; CCS’21, ‘22, ‘23, ‘24; USENIX Security’19, ‘20, ‘21, ‘24; NDSS’20, ‘22, ‘23, ‘24</li>
</ul>
<h4>Journal</h4>
<ul>
<li>Reviewer: IEEE TIFS, TDSC, TMC, TNNLS, TOSEM, IoT-J, TOIT, TCCN; ACM TOPS; IJCV.</li>
</ul>
</div>

## Honors and Awards

<div class="section-card">
<ul>
{% for award in site.data.awards %}
<li>{{ award.name }}</li>
{% endfor %}
</ul>
</div>
