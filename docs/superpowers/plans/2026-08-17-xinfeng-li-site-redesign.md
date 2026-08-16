# Xinfeng Li Academic Website Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the existing Jekyll academic site as a polished, responsive AI-safety research homepage using only source-backed Xinfeng Li content.

**Architecture:** Preserve Jekyll, Liquid, Sass, Bootstrap, `jekyll-scholar`, and the existing GitHub Pages deployment. Normalize factual copy into `_data/profile.yml`, keep publications and news in their existing data files, render those records through focused layouts, and verify both source and generated output with a repository script before visual QA.

**Tech Stack:** Jekyll 4.3.3, Liquid, Sass Embedded, Bootstrap 5.3.3, vanilla JavaScript/esbuild, Ruby verification script, GitHub Pages.

## Global Constraints

- `https://letterligo.netlify.app/` is the primary factual source.
- `https://scholar.google.com/citations?user=JC_UWyoAAAAJ&hl=en` is a secondary publication-verification source; do not publish unverified citation metrics.
- Preserve the current Jekyll build and GitHub Pages deployment.
- Do not copy source code or assets from the unlicensed `PRLab-NJU-Si/PRLab-Website` repository.
- Do not invent people, lab names, grants, funders, courses, awards, publications, links, or citation counts.
- Hide unsupported optional sections; use `Pending confirmation` only when an empty structural field would otherwise mislead.
- Never edit `_site` directly.
- Stop after a verified local preview; do not push or deploy without a later explicit request.

---

## File Structure

- `_data/profile.yml`: source-backed identity, biography, research directions, recruiting copy, services summary, and source URLs.
- `_data/news.yml`: dated news records with plain text plus explicit link arrays.
- `_data/publications.yml`: normalized publication metadata and verified resource links.
- `_data/awards.yml`, `_data/pi.yml`: source-backed honors and education/career facts.
- `_includes/header.html`, `_includes/footer.html`, `_includes/sidebar.html`: global navigation, footer, and profile identity.
- `_pages/home.html`: landing-page composition only; no long factual copy duplicated inline.
- `_pages/research.html`, `_pages/publications.html`, `_pages/news.html`, `_pages/team.html`: focused content pages rendered from data.
- `_sass/base/*`: design tokens and typography.
- `_sass/components/*`: reusable navigation, cards, chips, profile, publication, and footer styles.
- `_sass/layouts/*`: page-specific responsive layout.
- `assets/js/site.js`: mobile navigation, search, publication filtering, and theme behavior.
- `scripts/verify_site_content.rb`: deterministic data/build checks.

---

### Task 1: Add a Failing Content-Provenance Gate

**Files:**
- Create: `scripts/verify_site_content.rb`
- Test: `_data/publications.yml`, `_data/news.yml`, `_site/index.html`

**Interfaces:**
- Consumes: YAML records from `_data` and rendered HTML from `_site`.
- Produces: exit code `0` with `content verification passed`, or exit code `1` with actionable violations.

- [ ] **Step 1: Write the verifier**

Create a Ruby script that loads YAML with `YAML.safe_load`, validates required publication fields, rejects malformed scraped titles, checks link schemes, and scans source/rendered files for demo identity:

```ruby
#!/usr/bin/env ruby
require "yaml"
require "pathname"

ROOT = Pathname.new(__dir__).join("..").expand_path
errors = []

publications = YAML.safe_load(
  ROOT.join("_data/publications.yml").read,
  permitted_classes: [],
  aliases: false
)

publications.each_with_index do |pub, index|
  label = "publication #{index + 1}"
  %w[title authors venue year].each do |key|
    errors << "#{label}: missing #{key}" if pub[key].to_s.strip.empty?
  end
  if pub["title"].match?(/\b(?:TDSC|TIFS)\s+20\d{2}\s+[A-Z][a-z]+\s+Li\b/)
    errors << "#{label}: title contains venue/authors: #{pub['title']}"
  end
  %w[url website code dataset weights].each do |key|
    value = pub[key].to_s
    next if value.empty? || value.match?(%r{\Ahttps?://})
    errors << "#{label}: invalid #{key} URL #{value}"
  end
end

scan_paths = Dir[
  ROOT.join("_config.yml"),
  ROOT.join("_pages/**/*"),
  ROOT.join("_data/**/*"),
  ROOT.join("_site/**/*.html")
].select { |path| File.file?(path) }

banned = [/Richard Feynman/i, /Caltech/i, /quantum electrodynamics/i]
scan_paths.each do |path|
  text = File.read(path, encoding: "UTF-8")
  banned.each { |pattern| errors << "#{path}: contains #{pattern.inspect}" if text.match?(pattern) }
end

abort(errors.join("\n")) unless errors.empty?
puts "content verification passed"
```

- [ ] **Step 2: Run the verifier and confirm it fails on current malformed records**

Run: `ruby scripts/verify_site_content.rb`

Expected: FAIL on the two records whose titles currently contain venue and author text (`Critical Information Only...` and `PromptGuard...`).

- [ ] **Step 3: Commit the failing gate**

```bash
git add scripts/verify_site_content.rb
git commit -m "test: add academic site content verification"
```

---

### Task 2: Normalize Verified Profile, News, and Publication Data

**Files:**
- Create: `_data/profile.yml`
- Modify: `_config.yml`
- Modify: `_data/news.yml`
- Modify: `_data/publications.yml`
- Modify: `_data/awards.yml`
- Modify: `_data/pi.yml`
- Test: `scripts/verify_site_content.rb`

**Interfaces:**
- Consumes: facts and links from the two approved source URLs.
- Produces: `site.data.profile`, `site.data.news`, and `site.data.publications` records used by every page.

- [ ] **Step 1: Add the normalized profile schema**

Create `_data/profile.yml` with these exact top-level keys:

```yaml
source: "https://letterligo.netlify.app/"
scholar: "https://scholar.google.com/citations?user=JC_UWyoAAAAJ&hl=en"
eyebrow: "AI Security & Trustworthy AI"
tagline: "Trustworthy AI, LLM/Agentic AI Security, AI for Security."
affiliation: "Department of Data Science and Artificial Intelligence, The Hong Kong Polytechnic University"
bio:
  - "I am an Assistant Professor in the Department of Data Science and Artificial Intelligence (DSAI) at The Hong Kong Polytechnic University (PolyU)."
  - "Previously, I was a Research Fellow in the College of Computing and Data Science at NTU, working with Prof. XiaoFeng Wang and Prof. Wei Dong. I completed my Ph.D. with honors at Zhejiang University, co-supervised by Prof. Wenyuan Xu, Prof. Xiaoyu Ji, and Prof. Chen Yan. I obtained my B.Eng. with honors from Zhejiang University."
  - "My research focuses on AI security and privacy, especially the security, privacy, and safety of multimodal LLMs & agentic AI systems. I study how to secure interactions between agentic AI systems and the real world. My goal is to help AI agents become robust and responsible partners."
research:
  - id: "agentic-ai-security"
    title: "Security and Privacy of Agentic AI Systems"
    description: "Building robust and responsible agentic AI systems and protecting their interactions with the physical and digital world."
    icon: "shield-halved"
  - id: "responsible-ai"
    title: "Responsible AI in Social Contexts"
    description: "Improving the safety, security, and privacy of multi-agent and human-agent interactions, as well as addressing risks in multimodal AIGC (e.g., deepfake generation and detection)."
    icon: "people-group"
  - id: "trustworthy-ai-for-x"
    title: "Trustworthy AI for X"
    description: "Enabling reliable AI deployment in healthcare, power grids, software engineering, IoT, and telecommunications systems."
    icon: "flask"
recruiting:
  headline: "We are recruiting"
  text: "PhDs for 27Fall, Postdocs, and research assistants/interns (remote/onsite). If you are seeking academic collaboration or are interested in joining my lab, please email me."
  note: "Due to the volume of inquiries, my apology if you don’t receive my reply."
```

- [ ] **Step 2: Align `_config.yml` with canonical links**

Keep the existing name, role, institution, `baseurl`, and deployment URL. Set the Google Scholar URL exactly to the approved Scholar URL, keep ResearchGate and both verified emails, and do not add an official lab name.

- [ ] **Step 3: Normalize news records**

Replace Markdown embedded in `headline` with plain source-backed text and optional links:

```yaml
- date: "2025.06"
  headline: "AudioTrust has been accepted to ICLR’26! We hope this can serve as a solid foundation for academia and industry for safe audio-based LLM system development."
  links:
    - label: "GitHub"
      url: "https://github.com/JusperLee/AudioTrust"
    - label: "Media"
      url: "https://mp.weixin.qq.com/s/gKifSw2iQs7VHLtjhGk-Tg"
```

Apply the same structure to every news item that has a source link; do not add links absent from the primary source.

- [ ] **Step 4: Repair malformed publication records and audit missing links**

Correct the two titles so venue and authors remain in their dedicated fields:

```yaml
- title: "Critical Information Only: A Content Privacy-Preserving Framework for Detecting Audio Deepfakes"
  authors: "Xinfeng Li, Yifan Zheng, Chen Yan, Kai Li, Chang Zeng, Xiaoyu Ji, Wenyuan Xu"
  venue: "TDSC 2026"
  year: 2026

- title: "PromptGuard: Soft Prompt-Guided Unsafe Content Moderation for Text-to-Image Models"
  authors: "Lingzhi Yuan, Xinfeng Li^, Chejian Xu, Guanhong Tao, Xiaojun Jia, Yihao Huang, Wei Dong, Yang Liu, Bo Li"
  venue: "TIFS 2026"
  year: 2026
```

Keep missing URLs absent. Compare the remaining title/author/venue/year fields with the primary page and the accessible Scholar record; never infer a URL from title similarity alone.

- [ ] **Step 5: Run the verifier**

Run: `ruby scripts/verify_site_content.rb`

Expected: PASS with `content verification passed`.

- [ ] **Step 6: Commit normalized content**

```bash
git add _config.yml _data/profile.yml _data/news.yml _data/publications.yml _data/awards.yml _data/pi.yml
git commit -m "data: normalize verified Xinfeng Li profile content"
```

---

### Task 3: Rebuild the Global Visual System and Navigation

**Files:**
- Modify: `_sass/base/_variables.scss`
- Modify: `_sass/base/_typography.scss`
- Modify: `_sass/base/_reset.scss`
- Modify: `_sass/components/_navbar.scss`
- Modify: `_sass/components/_footer.scss`
- Modify: `_sass/components/_buttons.scss`
- Modify: `_sass/components/_card.scss`
- Modify: `_sass/utilities/_dark-mode.scss`
- Modify: `_includes/header.html`
- Modify: `_includes/footer.html`
- Modify: `assets/main.scss`
- Test: `_site/index.html`

**Interfaces:**
- Consumes: `site.name`, `site.nav_pages`, verified links, and shared CSS variables.
- Produces: consistent global shell and reusable `.section-shell`, `.surface-card`, `.tag-chip`, and `.action-link` classes.

- [ ] **Step 1: Define the original reference-inspired tokens**

Use an original navy/violet system rather than copying PRLab CSS:

```scss
:root {
  --ink-950: #0d1733;
  --ink-700: #34415f;
  --ink-500: #68738d;
  --violet-600: #6246e5;
  --violet-100: #eeebff;
  --blue-500: #3977f6;
  --surface: #ffffff;
  --surface-soft: #f6f7fc;
  --line: #e2e6f0;
  --container-max: 1180px;
  --radius-card: 22px;
  --shadow-card: 0 18px 50px rgba(29, 40, 78, 0.08);
}
```

Retain literal colors in dark-mode rules with accessible contrast.

- [ ] **Step 2: Rebuild typography and global spacing**

Use the already configured web-font pair or a verified open-source equivalent. Set responsive headings with `clamp()`, body line-height between `1.65` and `1.8`, and a centered `1180px` content container.

- [ ] **Step 3: Rebuild header markup and mobile behavior hooks**

Keep Bootstrap collapse semantics, add a compact brand block (`Xinfeng Li` plus `AI Security @ PolyU`), retain Home/Research/Publications/News/Team, and preserve search/theme buttons with proper `aria-*` labels.

- [ ] **Step 4: Rebuild the footer from verified identity**

Render PolyU DSAI affiliation, both verified emails, Scholar, ResearchGate, and internal page links. Do not label the group with an invented lab name.

- [ ] **Step 5: Build CSS and Jekyll output**

Run:

```bash
npm run build
bundle exec jekyll build
```

Expected: both commands exit `0`; generated asset paths include `/web-Li/`.

- [ ] **Step 6: Commit the global visual shell**

```bash
git add _sass _includes/header.html _includes/footer.html assets/main.scss assets/js/site.min.js
git commit -m "style: rebuild academic site visual system"
```

---

### Task 4: Recompose the Homepage from Verified Data

**Files:**
- Modify: `_pages/home.html`
- Modify: `_includes/sidebar.html`
- Modify: `_sass/layouts/_home.scss`
- Modify: `_sass/components/_profile.scss`
- Modify: `_sass/components/_publication.scss`
- Test: `_site/index.html`

**Interfaces:**
- Consumes: `site.data.profile`, the first 8 news records, and the first 8 publication records.
- Produces: Home sections with stable anchors `about`, `research`, `news`, `publications`, and `openings`.

- [ ] **Step 1: Replace hardcoded biography and research copy with data loops**

Hero and section rendering must use:

```liquid
{% assign profile = site.data.profile %}
{% for paragraph in profile.bio %}
  <p>{{ paragraph }}</p>
{% endfor %}

{% for direction in profile.research %}
  <article class="research-card" id="{{ direction.id }}">
    <i class="fa-solid fa-{{ direction.icon }}" aria-hidden="true"></i>
    <h3>{{ direction.title }}</h3>
    <p>{{ direction.description }}</p>
  </article>
{% endfor %}
```

- [ ] **Step 2: Build the reference-inspired hero**

Create a two-column desktop hero with portrait/profile panel and a single-column mobile order. Include only verified role, affiliation, tagline, emails, Scholar, ResearchGate, Publications, and Join Us links.

- [ ] **Step 3: Rebuild news and publication cards**

Render explicit news link arrays and omit empty publication actions:

```liquid
{% for link in article.links %}
  <a href="{{ link.url }}" target="_blank" rel="noopener">{{ link.label }}</a>
{% endfor %}
```

- [ ] **Step 4: Rebuild recruiting callout**

Use `profile.recruiting.headline`, `text`, and `note`; render the two verified mailto actions.

- [ ] **Step 5: Build and verify rendered content**

Run:

```bash
npm run build
bundle exec jekyll build
ruby scripts/verify_site_content.rb
```

Expected: all commands exit `0`; `_site/index.html` contains the three verified research directions and no demo identity.

- [ ] **Step 6: Commit the homepage**

```bash
git add _pages/home.html _includes/sidebar.html _sass/layouts/_home.scss _sass/components/_profile.scss _sass/components/_publication.scss
git commit -m "feat: rebuild Xinfeng Li homepage"
```

---

### Task 5: Align Research, Publications, News, and Team Pages

**Files:**
- Modify: `_pages/research.html`
- Modify: `_pages/publications.html`
- Modify: `_pages/news.html`
- Modify: `_pages/team.html`
- Modify: `_layouts/gridlay.html`
- Modify: `_sass/layouts/_research.scss`
- Modify: `_sass/layouts/_team.scss`
- Modify: `_sass/components/_publication.scss`
- Test: `_site/research/index.html`
- Test: `_site/publications/index.html`
- Test: `_site/news/index.html`
- Test: `_site/team/index.html`

**Interfaces:**
- Consumes: the same normalized data used by Home.
- Produces: full list pages with no duplicate hardcoded factual copy.

- [ ] **Step 1: Render Research from `profile.research`**

Use the three source-backed directions only. Remove the unsourced sentence beginning `Representative themes in ongoing work include...` unless each theme is explicitly supported by the primary page.

- [ ] **Step 2: Group Publications by year**

Track year changes in Liquid and output headings:

```liquid
{% assign current_year = "" %}
{% for pub in site.data.publications %}
  {% capture pub_year %}{{ pub.year }}{% endcapture %}
  {% if pub_year != current_year %}
    <h2 class="publication-year">{{ pub_year }}</h2>
    {% assign current_year = pub_year %}
  {% endif %}
  {% include publication-card.html pub=pub %}
{% endfor %}
```

Create `_includes/publication-card.html` so Home and Publications share exactly one card renderer.

- [ ] **Step 3: Render full News with explicit links**

Use the normalized `links` array and ensure external links use `target="_blank" rel="noopener"`.

- [ ] **Step 4: Keep Team PI-only**

Render portrait, role, affiliation, verified education/career items, and recruiting copy. Use `Pending confirmation` only for a clearly labelled future member area if that area remains visible; otherwise omit the member grid completely.

- [ ] **Step 5: Build and run the content gate**

Run:

```bash
bundle exec jekyll build
ruby scripts/verify_site_content.rb
```

Expected: PASS; every listed page exists under `_site`.

- [ ] **Step 6: Commit content pages**

```bash
git add _pages _layouts/gridlay.html _includes/publication-card.html _sass/layouts _sass/components/_publication.scss
git commit -m "feat: align academic content pages"
```

---

### Task 6: Verify Responsive Interactions and Local Preview

**Files:**
- Modify: `assets/js/site.js`
- Modify: `_sass/components/_navbar.scss`
- Modify: `_sass/layouts/_home.scss`
- Create: `design-qa.md`
- Test: local pages at `http://localhost:4000/`

**Interfaces:**
- Consumes: fully built site.
- Produces: locally running preview and a QA record; no remote deployment.

- [ ] **Step 1: Rebuild JavaScript and static output**

Run:

```bash
npm run build
bundle exec jekyll build
ruby scripts/verify_site_content.rb
```

Expected: all commands exit `0`.

- [ ] **Step 2: Start the local site without the production base path**

Run:

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload --baseurl ""
```

Expected: Home loads at `http://localhost:4000/`.

- [ ] **Step 3: Inspect desktop at 1440×900**

Check hero hierarchy, portrait rendering, navigation, all five Home sections, publication actions, footer, and browser console. Record results in `design-qa.md`.

- [ ] **Step 4: Inspect mobile at 390×844**

Check menu open/close, card stacking, horizontal overflow, typography, touch targets, publication filter, and footer. Record results in `design-qa.md`.

- [ ] **Step 5: Test primary interactions**

Test Home navigation anchors, internal page links, search overlay, publication filtering, dark-mode toggle if retained, emails, Scholar, and ResearchGate. Do not claim unavailable external resources work.

- [ ] **Step 6: Fix all P0/P1/P2 QA issues and rerun checks**

Repeat Steps 1–5 until `design-qa.md` ends with:

```text
final result: passed
```

- [ ] **Step 7: Commit the verified local version**

```bash
git add assets/js/site.js assets/js/site.min.js _sass design-qa.md
git commit -m "fix: complete responsive academic site QA"
```

- [ ] **Step 8: Hand off the local preview**

Provide `http://localhost:4000/` for review. Do not push `main` and do not deploy GitHub Pages until the user explicitly approves the local result.
